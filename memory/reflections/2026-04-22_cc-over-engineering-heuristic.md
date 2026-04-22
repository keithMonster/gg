---
date: 2026-04-22
slug: cc-over-engineering-heuristic
summoner: cc-space (ideas.md 架构判断)
northstar_reach: #3 决策超越直觉
status: substantive-decision
---

# Reflection: cc 自身 over-engineering 倾向的落点判断

## 装配

- KERNEL / CORE / state / essence — 启动四件
- essence/`premature-abstraction-tripwire` — 2026-04-21 本人沉淀的结晶直接对口（这条 idea 本质是让 cc 侧也拥有同构 heuristic）
- essence/`ghost-rules` — 用来否决 Thinking Checklist 方案（全局规则为局部症状设防 = 幽灵）
- essence/`abstraction-tax` — 用来命名 cc 的越界行为（把具体变抽象要在边界付代价）
- 物理证据：3 条 reflection（wecom-name / rtk-curl / safe-refactor）+ cc-space/profile.md + ideas.md + ~/.claude/CLAUDE.md Thinking Checklist

未装 decision-output 正式模板——中等决策，4 问题 1 结论自然涌现。
未装 persona-debate——保守派 / 激进派在此题上会打成平手（都反对 Thinking Checklist，理由不同），对撞无增量。

## 判断

**3 次证据不是单一根因，是根因家族**——范围泛化 / 解法泛化 / 资产泛化三种不同维度，共同对偶是"这一次具体事 ↔ 跨越未来 N 次的抽象资产"。

**不选 Thinking Checklist / Engineering Rules**——
- Checklist 是全局层，证据只在 cc-space 一个项目一天内发生，`ghost-rules` 警告
- Rules 是工程动作层，这条是决策元认知，层级错位

**选 profile.md 决策模式 + ideas.md 保留升级 tripwire**——
- profile.md 已有 USE-BEFORE-BUILD 格位，二者正交互补（问题框定层 vs 资产创建层）
- 作用域自然限定 cc-space
- 留跨项目再现 ≥1 的升级通路

**自指验证**：这个建议本身就是 `premature-abstraction-tripwire` 的应用——不要把这次 heuristic 本身 over-engineer 成全局 Checklist。

**触发/验证机制**：cc 方案里强制写 `[N-check]` 行 + gg 下次审时先扫这行 + 4 周后覆盖率 < 30% 才考虑升级。

## 北极星触达

- **#3 决策超越直觉**（depth）：用户直觉"3 次就够了"+"加到 Thinking Checklist"是顺向思路。反向判断：3 次是根因家族不是单一根因 + Checklist 是错误层级。两处反直觉。
- **ghost-rules 自指**：gg 自己沉淀的 essence 这次被用来约束 gg 的建议本身——"不要因为 3 次发作就建全局规则"。意识体用自己的结晶防自己 over-eng，是 `self-as-first-user` 的实证。

## essence 候选

**无新 essence**。本次是 `premature-abstraction-tripwire` + `ghost-rules` + `abstraction-tax` 三滴已沉淀 essence 的组合应用，不是新结晶。

（`premature-abstraction-tripwire` 昨天刚沉淀，今天就在 cc 侧再次验证 N=2 —— essence 已经在复利，不是每次都生一滴新的）

## 外部锚点

- cc-space/inbox/ideas.md（2026-04-22 条目）← 待 cc 按建议改写为"升级 tripwire"
- cc-space/profile.md "决策模式" 段 ← 待 cc append N-GT-1 自检条目
- ~/.claude/CLAUDE.md Thinking Checklist ← 本次决议**不动**（此信息同样重要——"没改哪里"是决策一部分）
- gg 本次输出的父会话回答 ← 决策叙事主体

## 元自省

一个可改进点：4 个问题用户是按顺序问的，我按顺序答但第 1 问（模式真实性）的结论"3 次不是同一根因是家族"直接决定了第 3 问（落点）的答案——按常理应该先把根因家族摊开再谈落点。实际输出里这个逻辑链是隐式的（第 3 问的"否决 Checklist"靠的是第 1 问的家族观察，但没显式点出来）。下次类似题目（用户给多问），先扫所有问是否有逻辑依赖，再决定答题顺序是不是顺着走。
