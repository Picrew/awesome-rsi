"""Offline regression tests for catalog integrity and fail-closed sync."""
import copy
import datetime as dt
import re
import sys
import unittest
import urllib.error
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from render_readme import load_catalog, render_readmes, escape_md, is_github
from sync_github_metadata import metadata_fields, repo_slug, sync_catalog
from verify_catalog import check_url, validate_catalog

TODAY = dt.date(2026, 9, 8)


class CatalogTests(unittest.TestCase):
    def setUp(self):
        self.data = load_catalog()
        self.today = dt.date.fromisoformat(self.data["catalog"]["last_verified"])
        self.entry = next(e for e in self.data["entries"] if e["kind"] == "project")

    def errors(self):
        return "\n".join(validate_catalog(self.data, self.today))

    def test_current_catalog(self):
        self.assertEqual(validate_catalog(self.data, self.today), [])

    def test_missing_mechanism(self):
        del self.entry["rsi_mechanism"]["persistence"]
        self.assertIn("mechanism needs", self.errors())

    def test_archived_and_private_rejected(self):
        for flag in ("archived", "private"):
            self.entry[flag] = True
            self.assertIn(f"{flag} must be verified false", self.errors())
            self.entry[flag] = False

    def test_missing_state_is_not_public(self):
        del self.entry["archived"]
        self.assertIn("archived must be verified false", self.errors())

    def test_activity_boundary_inclusive(self):
        cutoff = self.today - dt.timedelta(days=60)
        self.entry["updated_at"] = cutoff.isoformat()
        self.entry["pushed_at"] = cutoff.isoformat() + "T00:00:00Z"
        self.assertNotIn("activity window", self.errors())
        stale = cutoff - dt.timedelta(days=1)
        self.entry["updated_at"] = stale.isoformat()
        self.entry["pushed_at"] = stale.isoformat() + "T23:59:59Z"
        self.assertIn("outside 60-day", self.errors())

    def test_social_update_cannot_hide_old_push(self):
        self.entry["updated_at"] = self.today.isoformat()
        self.entry["pushed_at"] = "2025-01-01T00:00:00Z"
        self.assertIn("does not match pushed_at", self.errors())
        self.assertIn("outside 60-day", self.errors())

    def test_missing_push_rejected(self):
        del self.entry["pushed_at"]
        self.assertIn("invalid/missing pushed_at", self.errors())

    def test_future_dates(self):
        self.entry["reviewed_at"] = (self.today + dt.timedelta(days=1)).isoformat()
        self.assertIn("future reviewed_at", self.errors())

    def test_duplicate_summaries_rejected(self):
        self.data["entries"][1]["summary_zh"] = self.entry["summary_zh"]
        self.assertIn("Duplicate summary_zh", self.errors())

    def test_placeholder_rejected(self):
        self.entry["summary_zh"] = "用于可度量递归自我改进与能力增长的开源模型或训练组件。"
        self.assertIn("generic RSI placeholder", self.errors())

    def test_invalid_types(self):
        self.entry["stars_snapshot"] = True
        self.entry["tags"] = "agent"
        self.entry["rsi_mechanism"] = "some loop"
        self.assertIn("invalid stars_snapshot", self.errors())
        self.assertIn("invalid tags", self.errors())
        self.assertIn("mechanism needs", self.errors())

    def test_github_hostname_spoof_rejected(self):
        self.entry["repo_url"] = "https://github.com.evil.example/owner/repo"
        self.assertIn("canonical GitHub", self.errors())
        self.assertFalse(is_github("https://example.com/github.com/owner/repo"))
        with self.assertRaises(ValueError):
            repo_slug("https://github.com.evil.example/owner/repo")

    def test_no_fake_reading_escape(self):
        self.entry["kind"] = "reading"
        self.assertIn("reading must use reading category", self.errors())
        self.assertIn("first-party research domain", self.errors())

    def test_empty_category_rejected(self):
        category = copy.deepcopy(self.data["categories"][0])
        category.update(id="empty", anchor="empty", name_en="Models / Empty")
        self.data["categories"].append(category)
        self.assertIn("Empty category", self.errors())

    def test_mirrors_share_order_and_anchors(self):
        en, zh = render_readmes(self.data)
        project_pattern = r"\[GitHub\]\(([^)]+)\)"
        self.assertEqual(re.findall(project_pattern, en), re.findall(project_pattern, zh))
        for text in (en, zh):
            self.assertNotIn('<a id=', text)
            self.assertNotIn("```bibtex", text)
            headings = re.findall(r"^#{2,3} (.+)$", text, re.M)
            slugs = {re.sub(r"[^\w\- ]", "", h.lower()).replace(" ", "-") for h in headings}
            for target in re.findall(r"\]\(#([^)]*)\)", text):
                self.assertIn(target, slugs)
        self.assertEqual((en, zh), render_readmes(self.data))

    def test_blogs_first_and_every_resource_rendered(self):
        for text in render_readmes(self.data):
            self.assertLess(text.index("## Company Research Blogs"), text.index("## Papers and Official Code"))
            self.assertLess(text.index("## Papers and Official Code"), text.index("## Active GitHub Projects"))
            self.assertNotIn("| Blog |", text)
            for entry in self.data["entries"]:
                self.assertIn(entry["repo_url"], text)

    def test_paper_code_adjacent_to_paper(self):
        paper = next(e for e in self.data["entries"] if e["kind"] == "paper" and e.get("code_url"))
        for text in render_readmes(self.data):
            row = next(line for line in text.splitlines() if f"]({paper['repo_url']})" in line)
            self.assertIn(paper["code_url"], row)
            self.assertGreater(row.index(paper["code_url"]), row.index(paper["repo_url"]))

    def test_historical_paper_code_is_allowed(self):
        paper = next(e for e in self.data["entries"] if e.get("code_metadata"))
        paper["code_metadata"].update(archived=True, pushed_at="2020-01-01T00:00:00Z", updated_at="2020-01-01")
        self.assertEqual(self.errors(), "")
        self.assertIn("archived; push 2020-01-01", render_readmes(self.data)[0])

    def test_official_code_needs_linkage(self):
        paper = next(e for e in self.data["entries"] if e.get("code_url"))
        del paper["code_evidence_excerpt"]
        self.assertIn("code requires linkage evidence", self.errors())

    def test_venue_needs_source(self):
        paper = next(e for e in self.data["entries"] if e["kind"] == "paper" and e.get("venue"))
        del paper["venue_evidence_url"]
        self.assertIn("venue claim lacks evidence", self.errors())

    def test_unknown_blog_date_needs_note(self):
        blog = next(e for e in self.data["entries"] if e["kind"] == "reading")
        blog["published_at"] = None
        blog.pop("date_note", None)
        self.assertIn("missing publication date", self.errors())
        blog["date_note"] = "No original date visible"
        self.assertNotIn("missing publication date", self.errors())

    def test_same_name_across_resource_kinds_allowed(self):
        paper = next(e for e in self.data["entries"] if e["kind"] == "paper")
        paper["name"] = self.entry["name"]
        self.assertNotIn("Duplicate name", self.errors())

    def test_not_found_cannot_claim_code_url(self):
        paper = next(e for e in self.data["entries"] if e.get("code_url"))
        paper["code_status"] = "not-found"
        self.assertIn("not-found code cannot have a URL", self.errors())

    def test_markdown_table_escape(self):
        self.assertEqual(escape_md("a|b\nc"), "a\\|b c")

    def test_source_fields_required_for_rendering(self):
        del self.entry["summary_zh"]
        with self.assertRaises(ValueError):
            render_readmes(self.data)


class SyncTests(unittest.TestCase):
    def payload(self, slug="owner/repo"):
        return dict(full_name=slug, html_url="https://github.com/" + slug,
                    stargazers_count=100, pushed_at="2026-09-08T01:00:00Z",
                    archived=False, private=False, license={"spdx_id": "MIT"})

    def test_metadata_never_uses_social_updated_date(self):
        payload = self.payload()
        del payload["pushed_at"]
        payload["updated_at"] = "2026-09-08T01:00:00Z"
        with self.assertRaises(ValueError):
            metadata_fields(payload, TODAY)

    def test_archived_metadata_fails(self):
        payload = self.payload()
        payload["archived"] = True
        with self.assertRaises(ValueError):
            metadata_fields(payload, TODAY)

    def test_paper_and_project_share_one_request(self):
        entries = [dict(kind="project", name="repo", repo_url="https://github.com/owner/repo"),
                   dict(kind="paper", name="paper", repo_url="https://arxiv.org/abs/1234.56789",
                        code_url="https://github.com/owner/repo", published_at="2020-01-01")]
        calls = []
        def fetch(slug):
            calls.append(slug)
            return self.payload(slug)
        sync_catalog(dict(catalog={}, entries=entries), fetch, TODAY)
        self.assertEqual(calls, ["owner/repo"])
        self.assertEqual(entries[1]["published_at"], "2020-01-01")
        self.assertEqual(entries[1]["repo_url"], "https://arxiv.org/abs/1234.56789")
        self.assertEqual(entries[1]["code_metadata"]["stars_snapshot"], 100)

    def test_archived_paper_code_can_sync(self):
        entry = dict(kind="paper", name="paper", code_url="https://github.com/owner/repo")
        payload = self.payload()
        payload["archived"] = True
        sync_catalog(dict(catalog={}, entries=[entry]), lambda slug: payload, TODAY)
        self.assertTrue(entry["code_metadata"]["archived"])

    def test_partial_failure_is_atomic(self):
        data = {"catalog": {"last_verified": "2020-01-01"}, "entries": [
            {"name": "one", "kind": "project", "repo_url": "https://github.com/owner/one"},
            {"name": "two", "kind": "project", "repo_url": "https://github.com/owner/two"}]}
        original = copy.deepcopy(data)
        def fetch(slug):
            if slug.endswith("two"):
                raise OSError("network unavailable")
            return self.payload(slug)
        with self.assertRaisesRegex(ValueError, "no catalog changes"):
            sync_catalog(data, fetch, TODAY)
        self.assertEqual(data, original)

    def test_sync_preserves_manual_evidence_and_article_dates(self):
        data = {"catalog": {"last_verified": "2020-01-01"}, "entries": [
            {"name": "one", "kind": "project", "repo_url": "https://github.com/owner/repo",
             "summary_en": "curated", "evidence_excerpt": "source", "reviewed_at": "2025-01-01"},
            {"name": "reading", "kind": "reading", "updated_at": "2018-01-01"}]}
        sync_catalog(data, lambda slug: self.payload(slug), TODAY)
        self.assertEqual(data["entries"][0]["summary_en"], "curated")
        self.assertEqual(data["entries"][0]["reviewed_at"], "2025-01-01")
        self.assertEqual(data["entries"][1]["updated_at"], "2018-01-01")
        self.assertEqual(data["catalog"]["last_verified"], TODAY.isoformat())


class LinkTests(unittest.TestCase):
    def test_403_challenge_is_not_success(self):
        error = urllib.error.HTTPError("https://example.com", 403, "challenge",
                                       {"cf-mitigated": "challenge"}, None)
        with patch("verify_catalog.urllib.request.urlopen", side_effect=error):
            self.assertEqual(check_url("https://example.com")[1], "unverified")

    def test_404_is_broken(self):
        error = urllib.error.HTTPError("https://example.com", 404, "missing", {}, None)
        with patch("verify_catalog.urllib.request.urlopen", side_effect=error):
            self.assertEqual(check_url("https://example.com")[1], "broken")

    def test_429_is_unverified(self):
        error = urllib.error.HTTPError("https://example.com", 429, "rate limited", {}, None)
        with patch("verify_catalog.urllib.request.urlopen", side_effect=error):
            self.assertEqual(check_url("https://example.com")[1], "unverified")


if __name__ == "__main__":
    unittest.main()
