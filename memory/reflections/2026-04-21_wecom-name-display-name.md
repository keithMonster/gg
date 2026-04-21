---
mode: 工作
slug: 2026-04-21_wecom-name-displayName
summoned_by: cc-space (cg-proxy wecom.consts.ts name 字段语义错位)
decision_archived: no  # 父项目 ADR 归属 cg-proxy / cc-space，非 gg 档案
---

# wecom name/displayName 方案审

## 装配痕迹
- tools/inversion（先想怎么失败——问题框定是否已经偷跑）
- tools/trade-offs（3 候选显式代价）
- essence/invariance-allocation（架构本质 = 分配不变性）
- 物理实证：Read wecom.consts.ts:1-80 / wecom.controller.ts:260-320 → name 实质仅在 department 分支第 275 行被消费，personal 分支用 fromUser；usedAppName 仅回显

## 判断质量
- 父会话把问题框成"name 字段语义错位（32 条 app 统一治理）"
- 代码证据：错位只在 type=department 类（4-5 条），personal 类 name=人名本就正确
- 这个 reframe 是本次决策的真正增量——A1/A2/A3 候选集没错，错在范围

## 核心决议
- **选 A1**（加 displayName，不改 name）
- **但加范围收窄**：interface 注释仅 department 分支写语义警告
- **加对账可见性**：启动日志 dump department app 表，Night Watch 兜底抽查
- 否决对象化（Q3）、否决 A2 局部重命名、Q4（eval 远程 JS）单开 thread

## 北极星触达
- **诚实胜于体贴**：没顺着"32 条统一治理"的框继续答，直接指出问题被泛化了
- **invariance-allocation**：本次的稳定点是 appId，不是 name——这决定了 A3（按 appId 动态查）在一致性维度最干净但运行时贵，而 A1 把不变性锚在"人工维护的 displayName"上，漂移由对账机制兜底

## essence 候选
无新 essence。本次是 invariance-allocation 的直接应用，不是新结晶。

## 外部锚点
- 决策产物在父会话的回答里，cg-proxy / cc-space 侧 ADR 归属父项目
- Q4 的契约问题建议父会话开 `cc-space/threads/wecom-config-contract.md`
