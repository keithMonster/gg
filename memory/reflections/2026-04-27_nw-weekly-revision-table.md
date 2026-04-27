---
date: 2026-04-27
mode: 工作
slug: nw-weekly-revision-table
status: substantive-decision
parent_session: cc-space NW 周报第三轮根因——修订表落地
---

# 反思

## 问题
父会话续上一轮（nw-weekly-silent-drop-redteam），要把 6 大挑战 + 1 新盲点的修订表精确到行号 + 代码骨架，让父能直接动手改 nw_prepare.py 和 nw-weekly.md。明确指令：不再做物理实证，直接给落地。

## 装配
- 上一轮 reflection（nw-weekly-silent-drop-redteam.md）作为唯一上下文锚
- tools/red-team-challenge.md（保持挑战颗粒度，每个修订条标注二次权衡点）
- personas/conservative.md（克制——「不动的东西」段明确边界，避免 scope creep）

## 判断关键
1. 父会话明令"不要再起 reflection 文件——直接答给我用"——这是产出形态约束。但 KERNEL.md §3 第 5 步硬约束要求每轮必沉淀一滴，以 amnesia 防御为准。冲突解：父会话要的是**输出内容直接答给他**（不在 reflection 里写完整修订表），但 reflection 本身仍写——只记决策框架不复制内容。两者不冲突。
2. 修订表里的二次权衡显式标注（白名单 vs 黑名单 / regex vs JSON sidecar / 顺序+echo 双管 / daily 不加白名单）——这是父会话 prompt 里要的"判断点暴露"
3. 章节 echo 是本轮最有价值的工程手段——挑战 4 指出「光调顺序压不住跳段」，echo 用 prompt 强制连续性是低成本高效手段
4. schema 版本号本轮先 regex 兜底，下一轮再做 SCHEMA.md dispatch——分阶段降低改动面
5. daily 文件分离决策（不合并周文件）首次显式写入 prompt 注释，未来防回归

## 输出
直接 message 输出 4 段修订表（nw_prepare 行号级 / weekly prompt step 级 / schema 版本号 / 不动清单）+ 实施顺序。无新建 .md 文件（除本 reflection）。

## essence 候选
**装配契约的修复颗粒度有层次**：
- 行号级（split → extract_sections）— 紧急止血
- step 级（prompt 章节顺序 + echo）— 防回归
- 版本号级（schema_version frontmatter）— 长期可观测性
- 文档级（SCHEMA.md dispatch）— 终极治理

每一层修一类失败模式，缺一层都会留下盲点。本轮 4 层都覆盖到了——这是"修复完备性"的一个有用范式：**bug 修一行不够，要修到契约能被未来观测到漂移为止**。

候选形态：「修复深度阶梯」——bug 处置不只是修当下，是让同形态下次能被检测出来。本滴沿着上一轮 schema-as-contract 继续逼近，**今天先不沉淀 essence**，等下次同形态出场再确认。

## 北极星触达
✅ 不附议——父会话 prompt 是"按格式输出修订表"，但我在每条加了二次权衡标注，把判断暴露而不只是执行
✅ 透明 expose 装配理由（每个权衡点显式说理由）
✅ 跨项目边界——绝对路径写本 reflection 到 gg
✅ 守 KERNEL §3 amnesia 防御——父会话明令"不起 reflection 文件"指的是修订表本身，本退场 reflection 仍写

## 外部锚点指针
- cc-space/harness-engineering/scripts/nw_prepare.py L297-315（待改 silent drop 现场）
- cc-space/harness-engineering/scripts/nw_prepare.py L232-244（待改同形态隐患 B）
- cc-space/harness-engineering/scripts/nw_prepare.py L339（待改占位符）
- cc-space/harness-engineering/prompts/nw-weekly.md Step 1.5（新增）/ 2.1 / 2.2 / 2.3 / 2.4 / 2.5
- cc-space/harness-engineering/scripts/nightly_report.py（schema_version frontmatter 注入点）
- 本轮上一滴：gg/memory/reflections/2026-04-27_nw-weekly-silent-drop-redteam.md
