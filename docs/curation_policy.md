# RSI Curation Policy

## Scope

Recursive Self-Improvement (RSI) requires improved systems to participate in subsequent improvement. This catalog covers demonstrated loops, bounded components, and clearly labeled evaluation/agendas. Repeated tool calls alone do not qualify.

- `self-modification`: agent code or mutable harness state changes and influences subsequent improvement.
- `self-training`: internally generated tasks, trajectories or supervision update retained model weights across iterations.
- `bounded-optimization`: fixed search/evaluation machinery improves prompts, workflow graphs, model variants, training recipes or programs.
- `experience-learning`: feedback revises durable memory, playbooks or executable skills reused in later trials/tasks.
- `inference-refinement`: revision within a task without demonstrated cross-task persistence; adjacent context, not durable RSI.
- `safety-evaluation`: a direct study of improvement-loop validity, reward manipulation or research sabotage; not a beneficial self-improver.
- `research-agenda`: a proposed route to RSI, explicitly separated from demonstrated results.

No label proves indefinite capability growth. Do not silently promote fixed-model optimization to autonomous learner improvement.

## Presentation Priority

1. First-party company research blogs: mechanisms/results, evaluation/failure modes, research agendas, historical foundations/tutorials.
2. Papers, grouped by Models / Harness / Artifacts, with author-linked code in an adjacent column.
3. Active GitHub implementations, subject to the stricter repository activity gate.

Counts refer to resources, not independent breakthroughs: a blog, paper and repository may describe the same work. Prefer original technical accounts to syndicated duplicates. Related follow-ups need substantial new mechanisms, empirical applications or corrections.

## Company Blogs

Use first-party technical material from model builders and specialist AI research labs; identify the publisher accurately. Do not pretend every specialist lab is a frontier-scale model company. A product announcement only qualifies when a specific section describes a concrete retained loop. General agent engineering, press coverage and tool-use demos do not qualify by publisher prestige alone.

Preserve original publication dates separately from evidence review and API sync dates. Unknown dates may be null with a documented search note. Archived tutorials can appear only in the historical subsection with an explicit archive warning and limitations. Research agendas and failure reports have their own sections and labels. Publisher claims are not independent replications.

## Paper Gate

Read the canonical arXiv abstract/full text, proceedings/publisher article, and author-linked implementation documentation where available. Record a short exact excerpt and target/feedback/update/persistence mechanism, with specific bilingual contributions and limitations.

Use the first arXiv version date, or first publisher online date when no arXiv source is used. Do not substitute blog publication dates or journal issue dates. State conference/journal/workshop identity only when an author-linked source or publisher explicitly establishes it, and preserve that evidence URL and excerpt. A workshop is not the conference main track. A missing venue means not established in this review, not rejected or definitely unpublished.

Search the original paper, author project site and linked repository before recording `code_status: not-found`. This does not mean no code exists. Official means author-linked, not necessarily complete. Flag associated/partial releases and artifact-only releases. Do not label OpenEvolve as official AlphaEvolve code, or substitute an unofficial self-rewarding reproduction for Meta's unreleased implementation. Inactive and archived public code can remain next to useful historical papers; show archive status and last push instead of applying the active-project gate.

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
