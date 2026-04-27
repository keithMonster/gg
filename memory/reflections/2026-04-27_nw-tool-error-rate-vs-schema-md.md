---
date: 2026-04-27
slug: nw-tool-error-rate-vs-schema-md
summoner: cc-space
northstar_reach: "#3 决策超越直觉"
status: substantive-decision
---

# Reflection: NW 修复深度阶梯末段 — A vs B 优先级

## 核心假设

1. CLAUDE.md「核心指标」段对工具报错率的"采集方式 = nw_prepare.py 自动统计"声明，等价于一份契约——代码端必须实现，否则下游消费者（含未来 Claude）会被误导。
2. INPUT_SCHEMA_VERSION 当前只有 v1，没有 ≥2 次 schema 漂移事故记录——B 不满足 NW CLAUDE.md §禁伪 n≥k 条款的"门槛触发"条件。
3. Keith 短期（1-2 周）不会重构 NW 指标体系——这条假设我没物理核验，只是基于"4-21 二轮终审刚收口"推断。

## 可能出错的地方

最大风险点是假设 3——如果 Keith 已计划重构指标段而我不知情，A 的 5-10 行采集代码可能白写。概率我估 15-20%（Keith 通常会在 thread 或 essence 留信号，但未必走过我的视野）。已在 trade-off 段显式让 Keith 反驳。

## 本次哪里思考得不够

- 没读 nw_prepare.py 看告示牌方案的实现位置——只信用户 prompt 描述。如果告示牌写在 prompt 而非装配数据里，"拆告示牌"这个动作的归属可能不在 A 的改动范围内。
- 没核验 nightly_report.py 是否已经在某处统计了 is_error——如果已经统计但只是没冒泡到 prepare_daily，那 A 的真实改动只是 1 行管道修复，不是 5-10 行采集。这会改变两者改动量级对比但不改变结论方向。

## 如果 N 个月后证明决策错了，最可能的根因

最可能根因：低估了 B 的"复利价值"——schema 漂移这类 bug 是低频但定位贵的（远超 30 分钟阈值的潜质），等到第 2 次发生时再做 SCHEMA.md，前一次已经付了高昂的 debug 代价。tripwire 方案的盲点在"tripwire 触发后是否真的会被处理"——如果 tripwire 触发后被 Claude 当成可忽略的 warning 滑过去（参考"告示牌结疤"模式的同源失败），B 的延迟就变成纯损失。

## 北极星触达

#3 决策超越直觉。本议题的"凭直觉答"很可能是"两个都做"或"先做小的 A 再做 B"——通过 essence 里 `premature-abstraction-tripwire` 和 NW CLAUDE.md §禁伪 n≥k 两条结晶硬约束，把 B 推迟到 tripwire 触发后才做，是反直觉但有原则依据的判断。

## essence 候选（可选）

无新候选。本轮判断完全在既有 essence（`bug-shape-survives-fix` / `premature-abstraction-tripwire` / `field-gravity-over-prompt` 的同源——契约-实现错位）的覆盖内，没逼近新东西。

## 外部锚点（可选）

- `~/githubProject/cc-space/harness-engineering/CLAUDE.md` § 核心指标（被违反的契约源）
- `~/githubProject/cc-space/harness-engineering/lib/transcript.py` `analyze()` 函数（A 改动位置）
- `~/githubProject/cc-space/harness-engineering/scripts/nw_prepare.py` INPUT_SCHEMA_VERSION 常量（B 影响位置）
- `~/githubProject/cc-space/threads/night-watch.md` ← NW 主体协作叙事
