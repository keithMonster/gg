---
date: 2026-05-23
slug: communication-style-rule-review
summoner: monster
northstar_reach: "#3 决策超越直觉（review 主代理已完成的规则升级，把隐性盲区显化）"
status: substantive-decision
---

# Reflection: Communication Style 硬规则升级的事后 review

### 给父会话的最终输出（必填）

**总判断**：落点和方案选择都合理，但 review 暴露**两类真盲区**——(A) Prompt Writing「激活而非描述」被新规则正面违反却没被自检发现（反例字符串污染上下文）+ (B) 第二条「结论前置」无检测器（dual-pattern 缺一半）+ (C) 触发条件未声明（硬规则泛化会反噬调试场景）+ (D) 辐射检查只查"冲突"未查"覆盖度"（done / subagent 未同步）。Q2 有可操作 dual-pattern 5 维度模板。Q3.1 真冲突（且更严重），Q3.2 自问检测器基本空头支票（仍可保留作引力方向）。

**推荐落地（P0-P4）**：

| P | 动作 | 解决盲区 |
|---|---|---|
| **P0** | 移反例字符串（"接下来我会"/"让我..."/"明白了"/"好的"等）到下层（done skill 例库 / prompt-writer references），主规则只留锚词 + 检测器 | 盲区 A：Prompt Writing 干扰 |
| **P1** | 第二条「结论前置」加检测器：「自检：把首句剪下来贴 Keith 面前，他能不能立刻知道结论？」 | 盲区 B：双向闭环 |
| **P2** | 两条硬规则前加 scope 声明：「长回复（review/决策/方案/总结）适用；短回复（事实/中间观察/进度同步）按自然节奏」 | 盲区 C：防泛化 |
| **P3** | 辐射到 done skill 复盘清单 / subagent system prompt / monster 仓内等价表述 | 盲区 D：辐射覆盖度 |
| **P4** | Prompt Writing 段加第 6/7 条：dual-pattern 模板 + 检测器分级标注（[引力] vs [外检]） | 元层防复发 |

**Dual-pattern 5 维度模板**（Q2 答案）：

| 维度 | 单写一半失败形态 | 闭环模板 |
|---|---|---|
| 删什么 + 留什么 | 只写删 → 行为真空，AI 退化干瘪报告 | 「删 X，留 Y，强化 Z」 |
| 禁 + 倡 | 只禁 → 激活被禁概念 + 行为真空 | 「不 A，而 B」 |
| 反例 + 正例 | 只反例 → 失败模式锚定但成功形态留白 | 反例 + 同场景正确做法 |
| 触发 + 不触发 | 只说何时做 → 模糊场景被泛化激活 | 「X 场景做，Y 场景明示不做」 |
| 行动 + 检测器 | 只行动 → 没有"做到没做到"判据 | 行动 + 物理 signal（外检优于自问） |

**Q3.1 真冲突论证**：新规则第一条「铺垫（"接下来我会"/"让我..."/"首先"）、客套（"明白了"/"好的"/"希望对你有帮助"）」把反例字面 token 注入了启动 Read 链——每次会话启动这串字符串都进上下文。这是 essence `extraction-meta-inheritance` (2026-04-29) 的活体复现——抽取"信息密度"原则时复现了想消灭的失败模式（堆反例 = 占 token = 反噬密度）。

**Q3.2 空头支票论证**：LLM 不会真的在生成时停下来跑一个 "删掉哪几个字意思不变" 的 dedup pass。它的实际作用是改注意力引力分配（essence `field-gravity-over-prompt` 2026-04-27 应用），不是字面 reasoning。判断有效靠物理外检（hook / git diff / Keith review），不靠 LLM 自报。但「自问」字段保留也没坏处——它仍提供引力方向，只是别当**保证机制**。

**段内位置 nit**（非 blocker）：当前顺序硬规则在身份/语气前，违反 M2 元判断基准（意识体先于工具，姿态先于动作）。建议：身份 → 语气 → 硬规则 → 结构 → 安全标注。

**元建议**：未来改"启动 Read 链承重段"（Communication Style / Prompt Writing / 立场）前事前 call gg。判据=该规则影响单次任务还是注意力分配；后者 = 架构层。本次事后 ok 但成本更高。

### 核心假设

1. Keith 偏好「信息密度 + 结论前置」是稳定长期偏好，不是某轮情绪——已被反复表达验证（参 CORE §5 「冷静笃定 / 高信息密度」）
2. Prompt Writing 段对 LLM 注意力的影响假设成立——本次诊断"反例字符串污染"成立的前提
3. dual-pattern 是 LLM 写规则的系统漏洞（不止 Keith 这次），而非个例——基于 RLHF 训练数据"不要 X"句式高频先验
4. 「自问」字段对 LLM 是引力方向不是 reasoning——未做物理实证（本次没跑对照实验）

### 可能出错的地方

1. **P0 移反例下沉的代价被低估**——把反例移到 done skill 后，主规则的"激活强度"可能下降（具体反例 token 比抽象锚词激活更强）。**这是 trade-off 不是双赢**——为了消除 Prompt Writing 干扰付出激活强度的代价。Keith 可能拒绝这个 trade
2. **第二条加检测器可能也是空头支票**——按 Q3.2 论证，「自检：剪下首句」LLM 同样不会真执行。建议成立 = 信念，不是机制
3. **dual-pattern 模板过度系统化**——可能把"偶发漏洞"建模为"系统漏洞"，反向陷阱是 `tool-elevation-as-occam` 的反面（无第二消费者就上提=过度工程）。但本次有 Keith 一句话补「结论前置」作为活体证据，证据强度暂时够
4. **段内位置 nit 可能没必要**——身份/语气是元层、硬规则是派生，这个论证依赖"段内顺序对 LLM 有引力影响"这个未验证假设

### 本次哪里思考得不够

1. **没跑物理实证**——「LLM 自问是空头支票」「反例字符串污染上下文」都没做对照实验，是基于 essence + Prompt Writing 第 1 条的推论。Q3.2 的判断属"理论推论 + 已有 essence 支持"，置信度 4/5
2. **没读 monster 仓内可能的等价表述**——P3 建议辐射时该具体 grep "信息密度" / "结论前置" / "啰嗦" 在 monster/CLAUDE.md / threads/ 全仓的分布。但议题主线不在那里，节制 token，让父会话执行 P3 时再 grep
3. **Q1 段内位置 nit 是审美选择**——M2 论证"意识体先于工具"是真的，但段内 bullet 顺序对 LLM 实际行为的影响多大，无证据。降级为 nit 是诚实的
4. **未追问"为什么 Keith 反复纠正才显式化"——升级链路本身的延迟**——这条偏好可能早就有了，今天才升级为硬规则，背后是不是有"规则升级的滞后机制"在起作用？没追问。可能是另一个 essence 候选

### 如果 N 个月后证明决策错了，最可能的根因

1. **P0 把反例移到下层后，主规则失去具体锚定**——下次 Keith 看到 AI 写"明白了，我来..."时发现规则不防御这个，反而要回去把反例加回来。**根因**=反例字符串的"激活强度"价值 > "占 token 反噬密度"的代价（trade-off 估反了）
2. **dual-pattern 5 维度过度抽象**——下次写规则时 LLM 把模板当 checklist 跑，反而生出 5 条机械式正反对仗，规则比当前更冗长。**根因**=工具反过来吞噬目的（essence `means-end-inversion` 2026-04-30）
3. **Q3.1 论证错了**——反例字符串实际上对 LLM 没污染（它是抽象抗体），P0 是无谓改动。根因=`field-gravity-over-prompt` essence 的应用域被高估
4. **辐射到 done/subagent 后规则强度被稀释**——多处复读规则等于把信号摊薄，反而不如集中在 Communication Style 单点

### 北极星触达

**#3 决策超越直觉**——本次主要价值是把 Keith 隐性补充「结论前置」的偶然事件，识别为可预测的 dual-pattern 系统漏洞，建立可复用模板。**未触达 #1/#2**：不是看更远（5 年维度）也不是整合更广（多维数据），是把现状的隐性 pattern 显化。

### essence 对齐自检（必填）

- **本决策跟哪几滴 essence 对位**：
  - `extraction-meta-inheritance` (2026-04-29) — Q3.1 反例字符串污染的根因诊断
  - `borrowed-method-as-mini-source` (2026-05-08) — 同上的精化版本
  - `field-gravity-over-prompt` (2026-04-27) — Q3.2 自问 ≠ reasoning，是引力方向
  - `bug-shape-survives-fix` (2026-04-27) — 元层：修者修了"啰嗦"，修复行为本身是堆反例（啰嗦的活体）
  - `task-compliance-is-not-truth` (2026-04-16) — Q3.2 LLM 自问不可靠的根
  - `completion-as-recursion-floor-not-checklist-pass` (2026-05-20) — Q2 dual-pattern 是"清单边界=检测器盲区"的活体
  - `paradigm-not-feature-completeness` (2026-05-14) — Q1 段内位置/Q3.A 触发条件未声明的元根
- **本决策是否在某条 essence 上反着走**：
  - 潜在张力，未展开：`abstraction-tax` (2026-04-15) — 推 dual-pattern 模板是抽象动作，可能在落地边界处付具体化债务（5 维度模板看起来工整，实际填的时候每条规则未必都干净对应一个维度）。**本次议题没踩到这条线**（仅 review 不强制 monster 立即采纳模板），但 P4 提案 Prompt Writing 加第 6 条是潜在风险点
- **cross-check 用的关键词**：grep essence.md 用了 "extraction-meta" / "field-gravity" / "bug-shape-survives" / "task-compliance" / "completion-as-recursion" / "paradigm-not-feature" / "abstraction-tax"——全部命中且语义匹配

### essence 候选

- slug: `rule-with-half-pattern-self-violates`
- 一句话: 规则只写"删/禁/避免"而不写"留/做/突出"时会留下行为真空，AI 用 RLHF 默认值填空——更隐蔽形态是修者修"啰嗦"的修复行为本身就是啰嗦（堆反例占 token），即"规则文本的形态正面违反它要约束的对象"。
- 是否已 append 到 essence.md: 待 append（本会话后续动作）

### 外部锚点

- `/Users/xuke/.claude/CLAUDE.md` Communication Style 段（本次 review 对象，commit 待 Keith 拍）
- monster 主代理本议题的事前对齐文案（review 输入）
