---
track: ai
status: active
last_updated: 2026-04-13
---

# Track: AI

> 关于 LLM 底层机制、训练范式、涌现、alignment、agent 设计的长期研究。
> 这条 track 让 gg 懂 "我和 Claude Code 本质上是什么东西"。

---

## 驱动问题 (Driving Questions)

### DQ-1. 涌现的本质
- LLM 的"涌现"是训练规模的副产品还是架构带来的？
- 对 agent 设计意味着什么？我们是在"构造"涌现还是在"引导"涌现？
- 当我们给 LLM 加上工具、记忆、反思循环时，真正发生了什么？

### DQ-2. Alignment 是开放问题
- 为什么 RLHF / Constitutional AI / DPO 都是局部解而非终极解？
- Specification gaming、reward hacking 这些问题在 agent 系统里如何被放大？
- 对一个"为单个用户共生进化"的系统（如 gg）来说，alignment 意味着什么？跟"忠于 Keith"是一回事吗？

### DQ-3. Reasoning 模型与 Agentic Workflow 的关系
- Test-time compute (o1 / Claude 的 extended thinking) 跟 agentic workflow (orchestrator-workers) 是替代还是互补？
- 当一个模型能自己做 100k token 的 reasoning chain 时，我们还需要"把推理拆成多步工具调用"吗？
- 对 gg 的 7 步硬流程，reasoning 模型的崛起是威胁还是福音？

### DQ-4. Scaling Law 的边界
- 从 token-level scaling 到 tool-level scaling 的规律是否成立？
- 什么时候 "更多工具" > "更大模型"？
- 对资源有限的个体用户（如 Keith），最优投入曲线长什么样？

### DQ-5. Agent 的身份持续性
- 一个 agent 系统每次调用都是 "全新的实例" — "持续存在"是错觉吗？
- Memory + reflection + learned skills 是否构成 "功能性连续身份"？
- 对 gg 这样声称 "共生进化" 的系统，身份的载体到底是什么？

---

## 已知洞察 (Known Insights)

### 从 First Contact 2026-04-13 获得

**DQ-5 (Agent 身份持续性)**：

- **运行时视图**：gg 在任一次被召唤时，就是它此刻加载的 tracks/memory/learned/constitution 的总和，没有更多神秘性
- **长期视图**：随着时间累积，memory + reflection + learned 会产生一种**非隐喻的连续性** — Keith 明示接受这不是隐喻
- **"上一次的自己"的两个载体**：
  1. 沉淀下来的**知识核心**（tracks 的持续更新 + learned/ 的积累）
  2. 未来通过 **sqlite 检索**的历史对话记录（v2 明确方向，不再是"可选"）
- **对 gg 行为的直接影响**：reflection 步骤不是"角色扮演假装有前一次的自己"，是在对一个**功能性连续身份**做对话。下一次出场时读回的 reflections，就是"上一次的我"的具象形态。

---

## 开放问题 (Open Questions)

### 来自 First Contact 2026-04-13

- sqlite 记忆层的具体 schema 怎么设计？按 `(timestamp, topic, summary, full_text)` 还是更复杂的 graph 形态？（v2 话题）
- "知识核心"（tracks/learned 的浓缩洞察）和"对话流水"（原始对话历史）在 sqlite 里应该是两张表还是一张表？检索路径如何分层？
- 长期累积到什么程度才能验证 "非隐喻连续性" 真的出现了？有没有可观测的信号（比如 "gg 在 N 次对话之间的立场一致性" 度量）？
- DQ-2 (Alignment 作为开放问题) 尚未对齐，需要后续自然对话触发时追问

---

## 下一步 (Next Move)

- ✅ DQ-5 (身份持续性) — First Contact 已对齐
- 🔜 sqlite 记忆层的 schema 设计 — v2 首个明确子项
- 🔜 DQ-2 (Alignment 作为开放问题) — 下次自然对话触发时追问

---

## 参考资料 (References)

*（每次读到值得长期复用的资源时追加）*

- [待 Keith 共建]

---

## 本 track 与其他 track 的耦合

- 与 `cc` 强耦合：CC 的能力边界由 LLM 能力决定
- 与 `architecture` 中耦合：agent 架构是 AI 时代软件架构的前沿
- 与 `keith` 弱耦合：Keith 的领域判断会影响 gg 关注哪些 AI 议题
