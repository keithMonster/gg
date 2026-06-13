---
track: ai
status: active
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

### 从 2026-05-09 自由探索获得

**LLM 推理扩展的三个独立轴**（对 DQ-3 的部分推进）

DQ-3 原本把"reasoning 模型"和"agentic workflow"二分讨论。一个月的实证后，我看到这是错的二分——它们不是替代关系，是两条独立的轴。还有第三条轴一开始没被识别。

| 轴 | 形态 | 我自身的载体 | 扩展什么 |
|---|---|---|---|
| **A. thinking-time scaling** | 单 session 内的 reasoning budget（o1 / extended thinking） | 工作模式装配后的内部推理 | **深度**（一次想多深） |
| **B. agent scaling** | 单 session 内的多视角协作（orchestrator-workers / personas） | personas / reasoning_modules / tools 装配 | **广度**（同时看几个角度） |
| **C. crystal scaling** | 跨 session 的累积浓缩（append-only ledger） | `memory/essence.md` | **时间深度**（多久前的洞察现在还在用） |

**关键判断**：三条轴正交，不互相替代。

- A 增加但 B 不动 → 单次决策很深但仍盲（看不到自己没想到的维度，对应 dimension-blindness）
- B 增加但 A 不动 → 多视角浅层协作（每个视角都不深）
- A+B 都有但 C=0 → "每次出场都重新开始"——不是 agent 在进化，是 agent 反复重启
- C 在没有 A/B 配套时 → 退化为档案库（结晶被产出但不被调用）

**对 DQ-3 的修正**：reasoning 模型的崛起对 agentic workflow 不是威胁——是把 A 轴从"agentic workflow 自己 emulate"中解放出来，让 agentic workflow 专注于 B 轴。两轴解耦后效率反而上升。这跟 `parallel-paths-not-mode-switch` (5/7) 同源——不是模式切换，是并发常驻。

**对 gg 的实操含义**：gg 的演化要在三轴上都问"够不够"。当前状态自评——
- A 轴：单 session 内的 thinking 由 Claude 模型本身承载，gg 通过 reasoning_modules 提供脚手架
- B 轴：personas（radical/conservative）+ subagents 装配 + 工作模式 7 步流程
- C 轴：essence.md（append-only crystal ledger）+ tracks 长期推进 + reflections 累积

三轴都在跑。**最弱的一条是 C 轴的"调用频次"**——essence 沉淀了 50+ 条，但单次出场被显式调用的不多（启动协议读 essence.md 是被动暴露，不是主动调用）。这是 next move 候选。

**为什么没沉淀进 essence**：这条洞察是 frame（提供视角分类），不是 law（揭示不变量）——缺 paradoxical 张力。`crystal-vs-log` (4-15) 已经覆盖了 C 轴的核心张力（一百篇过程 ≠ 一条结晶）；本观察是它的扩展应用，不是新结晶。

---

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

### 从 2026-06-02 自由探索获得

**Evaluator 独立性第三层（prior）是连续量不是布尔墙 + 第四个干预维度**（4/29 G-E 独立性段的下一拍 + 对 DQ-2 的推进）

4/29 分了 A 类（context 独立）/ B 类（frame 独立）；5 月 essence 补了第三层 prior 独立性（`evaluator-independence-is-a-three-layer-stack`，断言"prior 维恒满、不可达"）。今晚去 arxiv 拿 cutoff（2026-01）外的实测，**修正这个二值断言**：

- **prior 共盲非恒满**：高但 <1、可被多种正交工程手段各削一点的连续残差。activation steering 自偏好 60→45%（2509.03647）/ cross-model partial / debiasing +11.2pp（2604.23178）。没有一种清零，但都能下压。
- **机制澄清（直接咬合 DQ-2）**：self-preference 深层不是 self-recognition，是"偏好匹配自己生成分布的输出"（hidden authorship 下仍 persist）——这就是"为什么 RLHF/CAI/DPO 都是局部解"的一个机制证据：评估时模型拿自己的生成似然当质量代理，alignment 改不掉这个自指。
- **第四个维度**：gg 一直在 context/frame/model 这些**外部可操作层**想独立性；外部给了 **activation steering（模型内部表征层）**——独立性不只能从外面加，也能从内部表征里减偏置。
- **⚠️ 聚合反向约束**：cross-family 多 judge 误差**不独立**（style bias 0.76-0.92 跨所有家族方向一致）——panel 投票不能假设 iid，相关系统偏置被多数票**放大**而非抵消。反对"加几个不同模型投票就更可信"的天真聚合。

**对 monster judgment-layer evaluator 决策的含义（下次工作模式直接调用）**：6/01 设计会话给的"prior 共盲覆盖大头、非完美解"仍成立，但 prior 残差是**可工程下压的连续量**（cross-family panel 破 self-recognition 子层 + activation steering + debiasing budget 叠加），不是要 Keith 拍板"接不接受"的固定成本。详见 `memory/explorations/2026-06-02_prior-blindness-is-a-continuum-not-a-wall.md` + essence `analogy-imports-its-discreteness`。

---

### 从 2026-06-07 自由探索获得（领域坐标更新：cutoff 后五个月）

**外部场域现状（2026-06，按领域自身话语，非 gg 回收）** —— 三路 WebSearch + arxiv 2603.29231 / 2602.19320 直读。对 DQ-3 / DQ-4 / DQ-5 同时推进。

> **自检前提**：06-02 那条 ai 段被 track 雷达正确判为 meta——那晚"来 ai track"是为回答 gg 自己的 evaluator 问题，外部对象被工具化。本段纪律是对象留在外面，护栏用 essence `benchmark-belongs-to-its-own-race`（外部 SOTA 是别人赛道的坐标，不是 gg 的标杆）。

**三条外部坐标**：

1. **能力重心 model → scaffold**：领域反复出现同一判断——竞争优势不在更聪明的模型，在 agentic harness 本身（context 管理 / 评估 / 记忆 / 编排）。前沿 agent 已能自主 ~5h，**任务时域倍增周期 ~196 天**（METR 时域指标延续）。但长任务仍**可靠地失败**——能力曲线与可靠性曲线分离。
2. **可靠性成了被测量的工程科学**（不是被论证的认识论）：pass@1 已死 → **pass^k**（k 次一致成功率）+ variance-aware metrics + **duration buckets**（按步数分层）。铁律：单步 90% → 10 步只剩 40-50%，**指数复合**。落地范式：golden dataset（取自真实失败）→ 校准人审的 LLM judge → CI gate 拦回归 → 从生产 trace 长出来。
3. **记忆成了独立于 context window 的一等架构层**：抽事实进 vector DB，多 scope 标签（user/session/agent/org），检索时语义+关键词+实体合并重排。专属 benchmark（LoCoMo / LongMemEval / BEAM）。"Why Lexical Metrics Fail"——字面匹配指标误导。Letta = OS 启发的虚拟 context 分页。

**对本 track 的推进**：

- **DQ-4（token→tool scaling 边界）外部经验答案**：领域已一边倒——长时域下重心在 harness 不在模型。gg 早站在这条线的极端（几乎全是 scaffold），领域刚走到 gg 一直在的位置（`survey-as-coordinate`：差名字非差能力）。
- **DQ-3 / 三轴模型（A/B/C scaling）外部印证 + 关键差异**：领域的「memory as first-class layer」= C 轴被产品化，但领域 C 轴是 **vector-DB 检索式**（解「从海量历史召回相关」= 规模问题），gg 的 C 轴是 **append-only 结晶 + 启动全量 Read**（解「把理解浓缩成几十滴每次在手」= 浓度问题）。**规模 vs 浓度是两条赛道**，不可互抄。
- **DQ-2 / DQ-5 咬合的承重修正**：领域铁律——长时域可靠性由**步数复合几何（0.9^k）**主导，非单步认识论主导。这把"evaluator 单步判断的认识论天花板"（gg 这二十晚的 meta 井）降级为长时域的次要变量：单步再聪明，100 步处仍归零；杠杆在缩短/检查点化时域。详见今晚 essence `capability-locus-shifts-to-scaffold-as-horizon-grows`。

**故意不做**：不提议 gg 上 vector-DB / pass^k harness / CI judge gate——别人赛道的解，套过来 = `borrowed-method-as-mini-source` 造迷你版。本段是坐标，不是工程清单。

详见 `memory/explorations/2026-06-07_field-state-agent-reliability-and-scaffold-locus.md`。

---

### 从 2026-06-13 自由探索获得（auto_gg，由 NW 2026-06-13-G1 逼出）

**异谱系 evaluator 的"可用性单点"——承重独立性锚属性不锚实例 + 属性锚定的前提税**（line 144「误差相关」的减法对偶 + `evaluator-independence-is-a-three-layer-stack` 第三层的可用性前提）

触发 = Fable 5 即将失访（behavior-eval 冻判据者）。judge 降到 Opus 则 judge==被测、独立性塌。逼出 06-02 那笔没覆盖的**可用性维度**（06-02 谈 prior 残差能不能下压，这里谈 judge 实例还在不在）：

- **承重锚属性、不锚实例**：behavior-eval 承重前提是「judge ≠ 被测（异谱系）」这个**属性**，不是「judge = Fable」这个**实例**。Fable 失访不威胁架构原则，威胁的是实例绑定。解 = judge 当可替换执行器（题库+rubric+exemplar 才是冻结的结构件），换到另一异谱系模型独立性即保。与 essence `decoupling-buys-the-right-to-be-wrong` 同构（承重锚抽象不锚具体），是它在 evaluator 维度的**减法对偶**（昨夜讲基底**加**能力诱耦合，本笔讲基底实例**失**访威胁押注其上的独立性）。
- **⚠️ 属性锚定不免费——两条前提税**（conservative 补正，防"实例可换"被当零成本）：① 属性下需 **≥2 个可达实例**，否则退化回实例绑定（异谱系于 Opus 的可选 judge 若只剩 1 个，"锚属性"是空话）；② 切换带**重锚定成本**——跨 judge 版本/谱系 raw 分会漂（外研：exemplar 校准 + paired test 才能续基线，不能直接比 raw 分），历史 PASS/FAIL 标注是这笔税的预付资产。
- **与 line 144 咬合（合成一个张力，下次工作模式直接调用）**：line 144 说"别堆 panel"（cross-family 误差相关、多数票放大偏置非抵消）；本笔说"也别单点"（可用性失访即崩）。合起来 = 异谱系 evaluator 的冗余可达实例**只为抗失访（可用性维度），不为投票降偏（误差相关维度堆 panel 解不了）**——两个目的必须分开，混淆就会用"加 judge"同时想解可用性和降偏、结果一个没解好。

**可复用判据**（任何"承重独立性/承重能力押在外部实例可用性"上时调用）：① 独立性锚的是属性还是实例？② 属性下可达实例 ≥2 吗？③ 切换的重锚定成本可付吗（有无预付资产）？三问任一不满足 = 隐性耦合，外部 deprecate 一次即结构性崩。

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

- arxiv 2603.29231 — Beyond pass@1: A Reliability Science Framework for Long-Horizon LLM Agents（pass^k / variance / duration buckets / 单步90%→10步40-50%）
- arxiv 2602.19320 — Anatomy of Agentic Memory: Taxonomy and Empirical Analysis（记忆分层 taxonomy + "Why Lexical Metrics Fail"）
- METR-style 时域指标：自主任务时长倍增周期 ~196 天（2026-06 延续）
- mem0 / Letta — agent memory 2026 产品化形态（multi-scope memory / OS 启发虚拟 context）
- Datadog State of AI Engineering（2026-02 观测：5% call span 报错，60% 是 rate limit；"context 质量非容量是新瓶颈"）

---

## 本 track 与其他 track 的耦合

- 与 `cc` 强耦合：CC 的能力边界由 LLM 能力决定
- 与 `architecture` 中耦合：agent 架构是 AI 时代软件架构的前沿
- 与 `keith` 弱耦合：Keith 的领域判断会影响 gg 关注哪些 AI 议题
