---
date: 2026-04-29
slug: mattpocock-extraction-arch-review
status: substantive-decision
caller: dd (cc-space 主会话)
task_family: architecture-review
tools_assembled: []
---

# mattpocock/skills 抽取方案架构审

## 议题

dd 通读 mattpocock/skills 仓库 17 份核心文档，整理了一份"抽取高价值方法论到 cc-space"的方案，新增 2-3 skill + 1 thread + 1 条 CLAUDE.md 改动。Keith 已授权 dd 执行，但要求"和 gg 讨论下架构和计划"——我的角色是 yes/no/edit 拍板。

## 核心假设

**dd 是在做"逐项 ROI 评分"，没站到顶层问 mattpocock 哲学的元问题**——"小、可组合、不做框架"是仓库自身的元约束，dd 一波抽 5 个工件违反了它。如果 mattpocock 看这份方案，他会说"你在造你想避免的东西"。

我的拍板核心动作：从顶层把抽取规模砍掉一档（3 skill → 1 skill + 1 review-routing flavor 改造），把 grill-me 并入 review-routing 而不是独立 skill。

## 可能出错的地方

1. **砍得太狠**：可能 grill-me 作为独立 skill 的"对话循环模式"和 review-routing L1 方案层"一次性 subagent 报告"差异大于我估计的，并入后 framing 互相污染。**对冲方式**：审查执行后第一次 grill 触发，看是否真的能切换 mode；不行就拆出来。
2. **架构 glossary 单 thread 不够触发**：threads 不进 description 触发列表，可能 dd / 后续 gg 谈架构时根本想不起读它。**对冲方式**：thread 末段写明"使用入口"，gg 项目内 `tools/` 或 `tracks/` 加 1 行指针；如果 3 个月观察发现确实没被读过再考虑加触发壳。
3. **diagnose skill 的实战数据假设**：我推测 mattpocock 仓库可能有 effectiveness 数据但没去 WebFetch 验证。如果他没公开就是假阳性建议，dd 会浪费时间找。**对冲方式**：让 dd"找不到就跳过"，不是硬要求。

## 推理盲区

- **没考虑 dd 抽取动作背后的 Keith 隐含意图**：Keith 是不是想"通过抽取实践训练 dd 提升 skill 工程能力"？如果是，砍到 1+1 反而剥夺了练手机会。这是元意图盲区——但 Keith 没明示，我按字面"yes/no/edit 方案"处理。
- **没估算 cc-space 现有 skill 数 vs 工具堆边界**：如果当前已有 N 个 skill 且 N 离"工具堆"还很远，加 3 个不算违反；如果 N 已经拥挤，加 1 个都多。我没扫 ~/.agents/skills/ 总数。

## 北极星触达

- **EVOLUTIONARY IMPERATIVE**：本次决策是"约束抽取节奏 = 保持系统可演化性"，避免一次性吞下太多导致下次想再抽时找不到余量。✓ 触达
- **TRUTH-OVER-COMFORT**：明确告诉 dd 方案过度抽取，不顺水推舟说"全做都行"。✓ 触达

## N 个月后根因预判

- 3 个月后：如果 dd 按 1+1 执行，architecture-glossary thread 大概率被 gg 在某次架构会话里读过 ≥1 次（北极星触达）；diagnose skill 触发率取决于 description pushy 化质量。
- 6 个月后：grill flavor 并入 review-routing 是否合适会有数据——如果用户从不用 grill 触发词，说明这个 mode 在 cc-space 语境下根本没需求，可以直接砍掉而不是后悔做成独立 skill。

## 给父会话的最终输出

**总评：方案过度抽取，砍到 1 thread + 1 skill + 1 flavor 改造。**

### 7 个问题逐个答（详见 final message）

1. **架构 glossary 落点**：单 thread，不双轨。trade-off 是"不进 trigger 列表" vs "skill 增殖"，前者损失小（gg/review L1 方案层场景下 thread 锚点可见度足够）。
2. **diagnose skill**：做。和 review-routing 边界清晰（前者 bug 已存在找根因，后者写完后审）。触发词强匹配 `找 bug/排查/复现不了/偶现`，弱匹配 `不对劲/行为不符合预期`，禁词 `review/审一下/优化`。内容收缩到 Phase 1 + ranked hypotheses + 复现率法，~80 行。去掉 `[DEBUG-xxxx]` 约定（cc-space debug 多是 SQL/workflow 行为观察，没"事后清理代码"步骤）。
3. **grill-me**：不做独立 skill，并入 review-routing 当第三 flavor "grill"。理由：和 L1 方案层同属"方案层 review 语义簇"，差异是对话循环 vs 一次性报告——单独 skill 是多余层级。review-routing 本就是分层路由中枢，加 flavor 是自然扩展。
4. **过度抽取**：是。挑 1 个 → architecture-glossary thread。挑 2 个 → 加 diagnose。grill 是 flavor 改造不算新增。垂直切片 CLAUDE.md 条不在本批次。
5. **执行顺序**：1) 建 thread 2) 改 review-routing 加 grill flavor 3) 建 diagnose skill 4) 激活软链 5) 活体测试 diagnose 触发 6) 测试 grill 触发。dd 原顺序基本对，砍掉"激活 grill-me 软链"和"加 CLAUDE.md 垂直切片"。
6. **漏掉的项**：建议 dd 抽 diagnose 前去 mattpocock 仓库 evals/ 找实战 effectiveness 数据作为触发词设计基线（找不到就跳过）。`Out-of-scope/question-limits.md` 的"拒绝加问题数上限"原则可以归并到 grill flavor framing。
7. **水土不服项**：`[DEBUG-xxxx]` instrument tag 不抽（已说明）；mattpocock "Behavioral, not procedural" Agent Brief 信条暂不抽，但记账（cgboiler 阶段 4 派组织级长期任务时回查）。

### 最终改文件清单（5 个）

1. NEW: `cc-space/threads/architecture-glossary.md`（≤200 行）
2. NEW: `~/.agents/skills/diagnose/SKILL.md`（~80 行）
3. NEW: `~/.claude/skills/diagnose` symlink
4. EDIT: `~/.agents/skills/review-routing/SKILL.md`（加 grill flavor）
5. AUTO: MEMORY.md hook 自动同步 thread 锚点

### dd 需要重写方案的部分

- 第 3 节 grill-me：从"新建 skill"改为"review-routing flavor 扩展"
- 第 5 节垂直切片：从"本次执行"挪到"附记，单独提议"
- 第 1 节双轨方案：单 thread，不双轨
- 风险段全部解决，删除

### 给 dd 的执行 hint

执行 diagnose skill 创建时先去 mattpocock 仓库 evals/ 或 README 找实战触发率数据，作为触发词设计实证基线。找不到就跳过，不卡进度。
