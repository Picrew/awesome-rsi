# RSI Discovery Queries

Queries discover candidates; they do not establish relevance. Inspect primary documentation and executable mechanisms before adding an entry. Compute the 60-day cutoff at research time. For the 2026-09-08 audit, use `pushed:>=2026-07-10 archived:false`; `stars:>=100` is an optional triage preference, never a substitute for evidence.

## Models

- `"self-play" "reasoning" in:readme`
- `"curriculum" "co-evolution" in:readme`
- `"self-training" "iterations" in:readme`
- `"autonomous" "fine-tuning" "feedback" in:readme`

Check that weights actually update, how tasks/rewards are produced, and whether improved checkpoints feed later rounds. Do not infer a recursive loop from ordinary RL support.

## Harness

- `"self-modification" "agent" in:readme`
- `"meta-agent" "self-improving" in:readme`
- `"reflective" "prompt optimization" in:readme`
- `"workflow" "evolution" "evaluation" in:readme`

Read the patch application, evaluation and successor-selection paths. Determine whether mutation logic is itself editable or remains externally fixed.

## Artifacts

- `"program evolution" "evaluator" in:readme`
- `"algorithm discovery" "archive" in:readme`
- `"skills" "learning loop" in:readme`
- `"training loss" "evolution" in:readme`

Look for retained candidates or skill revisions that influence future runs. A static artifact library, generic code generator or memory store is insufficient.

## Company Blogs (Highest Priority)

Start with original research indexes and sitemaps from Anthropic, OpenAI, Google DeepMind/Research, Meta, Microsoft, MiniMax, Moonshot/Kimi, Sakana AI and other model-building labs. Useful concepts include recursive self-improvement, automated alignment research, AI for AI, self-harness evolution, self-training, reward tampering and learned optimization. Follow original links, inspect the actual mechanism section and verify dates from article content or a dated publisher index. Prefer an absent organization over generic filler. Record blocked pages separately; HTTP 200 with unrelated content is not evidence.

## Papers and Official Code

Search exact paper titles in arXiv, OpenReview, NeurIPS proceedings, PMLR, ACL Anthology and journal publishers. Follow paper-to-project-to-repository links, verify matching title/authors, inspect the default branch, and distinguish complete implementation from scripts/data/associated harness only. Venue assertions need a specific author/publisher source; do not upgrade a workshop to main track. Do not apply the 60-day repository gate to these historical research resources. A code search that finds nothing should record the checked sources, not assert universal absence.
