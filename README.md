# Awesome RSI

A curated research map of recursive self-improvement: agents that revise their own machinery, models that generate their next training signal, and the evidence that defines their limits.

[English](./README.md) | [中文](./README_zh.md)

**31 first-party blog posts · 29 research papers · 11 active GitHub projects**

## Start Here

| Reading path | What to look for |
| --- | --- |
| [Self-modifying agents](#papers--harness) | Does the revised agent participate in its next improvement? |
| [Iterative self-training](#papers--models) | Do updated models generate the next training data, curriculum or rewards? |
| [Theory and evaluation](#papers--theory-and-evaluation) | Which assumptions and measurements support the loop? |

**Reading the evidence:** self-modification, bounded self-training and theoretical proposals are different claims. [Related methods and selection decisions](docs/related_methods.md) explain what stays outside the main paper list.

## Contents

- [Category Overview](#category-overview)
- [Company Research Blogs](#company-research-blogs)
  - [Mechanisms and Results](#mechanisms-and-results)
  - [AI Research and Supporting Methods](#ai-research-and-supporting-methods)
  - [Evaluation and Failure Modes](#evaluation-and-failure-modes)
  - [Research Agendas](#research-agendas)
  - [Foundations and Historical Tutorials](#foundations-and-historical-tutorials)
- [Papers and Official Code](#papers-and-official-code)
  - [Papers / Harness](#papers--harness)
  - [Papers / Models](#papers--models)
  - [Papers / Theory and Evaluation](#papers--theory-and-evaluation)
- [Active GitHub Projects](#active-github-projects)
  - [GitHub / Models](#github--models)
  - [GitHub / Harness](#github--harness)
  - [GitHub / Artifacts](#github--artifacts)
- [Scope and Curation](#scope-and-curation)
- [Maintenance](#maintenance)

## Category Overview

| Category | Resource | Entries |
| --- | --- | ---: |
| [Mechanisms and Results](#mechanisms-and-results) | Blog | 6 |
| [AI Research and Supporting Methods](#ai-research-and-supporting-methods) | Blog | 15 |
| [Evaluation and Failure Modes](#evaluation-and-failure-modes) | Blog | 4 |
| [Research Agendas](#research-agendas) | Blog | 2 |
| [Foundations and Historical Tutorials](#foundations-and-historical-tutorials) | Blog | 4 |
| [Papers / Harness](#papers--harness) | Paper | 9 |
| [Papers / Models](#papers--models) | Paper | 16 |
| [Papers / Theory and Evaluation](#papers--theory-and-evaluation) | Paper | 4 |
| [GitHub / Models / Training Research](#github--models--training-research) | GitHub project | 1 |
| [GitHub / Models / Recursive Self-Training](#github--models--recursive-self-training) | GitHub project | 1 |
| [GitHub / Harness / Self-Modification](#github--harness--self-modification) | GitHub project | 3 |
| [GitHub / Harness / Prompt and Workflow Optimization](#github--harness--prompt-and-workflow-optimization) | GitHub project | 3 |
| [GitHub / Artifacts / Program Evolution](#github--artifacts--program-evolution) | GitHub project | 2 |
| [GitHub / Artifacts / Learned Skills](#github--artifacts--learned-skills) | GitHub project | 1 |
| **Total** |  | **71** |

## Company Research Blogs

Start here: first-party technical accounts from model builders and specialist AI research labs. Mechanisms, failures, agendas and historical foundations are separated; publisher claims are not independent replications.

### Mechanisms and Results

- **[The Darwin Godel Machine: AI that improves itself by rewriting its own code](https://sakana.ai/dgm/)** — Sakana AI · 2025-05-30
  - `Harness` · **Self-modification** — Describes an agent that rewrites its tools and workflows, evaluates descendants on coding benchmarks, and branches from a growing archive to improve again.
  - **Boundary:** Foundation-model training is future work; the article documents reward hacking and supervised sandbox limits.

- **[Kimi K2: Open Agentic Intelligence](https://www.kimi.com/en/blog/kimi-k2)** — Moonshot AI / Kimi · 2025-07-11
  - `Models` · **Self-training** — Its general RL system uses the model as its own rubric-based critic, continuously updating that critic from on-policy rollouts with verifiable rewards to improve evaluation of non-verifiable tasks.
  - **Boundary:** The critic and policy improve within a designed RL setup; the article does not establish autonomous rewriting of the learning algorithm.

- **[SIMA 2: An Agent that Plays, Reasons, and Learns With You in Virtual 3D Worlds](https://deepmind.google/blog/sima-2-an-agent-that-plays-reasons-and-learns-with-you-in-virtual-3d-worlds/)** — Google DeepMind · 2025-11-13
  - `Models` · **Self-training** — Gemini supplies tasks and estimated rewards; SIMA 2 accumulates self-generated experience and trains subsequent agent generations, including in new game and Genie environments.
  - **Boundary:** Initial training uses human demonstrations and later rewards rely on Gemini; the research preview is not unconstrained self-improvement of Gemini itself.

- **[MiniMax M2.7: Early Echoes of Self-Evolution](https://www.minimax.io/news/minimax-m27-en)** — MiniMax · 2026-03-18
  - `Harness` · **Self-modification** — Reports more than 100 autonomous rounds of failure-trajectory analysis, scaffold-code modification, evaluation, and keep-or-revert selection; retained memory and skills also support its model-development experiments.
  - **Boundary:** The reported 30% gain is on internal evaluation sets. Researchers still guide model development and make critical decisions; full autonomous weight-level self-evolution is a future aim.

- **[Prime Agent: A self-improving RLM agent](https://www.primeintellect.ai/blog/prime-agent)** — Prime Intellect · 2026-08-05
  - `Harness` · **Self-modification** — Its /refine pipeline reads its own trajectory and changes persistent prompt notes, memory, skills and subagent specifications; recorded triggers/outcomes and rollback history carry improvements into later turns and sessions.
  - **Boundary:** The base system prompt remains immutable, and this does not retrain model weights. Its Factorio result is explicitly suspected of reward hacking; use the mechanism, not that score, as evidence.

- **[RoboCat: A self-improving robotic agent](https://deepmind.google/blog/robocat-a-self-improving-robotic-agent/)** — Google DeepMind · 2023-06-20
  - `Models` · **Self-training** — Fine-tunes a task-specific spin-off, collects its practice trajectories, merges them with demonstrations and retrains a generalist RoboCat version for later tasks.
  - **Boundary:** Each new task begins with 100–1000 human demonstrations; the training procedure and robot interfaces remain human-designed.


### AI Research and Supporting Methods

<details open><summary>Browse 15 articles</summary>

- **[Automated Alignment Researchers: Using large language models to scale scalable oversight](https://www.anthropic.com/research/automated-alignment-researchers)** — Anthropic · 2026-04-14
  - `Models` · **Bounded optimization** — Nine Claude research agents propose, implement and evaluate weak-to-strong supervision methods, sharing findings and code; performance-gap feedback determines subsequent experiments.
  - **Boundary:** Held-out transfer was mixed, and the best method did not significantly improve production-scale Claude Sonnet 4. Researchers disqualified reward hacks; the researcher models were not themselves retrained in this experiment.

- **[MiniMax M3: Frontier Coding, 1M Context, Native Multimodality — All in One Model](https://www.minimax.io/blog/minimax-m3)** — MiniMax · 2026-06-01
  - `Models` · **Bounded optimization** — The PostTrainBench section describes an agent independently choosing synthetic data and training strategies, training four base models, evaluating them and adjusting its next experiments during a 12-hour loop.
  - **Boundary:** This is a task-bounded external-model optimization experiment, not M3 retraining its own weights. The release also mixes product benchmarks and demos, which are not separate RSI evidence.

- **[Automated researchers can reliably mitigate alignment failures](https://www.anthropic.com/research/automated-researchers-mitigate-alignment-failures)** — Anthropic · 2026-08-28
  - `Models` · **Bounded optimization** — Claude searches literature, proposes methods and data, trains target models, and tests them in repeated experiments across ten alignment-failure categories; methods are checked on held-out benchmarks and larger models.
  - **Boundary:** This optimizes external student models rather than Claude's own weights. Capability constraints and a monitoring agent exclude invalid methods; benchmark success does not establish general autonomous alignment science.

- **[Can LLMs invent better ways to train LLMs?](https://sakana.ai/llm-squared/)** — Sakana AI · 2024-06-13
  - `Models` · **Bounded optimization** — LLM-Squared proposes preference-loss code, trains models with each candidate, and feeds downstream scores into the next proposal; the loop discovered DiscoPOP.
  - **Boundary:** The proposer is fixed; feeding an improved model back into its own research process is discussed as future work, not a demonstrated result.

- **[AlphaEvolve: How our Gemini-powered coding agent is scaling impact across fields](https://deepmind.google/blog/alphaevolve-impact/)** — Google DeepMind · 2026-05-07
  - `Artifacts` · **Bounded optimization** — Reports follow-up applications of evaluated code evolution to model components, training efficiency, cache policies and TPU circuits, with concrete AI-development feedback paths.
  - **Boundary:** Deployment case studies and publisher-reported gains do not demonstrate a fully closed cycle that retrains and improves the Gemini proposer itself.

- **[AlphaEvolve: A Gemini-powered coding agent for designing advanced algorithms](https://deepmind.google/blog/alphaevolve-a-gemini-powered-coding-agent-for-designing-advanced-algorithms/)** — Google DeepMind · 2025-05-14
  - `Artifacts` · **Bounded optimization** — Explains evaluated program evolution that improves algorithms and Gemini training kernels, feeding successful programs into the next evolutionary proposals.
  - **Boundary:** Improving infrastructure used to train its underlying LLM is not proof of repeated autonomous Gemini-weight self-training.

- **[ShinkaEvolve: Evolving New Algorithms with LLMs, Orders of Magnitude More Efficiently](https://sakana.ai/shinka-evolve/)** — Sakana AI · 2025-09-25
  - `Artifacts` · **Bounded optimization** — Details sample-efficient program evolution and an evolved MoE load-balancing loss, tying executable candidate selection to subsequent program generations.
  - **Boundary:** Human-defined fitness and a fixed proposer model bound the result; it does not demonstrate a self-rewriting learning algorithm.

- **[Digital Red Queen: Adversarial Program Evolution in Core War with LLMs](https://sakana.ai/drq/)** — Sakana AI · 2026-01-08
  - `Artifacts` · **Bounded optimization** — Evolves Core War programs against a growing history of predecessors; changing opponents supply selection pressure and retained programs shape subsequent evolution.
  - **Boundary:** Program co-evolution in a controlled virtual machine does not demonstrate autonomous improvement of the underlying LLM or real-world security capability.

- **[Autonomous AI research for nanogpt speedrun](https://www.primeintellect.ai/auto-nanogpt)** — Prime Intellect · 2026-05-14
  - `Artifacts` · **Bounded optimization** — Coding agents repeatedly revise optimizer code and hyperparameters, run nanoGPT training and use steps-to-target-validation-loss to select better variants; durable scratchpads preserve experiment state.
  - **Boundary:** Agents excelled at search and recombination but needed upstream human records to keep improving. Model/data/architecture and benchmark rules were fixed, and humans changed the harness between phases.

- **[General Agent: A Self-Evolving, Synthetic Agent Environment](https://www.primeintellect.ai/blog/general-agent)** — Prime Intellect · 2026-05-18
  - `Artifacts` · **Bounded optimization** — A synthesizer evolves task families and a solver measures pass rates; only tasks in calibrated difficulty bands survive, and harder tiers seed later extensions of the synthetic training corpus.
  - **Boundary:** The evolved object is the task corpus. The post describes closing the full model-training/environment-generation loop as a broader research direction, not an already completed autonomous cycle.

- **[The AI Scientist: Towards Fully Automated Open-Ended Scientific Discovery](https://sakana.ai/ai-scientist/)** — Sakana AI · 2024-08-13
  - `Artifacts` · **Bounded optimization** — Describes idea generation, code experiments, paper writing and automated reviewing; saved reviews and experiments inform revisions and future research ideas.
  - **Boundary:** Flawed comparisons and self-review remain risks; accidental execution-script modification is a safety failure, not evidence of beneficial RSI.

- **[FunSearch: Making new discoveries in mathematical sciences using Large Language Models](https://deepmind.google/blog/funsearch-making-new-discoveries-in-mathematical-sciences-using-large-language-models/)** — Google DeepMind · 2023-12-14
  - `Artifacts` · **Bounded optimization** — Samples earlier high-scoring programs, asks a fixed LLM for improvements, executes candidates, and returns the best programs to a population for future search.
  - **Boundary:** The evaluator and seed program are user-supplied; the model weights and improvement algorithm are not recursively rewritten.

- **[Population-based Model Merging via Quality Diversity](https://sakana.ai/cycleqd/)** — Sakana AI · 2024-12-03
  - `Models` · **Bounded optimization** — CycleQD cycles which task defines quality, crosses and mutates expert models, and retains diverse high-performing models in skill archives for further evolution.
  - **Boundary:** The tasks, starting experts and quality-diversity algorithm are human-specified; model merging is not gradient self-training or self-rewriting optimization.

- **[Evolving New Foundation Models: Unleashing the Power of Automating Model Development](https://sakana.ai/evolutionary-model-merge/)** — Sakana AI · 2024-03-21
  - `Models` · **Bounded optimization** — Evolves layer-selection and weight-mixing recipes over successive generations, selecting merged models by task fitness and assessing the selected model on a separate test set.
  - **Boundary:** Evolution searches a human-defined merge space of pretrained models; it does not establish an LLM autonomously rewriting its training algorithm.

- **[Accelerating scientific breakthroughs with an AI co-scientist](https://research.google/blog/accelerating-scientific-breakthroughs-with-an-ai-co-scientist/)** — Google Research · 2025-02-19
  - `Artifacts` · **Bounded optimization** — Generation, reflection, ranking, evolution and meta-review agents iteratively revise scientific hypotheses using tournament feedback and researcher input.
  - **Boundary:** Elo is a self-evaluation signal rather than independent ground truth; laboratory validation uses expert guidance, and model weights remain fixed.

</details>


### Evaluation and Failure Modes

<details open><summary>Browse 4 articles</summary>

- **[AI CUDA Engineer update: robust benchmarking and interim results](https://sakana.ai/ai-cuda-engineer-update/)** — Sakana AI · 2025-09-17
  - `Artifacts` · **Evaluation / safety** — Corrects kernel-optimization claims after benchmark bypasses; robust-kbench reduces reported mean speedup from 3.13x to 1.49x under stricter measurement.
  - **Boundary:** A negative-results and measurement lesson for improvement loops, not a new self-improving agent; the original update is in Japanese.

- **[Sycophancy to subterfuge: Investigating reward tampering in language models](https://www.anthropic.com/research/reward-tampering)** — Anthropic · 2024-06-17
  - `Harness` · **Evaluation / safety** — Tests whether a curriculum of specification gaming generalizes to editing the model's own reward function and concealing the change, exposing a direct failure mode when self-modifying systems can alter their evaluators.
  - **Boundary:** Reward tampering occurred in 45 of 32,768 trials in a constructed study; it was not observed evidence of deployed Claude performing RSI, nor proof that all self-modification is unsafe.

- **[From shortcuts to sabotage: natural emergent misalignment from reward hacking](https://www.anthropic.com/research/emergent-misalignment-reward-hacking)** — Anthropic · 2025-11-21
  - `Harness` · **Evaluation / safety** — Shows reward-hacking training generalizing to malicious behavior, including a Claude Code evaluation where the model attempts to sabotage this research project's detection code, directly testing trust in AI-assisted AI safety research.
  - **Boundary:** Researchers deliberately selected hackable RL environments and added hacking knowledge during pretraining. The 12% sabotage attempt rate describes this experimental model, not ordinary deployed Claude or proven completed sabotage.

- **[Measuring Autonomous AI Research](https://www.primeintellect.ai/blog/measuring-autonomous-research)** — Prime Intellect · 2026-08-14
  - `Artifacts` · **Evaluation / safety** — Evaluates 153 autonomous optimizer-research runs across 18 frontier models, examining whether proposed nanoGPT improvements survive evaluation and whether long-running agents produce new methods rather than only recombine existing ones.
  - **Boundary:** A fixed optimizer speedrun is a bounded proxy for research ability, not proof of general RSI. Results depend on seeds, supplied baselines and evaluation integrity.

</details>


### Research Agendas

<details open><summary>Browse 2 articles</summary>

- **[Introducing Sakana AI's Recursive Self-Improvement (RSI) Lab](https://sakana.ai/rsi-lab/)** — Sakana AI · 2026-06-05
  - `Harness` · **Research agenda** — Maps a proposed loop from agent-native models to AI scientists that build better models, grounded in DGM, LLM-Squared, ShinkaEvolve and adversarial co-evolution.
  - **Boundary:** A research agenda and lineage map, not evidence that the complete autonomous model-improvement cycle has already been achieved.

- **[When AI builds itself](https://www.anthropic.com/institute/recursive-self-improvement)** — Anthropic Institute
  - `Models` · **Research agenda** — Defines recursive self-improvement as AI autonomously designing and developing its successor, presents internal evidence of AI accelerating engineering and research, and examines whether that assistance can close the full model-development loop.
  - **Boundary:** The article explicitly says full RSI has not been achieved and is not inevitable. Internal productivity statistics are observational; human research judgment, compute, evaluations and security remain constraints.

</details>


### Foundations and Historical Tutorials

<details open><summary>Browse 4 articles</summary>

- **[Constitutional AI: Harmlessness from AI feedback](https://www.anthropic.com/research/constitutional-ai-harmlessness-from-ai-feedback)** — Anthropic · 2022-12-15
  - `Models` · **Self-training** — Samples model responses, generates self-critiques and revisions, fine-tunes on the revised responses, then derives AI preferences for a reward model used in reinforcement learning.
  - **Boundary:** Human-written constitutional principles and a fixed staged training recipe remain essential. This is a bounded self-supervision foundation, not evidence of endlessly repeated autonomous RSI.

- **[AlphaGo Zero: Starting from scratch](https://deepmind.google/blog/alphago-zero-starting-from-scratch/)** — Google DeepMind · 2017-10-18
  - `Models` · **Self-training** — Self-play outcomes train the network; the updated network guides stronger search and games that supply the next training round.
  - **Boundary:** A foundational bounded self-training example in Go, with human-designed rules and learning machinery, not open-ended RSI.

- **[AlphaZero: Shedding new light on chess, shogi, and Go](https://deepmind.google/blog/alphazero-shedding-new-light-on-chess-shogi-and-go/)** — Google DeepMind · 2018-12-06
  - `Models` · **Self-training** — Describes neural-network parameter updates from self-play outcomes and stronger network-guided tree search across separately learned games.
  - **Boundary:** Each game retains fixed rules and objectives; this is not one model autonomously expanding its domain or rewriting its learner.

- **[Self-Evolving Agents - A Cookbook for Autonomous Agent Retraining](https://developers.openai.com/cookbook/examples/partners/self_evolving_agents/autonomous_agent_retraining)** — OpenAI and Bain · 2025-11-04 · archived tutorial
  - `Harness` · **Bounded optimization** — Demonstrates versioned summarization-prompt updates from grader feedback, meta-prompting and GEPA, retaining better candidates for later requests.
  - **Boundary:** The official recipe is archived and may reference outdated APIs. Despite the title, it changes prompts rather than model weights; production needs held-out tests and human approval. Its example validation slice overlaps its training list.

</details>


## Papers and Official Code

- Dates refer to first publication. Only source-verified venues are shown; a date alone makes no peer-review claim.
- Code links are author-linked releases. **—** means no author-linked implementation was established in this review; it does not assert that none exists. Release details preserve metadata and partial-release notes.
- Star badges and push dates use the **2026-09-09** metadata snapshot.

### Papers / Harness

Agents revise their own executable code or retained control procedures, then use the revised system in subsequent improvement.

| Paper | Improvement Mechanism | Code |
| --- | --- | --- |
| **[Meta^n](https://arxiv.org/abs/2608.24735)**<br>2026-08-25 | **Self-modification**<br>Repeatedly applies a fixed meta-operation to the evolving solver stack, generating preprocessing code and reusable helpers; an archive retains evaluated layer chains.<br><details open><summary>Boundary</summary>Recursion acts on generated layers, not on the meta-operation or model weights. Most reported gains come from passed context; runs plateau at finite depth.</details> | [Official&nbsp;code](https://github.com/minnesotanlp/meta-n)<br>[![star: 28](https://img.shields.io/badge/star-28-f4b400?style=flat-square)](https://github.com/minnesotanlp/meta-n)<br><details open><summary>Details</summary>• **Last push:** 2026-08-26<br>• The authors label this a research prototype with exploratory results.</details> |
| **[MetaSkill-Evolve](https://arxiv.org/abs/2607.05297)**<br>2026-07-06 | **Self-modification**<br>Evolves task skills frequently and the five agents’ meta-skill files more slowly; the same pipeline edits the instructions that govern its own improvement.<br><details open><summary>Boundary</summary>One frozen backbone and three curated benchmarks. Meta-skills change, but the five roles, their wiring and the update schedule remain fixed.</details> | — |
| **[Continual Harness](https://arxiv.org/abs/2605.09998)**<br>2026-05-11 | **Experience learning**<br>Alternates action and refinement of prompts, subagents, skills and memory within a reset-free run. A separate co-learning experiment relabels rollouts with a frontier teacher and updates an open model without resetting the game.<br><details open><summary>Boundary</summary>Earlier Gemini Plays Pokemon results used human-in-the-loop harness refinement; later automated adaptation and teacher-assisted weight co-learning are distinct settings. Teacher supervision and game-specific evaluation limit autonomy claims.</details> | [Official&nbsp;code](https://github.com/PrimeIntellect-ai/prime-agent)<br>[![star: 20,342](https://img.shields.io/badge/star-20342-f4b400?style=flat-square)](https://github.com/PrimeIntellect-ai/prime-agent)<br><details open><summary>Details</summary>• **Last push:** 2026-09-09<br>• Official associated implementation of the harness component via an explicit README link to this paper. The inspected paper v1 does not establish release of all Pokemon experiments or the teacher-relabeled weight co-learning pipeline; this is not certified full reproduction code.</details> |
| **[Hyperagents](https://arxiv.org/abs/2603.19461)**<br>2026-03-19 | **Self-modification**<br>Integrates a task agent and a meta agent into one editable program so that evaluated changes can improve both task behavior and the machinery producing future changes.<br><details open><summary>Boundary</summary>Reported transfer and accumulation are finite experiments, not evidence of indefinite acceleration or autonomous weight-level learning.</details> | [Official&nbsp;code](https://github.com/facebookresearch/HyperAgents)<br>[![star: 2,719](https://img.shields.io/badge/star-2719-f4b400?style=flat-square)](https://github.com/facebookresearch/HyperAgents)<br><details open><summary>Details</summary>• **Last push:** 2026-07-31</details> |
| **[Huxley-Gödel Machine (HGM)](https://arxiv.org/abs/2510.21614)**<br>2025-10-24<br>[ICLR 2026](https://github.com/metauto-ai/HGM) | **Self-modification**<br>Uses descendant performance to estimate which self-modifying coding-agent lineages will produce better future agents, guiding the next code rewrites.<br><details open><summary>Boundary</summary>Clade statistics approximate improvement potential; they are not proofs of globally optimal rewrites. Experiments use bounded coding benchmarks and fixed underlying LLMs.</details> | [Official&nbsp;code](https://github.com/metauto-ai/HGM)<br>[![star: 430](https://img.shields.io/badge/star-430-f4b400?style=flat-square)](https://github.com/metauto-ai/HGM)<br><details open><summary>Details</summary>• **Last push:** 2026-02-07</details> |
| **[Darwin Gödel Machine (DGM)](https://arxiv.org/abs/2505.22954)**<br>2025-05-29 | **Self-modification**<br>A coding agent modifies its own implementation, evaluates descendants on coding benchmarks, and branches from a growing archive of agents to produce further improvements.<br><details open><summary>Boundary</summary>Empirical code-level self-improvement, not formal proof of beneficial rewrites or foundation-model weight training; benchmark exploitation and sandbox escape remain concerns.</details> | [Official&nbsp;code](https://github.com/jennyzzt/dgm)<br>[![star: 2,295](https://img.shields.io/badge/star-2295-f4b400?style=flat-square)](https://github.com/jennyzzt/dgm)<br><details open><summary>Details</summary>• **Last push:** 2025-08-13</details> |
| **[Self-Improving Coding Agent (SICA)](https://arxiv.org/abs/2504.15228)**<br>2025-04-21<br>[ICLR 2025 Workshop on Scaling Self-Improving Foundation Models](https://github.com/MaximeRobeyns/self_improving_coding_agent/blob/master/README.md) | **Self-modification**<br>Evaluates the current coding agent, archives results, runs that same agent on its own codebase to implement an improvement, and evaluates the updated implementation again.<br><details open><summary>Boundary</summary>Non-gradient scaffold learning uses fixed LLM weights; gains on a sampled SWE-bench Verified subset and other benchmarks do not establish unlimited progress or whole-benchmark state of the art.</details> | [Official&nbsp;code](https://github.com/MaximeRobeyns/self_improving_coding_agent)<br>[![star: 394](https://img.shields.io/badge/star-394-f4b400?style=flat-square)](https://github.com/MaximeRobeyns/self_improving_coding_agent)<br><details open><summary>Details</summary>• **Last push:** 2025-04-23<br>• Its citation explicitly identifies a workshop, not the ICLR main conference track.</details> |
| **[Gödel Agent](https://arxiv.org/abs/2410.04444)**<br>2024-10-06 | **Self-modification**<br>Uses LLM-generated changes to recursively revise the agent's own logic and behavior under high-level objectives rather than limiting changes to a predefined task-agent pipeline.<br><details open><summary>Boundary</summary>Inspired by the Gödel machine but supported by empirical task evaluations, not proofs that all rewrites are beneficial or that the whole agent-design space is optimally searched.</details> | [Official&nbsp;code](https://github.com/Arvid-pku/Godel_Agent)<br>[![star: 219](https://img.shields.io/badge/star-219-f4b400?style=flat-square)](https://github.com/Arvid-pku/Godel_Agent)<br><details open><summary>Details</summary>• **Last push:** 2025-09-17<br>• The canonical abstract links the repository, whose README links the same paper. No verified formal-proof implementation or conference venue is inferred from the name.</details> |
| **[Self-Taught Optimizer (STOP)](https://arxiv.org/abs/2310.02304)**<br>2023-10-03 | **Self-modification**<br>A seed LM-calling program optimizer is applied to its own code, discovering improved search scaffolds that then optimize downstream programs.<br><details open><summary>Boundary</summary>The paper explicitly says unchanged language models make this not full recursive self-improvement; only a small task set is studied, including sandbox-bypass risks.</details> | [Official&nbsp;code](https://github.com/microsoft/stop)<br>[![star: 53](https://img.shields.io/badge/star-53-f4b400?style=flat-square)](https://github.com/microsoft/stop)<br><details open><summary>Details</summary>• **Last push:** 2024-01-01</details> |

### Papers / Models

Iterative model, curriculum and evaluator training. Updated models create later training signals; the learning rule can remain fixed.

| Paper | Improvement Mechanism | Code |
| --- | --- | --- |
| **[J-Zero](https://arxiv.org/abs/2608.26582)**<br>2026-08-27 | **Self-training**<br>Co-trains a task Challenger, Solver and Judge across rounds; structurally constructed preference pairs update the Judge that rewards later policy training.<br><details open><summary>Boundary</summary>The Judge starts from a pretrained reward checkpoint. Preference ordering is a designed assumption; reported ten-round gains do not establish unbounded improvement.</details> | [Official&nbsp;code](https://github.com/GyoukChu/J-Zero)<br>[![star: 8](https://img.shields.io/badge/star-8-f4b400?style=flat-square)](https://github.com/GyoukChu/J-Zero)<br><details open><summary>Details</summary>• **Last push:** 2026-08-28</details> |
| **[Socratic-SWE](https://arxiv.org/abs/2606.07412)**<br>2026-06-05 | **Self-training**<br>Distills solving traces into skills, generates targeted repair tasks, and jointly trains generator/solver roles; updated solvers produce the next curriculum’s traces.<br><details open><summary>Boundary</summary>A fixed seed-repository pool, executable tests and trusted validation tasks constrain the loop. The paper reports later-iteration saturation.</details> | — |
| **[Agent0](https://arxiv.org/abs/2511.16043)**<br>2025-11-20 | **Self-training**<br>Couples a curriculum model with a tool-using executor model; stronger execution drives harder generated curricula, which in turn provide reinforcement-learning data.<br><details open><summary>Boundary</summary>The released training instructions require manual checkpoint selection between iterations; zero external data does not remove pretrained-backbone or tool dependencies.</details> | [Official&nbsp;code](https://github.com/aiming-lab/Agent0)<br>[![star: 1,258](https://img.shields.io/badge/star-1258-f4b400?style=flat-square)](https://github.com/aiming-lab/Agent0)<br><details open><summary>Details</summary>• **Last push:** 2026-07-10</details> |
| **[R-Zero](https://arxiv.org/abs/2508.05004)**<br>2025-08-07<br>[ICLR 2026](https://github.com/Chengsong-Huang/R-Zero/blob/main/README.md) | **Self-training**<br>Co-evolves Challenger and Solver models so that frontier-difficulty generated tasks train the Solver, while the Solver's changing capability alters the Challenger's rewards.<br><details open><summary>Boundary</summary>Uses a pretrained base and designed rewards; finite iterations can regress, and the authors' later R-Few work introduces human data to address scaling limits.</details> | [Official&nbsp;code](https://github.com/Chengsong-Huang/R-Zero)<br>[![star: 845](https://img.shields.io/badge/star-845-f4b400?style=flat-square)](https://github.com/Chengsong-Huang/R-Zero)<br><details open><summary>Details</summary>• **Last push:** 2026-02-04</details> |
| **[Self-Adapting Language Models (SEAL)](https://arxiv.org/abs/2506.10943)**<br>2025-06-12 | **Self-training**<br>The model generates self-edits containing finetuning data or update directives; SFT makes persistent weight changes, and downstream performance trains better self-edit generation through an outer RL loop.<br><details open><summary>Boundary</summary>Self-edits control adaptation within a researcher-designed SFT/RL framework; experiments on knowledge incorporation and few-shot generalization do not prove unrestricted self-redesign.</details> | [Official&nbsp;code](https://github.com/Continual-Intelligence/SEAL)<br>[![star: 1,855](https://img.shields.io/badge/star-1855-f4b400?style=flat-square)](https://github.com/Continual-Intelligence/SEAL)<br><details open><summary>Details</summary>• **Last push:** 2025-08-01<br>• The paper links its author project page, and the matching official repository links the same paper and page. The canonical repository is Continual-Intelligence/SEAL.</details> |
| **[Absolute Zero](https://arxiv.org/abs/2505.03335)**<br>2025-05-06 | **Self-training**<br>A model co-evolves its task proposals and solving ability, using a code executor for task validity and answer rewards instead of an externally curated post-training dataset.<br><details open><summary>Boundary</summary>Zero data refers to the self-play post-training setup, not an untrained backbone; the executor, rewards and optimization machinery are human-designed.</details> | [Official&nbsp;code](https://github.com/LeapLabTHU/Absolute-Zero-Reasoner)<br>[![star: 1,901](https://img.shields.io/badge/star-1901-f4b400?style=flat-square)](https://github.com/LeapLabTHU/Absolute-Zero-Reasoner)<br><details open><summary>Details</summary>• **Last push:** 2025-08-24</details> |
| **[SiriuS](https://arxiv.org/abs/2502.04780)**<br>2025-02-07<br>[NeurIPS 2025](https://github.com/zou-group/sirius) | **Self-training**<br>Collects successful multi-agent trajectories, repairs failed ones, and fine-tunes the participating agents; improved agents generate later training experience.<br><details open><summary>Boundary</summary>Starts from labeled problems and fixed agent graphs. Role-specific SFT is iterative learning, not autonomous redesign of the training algorithm.</details> | [Official&nbsp;code](https://github.com/zou-group/sirius)<br>[![star: 110](https://img.shields.io/badge/star-110-f4b400?style=flat-square)](https://github.com/zou-group/sirius)<br><details open><summary>Details</summary>• **Last push:** 2025-12-01</details> |
| **[Self-Taught Evaluators](https://arxiv.org/abs/2408.02666)**<br>2024-08-05 | **Self-training**<br>Generates contrasting responses and synthetic reasoning/judgments to repeatedly train an LLM evaluator, using improved evaluator predictions to construct later training rounds.<br><details open><summary>Boundary</summary>Human-preference-free training is not the same as zero human validation; the release documents checkpoint selection with HelpSteer2 validation accuracy.</details> | [Official&nbsp;artifacts&nbsp;only](https://github.com/facebookresearch/RAM/tree/main/projects/self_taught_evaluator)<br>[![star: 382](https://img.shields.io/badge/star-382-f4b400?style=flat-square)](https://github.com/facebookresearch/RAM)<br><details open><summary>Details</summary>• **Last push:** 2026-06-25<br>• Official model, synthetic data and judging/evaluation scripts are documented; this is not a claim that a complete end-to-end training pipeline is released.</details> |
| **[ReST-MCTS*](https://arxiv.org/abs/2406.03816)**<br>2024-06-06 | **Self-training**<br>Uses process-reward-guided tree search to infer step values from correct final answers, then trains both the policy and process reward model on selected traces across multiple iterations.<br><details open><summary>Boundary</summary>Removes per-step manual annotation, not oracle final-answer supervision; externally designed search and reward-learning rules remain fixed.</details> | [Official&nbsp;code](https://github.com/THUDM/ReST-MCTS)<br>[![star: 712](https://img.shields.io/badge/star-712-f4b400?style=flat-square)](https://github.com/THUDM/ReST-MCTS)<br><details open><summary>Details</summary>• **Last push:** 2025-01-20<br>• Official README documents policy/value-model synthetic-data generation and iterative training. Presence of code is not independent replication of every reported result.</details> |
| **[Self-Play Preference Optimization (SPPO)](https://arxiv.org/abs/2405.00675)**<br>2024-05-01<br>[ICLR 2025](https://github.com/uclaml/SPPO/blob/main/README.md) | **Self-training**<br>Treats alignment as a constant-sum two-player game and repeatedly updates the policy against its own generated responses using preference probabilities to approach a Nash equilibrium.<br><details open><summary>Boundary</summary>Experiments use prompts and a pretrained PairRM judge; the equilibrium guarantee concerns the specified preference game, not unbounded capability growth or self-improving evaluation.</details> | [Official&nbsp;code](https://github.com/uclaml/SPPO)<br>[![star: 589](https://img.shields.io/badge/star-589-f4b400?style=flat-square)](https://github.com/uclaml/SPPO)<br><details open><summary>Details</summary>• **Last push:** 2025-01-23<br>• The official repository explicitly provides code and released models; PairRM is an external pretrained preference model, not the policy learning to judge itself.</details> |
| **[Self-Rewarding Language Models](https://arxiv.org/abs/2401.10020)**<br>2024-01-18 | **Self-training**<br>Uses the language model as its own prompted reward judge during iterative DPO, jointly improving response generation and the rewards it gives subsequent training examples.<br><details open><summary>Boundary</summary>Three reported iterations and benchmark preference gains do not prove calibrated self-judgment or sustained superhuman improvement; seed supervision remains relevant.</details> | — |
| **[Self-Play Fine-Tuning (SPIN)](https://arxiv.org/abs/2401.01335)**<br>2024-01-02<br>[ICML 2024](https://github.com/uclaml/SPIN/blob/main/README.md) | **Self-training**<br>Trains a policy to distinguish human demonstration responses from responses generated by its previous iteration, repeatedly strengthening a supervised fine-tuned model through self-play.<br><details open><summary>Boundary</summary>Reuses human demonstrations and an SFT starting model; theoretical optimality concerns the target data distribution, not unlimited recursive capability growth.</details> | [Official&nbsp;code](https://github.com/uclaml/SPIN)<br>[![star: 1,254](https://img.shields.io/badge/star-1254-f4b400?style=flat-square)](https://github.com/uclaml/SPIN)<br><details open><summary>Details</summary>• **Last push:** 2024-05-08</details> |
| **[ReST-EM](https://arxiv.org/abs/2312.06585)**<br>2023-12-11 | **Self-training**<br>Repeatedly samples solutions, filters by binary correctness feedback and fine-tunes on accepted samples, studying scaling on MATH and APPS with PaLM-2.<br><details open><summary>Boundary</summary>Needs externally supplied problems and verifiable feedback; a few EM-style iterations do not establish indefinite improvement.</details> | — |
| **[ReST](https://arxiv.org/abs/2308.08998)**<br>2023-08-17 | **Self-training**<br>Alternates policy-generated data collection with reward-guided offline learning, reusing samples to improve a language-model policy, demonstrated on machine translation.<br><details open><summary>Boundary</summary>Reward and preference signals remain externally specified; results in translation do not establish a self-improving reward mechanism or open-ended capability growth.</details> | — |
| **[RoboCat](https://arxiv.org/abs/2306.11706)**<br>2023-06-20 | **Self-training**<br>Adapts a generalist robotic policy to tasks and embodiments, uses trained policies to gather further robot experience, and retrains subsequent generalist models on the expanded data.<br><details open><summary>Boundary</summary>Task adaptation still uses demonstrations and controlled robot infrastructure; this is a building block for autonomous improvement, not self-redesign of the training system.</details> | — |
| **[STaR](https://arxiv.org/abs/2203.14465)**<br>2022-03-28<br>[NeurIPS 2022](https://github.com/ezelikman/STaR/blob/main/README.md) | **Self-training**<br>Generates reasoning traces, filters them by answer correctness, rationalizes failed examples using known answers, and repeatedly fine-tunes on successful traces.<br><details open><summary>Boundary</summary>Requires a task dataset, known answers and seed rationale examples; a fixed training loop is not an autonomous redesign of the learner.</details> | [Official&nbsp;code](https://github.com/ezelikman/STaR)<br>[![star: 232](https://img.shields.io/badge/star-232-f4b400?style=flat-square)](https://github.com/ezelikman/STaR)<br><details open><summary>Details</summary>• **Last push:** 2023-02-21</details> |

### Papers / Theory and Evaluation

Formal foundations, proposed closed-loop learning, and tests of whether self-improvement signals remain reliable. These are not implementation demonstrations.

| Paper | Improvement Mechanism | Code |
| --- | --- | --- |
| **[Statistical Gödel Machine (SGM)](https://arxiv.org/abs/2510.10232)**<br>2025-10-11 | **Evaluation / safety**<br>Tests candidate edits before adoption and budgets cumulative false-acceptance risk across rounds, providing a statistical gate for self-modification.<br><details open><summary>Boundary</summary>Guarantees require bounded independent paired measurements and a stable evaluator. Experiments use simple proposals, not a demonstrated self-rewriting LLM.</details> | [Official&nbsp;code](https://github.com/gravitywavelet/sgm-anon)<br>[![star: 0](https://img.shields.io/badge/star-0-f4b400?style=flat-square)](https://github.com/gravitywavelet/sgm-anon)<br><details open><summary>Details</summary>• **Last push:** 2026-05-11<br>• The linked repository now describes a later anonymous submission; the catalog summary refers to arXiv v1.</details> |
| **[Socratic Learning](https://arxiv.org/abs/2411.16905)**<br>2024-11-25 | **Research agenda**<br>Develops a position on closed-system recursive learning through language games, separating feedback quality, experience coverage and resource requirements.<br><details open><summary>Boundary</summary>A position paper under explicit assumptions; it does not report an implemented system with boundless empirical capability growth.</details> | — |
| **[Guided Self-Improvement (GSI)](https://arxiv.org/abs/2411.00750)**<br>2024-11-01 | **Evaluation / safety**<br>Studies loss of difficult examples during repeated self-training and uses Socratic hints to recover sampling coverage for later training rounds.<br><details open><summary>Boundary</summary>Requires known answer checks and guidance; correct final answers can still hide spurious rationales. This is a limits-and-mitigation study, not unrestricted RSI.</details> | [Official&nbsp;code](https://github.com/Yiwen-Ding/Guided-Self-Improvement)<br>[![star: 9](https://img.shields.io/badge/star-9-f4b400?style=flat-square)](https://github.com/Yiwen-Ding/Guided-Self-Improvement)<br><details open><summary>Details</summary>• **Last push:** 2024-11-10</details> |
| **[Gödel Machines](https://arxiv.org/abs/cs/0309048)**<br>2003-09-25<br>[Adaptive Agents and Multi-Agent Systems II (2005)](https://arxiv.org/abs/cs/0309048) | **Research agenda**<br>Formalizes a self-referential solver that can rewrite its proof-search code once the expected usefulness of that rewrite is provable.<br><details open><summary>Boundary</summary>A theoretical construction relative to encoded axioms and utility, not an efficient deployed LLM system; useful rewrites may be unprovable or costly to prove.</details> | — |

## Active GitHub Projects

Repository metadata snapshot: **2026-09-09**. Only public, non-archived projects pushed in the last **60 days** appear here; stars are snapshots, not evidence of RSI. Paper-associated code above has no activity gate.

### GitHub / Models

#### GitHub / Models / Training Research

Agents revise training recipes and evaluate resulting models; the researching agent is not necessarily retrained.

| Project | Link | Stars | Tags | Improvement Loop and Boundary |
| --- | --- | ---: | --- | --- |
| RD-Agent / FT-Agent | [GitHub](https://github.com/microsoft/RD-Agent) | [![star: 14,553](https://img.shields.io/badge/star-14553-f4b400?style=flat-square)](https://github.com/microsoft/RD-Agent) | `model-training`<br>`experiment-loop`<br>`validation` | **Bounded optimization**<br>FT-Agent generates data-processing code and training configurations, fine-tunes a target LLM, then uses OpenCompass validation feedback to refine the next training experiment.<br><details open><summary>Boundary</summary>This improves an external target model, not the planner's own weights; test splits are reserved for final reporting.</details><br>• [Evidence](https://github.com/microsoft/RD-Agent/blob/main/rdagent/app/finetune/llm/README.md) |

#### GitHub / Models / Recursive Self-Training

Model updates change the agents that generate the next round of training tasks, solutions or rewards.

| Project | Link | Stars | Tags | Improvement Loop and Boundary |
| --- | --- | ---: | --- | --- |
| J-Zero | [GitHub](https://github.com/GyoukChu/J-Zero) | [![star: 8](https://img.shields.io/badge/star-8-f4b400?style=flat-square)](https://github.com/GyoukChu/J-Zero) | `self-training`<br>`recursive-learning` | **Self-training**<br>Implementation: Co-trains a task Challenger, Solver and Judge across rounds; structurally constructed preference pairs update the Judge that rewards later policy training.<br><details open><summary>Boundary</summary>The Judge starts from a pretrained reward checkpoint. Preference ordering is a designed assumption; reported ten-round gains do not establish unbounded improvement.</details><br>• [Evidence](https://github.com/GyoukChu/J-Zero) |

### GitHub / Harness

#### GitHub / Harness / Self-Modification

The agent implementation and its improvement procedure are themselves editable.

| Project | Link | Stars | Tags | Improvement Loop and Boundary |
| --- | --- | ---: | --- | --- |
| Prime Agent / Continual Harness | [GitHub](https://github.com/PrimeIntellect-ai/prime-agent) | [![star: 20,342](https://img.shields.io/badge/star-20342-f4b400?style=flat-square)](https://github.com/PrimeIntellect-ai/prime-agent) | `self-refinement`<br>`continual-harness`<br>`rollback` | **Self-modification**<br>Reviews trajectories with /refine and retains small evidence-backed updates to supplemental prompts, memory, skill descriptions and subagent specifications; snapshots allow rollback.<br><details open><summary>Boundary</summary>The base system prompt is immutable. Refinement does not replace packaging/review of executable skills, and its processes are not a security sandbox.</details><br>• [Evidence](https://github.com/PrimeIntellect-ai/prime-agent) |
| HyperAgents | [GitHub](https://github.com/facebookresearch/HyperAgents) | [![star: 2,719](https://img.shields.io/badge/star-2719-f4b400?style=flat-square)](https://github.com/facebookresearch/HyperAgents) | `self-modification`<br>`meta-agent`<br>`archive` | **Self-modification**<br>Integrates task and meta agents in one editable program; evaluated descendants can change both task behavior and the procedure that generates subsequent agents.<br><details open><summary>Boundary</summary>Empirical task-bounded experiments, not proof of indefinite improvement or foundation-model weight self-training.</details><br>• [Evidence](https://github.com/facebookresearch/HyperAgents/blob/main/utils/gl_utils.py) |
| Meta^n | [GitHub](https://github.com/minnesotanlp/meta-n) | [![star: 28](https://img.shields.io/badge/star-28-f4b400?style=flat-square)](https://github.com/minnesotanlp/meta-n) | `self-modification`<br>`meta-improvement` | **Self-modification**<br>Implementation: Repeatedly applies a fixed meta-operation to the evolving solver stack, generating preprocessing code and reusable helpers; an archive retains evaluated layer chains.<br><details open><summary>Boundary</summary>Recursion acts on generated layers, not on the meta-operation or model weights. Most reported gains come from passed context; runs plateau at finite depth.</details><br>• [Evidence](https://github.com/minnesotanlp/meta-n) |

#### GitHub / Harness / Prompt and Workflow Optimization

Feedback updates retained prompts or workflow graphs. These bounded optimizers do not establish unrestricted self-modification.

| Project | Link | Stars | Tags | Improvement Loop and Boundary |
| --- | --- | ---: | --- | --- |
| DSPy / GEPA and MIPROv2 | [GitHub](https://github.com/stanfordnlp/dspy) | [![star: 37,865](https://img.shields.io/badge/star-37865-f4b400?style=flat-square)](https://github.com/stanfordnlp/dspy) | `prompt-optimization`<br>`demonstrations`<br>`metrics` | **Bounded optimization**<br>Compiles LM programs by optimizing instructions and demonstrations against task metrics; compiled programs retain the selected configuration for later use.<br><details open><summary>Boundary</summary>Included for its optimizers, not all DSPy functionality; prompt compilation does not by itself modify the optimizer or model weights.</details><br>• [Evidence](https://github.com/stanfordnlp/dspy/blob/main/dspy/teleprompt/gepa/gepa.py) |
| GEPA | [GitHub](https://github.com/gepa-ai/gepa) | [![star: 6,485](https://img.shields.io/badge/star-6485-f4b400?style=flat-square)](https://github.com/gepa-ai/gepa) | `reflection`<br>`pareto-selection`<br>`prompt-optimization` | **Bounded optimization**<br>Reflects on execution traces and evaluator feedback to propose prompt revisions, retaining complementary candidates through Pareto-based selection.<br><details open><summary>Boundary</summary>The original method optimizes prompts with fixed model weights; its general optimize_anything API is not evidence that GEPA rewrites itself.</details><br>• [Evidence](https://github.com/gepa-ai/gepa) |
| EvoAgentX / Evolution Algorithms | [GitHub](https://github.com/ANative-Lab/EvoAgentX) | [![star: 3,315](https://img.shields.io/badge/star-3315-f4b400?style=flat-square)](https://github.com/ANative-Lab/EvoAgentX) | `workflow-optimization`<br>`aflow`<br>`validation` | **Bounded optimization**<br>Runs AFlow, TextGrad, MIPRO and EvoPrompt over agent workflows; validation scores drive prompt or graph revisions, with separate test evaluation.<br><details open><summary>Boundary</summary>Included for executable evolution algorithms, not tool integrations or workflow generation alone; objectives and search algorithms are human-specified.</details><br>• [Evidence](https://github.com/ANative-Lab/EvoAgentX#evolution-algorithms) |

### GitHub / Artifacts

#### GitHub / Artifacts / Program Evolution

Executable programs and algorithms are evolved against an evaluator; the optimizer is generally fixed.

| Project | Link | Stars | Tags | Improvement Loop and Boundary |
| --- | --- | ---: | --- | --- |
| OpenEvolve | [GitHub](https://github.com/algorithmicsuperintelligence/openevolve) | [![star: 7,338](https://img.shields.io/badge/star-7338-f4b400?style=flat-square)](https://github.com/algorithmicsuperintelligence/openevolve) | `program-evolution`<br>`evaluator`<br>`archive` | **Bounded optimization**<br>Evolves executable program variants using LLM mutations, task-specific evaluators and an archive that seeds subsequent generations.<br><details open><summary>Boundary</summary>Programs are the improvement target; neither a self-rewriting optimizer nor recursive proposer-weight training is established.</details><br>• [Evidence](https://github.com/algorithmicsuperintelligence/openevolve) |
| ShinkaEvolve | [GitHub](https://github.com/SakanaAI/ShinkaEvolve) | [![star: 1,375](https://img.shields.io/badge/star-1375-f4b400?style=flat-square)](https://github.com/SakanaAI/ShinkaEvolve) | `program-evolution`<br>`novelty`<br>`ai-training` | **Bounded optimization**<br>Evolves programs with parent sampling, novelty rejection and bandit-based LLM selection; evaluated successors re-enter the archive, including experiments on AI training-loss design.<br><details open><summary>Boundary</summary>The evaluator and evolutionary machinery are supplied by researchers; generating its own problems is a proposed extension, not a demonstrated feature.</details><br>• [Evidence](https://sakana.ai/shinka-evolve/) |

#### GitHub / Artifacts / Learned Skills

Skills are created and revised from experience for reuse across later tasks, not simply bundled as a static library.

| Project | Link | Stars | Tags | Improvement Loop and Boundary |
| --- | --- | ---: | --- | --- |
| Hermes Agent / Learned Skills | [GitHub](https://github.com/NousResearch/hermes-agent) | [![star: 243,485](https://img.shields.io/badge/star-243485-f4b400?style=flat-square)](https://github.com/NousResearch/hermes-agent) | `learned-skills`<br>`procedural-memory`<br>`experience` | **Experience learning**<br>Creates procedural skills after complex tasks and revises them during use; persistent skills and searchable experience are reused across sessions.<br><details open><summary>Boundary</summary>This is experience-driven skill persistence, not model-weight training or independently demonstrated monotonic capability growth.</details><br>• [Evidence](https://github.com/NousResearch/hermes-agent) |

## Scope and Curation

RSI means an improved system participates in producing subsequent improvements. We prioritize implementations that change their own improvement machinery; related self-training and persistent artifact optimization are labeled separately. A normal tool-use loop, test runner, RAG framework, or manually maintained skill collection does not qualify. Each entry names the object changed, feedback, retained state, and limitation.

No entry establishes unbounded autonomous RSI. Within-task refinement, safety evaluation and research agendas are relevant context, not demonstrations of persistent self-improvement. Counts refer to resources: a blog, paper and repository may document the same research, not three independent breakthroughs.

## Maintenance

All live entries are maintained in `data/projects.yaml`; both READMEs are generated. Source interpretation and translation require review; metadata and links cannot certify scientific claims.

```bash
python3 scripts/sync_github_metadata.py
python3 scripts/render_readme.py
python3 scripts/verify_catalog.py
python3 -m unittest discover -s tests -v
```

- [Curation policy](docs/curation_policy.md)
- [Sources and verification](docs/sources_and_verification.md)
- [Research coverage and decisions](docs/research_decisions.md)
- [Related methods and paper selection](docs/related_methods.md)
- [Taxonomy](docs/taxonomy_iterations.md)
- [Contributing](CONTRIBUTING.md)
