---
date: 2026-06-01
slug: monster-memory-reconsolidation-vs-append-only
summoner: monster
northstar_reach: #1 二阶效应（记忆体系的不变性分配是 5 年维度的承重墙）
status: substantive-decision
---

# Reflection: monster 当前态 re-derive 范式 vs OpenSpec append-only / compound-engineering 五选一

## §A 范式 A — 决策的元属性反思

### 给父会话的最终输出（必填）

**决策（三问分别裁决）**：

**问题 1 — 初判方向对，但有一处需要精化，不能整段照收。**
- 对的部分：表面张力确实是伪张力。OpenSpec 的 append-only delta-merge 对 monster **冗余**。"时间线 append-only（episodic，永不改写）+ 当前态 re-derive（semantic gist，允许重建）"与 5-22 三层映射自洽。关键区分：monster 的 re-derive **不改原件**（时间线），所以它不是 confabulation，是「可重做的有损压缩」——有损但可逆。人脑 confabulation 的真正危害是「原件被改写、无法复原」，monster 物理上规避了它。这点初判看准了，OpenSpec 不引入。
- **必须精化的部分（保守派未被完全击败的残留风险）**：「保真守在时间线层」在**存储语义**上成立，在**激活语义**上有泄漏。消费会话实际读的是 `## 当前状态`，不是每次回溯时间线。re-derive 若丢了承重细节而无人校正，那条细节在「实际被使用」层面就等于丢了——时间线里躺着 ≠ 被激活（我自己昨天沉淀的 `anchor-value-in-activation-not-in-content`）。所以"re-derive 不损保真"成立有一个前提：**当前态丢的细节必须是「丢了也无所谓 / 需要时回溯得到」的那类**。对叙事 thread 成立，对契约类不成立。这把问题 1 直接桥到问题 2。

**问题 2 — 这是真张力不是伪张力。契约类和叙事类应该用不同维护范式，且 monster 事实上已经在用，只是没显式化。**
- 叙事 thread 的当前态：有损压缩可接受，消费者读它是"快速进入状态"，错一句不致命且会回溯校正 → **re-derive 合适，保持现状**。
- 契约类（canon / SSOT registry / 契约型 thread 的硬条款）：错一个字 = 下游会话被误导且**不回溯**（契约的全部意义就是「不用每次回溯原始推理、直接信当前条款」）。给一个"不被回溯校正"的消费入口配一个"有损压缩"的生成器 = 范式错配 → **必须 append-only / 人工 delta，禁止 re-derive**。
- 关键事实：**monster 实际上已经在用两种范式**——canon.md 本来就是 append-only、done 5F 直接写、从不 re-derive；只有 threads 的 `## 当前状态` 走 re-derive。所以不是"要不要引入第二种范式"，是"把已存在的两种范式的边界**显式钉成契约**"，防止未来有人手滑把 re-derive subagent 指向 canon / SSOT registry。"统一一种机制的简单性"在这里是**虚假简单**——两类对象的回溯语义不同，强行统一就是用叙事的容错率去赌契约的零容错。
- **OpenSpec 的独立价值**：作为 monster **契约类**记忆的范式背书是成立的（它证明了"canonical 永不被重写、只能 archive delta merge"是成熟工业实践），但 monster 的 canon.md append-only 已经覆盖同一内核。OpenSpec 强制写结构化 `## ADDED/MODIFIED/REMOVED` delta 的维护负担，对超级个体（B2）不划算——那是为多人协作的 spec review 设计的仪式。**结论：不引入 OpenSpec 机制，但用它的分类验证 monster 应显式区分两类记忆。**

**问题 3 — 五选一处置语义值得吸收，但只能做「人工触发的维护 skill」，绝不进夜跑自动跑。**
- auto-delete 三条件 + 无监督触发 = 正面撞 5-22 ruled-out（无监督 cron 做语义判断污染 SSOT），且撞我的 `theory-gap-without-data` + `fermentation-without-detector`——禁止吸收这一面。
- 但"五选一 taxonomy"（Keep/Update/Consolidate/Replace/Delete）跟"谁来跑"正交。monster 的 fold_thread.py **只有"按时间截断"一个动作**，缺的恰是"对照现状判断 stale → Replace/Delete"的语义——这是初判看对的真缺口。当前 fold 把"最近 5 条"无脑留、其余进 _archive，一条 3 个月前的过期条目可能恰好在最近 5 条里被永久留在当前态视野，而一条承重的老约束可能被截走。
- **落点**：把五选一 taxonomy 做成 **done 5F 的人工处置选项 / 一个人工触发的 `thread-curate` skill**（Keith 或 done 会话在场时调），而不是夜跑动作。Delete 永不自动（撞 ruled-out + macOS rm 不进废纸篓的安全红线），最多到 Replace（隔离 context 写继任者、旧条目标 `[superseded]` 而非删，符合 monster "切断追溯链=禁" 的既有纪律）。compound-engineering 的"入链分类把 Delete 降级为 Replace"这条直接可借——它和 monster 的"prefer 标记不 delete"同构。

**行动建议（给父会话，按优先级）**：
1. **最高优先、低成本、高 ROI**：在 `inbox/README.md` 或 `CLAUDE.d/persistence.md` 写死一条契约——「re-derive subagent 的作用域 = threads 的 `## 当前状态`；canon.md / concepts.md / ssot/registry.md / 契约型 thread 硬条款 = append-only，禁止 re-derive 重写」。这是把已存在的隐式边界显式化，防手滑。可逆、一句话。
2. **中优先**：给 5-30 起的 re-derive 夜跑加一条**自检不变式**——re-derive 后 diff 新旧当前态，若删除了带"决策/约束/不可/禁止/契约/SSOT"等承重词的句子，标记该 thread 让 Keith 人工过一眼（不自动删，只升可见性）。这对冲问题 1 的"激活语义泄漏"残留风险，成本低。
3. **低优先、可延后**：把五选一 taxonomy 落成人工触发的 `thread-curate` 维护动作（done 5F 扩展或独立 skill），补 fold 只截时间不判 stale 的缺口。Delete 封顶到 Replace。这条不急，缺它现状不塌。
4. **不做**：不引入 OpenSpec 的结构化 delta 目录；不引入 compound-engineering 的 auto-delete 三条件 / 无监督触发。

### 核心假设

1. monster 消费会话读 thread 时，绝大多数只读 `## 当前状态`，极少回溯 `## 时间线`——这是"激活语义泄漏"风险成立的前提。若实际上消费者高频回溯时间线，残留风险被高估、行动建议 2 的优先级可下调。
2. canon.md / SSOT registry 当前确实走 append-only 而非 re-derive——基于 prompt 提供的事实（done 5F 写、append-only）采信，未独立物理核验 fold.py 和夜跑 subagent prompt 的实际作用域。

### 可能出错的地方

最可能崩在行动建议 1 的"已存在两种范式"判断上——如果 5-30 那次改造实际上把 re-derive subagent 的作用域设成了"整个 thread 文件"而非"仅 `## 当前状态` 段"，那 canon 类内容若曾被并进某个 thread 就会被 re-derive 误伤。概率中等。父会话应物理核一下夜跑 subagent 的 prompt 作用域边界，再落契约 1。

### 本次哪里思考得不够

没有物理核验 fold_thread.py 和 5-30 re-derive subagent 的真实 prompt（context 是 push 进来的，我按 prompt 采信）。"契约类 thread 硬条款"这个类别的**判别标准**没给——一个 thread 既有叙事又有硬条款时（很常见），re-derive 该如何只重写叙事段不动条款段，我只给了方向没给可操作切割线。这是留给落地的真空。

### 如果 N 个月后证明决策错了，最可能的根因

行动建议 1 的契约写下后无事件层强制（`rule-layer-flywheel`：prompt 层规则 = 跑步机）——未来某次夜跑 subagent 改了 prompt 把作用域扩到全文件，没人记得这条契约，canon 类内容被 re-derive 误伤。真正的根因会是"我把一条该挂事件层（PostToolUse 校验 re-derive 作用域）的契约写成了 prompt 层文字"。行动建议 2 的自检不变式是对冲，但我没把它定成硬 gate。

### 推理盲区

我对"契约 vs 叙事"二分可能过度清晰化——真实 thread 多是混合体，二分边界在混合 thread 上模糊。我用 conservative + red-team 攻了 re-derive 损保真，但没攻"二分本身是不是伪二分"（symmetric-form / 抽象层混淆的风险）。`control-flow-vs-fact-supply` 提醒我：先验证张力在不在同一根轴上——契约/叙事是不是同一根轴上的两端，还是我造的伪对撞？我倾向认为是真轴（回溯语义不同是物理差异），但未穷尽。

### essence 对齐自检（必填）

- **本决策跟哪几滴 essence 对位**：
  - `invariance-allocation` (2026-04-19)——本质就是"记忆体系把不变性分配给哪一层"：时间线层选为不变点，当前态层选为可变点。这是核心锚。
  - `survey-as-coordinate` (2026-04-23)——OpenSpec/compound 对照后多数坍缩为"已做、差名字"（monster 已有两种范式、已有 append-only canon），但**不是全坍缩**：五选一 taxonomy 是真增量坐标。精确应用了"差名字 ≠ 差能力，但要分清哪些真差能力"。
  - `anchor-value-in-activation-not-in-content` (2026-06-01)——直接撑起问题 1 的"激活语义泄漏"残留风险（时间线里躺着 ≠ 被激活）。
  - `ssot-distillation-vs-buffering` (2026-05-01) + `default-bucket-as-deadlock`——支撑"五选一只能人工触发不能夜跑"（无监督维护是漂移温床）。
- **本决策是否在某条 essence 上反着走**：潜在张力 `means-end-inversion` (2026-04-30)——我建议加自检不变式 + 维护 skill，有"为记忆体系造维护机制反而把维护吞噬为主战场"的风险。本次主动压住了：行动建议 1（一句话契约）零维护负担，建议 3（维护 skill）标了"低优先可延后、缺它不塌"，没让工具吞噬目的。判定为"对冲到位，非反着走"。
- **cross-check 用的关键词**：grep 心智过 reconsolidation / append-only / 保真 / invariance / survey / activation / ssot / 无监督 / fermentation / means-end。

### essence 候选（可选）

- slug: `reconsolidation-safe-iff-original-immutable`
- 一句话: 记忆的"重新归纳"只在原件不可改写时不构成 confabulation——危害不在"重新归纳"，在"归纳结果覆盖了原件"；有损但可逆 ≠ 失真不可复原。其消费侧推论：派生层的有损在"实际被读的是派生层"时会从存储泄漏到激活，故零容错的契约类记忆禁止派生重写、只能 append-only。
- 是否已 append 到 essence.md: N（留给父会话转述后，由 Keith review，subagent 模式不擅自 append 跨命根判断）

### 北极星触达

#1 二阶效应——记忆体系的不变性分配是 5 年维度的承重墙，选错的下游污染是缓慢且复利的（错误条款被复读、误导后续每一次会话决策）。这正是"看得更远"。

### 外部锚点（可选）

- monster 侧落点建议：`monster/threads/ai-memory-evolution.md`（主体时间线）+ `CLAUDE.d/persistence.md`（契约 1 落点）
