# Research Decisions: 2026-09-08

This is a dated audit trail, not an alternative active catalog. Retained entries live only in `data/projects.yaml`. GitHub activity below was observed from repository REST metadata; the inclusive 60-day cutoff is 2026-07-10.

## Removed False Positives

The previous 89-entry catalog was not RSI-focused. Examples included Dify, Langflow, system-prompts-and-models-of-ai-tools, awesome-llm-apps, TradingAgents, RAGFlow, MinerU, JavaGuide, JeecgBoot, tldraw and Front-End-Checklist. High stars and recent activity did not demonstrate a self-improvement mechanism. Many had the identical Chinese summary claiming they were open models/training components.

Generic OpenHands and SWE-agent entries were also rejected during this audit: being usable as an evaluation substrate is not enough. Open-R1's general RL/distillation recipes do not independently establish the recursive internally generated-data loop required here. It was also outside the activity window.

General Anthropic/OpenAI harness articles, including building-effective-agents, effective-harnesses-for-long-running-agents, harness-engineering and unrolling-the-codex-agent-loop, are not retained just for describing repeated tool use or human-led engineering.

## Relevant Research Outside the Activity Window

| Repository | Observed last push | Decision |
| --- | --- | --- |
| [jennyzzt/dgm](https://github.com/jennyzzt/dgm) | 2025-08-13 | Genuine self-modifying agent research; code excluded from active list. Its primary Sakana article is retained as research reading. |
| [LeapLabTHU/Absolute-Zero-Reasoner](https://github.com/LeapLabTHU/Absolute-Zero-Reasoner) | 2025-08-24 | Proposal/solve self-play with execution rewards and TRR++ model updates; strong model-loop evidence, but inactive. |
| [Chengsong-Huang/R-Zero](https://github.com/Chengsong-Huang/R-Zero) | 2026-02-04 | Challenger/solver co-evolution; finite, non-monotonic experiments, not infinite RSI. Outside window. |
| [karpathy/autoresearch](https://github.com/karpathy/autoresearch) | 2026-03-26 | `program.md` edits `train.py`, evaluates fixed `val_bpb`, retains improvements and rejects regressions. About 95k stars does not override inactivity. |
| [SakanaAI/AI-Scientist](https://github.com/SakanaAI/AI-Scientist) | 2025-12-19 | Automated experiment/review artifacts, not evidence of self-modifying research machinery; outside window. |
| [microsoft/PromptWizard](https://github.com/microsoft/PromptWizard) | 2025-10-13 | Bounded prompt/example optimization, not weight RSI; outside window. |
| [zou-group/TextGrad](https://github.com/zou-group/TextGrad) | 2025-07-25 | Textual-gradient optimization is relevant background but outside window. |
| [huggingface/open-r1](https://github.com/huggingface/open-r1) | 2026-04-02 | General reasoning training recipes; insufficient recursive-loop evidence and stale. |
| [NousResearch/hermes-agent-self-evolution](https://github.com/NousResearch/hermes-agent-self-evolution) | 2026-06-17 | Dedicated project discovered from GEPA links. Metadata checked; README API hit rate limit, so mechanism not certified. Also stale. |

The main Hermes Agent entry is explicitly about learned skills, not a substitute claim about its separate self-evolution repository.

## Misleading Labels and Canonical URLs

- [EvoMap/evolver](https://github.com/EvoMap/evolver), active 2026-09-06, says **'Evolver is a prompt generator, not a code patcher'** and **'Automatically edit your source code'** under what it does NOT do. Host interpretation is required for printed session-spawn instructions. Its README also states core engine modules are obfuscated. Excluded from an inspectable autonomous self-modification list.
- [facebookresearch/cwm](https://github.com/facebookresearch/cwm), active 2026-07-17, describes execution-trajectory pretraining and multitask RL, not a demonstrated repeated self-generated-data self-training loop. Activity alone is insufficient.
- The DGM article links `jennyzzt/dgm`. `evanthebouncy/Darwin-Godel-Machine` and `SakanaAI/DGM` returned 404. Absolute Zero's verified repository is `LeapLabTHU/Absolute-Zero-Reasoner`, not an organization inferred from the paper title.
- Agent0 was exactly on the 2026-09-08 60-day calendar-date boundary. On 2026-09-09 the cutoff moved to 2026-07-11, so its 2026-07-10 push aged out and the active project entry was removed. The paper record remains, and its public guide's manual checkpoint selection remains documented.

## Initial Reading Decisions (Superseded by Expansion Below)

Retained first-party readings: Sakana's DGM and ShinkaEvolve; Google DeepMind's AlphaEvolve, AlphaGo Zero and AlphaZero. Publication dates came from visible original article content. The two game self-play posts are marked foundational, not recent frontier releases.

[OpenAI/Bain's Self-Evolving Agents cookbook](https://developers.openai.com/cookbook/examples/partners/self_evolving_agents/autonomous_agent_retraining), published 2025-11-04, was discovered in GEPA's README and read at its canonical redirected URL. The page explicitly says **'This recipe is archived and may reference outdated models or APIs.'** It demonstrates prompt version updates, graders and GEPA, not model-weight retraining despite its title. It also warns about overfitting and recommends production human approval. The example constructs `valset` as a slice of `trainset` without removing those samples from `trainset`; do not repeat the surrounding claim of fully disjoint validation as verified. Kept here as historical bounded prompt-optimization material, not active selected reading.

OpenAI weak-to-strong and Anthropic Constitutional AI requests returned 403 in this run; these were not included on the strength of memory alone. No generic article was substituted simply to fill an organization quota.

## Expanded Review: Blogs First, Papers Separate

The user's expanded scope replaces the initial five-reading selection: **31 company blogs, 37 papers and 10 active projects**. All live records are in the canonical YAML, with bilingual mechanism/limitation text. The dated worksheets preserve discovery evidence, exclusions and retrieval notes:

- `reports/research/company-blogs.yaml`: 14 retained candidates from Anthropic, MiniMax, Kimi, OpenAI/Bain and Prime Intellect, plus excluded/blocked candidates.
- `reports/research/google-sakana-blogs.yaml`: 12 additional Google/Sakana articles plus specific exclusions; the original five remain.
- `reports/research/papers.yaml` and `papers-extra.yaml`: 37 distinct papers. STOP / Self-Taught Optimizer is one paper. Prime Agent and Continual Harness are distinct papers, not duplicate names for one system.

Anthropic Constitutional AI and three direct automated-research/RSI sources were retrieved successfully in the expanded review. The first-party RSI agenda explicitly says the complete cycle is not yet achieved or inevitable. Sakana's RSI Lab agenda is likewise a direction, not a demonstrated complete loop. MiniMax M2.7's internal scaffold results and M3's external-model training experiments have different changed objects.

The OpenAI/Bain tutorial is now included under **Foundations and Historical Tutorials**, with its archive warning and overlapping train/validation example caveat. This is an explicit scope change, not a claim that the archived recipe is current. OpenAI research URLs for competitive self-play, emergent tool use and weak-to-strong generalization continued to return 403; sitemap branches also failed/timed out. No content claims were inferred from those failures. Meta/Microsoft sources that could not be retrieved were not replaced with generic announcements.

Historical DGM, Absolute Zero, R-Zero, TextGrad, DiscoPOP, CycleQD and other code can now appear beside papers without entering the active-project list. Thirty-two papers have author-linked code or associated implementations; five do not in reviewed sources. Meta's RAM project inventory links Self-Rewarding Language Models as a paper, not a released implementation. AlphaEvolve is not linked to OpenEvolve as official code. Self-Taught Evaluators releases evaluation scripts/models/data, and the Continual Harness repository does not certify reproduction of every weight co-learning experiment.

Thirteen papers have explicitly sourced venue claims, including NeurIPS, ICML, ICLR, ACL and Nature. SICA is an **ICLR workshop**, not main track. Null venues mean not established in this review. Dates are first arXiv submissions or first online publisher dates: DGM paper May 29 versus blog May 30; Shinka paper September 17 versus blog September 25; Prime Agent arXiv August 24 versus blog August 5. Unknown original blog dates remain null.

Prime Agent's primary README and REST metadata establish retained supplemental-harness refinement and current activity; it joins the active project list. Base prompts remain immutable and process isolation is not a security sandbox. DRQ, DiscoPOP and CycleQD repositories were also inspected but are outside the active window.

The full link check found Absolute Zero's evidence README used `main` even though its default branch is `master`; the original README was fetched and the live evidence URL corrected. This illustrates why checking repository roots alone is insufficient.

## Retrieval and Limits

The configured web search lacked its API credential. The web-fetch helper rejected several public hostnames after DNS resolution; direct read-only HTTP retrieval of public GitHub REST/raw endpoints and original publisher HTML succeeded. GitHub REST later hit an unauthenticated research-read rate limit; the final nine-project metadata sync had already succeeded. Research used primary README/source/article content, not search snippets. No API credential was exposed or changed.

Link reachability, metadata freshness and hand-reviewed evidence are different checks. Catalog verification reports only the checks it actually performs. Benchmark claims were not independently reproduced.
