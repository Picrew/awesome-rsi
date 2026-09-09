# Contributing to Awesome RSI

Prioritize first-party model-company research, well-screened papers and concrete implementations. Read [curation policy](docs/curation_policy.md). This standalone repository uses awesome-agent-harness only as a read-only format reference.

## Evidence

Explain what changes, the feedback signal, the update and what survives into later rounds. Read original technical material and author-linked implementation documentation. Disclose fixed-model, human-selection, benchmark and release limitations in both languages. No catalog-size or star quota applies.

Papers and their official code have no activity gate. Only the active GitHub section requires public, non-archived repositories pushed within 60 UTC calendar days.

## Data Contract

Edit `data/projects.yaml` only for live entry changes. Preserve top-level `catalog`, `categories`, `entries` and original fields:

`name | repo_url | category | summary_en | summary_zh | tags | stars_snapshot | updated_at | why_included`

Every entry also needs:

- `kind`: `project`, `reading` (company blog), or `paper`.
- `scope`: `self-modification`, `self-training`, `bounded-optimization`, `experience-learning`, `inference-refinement`, `safety-evaluation`, or `research-agenda`.
- `rsi_mechanism`: nonempty `target`, `feedback`, `update`, `persistence`; agendas/evaluations must describe their non-demonstration boundary honestly.
- `evidence_url`, `evidence_excerpt`, `reviewed_at`: primary source, short exact passage, manual review date.
- `limitation_en`, `limitation_zh`: specific, truthful limits.

Project metadata is synced: `pushed_at`, `updated_at` (push date), `stars_snapshot`, `archived`, `private`, `license`, `metadata_checked_at`, `metadata_source`. Never invent missing metadata. Sync does not advance editorial review dates.

Blogs require `publisher`, `published_at`, `improvement_target` and `blog_section` (`mechanisms`, `safety`, `agenda`, `foundations`). A null publication date requires `date_note`. Preserve a `date_evidence_url` when a publisher index establishes the date. `priority` orders entries within the subsection, followed by date/name; `content_status: archived` marks historical tutorials.

Papers require `improvement_target`, `published_at`, `publication_status` (`published` or `preprint`), nullable `venue`, and `venue_evidence_url`/excerpt for any venue claim. `preprint` means an arXiv source with venue unverified here, not proof that no later publication exists. Preserve a more specific `publication_status_detail` where helpful.

Papers also require `code_status` (`official`, `not-found`, `third-party`), nullable `code_url`, linkage `code_evidence_url`/`code_evidence_excerpt`, and `code_release` (`implementation` or `artifacts-only`) when linked. `code_note_en/zh` discloses partial or associated implementations. A code URL is the repository root for API sync; optional `code_subdirectory_url` links the precise implementation in the table. Missing code requires `code_search_note` documenting reviewed sources. Synced `code_metadata` belongs to the code repository, never to the arXiv URL or paper publication date.

Categories retain `id`, `anchor`, `name_en`, `name_zh`, `group`, `description_en`, `description_zh`. Do not introduce empty sections. Names may repeat across resource kinds, but duplicate resources within one kind and duplicate URLs/summaries fail verification.

## Validation

Python 3.10+ and `requirements.txt` are required. Optional `GITHUB_TOKEN` or existing `gh auth` avoids public API limits; never put credentials in YAML.

```bash
python3 scripts/sync_github_metadata.py
python3 scripts/render_readme.py
python3 scripts/verify_catalog.py
python3 -m unittest discover -s tests -v
python3 scripts/render_readme.py --check
```

Review both generated mirrors, especially blog coverage/order, paper-code adjacency, workshop identities and historical code labels. Include the data, mirrors and verification report. `--skip-links` is offline-only; HTTP 403/429 is unverified, not successful. Dated research worksheets are audit artifacts; do not rerun the one-time merger during ordinary maintenance.
