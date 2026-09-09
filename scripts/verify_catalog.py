#!/usr/bin/env python3
"""Validate evidence contracts, active metadata, mirrored output and source links."""
from __future__ import annotations

import argparse
import datetime as dt
import re
import urllib.error
import urllib.request
from collections import Counter
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from urllib.parse import urlparse

from render_readme import (DATA_FILE, README_EN, README_ZH, REQUIRED_ENTRY_FIELDS,
                           SCOPE_LABELS, is_github, load_catalog, render_readmes)

ROOT = Path(__file__).resolve().parents[1]
REPORT_DIR = ROOT / "reports" / "verification"
ACTIVITY_DAYS = 60
PRIMARY_HOSTS = {"sakana.ai", "deepmind.google", "www.anthropic.com", "anthropic.com",
                 "openai.com", "developers.openai.com", "ai.meta.com", "research.google", "nousresearch.com",
                 "www.primeintellect.ai", "primeintellect.ai", "www.minimax.io", "minimax.io",
                 "moonshotai.github.io", "www.kimi.com", "kimi.com", "www.microsoft.com", "microsoft.com"}
PAPER_HOSTS = {"arxiv.org", "www.nature.com", "nature.com", "openreview.net", "proceedings.neurips.cc",
               "proceedings.mlr.press", "aclanthology.org", "dl.acm.org"}
PLACEHOLDERS = ("用于可度量递归自我改进与能力增长", "Open-source model and training component",
                "用于研究能力增长与递归自我改进", "Public, non-archived GitHub project with substantial adoption")


def iso_date(value):
    if not isinstance(value, str):
        raise ValueError("Dates must be quoted ISO strings")
    return dt.date.fromisoformat(value)


def validate_catalog(catalog, today=None):
    today = today or dt.datetime.now(dt.timezone.utc).date()
    errors = []
    if not isinstance(catalog, dict):
        return ["Catalog must be a mapping"]
    meta, categories, entries = (catalog.get(k) for k in ("catalog", "categories", "entries"))
    if not isinstance(meta, dict) or not isinstance(categories, list) or not isinstance(entries, list):
        return ["Invalid catalog/categories/entries types"]
    if not entries:
        errors.append("Catalog has no entries; no arbitrary entry quota is imposed")
    names, ids, anchors, groups = [], [], [], []
    for c in categories:
        if not isinstance(c, dict) or not all(isinstance(c.get(k), str) and c[k].strip()
                    for k in ("id", "anchor", "group", "name_en", "name_zh", "description_en", "description_zh")):
            errors.append("Invalid category contract")
            continue
        names.append(c["name_en"])
        ids.append(c["id"])
        anchors.append(c["anchor"])
        groups.append(c["group"])
        if c["group"] not in {"Models", "Harness", "Artifacts", "Readings", "Papers"}:
            errors.append(f"Invalid group: {c['group']}")
    if not {"Models", "Harness", "Artifacts"}.issubset(groups):
        errors.append("Models, Harness and Artifacts groups are required")
    for label, values in (("category names", names), ("category ids", ids), ("anchors", anchors)):
        if len(values) != len(set(values)):
            errors.append(f"Duplicate {label}")
    for key in ("title_en", "title_zh", "description_en", "description_zh", "scope_en", "scope_zh"):
        if not isinstance(meta.get(key), str) or not meta[key].strip():
            errors.append(f"Missing catalog text: {key}")
    try:
        snapshot = iso_date(meta.get("last_verified"))
        if snapshot > today or (today - snapshot).days > 7:
            errors.append("Metadata snapshot must be within the past 7 days")
    except (ValueError, TypeError):
        errors.append("Invalid catalog last_verified")
        snapshot = None
    for index, e in enumerate(entries):
        if not isinstance(e, dict):
            errors.append(f"entry[{index}] must be a mapping")
            continue
        name = e.get("name", f"entry[{index}]")
        missing = [k for k in REQUIRED_ENTRY_FIELDS if k not in e]
        if missing:
            errors.append(f"{name}: missing {missing}")
        for field in ("name", "summary_en", "summary_zh", "why_included", "limitation_en", "limitation_zh", "evidence_excerpt"):
            if not isinstance(e.get(field), str) or not e[field].strip():
                errors.append(f"{name}: empty/invalid {field}")
        if not re.search(r"[\u4e00-\u9fff]", str(e.get("summary_zh", ""))):
            errors.append(f"{name}: Chinese summary missing")
        if e.get("summary_en") == e.get("summary_zh"):
            errors.append(f"{name}: untranslated summary")
        if any(p in str(e.get("summary_en", "")) + str(e.get("summary_zh", "")) + str(e.get("why_included", "")) for p in PLACEHOLDERS):
            errors.append(f"{name}: generic RSI placeholder")
        if e.get("category") not in names:
            errors.append(f"{name}: unknown category")
        if e.get("scope") not in SCOPE_LABELS:
            errors.append(f"{name}: invalid improvement scope")
        tags = e.get("tags")
        if not isinstance(tags, list) or not tags or not all(isinstance(t, str) and t for t in tags):
            errors.append(f"{name}: invalid tags")
        if type(e.get("stars_snapshot")) is not int or e.get("stars_snapshot", -1) < 0:
            errors.append(f"{name}: invalid stars_snapshot")
        mechanism = e.get("rsi_mechanism")
        if not isinstance(mechanism, dict) or not all(isinstance(mechanism.get(k), str) and mechanism[k].strip()
                                                    for k in ("target", "feedback", "update", "persistence")):
            errors.append(f"{name}: mechanism needs target, feedback, update, persistence")
        url_fields = ("repo_url", "evidence_url", "code_url", "code_subdirectory_url", "code_evidence_url", "venue_evidence_url", "date_evidence_url")
        for field in url_fields:
            if field not in {"repo_url", "evidence_url"} and not e.get(field):
                continue
            url = urlparse(str(e.get(field, "")))
            if url.scheme != "https" or not url.hostname or url.username:
                errors.append(f"{name}: invalid {field}")
        for field in ("updated_at", "reviewed_at"):
            try:
                date = iso_date(e.get(field))
                if date > today:
                    errors.append(f"{name}: future {field}")
            except (ValueError, TypeError):
                errors.append(f"{name}: invalid {field}")
        if e.get("kind") == "project":
            parsed = urlparse(str(e.get("repo_url", "")))
            if not is_github(e.get("repo_url", "")) or len(parsed.path.strip("/").split("/")) != 2:
                errors.append(f"{name}: project must have a canonical GitHub repository URL")
            if str(e.get("category", "")).startswith("Essential"):
                errors.append(f"{name}: project cannot masquerade as a reading")
            for flag in ("archived", "private"):
                if e.get(flag) is not False:
                    errors.append(f"{name}: {flag} must be verified false")
            try:
                pushed = dt.datetime.fromisoformat(e["pushed_at"].replace("Z", "+00:00"))
                if pushed.tzinfo is None:
                    raise ValueError("Missing timezone")
                date = pushed.astimezone(dt.timezone.utc).date()
                if date.isoformat() != e.get("updated_at"):
                    errors.append(f"{name}: updated_at does not match pushed_at")
                if date < today - dt.timedelta(days=ACTIVITY_DAYS) or date > today:
                    errors.append(f"{name}: outside {ACTIVITY_DAYS}-day activity window ({date})")
            except (ValueError, TypeError, KeyError, AttributeError):
                errors.append(f"{name}: invalid/missing pushed_at")
            try:
                checked = iso_date(e.get("metadata_checked_at"))
                if checked != snapshot:
                    errors.append(f"{name}: metadata check date differs from snapshot")
            except (ValueError, TypeError):
                errors.append(f"{name}: missing metadata check date")
            expected = "https://api.github.com/repos/" + parsed.path.strip("/")
            if str(e.get("metadata_source", "")).lower() != expected.lower():
                errors.append(f"{name}: missing canonical metadata source")
        elif e.get("kind") in {"reading", "paper"}:
            paper = e["kind"] == "paper"
            prefix = "Papers /" if paper else "Essential"
            if not str(e.get("category", "")).startswith(prefix):
                errors.append(f"{name}: {'paper' if paper else 'reading'} must use {'paper' if paper else 'reading'} category")
            hosts = PAPER_HOSTS if paper else PRIMARY_HOSTS
            if urlparse(e.get("repo_url", "")).hostname not in hosts:
                errors.append(f"{name}: {'paper must use a reviewed research source' if paper else 'reading must use a reviewed first-party research domain'}")
            if e.get("improvement_target") not in {"Models", "Harness", "Artifacts"}:
                errors.append(f"{name}: missing improvement target")
            if not paper and not e.get("publisher"):
                errors.append(f"{name}: missing publisher")
            if not paper and e.get("blog_section") not in {"mechanisms", "safety", "agenda", "foundations"}:
                errors.append(f"{name}: missing blog section")
            try:
                if e.get("published_at") is None and not paper and e.get("date_note"):
                    pass
                elif iso_date(e.get("published_at")) > today:
                    errors.append(f"{name}: future publication date")
            except (ValueError, TypeError):
                errors.append(f"{name}: missing publication date")
            if paper:
                if e.get("publication_status") not in {"published", "preprint"}:
                    errors.append(f"{name}: invalid publication status")
                if e.get("venue") and (not e.get("venue_evidence_url") or not e.get("venue_evidence_excerpt")):
                    errors.append(f"{name}: venue claim lacks evidence")
                if e.get("publication_status") == "published" and not e.get("venue"):
                    errors.append(f"{name}: published status requires a verified venue")
                status, code = e.get("code_status"), e.get("code_url")
                if status not in {"official", "not-found", "third-party"}:
                    errors.append(f"{name}: invalid code status")
                if status == "not-found" and code:
                    errors.append(f"{name}: not-found code cannot have a URL")
                if status in {"official", "third-party"}:
                    if not code or not is_github(code) or len(urlparse(code).path.strip('/').split('/')) != 2:
                        errors.append(f"{name}: code must have a canonical GitHub URL")
                    if not e.get("code_evidence_url") or not e.get("code_evidence_excerpt"):
                        errors.append(f"{name}: official/reproduction code requires linkage evidence")
                    if e.get("code_release") not in {"implementation", "artifacts-only"}:
                        errors.append(f"{name}: code release completeness must be explicit")
                    cm = e.get("code_metadata")
                    if not isinstance(cm, dict):
                        errors.append(f"{name}: missing code metadata")
                    else:
                        if cm.get("private") is not False or type(cm.get("archived")) is not bool:
                            errors.append(f"{name}: unverified code public/archive state")
                        if cm.get("metadata_checked_at") != meta.get("last_verified"):
                            errors.append(f"{name}: code metadata snapshot mismatch")
                        if cm.get("repo_url") != code:
                            errors.append(f"{name}: canonical code URL mismatch")
                        try:
                            pushed = dt.datetime.fromisoformat(cm["pushed_at"].replace('Z', '+00:00')).date()
                            if pushed > today or pushed.isoformat() != cm.get("updated_at"):
                                errors.append(f"{name}: invalid code push date")
                        except (KeyError, ValueError, TypeError, AttributeError):
                            errors.append(f"{name}: missing code push timestamp")
                elif not e.get("code_search_note"):
                    errors.append(f"{name}: document sources checked for missing code")
        else:
            errors.append(f"{name}: invalid entry kind")
    for field in ("name", "repo_url", "summary_en", "summary_zh"):
        values = [((e.get("kind", "") + ":") if field == "name" else "") + str(e.get(field, "")).strip().rstrip("/").lower()
                  for e in entries if isinstance(e, dict)]
        duplicates = [v for v, n in Counter(values).items() if v and n > 1]
        if duplicates:
            errors.append(f"Duplicate {field}: {duplicates}")
    counts = Counter(e.get("category") for e in entries if isinstance(e, dict))
    for name in names:
        if not counts[name]:
            errors.append(f"Empty category: {name}")
    return errors


def check_url(url, timeout=20):
    """403/429 are unverified, never reported as successful content checks."""
    last = "No response"
    for method in ("HEAD", "GET"):
        try:
            request = urllib.request.Request(url, method=method,
                                            headers={"User-Agent": "awesome-rsi-verify"})
            with urllib.request.urlopen(request, timeout=timeout) as response:
                if 200 <= response.status < 300:
                    return url, "reachable", f"{method} {response.status}"
                last = f"{method} {response.status}"
        except urllib.error.HTTPError as exc:
            last = f"HTTP {exc.code}"
            if exc.code in (403, 429):
                if method == "GET":
                    return url, "unverified", last
            elif method == "GET":
                return url, "broken", last
        except Exception as exc:
            last = str(exc)
    return url, "unverified", last


def gather_links(catalog):
    fields = ("repo_url", "evidence_url", "code_url", "code_evidence_url", "venue_evidence_url", "date_evidence_url")
    return sorted({e[k] for e in catalog["entries"] for k in fields if e.get(k)})


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--skip-links", action="store_true", help="Offline check; does not certify link health")
    args = parser.parse_args()
    catalog = load_catalog()
    errors = validate_catalog(catalog)
    try:
        rendered = render_readmes(catalog)
        for path, text in zip((README_EN, README_ZH), rendered):
            if not path.exists() or path.read_text(encoding="utf-8") != text:
                errors.append(f"{path.name} is out of sync")
            if '<a id=' in text or "```bibtex" in text:
                errors.append(f"{path.name}: raw anchors or invented citation")
    except (ValueError, KeyError, TypeError) as exc:
        errors.append(f"Rendering contract failed: {exc}")
    results = []
    if not args.skip_links and not errors:
        with ThreadPoolExecutor(max_workers=8) as pool:
            results = list(pool.map(check_url, gather_links(catalog)))
        for url, status, detail in results:
            if status != "reachable":
                errors.append(f"Link {status}: {detail} {url}")
    projects = [e for e in catalog["entries"] if e.get("kind") == "project"]
    date = dt.datetime.now(dt.timezone.utc).date().isoformat()
    report = ["# Verification Report", "", f"- Generated at: {dt.datetime.now(dt.timezone.utc).isoformat()}",
              f"- Active project entries: {len(projects)}", f"- First-party blogs: {sum(e.get('kind') == 'reading' for e in catalog['entries'])}",
              f"- Research papers: {sum(e.get('kind') == 'paper' for e in catalog['entries'])}",
              f"- Activity window: {ACTIVITY_DAYS} days, inclusive UTC calendar dates; based on pushed_at",
              f"- Link checks: {'SKIPPED (offline only)' if args.skip_links else len(results)}",
              "- Automated checks validate structure and reachability, not scientific truth or benchmark reproduction.",
              "", "## Errors", ""]
    report += [f"- {e}" for e in errors] or ["- None"]
    report += ["", "## Links", "", "| URL | Status | Detail |", "| --- | --- | --- |"]
    report += [f"| {u} | {s} | {d.replace('|', '/')} |" for u, s, d in sorted(results)]
    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    suffix = "-offline" if args.skip_links else ""
    path = REPORT_DIR / f"{date}{suffix}.md"
    path.write_text("\n".join(report) + "\n", encoding="utf-8")
    print(f"Wrote report: {path}")
    if errors:
        raise SystemExit("Verification failed:\n" + "\n".join(errors))
    print("Verification passed." + (" Link checks skipped." if args.skip_links else " All source links reachable."))


if __name__ == "__main__":
    main()
