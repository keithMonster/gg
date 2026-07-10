# Agent 理论层论文考证（侦察原件 · 2026-07-10，WebSearch 逐条验证）

1. ReAct | ReAct: Synergizing Reasoning and Acting in Language Models | Yao et al. 2022（ICLR 2023）| https://arxiv.org/abs/2210.03629 | 思考文本与动作调用交替生成，推理指导行动、行动反哺推理 | agent loop 最小骨架
2. Reflexion | Reflexion: Language Agents with Verbal Reinforcement Learning | Shinn et al. 2023（NeurIPS 2023）| https://arxiv.org/abs/2303.11366 | 语言化反思存入 episodic memory，免训练试错学习 | 自我纠错/经验回灌
3. CoT | Chain-of-Thought Prompting Elicits Reasoning in Large Language Models | Wei et al. 2022 | https://arxiv.org/abs/2201.11903 | 中间推理步骤示例大幅提升复杂推理 | 一切"先想后做"的底座
4. ToT | Tree of Thoughts: Deliberate Problem Solving with Large Language Models | Yao et al. 2023（NeurIPS 2023）| https://arxiv.org/abs/2305.10601 | 单链推理泛化成树搜索：自评估/前瞻/回溯 | deliberate search 范式
5. Generative Agents | Generative Agents: Interactive Simulacra of Human Behavior | Park et al. 2023（UIST '23）| https://arxiv.org/abs/2304.03442 | 记忆流+反思+规划三件套产生可信社会行为 | 长时程记忆架构奠基
6. MemGPT | MemGPT: Towards LLMs as Operating Systems | Packer et al. 2023 | https://arxiv.org/abs/2310.08560 | OS 虚拟内存分页思想管理上下文换入换出 | 分层/虚拟上下文管理
7. Voyager | Voyager: An Open-Ended Embodied Agent with Large Language Models | Wang et al. 2023 | https://arxiv.org/abs/2305.16291 | 自动课程+可执行技能库+迭代自我验证的终身学习 | 技能库持续学习
8. Toolformer | Toolformer: Language Models Can Teach Themselves to Use Tools | Schick et al. 2023 | https://arxiv.org/abs/2302.04761 | 自监督学习何时调用/传什么参 | function calling 源头
9. Constitutional AI | Constitutional AI: Harmlessness from AI Feedback | Bai et al. 2022（Anthropic）| https://arxiv.org/abs/2212.08073 | 宪法原则 + AI 自我评判替代人工安全标注（RLAIF）| 对齐/护栏理论基础
10. LLM-as-a-Judge | Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena | Zheng et al. 2023（NeurIPS 2023）| https://arxiv.org/abs/2306.05685 | 裁判可行但有位置/冗长/自我偏好三类偏差 | 自动化评审方法论
11. Self-Refine | Self-Refine: Iterative Refinement with Self-Feedback | Madaan et al. 2023（NeurIPS 2023）| https://arxiv.org/abs/2303.17651 | 生成/反馈/改写三角色一体迭代改进 | agent 内循环质检最简形态
12a. AutoGen | AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation | Wu et al. 2023（微软）| https://arxiv.org/abs/2308.08155 | 对话驱动的多 agent 编排框架
12b. MetaGPT | MetaGPT: Meta Programming for A Multi-Agent Collaborative Framework | Hong et al. 2023 | https://arxiv.org/abs/2308.00352 | SOP 编码进角色流水线，抑制级联幻觉
13a. Context Engineering 综述 | A Survey of Context Engineering for Large Language Models | Mei et al. 2025 | https://arxiv.org/abs/2507.13334 | 1400+ 篇：信息负载系统化优化，检索/处理/管理三层
13b. 记忆演化综述 | From Storage to Experience: A Survey on the Evolution of LLM Agent Memory Mechanisms | Luo et al. 2026 | https://arxiv.org/abs/2605.06716 | 存储→经验的记忆演化分类法
14a. Building Effective Agents | Anthropic 工程团队 2024-12 | https://www.anthropic.com/engineering/building-effective-agents | workflow vs agent 架构选型框架
14b. Effective Context Engineering for AI Agents | Anthropic 2025 | https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents | 上下文治理心智模型

## 2025-2026 新里程碑

A. MCP | Model Context Protocol | Anthropic 2024-11 | https://www.anthropic.com/news/model-context-protocol | N×M 集成 → N+M，事实标准
B. 多 agent 研究系统 | How we built our multi-agent research system | Anthropic 2025-06 | https://www.anthropic.com/engineering/multi-agent-research-system | orchestrator-worker 提升 90.2% + 适用边界判据
C. AlphaEvolve | AlphaEvolve: A coding agent for scientific and algorithmic discovery | Novikov et al. 2025（Google DeepMind）| https://arxiv.org/abs/2506.13131 | LLM+进化算法在真实基础设施取得 SOTA（未入图，候选）
D. Hindsight | Hindsight is 20/20: Building Agent Memory that Retains, Recalls, and Reflects | Latimer et al. 2025-12 | https://arxiv.org/abs/2512.12818 | 四网络分离事实/经验/摘要/信念
