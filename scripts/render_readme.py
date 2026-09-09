#!/usr/bin/env python3
"""Generate blog-first mirrored Markdown from one evidence-led catalog."""
from __future__ import annotations

import argparse
from collections import OrderedDict
from pathlib import Path
from typing import Any
from urllib.parse import urlparse

import yaml

ROOT = Path(__file__).resolve().parents[1]
DATA_FILE = ROOT / "data" / "projects.yaml"
README_EN = ROOT / "README.md"
README_ZH = ROOT / "README_zh.md"
READINGS_CATEGORY = "Essential Readings / Primary Research"
REQUIRED_ENTRY_FIELDS = [
    "name", "repo_url", "category", "summary_en", "summary_zh", "tags",
    "stars_snapshot", "updated_at", "why_included", "kind", "scope",
    "rsi_mechanism", "evidence_url", "evidence_excerpt", "reviewed_at",
    "limitation_en", "limitation_zh",
]
SCOPE_LABELS = {
    "self-modification": ("Self-modification", "直接自修改"),
    "self-training": ("Self-training", "自训练"),
    "bounded-optimization": ("Bounded optimization", "有界优化"),
    "experience-learning": ("Experience learning", "经验学习"),
    "inference-refinement": ("Within-task refinement", "任务内修订"),
    "safety-evaluation": ("Evaluation / safety", "评测与安全"),
    "research-agenda": ("Research agenda", "研究路线"),
}
BLOG_SECTIONS = OrderedDict([
    ("mechanisms", ("Mechanisms and Results", "机制与实证结果")),
    ("safety", ("Evaluation and Failure Modes", "评测与失败模式")),
    ("agenda", ("Research Agendas", "研究路线")),
    ("foundations", ("Foundations and Historical Tutorials", "奠基研究与历史教程")),
])


def is_github(url: str) -> bool:
    return urlparse(url).hostname == "github.com"


def load_catalog(path: Path = DATA_FILE) -> dict[str, Any]:
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError("Catalog must be a mapping")
    return data


def escape_md(text: Any) -> str:
    return str(text).replace("|", "\\|").replace("\n", " ").strip()


def github_ratio(entries: list[dict[str, Any]]) -> tuple[int, int, float]:
    total = len(entries)
    count = sum(is_github(str(e.get("repo_url", ""))) for e in entries)
    return count, total, count / total * 100 if total else 0.0


def sorted_entries(entries, categories):
    return OrderedDict(
        (c["name_en"], sorted(
            [e for e in entries if e["category"] == c["name_en"]],
            key=lambda e: (-e["stars_snapshot"], e["name"].lower()),
        )) for c in categories
    )


def validate_contract(catalog: dict[str, Any]) -> None:
    if not all(k in catalog for k in ("catalog", "categories", "entries")):
        raise ValueError("Catalog must contain catalog, categories, entries")
    for entry in catalog["entries"]:
        missing = [k for k in REQUIRED_ENTRY_FIELDS if k not in entry]
        if missing:
            raise ValueError(f"{entry.get('name', '<unnamed>')}: missing {missing}")


def table_row(cells):
    return "| " + " | ".join(escape_md(cell) for cell in cells) + " |"


def heading_slug(text):
    import re
    return re.sub(r"[^\w\- ]", "", text.lower()).replace(" ", "-")


def star_badge(url, stars):
    """Use the same snapshot badge style as awesome-agent-harness."""
    return f"[![star: {stars:,}](https://img.shields.io/badge/star-{stars}-f4b400?style=flat-square)]({url})"


def cell_list(items):
    """Keep list items on separate lines inside GitHub Markdown tables."""
    return "<br>".join(f"• {item}" for item in items if item)


def paper_code_cell(entry, zh=False):
    label = lambda en, cn: cn if zh else en
    url = entry.get("code_url")
    status = entry.get("code_status")
    if not url:
        return label("Not found in reviewed sources", "已审查来源未找到")
    title = label("Official code", "官方代码") if status == "official" else label("Third-party reproduction", "第三方复现")
    if entry.get("code_release") == "artifacts-only":
        title = label("Official artifacts only", "仅官方产物")
    items = [f"[{title}]({entry.get('code_subdirectory_url') or url})"]
    metadata = entry.get("code_metadata")
    if metadata:
        items.append(star_badge(url, metadata["stars_snapshot"]))
        items.append(f"**{label('Last push', '最近推送')}:** {metadata['updated_at']}")
        if metadata["archived"]:
            items.append(f"**{label('Archived', '已归档')}**")
    note = entry.get("code_note_zh" if zh else "code_note_en")
    if note:
        items.append(f"**{label('Release notes', '发布说明')}:** {note}")
    return cell_list(items)


def category_overview(entries, categories, zh=False):
    label = lambda en, cn: cn if zh else en
    lines = ["## Category Overview", "",
             label("| Category | Resource | Entries |", "| 分类 | 资源类型 | 数量 |"),
             "| --- | --- | ---: |"]
    for key, titles in BLOG_SECTIONS.items():
        count = sum(e["kind"] == "reading" and e.get("blog_section") == key for e in entries)
        if count:
            lines.append(table_row([f"[{titles[int(zh)]}](#{heading_slug(titles[0])})",
                                    label("Blog", "博客"), count]))
    for kind, resource in (("paper", label("Paper", "论文")), ("project", label("GitHub project", "GitHub 项目"))):
        for category in categories:
            count = sum(e["kind"] == kind and e["category"] == category["name_en"] for e in entries)
            if count:
                title = category["name_zh" if zh else "name_en"]
                lines.append(table_row([f"[{title}](#{heading_slug(category['name_en'])})", resource, count]))
    lines += [table_row([label("**Total**", "**合计**"), "", f"**{len(entries)}**"]), ""]
    return lines


def render_readmes(catalog: dict[str, Any]) -> tuple[str, str]:
    validate_contract(catalog)
    entries, categories, meta = catalog["entries"], catalog["categories"], catalog["catalog"]
    projects = [e for e in entries if e["kind"] == "project"]
    papers = [e for e in entries if e["kind"] == "paper"]
    blogs = [e for e in entries if e["kind"] == "reading"]
    grouped = sorted_entries(projects, categories)
    outputs = []
    for language in ("en", "zh"):
        zh = language == "zh"
        label = lambda en, cn: cn if zh else en
        def explanation(entry):
            scope = SCOPE_LABELS[entry["scope"]][int(zh)]
            return cell_list([f"**{scope}**",
                              f"**{label('Loop', '闭环')}:** {entry['summary_' + language]}",
                              f"**{label('Boundary', '边界')}:** {entry['limitation_' + language]}"])
        lines = [f"# {meta['title_' + language]}", "", meta["description_" + language], "",
                 "[English](./README.md) | [中文](./README_zh.md)", "",
                 label(f"**{len(blogs)} first-party blog posts · {len(papers)} research papers · {len(projects)} active GitHub projects**",
                       f"**{len(blogs)} 篇一手博客 · {len(papers)} 篇研究论文 · {len(projects)} 个活跃 GitHub 项目**"), "",
                 label("## Contents", "## 目录"), "",
                 label("- [Category Overview](#category-overview)", "- [分类概览](#category-overview)"),
                 label("- [Company Research Blogs](#company-research-blogs)", "- [模型公司研究博客（优先阅读）](#company-research-blogs)")]
        for key, titles in BLOG_SECTIONS.items():
            if any(e.get("blog_section") == key for e in blogs):
                lines.append(f"  - [{titles[int(zh)]}](#{heading_slug(titles[0])})")
        lines.append(label("- [Papers and Official Code](#papers-and-official-code)", "- [论文与官方代码](#papers-and-official-code)"))
        for group in ("Models", "Harness", "Artifacts"):
            if any(e["improvement_target"] == group for e in papers):
                lines.append(f"  - [{group}](#papers--{group.lower()})")
        lines.append(label("- [Active GitHub Projects](#active-github-projects)", "- [活跃 GitHub 项目](#active-github-projects)"))
        for group in ("Models", "Harness", "Artifacts"):
            lines.append(f"  - [{group}](#{group.lower()})")
        lines += [label("- [Scope and Curation](#scope-and-curation)", "- [边界与收录原则](#scope-and-curation)"),
                  label("- [Maintenance](#maintenance)", "- [维护](#maintenance)"), ""]
        lines += category_overview(entries, categories, zh)
        lines += ["## Company Research Blogs", "",
                  label("Start here: first-party technical accounts from model builders and specialist AI research labs. Mechanisms, failures, agendas and historical foundations are separated; publisher claims are not independent replications.",
                        "建议从这里开始：模型开发公司与专项 AI 研究机构的一手技术材料。机制、失败、路线与历史基础分开呈现；发布方结论不等于独立复现。"), ""]
        for key, titles in BLOG_SECTIONS.items():
            selected = [e for e in blogs if e.get("blog_section") == key]
            if not selected:
                continue
            selected.sort(key=lambda e: (e.get("priority", 99), e["published_at"] or "", e["name"]))
            lines += [f"### {titles[0]}", ""]
            for e in selected:
                date = e["published_at"] or label("date not verified", "日期未核实")
                status = label(" · archived tutorial", " · 已归档教程") if e.get("content_status") == "archived" else ""
                title = f"[{e['name']}]({e['repo_url']})"
                lines.append(f"- **{title}** — {escape_md(e['publisher'])} · {date}{status}")
                scope = SCOPE_LABELS[e["scope"]][int(zh)]
                lines.append(f"  - **{label('Target', '改进对象')}:** `{e['improvement_target']}` · {scope}")
                lines.append(f"  - **{label('Loop', '闭环')}:** {escape_md(e['summary_' + language])}")
                lines.append(f"  - **{label('Boundary', '边界')}:** {escape_md(e['limitation_' + language])}")
                lines.append("")
            lines.append("")
        lines += ["## Papers and Official Code", "",
                  label("- Dates refer to first publication. Only source-verified venues are shown; a date alone makes no peer-review claim.",
                        "- 日期为首次发表日期。仅显示经来源核实的会议或期刊；只有日期不代表已通过同行评审。"),
                  label("- Official code is author-linked; artifact-only and archived releases are marked. Older code does not disqualify a useful paper.",
                        "- 官方代码指作者关联；仅发布产物和已归档的情况单独标注。旧代码不会使有价值的论文被排除。"),
                  label(f"- Star badges and push dates use the **{meta['last_verified']}** metadata snapshot.",
                        f"- Star 徽章与推送日期来自 **{meta['last_verified']}** 的元数据快照。"), ""]
        for group in ("Models", "Harness", "Artifacts"):
            selected = sorted([e for e in papers if e["improvement_target"] == group],
                              key=lambda e: (e["published_at"], e["name"]), reverse=True)
            if not selected:
                continue
            lines += [f"### Papers / {group}", "", label("| Paper | Date / Publication | Code | Contribution and Boundary |",
                         "| 论文 | 日期 / 发表状态 | 代码 | 贡献与边界 |"), "| --- | --- | --- | --- |"]
            for e in selected:
                publication = e["published_at"]
                if e.get("venue") and e.get("venue_evidence_url"):
                    publication += f"<br>[{e['venue']}]({e['venue_evidence_url']})"
                lines.append(table_row([f"[{e['name']}]({e['repo_url']})", publication,
                                        paper_code_cell(e, zh), explanation(e)]))
            lines.append("")
        lines += ["## Active GitHub Projects", "",
                  label(f"Repository metadata snapshot: **{meta['last_verified']}**. Only public, non-archived projects pushed in the last **60 days** appear here; stars are snapshots, not evidence of RSI. Paper-associated code above has no activity gate.",
                        f"仓库元数据快照：**{meta['last_verified']}**。本节只列公开、未归档、最近 **60 天**有 push 的项目；star 是快照，不是 RSI 证据。上方论文配套代码不受活跃窗口限制。"), ""]
        for group in ("Models", "Harness", "Artifacts"):
            lines += [f"### {group}", ""]
            for c in categories:
                if c["group"] != group or not grouped[c["name_en"]]:
                    continue
                lines += [f"#### {c['name_en']}", "", c["description_" + language], "",
                          label("| Project | Link | Stars | Tags | Improvement Loop and Boundary |",
                                "| 项目 | 链接 | Stars | 标签 | 改进闭环与边界 |"), "| --- | --- | ---: | --- | --- |"]
                for e in grouped[c["name_en"]]:
                    lines.append(table_row([e["name"], f"[GitHub]({e['repo_url']})", star_badge(e["repo_url"], e["stars_snapshot"]),
                        "<br>".join(f"`{tag}`" for tag in e["tags"]),
                        explanation(e) + f"<br>• [{label('Evidence', '证据')}]({e['evidence_url']})"]))
                lines.append("")
        lines += ["## Scope and Curation", "", meta["scope_" + language], "",
                  label("No entry establishes unbounded autonomous RSI. Within-task refinement, safety evaluation and research agendas are relevant context, not demonstrations of persistent self-improvement. Counts refer to resources: a blog, paper and repository may document the same research, not three independent breakthroughs.",
                        "任何条目都不代表已实现无界自主 RSI。任务内修订、安全评测和研究路线是相关背景，不是持久自改进的实证。数量统计的是资源：一篇博客、论文和仓库可能对应同一研究，并非三项独立突破。"), "",
                  "## Maintenance", "",
                  label("All live entries are maintained in `data/projects.yaml`; both READMEs are generated. Source interpretation and translation require review; metadata and links cannot certify scientific claims.",
                        "所有正式条目在 `data/projects.yaml` 维护，两份 README 均由脚本生成。来源解读与翻译需要审查；元数据和链接不能证明科研结论。"), "",
                  "```bash", "python3 scripts/sync_github_metadata.py", "python3 scripts/render_readme.py",
                  "python3 scripts/verify_catalog.py", "python3 -m unittest discover -s tests -v", "```", "",
                  "- [Curation policy](docs/curation_policy.md)", "- [Sources and verification](docs/sources_and_verification.md)",
                  "- [Research coverage and decisions](docs/research_decisions.md)",
                  "- [Taxonomy](docs/taxonomy_iterations.md)", "- [Contributing](CONTRIBUTING.md)", ""]
        outputs.append("\n".join(lines))
    return tuple(outputs)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    en, zh = render_readmes(load_catalog())
    for path, text in ((README_EN, en), (README_ZH, zh)):
        if args.check:
            if not path.exists() or path.read_text(encoding="utf-8") != text:
                raise SystemExit(f"Out of sync: {path.name}")
        else:
            path.write_text(text, encoding="utf-8")
            print(f"Rendered: {path}")
    if args.check:
        print("README mirrors are up-to-date.")


if __name__ == "__main__":
    main()
