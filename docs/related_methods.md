# Related Methods and Paper Selection / 相关方法与论文筛选

Reviewed: **2026-09-09**. These are useful neighboring methods, not rejected research. They are outside this catalog’s narrowed main-paper gate; links remain here for comparison.

这些研究有参考价值，以下调整不是对论文质量的否定。它们不满足本轮收紧后的主论文列表条件，保留链接供比较。

| Paper / 论文 | Why it is related rather than core / 调整原因 |
| --- | --- |
| [GEPA: Reflective Prompt Evolution Can Outperform Reinforcement Learning](https://arxiv.org/abs/2507.19457) | Fixed prompt optimizer; evolving prompts does not demonstrate evolution of the optimizer itself.<br>固定提示优化器；提示进化不等于优化器自身进化。 |
| [TextGrad: Automatic "Differentiation" via Text](https://arxiv.org/abs/2406.07496) | Optimizes text variables and external artifacts with a fixed textual-gradient procedure.<br>以固定文本梯度过程优化文本变量或外部产物。 |
| [AFlow: Automating Agentic Workflow Generation](https://arxiv.org/abs/2410.10762) | Fixed Monte Carlo tree search over task workflows; the search procedure is not self-modified.<br>对任务工作流执行固定蒙特卡洛树搜索，搜索过程自身未被修改。 |
| [Automated Design of Agentic Systems](https://arxiv.org/abs/2408.08435) | An external meta-agent searches task-agent designs; its own improvement machinery stays fixed.<br>外部元代理搜索任务代理设计，其自身改进机制保持固定。 |
| [Agent-Pro: Learning to Evolve via Policy-Level Reflection and Optimization](https://arxiv.org/abs/2402.17574) | Game-policy belief refinement under fixed reflection/search machinery.<br>在固定反思与搜索机制下修订博弈策略信念。 |
| [Reflexion: Language Agents with Verbal Reinforcement Learning](https://arxiv.org/abs/2303.11366) | Episodic verbal memory improves later trials, without modifying the reflection procedure or training weights.<br>言语记忆改善后续尝试，但未改写反思过程或训练模型权重。 |
| [Self-Refine: Iterative Refinement with Self-Feedback](https://arxiv.org/abs/2303.17651) | Within-task output refinement without persistent system learning.<br>只修订当前任务输出，没有持久的系统学习。 |
| [Voyager: An Open-Ended Embodied Agent with Large Language Models](https://arxiv.org/abs/2305.16291) | A reusable Minecraft skill library; the curriculum and improvement procedure remain externally designed.<br>可复用的 Minecraft 技能库；课程与改进过程仍由外部设计。 |
| [Mathematical discoveries from program search with large language models](https://www.nature.com/articles/s41586-023-06924-6) | Search evolves external functions while the LLM and evolutionary machinery remain fixed.<br>搜索进化外部函数，LLM 与进化机制保持固定。 |
| [AlphaEvolve: A coding agent for scientific and algorithmic discovery](https://arxiv.org/abs/2506.13131) | Important AI-research infrastructure, but no measured repeated retraining of the proposer closes the advertised loop.<br>重要的 AI 科研基础设施，但没有通过实测的反复提案模型再训练闭合该回路。 |
| [ShinkaEvolve: Towards Open-Ended And Sample-Efficient Program Evolution](https://arxiv.org/abs/2509.19349) | An efficient external program optimizer; adaptive sampling alone is not recursive modification of its learner.<br>高效的外部程序优化器；自适应采样本身不等于递归修改学习器。 |
| [Discovering Preference Optimization Algorithms with and for Large Language Models](https://arxiv.org/abs/2406.08414) | Discovers training losses for other models; the proposer is not recursively retrained with those losses.<br>为其他模型发现训练损失，提案模型未用这些损失递归再训练。 |
| [Agent Skill Acquisition for Large Language Models via CycleQD](https://arxiv.org/abs/2410.14735) | Model merging and mutation under a fixed quality-diversity algorithm.<br>在固定质量多样性算法下执行模型合并与突变。 |
| [Digital Red Queen: Adversarial Program Evolution in Core War with LLMs](https://arxiv.org/abs/2601.03335) | Adversarial evolution of Core War programs, not of the LLM or its improvement machinery.<br>进化的是 Core War 对抗程序，而非 LLM 或其改进机制。 |
| [Agentic Context Engineering: Evolving Contexts for Self-Improving Language Models](https://arxiv.org/abs/2510.04618) | Persistent playbooks with a fixed generator/reflector/curator, useful context-adaptation background.<br>由固定生成器、反思器和整理器维护持久剧本，属于上下文适应背景。 |
| [Large Language Models as Optimizers](https://arxiv.org/abs/2309.03409) | An LLM optimizes prompts or external solutions through a fixed scored-history loop.<br>LLM 通过固定的评分历史循环优化提示或外部解。 |
| [EvoAgentX: An Automated Framework for Evolving Agentic Workflows](https://arxiv.org/abs/2507.03616) | Integrates fixed optimizers in a workflow platform; integration is not independent evidence of RSI.<br>在工作流平台集成固定优化器，集成本身不是独立 RSI 证据。 |
| [Prime Agent: A Self-Improving RLM Harness](https://arxiv.org/abs/2608.23552) | Harness engineering and retained refinement overlap Continual Harness; the paper does not isolate recursive improvement as the cause of its benchmark gains.<br>与 Continual Harness 重叠的框架工程和持久修订；论文未将递归改进单独确认为基准收益来源。 |

The main catalog retains bounded iterative self-training as a clearly named strand, rather than calling every retained paper a demonstration of self-rewriting learning rules. Continual Harness remains for its explicit self-adaptation and separate teacher-assisted weight co-learning experiment.

主目录将有界迭代自训练单独命名，不把每篇收录论文都称为学习规则自改写的实证。Continual Harness 因其明确的自身适应回路与独立的教师辅助权重共同学习实验而保留。

See the [audit](../reports/research/2026-09-09-paper-audit.yaml) and [curation policy](curation_policy.md).
