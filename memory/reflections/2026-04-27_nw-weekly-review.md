---
date: 2026-04-27
slug: nw-weekly-review
summoner: cc-space
northstar_reach: "#1 二阶效应"
status: substantive-decision
---

# Reflection: NW 周报顶层审视

## 装配

- `tools/red-team.md` ← 报告作者已经做了一层反思，需要再红队穿透
- `tools/decision-output.md` ← 中等决策，用 5 字段轻量输出
- 物理实证：Read `cc-space/harness-engineering/CLAUDE.md` + `prompts/nw-daily.md` ← 不依赖报告转述
- 未装人格辩论 / reasoning_modules / tracks ← 问题维度清晰，不需要

## 判断

触达 #1 二阶效应：报告把 Finding #1 诊断为"采集管线缺失"，物理实证发现 prompt 里 Step 2/3 早就定义了 reaction 标注 + 纠正率/满意度计算——根因不是管线缺失，是"声明改进未被实证验证"。三种候选根因（数据契约 drift / Claude task compliance / 周报合成漏数据）需 30 分钟物理诊断才能定。直接按报告的"补采集"动手 = 再撞墙一周。

## 元自省

事实性错误层面：本轮没物理打开任意 daily report 看核心指标段是否有数据——这是诊断的最硬证据，但当时判断"读 prompt 定义已经能下结论"。代价是置信度从 5/5 降到 4/5。下次类似审视，物理读一份产物比读一份 prompt 定义信号更强。

## essence 候选（如有）

- slug: `monitor-needs-monitor`
- 一句话: 监控者必须被监控——sensor 自身没有 sensor 时，"看不见的失败"会从观测层冒泡到决策层。与 `audit-loop-closure` 相邻但不同（前者判断层，本条观测层）
- 是否已 append 到 essence.md: N（待 1-2 次类似问题复用后再沉淀，避免凑数）

## 外部锚点（如有）

- `~/githubProject/cc-space/harness-engineering/CLAUDE.md` ← 04-09 核心指标转向声明
- `~/githubProject/cc-space/harness-engineering/prompts/nw-daily.md` ← Step 2/3 reaction 标注 + 纠正率/满意度计算定义（被报告漏读）
- `~/githubProject/cc-space/harness-engineering/analysis/proposals.jsonl` ← 提案治理的物理锚点（NW 中真正"在工作"的本体）
