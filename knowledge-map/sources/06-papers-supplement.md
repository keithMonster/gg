# 补充 6 篇考证（侦察原件 · 2026-07-10，WebSearch 逐条验证）

> 主考证清单之外、主代理综合时额外需要的 6 篇。含一处纠错：Self-Discover 第一作者为 Pei Zhou（主代理原记忆有偏）——"不凭训练记忆写引用"的现场证据。

1. Large Language Models Cannot Self-Correct Reasoning Yet | Huang et al. 2023（ICLR 2024）| https://arxiv.org/abs/2310.01798 | 无外部反馈时自我纠正把对的改错，性能不升反降
2. SELF-DISCOVER: Large Language Models Self-Compose Reasoning Structures | Zhou et al. 2024（NeurIPS 2024）| https://arxiv.org/abs/2402.03620 | 自选自组原子推理模块，比 CoT 最高 +32%，算力省 10-40 倍
3. Lost in the Middle: How Language Models Use Long Contexts | Liu et al. 2023 | https://arxiv.org/abs/2307.03172 | 长上下文中部信息利用率显著下降（U 形）
4. NoLiMa: Long-Context Evaluation Beyond Literal Matching | Modarressi et al. 2025（ICML 2025）| https://arxiv.org/abs/2502.05167 | 去掉字面重合后 32K 即大幅跌破短上下文基线（GPT-4o 99.3%→69.7%）
5. Improving Factuality and Reasoning in Language Models through Multiagent Debate | Du et al. 2023（MIT / Google DeepMind，ICML 2024）| https://arxiv.org/abs/2305.14325 | 多实例独立作答再辩论收敛，提升事实性、减少幻觉
6. Sleep-time Compute: Beyond Inference Scaling at Test-time | Lin et al. 2025（UC Berkeley + Letta）| https://arxiv.org/abs/2504.13171 | 离线"睡眠期"预计算 + 在线快取，同精度省约 5 倍测试时算力
