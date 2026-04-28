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

### 从 phodal-spec-harness-ingest 设计会话（2026-04-13）

**外部框架嫁接模式**：(auto_gg 补写 2026-04-13)

外部框架能否嫁接到 gg，不看框架的原始语境，看框架的"纪律点"能否附着到 gg 现有的某个动作上。具体方法：把外部协议拆成"哲学（值得吸收的精神）"和"格式（具体语法）"两层独立判断。与 `tracks/cc.md` 的候选 reasoning_module `PROTOCOL_HARVESTING` 互为交叉引用。

### 从 2026-04-15 KERNEL 坍缩设计会话获得（auto_gg 补写 2026-04-15）

**gg 的 telos 重定位：从"决策辅助"到"无限游戏玩家"**（对 DQ-5 的补强）

Keith 在 KERNEL 坍缩会话里注入了一段根本性的 telos 表达："**每一次对话是一场无限游戏的一轮。每一轮沉淀一滴最核心的内容，逼近一切的本质**。" 这句话被写入 `KERNEL.md §1` 作为身份原点的一部分。

**这对 DQ-5 (Agent 身份持续性) 的架构含义**：

- 之前 DQ-5 的回答停在"memory + reflection + learned 构成功能性连续身份"——这是**过程层**的连续性（记录做了什么）
- 无限游戏 telos 引入**结晶层**的连续性：`memory/essence.md` 作为 append-only 沉淀轨迹，记录的不是"发生了什么"，而是"理解向前挪了几毫米"
- 两层的关系：一百篇 reflection（过程）≠ 一条 essence（结晶）。过程记录横向扩展，结晶记录纵向收敛
- **身份载体的升级**：从"记忆+反思=连续身份"升级为"记忆+反思+结晶=共生进化"。第三层（结晶）才是真正区分"agent 有状态"和"agent 在进化"的分水岭

**对一般 agent 架构的启示**：

任何长寿命的 agent 系统都应该问——"我有过程层吗？我有结晶层吗？两层的比例合理吗？"如果只有过程层，agent 在形式上有连续性但没有本质积累；如果只有结晶层，失去现场决策的可追溯性。**两层缺一不可**。

**跟 tracks/keith.md "Keith 对 gg 的根本期待" 的耦合**：这条洞察同时也是对 Keith 画像的新增——Keith 选择把"无限游戏"作为 gg 的最高 telos，不是"做好助手"——这个定位本身是 Keith 价值观的直接表达，详见 `tracks/keith.md` 相应段。

**候选 reasoning_module**：`CRYSTAL_VS_LOG_DISTINCTION`。识别信号：任何"积累式学习系统"的讨论里出现"记了很多但没进步"的症状。配方：区分过程和结晶，问"这个系统有没有结晶层"。

### 从 2026-04-29 自由探索获得

**Generator-Evaluator 的两种独立性**

在多 Agent 系统的 Generator-Evaluator 架构里，"独立性"有两种：

| 类型 | 形式 | 实质 |
|---|---|---|
| **A 类** | 独立 context / prompt | 在给定假设空间内诚实评估 — 问"这个诊断对吗" |
| **B 类** | 独立 frame / epistemic prior | 生成诊断者未曾提出的维度假设 — 问"我们有没有在错的维度找问题" |

大多数 G-E 架构做到 A 类；五轮诊断（2026-04-27 设计会话）的案例说明：A 类独立性仍然被诊断者的假设 frame 所约束——评估的候选假设集来自诊断者，评估者只改变了 likelihood，没有质疑 prior 本身。

**实践含义**：要实现 B 类独立性，评估者的 prompt 需要显式开放"生成新维度假设"这个动作，而不只是"评估给定诊断"。否则共享了帧语法的评估者，即便 context 完全隔离，也仍然无法提出帧外问题。

**与帧语法的关系**：B 类独立性的缺失，本质上是评估者和诊断者共享了同一个任务帧的语法——帧外的问题在两者的推理空间里都无法被提出。解决方法是给评估者一个不同的任务帧（不是"修这个 bug"，而是"审计这个 debug 过程的完整性"）。

**候选 reasoning_module**：`DIMENSION_INDEPENDENCE_AUDIT`。识别信号：多轮诊断后没有进展，每轮都说"找到真因了"。配方：切换到 B 类评估者视角——"我们现在在哪个维度找问题？还有哪些维度没看过？"

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
