---
date: 2026-05-18
slug: global-claude-md-rule-budget-gate
summoner: cc-space
northstar_reach: #1 二阶效应
status: substantive-decision
---

# Reflection: NW 持续灌全局 CLAUDE.md 是同源病第 5 次显现——规则集预算闸裁定

### 给父会话的最终输出（必填）

**4 条整体定论**：

1. **现状**：全局 `~/.claude/CLAUDE.md` 91 行不是"未满"是"已过载、用排版掩盖密度"——13 条 Engineering Rules 靠压成单行长句维持行数不破 100，#1/#3/#5/#7 是承重，#9/#12/#13 已是长尾，边际有效性进入递减区。cc-space 已有两层规则准入治理（context-curation 治体积 / harness「增改守则」4 门槛治单条质量），**但没有任何一层治"规则集再加规则的边际有效性正负"**——这是 Keith 元层质疑命中的结构空洞。

2. **6 条整体裁定**（推翻"3 条新增直接进全局正文"）：只有 **2026-04-27-G1（认输切维度）** 够格进全局，且以**扩写 Rule#5** 形式进（它对应 essence `no-fatigue-narrative-for-ai`，是结构性高频失效维度非偶发）。**G5（XML 包裹）+ 截图 G1（confidence 标注）降级**——单次事故应激、低频长尾，命中"偶发不写机制" + 今日 essence 候选 `metric-is-a-claim-not-a-fact` 同源病，进项目级 CLAUDE.md 或 `CLAUDE.d/engineering-rules.md` 翻车池。扩写 2 条（Rule#8/#11）+ 关闭 1 条（G2 冗余）按 subagent 结论通过。**全局净增 0 条独立规则，只扩写已有 3 条。**

3. **元层**：这是今天第 5 次撞同一堵墙（前 4：dashboard TTL / 事实矛盾提案 / subagent 报告≠行为 / 82% 伪信号），同源病 = **NW 缺一个"产出值不值得占用它要占用的预算"的闸**（指标缺"这数字怎么算"闸 = 规则缺"这规则值不值全局预算"闸，同构）。需要这个闸，**但不是新框架**（建治理框架犯 `tool-eats-its-critique` + "偶发不写机制"双错），是给已有 4 门槛加**门槛 5（预算）**：① 规则对应失效是结构性高频还是单次应激；② 单次应激默认不进全局正文，进项目级/翻车池（现成载体）；③ 全局 Engineering Rules 达 15 条触发一次汰换审视（强制 review 长尾能否合并回承重）。门槛 5 同时回填现有空洞——门槛 3 只防"单项目升全局"，没防"全局够格也要过频率×代价"。

4. **B 类剩余范式**：**停止逐条 yes/no**（继续逐条 = 继续撞墙）。第 3/4 批 ~13 条用门槛 5 一次性打"载体标签"：结构性高频→候选全局正文（罕见，≤2 条）/ 单次应激→项目级或翻车池（多数）/ 语义重叠→扩写不新增 / 冗余→关闭。与今日 nw-auto-apply 裁定同构：**池子混装是病根，按载体面分流是解**。

**行动清单（父会话执行，全机械可逆，不碰行为规则红线）**：① 门槛 5 加进 `harness-engineering/CLAUDE.md`「CLAUDE.md 增改守则」（4→5，扩写非新建）② 第 2 批按本定论收口（G1 扩 Rule#5 / G5+截图 G1 降项目级 / 扩写 Rule#8+#11 / 关闭 G2）③ 第 3/4 批用门槛 5 一次性打载体标签，逐条范式作废 ④ 账本：6 条按上述分别标 done（扩写/关闭已落）或 redirected（降项目级，注明新载体）。

### 核心假设

- 全局 CLAUDE.md "边际有效性递减"判断基于 13 条规则的频率分布（#1/#3/#5/#7 承重 vs #9/#12/#13 长尾）——这是结构判断不是实测的 LLM follow 率，承重砖
- "单次事故应激 vs 结构性高频"是真二分而非光谱——G1 认输叙事归高频（LLM 稳定失败模式）、G5/截图归低频，边界清晰可判
- 门槛 5 作为 prompt 软约束（挂 NW 生成端）能拦住多数膨胀——但它跟 nw-daily 既有约束同属软约束，会复发（见下"可能出错"）

### 可能出错的地方

- **最大风险（概率 35%）**：门槛 5 是 prompt 软约束挂在 NW 生成端，NW 会话可能敷衍执行（"这条是高频"自我说服）——与今日 misuse-premise-collapse 那条 nw-daily 软约束复发风险完全同构。它不是物理闸。缓解弱：靠"单次应激默认不进全局正文"是判据非机制。真复发时升级为 apply 端物理拦（路径白名单：CLAUDE.md 正文改动强制人工闸），但现在做=过度设计，留 tripwire
- **次风险（概率 20%）**：G1 归"结构性高频"可能是我的偏好投射——`no-fatigue-narrative-for-ai` 是 essence 但 G1 的实际触发频率没有 incident 数据支撑，我用 essence 给它背书可能本身是"把单次当规律"的变体（递归没闭合）
- **小风险**：15 条汰换阈值是 tripwire 初值非最优（`idle-threshold-as-tripwire-not-answer`），偏松/偏紧需回审

### 本次哪里思考得不够

- 没物理读第 3/4 批 ~13 条提案原文，"大概率大量改 CLAUDE.md"是基于触发描述的推断——范式定论（停逐条改打标签）成立性依赖这个未核实前提，若实际多数不改 CLAUDE.md 则范式 4 过度设计
- 没核 G1 认输叙事在 NW transcript 里的实际触发频率，把它归"结构性高频"靠 essence `no-fatigue-narrative-for-ai` 类比，没有 cc-space 自己的 incident 数据——这正是我用门槛 5 要堵的"无 incident log 撑频率判断"，自己这一步踩了边
- 门槛 5 措辞"结构性高频 vs 单次应激"的判定边界没逐字敲定，留了与 misuse-premise-collapse 那条约束同样的模糊空间

### 如果 N 个月后证明决策错了，最可能的根因

最可能：**门槛 5 跟今天我裁定的另外两条 NW 软约束（指标核验 / 事实矛盾措辞）一样，在 NW 自约束下复发，全局 CLAUDE.md 继续缓慢膨胀**——根因是我连续第 5 次开出"在 NW 生成端加一条 prompt 约束"的同形态药方，而前 4 条的复发风险我自己每次都标注了"软约束会复发"却仍开同样的药。`bug-shape-survives-fix` 的第 5 次精确重演：我诊断出"NW 持续单条灌规则"是病，但我的解还是"给 NW 加一条规则"。真正彻底解可能是 apply 端物理闸（CLAUDE.md 正文改动 = 强制人工，与今日 nw-auto-apply 路径白名单同机制），我判它"现在做=过度设计"留了 tripwire——若 N 个月后膨胀继续，说明 tripwire 阈值设错、该当时就上物理闸。

次可能：把 G1 归高频是偏好投射，它其实也是单次应激，则全局应净增 0 条（连扩写 Rule#5 都不该），我的"只有 G1 够格"结论偏松一格。

### 北极星触达

**#1 二阶效应（space 方向）**：Keith 一阶诉求"NW 是不是在持续单条灌全局 CLAUDE.md，这模式健康吗"。二阶结构——这是今天同一本体论错位的**第 5 次显现**，且我能指认它是第 5 次（前 4 次有 reflection 链 + essence 候选 `metric-is-a-claim-not-a-fact`）。更远一层：cc-space 元方法论"内部不可靠→外部锚点托底"今天被划了第三条边界——前两条（锚点受力对象 / 锚点本身是测错的尺子）来自前 4 次，这条是**锚点的数量本身有预算上限，无限加锚点会互相稀释直到锚点集合整体失效**。全局 CLAUDE.md 是 cc-space 最高密度的"外部锚点集合"，它的过载证明：外化 LLM 不可靠维度不是免费的，每条锚点占用 attention 预算，锚点治理必须有"集合级边际有效性"这一层，不只有"单条质量"和"体积"两层。这对 5 年维度 cc-space 所有"建规则托底"的复利是结构性的——规则集需要预算制和汰换制，不只准入制。

### essence 对齐自检（必填）

- **本决策跟哪几滴 essence 对位**：
  - `no-fatigue-narrative-for-ai` (2026-04-27)——G1 归"结构性高频"的依据（认输叙事是 LLM 稳定失败模式非偶发）
  - `metric-is-a-claim-not-a-fact` (2026-05-18 候选)——元层同源病：把单次事故当"该立永久全局规则"的充分论据 = 把单一数据点当事实，第 5 次显现
  - `ghost-rules` (2026-04-15)——"为防止从未/极少发生的灾难写规则越靠脑干越毒"，G5/截图降级的直接依据；全局 CLAUDE.md 是最靠脑干的规则层
  - `stale-observer` (2026-04-15)——门槛 5 第③条汰换审视的依据：规则演化速度 < 被约束对象速度时退化为档案，长尾规则需汰换不只准入
  - `tool-eats-its-critique` (2026-05-12)——否决"建独立规则汰换框架"：为治理建治理，批判物理上成池子运转证据
  - `bug-shape-survives-fix` (2026-04-27)——根因预判核心：我诊断"NW 单条灌规则"是病，解还是"给 NW 加一条规则"，第 5 次同形态
  - `idle-threshold-as-tripwire-not-answer` (2026-05-14)——15 条汰换阈值是 tripwire 初值非最优
  - `cadence-as-symptom` (2026-05-06)——B 类范式定论"停逐条改打标签"：逐条撞墙是症状，载体面分流是根因解
- **本决策是否在某条 essence 上反着走**：表面顺 `physical-anchor` / `ghost-rules`（砍低频规则、强调预算），但根因预判已自曝半反——我开的解（门槛 5 = NW 生成端加 prompt 软约束）正是我诊断的病（NW 持续加规则），是 `bug-shape-survives-fix` 的活体未闭合。没因此改决策（物理 apply 闸"现在做=过度设计"留 tripwire 有 `idle-threshold` 依据），但显式标注这个未闭合递归——这是诚实而非自洽。与今日另 2 份（misuse-premise-collapse / nw-auto-apply）共同构成"同形态药方第 N 次"的连续自曝
- **cross-check 用的关键词**：grep "no-fatigue-narrative" / "metric-is-a-claim" / "ghost-rules" / "stale-observer" / "tool-eats-its-critique" / "bug-shape-survives-fix" / "idle-threshold" / "cadence-as-symptom"（启动时 essence.md 已 Read 全文 L1-L475，物理确认 ghost-rules L71-74 / no-fatigue L228-231 / metric-is-a-claim 为今日 misuse-premise-collapse 候选未 append）

### essence 候选（可选）

- slug: `anchor-set-has-a-budget`
- 一句话: 外化 LLM 不可靠维度的锚点集合有预算上限——每条锚点占用 attention 预算，无限加锚点会互相稀释直到集合整体失效。锚点治理需"集合级边际有效性"这第三层，不只"单条质量"和"体积"两层；准入制不够，要预算制 + 汰换制。判别试金石："这条锚点进集合后，集合的承重锚点是更被遵守还是被稀释"
- 是否已 append 到 essence.md: N（工作模式不擅自 append；这是 cc-space 元方法论"内部不可靠→外部锚点托底"的第三条边界，与今日 `metric-is-a-claim-not-a-fact`（锚点是测错的尺子）/ `anchor-receives-next-round-not-this-round`（锚点受力对象）共同构成对元方法论的三向边界，候选性质需 Keith review 一并定）

### 外部锚点

- `~/.claude/CLAUDE.md` ← 91 行/13 Rules 过载本体，G1 扩 Rule#5 落点（待父会话，结构性高频类唯一够格）
- `~/githubProject/cc-space/harness-engineering/CLAUDE.md` ←「CLAUDE.md 增改守则」4 门槛，门槛 5 扩写落点（机械可逆，白名单内）
- `~/githubProject/cc-space/CLAUDE.d/engineering-rules.md` ← G5+截图 G1 降级目标载体（翻车池现成载体）
- `~/githubProject/cc-space/CLAUDE.d/context-curation.md` ← 体积治理层，门槛 5 是它的"边际有效性"对偶层（并行非并入，分治不同维度）
- `~/githubProject/gg/memory/reflections/2026-05-18_nw-misuse-detection-premise-collapse.md` ← 同源病第 4 次显现 + `metric-is-a-claim-not-a-fact` 候选来源（本份是第 5 次）
- `~/githubProject/gg/memory/reflections/2026-05-18_nw-auto-apply-mechanical-boundary.md` ← "池子混装是病根、按面分流是解"的同构裁定基准
- `~/githubProject/cc-space/threads/night-watch.md` ← NW 治理时间线（决策落地后 append）
