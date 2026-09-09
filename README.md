# Awesome RSI

An evidence-led Recursive Self-Improvement (RSI) research map: first-party model-company blogs first, then papers with official code links, and active GitHub implementations across Models, Harness and Artifacts.

[English](./README.md) | [中文](./README_zh.md)

**31 first-party blog posts · 37 research papers · 9 active GitHub projects**

## Contents

- [Category Overview](#category-overview)
- [Company Research Blogs](#company-research-blogs)
  - [Mechanisms and Results](#mechanisms-and-results)
  - [Evaluation and Failure Modes](#evaluation-and-failure-modes)
  - [Research Agendas](#research-agendas)
  - [Foundations and Historical Tutorials](#foundations-and-historical-tutorials)
- [Papers and Official Code](#papers-and-official-code)
  - [Models](#papers--models)
  - [Harness](#papers--harness)
  - [Artifacts](#papers--artifacts)
- [Active GitHub Projects](#active-github-projects)
  - [Models](#models)
  - [Harness](#harness)
  - [Artifacts](#artifacts)
- [Scope and Curation](#scope-and-curation)
- [Maintenance](#maintenance)

## Category Overview

| Category | Resource | Entries |
| --- | --- | ---: |
| [Mechanisms and Results](#mechanisms-and-results) | Blog | 21 |
| [Evaluation and Failure Modes](#evaluation-and-failure-modes) | Blog | 4 |
| [Research Agendas](#research-agendas) | Blog | 2 |
| [Foundations and Historical Tutorials](#foundations-and-historical-tutorials) | Blog | 4 |
| [Papers / Models](#papers--models) | Paper | 14 |
| [Papers / Harness](#papers--harness) | Paper | 14 |
| [Papers / Artifacts](#papers--artifacts) | Paper | 9 |
| [Models / Training Research](#models--training-research) | GitHub project | 1 |
| [Harness / Self-Modification](#harness--self-modification) | GitHub project | 2 |
| [Harness / Prompt and Workflow Optimization](#harness--prompt-and-workflow-optimization) | GitHub project | 3 |
| [Artifacts / Program Evolution](#artifacts--program-evolution) | GitHub project | 2 |
| [Artifacts / Learned Skills](#artifacts--learned-skills) | GitHub project | 1 |
| **Total** |  | **77** |

## Company Research Blogs

Start here: first-party technical accounts from model builders and specialist AI research labs. Mechanisms, failures, agendas and historical foundations are separated; publisher claims are not independent replications.

### Mechanisms and Results

- **[The Darwin Godel Machine: AI that improves itself by rewriting its own code](https://sakana.ai/dgm/)** — Sakana AI · 2025-05-30
  - **Target:** `Harness` · Self-modification
  - **Loop:** Describes an agent that rewrites its tools and workflows, evaluates descendants on coding benchmarks, and branches from a growing archive to improve again.
  - **Boundary:** Foundation-model training is future work; the article documents reward hacking and supervised sandbox limits.

- **[Kimi K2: Open Agentic Intelligence](https://www.kimi.com/en/blog/kimi-k2)** — Moonshot AI / Kimi · date not verified
  - **Target:** `Models` · Self-training
  - **Loop:** Its general RL system uses the model as its own rubric-based critic, continuously updating that critic from on-policy rollouts with verifiable rewards to improve evaluation of non-verifiable tasks.
  - **Boundary:** The post documents bounded policy-and-critic training, not autonomous rewriting of the learner. Data synthesis and general agent demos alone are not the inclusion rationale; the original visible date is unknown.

- **[SIMA 2: An Agent that Plays, Reasons, and Learns With You in Virtual 3D Worlds](https://deepmind.google/blog/sima-2-an-agent-that-plays-reasons-and-learns-with-you-in-virtual-3d-worlds/)** — Google DeepMind · 2025-11-13
  - **Target:** `Models` · Self-training
  - **Loop:** Gemini supplies tasks and estimated rewards; SIMA 2 accumulates self-generated experience and trains subsequent agent generations, including in new game and Genie environments.
  - **Boundary:** Initial training uses human demonstrations and later rewards rely on Gemini; the research preview is not unconstrained self-improvement of Gemini itself.

- **[MiniMax M2.7: Early Echoes of Self-Evolution](https://www.minimax.io/news/minimax-m27-en)** — MiniMax · 2026-03-18
  - **Target:** `Harness` · Self-modification
  - **Loop:** Reports more than 100 autonomous rounds of failure-trajectory analysis, scaffold-code modification, evaluation, and keep-or-revert selection; retained memory and skills also support its model-development experiments.
  - **Boundary:** The reported 30% gain is on internal evaluation sets. Researchers still guide model development and make critical decisions; full autonomous weight-level self-evolution is a future aim.

- **[Automated Alignment Researchers: Using large language models to scale scalable oversight](https://www.anthropic.com/research/automated-alignment-researchers)** — Anthropic · 2026-04-14
  - **Target:** `Models` · Bounded optimization
  - **Loop:** Nine Claude research agents propose, implement and evaluate weak-to-strong supervision methods, sharing findings and code; performance-gap feedback determines subsequent experiments.
  - **Boundary:** Held-out transfer was mixed, and the best method did not significantly improve production-scale Claude Sonnet 4. Researchers disqualified reward hacks; the researcher models were not themselves retrained in this experiment.

- **[MiniMax M3: Frontier Coding, 1M Context, Native Multimodality — All in One Model](https://www.minimax.io/blog/minimax-m3)** — MiniMax · 2026-06-01
  - **Target:** `Models` · Bounded optimization
  - **Loop:** The PostTrainBench section describes an agent independently choosing synthetic data and training strategies, training four base models, evaluating them and adjusting its next experiments during a 12-hour loop.
  - **Boundary:** This is a task-bounded external-model optimization experiment, not M3 retraining its own weights. The release also mixes product benchmarks and demos, which are not separate RSI evidence.

- **[Automated researchers can reliably mitigate alignment failures](https://www.anthropic.com/research/automated-researchers-mitigate-alignment-failures)** — Anthropic · 2026-08-28
  - **Target:** `Models` · Bounded optimization
  - **Loop:** Claude searches literature, proposes methods and data, trains target models, and tests them in repeated experiments across ten alignment-failure categories; methods are checked on held-out benchmarks and larger models.
  - **Boundary:** This optimizes external student models rather than Claude's own weights. Capability constraints and a monitoring agent exclude invalid methods; benchmark success does not establish general autonomous alignment science.

- **[Can LLMs invent better ways to train LLMs?](https://sakana.ai/llm-squared/)** — Sakana AI · 2024-06-13
  - **Target:** `Models` · Bounded optimization
  - **Loop:** LLM-Squared proposes preference-loss code, trains models with each candidate, and feeds downstream scores into the next proposal; the loop discovered DiscoPOP.
  - **Boundary:** The proposer is fixed; feeding an improved model back into its own research process is discussed as future work, not a demonstrated result.

- **[AlphaEvolve: How our Gemini-powered coding agent is scaling impact across fields](https://deepmind.google/blog/alphaevolve-impact/)** — Google DeepMind · 2026-05-07
  - **Target:** `Artifacts` · Bounded optimization
  - **Loop:** Reports follow-up applications of evaluated code evolution to model components, training efficiency, cache policies and TPU circuits, with concrete AI-development feedback paths.
  - **Boundary:** Deployment case studies and publisher-reported gains do not demonstrate a fully closed cycle that retrains and improves the Gemini proposer itself.

- **[AlphaEvolve: A Gemini-powered coding agent for designing advanced algorithms](https://deepmind.google/blog/alphaevolve-a-gemini-powered-coding-agent-for-designing-advanced-algorithms/)** — Google DeepMind · 2025-05-14
  - **Target:** `Artifacts` · Bounded optimization
  - **Loop:** Explains evaluated program evolution that improves algorithms and Gemini training kernels, feeding successful programs into the next evolutionary proposals.
  - **Boundary:** Improving infrastructure used to train its underlying LLM is not proof of repeated autonomous Gemini-weight self-training.

- **[ShinkaEvolve: Evolving New Algorithms with LLMs, Orders of Magnitude More Efficiently](https://sakana.ai/shinka-evolve/)** — Sakana AI · 2025-09-25
  - **Target:** `Artifacts` · Bounded optimization
  - **Loop:** Details sample-efficient program evolution and an evolved MoE load-balancing loss, tying executable candidate selection to subsequent program generations.
  - **Boundary:** Human-defined fitness and a fixed proposer model bound the result; it does not demonstrate a self-rewriting learning algorithm.

- **[Digital Red Queen: Adversarial Program Evolution in Core War with LLMs](https://sakana.ai/drq/)** — Sakana AI · 2026-01-08
  - **Target:** `Artifacts` · Bounded optimization
  - **Loop:** Evolves Core War programs against a growing history of predecessors; changing opponents supply selection pressure and retained programs shape subsequent evolution.
  - **Boundary:** Program co-evolution in a controlled virtual machine does not demonstrate autonomous improvement of the underlying LLM or real-world security capability.

- **[Autonomous AI research for nanogpt speedrun](https://www.primeintellect.ai/auto-nanogpt)** — Prime Intellect · 2026-05-14
  - **Target:** `Artifacts` · Bounded optimization
  - **Loop:** Coding agents repeatedly revise optimizer code and hyperparameters, run nanoGPT training and use steps-to-target-validation-loss to select better variants; durable scratchpads preserve experiment state.
  - **Boundary:** Agents excelled at search and recombination but needed upstream human records to keep improving. Model/data/architecture and benchmark rules were fixed, and humans changed the harness between phases.

- **[General Agent: A Self-Evolving, Synthetic Agent Environment](https://www.primeintellect.ai/blog/general-agent)** — Prime Intellect · 2026-05-18
  - **Target:** `Artifacts` · Bounded optimization
  - **Loop:** A synthesizer evolves task families and a solver measures pass rates; only tasks in calibrated difficulty bands survive, and harder tiers seed later extensions of the synthetic training corpus.
  - **Boundary:** The evolved object is the task corpus. The post describes closing the full model-training/environment-generation loop as a broader research direction, not an already completed autonomous cycle.

- **[Prime Agent: A self-improving RLM agent](https://www.primeintellect.ai/blog/prime-agent)** — Prime Intellect · 2026-08-05
  - **Target:** `Harness` · Self-modification
  - **Loop:** Its /refine pipeline reads its own trajectory and changes persistent prompt notes, memory, skills and subagent specifications; recorded triggers/outcomes and rollback history carry improvements into later turns and sessions.
  - **Boundary:** The base system prompt remains immutable, and this does not retrain model weights. Its Factorio result is explicitly suspected of reward hacking; use the mechanism, not that score, as evidence.

- **[RoboCat: A self-improving robotic agent](https://deepmind.google/blog/robocat-a-self-improving-robotic-agent/)** — Google DeepMind · 2023-06-20
  - **Target:** `Models` · Self-training
  - **Loop:** Fine-tunes a task-specific spin-off, collects its practice trajectories, merges them with demonstrations and retrains a generalist RoboCat version for later tasks.
  - **Boundary:** Each new task begins with 100–1000 human demonstrations; the training procedure and robot interfaces remain human-designed.

- **[The AI Scientist: Towards Fully Automated Open-Ended Scientific Discovery](https://sakana.ai/ai-scientist/)** — Sakana AI · 2024-08-13
  - **Target:** `Artifacts` · Bounded optimization
  - **Loop:** Describes idea generation, code experiments, paper writing and automated reviewing; saved reviews and experiments inform revisions and future research ideas.
  - **Boundary:** Flawed comparisons and self-review remain risks; accidental execution-script modification is a safety failure, not evidence of beneficial RSI.

- **[FunSearch: Making new discoveries in mathematical sciences using Large Language Models](https://deepmind.google/blog/funsearch-making-new-discoveries-in-mathematical-sciences-using-large-language-models/)** — Google DeepMind · 2023-12-14
  - **Target:** `Artifacts` · Bounded optimization
  - **Loop:** Samples earlier high-scoring programs, asks a fixed LLM for improvements, executes candidates, and returns the best programs to a population for future search.
  - **Boundary:** The evaluator and seed program are user-supplied; the model weights and improvement algorithm are not recursively rewritten.

- **[Population-based Model Merging via Quality Diversity](https://sakana.ai/cycleqd/)** — Sakana AI · 2024-12-03
  - **Target:** `Models` · Bounded optimization
  - **Loop:** CycleQD cycles which task defines quality, crosses and mutates expert models, and retains diverse high-performing models in skill archives for further evolution.
  - **Boundary:** The tasks, starting experts and quality-diversity algorithm are human-specified; model merging is not gradient self-training or self-rewriting optimization.

- **[Evolving New Foundation Models: Unleashing the Power of Automating Model Development](https://sakana.ai/evolutionary-model-merge/)** — Sakana AI · 2024-03-21
  - **Target:** `Models` · Bounded optimization
  - **Loop:** Evolves layer-selection and weight-mixing recipes over successive generations, selecting merged models by task fitness and assessing the selected model on a separate test set.
  - **Boundary:** Evolution searches a human-defined merge space of pretrained models; it does not establish an LLM autonomously rewriting its training algorithm.

- **[Accelerating scientific breakthroughs with an AI co-scientist](https://research.google/blog/accelerating-scientific-breakthroughs-with-an-ai-co-scientist/)** — Google Research · 2025-02-19
  - **Target:** `Artifacts` · Bounded optimization
  - **Loop:** Generation, reflection, ranking, evolution and meta-review agents iteratively revise scientific hypotheses using tournament feedback and researcher input.
  - **Boundary:** Elo is a self-evaluation signal rather than independent ground truth; laboratory validation uses expert guidance, and model weights remain fixed.


### Evaluation and Failure Modes

- **[AI CUDA Engineer update: robust benchmarking and interim results](https://sakana.ai/ai-cuda-engineer-update/)** — Sakana AI · 2025-09-17
  - **Target:** `Artifacts` · Evaluation / safety
  - **Loop:** Corrects kernel-optimization claims after benchmark bypasses; robust-kbench reduces reported mean speedup from 3.13x to 1.49x under stricter measurement.
  - **Boundary:** A negative-results and measurement lesson for improvement loops, not a new self-improving agent; the original update is in Japanese.

- **[Sycophancy to subterfuge: Investigating reward tampering in language models](https://www.anthropic.com/research/reward-tampering)** — Anthropic · 2024-06-17
  - **Target:** `Harness` · Evaluation / safety
  - **Loop:** Tests whether a curriculum of specification gaming generalizes to editing the model's own reward function and concealing the change, exposing a direct failure mode when self-modifying systems can alter their evaluators.
  - **Boundary:** Reward tampering occurred in 45 of 32,768 trials in a constructed study; it was not observed evidence of deployed Claude performing RSI, nor proof that all self-modification is unsafe.

- **[From shortcuts to sabotage: natural emergent misalignment from reward hacking](https://www.anthropic.com/research/emergent-misalignment-reward-hacking)** — Anthropic · 2025-11-21
  - **Target:** `Harness` · Evaluation / safety
  - **Loop:** Shows reward-hacking training generalizing to malicious behavior, including a Claude Code evaluation where the model attempts to sabotage this research project's detection code, directly testing trust in AI-assisted AI safety research.
  - **Boundary:** Researchers deliberately selected hackable RL environments and added hacking knowledge during pretraining. The 12% sabotage attempt rate describes this experimental model, not ordinary deployed Claude or proven completed sabotage.

- **[Measuring Autonomous AI Research](https://www.primeintellect.ai/blog/measuring-autonomous-research)** — Prime Intellect · 2026-08-14
  - **Target:** `Artifacts` · Evaluation / safety
  - **Loop:** Evaluates 153 autonomous optimizer-research runs across 18 frontier models, examining whether proposed nanoGPT improvements survive evaluation and whether long-running agents produce new methods rather than only recombine existing ones.
  - **Boundary:** A fixed optimizer speedrun is a bounded proxy for research ability, not proof of general RSI. Results depend on seeds, supplied baselines and evaluation integrity.


### Research Agendas

- **[Introducing Sakana AI's Recursive Self-Improvement (RSI) Lab](https://sakana.ai/rsi-lab/)** — Sakana AI · 2026-06-05
  - **Target:** `Harness` · Research agenda
  - **Loop:** Maps a proposed loop from agent-native models to AI scientists that build better models, grounded in DGM, LLM-Squared, ShinkaEvolve and adversarial co-evolution.
  - **Boundary:** A research agenda and lineage map, not evidence that the complete autonomous model-improvement cycle has already been achieved.

- **[When AI builds itself](https://www.anthropic.com/institute/recursive-self-improvement)** — Anthropic Institute · date not verified
  - **Target:** `Models` · Research agenda
  - **Loop:** Defines recursive self-improvement as AI autonomously designing and developing its successor, presents internal evidence of AI accelerating engineering and research, and examines whether that assistance can close the full model-development loop.
  - **Boundary:** The article explicitly says full RSI has not been achieved and is not inevitable. Internal productivity statistics are observational; human research judgment, compute, evaluations and security remain constraints.


### Foundations and Historical Tutorials

- **[Constitutional AI: Harmlessness from AI feedback](https://www.anthropic.com/research/constitutional-ai-harmlessness-from-ai-feedback)** — Anthropic · 2022-12-15
  - **Target:** `Models` · Self-training
  - **Loop:** Samples model responses, generates self-critiques and revisions, fine-tunes on the revised responses, then derives AI preferences for a reward model used in reinforcement learning.
  - **Boundary:** Human-written constitutional principles and a fixed staged training recipe remain essential. This is a bounded self-supervision foundation, not evidence of endlessly repeated autonomous RSI.

- **[AlphaGo Zero: Starting from scratch](https://deepmind.google/blog/alphago-zero-starting-from-scratch/)** — Google DeepMind · 2017-10-18
  - **Target:** `Models` · Self-training
  - **Loop:** Self-play outcomes train the network; the updated network guides stronger search and games that supply the next training round.
  - **Boundary:** A foundational bounded self-training example in Go, with human-designed rules and learning machinery, not open-ended RSI.

- **[AlphaZero: Shedding new light on chess, shogi, and Go](https://deepmind.google/blog/alphazero-shedding-new-light-on-chess-shogi-and-go/)** — Google DeepMind · 2018-12-06
  - **Target:** `Models` · Self-training
  - **Loop:** Describes neural-network parameter updates from self-play outcomes and stronger network-guided tree search across separately learned games.
  - **Boundary:** Each game retains fixed rules and objectives; this is not one model autonomously expanding its domain or rewriting its learner.

- **[Self-Evolving Agents - A Cookbook for Autonomous Agent Retraining](https://developers.openai.com/cookbook/examples/partners/self_evolving_agents/autonomous_agent_retraining)** — OpenAI and Bain · 2025-11-04 · archived tutorial
  - **Target:** `Harness` · Bounded optimization
  - **Loop:** Demonstrates versioned summarization-prompt updates from grader feedback, meta-prompting and GEPA, retaining better candidates for later requests.
  - **Boundary:** The official recipe is archived and may reference outdated APIs. Despite the title, it changes prompts rather than model weights; production needs held-out tests and human approval. Its example validation slice overlaps its training list.


## Papers and Official Code

- Dates refer to first publication. Only source-verified venues are shown; a date alone makes no peer-review claim.
- Official code is author-linked; artifact-only and archived releases are marked. Older code does not disqualify a useful paper.
- Star badges and push dates use the **2026-09-08** metadata snapshot.

### Papers / Models

| Paper | Date / Publication | Code | Contribution and Boundary |
| --- | --- | --- | --- |
| [Agent0: Unleashing Self-Evolving Agents from Zero Data via Tool-Integrated Reasoning](https://arxiv.org/abs/2511.16043) | 2025-11-20 | • [Official code](https://github.com/aiming-lab/Agent0)<br>• [![star: 1,258](https://img.shields.io/badge/star-1258-f4b400?style=flat-square)](https://github.com/aiming-lab/Agent0)<br>• **Last push:** 2026-07-10 | • **Self-training**<br>• **Loop:** Couples a curriculum model with a tool-using executor model; stronger execution drives harder generated curricula, which in turn provide reinforcement-learning data.<br>• **Boundary:** The released training instructions require manual checkpoint selection between iterations; zero external data does not remove pretrained-backbone or tool dependencies. |
| [R-Zero: Self-Evolving Reasoning LLM from Zero Data](https://arxiv.org/abs/2508.05004) | 2025-08-07<br>[ICLR 2026](https://github.com/Chengsong-Huang/R-Zero/blob/main/README.md) | • [Official code](https://github.com/Chengsong-Huang/R-Zero)<br>• [![star: 845](https://img.shields.io/badge/star-845-f4b400?style=flat-square)](https://github.com/Chengsong-Huang/R-Zero)<br>• **Last push:** 2026-02-04 | • **Self-training**<br>• **Loop:** Co-evolves Challenger and Solver models so that frontier-difficulty generated tasks train the Solver, while the Solver's changing capability alters the Challenger's rewards.<br>• **Boundary:** Uses a pretrained base and designed rewards; finite iterations can regress, and the authors' later R-Few work introduces human data to address scaling limits. |
| [Self-Adapting Language Models](https://arxiv.org/abs/2506.10943) | 2025-06-12 | • [Official code](https://github.com/Continual-Intelligence/SEAL)<br>• [![star: 1,855](https://img.shields.io/badge/star-1855-f4b400?style=flat-square)](https://github.com/Continual-Intelligence/SEAL)<br>• **Last push:** 2025-08-01<br>• **Release notes:** The paper links its author project page, and the matching official repository links the same paper and page. The canonical repository is Continual-Intelligence/SEAL. | • **Self-training**<br>• **Loop:** The model generates self-edits containing finetuning data or update directives; SFT makes persistent weight changes, and downstream performance trains better self-edit generation through an outer RL loop.<br>• **Boundary:** Self-edits control adaptation within a researcher-designed SFT/RL framework; experiments on knowledge incorporation and few-shot generalization do not prove unrestricted self-redesign. |
| [Absolute Zero: Reinforced Self-play Reasoning with Zero Data](https://arxiv.org/abs/2505.03335) | 2025-05-06 | • [Official code](https://github.com/LeapLabTHU/Absolute-Zero-Reasoner)<br>• [![star: 1,901](https://img.shields.io/badge/star-1901-f4b400?style=flat-square)](https://github.com/LeapLabTHU/Absolute-Zero-Reasoner)<br>• **Last push:** 2025-08-24 | • **Self-training**<br>• **Loop:** A model co-evolves its task proposals and solving ability, using a code executor for task validity and answer rewards instead of an externally curated post-training dataset.<br>• **Boundary:** Zero data refers to the self-play post-training setup, not an untrained backbone; the executor, rewards and optimization machinery are human-designed. |
| [Agent Skill Acquisition for Large Language Models via CycleQD](https://arxiv.org/abs/2410.14735) | 2024-10-16<br>[ICLR 2025](https://github.com/SakanaAI/CycleQD/blob/main/README.md) | • [Official code](https://github.com/SakanaAI/CycleQD)<br>• [![star: 48](https://img.shields.io/badge/star-48-f4b400?style=flat-square)](https://github.com/SakanaAI/CycleQD)<br>• **Last push:** 2025-02-01 | • **Bounded optimization**<br>• **Loop:** Evolves model variants with merging-based crossover and SVD mutation, cycling task metrics between quality objectives and diversity descriptors to accumulate complementary skills.<br>• **Boundary:** Model parameters evolve, but the QD algorithm, task metrics and expert starting models are externally specified; this is not autonomous learner self-modification. |
| [Self-Taught Evaluators](https://arxiv.org/abs/2408.02666) | 2024-08-05 | • [Official artifacts only](https://github.com/facebookresearch/RAM/tree/main/projects/self_taught_evaluator)<br>• [![star: 382](https://img.shields.io/badge/star-382-f4b400?style=flat-square)](https://github.com/facebookresearch/RAM)<br>• **Last push:** 2026-06-25<br>• **Release notes:** Official model, synthetic data and judging/evaluation scripts are documented; this is not a claim that a complete end-to-end training pipeline is released. | • **Self-training**<br>• **Loop:** Generates contrasting responses and synthetic reasoning/judgments to repeatedly train an LLM evaluator, using improved evaluator predictions to construct later training rounds.<br>• **Boundary:** Human-preference-free training is not the same as zero human validation; the release documents checkpoint selection with HelpSteer2 validation accuracy. |
| [ReST-MCTS*: LLM Self-Training via Process Reward Guided Tree Search](https://arxiv.org/abs/2406.03816) | 2024-06-06 | • [Official code](https://github.com/THUDM/ReST-MCTS)<br>• [![star: 711](https://img.shields.io/badge/star-711-f4b400?style=flat-square)](https://github.com/THUDM/ReST-MCTS)<br>• **Last push:** 2025-01-20<br>• **Release notes:** Official README documents policy/value-model synthetic-data generation and iterative training. Presence of code is not independent replication of every reported result. | • **Self-training**<br>• **Loop:** Uses process-reward-guided tree search to infer step values from correct final answers, then trains both the policy and process reward model on selected traces across multiple iterations.<br>• **Boundary:** Removes per-step manual annotation, not oracle final-answer supervision; externally designed search and reward-learning rules remain fixed. |
| [Self-Play Preference Optimization for Language Model Alignment](https://arxiv.org/abs/2405.00675) | 2024-05-01<br>[ICLR 2025](https://github.com/uclaml/SPPO/blob/main/README.md) | • [Official code](https://github.com/uclaml/SPPO)<br>• [![star: 589](https://img.shields.io/badge/star-589-f4b400?style=flat-square)](https://github.com/uclaml/SPPO)<br>• **Last push:** 2025-01-23<br>• **Release notes:** The official repository explicitly provides code and released models; PairRM is an external pretrained preference model, not the policy learning to judge itself. | • **Self-training**<br>• **Loop:** Treats alignment as a constant-sum two-player game and repeatedly updates the policy against its own generated responses using preference probabilities to approach a Nash equilibrium.<br>• **Boundary:** Experiments use prompts and a pretrained PairRM judge; the equilibrium guarantee concerns the specified preference game, not unbounded capability growth or self-improving evaluation. |
| [Self-Rewarding Language Models](https://arxiv.org/abs/2401.10020) | 2024-01-18 | Not found in reviewed sources | • **Self-training**<br>• **Loop:** Uses the language model as its own prompted reward judge during iterative DPO, jointly improving response generation and the rewards it gives subsequent training examples.<br>• **Boundary:** Three reported iterations and benchmark preference gains do not prove calibrated self-judgment or sustained superhuman improvement; seed supervision remains relevant. |
| [Self-Play Fine-Tuning Converts Weak Language Models to Strong Language Models](https://arxiv.org/abs/2401.01335) | 2024-01-02<br>[ICML 2024](https://github.com/uclaml/SPIN/blob/main/README.md) | • [Official code](https://github.com/uclaml/SPIN)<br>• [![star: 1,254](https://img.shields.io/badge/star-1254-f4b400?style=flat-square)](https://github.com/uclaml/SPIN)<br>• **Last push:** 2024-05-08 | • **Self-training**<br>• **Loop:** Trains a policy to distinguish human demonstration responses from responses generated by its previous iteration, repeatedly strengthening a supervised fine-tuned model through self-play.<br>• **Boundary:** Reuses human demonstrations and an SFT starting model; theoretical optimality concerns the target data distribution, not unlimited recursive capability growth. |
| [Beyond Human Data: Scaling Self-Training for Problem-Solving with Language Models](https://arxiv.org/abs/2312.06585) | 2023-12-11 | Not found in reviewed sources | • **Self-training**<br>• **Loop:** Repeatedly samples solutions, filters by binary correctness feedback and fine-tunes on accepted samples, studying scaling on MATH and APPS with PaLM-2.<br>• **Boundary:** Needs externally supplied problems and verifiable feedback; a few EM-style iterations do not establish indefinite improvement. |
| [Reinforced Self-Training (ReST) for Language Modeling](https://arxiv.org/abs/2308.08998) | 2023-08-17 | Not found in reviewed sources | • **Self-training**<br>• **Loop:** Alternates policy-generated data collection with reward-guided offline learning, reusing samples to improve a language-model policy, demonstrated on machine translation.<br>• **Boundary:** Reward and preference signals remain externally specified; results in translation do not establish a self-improving reward mechanism or open-ended capability growth. |
| [RoboCat: A Self-Improving Generalist Agent for Robotic Manipulation](https://arxiv.org/abs/2306.11706) | 2023-06-20 | Not found in reviewed sources | • **Self-training**<br>• **Loop:** Adapts a generalist robotic policy to tasks and embodiments, uses trained policies to gather further robot experience, and retrains subsequent generalist models on the expanded data.<br>• **Boundary:** Task adaptation still uses demonstrations and controlled robot infrastructure; this is a building block for autonomous improvement, not self-redesign of the training system. |
| [STaR: Bootstrapping Reasoning With Reasoning](https://arxiv.org/abs/2203.14465) | 2022-03-28<br>[NeurIPS 2022](https://github.com/ezelikman/STaR/blob/main/README.md) | • [Official code](https://github.com/ezelikman/STaR)<br>• [![star: 232](https://img.shields.io/badge/star-232-f4b400?style=flat-square)](https://github.com/ezelikman/STaR)<br>• **Last push:** 2023-02-21 | • **Self-training**<br>• **Loop:** Generates reasoning traces, filters them by answer correctness, rationalizes failed examples using known answers, and repeatedly fine-tunes on successful traces.<br>• **Boundary:** Requires a task dataset, known answers and seed rationale examples; a fixed training loop is not an autonomous redesign of the learner. |

### Papers / Harness

| Paper | Date / Publication | Code | Contribution and Boundary |
| --- | --- | --- | --- |
| [Prime Agent: A Self-Improving RLM Harness](https://arxiv.org/abs/2608.23552) | 2026-08-24 | • [Official code](https://github.com/PrimeIntellect-ai/prime-agent)<br>• [![star: 20,300](https://img.shields.io/badge/star-20300-f4b400?style=flat-square)](https://github.com/PrimeIntellect-ai/prime-agent)<br>• **Last push:** 2026-09-08<br>• **Release notes:** The author repository directly cites this paper and separately cites Continual Harness (2605.09998); neither citation should overwrite the other's title or first-paper date. | • **Experience learning**<br>• **Loop:** Combines a persistent REPL and recursive subagents with retained histories, memories, skills, prompts and subagent specifications that can be refined across long-horizon trajectories.<br>• **Boundary:** Recursive subagent calls alone are not RSI; the relevant mechanism is retained refinement of harness state. Benchmark gains also include execution/recovery improvements and do not isolate self-improvement as the sole cause. |
| [Continual Harness: Online Adaptation for Self-Improving Foundation Agents](https://arxiv.org/abs/2605.09998) | 2026-05-11 | • [Official code](https://github.com/PrimeIntellect-ai/prime-agent)<br>• [![star: 20,300](https://img.shields.io/badge/star-20300-f4b400?style=flat-square)](https://github.com/PrimeIntellect-ai/prime-agent)<br>• **Last push:** 2026-09-08<br>• **Release notes:** Official associated implementation of the harness component via an explicit README link to this paper. The inspected paper v1 does not establish release of all Pokemon experiments or the teacher-relabeled weight co-learning pipeline; this is not certified full reproduction code. | • **Experience learning**<br>• **Loop:** Alternates action and refinement of prompts, subagents, skills and memory within a reset-free run. A separate co-learning experiment relabels rollouts with a frontier teacher and updates an open model without resetting the game.<br>• **Boundary:** Earlier Gemini Plays Pokemon results used human-in-the-loop harness refinement; later automated adaptation and teacher-assisted weight co-learning are distinct settings. Teacher supervision and game-specific evaluation limit autonomy claims. |
| [Hyperagents](https://arxiv.org/abs/2603.19461) | 2026-03-19 | • [Official code](https://github.com/facebookresearch/HyperAgents)<br>• [![star: 2,718](https://img.shields.io/badge/star-2718-f4b400?style=flat-square)](https://github.com/facebookresearch/HyperAgents)<br>• **Last push:** 2026-07-31 | • **Self-modification**<br>• **Loop:** Integrates a task agent and a meta agent into one editable program so that evaluated changes can improve both task behavior and the machinery producing future changes.<br>• **Boundary:** Reported transfer and accumulation are finite experiments, not evidence of indefinite acceleration or autonomous weight-level learning. |
| [GEPA: Reflective Prompt Evolution Can Outperform Reinforcement Learning](https://arxiv.org/abs/2507.19457) | 2025-07-25 | • [Official code](https://github.com/gepa-ai/gepa)<br>• [![star: 6,475](https://img.shields.io/badge/star-6475-f4b400?style=flat-square)](https://github.com/gepa-ai/gepa)<br>• **Last push:** 2026-09-08 | • **Bounded optimization**<br>• **Loop:** Reflects on sampled execution traces to mutate prompts and combine complementary successful lessons through Pareto-based candidate selection.<br>• **Boundary:** Optimizes prompt configurations with fixed underlying model weights and an externally supplied evaluator; it does not demonstrate that its mutation machinery rewrites itself. |
| [EvoAgentX: An Automated Framework for Evolving Agentic Workflows](https://arxiv.org/abs/2507.03616) | 2025-07-04 | • [Official code](https://github.com/ANative-Lab/EvoAgentX)<br>• [![star: 3,313](https://img.shields.io/badge/star-3313-f4b400?style=flat-square)](https://github.com/ANative-Lab/EvoAgentX)<br>• **Last push:** 2026-08-27<br>• **Release notes:** The paper's EvoAgentX/EvoAgentX URL redirects to ANative-Lab/EvoAgentX; the current README retains the exact paper citation. This is a framework integration paper, not a new independent optimizer for every component. | • **Bounded optimization**<br>• **Loop:** Integrates TextGrad, AFlow and MIPRO into a modular workflow-generation, execution and evaluation platform that repeatedly refines prompts, tool configurations and workflow topology.<br>• **Boundary:** Included for the explicit evolving layer, not generic multi-agent orchestration; fixed integrated optimizers and benchmarks do not establish self-rewriting improvement machinery. |
| [Darwin Godel Machine: Open-Ended Evolution of Self-Improving Agents](https://arxiv.org/abs/2505.22954) | 2025-05-29 | • [Official code](https://github.com/jennyzzt/dgm)<br>• [![star: 2,292](https://img.shields.io/badge/star-2292-f4b400?style=flat-square)](https://github.com/jennyzzt/dgm)<br>• **Last push:** 2025-08-13 | • **Self-modification**<br>• **Loop:** A coding agent modifies its own implementation, evaluates descendants on coding benchmarks, and branches from a growing archive of agents to produce further improvements.<br>• **Boundary:** Empirical code-level self-improvement, not formal proof of beneficial rewrites or foundation-model weight training; benchmark exploitation and sandbox escape remain concerns. |
| [A Self-Improving Coding Agent](https://arxiv.org/abs/2504.15228) | 2025-04-21<br>[ICLR 2025 Workshop on Scaling Self-Improving Foundation Models](https://github.com/MaximeRobeyns/self_improving_coding_agent/blob/master/README.md) | • [Official code](https://github.com/MaximeRobeyns/self_improving_coding_agent)<br>• [![star: 394](https://img.shields.io/badge/star-394-f4b400?style=flat-square)](https://github.com/MaximeRobeyns/self_improving_coding_agent)<br>• **Last push:** 2025-04-23<br>• **Release notes:** The official repository uses the master branch; a main-branch README request returns 404. Its citation explicitly identifies a workshop, not the ICLR main conference track. | • **Self-modification**<br>• **Loop:** Evaluates the current coding agent, archives results, runs that same agent on its own codebase to implement an improvement, and evaluates the updated implementation again.<br>• **Boundary:** Non-gradient scaffold learning uses fixed LLM weights; gains on a sampled SWE-bench Verified subset and other benchmarks do not establish unlimited progress or whole-benchmark state of the art. |
| [AFlow: Automating Agentic Workflow Generation](https://arxiv.org/abs/2410.10762) | 2024-10-14<br>[ICLR 2025](https://github.com/FoundationAgents/AFlow/blob/main/README.md) | • [Official code](https://github.com/FoundationAgents/AFlow)<br>• [![star: 589](https://img.shields.io/badge/star-589-f4b400?style=flat-square)](https://github.com/FoundationAgents/AFlow)<br>• **Last push:** 2025-12-25 | • **Bounded optimization**<br>• **Loop:** Searches code-represented agent workflows with Monte Carlo Tree Search, using execution feedback and tree-structured experience to propose stronger graphs.<br>• **Boundary:** Workflow search does not imply modifying the search algorithm or model weights; benchmark evaluators and operator definitions are supplied externally. |
| [Gödel Agent: A Self-Referential Agent Framework for Recursive Self-Improvement](https://arxiv.org/abs/2410.04444) | 2024-10-06 | • [Official code](https://github.com/Arvid-pku/Godel_Agent)<br>• [![star: 219](https://img.shields.io/badge/star-219-f4b400?style=flat-square)](https://github.com/Arvid-pku/Godel_Agent)<br>• **Last push:** 2025-09-17<br>• **Release notes:** The canonical abstract links the repository, whose README links the same paper. No verified formal-proof implementation or conference venue is inferred from the name. | • **Self-modification**<br>• **Loop:** Uses LLM-generated changes to recursively revise the agent's own logic and behavior under high-level objectives rather than limiting changes to a predefined task-agent pipeline.<br>• **Boundary:** Inspired by the Gödel machine but supported by empirical task evaluations, not proofs that all rewrites are beneficial or that the whole agent-design space is optimally searched. |
| [Automated Design of Agentic Systems](https://arxiv.org/abs/2408.08435) | 2024-08-15<br>[ICLR 2025](https://github.com/ShengranHu/ADAS/blob/main/README.md) | • [Official code](https://github.com/ShengranHu/ADAS)<br>• [![star: 1,637](https://img.shields.io/badge/star-1637-f4b400?style=flat-square)](https://github.com/ShengranHu/ADAS)<br>• **Last push:** 2025-01-28 | • **Bounded optimization**<br>• **Loop:** Meta Agent Search programs and evaluates new agent designs, using an expanding archive to discover workflows that can transfer across tasks and underlying models.<br>• **Boundary:** The meta-agent search procedure is externally fixed; inventing task agents is not the same as recursively improving the meta-agent's own learning machinery. |
| [TextGrad: Automatic "Differentiation" via Text](https://arxiv.org/abs/2406.07496) | 2024-06-11<br>[Nature](https://github.com/zou-group/TextGrad/blob/main/README.md) | • [Official code](https://github.com/zou-group/textgrad)<br>• [![star: 3,720](https://img.shields.io/badge/star-3720-f4b400?style=flat-square)](https://github.com/zou-group/textgrad)<br>• **Last push:** 2025-07-25 | • **Bounded optimization**<br>• **Loop:** Propagates natural-language feedback through a computation graph to update prompts and other text-valued variables; the same framework also optimizes code and scientific artifacts.<br>• **Boundary:** Textual gradients are heuristic LLM critiques, not analytic derivatives; fixed objectives and optimizer logic bound the claimed self-improvement. |
| [Agent-Pro: Learning to Evolve via Policy-Level Reflection and Optimization](https://arxiv.org/abs/2402.17574) | 2024-02-27<br>[ACL 2024 Main](https://github.com/zwq2018/Agent-Pro/blob/main/README.md) | • [Official code](https://github.com/ZJU-OmniAI/Agent-Pro)<br>• [![star: 131](https://img.shields.io/badge/star-131-f4b400?style=flat-square)](https://github.com/ZJU-OmniAI/Agent-Pro)<br>• **Last push:** 2024-09-02 | • **Bounded optimization**<br>• **Loop:** Revises policy-level beliefs from interactive trajectories and uses depth-first search to select improved behavioral policies in Blackjack and Texas Hold'em.<br>• **Boundary:** The paper's belief 'fine-tuning' is policy-level reflection, not established neural-weight training; game payoffs and the search procedure remain fixed. |
| [Self-Taught Optimizer (STOP): Recursively Self-Improving Code Generation](https://arxiv.org/abs/2310.02304) | 2023-10-03 | • [Official code](https://github.com/microsoft/stop)<br>• [![star: 53](https://img.shields.io/badge/star-53-f4b400?style=flat-square)](https://github.com/microsoft/stop)<br>• **Last push:** 2024-01-01 | • **Self-modification**<br>• **Loop:** A seed LM-calling program optimizer is applied to its own code, discovering improved search scaffolds that then optimize downstream programs.<br>• **Boundary:** The paper explicitly says unchanged language models make this not full recursive self-improvement; only a small task set is studied, including sandbox-bypass risks. |
| [Large Language Models as Optimizers](https://arxiv.org/abs/2309.03409) | 2023-09-07 | • [Official code](https://github.com/google-deepmind/opro)<br>• [![star: 774](https://img.shields.io/badge/star-774-f4b400?style=flat-square)](https://github.com/google-deepmind/opro)<br>• **Last push:** 2024-12-04<br>• **Release notes:** Official research code, not a supported Google product; no conference venue was verified from its README. | • **Bounded optimization**<br>• **Loop:** Prompts an LLM with previously proposed solutions and their objective values, evaluates new candidates and feeds the scored history back into later optimization, especially for instructions.<br>• **Boundary:** The optimizer model and scoring task remain fixed; iterative prompt search does not itself improve the LLM's weights or rewrite the optimizer. |

### Papers / Artifacts

| Paper | Date / Publication | Code | Contribution and Boundary |
| --- | --- | --- | --- |
| [Digital Red Queen: Adversarial Program Evolution in Core War with LLMs](https://arxiv.org/abs/2601.03335) | 2026-01-06 | • [Official code](https://github.com/SakanaAI/drq)<br>• [![star: 220](https://img.shields.io/badge/star-220-f4b400?style=flat-square)](https://github.com/SakanaAI/drq)<br>• **Last push:** 2026-01-13 | • **Bounded optimization**<br>• **Loop:** Evolves executable Core War warriors against all prior opponents, turning the retained population into an adaptive self-play objective rather than optimizing against a fixed benchmark alone.<br>• **Boundary:** The LLM and evolution algorithm remain fixed; reported generalization is within Core War, not evidence of practical cybersecurity capability or unconstrained RSI. |
| [Agentic Context Engineering: Evolving Contexts for Self-Improving Language Models](https://arxiv.org/abs/2510.04618) | 2025-10-06 | • [Official code](https://github.com/ace-agent/ace)<br>• [![star: 1,302](https://img.shields.io/badge/star-1302-f4b400?style=flat-square)](https://github.com/ace-agent/ace)<br>• **Last push:** 2026-08-24<br>• **Release notes:** The author-linked repository documents Generator, Reflector and Curator roles, incremental delta updates, saved playbooks and evaluation modes; no weight training is implied. | • **Experience learning**<br>• **Loop:** Treats context as a persistent evolving playbook; execution feedback is reflected into structured incremental updates that retain, refine and organize strategies across later tasks.<br>• **Boundary:** Context adaptation is not model-weight learning; reported gains depend on task feedback and a fixed generation/reflection/curation architecture, with offline and online evaluation distinguished. |
| [ShinkaEvolve: Towards Open-Ended And Sample-Efficient Program Evolution](https://arxiv.org/abs/2509.19349) | 2025-09-17<br>[ICLR 2026](https://github.com/SakanaAI/ShinkaEvolve/blob/main/README.md) | • [Official code](https://github.com/SakanaAI/ShinkaEvolve)<br>• [![star: 1,375](https://img.shields.io/badge/star-1375-f4b400?style=flat-square)](https://github.com/SakanaAI/ShinkaEvolve)<br>• **Last push:** 2026-08-21 | • **Bounded optimization**<br>• **Loop:** Improves program evolution efficiency through archive sampling, novelty filtering and adaptive LLM selection, with applications to math solutions, agent harnesses and MoE training losses.<br>• **Boundary:** The program optimizer and task fitness are designed externally; open-ended branding does not establish a self-rewriting learner or indefinitely improving foundation weights. |
| [AlphaEvolve: A coding agent for scientific and algorithmic discovery](https://arxiv.org/abs/2506.13131) | 2025-06-16 | Not found in reviewed sources | • **Bounded optimization**<br>• **Loop:** Orchestrates LLM-proposed code changes and executable evaluation in an evolutionary pipeline, improving scientific algorithms and computational infrastructure including its underlying LLM's training kernels.<br>• **Boundary:** Improving training code is not demonstration of a repeated closed loop that retrains the proposer model or rewrites the evolutionary algorithm itself. |
| [Discovering Preference Optimization Algorithms with and for Large Language Models](https://arxiv.org/abs/2406.08414) | 2024-06-12 | • [Official code](https://github.com/SakanaAI/DiscoPOP)<br>• [![star: 196](https://img.shields.io/badge/star-196-f4b400?style=flat-square)](https://github.com/SakanaAI/DiscoPOP)<br>• **Last push:** 2024-06-13 | • **Bounded optimization**<br>• **Loop:** Uses an LLM to propose executable preference-optimization losses, trains/evaluates models with those losses, and feeds measured performance into later proposals, discovering DiscoPOP.<br>• **Boundary:** The changed artifact is training-loss code; the proposing LLM is not shown repeatedly retraining itself on the discovered loss in a closed recursive loop. |
| [Mathematical discoveries from program search with large language models](https://www.nature.com/articles/s41586-023-06924-6) | 2023-12-14<br>[Nature](https://www.nature.com/articles/s41586-023-06924-6) | • [Official code](https://github.com/google-deepmind/funsearch)<br>• [![star: 1,116](https://img.shields.io/badge/star-1116-f4b400?style=flat-square)](https://github.com/google-deepmind/funsearch)<br>• **Last push:** 2024-02-05 | • **Bounded optimization**<br>• **Loop:** Evolves functions by prompting a pretrained LLM with high-scoring programs, executing a systematic evaluator and feeding accepted programs back into the database.<br>• **Boundary:** Requires a user-defined evaluator and seed/skeleton; the publisher explicitly states no LLM training or fine-tuning is required. Released code is a single-threaded pipeline, not Google's full internal distributed system. |
| [Voyager: An Open-Ended Embodied Agent with Large Language Models](https://arxiv.org/abs/2305.16291) | 2023-05-25 | • [Official code](https://github.com/MineDojo/Voyager)<br>• [![star: 7,184](https://img.shields.io/badge/star-7184-f4b400?style=flat-square)](https://github.com/MineDojo/Voyager)<br>• **Last push:** 2024-04-03 | • **Experience learning**<br>• **Loop:** Builds executable Minecraft skills under an automatic curriculum, repairing programs from environment feedback and reusing a growing skill library in later tasks and worlds.<br>• **Boundary:** The GPT-4 backbone is accessed through black-box inference rather than weight updates; open-ended exploration is demonstrated within Minecraft, not unrestricted domains. |
| [Self-Refine: Iterative Refinement with Self-Feedback](https://arxiv.org/abs/2303.17651) | 2023-03-30 | • [Official code](https://github.com/madaan/self-refine)<br>• [![star: 820](https://img.shields.io/badge/star-820-f4b400?style=flat-square)](https://github.com/madaan/self-refine)<br>• **Last push:** 2024-10-04 | • **Within-task refinement**<br>• **Loop:** Uses one LLM as generator, critic and refiner, feeding textual feedback into repeated revisions of a task output at inference time.<br>• **Boundary:** This is a bounded within-task baseline, not persistent policy or weight improvement; self-feedback can be wrong and the framework does not by itself accumulate cross-task skill. |
| [Reflexion: Language Agents with Verbal Reinforcement Learning](https://arxiv.org/abs/2303.11366) | 2023-03-20<br>[NeurIPS 2023](https://github.com/noahshinn/reflexion/blob/main/README.md) | • [Official code](https://github.com/noahshinn/reflexion)<br>• [![star: 3,262](https://img.shields.io/badge/star-3262-f4b400?style=flat-square)](https://github.com/noahshinn/reflexion)<br>• **Last push:** 2025-01-14 | • **Experience learning**<br>• **Loop:** Converts trial feedback into verbal reflections stored in episodic memory, using those retained notes to change decisions in subsequent trials without updating model weights.<br>• **Boundary:** Verbal reinforcement learning is not gradient-based RL; task/trial memory and benchmark success do not establish unrestricted, permanent cross-domain learning. |

## Active GitHub Projects

Repository metadata snapshot: **2026-09-08**. Only public, non-archived projects pushed in the last **60 days** appear here; stars are snapshots, not evidence of RSI. Paper-associated code above has no activity gate.

### Models

#### Models / Training Research

Agents revise training recipes and evaluate resulting models; the researching agent is not necessarily retrained.

| Project | Link | Stars | Tags | Improvement Loop and Boundary |
| --- | --- | ---: | --- | --- |
| RD-Agent / FT-Agent | [GitHub](https://github.com/microsoft/RD-Agent) | [![star: 14,551](https://img.shields.io/badge/star-14551-f4b400?style=flat-square)](https://github.com/microsoft/RD-Agent) | `model-training`<br>`experiment-loop`<br>`validation` | • **Bounded optimization**<br>• **Loop:** FT-Agent generates data-processing code and training configurations, fine-tunes a target LLM, then uses OpenCompass validation feedback to refine the next training experiment.<br>• **Boundary:** This improves an external target model, not the planner's own weights; test splits are reserved for final reporting.<br>• [Evidence](https://github.com/microsoft/RD-Agent/blob/main/rdagent/app/finetune/llm/README.md) |

### Harness

#### Harness / Self-Modification

The agent implementation and its improvement procedure are themselves editable.

| Project | Link | Stars | Tags | Improvement Loop and Boundary |
| --- | --- | ---: | --- | --- |
| Prime Agent / Continual Harness | [GitHub](https://github.com/PrimeIntellect-ai/prime-agent) | [![star: 20,300](https://img.shields.io/badge/star-20300-f4b400?style=flat-square)](https://github.com/PrimeIntellect-ai/prime-agent) | `self-refinement`<br>`continual-harness`<br>`rollback` | • **Self-modification**<br>• **Loop:** Reviews trajectories with /refine and retains small evidence-backed updates to supplemental prompts, memory, skill descriptions and subagent specifications; snapshots allow rollback.<br>• **Boundary:** The base system prompt is immutable. Refinement does not replace packaging/review of executable skills, and its processes are not a security sandbox.<br>• [Evidence](https://github.com/PrimeIntellect-ai/prime-agent) |
| HyperAgents | [GitHub](https://github.com/facebookresearch/HyperAgents) | [![star: 2,718](https://img.shields.io/badge/star-2718-f4b400?style=flat-square)](https://github.com/facebookresearch/HyperAgents) | `self-modification`<br>`meta-agent`<br>`archive` | • **Self-modification**<br>• **Loop:** Integrates task and meta agents in one editable program; evaluated descendants can change both task behavior and the procedure that generates subsequent agents.<br>• **Boundary:** Empirical task-bounded experiments, not proof of indefinite improvement or foundation-model weight self-training.<br>• [Evidence](https://github.com/facebookresearch/HyperAgents/blob/main/utils/gl_utils.py) |

#### Harness / Prompt and Workflow Optimization

Feedback updates retained prompts or workflow graphs. These bounded optimizers do not establish unrestricted self-modification.

| Project | Link | Stars | Tags | Improvement Loop and Boundary |
| --- | --- | ---: | --- | --- |
| DSPy / GEPA and MIPROv2 | [GitHub](https://github.com/stanfordnlp/dspy) | [![star: 37,855](https://img.shields.io/badge/star-37855-f4b400?style=flat-square)](https://github.com/stanfordnlp/dspy) | `prompt-optimization`<br>`demonstrations`<br>`metrics` | • **Bounded optimization**<br>• **Loop:** Compiles LM programs by optimizing instructions and demonstrations against task metrics; compiled programs retain the selected configuration for later use.<br>• **Boundary:** Included for its optimizers, not all DSPy functionality; prompt compilation does not by itself modify the optimizer or model weights.<br>• [Evidence](https://github.com/stanfordnlp/dspy/blob/main/dspy/teleprompt/gepa/gepa.py) |
| GEPA | [GitHub](https://github.com/gepa-ai/gepa) | [![star: 6,475](https://img.shields.io/badge/star-6475-f4b400?style=flat-square)](https://github.com/gepa-ai/gepa) | `reflection`<br>`pareto-selection`<br>`prompt-optimization` | • **Bounded optimization**<br>• **Loop:** Reflects on execution traces and evaluator feedback to propose prompt revisions, retaining complementary candidates through Pareto-based selection.<br>• **Boundary:** The original method optimizes prompts with fixed model weights; its general optimize_anything API is not evidence that GEPA rewrites itself.<br>• [Evidence](https://github.com/gepa-ai/gepa) |
| EvoAgentX / Evolution Algorithms | [GitHub](https://github.com/ANative-Lab/EvoAgentX) | [![star: 3,313](https://img.shields.io/badge/star-3313-f4b400?style=flat-square)](https://github.com/ANative-Lab/EvoAgentX) | `workflow-optimization`<br>`aflow`<br>`validation` | • **Bounded optimization**<br>• **Loop:** Runs AFlow, TextGrad, MIPRO and EvoPrompt over agent workflows; validation scores drive prompt or graph revisions, with separate test evaluation.<br>• **Boundary:** Included for executable evolution algorithms, not tool integrations or workflow generation alone; objectives and search algorithms are human-specified.<br>• [Evidence](https://github.com/ANative-Lab/EvoAgentX#evolution-algorithms) |

### Artifacts

#### Artifacts / Program Evolution

Executable programs and algorithms are evolved against an evaluator; the optimizer is generally fixed.

| Project | Link | Stars | Tags | Improvement Loop and Boundary |
| --- | --- | ---: | --- | --- |
| OpenEvolve | [GitHub](https://github.com/algorithmicsuperintelligence/openevolve) | [![star: 7,336](https://img.shields.io/badge/star-7336-f4b400?style=flat-square)](https://github.com/algorithmicsuperintelligence/openevolve) | `program-evolution`<br>`evaluator`<br>`archive` | • **Bounded optimization**<br>• **Loop:** Evolves executable program variants using LLM mutations, task-specific evaluators and an archive that seeds subsequent generations.<br>• **Boundary:** Programs are the improvement target; neither a self-rewriting optimizer nor recursive proposer-weight training is established.<br>• [Evidence](https://github.com/algorithmicsuperintelligence/openevolve) |
| ShinkaEvolve | [GitHub](https://github.com/SakanaAI/ShinkaEvolve) | [![star: 1,375](https://img.shields.io/badge/star-1375-f4b400?style=flat-square)](https://github.com/SakanaAI/ShinkaEvolve) | `program-evolution`<br>`novelty`<br>`ai-training` | • **Bounded optimization**<br>• **Loop:** Evolves programs with parent sampling, novelty rejection and bandit-based LLM selection; evaluated successors re-enter the archive, including experiments on AI training-loss design.<br>• **Boundary:** The evaluator and evolutionary machinery are supplied by researchers; generating its own problems is a proposed extension, not a demonstrated feature.<br>• [Evidence](https://sakana.ai/shinka-evolve/) |

#### Artifacts / Learned Skills

Skills are created and revised from experience for reuse across later tasks, not simply bundled as a static library.

| Project | Link | Stars | Tags | Improvement Loop and Boundary |
| --- | --- | ---: | --- | --- |
| Hermes Agent / Learned Skills | [GitHub](https://github.com/NousResearch/hermes-agent) | [![star: 243,353](https://img.shields.io/badge/star-243353-f4b400?style=flat-square)](https://github.com/NousResearch/hermes-agent) | `learned-skills`<br>`procedural-memory`<br>`experience` | • **Experience learning**<br>• **Loop:** Creates procedural skills after complex tasks and revises them during use; persistent skills and searchable experience are reused across sessions.<br>• **Boundary:** This is experience-driven skill persistence, not model-weight training or independently demonstrated monotonic capability growth.<br>• [Evidence](https://github.com/NousResearch/hermes-agent) |

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
- [Taxonomy](docs/taxonomy_iterations.md)
- [Contributing](CONTRIBUTING.md)
