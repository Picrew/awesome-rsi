# RSI Taxonomy Decisions

## 1. Remove Inherited Harness Categories

The previous catalog renamed general agent tools without changing their inclusion logic. Empty foundation-model categories and hundreds of identical summary fragments created a false RSI map. Generic runtimes, RAG, observability, sandboxes, and static skill lists are no longer categories.

## 2. Classify the Object Changed

| Group | Subtopics | What changes |
| --- | --- | --- |
| Models | Self-Training; Training Research | Model weights, training recipe and model experiments |
| Harness | Self-Modification; Prompt and Workflow Optimization | Agent source, improvement procedure, prompts, workflow graph |
| Artifacts | Program Evolution; Learned Skills | Executable algorithms and durable procedural skill artifacts |

Prompt tuning is not weight training. A program-evolution harness belongs under Artifacts when the changed object is the candidate program. FT-Agent's specific training scenario belongs under Models, not every RD-Agent feature. Hermes is included for learned skills, not its terminal or chat integrations.

## 3. Separate Recursion Strength

Use explicit scope labels instead of treating all iteration as RSI: self-modification, self-training, bounded-optimization and experience-learning. Expanded context also includes inference-refinement, safety-evaluation and research-agenda; none of these three is presented as demonstrated persistent capability improvement. Display limitations in the same table cell as the mechanism. Fixed-optimizer program search is related research, not a claim that the search machinery improves itself.

## 4. Gate Before Ranking

First require a supported mechanism; then public/non-archived GitHub and a recent push; then weigh inspectability, evaluations, adoption and stars. No minimum count is used to populate weak categories. Historical research belongs in the paper/blog sections without the activity gate, not in the active-project list. Official paper code retains push/archive metadata even when old.

## 5. Keep Mirrors and Navigation Simple

Use the reference's data-driven Markdown tables and matching project order. Both mirrors retain English topic headings for stable automatic GitHub anchors; Chinese descriptions, table content, boundary statements and navigation labels are translated. Do not emit raw HTML anchors that some Markdown renderers display literally. A short reading path and category overview lead into company blogs, grouped by mechanisms, supporting methods, failure modes, agendas and historical material. All collapsible content, including supporting/contextual blog groups, is open by default. Papers follow in Papers / Harness, Papers / Models and Papers / Theory and Evaluation tables with adjacent official code. Active projects use consistent GitHub / Models, GitHub / Harness and GitHub / Artifacts headings, including the GitHub prefix on their subtopics. Fixed-optimizer and within-task-refinement papers are retained in the related-methods document rather than the main paper tables. Every resource has a stated improvement target.
