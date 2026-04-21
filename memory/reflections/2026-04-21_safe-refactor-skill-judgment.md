---
date: 2026-04-21
slug: safe-refactor-skill-judgment
summoner: cg-proxy CC 主会话
northstar_reach: #3 决策超越直觉
status: substantive-decision
---

# Reflection: safe-refactor skill 抽不抽

## 装配

- `reasoning_modules.md` ← M7 Cynefin（路由到 complicated）+ M2 Pre-Mortem（方向 A 失败模式 3 条）+ M5 Red Team（挑战"不做"立场）
- `tools/solution-space.md` ← 父会话倾向"不做"，先验锁定信号，强制展开 ≥2 方向（做 / 不做 / 等信号+tripwire）
- `tools/decision-output.md` ← 中等决策，6 字段涌现
- `personas/{radical,conservative}.md` ← 简式对撞一轮（保守派胜，理由：`ghost-rules` essence 比 `self-as-first-user` 更对口）

未装 `constitution-audit`——触达 OCCAM 显而易见，不需要系统化自审。未装 `tracks/cc.md`——essence 里的 ghost-rules / self-as-first-user 已给足先验。

## 判断

触达北极星 #3（决策超越直觉）：父会话直觉（走得顺 → 想固化）与纪律（项目 CLAUDE.md "三条相似的线"红线）冲突，决策是**听纪律，不听直觉**。结论：不抽 skill，落 15 行 skill-notes 当 tripwire，第三次实例触发时再回溯抽。置信度 4/5（扣 1 分因未物理验证 search-skill 对 "refactor" 的召回质量）。

## 元自省

装配质量 OK——双人格对撞一轮就定调（保守派借 `ghost-rules` 的打法干净利落），没有拖泥带水走完整 persona-debate 流程，符合"装配数量是涌现"。一个可改进点：最初没立刻识别父会话 4 条顾虑的第 2 条（"LLM 能从头推演"）其实就是核心论据——我是 solution-space 展开后才反推回来。下次见到父会话已列顾虑，应先扫一遍哪条是**隐藏的核心论据**，再决定装配。

## essence 候选（如有）

- slug: `premature-abstraction-tripwire`
- 一句话: 过早抽象的对症方案不是"抽"或"不抽"的二分，而是留一个轻量 tripwire（触发器 + 红旗 + 物理锚点，不含流程），把决定权交给"第 N 次场景是否真的出现"。
- 是否已 append 到 essence.md: Y

## 外部锚点（如有）

- cg-proxy commit `fbe63e3` ← 本次重构的物理锚点（父会话侧的决策底稿）
- 父会话 CC 对话本身 ← 本决策的完整对话叙事，不在 gg 侧归档
