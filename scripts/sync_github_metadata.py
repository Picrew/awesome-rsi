#!/usr/bin/env python3
"""Refresh GitHub-only metadata atomically; never overwrite curated evidence."""
from __future__ import annotations

import datetime as dt
import json
import os
import subprocess
import time
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from urllib.parse import urlparse

import yaml

ROOT = Path(__file__).resolve().parents[1]
DATA_FILE = ROOT / "data" / "projects.yaml"


def get_token():
    if os.getenv("GITHUB_TOKEN"):
        return os.environ["GITHUB_TOKEN"]
    try:
        return subprocess.check_output(["gh", "auth", "token"], text=True,
                                       stderr=subprocess.DEVNULL, timeout=10).strip() or None
    except (OSError, subprocess.SubprocessError):
        return None


def repo_slug(url):
    parsed = urlparse(url)
    parts = parsed.path.strip("/").split("/")
    if parsed.scheme != "https" or parsed.hostname != "github.com" or len(parts) != 2:
        raise ValueError(f"Expected canonical GitHub repository URL: {url}")
    return "/".join(parts).removesuffix(".git")


def fetch_repo(slug, token):
    headers = {"Accept": "application/vnd.github+json", "User-Agent": "awesome-rsi-sync"}
    if token:
        headers["Authorization"] = f"Bearer {token}"
    for attempt in range(3):
        try:
            request = urllib.request.Request(f"https://api.github.com/repos/{slug}", headers=headers)
            with urllib.request.urlopen(request, timeout=25) as response:
                return json.load(response)
        except Exception:
            if attempt == 2:
                raise
            time.sleep(0.5 * (attempt + 1))


def metadata_fields(payload, today, require_active_project=True):
    for key in ("full_name", "stargazers_count", "pushed_at", "archived", "private", "html_url"):
        if key not in payload or payload[key] is None:
            raise ValueError(f"Incomplete GitHub response: missing {key}")
    if type(payload["archived"]) is not bool or type(payload["private"]) is not bool:
        raise ValueError("Invalid repository state")
    if payload["private"] or (require_active_project and payload["archived"]):
        raise ValueError(f"Repository must be public and non-archived for active projects: {payload['full_name']}")
    stars = payload["stargazers_count"]
    if type(stars) is not int or stars < 0:
        raise ValueError("Invalid star count")
    pushed = payload["pushed_at"]
    date = dt.datetime.fromisoformat(pushed.replace("Z", "+00:00")).date()
    if date > today:
        raise ValueError("Future pushed_at")
    return {
        "repo_url": payload["html_url"], "stars_snapshot": stars,
        "updated_at": date.isoformat(), "pushed_at": pushed,
        "archived": payload["archived"], "private": payload["private"],
        "license": (payload.get("license") or {}).get("spdx_id") or "none",
        "metadata_checked_at": today.isoformat(),
        "metadata_source": f"https://api.github.com/repos/{payload['full_name']}",
    }


def sync_catalog(catalog, fetcher, today):
    references = {}
    for entry in catalog["entries"]:
        url = entry["repo_url"] if entry["kind"] == "project" else entry.get("code_url")
        if url:
            references.setdefault(repo_slug(url).lower(), []).append(entry)
    updates, errors = [], []
    with ThreadPoolExecutor(max_workers=4) as pool:
        jobs = {pool.submit(fetcher, slug): related for slug, related in references.items()}
        for future in as_completed(jobs):
            related = jobs[future]
            try:
                fields = metadata_fields(future.result(), today,
                    require_active_project=any(e["kind"] == "project" for e in related))
                updates.append((related, fields))
            except Exception as exc:
                errors.append(f"{related[0]['name']}: {exc}")
    if errors:
        raise ValueError("Metadata sync failed; no catalog changes saved:\n" + "\n".join(sorted(errors)))
    for related, fields in updates:
        for entry in related:
            if entry["kind"] == "project":
                entry.update(fields)
                if dt.date.fromisoformat(entry["updated_at"]) < today - dt.timedelta(days=60):
                    print(f"STALE: {entry['name']} pushed {entry['updated_at']}; catalog verification will reject it")
            else:
                entry["code_url"] = fields["repo_url"]
                entry["code_metadata"] = dict(fields)
    catalog["catalog"]["last_verified"] = today.isoformat()
    return len(updates)


def main():
    catalog = yaml.safe_load(DATA_FILE.read_text(encoding="utf-8"))
    token = get_token()
    count = sync_catalog(catalog, lambda slug: fetch_repo(slug, token), dt.datetime.now(dt.timezone.utc).date())
    text = yaml.safe_dump(catalog, allow_unicode=True, sort_keys=False, width=120)
    temporary = DATA_FILE.with_suffix(".yaml.tmp")
    try:
        temporary.write_text(text, encoding="utf-8")
        temporary.replace(DATA_FILE)
    finally:
        temporary.unlink(missing_ok=True)
    print(f"GitHub metadata refreshed: {count}/{count}. Curated descriptions/evidence unchanged.")


if __name__ == "__main__":
    main()
