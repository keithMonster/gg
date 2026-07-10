# Prompt 工程层 + LLM 理论层论文考证（侦察原件 · 2026-07-10，WebSearch 逐条验证）

## 提示词工程层

1. Few-shot ICL 开山 | Language Models are Few-Shot Learners (GPT-3) | Brown et al. 2020 | https://arxiv.org/abs/2005.14165 | 无梯度更新，prompt 内示例学新任务
2. Zero-shot CoT | Large Language Models are Zero-Shot Reasoners | Kojima et al. 2022 | https://arxiv.org/abs/2205.11916 | "Let's think step by step"，MultiArith 17.7%→78.7%
3. 指令微调 | Finetuned Language Models Are Zero-Shot Learners (FLAN) | Wei et al. 2021 | https://arxiv.org/abs/2109.01652 | 指令化多任务微调提升零样本泛化
4a. 顺序效应 | Fantastically Ordered Prompts and Where to Find Them | Lu et al. 2022 | https://arxiv.org/abs/2104.08786 | 示例排列使准确率随机↔SOTA 波动，不可跨模型迁移
4b. 校准 | Calibrate Before Use | Zhao et al. 2021 | https://arxiv.org/abs/2102.09690 | 内容无关探针校准先验偏置，最高 +30%
5. System prompt | Giving Claude a role with a system prompt | Anthropic 官方文档 | https://docs.claude.com/en/docs/build-with-claude/prompt-engineering/system-prompts | 角色设定聚焦语气与行为边界
6. Prompt injection | Not what you've signed up for… Indirect Prompt Injection | Greshake et al. 2023 | https://arxiv.org/abs/2302.12173 | 间接注入攻击面开山
7. 约束解码 | Efficient Guided Generation for Large Language Models | Willard & Louf 2023 | https://arxiv.org/abs/2307.09702 | FSM 约束解码近零开销（outlines 理论基础）

## LLM 理论基础层

8. Transformer | Attention Is All You Need | Vaswani et al. 2017 | https://arxiv.org/abs/1706.03762
9. next-token 范式 | GPT-3（同 1；GPT-2 无 arXiv 版本，有意复用）
10. RLHF | Training language models to follow instructions with human feedback (InstructGPT) | Ouyang et al. 2022 | https://arxiv.org/abs/2203.02155 | 对齐后 1.3B 胜原始 175B
11a. Scaling laws | Kaplan et al. 2020 | https://arxiv.org/abs/2001.08361 | 跨七个数量级幂律
11b. Chinchilla | Hoffmann et al. 2022 | https://arxiv.org/abs/2203.15556 | 模型与数据等比放大
12a. 涌现 | Emergent Abilities of Large Language Models | Wei et al. 2022 | https://arxiv.org/abs/2206.07682
12b. 质疑 | Are Emergent Abilities of Large Language Models a Mirage? | Schaeffer et al. 2023 | https://arxiv.org/abs/2304.15004 | 非线性指标造成的测量假象
13. ICL 机制 | In-context Learning and Induction Heads | Olsson et al. 2022（Anthropic）| https://transformer-circuits.pub/2022/in-context-learning-and-induction-heads/index.html | 归纳头电路
14. RAG | Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks | Lewis et al. 2020 | https://arxiv.org/abs/2005.11401
15a. FlashAttention | Dao et al. 2022 | https://arxiv.org/abs/2205.14135 | 显存平方→线性
15b. FlashAttention-2 | Dao 2023 | https://arxiv.org/abs/2307.08691（未入图，候选）
16a. 叠加态 | Toy Models of Superposition | Elhage et al. 2022 | https://transformer-circuits.pub/2022/toy_model/index.html
16b. 单义特征 | Towards Monosemanticity | Bricken et al. 2023 | https://transformer-circuits.pub/2023/monosemantic-features
16c. 电路追踪 | Circuit Tracing | Ameisen et al. 2025 | https://transformer-circuits.pub/2025/attribution-graphs/methods.html

## 2025-2026 新进展

- s1: Simple test-time scaling | Muennighoff et al. 2025 | https://arxiv.org/abs/2501.19393 | 1000 条轨迹 + budget forcing 复现 o1 级
- DeepSeek-R1 | Guo et al. 2025 | https://arxiv.org/abs/2501.12948 | 纯 RL 激励推理行为（Nature 发表）
- The Art of Scaling Reinforcement Learning Compute for LLMs | Khatri et al. 2025 | https://arxiv.org/abs/2510.13786 | 40万+ GPU 时的 RL scaling 框架
