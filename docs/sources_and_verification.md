# Sources and Verification

## Evidence Workflow

Start from a primary paper/article and its released implementation, or inspect a repository's actual optimizer code. Follow primary links to broaden discovery. Record the exact changed object, feedback, update rule, retained state, limitations and short source excerpt in `data/projects.yaml`. Review English and Chinese together.

The 2026-09-09 audit includes 31 first-party blogs, 29 papers and 11 active projects. Original publisher content covers Google DeepMind/Research, Anthropic, MiniMax, Moonshot/Kimi, OpenAI/Bain, Sakana AI and Prime Intellect. The main paper list focuses on self-modifying agents, iterative self-training, and theory/evaluation of these loops. Eighteen adjacent methods are documented separately in [related methods](related_methods.md); ten primary-source papers were added. Twenty-one papers have author-linked code or associated implementations; eight have no official code established in reviewed sources. See [dated research decisions](research_decisions.md) and `reports/research/` for provenance and excluded candidates.

## Commands

Python 3.10+ and PyYAML are required:

```bash
python3 -m pip install -r requirements.txt
python3 scripts/sync_github_metadata.py
python3 scripts/render_readme.py
python3 scripts/verify_catalog.py
python3 -m unittest discover -s tests -v
```

A `GITHUB_TOKEN` environment variable or existing `gh auth` login is optional but recommended to avoid public REST rate limits. Do not put tokens in YAML or commit them.

## What Each Step Proves

- **sync_github_metadata.py** fetches public GitHub REST metadata for active projects and paper-linked code: canonical URL, stars, full push timestamp, public/archive flags and SPDX result. Shared repositories are fetched once. Paper code gets nested `code_metadata` and may be inactive/archived; active projects may not be archived. It never rewrites curated descriptions, scope, source evidence or review dates. Any request/state failure returns nonzero and leaves the catalog unchanged. A complete successful fetch advances the metadata snapshot date; that is not a new scientific review.
- **render_readme.py** produces both languages from one catalog and identical project order. It does not synthesize missing summaries or hard-code unrelated featured articles. `--check` compares without writing. Standard Markdown headings avoid visible raw HTML anchor tags. Snapshot star badges use one consistent style. Paper dates sit below concise titles; boundaries and release metadata are shown by default in manually collapsible details. Unknown blog dates are omitted from the rendered page, while their uncertainty remains recorded in the catalog.
- **verify_catalog.py** checks typed required fields, duplicate summaries/names/URLs, complete feedback-loop evidence, allowed scopes, the narrower main-paper scope gate, category membership, empty sections, canonical public/non-archived GitHub metadata, the inclusive 60-day UTC-date push window, metadata snapshot age (maximum seven days), dates, mirrored output and every included repository, article, paper, venue, code-linkage, code-subdirectory and date-evidence URL. Names can repeat across resource kinds but not within one kind. Venue/code claims require evidence fields; unknown blog dates require an explicit note. Missing metadata fails closed.
- **Link checks** use HEAD then GET as needed. 403/challenge pages, 429/rate limits and network failures are unverified, not silently successful. Full verification fails on any broken or unverified included source link. HTTP reachability does not certify article content or GitHub fragment existence.

Reports are written to `reports/verification/YYYY-MM-DD.md`. `--skip-links` is explicitly offline-only and writes a separate `YYYY-MM-DD-offline.md` so it cannot overwrite a full report.

## Manual Review Remains Necessary

Mechanism descriptions and translations require human judgment. A schema cannot prove RSI relevance, causal capability improvement, held-out generalization, substantive recent development, license suitability or safety. The audit did not execute third-party self-modifying code or reproduce GPU-intensive experiments. Never convert these limitations into a 'fully verified RSI' claim.
