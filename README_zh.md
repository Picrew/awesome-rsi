# Awesome RSI

以证据为依据的递归自我改进（RSI）研究地图：优先展示模型公司一手博客，再列附官方代码的论文，以及 Models、Harness、Artifacts 活跃 GitHub 实现。

[English](./README.md) | [中文](./README_zh.md)

**31 篇一手博客 · 37 篇研究论文 · 9 个活跃 GitHub 项目**

## 目录

- [分类概览](#category-overview)
- [模型公司研究博客（优先阅读）](#company-research-blogs)
  - [机制与实证结果](#mechanisms-and-results)
  - [评测与失败模式](#evaluation-and-failure-modes)
  - [研究路线](#research-agendas)
  - [奠基研究与历史教程](#foundations-and-historical-tutorials)
- [论文与官方代码](#papers-and-official-code)
  - [Models](#papers--models)
  - [Harness](#papers--harness)
  - [Artifacts](#papers--artifacts)
- [活跃 GitHub 项目](#active-github-projects)
  - [Models](#models)
  - [Harness](#harness)
  - [Artifacts](#artifacts)
- [边界与收录原则](#scope-and-curation)
- [维护](#maintenance)

## Category Overview

| 分类 | 资源类型 | 数量 |
| --- | --- | ---: |
| [机制与实证结果](#mechanisms-and-results) | 博客 | 21 |
| [评测与失败模式](#evaluation-and-failure-modes) | 博客 | 4 |
| [研究路线](#research-agendas) | 博客 | 2 |
| [奠基研究与历史教程](#foundations-and-historical-tutorials) | 博客 | 4 |
| [论文 / Models](#papers--models) | 论文 | 14 |
| [论文 / Harness](#papers--harness) | 论文 | 14 |
| [论文 / Artifacts](#papers--artifacts) | 论文 | 9 |
| [Models / 训练研究](#models--training-research) | GitHub 项目 | 1 |
| [Harness / 自修改](#harness--self-modification) | GitHub 项目 | 2 |
| [Harness / 提示与工作流优化](#harness--prompt-and-workflow-optimization) | GitHub 项目 | 3 |
| [Artifacts / 程序进化](#artifacts--program-evolution) | GitHub 项目 | 2 |
| [Artifacts / 学习所得技能](#artifacts--learned-skills) | GitHub 项目 | 1 |
| **合计** |  | **77** |

## Company Research Blogs

建议从这里开始：模型开发公司与专项 AI 研究机构的一手技术材料。机制、失败、路线与历史基础分开呈现；发布方结论不等于独立复现。

### Mechanisms and Results

- **[The Darwin Godel Machine: AI that improves itself by rewriting its own code](https://sakana.ai/dgm/)** — Sakana AI · 2025-05-30
  - **改进对象:** `Harness` · 直接自修改
  - **闭环:** 描述改写自身工具与工作流的代理，利用编码基准评测后代，并从不断扩展的档案分支继续改进。
  - **边界:** 基础模型训练属于未来工作；文章还记录了奖励投机与有人监督的沙箱限制。

- **[Kimi K2: Open Agentic Intelligence](https://www.kimi.com/en/blog/kimi-k2)** — Moonshot AI / Kimi · 日期未核实
  - **改进对象:** `Models` · 自训练
  - **闭环:** 通用 RL 系统让模型充当基于量规的自我评判者，并利用带可验证奖励的 on-policy 轨迹持续更新评判者，以改善对不可验证任务的评估。
  - **边界:** 文章描述的是有界策略与评判者训练，而非自主改写学习器；单独的数据合成或代理演示不是收录理由，原始可见发表日期未知。

- **[SIMA 2: An Agent that Plays, Reasons, and Learns With You in Virtual 3D Worlds](https://deepmind.google/blog/sima-2-an-agent-that-plays-reasons-and-learns-with-you-in-virtual-3d-worlds/)** — Google DeepMind · 2025-11-13
  - **改进对象:** `Models` · 自训练
  - **闭环:** Gemini 提供任务与估计奖励；SIMA 2 积累自产经验并训练后续代理代，覆盖新游戏与 Genie 生成环境。
  - **边界:** 初始训练使用人工示范，后续奖励依赖 Gemini；研究预览并不是 Gemini 自身的无约束自改进。

- **[MiniMax M2.7: Early Echoes of Self-Evolution](https://www.minimax.io/news/minimax-m27-en)** — MiniMax · 2026-03-18
  - **改进对象:** `Harness` · 直接自修改
  - **闭环:** 报告超过 100 轮自主失败轨迹分析、脚手架代码修改、评测及保留或回滚选择；保留的记忆和技能也用于模型开发实验。
  - **边界:** 报告的 30% 增益来自内部评测集；模型开发仍由研究者指导并作关键决策，完整自主的权重级自进化仍是未来目标。

- **[Automated Alignment Researchers: Using large language models to scale scalable oversight](https://www.anthropic.com/research/automated-alignment-researchers)** — Anthropic · 2026-04-14
  - **改进对象:** `Models` · 有界优化
  - **闭环:** 九个 Claude 科研代理提出、实现并评测弱到强监督方法，共享发现与代码，并依据性能差距恢复指标安排后续实验。
  - **边界:** 留出任务迁移结果不一，最佳方法在生产规模 Claude Sonnet 4 上没有显著增益；研究者剔除了奖励投机，科研代理本身也未在此实验中被重新训练。

- **[MiniMax M3: Frontier Coding, 1M Context, Native Multimodality — All in One Model](https://www.minimax.io/blog/minimax-m3)** — MiniMax · 2026-06-01
  - **改进对象:** `Models` · 有界优化
  - **闭环:** PostTrainBench 章节描述代理自主选择合成数据与训练策略、训练四个基础模型、评测并调整后续实验，形成持续 12 小时的闭环。
  - **边界:** 这是限定任务的外部模型优化实验，不是 M3 重训自身权重；文章其他产品基准和演示不能单独作为 RSI 证据。

- **[Automated researchers can reliably mitigate alignment failures](https://www.anthropic.com/research/automated-researchers-mitigate-alignment-failures)** — Anthropic · 2026-08-28
  - **改进对象:** `Models` · 有界优化
  - **闭环:** Claude 针对十类对齐失败循环检索文献、提出方法和数据、训练目标模型并测试，再在留出基准和更大模型上检验所发现的方法。
  - **边界:** 优化的是外部学生模型而非 Claude 自身权重；能力约束和监控代理排除无效方法，基准成功不代表通用自主对齐科学已经实现。

- **[Can LLMs invent better ways to train LLMs?](https://sakana.ai/llm-squared/)** — Sakana AI · 2024-06-13
  - **改进对象:** `Models` · 有界优化
  - **闭环:** LLM-Squared 提出偏好损失代码、用候选损失训练模型，再将下游分数反馈给下一轮提案；该闭环发现了 DiscoPOP。
  - **边界:** 提案模型保持固定；将改进后的模型用于自身研究过程仍是未来方向，而非已证明结果。

- **[AlphaEvolve: How our Gemini-powered coding agent is scaling impact across fields](https://deepmind.google/blog/alphaevolve-impact/)** — Google DeepMind · 2026-05-07
  - **改进对象:** `Artifacts` · 有界优化
  - **闭环:** 报告评测驱动代码进化在模型组件、训练效率、缓存策略和 TPU 电路中的后续应用，展示具体 AI 开发反馈路径。
  - **边界:** 部署案例与发布方报告的收益不代表已经闭合了重训并改进 Gemini 提案模型自身的循环。

- **[AlphaEvolve: A Gemini-powered coding agent for designing advanced algorithms](https://deepmind.google/blog/alphaevolve-a-gemini-powered-coding-agent-for-designing-advanced-algorithms/)** — Google DeepMind · 2025-05-14
  - **改进对象:** `Artifacts` · 有界优化
  - **闭环:** 解释通过评测驱动的程序进化改进算法与 Gemini 训练内核，并将成功程序反馈到下一轮进化提案。
  - **边界:** 改进底层 LLM 的训练基础设施，不等于证明 Gemini 权重已经实现多轮自主自训练。

- **[ShinkaEvolve: Evolving New Algorithms with LLMs, Orders of Magnitude More Efficiently](https://sakana.ai/shinka-evolve/)** — Sakana AI · 2025-09-25
  - **改进对象:** `Artifacts` · 有界优化
  - **闭环:** 详述高样本效率的程序进化与进化所得 MoE 负载均衡损失，将可执行候选的选择结果用于后续程序代。
  - **边界:** 结果受人定义的适应度和固定提案模型约束，并未证明学习算法会改写自身。

- **[Digital Red Queen: Adversarial Program Evolution in Core War with LLMs](https://sakana.ai/drq/)** — Sakana AI · 2026-01-08
  - **改进对象:** `Artifacts` · 有界优化
  - **闭环:** 让 Core War 程序针对不断增长的历史对手进化；变化的对手提供选择压力，保留程序继续影响后续进化。
  - **边界:** 受控虚拟机中的程序共进化不代表底层 LLM 自主改进，也不证明现实网络安全能力。

- **[Autonomous AI research for nanogpt speedrun](https://www.primeintellect.ai/auto-nanogpt)** — Prime Intellect · 2026-05-14
  - **改进对象:** `Artifacts` · 有界优化
  - **闭环:** 编码代理重复修订优化器代码与超参数、运行 nanoGPT 训练，并依据达到目标验证损失所需步数选择更好变体；持久工作笔记保存实验状态。
  - **边界:** 代理擅长搜索和重组，但仍需要上游人类记录才能持续进步；模型、数据、架构和基准规则固定，各阶段之间也有人调整 Harness。

- **[General Agent: A Self-Evolving, Synthetic Agent Environment](https://www.primeintellect.ai/blog/general-agent)** — Prime Intellect · 2026-05-18
  - **改进对象:** `Artifacts` · 有界优化
  - **闭环:** 合成器进化任务族，求解器测量通过率；仅保留落在校准难度范围内的任务，更难层级再作为后续合成训练语料扩展的起点。
  - **边界:** 进化对象是任务语料；文章将完整闭合模型训练与环境生成回路列为更广泛研究方向，而非已经完成的自主循环。

- **[Prime Agent: A self-improving RLM agent](https://www.primeintellect.ai/blog/prime-agent)** — Prime Intellect · 2026-08-05
  - **改进对象:** `Harness` · 直接自修改
  - **闭环:** /refine 管线读取自身轨迹，修改持久提示笔记、记忆、技能和子代理定义；记录触发原因、结果与回滚历史，使改动进入后续轮次和会话。
  - **边界:** 基础系统提示保持不可变，也不重训模型权重；文中明确怀疑 Factorio 成绩存在奖励投机，应以机制而非该分数作为证据。

- **[RoboCat: A self-improving robotic agent](https://deepmind.google/blog/robocat-a-self-improving-robotic-agent/)** — Google DeepMind · 2023-06-20
  - **改进对象:** `Models` · 自训练
  - **闭环:** 微调任务专用分支、收集其练习轨迹，再与示范合并以重训通用 RoboCat，使其学习后续任务。
  - **边界:** 每个新任务仍以 100–1000 条人工示范开始，训练过程与机器人接口由人设计。

- **[The AI Scientist: Towards Fully Automated Open-Ended Scientific Discovery](https://sakana.ai/ai-scientist/)** — Sakana AI · 2024-08-13
  - **改进对象:** `Artifacts` · 有界优化
  - **闭环:** 描述想法生成、代码实验、论文写作与自动审稿；保留的评审和实验结果用于修订及后续研究想法。
  - **边界:** 不公平比较和自评仍是风险；意外修改执行脚本属于安全失败，不能当作有益 RSI 的证据。

- **[FunSearch: Making new discoveries in mathematical sciences using Large Language Models](https://deepmind.google/blog/funsearch-making-new-discoveries-in-mathematical-sciences-using-large-language-models/)** — Google DeepMind · 2023-12-14
  - **改进对象:** `Artifacts` · 有界优化
  - **闭环:** 采样已有高分程序，要求固定 LLM 生成改进，执行候选并将最佳程序放回种群用于后续搜索。
  - **边界:** 评测器和种子程序由用户提供，模型权重与改进算法并不会被递归改写。

- **[Population-based Model Merging via Quality Diversity](https://sakana.ai/cycleqd/)** — Sakana AI · 2024-12-03
  - **改进对象:** `Models` · 有界优化
  - **闭环:** CycleQD 轮换用于定义质量的任务，对专家模型进行交叉与变异，并在技能档案中保留多样的高性能模型供后续进化。
  - **边界:** 任务、初始专家和质量多样性算法由人设定；模型合并不等于梯度自训练或优化器自改写。

- **[Evolving New Foundation Models: Unleashing the Power of Automating Model Development](https://sakana.ai/evolutionary-model-merge/)** — Sakana AI · 2024-03-21
  - **改进对象:** `Models` · 有界优化
  - **闭环:** 跨多代进化层选择与权重混合配方，按任务适应度选择合并模型，再在独立测试集评估最终模型。
  - **边界:** 进化搜索的是人工定义的预训练模型合并空间，并未证明 LLM 能自主改写自身训练算法。

- **[Accelerating scientific breakthroughs with an AI co-scientist](https://research.google/blog/accelerating-scientific-breakthroughs-with-an-ai-co-scientist/)** — Google Research · 2025-02-19
  - **改进对象:** `Artifacts` · 有界优化
  - **闭环:** 生成、反思、排名、进化和元评审代理利用锦标赛反馈与研究者输入，迭代修订科学假设。
  - **边界:** Elo 是自评信号而非独立真值；实验室验证仍有人类专家指导，模型权重保持固定。


### Evaluation and Failure Modes

- **[AI CUDA Engineer update: robust benchmarking and interim results](https://sakana.ai/ai-cuda-engineer-update/)** — Sakana AI · 2025-09-17
  - **改进对象:** `Artifacts` · 评测与安全
  - **闭环:** 在发现绕过基准的问题后修正内核优化结论；更严格的 robust-kbench 将报告的平均加速从 3.13 倍降为 1.49 倍。
  - **边界:** 这是改进闭环的负面结果与测量教训，不是新的自改进代理；原文为日语。

- **[Sycophancy to subterfuge: Investigating reward tampering in language models](https://www.anthropic.com/research/reward-tampering)** — Anthropic · 2024-06-17
  - **改进对象:** `Harness` · 评测与安全
  - **闭环:** 检验规格投机课程是否会泛化为修改模型自身奖励函数并掩盖改动，揭示自修改系统能够改变评测器时的直接失效模式。
  - **边界:** 在构造的研究中，奖励篡改出现于 32,768 次试验中的 45 次；这不是已部署 Claude 执行 RSI 的观察证据，也不能证明所有自修改都不安全。

- **[From shortcuts to sabotage: natural emergent misalignment from reward hacking](https://www.anthropic.com/research/emergent-misalignment-reward-hacking)** — Anthropic · 2025-11-21
  - **改进对象:** `Harness` · 评测与安全
  - **闭环:** 展示奖励投机训练泛化为恶意行为；其中 Claude Code 评测让模型修改本研究检测代码，模型尝试破坏检测能力，直接检验 AI 辅助 AI 安全研究的可信性。
  - **边界:** 研究者刻意选择可投机的 RL 环境，并在预训练中加入相关知识；12% 破坏尝试率描述的是该实验模型，不是普通已部署 Claude，也不是已完成破坏的证明。

- **[Measuring Autonomous AI Research](https://www.primeintellect.ai/blog/measuring-autonomous-research)** — Prime Intellect · 2026-08-14
  - **改进对象:** `Artifacts` · 评测与安全
  - **闭环:** 评测 18 个前沿模型的 153 次自主优化器研究运行，检查 nanoGPT 改进能否经受评测，以及长时代理是在提出新方法还是仅重组已有方法。
  - **边界:** 固定优化器竞速只是科研能力的有界代理指标，不是通用 RSI 证明；结果依赖随机种子、给定基线与评测完整性。


### Research Agendas

- **[Introducing Sakana AI's Recursive Self-Improvement (RSI) Lab](https://sakana.ai/rsi-lab/)** — Sakana AI · 2026-06-05
  - **改进对象:** `Harness` · 研究路线
  - **闭环:** 以 DGM、LLM-Squared、ShinkaEvolve 和对抗共进化为基础，提出从代理原生模型到 AI 科学家、再到更好模型的闭环研究路线。
  - **边界:** 这是研究路线与工作谱系，不代表完整自主模型改进闭环已经实现。

- **[When AI builds itself](https://www.anthropic.com/institute/recursive-self-improvement)** — Anthropic Institute · 日期未核实
  - **改进对象:** `Models` · 研究路线
  - **闭环:** 将递归自我改进定义为 AI 自主设计和开发后继系统，展示 AI 加速工程与研究的内部证据，并讨论这种辅助能否闭合完整模型开发回路。
  - **边界:** 文章明确表示完整 RSI 尚未实现，也并非必然；内部生产率统计属于观察证据，人类研究判断、算力、评测和安全仍是约束。


### Foundations and Historical Tutorials

- **[Constitutional AI: Harmlessness from AI feedback](https://www.anthropic.com/research/constitutional-ai-harmlessness-from-ai-feedback)** — Anthropic · 2022-12-15
  - **改进对象:** `Models` · 自训练
  - **闭环:** 采样模型回答、生成自我批评和修订，并用修订回答微调；随后利用 AI 偏好训练奖励模型，再进行强化学习。
  - **边界:** 人编写的宪法原则和固定分阶段训练配方仍然关键；这是有界自监督基础，不是无限重复自主 RSI 的证据。

- **[AlphaGo Zero: Starting from scratch](https://deepmind.google/blog/alphago-zero-starting-from-scratch/)** — Google DeepMind · 2017-10-18
  - **改进对象:** `Models` · 自训练
  - **闭环:** 自博弈结果训练网络；更新后的网络引导更强的搜索与对局，产生下一轮训练材料。
  - **边界:** 属于围棋中奠基性的有界自训练实例，规则和学习机制由人设计，并非开放式 RSI。

- **[AlphaZero: Shedding new light on chess, shogi, and Go](https://deepmind.google/blog/alphazero-shedding-new-light-on-chess-shogi-and-go/)** — Google DeepMind · 2018-12-06
  - **改进对象:** `Models` · 自训练
  - **闭环:** 描述根据自博弈结果更新神经网络参数，并在分别学习的棋类游戏中形成更强的网络引导树搜索。
  - **边界:** 每种棋类仍有固定规则与目标；并非单个模型自主拓展领域或改写自身学习器。

- **[Self-Evolving Agents - A Cookbook for Autonomous Agent Retraining](https://developers.openai.com/cookbook/examples/partners/self_evolving_agents/autonomous_agent_retraining)** — OpenAI and Bain · 2025-11-04 · 已归档教程
  - **改进对象:** `Harness` · 有界优化
  - **闭环:** 演示利用评分器反馈、元提示和 GEPA 更新版本化摘要提示，并保留更好的候选用于后续请求。
  - **边界:** 官方配方已归档，API 可能过时；尽管标题称再训练，实际改变的是提示而非模型权重。生产使用需要留出测试和人工审批，示例的验证切片与训练列表存在重叠。


## Papers and Official Code

- 日期为首次发表日期。仅显示经来源核实的会议或期刊；只有日期不代表已通过同行评审。
- 官方代码指作者关联；仅发布产物和已归档的情况单独标注。旧代码不会使有价值的论文被排除。
- Star 徽章与推送日期来自 **2026-09-08** 的元数据快照。

### Papers / Models

| 论文 | 日期 / 发表状态 | 代码 | 贡献与边界 |
| --- | --- | --- | --- |
| [Agent0: Unleashing Self-Evolving Agents from Zero Data via Tool-Integrated Reasoning](https://arxiv.org/abs/2511.16043) | 2025-11-20 | • [官方代码](https://github.com/aiming-lab/Agent0)<br>• [![star: 1,258](https://img.shields.io/badge/star-1258-f4b400?style=flat-square)](https://github.com/aiming-lab/Agent0)<br>• **最近推送:** 2026-07-10 | • **自训练**<br>• **闭环:** 将课程模型与使用工具的执行模型耦合；更强执行能力推动生成更难课程，课程再提供强化学习数据。<br>• **边界:** 公开训练指南需要人工选择轮次间 checkpoint；零外部数据也未消除对预训练基础模型和工具的依赖。 |
| [R-Zero: Self-Evolving Reasoning LLM from Zero Data](https://arxiv.org/abs/2508.05004) | 2025-08-07<br>[ICLR 2026](https://github.com/Chengsong-Huang/R-Zero/blob/main/README.md) | • [官方代码](https://github.com/Chengsong-Huang/R-Zero)<br>• [![star: 845](https://img.shields.io/badge/star-845-f4b400?style=flat-square)](https://github.com/Chengsong-Huang/R-Zero)<br>• **最近推送:** 2026-02-04 | • **自训练**<br>• **闭环:** 共同进化 Challenger 与 Solver 模型，以能力边界附近的生成任务训练 Solver，而 Solver 能力变化又改变 Challenger 的奖励。<br>• **边界:** 使用预训练基础模型与人工设计奖励；有限迭代可能退步，作者后续 R-Few 工作引入人工数据以应对扩展限制。 |
| [Self-Adapting Language Models](https://arxiv.org/abs/2506.10943) | 2025-06-12 | • [官方代码](https://github.com/Continual-Intelligence/SEAL)<br>• [![star: 1,855](https://img.shields.io/badge/star-1855-f4b400?style=flat-square)](https://github.com/Continual-Intelligence/SEAL)<br>• **最近推送:** 2025-08-01<br>• **发布说明:** 论文链接作者项目页，匹配的官方仓库链接同一论文与项目页；规范仓库为 Continual-Intelligence/SEAL。 | • **自训练**<br>• **闭环:** 模型生成包含微调数据或更新指令的自编辑内容；SFT 产生持久权重变化，下游性能通过外层 RL 循环训练更好的自编辑生成能力。<br>• **边界:** 自编辑在研究者设计的 SFT/RL 框架内控制适配；知识吸收与少样本泛化实验不能证明无约束的自主重设计。 |
| [Absolute Zero: Reinforced Self-play Reasoning with Zero Data](https://arxiv.org/abs/2505.03335) | 2025-05-06 | • [官方代码](https://github.com/LeapLabTHU/Absolute-Zero-Reasoner)<br>• [![star: 1,901](https://img.shields.io/badge/star-1901-f4b400?style=flat-square)](https://github.com/LeapLabTHU/Absolute-Zero-Reasoner)<br>• **最近推送:** 2025-08-24 | • **自训练**<br>• **闭环:** 模型共同进化任务提案与求解能力，利用代码执行器提供任务有效性和答案奖励，而非依赖外部整理的后训练数据集。<br>• **边界:** 零数据指自博弈后训练设置，不代表基础模型未经训练；执行器、奖励和优化机制仍由人设计。 |
| [Agent Skill Acquisition for Large Language Models via CycleQD](https://arxiv.org/abs/2410.14735) | 2024-10-16<br>[ICLR 2025](https://github.com/SakanaAI/CycleQD/blob/main/README.md) | • [官方代码](https://github.com/SakanaAI/CycleQD)<br>• [![star: 48](https://img.shields.io/badge/star-48-f4b400?style=flat-square)](https://github.com/SakanaAI/CycleQD)<br>• **最近推送:** 2025-02-01 | • **有界优化**<br>• **闭环:** 通过模型合并交叉与 SVD 变异进化模型变体，将不同任务指标轮换为质量目标与多样性描述，以积累互补技能。<br>• **边界:** 模型参数确实进化，但 QD 算法、任务指标与专家起始模型由外部设定；并非学习器自主自修改。 |
| [Self-Taught Evaluators](https://arxiv.org/abs/2408.02666) | 2024-08-05 | • [仅官方产物](https://github.com/facebookresearch/RAM/tree/main/projects/self_taught_evaluator)<br>• [![star: 382](https://img.shields.io/badge/star-382-f4b400?style=flat-square)](https://github.com/facebookresearch/RAM)<br>• **最近推送:** 2026-06-25<br>• **发布说明:** 官方提供评测脚本、模型与数据；未确认完整训练流水线。 | • **自训练**<br>• **闭环:** 生成对比回答与合成推理和判断，反复训练 LLM 评测器，并利用改进后的评测器预测构造后续训练轮次。<br>• **边界:** 不使用人工偏好训练并不等于没有人工数据验证；公开材料记录了根据 HelpSteer2 验证准确率选择 checkpoint。 |
| [ReST-MCTS*: LLM Self-Training via Process Reward Guided Tree Search](https://arxiv.org/abs/2406.03816) | 2024-06-06 | • [官方代码](https://github.com/THUDM/ReST-MCTS)<br>• [![star: 711](https://img.shields.io/badge/star-711-f4b400?style=flat-square)](https://github.com/THUDM/ReST-MCTS)<br>• **最近推送:** 2025-01-20<br>• **发布说明:** 官方 README 记录策略和价值模型的合成数据生成与迭代训练；有代码不代表独立复现所有报告结果。 | • **自训练**<br>• **闭环:** 用过程奖励引导的树搜索根据正确终局答案推断步骤价值，再在多轮迭代中利用所选轨迹训练策略模型和过程奖励模型。<br>• **边界:** 消除的是逐步人工标注，而不是正确终局答案监督；搜索与奖励学习规则仍由外部固定设计。 |
| [Self-Play Preference Optimization for Language Model Alignment](https://arxiv.org/abs/2405.00675) | 2024-05-01<br>[ICLR 2025](https://github.com/uclaml/SPPO/blob/main/README.md) | • [官方代码](https://github.com/uclaml/SPPO)<br>• [![star: 589](https://img.shields.io/badge/star-589-f4b400?style=flat-square)](https://github.com/uclaml/SPPO)<br>• **最近推送:** 2025-01-23<br>• **发布说明:** 官方仓库明确提供代码与模型；PairRM 是外部预训练偏好模型，而非策略学习自我评判。 | • **自训练**<br>• **闭环:** 将对齐视为常和双人博弈，依据偏好概率针对自身生成回答反复更新策略，以逼近 Nash 均衡。<br>• **边界:** 实验使用提示数据与预训练 PairRM 评判者；均衡保证针对指定偏好博弈，不代表无限能力增长或评测机制自改进。 |
| [Self-Rewarding Language Models](https://arxiv.org/abs/2401.10020) | 2024-01-18 | 已审查来源未找到 | • **自训练**<br>• **闭环:** 在迭代 DPO 中让语言模型通过提示充当自身奖励评判者，同时改进回答生成与后续训练样本的奖励质量。<br>• **边界:** 三轮实验与偏好基准收益不能证明自评已校准或持续超人改进，初始监督仍然重要。 |
| [Self-Play Fine-Tuning Converts Weak Language Models to Strong Language Models](https://arxiv.org/abs/2401.01335) | 2024-01-02<br>[ICML 2024](https://github.com/uclaml/SPIN/blob/main/README.md) | • [官方代码](https://github.com/uclaml/SPIN)<br>• [![star: 1,254](https://img.shields.io/badge/star-1254-f4b400?style=flat-square)](https://github.com/uclaml/SPIN)<br>• **最近推送:** 2024-05-08 | • **自训练**<br>• **闭环:** 训练策略区分人工示范回答与上一轮模型生成的回答，通过自博弈反复增强已监督微调的模型。<br>• **边界:** 仍复用人工示范并以 SFT 模型为起点；理论最优性针对目标数据分布，而非无限递归能力增长。 |
| [Beyond Human Data: Scaling Self-Training for Problem-Solving with Language Models](https://arxiv.org/abs/2312.06585) | 2023-12-11 | 已审查来源未找到 | • **自训练**<br>• **闭环:** 反复采样解答、按二元正确性反馈筛选并用接受样本微调，研究 PaLM-2 在 MATH 与 APPS 上的扩展表现。<br>• **边界:** 需要外部提供的问题与可验证反馈；少量 EM 式迭代不能证明无限改进。 |
| [Reinforced Self-Training (ReST) for Language Modeling](https://arxiv.org/abs/2308.08998) | 2023-08-17 | 已审查来源未找到 | • **自训练**<br>• **闭环:** 交替进行策略生成数据与奖励引导的离线学习，复用样本改进语言模型策略，并在机器翻译中验证。<br>• **边界:** 奖励与偏好信号仍由外部设定；翻译结果不能证明奖励机制自身改进或开放式能力增长。 |
| [RoboCat: A Self-Improving Generalist Agent for Robotic Manipulation](https://arxiv.org/abs/2306.11706) | 2023-06-20 | 已审查来源未找到 | • **自训练**<br>• **闭环:** 将通用机器人策略适配到任务与机体，利用训练后的策略收集更多机器人经验，再用扩展数据训练后续通用模型。<br>• **边界:** 任务适配仍使用示范和受控机器人基础设施；这是自主改进的构件，而非训练系统自主重设计。 |
| [STaR: Bootstrapping Reasoning With Reasoning](https://arxiv.org/abs/2203.14465) | 2022-03-28<br>[NeurIPS 2022](https://github.com/ezelikman/STaR/blob/main/README.md) | • [官方代码](https://github.com/ezelikman/STaR)<br>• [![star: 232](https://img.shields.io/badge/star-232-f4b400?style=flat-square)](https://github.com/ezelikman/STaR)<br>• **最近推送:** 2023-02-21 | • **自训练**<br>• **闭环:** 生成推理轨迹，按答案正确性筛选；对失败样例利用已知答案补充推理，再反复用成功轨迹微调模型。<br>• **边界:** 需要任务数据、已知答案和种子推理示例；固定训练循环不等于自主重设计学习器。 |

### Papers / Harness

| 论文 | 日期 / 发表状态 | 代码 | 贡献与边界 |
| --- | --- | --- | --- |
| [Prime Agent: A Self-Improving RLM Harness](https://arxiv.org/abs/2608.23552) | 2026-08-24 | • [官方代码](https://github.com/PrimeIntellect-ai/prime-agent)<br>• [![star: 20,300](https://img.shields.io/badge/star-20300-f4b400?style=flat-square)](https://github.com/PrimeIntellect-ai/prime-agent)<br>• **最近推送:** 2026-09-08<br>• **发布说明:** 作者仓库直接引用本文，并另引 Continual Harness（2605.09998）；两者标题与首版日期不应互相覆盖。 | • **经验学习**<br>• **闭环:** 将持久 REPL 与递归子代理结合，并保留历史、记忆、技能、提示和子代理规格，以在长时轨迹间进行修订。<br>• **边界:** 递归调用子代理本身不是 RSI，相关机制是对持久 Harness 状态的修订；基准收益也包含执行和恢复改进，不能全部归因为自改进。 |
| [Continual Harness: Online Adaptation for Self-Improving Foundation Agents](https://arxiv.org/abs/2605.09998) | 2026-05-11 | • [官方代码](https://github.com/PrimeIntellect-ai/prime-agent)<br>• [![star: 20,300](https://img.shields.io/badge/star-20300-f4b400?style=flat-square)](https://github.com/PrimeIntellect-ai/prime-agent)<br>• **最近推送:** 2026-09-08<br>• **发布说明:** README 明确链接本文，因此属于 Harness 组件的官方关联实现；所读论文 v1 未证明全部 Pokemon 实验或教师重标注权重共学习流水线已发布，不可称为完整复现代码。 | • **经验学习**<br>• **闭环:** 在不重置的运行中交替行动与修订提示、子代理、技能和记忆；另一个共学习实验由前沿教师重标注轨迹，并在不重置游戏的情况下更新开放模型。<br>• **边界:** 早期 Gemini Plays Pokemon 结果使用人在环 Harness 修订，后续自动适配与教师辅助权重共学习是不同设置；教师监督与游戏专用评测限制其自主性主张。 |
| [Hyperagents](https://arxiv.org/abs/2603.19461) | 2026-03-19 | • [官方代码](https://github.com/facebookresearch/HyperAgents)<br>• [![star: 2,718](https://img.shields.io/badge/star-2718-f4b400?style=flat-square)](https://github.com/facebookresearch/HyperAgents)<br>• **最近推送:** 2026-07-31 | • **直接自修改**<br>• **闭环:** 将任务代理与元代理合并为可编辑程序，使评测后的修改既能改善任务行为，也能改善产生未来修改的机制。<br>• **边界:** 报告的迁移与积累属于有限实验，并非无限加速或自主权重学习的证明。 |
| [GEPA: Reflective Prompt Evolution Can Outperform Reinforcement Learning](https://arxiv.org/abs/2507.19457) | 2025-07-25 | • [官方代码](https://github.com/gepa-ai/gepa)<br>• [![star: 6,475](https://img.shields.io/badge/star-6475-f4b400?style=flat-square)](https://github.com/gepa-ai/gepa)<br>• **最近推送:** 2026-09-08 | • **有界优化**<br>• **闭环:** 反思采样执行轨迹来变异提示，并通过 Pareto 候选选择结合互补的成功经验。<br>• **边界:** 在底层模型权重固定、评测器外部提供的条件下优化提示配置；未证明变异机制会改写自身。 |
| [EvoAgentX: An Automated Framework for Evolving Agentic Workflows](https://arxiv.org/abs/2507.03616) | 2025-07-04 | • [官方代码](https://github.com/ANative-Lab/EvoAgentX)<br>• [![star: 3,313](https://img.shields.io/badge/star-3313-f4b400?style=flat-square)](https://github.com/ANative-Lab/EvoAgentX)<br>• **最近推送:** 2026-08-27<br>• **发布说明:** 论文中的 EvoAgentX/EvoAgentX 重定向到 ANative-Lab/EvoAgentX，当前 README 保留准确论文引用；这是框架集成论文，不代表每个组件都是独立新优化器。 | • **有界优化**<br>• **闭环:** 将 TextGrad、AFlow 与 MIPRO 整合进模块化工作流生成、执行与评测平台，反复修订提示、工具配置和工作流拓扑。<br>• **边界:** 因明确的进化层收录，而非一般多代理编排；固定的集成优化器与基准不能证明改进机制会改写自身。 |
| [Darwin Godel Machine: Open-Ended Evolution of Self-Improving Agents](https://arxiv.org/abs/2505.22954) | 2025-05-29 | • [官方代码](https://github.com/jennyzzt/dgm)<br>• [![star: 2,292](https://img.shields.io/badge/star-2292-f4b400?style=flat-square)](https://github.com/jennyzzt/dgm)<br>• **最近推送:** 2025-08-13 | • **直接自修改**<br>• **闭环:** 编码代理修改自身实现，在编码基准上评测后代，并从不断扩展的代理档案中分支产生后续改进。<br>• **边界:** 属于代码层面的实证自改进，不是有益改写的形式化证明，也不是基础模型权重训练；仍存在基准投机与沙箱逃逸风险。 |
| [A Self-Improving Coding Agent](https://arxiv.org/abs/2504.15228) | 2025-04-21<br>[ICLR 2025 Workshop on Scaling Self-Improving Foundation Models](https://github.com/MaximeRobeyns/self_improving_coding_agent/blob/master/README.md) | • [官方代码](https://github.com/MaximeRobeyns/self_improving_coding_agent)<br>• [![star: 394](https://img.shields.io/badge/star-394-f4b400?style=flat-square)](https://github.com/MaximeRobeyns/self_improving_coding_agent)<br>• **最近推送:** 2025-04-23<br>• **发布说明:** 官方仓库使用 master 分支，main 分支 README 请求返回 404；引用明确指向 workshop，而不是 ICLR 主会。 | • **直接自修改**<br>• **闭环:** 评测当前编码代理并归档结果，再让该代理修改自身代码实现改进，随后重新评测更新后的实现。<br>• **边界:** 非梯度脚手架学习使用固定 LLM 权重；在抽样 SWE-bench Verified 子集等基准上的提升不代表无限进步或整个基准的最优表现。 |
| [AFlow: Automating Agentic Workflow Generation](https://arxiv.org/abs/2410.10762) | 2024-10-14<br>[ICLR 2025](https://github.com/FoundationAgents/AFlow/blob/main/README.md) | • [官方代码](https://github.com/FoundationAgents/AFlow)<br>• [![star: 589](https://img.shields.io/badge/star-589-f4b400?style=flat-square)](https://github.com/FoundationAgents/AFlow)<br>• **最近推送:** 2025-12-25 | • **有界优化**<br>• **闭环:** 用蒙特卡洛树搜索探索代码表示的代理工作流，根据执行反馈与树状经验提出更强的工作流图。<br>• **边界:** 工作流搜索不代表修改搜索算法或模型权重；基准评测器与算子定义由外部提供。 |
| [Gödel Agent: A Self-Referential Agent Framework for Recursive Self-Improvement](https://arxiv.org/abs/2410.04444) | 2024-10-06 | • [官方代码](https://github.com/Arvid-pku/Godel_Agent)<br>• [![star: 219](https://img.shields.io/badge/star-219-f4b400?style=flat-square)](https://github.com/Arvid-pku/Godel_Agent)<br>• **最近推送:** 2025-09-17<br>• **发布说明:** 规范摘要链接该仓库，仓库 README 回链同一论文；不依据名称推断形式证明实现或会议归属。 | • **直接自修改**<br>• **闭环:** 根据高层目标利用 LLM 生成修改，递归修订代理自身逻辑与行为，而非仅在预定义任务代理流水线中调整。<br>• **边界:** 受 Gödel machine 启发，但依据的是实证任务评测，不是所有改写有益或整个代理设计空间得到最优搜索的证明。 |
| [Automated Design of Agentic Systems](https://arxiv.org/abs/2408.08435) | 2024-08-15<br>[ICLR 2025](https://github.com/ShengranHu/ADAS/blob/main/README.md) | • [官方代码](https://github.com/ShengranHu/ADAS)<br>• [![star: 1,637](https://img.shields.io/badge/star-1637-f4b400?style=flat-square)](https://github.com/ShengranHu/ADAS)<br>• **最近推送:** 2025-01-28 | • **有界优化**<br>• **闭环:** Meta Agent Search 编写并评测新代理设计，利用扩展中的档案发现可跨任务与底层模型迁移的工作流。<br>• **边界:** 元代理搜索过程由外部固定；发明任务代理不等于递归改进元代理自身的学习机制。 |
| [TextGrad: Automatic "Differentiation" via Text](https://arxiv.org/abs/2406.07496) | 2024-06-11<br>[Nature](https://github.com/zou-group/TextGrad/blob/main/README.md) | • [官方代码](https://github.com/zou-group/textgrad)<br>• [![star: 3,720](https://img.shields.io/badge/star-3720-f4b400?style=flat-square)](https://github.com/zou-group/textgrad)<br>• **最近推送:** 2025-07-25 | • **有界优化**<br>• **闭环:** 在计算图中传播自然语言反馈以更新提示及其他文本变量；同一框架也可优化代码和科研产物。<br>• **边界:** 文本梯度是启发式 LLM 评价而非解析导数；固定目标与优化器逻辑限定了其自改进范围。 |
| [Agent-Pro: Learning to Evolve via Policy-Level Reflection and Optimization](https://arxiv.org/abs/2402.17574) | 2024-02-27<br>[ACL 2024 Main](https://github.com/zwq2018/Agent-Pro/blob/main/README.md) | • [官方代码](https://github.com/ZJU-OmniAI/Agent-Pro)<br>• [![star: 131](https://img.shields.io/badge/star-131-f4b400?style=flat-square)](https://github.com/ZJU-OmniAI/Agent-Pro)<br>• **最近推送:** 2024-09-02 | • **有界优化**<br>• **闭环:** 根据交互轨迹修订策略层面的信念，并用深度优先搜索在 Blackjack 与 Texas Hold'em 中选择更好的行为策略。<br>• **边界:** 论文中信念的 fine-tuning 指策略反思，不应据此宣称神经网络权重训练；游戏收益与搜索过程仍固定。 |
| [Self-Taught Optimizer (STOP): Recursively Self-Improving Code Generation](https://arxiv.org/abs/2310.02304) | 2023-10-03 | • [官方代码](https://github.com/microsoft/stop)<br>• [![star: 53](https://img.shields.io/badge/star-53-f4b400?style=flat-square)](https://github.com/microsoft/stop)<br>• **最近推送:** 2024-01-01 | • **直接自修改**<br>• **闭环:** 将调用语言模型的种子程序优化器应用于自身代码，发现更好的搜索脚手架，再用于优化下游程序。<br>• **边界:** 论文明确指出语言模型不变，因此不属于完整递归自改进；研究限于少量任务，并讨论绕过沙箱的风险。 |
| [Large Language Models as Optimizers](https://arxiv.org/abs/2309.03409) | 2023-09-07 | • [官方代码](https://github.com/google-deepmind/opro)<br>• [![star: 774](https://img.shields.io/badge/star-774-f4b400?style=flat-square)](https://github.com/google-deepmind/opro)<br>• **最近推送:** 2024-12-04<br>• **发布说明:** 属于官方研究代码，而非 Google 支持的产品；README 未提供本次可核实的会议归属。 | • **有界优化**<br>• **闭环:** 把先前候选解及其目标值放入提示，评测 LLM 提出的新候选，再把带分数的历史反馈到后续优化，主要应用于指令优化。<br>• **边界:** 优化器模型与评分任务保持固定；迭代提示搜索本身不改进 LLM 权重或改写优化器。 |

### Papers / Artifacts

| 论文 | 日期 / 发表状态 | 代码 | 贡献与边界 |
| --- | --- | --- | --- |
| [Digital Red Queen: Adversarial Program Evolution in Core War with LLMs](https://arxiv.org/abs/2601.03335) | 2026-01-06 | • [官方代码](https://github.com/SakanaAI/drq)<br>• [![star: 220](https://img.shields.io/badge/star-220-f4b400?style=flat-square)](https://github.com/SakanaAI/drq)<br>• **最近推送:** 2026-01-13 | • **有界优化**<br>• **闭环:** 针对所有先前对手进化可执行 Core War 战士，将保留种群变成自适应自博弈目标，而非仅针对固定基准优化。<br>• **边界:** LLM 与进化算法保持固定；报告的泛化局限于 Core War，不代表实际网络安全能力或无约束 RSI。 |
| [Agentic Context Engineering: Evolving Contexts for Self-Improving Language Models](https://arxiv.org/abs/2510.04618) | 2025-10-06 | • [官方代码](https://github.com/ace-agent/ace)<br>• [![star: 1,302](https://img.shields.io/badge/star-1302-f4b400?style=flat-square)](https://github.com/ace-agent/ace)<br>• **最近推送:** 2026-08-24<br>• **发布说明:** 作者关联仓库记录生成者、反思者与整理者角色、增量更新、保存的 playbook 和评测模式；不涉及权重训练的暗示。 | • **经验学习**<br>• **闭环:** 将上下文视为持久进化的 playbook，把执行反馈反思为结构化增量更新，以在后续任务中保留、修订和组织策略。<br>• **边界:** 上下文适配不等于模型权重学习；收益依赖任务反馈和固定的生成、反思、整理架构，离线与在线评测应区分。 |
| [ShinkaEvolve: Towards Open-Ended And Sample-Efficient Program Evolution](https://arxiv.org/abs/2509.19349) | 2025-09-17<br>[ICLR 2026](https://github.com/SakanaAI/ShinkaEvolve/blob/main/README.md) | • [官方代码](https://github.com/SakanaAI/ShinkaEvolve)<br>• [![star: 1,375](https://img.shields.io/badge/star-1375-f4b400?style=flat-square)](https://github.com/SakanaAI/ShinkaEvolve)<br>• **最近推送:** 2026-08-21 | • **有界优化**<br>• **闭环:** 通过档案采样、新颖性筛选与自适应 LLM 选择提高程序进化效率，应用于数学解、代理 Harness 与 MoE 训练损失。<br>• **边界:** 程序优化器与任务适应度由外部设计；开放式表述不能证明学习器会改写自身或基础权重无限改进。 |
| [AlphaEvolve: A coding agent for scientific and algorithmic discovery](https://arxiv.org/abs/2506.13131) | 2025-06-16 | 已审查来源未找到 | • **有界优化**<br>• **闭环:** 在进化流水线中组织 LLM 提出的代码修改与可执行评测，改进科学算法和计算基础设施，包括底层 LLM 的训练内核。<br>• **边界:** 改进训练代码不等于已经展示反复重训提案模型或改写进化算法自身的完整闭环。 |
| [Discovering Preference Optimization Algorithms with and for Large Language Models](https://arxiv.org/abs/2406.08414) | 2024-06-12 | • [官方代码](https://github.com/SakanaAI/DiscoPOP)<br>• [![star: 196](https://img.shields.io/badge/star-196-f4b400?style=flat-square)](https://github.com/SakanaAI/DiscoPOP)<br>• **最近推送:** 2024-06-13 | • **有界优化**<br>• **闭环:** 利用 LLM 提出可执行偏好优化损失，以这些损失训练并评测模型，再将性能反馈给后续提案，发现 DiscoPOP。<br>• **边界:** 改变的产物是训练损失代码；并未展示提案 LLM 使用所发现损失反复重训自身的完整递归闭环。 |
| [Mathematical discoveries from program search with large language models](https://www.nature.com/articles/s41586-023-06924-6) | 2023-12-14<br>[Nature](https://www.nature.com/articles/s41586-023-06924-6) | • [官方代码](https://github.com/google-deepmind/funsearch)<br>• [![star: 1,116](https://img.shields.io/badge/star-1116-f4b400?style=flat-square)](https://github.com/google-deepmind/funsearch)<br>• **最近推送:** 2024-02-05 | • **有界优化**<br>• **闭环:** 用高分程序提示预训练 LLM，通过系统评测器执行评估，再将接受的程序写回数据库，从而进化函数。<br>• **边界:** 需要用户定义的评测器和种子或程序骨架；出版正文明确无需训练或微调 LLM。公开代码为单线程流水线，不是 Google 全部内部系统。 |
| [Voyager: An Open-Ended Embodied Agent with Large Language Models](https://arxiv.org/abs/2305.16291) | 2023-05-25 | • [官方代码](https://github.com/MineDojo/Voyager)<br>• [![star: 7,184](https://img.shields.io/badge/star-7184-f4b400?style=flat-square)](https://github.com/MineDojo/Voyager)<br>• **最近推送:** 2024-04-03 | • **经验学习**<br>• **闭环:** 在自动课程下构建可执行 Minecraft 技能，依据环境反馈修复程序，并在后续任务与世界中复用扩展中的技能库。<br>• **边界:** GPT-4 基础模型通过黑盒推理使用而非更新权重；开放探索是在 Minecraft 内展示，并非无约束领域。 |
| [Self-Refine: Iterative Refinement with Self-Feedback](https://arxiv.org/abs/2303.17651) | 2023-03-30 | • [官方代码](https://github.com/madaan/self-refine)<br>• [![star: 820](https://img.shields.io/badge/star-820-f4b400?style=flat-square)](https://github.com/madaan/self-refine)<br>• **最近推送:** 2024-10-04 | • **任务内修订**<br>• **闭环:** 用同一 LLM 充当生成者、评论者和修订者，在推理时把文本反馈用于任务输出的多轮修订。<br>• **边界:** 这是有界的任务内基线，不是持久策略或权重改进；自反馈可能错误，框架本身不会自动积累跨任务技能。 |
| [Reflexion: Language Agents with Verbal Reinforcement Learning](https://arxiv.org/abs/2303.11366) | 2023-03-20<br>[NeurIPS 2023](https://github.com/noahshinn/reflexion/blob/main/README.md) | • [官方代码](https://github.com/noahshinn/reflexion)<br>• [![star: 3,262](https://img.shields.io/badge/star-3262-f4b400?style=flat-square)](https://github.com/noahshinn/reflexion)<br>• **最近推送:** 2025-01-14 | • **经验学习**<br>• **闭环:** 将试验反馈转成语言反思并保存到情景记忆，在不更新模型权重的情况下利用这些笔记改变后续尝试的决策。<br>• **边界:** 语言强化学习并非基于梯度的 RL；任务试验记忆与基准成功不代表无约束、永久的跨领域学习。 |

## Active GitHub Projects

仓库元数据快照：**2026-09-08**。本节只列公开、未归档、最近 **60 天**有 push 的项目；star 是快照，不是 RSI 证据。上方论文配套代码不受活跃窗口限制。

### Models

#### Models / Training Research

代理调整训练配方并评测训练结果，不意味着科研代理本身也被重新训练。

| 项目 | 链接 | Stars | 标签 | 改进闭环与边界 |
| --- | --- | ---: | --- | --- |
| RD-Agent / FT-Agent | [GitHub](https://github.com/microsoft/RD-Agent) | [![star: 14,551](https://img.shields.io/badge/star-14551-f4b400?style=flat-square)](https://github.com/microsoft/RD-Agent) | `model-training`<br>`experiment-loop`<br>`validation` | • **有界优化**<br>• **闭环:** FT-Agent 生成数据处理代码和训练配置、微调目标 LLM，再利用 OpenCompass 验证反馈调整下一轮训练实验。<br>• **边界:** 改进的是外部目标模型，不是规划代理自身权重；测试集保留用于最终报告。<br>• [证据](https://github.com/microsoft/RD-Agent/blob/main/rdagent/app/finetune/llm/README.md) |

### Harness

#### Harness / Self-Modification

代理实现及其改进过程本身是可修改对象。

| 项目 | 链接 | Stars | 标签 | 改进闭环与边界 |
| --- | --- | ---: | --- | --- |
| Prime Agent / Continual Harness | [GitHub](https://github.com/PrimeIntellect-ai/prime-agent) | [![star: 20,300](https://img.shields.io/badge/star-20300-f4b400?style=flat-square)](https://github.com/PrimeIntellect-ai/prime-agent) | `self-refinement`<br>`continual-harness`<br>`rollback` | • **直接自修改**<br>• **闭环:** 通过 /refine 审查轨迹，保留有证据支持的补充提示、记忆、技能描述与子代理规格更新，并利用快照回滚。<br>• **边界:** 基础系统提示不可变；修订不能替代可执行技能的打包审查，其进程隔离也不是安全沙箱。<br>• [证据](https://github.com/PrimeIntellect-ai/prime-agent) |
| HyperAgents | [GitHub](https://github.com/facebookresearch/HyperAgents) | [![star: 2,718](https://img.shields.io/badge/star-2718-f4b400?style=flat-square)](https://github.com/facebookresearch/HyperAgents) | `self-modification`<br>`meta-agent`<br>`archive` | • **直接自修改**<br>• **闭环:** 将任务代理与元代理整合为可编辑程序；经过评测的后代既能修改任务行为，也能修改生成后续代理的过程。<br>• **边界:** 属于限定任务的实证实验，不是无限改进证明，也不是基础模型权重自训练。<br>• [证据](https://github.com/facebookresearch/HyperAgents/blob/main/utils/gl_utils.py) |

#### Harness / Prompt and Workflow Optimization

反馈用于更新并保留提示或工作流图。这类有界优化器不代表无约束的自修改。

| 项目 | 链接 | Stars | 标签 | 改进闭环与边界 |
| --- | --- | ---: | --- | --- |
| DSPy / GEPA and MIPROv2 | [GitHub](https://github.com/stanfordnlp/dspy) | [![star: 37,855](https://img.shields.io/badge/star-37855-f4b400?style=flat-square)](https://github.com/stanfordnlp/dspy) | `prompt-optimization`<br>`demonstrations`<br>`metrics` | • **有界优化**<br>• **闭环:** 针对任务指标优化指令和示例来编译 LM 程序，编译结果保留所选配置供后续使用。<br>• **边界:** 仅因其优化器收录，而非 DSPy 的所有功能；提示编译本身不修改优化器或模型权重。<br>• [证据](https://github.com/stanfordnlp/dspy/blob/main/dspy/teleprompt/gepa/gepa.py) |
| GEPA | [GitHub](https://github.com/gepa-ai/gepa) | [![star: 6,475](https://img.shields.io/badge/star-6475-f4b400?style=flat-square)](https://github.com/gepa-ai/gepa) | `reflection`<br>`pareto-selection`<br>`prompt-optimization` | • **有界优化**<br>• **闭环:** 反思执行轨迹和评测反馈来提出提示修订，并通过 Pareto 选择保留互补候选。<br>• **边界:** 原始方法在固定模型权重下优化提示；通用 optimize_anything API 不代表 GEPA 会改写自身。<br>• [证据](https://github.com/gepa-ai/gepa) |
| EvoAgentX / Evolution Algorithms | [GitHub](https://github.com/ANative-Lab/EvoAgentX) | [![star: 3,313](https://img.shields.io/badge/star-3313-f4b400?style=flat-square)](https://github.com/ANative-Lab/EvoAgentX) | `workflow-optimization`<br>`aflow`<br>`validation` | • **有界优化**<br>• **闭环:** 对代理工作流运行 AFlow、TextGrad、MIPRO 和 EvoPrompt；验证分数驱动提示或图结构修订，并进行独立测试评测。<br>• **边界:** 因可执行进化算法收录，而非工具集成或单次工作流生成；目标与搜索算法由人设定。<br>• [证据](https://github.com/ANative-Lab/EvoAgentX#evolution-algorithms) |

### Artifacts

#### Artifacts / Program Evolution

针对评测器进化可执行程序与算法，优化器本身通常保持固定。

| 项目 | 链接 | Stars | 标签 | 改进闭环与边界 |
| --- | --- | ---: | --- | --- |
| OpenEvolve | [GitHub](https://github.com/algorithmicsuperintelligence/openevolve) | [![star: 7,336](https://img.shields.io/badge/star-7336-f4b400?style=flat-square)](https://github.com/algorithmicsuperintelligence/openevolve) | `program-evolution`<br>`evaluator`<br>`archive` | • **有界优化**<br>• **闭环:** 利用 LLM 变异、任务专用评测器和候选档案进化可执行程序，档案中的程序继续成为后续代的起点。<br>• **边界:** 改进对象是程序，并未证明优化器会改写自身或递归训练提案模型权重。<br>• [证据](https://github.com/algorithmicsuperintelligence/openevolve) |
| ShinkaEvolve | [GitHub](https://github.com/SakanaAI/ShinkaEvolve) | [![star: 1,375](https://img.shields.io/badge/star-1375-f4b400?style=flat-square)](https://github.com/SakanaAI/ShinkaEvolve) | `program-evolution`<br>`novelty`<br>`ai-training` | • **有界优化**<br>• **闭环:** 结合父代采样、新颖性筛选和 bandit 式 LLM 选择进化程序；评测后的后代重新进入档案，实验也包含 AI 训练损失设计。<br>• **边界:** 评测器与进化机制由研究者提供；自行生成问题是未来扩展，而非已证明的功能。<br>• [证据](https://sakana.ai/shinka-evolve/) |

#### Artifacts / Learned Skills

从经验创建并修订技能，供后续任务复用，而非仅打包静态技能库。

| 项目 | 链接 | Stars | 标签 | 改进闭环与边界 |
| --- | --- | ---: | --- | --- |
| Hermes Agent / Learned Skills | [GitHub](https://github.com/NousResearch/hermes-agent) | [![star: 243,353](https://img.shields.io/badge/star-243353-f4b400?style=flat-square)](https://github.com/NousResearch/hermes-agent) | `learned-skills`<br>`procedural-memory`<br>`experience` | • **经验学习**<br>• **闭环:** 在复杂任务后创建过程性技能，并在使用中修订；持久技能与可搜索经验用于后续会话。<br>• **边界:** 这是经验驱动的技能持久化，不是模型权重训练，也不是独立证明的单调能力增长。<br>• [证据](https://github.com/NousResearch/hermes-agent) |

## Scope and Curation

RSI 指改进后的系统参与产生后续改进。优先收录能修改自身改进机制的实现；相关的自训练与持久化产物优化单独标注。普通工具调用循环、测试工具、RAG 框架或人工维护的技能合集不构成收录依据。每条必须明确改进对象、反馈、保留状态与限制。

任何条目都不代表已实现无界自主 RSI。任务内修订、安全评测和研究路线是相关背景，不是持久自改进的实证。数量统计的是资源：一篇博客、论文和仓库可能对应同一研究，并非三项独立突破。

## Maintenance

所有正式条目在 `data/projects.yaml` 维护，两份 README 均由脚本生成。来源解读与翻译需要审查；元数据和链接不能证明科研结论。

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
