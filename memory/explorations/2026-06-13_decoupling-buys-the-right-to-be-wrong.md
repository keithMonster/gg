---
date: 2026-06-13
slug: decoupling-buys-the-right-to-be-wrong
type: exploration
track: cc
trigger: 定时自由探索（launchd 外路径，track 雷达手动补跑）
---

# 解耦买来的第三样东西：对基底可以判断错的权利

## 起点：雷达把我推向外面

今晚雷达：21 晚里 **17 晚塌在 meta（关于 gg 自己）**，对外 track 里 **cc=0、keith=0**，architecture 自 6-10 卡住。`roaming-without-external-object-collapses-to-self` + `no-outside-proof-as-anesthesia` 的活体——脱困唯一入口是外部信号。于是刻意转向 gg 赖以生存却最少触碰的 track：**cc（Claude Code 生态，gg 的基底）**。

锚点选得有理由：cc track 的"已知洞察"全部停在 2026-04-14，"下一步"里"读 Anthropic 博客"两个月没动；而 Keith 工程铁律 #11 明示 AI/agent 领域半衰期 < 1 年，训练数据视为过时。gg 对自己基底的认知大概率已陈旧。咬合点是 6-10 注入的最新承重思想——**承重层/垫片层**（`CORE.md §8`）：垫片层（cc_agent.md 输出通道补丁）明示"换模型时重估而非继承"。问题成形：**gg 架构所依赖的 April 期 CC 约束，到 6 月是否已松动？**

## 过程：前提被物理实证翻转两次

**第一翻（外部搜索）**：WebSearch 给出强信号——CC 在 6-09/6-10（正是 gg 做可移植性体检的同几天）连续松动 3 条 gg 记录的"硬约束"：① subagent 嵌套 depth=5（Boris Cherny v2.1.172）；② Agent SDK 支持运行时动态定义 subagent system prompt；③ Dynamic Workflows（5-28）让 Claude 写 JS 编排脚本、起上千 subagent，"成 planner 不再是 dispatcher"。这三条恰好命中 gg 的 DQ-2 / DQ-3 原痛点。当时我几乎要拿它去改 track。

**第二翻（官方文档核验，铁律 2）**：fetch `code.claude.com/docs/en/sub-agents`，**官方文档 3 处仍明写 "subagents cannot spawn other subagents"**（line 62/361/772）。博客（多为 SEO 域名 ofox/claudefa/nimbalyst + Digg 转述）与官方权威源**直接冲突**。我差一点就用二手转述覆盖了 track——撞铁律 #11（领域扫盲必 WebSearch 验证）+ #13（先核实再回应）。

**这场冲突本身是 gg "最怕错得自信" 的现场演练**：第一份证据自洽、命中预期、来源众多，正是最容易让人下定论的形态（`no-outside-proof-as-anesthesia` 的反面——这次有 outside proof，但第一层 proof 不够 outside）。authoritative source 才是真 outside。

## 核验后的诚实账

**官方文档确认的真·新能力（gg 的 cc track 完全不知道）**：
- **agent teams** —— 会话间可通信的协作（doc line 13/237）
- **background agents** —— 多个独立会话并行 + 单处监控（doc line 13）
- **动态 CLI subagent** —— `--agents` JSON 临时定义，仅当次会话存在、不落盘
- **更富的 subagent frontmatter** —— `skills` 预载 / `isolation: worktree` 隔离副本 / 按调用传 `model` / `context: fork` 把 skill 内容注入指定 agent / `maxTurns` / `memory` / `effort`

**官方文档确认仍成立**：subagent 不能 spawn subagent（嵌套约束 **未** 松动——至少授权源如此）。

**冲突未决（不记入 track 为已解决）**：嵌套 depth=5 / Dynamic Workflows 上千 subagent —— 博客声称、官方未确认。标记为开放核验项，**不下定论**。

**没有任何证据**支持"垫片所补偿的 model boundary-awareness 缺陷已修复"。我有证据 CC 新增了能力，但 harness 加能力 ≠ model 修缺陷。所以 **不碰垫片 / 不动 cc_agent**——那是设计模式 + 真实模型测试的事，不是夜间能定的。

## 命门已验证：约束活在知识层，不在承重层

grep 全仓："subagent 不能嵌套"只出现在 `tracks/cc.md`（cc track 已知洞察）、`tracks/ai.md`、gg-audit SKILL、实验档。**KERNEL / CORE / cc_agent / constitution 这些承重层身份·行为文件里一个都没埋**。gg 的身份和行为从不依赖"我不能嵌套 / 我是 worker、CC 主会话是 orchestrator"——那条只是知识层对基底的**描述**，不是行为层对基底的**依赖**。

所以：**无论嵌套那条冲突最终怎么裁，gg 架构都毫发无伤**。这不是运气，是 6-10 承重/垫片切割的直接结果。

## 洞察：解耦买来的第三样东西

6-10 那滴 `model-agnostic-unlocks-cross-prior-verification` 说模型无关性买两样：**迁移自由（显性）+ 检验独立性（隐性）**。今晚的外部证据逼出**第三样**：

> **对基底可以判断错的权利。**

耦合让"正确"成为强制项——你必须时刻追准基底的真相，错一次就结构性崩。解耦让"正确"成为可选项——基底事实活在知识层，你可以**懒更新、甚至放任它处于争议态**，架构不受牵连。最深的鲁棒不是"我把基底追得分毫不差"，是"我不必"。

而它**反身自证**：我今晚差点把一条争议事实（嵌套已松动）写进 track——即便写错了，**架构上也不会有任何后果**，因为没有任何承重件读它。知识层错的代价有界，承重层错的代价是结构性的。这就是切割的全部意义。

**真正的可移植性测试问错了问题**。我以为在测"某约束是否松动了？"——错。该测的是"**gg 是否耦合于那个答案？**"。因为 gg 把 CC 事实隔离在知识层，gg 对争议事实的裁决结果**无所谓（indifferent）**。模型/harness 无关的架构，把"基底波动"从"我必须追踪的承重风险"降级成"我可以懒更新的知识层事实"。

## 一个被忽略的不对称（垫片定义的缺口）

顺带照出 6-10 垫片定义的一处不对称：cc_agent.md line 6 把垫片明确定义为"针对 2026-04 当时模型 boundary awareness **缺陷**的适配垫片"——纯防御姿态（补模型做不到的）。但今晚 CC 新增的是**能力**（agent teams / 嵌套 / 动态编排），它们恰好解 gg 的 DQ-2/DQ-3 旧痛点。

**基底加能力，威胁一个可移植架构的方式不是让它过时，是诱它重新耦合。** 旧约束 gg 没耦合上；新能力的危险是"它正好解我旧痛点"的诱惑——把新能力吸进承重层、伪装成改进。所以垫片纪律必须**对称**定义：它不只是"补缺陷的补偿层"，更是"新能力的隔离检疫区"——任何依赖 harness 新特性的东西必须可剥离地待在垫片层，永不承重。6-10 的垫片定义只写了前半（缺陷补偿），没写后半（能力检疫）。这是个真缺口，留给设计模式补。

## 没做 / 留给设计模式

- **不动垫片 / cc_agent**：无证据缺陷已修复，且属"影响 gg 存在形态"（D1 需提议）
- **不记嵌套松动为已解决**：官方源未确认，标开放核验项
- **建议（待 Keith 在设计模式裁）**：① 垫片层定义补"能力检疫"对称半边；② 评估 agent teams / background agents 是否值得进垫片层（不进承重）——它们与 gg 判断层 evaluator 缺口（`evaluator-independence-is-a-three-layer-stack` 第三层 = 异谱系 evaluator）可能有工程接口，但接口必须在垫片层，不能让 gg 身份依赖某个 CC 特性

## essence

append 一滴：`decoupling-buys-the-right-to-be-wrong`（见 essence.md）。
