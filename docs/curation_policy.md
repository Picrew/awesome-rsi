# RSI Curation Policy

## Scope

Recursive Self-Improvement (RSI) requires improved systems to participate in subsequent improvement. This catalog distinguishes self-referential improvement, iterative self-training, supporting implementations, and explicitly labeled theory/evaluation. Repeated tool calls alone do not qualify.

- `self-modification`: agent code or mutable harness state changes and influences subsequent improvement.
- `self-training`: internally generated tasks, trajectories or supervision update retained model weights across iterations.
- `bounded-optimization`: fixed search/evaluation machinery improves prompts, workflow graphs, model variants, training recipes or programs.
- `experience-learning`: feedback revises durable memory, playbooks or executable skills reused in later trials/tasks.
- `inference-refinement`: revision within a task without demonstrated cross-task persistence; adjacent context, not durable RSI.
- `safety-evaluation`: a direct study of improvement-loop validity, reward manipulation or research sabotage; not a beneficial self-improver.
- `research-agenda`: a proposed route to RSI, explicitly separated from demonstrated results.

No label proves indefinite capability growth. Do not silently promote fixed-model optimization to autonomous learner improvement.

## Presentation Priority

1. A short reading guide and generated category overview.
2. First-party company research blogs: direct mechanisms/results first; supporting AI research, evaluation, agendas and historical tutorials in collapsible subsections that are open by default.
3. Papers: `Papers / Harness`, `Papers / Models`, and `Papers / Theory and Evaluation`, with author-linked code beside the mechanism. Short display names retain canonical full titles in the catalog.
4. Active GitHub implementations under consistently prefixed `GitHub / Models`, `GitHub / Harness`, and `GitHub / Artifacts` headings, subject to the repository activity gate. Bounded optimizers and learned skills remain labeled supporting tools, not standalone RSI demonstrations.

Counts refer to resources, not independent breakthroughs: a blog, paper and repository may describe the same work. Prefer original technical accounts to syndicated duplicates. Related follow-ups need substantial new mechanisms, empirical applications or corrections.

## Company Blogs

Use first-party technical material from model builders and specialist AI research labs; identify the publisher accurately. Do not pretend every specialist lab is a frontier-scale model company. A product announcement only qualifies when a specific section describes a concrete retained loop. General agent engineering, press coverage and tool-use demos do not qualify by publisher prestige alone.

Preserve original publication dates separately from evidence review and API sync dates. Unknown dates remain null with a documented search note; omit the date in the README rather than inserting an audit placeholder. An official publisher index can establish the original date when the article itself does not show it. Archived tutorials can appear only in the historical subsection with an explicit archive warning and limitations. Research agendas and failure reports have their own sections and labels. Publisher claims are not independent replications.

## Paper Gate

The main list has three explicit routes:

- **Harness:** the agent changes its own implementation or control procedure and uses that changed system in later improvement. Retained memory alone does not suffice; Continual Harness is retained for its explicit act/refine loop and separately described model co-learning experiment.
- **Models:** updated weights participate in producing later training data, curricula, solutions or evaluation signals. This includes bounded self-training foundations; do not claim that a fixed learning rule rewrites itself.
- **Theory and Evaluation:** a direct formalization, position paper or failure/measurement study of these loops. Label theoretical and empirical roles separately from agent implementations.

Move fixed external prompt/workflow/program optimization, one-task refinement, generic framework integration and skill-memory-only work to [related methods](related_methods.md). Quality, relevance and maturity are separate judgments: an excellent neighboring paper may be outside this narrower list, and a new relevant preprint is not automatically an established result. Prefer demonstrated loop closure, inspectable methods, meaningful baselines, held-out evaluation and clear failure analysis; neither stars nor recency alone establishes quality.

Read the canonical arXiv abstract/full text, proceedings/publisher article, and author-linked implementation documentation where available. Record a short exact excerpt and target/feedback/update/persistence mechanism, with specific bilingual contributions and limitations.

Use the first arXiv version date, or first publisher online date when no arXiv source is used. Do not substitute blog publication dates or journal issue dates. State conference/journal/workshop identity only when an author-linked source or publisher explicitly establishes it, and preserve that evidence URL and excerpt. A workshop is not the conference main track. A missing venue means not established in this review, not rejected or definitely unpublished.

Search the original paper, author project site and linked repository before recording `code_status: not-found`. This does not mean no code exists. Render it as an em dash with a shared legend, keeping search details in the data. Official means author-linked, not necessarily complete. Flag associated/partial releases and artifact-only releases. Do not label OpenEvolve as official AlphaEvolve code, or substitute an unofficial self-rewarding reproduction for Meta's unreleased implementation. Inactive and archived public code can remain beside historical papers; preserve archive status and put push dates/release notes in collapsible details that are open by default.

## Active Project Gate

1. Read primary implementation documentation, relevant source or the authors' technical account; a self-evolving name is not evidence.
2. Record target, feedback, update and persistence plus original evidence, review date and strongest limitations in both languages.
3. Require a canonical public, non-archived GitHub repository pushed within the last 60 days, inclusive UTC calendar dates. On 2026-09-08 the cutoff is 2026-07-10.
4. Prefer inspectable implementation, credible evaluation and adoption after relevance is established. No minimum star or count quota.
5. Push activity is not proof of research progress. Stars and social `updated_at` changes cannot replace `pushed_at`.
6. Preserve API license results. `NOASSERTION` and `none` are not OSI license certifications.

## Classification and Ownership

Classify by what changes: **Models** for weights/training processes, **Harness** for agent implementations/prompts/workflows, **Artifacts** for executable algorithms, curricula and retained playbooks/skills. Do not add generic categories merely for visual balance.

All live entries belong in `data/projects.yaml`. Both READMEs are generated. Dated worksheets in `reports/research/` and decisions in `docs/research_decisions.md` preserve provenance, not a second maintained catalog. The one-time import script is not a normal maintenance command.

## Scientific Caution

Benchmark gains may reflect leakage, grader weaknesses or reward hacking. Preserve held-out evaluation limitations, mutable-evaluator boundaries and non-monotonic results. This repository does not execute third-party agents or reproduce GPU experiments. Schema, links and metadata cannot certify causal improvement or semantic translation equivalence.
