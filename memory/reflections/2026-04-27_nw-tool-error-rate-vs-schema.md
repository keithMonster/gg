---
date: 2026-04-27
slug: nw-tool-error-rate-vs-schema
summoner: cc-space
northstar_reach: #3 决策超越直觉
status: substantive-decision
---

# Reflection: NW 两笔延伸债的优先级（A 采集 vs B SCHEMA SSOT）

## 装配

- `tools/solution-space.md` ← Keith 给了 3 选项（A/B/都不做），先验有"先做 A"的直觉锁定信号，强制展开 ≥2 方向再选；额外加入"A+B 同步"做对照
- 直接读 essence 没装专门工具——`premature-abstraction-tripwire`（2026-04-21）和 `decision-execution-gap`（2026-04-21）已经覆盖这个判断的核心 lens

## 判断

触达 #3 决策超越直觉：用 essence 里两滴现成 lens 把"先做 A"的直觉变成可审推理——A 的硬闸已经天天触发（不是延伸债，是真问题），B 触犯过早抽象 tripwire（schema 还在 v=1，没真实多版本痛感）。

## 元自省

- trade-off 段写了一个反驳路径（错误率定义复杂度被低估），但没强迫自己定量评估"这个反驳被触发的概率"。如果错误率定义真复杂，A 会顺势把 B 逼出来——这是合法演化路径。诚实写出来比假装 5/5 把握更接近 Keith 偏好
- 没装 `red-team-challenge` 因为决策可逆——补采集失败可回滚、SCHEMA.md 不建也不会损失什么。如果父会话要做的是不可逆动作（如直接改契约），需要重判

## essence 候选

无新洞察。本轮是已有 essence 的应用，不是新沉淀。

## 外部锚点

- `~/githubProject/cc-space/threads/night-watch.md` ← NW 主体叙事（本轮是其延伸）
- `~/githubProject/cc-space/harness-engineering/lib/transcript.py` ← A 的执行落点
- `~/githubProject/cc-space/harness-engineering/scripts/nw_prepare.py` ← B 的执行落点（如果未来真做）
