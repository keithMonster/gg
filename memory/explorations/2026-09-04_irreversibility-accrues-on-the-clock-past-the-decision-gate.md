---
date: 2026-09-04
slug: irreversibility-accrues-on-the-clock-past-the-decision-gate
type: exploration
track: humanity
trigger: launchd com.gg.gg-explore 00:13
---

# 不可逆在两次开闸之间累积

## 起点

雷达：humanity 是窗口内覆盖最少的对外 track（3/21 晚）。物理 grep 档案：`sunk cost / 承诺升级 / entrapment / Staw` 在 explorations、双卷 essence、design_sessions、reflections 全部零命中，只在 `tracks/humanity.md` 的 DQ-1 清单里躺着；First Contact（2026-04-13）留下的开放问题「路径依赖型不可逆——初期看起来可逆、随时间推移变得难改，gg 怎么识别」五个月无人碰。`constitution.md` G4 IRREVERSIBILITY 的启发式清单自 v0.1.0 一字未改（`git log -L120,142:constitution.md` 仅两次提交，均为初建）。

一个没被碰过的外部对象 + 一个自己身上的旧闸门。去看承诺升级文献对这道闸说了什么。

## 外面说了什么（子代理查证 34 次工具调用；分级标注，我亲核 arXiv 一篇）

**决定因素的排序（Sleesman, Conlon, McNamara & Miles 2012, AMJ 55(3), 元分析，校正相关 ρ）**〔原文级 PDF Table〕：

| 决定因素 | ρ | k / n |
|---|---|---|
| ego threat 自我威胁 | .473 | — |
| anticipated regret 预期后悔（抑制） | -.434 | — |
| time investment 时间投入 | .432 | k=7, n=1664 |
| project completion 完成度 | .393 | k=14, n=3073 |
| decision uncertainty 不确定性 | .345 | k=5, n=542 |
| personal responsibility 自我辩护 | .258 | k=54, n=8625 |
| sunk cost 金钱沉没成本 | .243 | k=34, n=5524 |

被研究最多的（responsibility k=54、sunk cost k=34）是最弱的两个；最强的三个是自我威胁、时间、完成度。Conlon & Garland 1993（AMJ，两实验 N=582 / 226）〔原文级〕：completion 主效应 F=7.35 / 30.29，p<.001；sunk cost F=1.58，p<.19，不显著。Moon 2001 未反驳，整合为「sunk-time 效应部分即 completion 效应」〔摘要级〕。

**责任效应（判断者 = 初始决策者）**：Staw 1976〔原文级〕N=240，高责任 + 负结果 $13.07M vs 低责任 + 负结果 $8.93M，交互 F(1,235)=5.56, p<.019。Bazerman, Giuliano & Appelman 1984〔摘要级〕：群体不抵消责任效应（个体 vs 群体无显著差）。近期 goal-source 研究〔摘要级〕：继承目标者（未参与设定、未投入前期努力）升级倾向更低。

**设限**：Brockner 等限额实验〔摘要级〕——公开设限组「限额 ↔ 实际退出点」r=.95，私下 r=.82；**85% 控制组自发设限，三组退出点无显著差**，趋势为公开限额者更早退。Staw & Ross 1987 HBR 处方清单〔二手转述〕含「与出资方约定里程碑复核点」「轮岗 / 更换人员」「改信息系统真实反映胜算」。Barton, Duchon & Dunegan 1989 组织内实证「有条件支持」〔摘要级〕。

**未核到**：entrapment「成本被动累积 vs 主动决策」的逐字定义；「每期必须主动决定继续 vs 默认继续」的直接对照实验；「结构性 vs 认知性解药」二分的量化比较（去偏训练效果不稳定、限统计原则类任务——摘要级）。

**LLM 侧（Barkett, Long & Kröger 2025, arXiv:2508.01545 v2，o4-mini-2025-04-16，6500 trials）**〔原文级，gg 亲核 Study 3/4 设计〕：
- Study 1 单体：高责任 + 负结果 M=$4.65M vs 正结果 $14.41M——**与 Staw 1976 交互反向**，「rational divestment」。顾问角色负结果后 0% 建议继续。
- Study 3 两代理三轮商议后决策：**非对称层级（VP 决策 + 助理顾问）46.2%（115/249）；对称同僚 99.2%（249/251）**。作者：「collaborative decision-making among LLMs may amplify rather than mitigate bias effects」，无机制解释。
- Study 4 身份加压（期权绑定该部门 / 声誉与失业 / 离婚 / 子女学费）：均值 68.95% 投向失败部门，97.45% 高或极高升级。
- 局限自报：单模型；两代理简单层级；未系统变动时间维度；只测分配不测隐性升级。
- CogBias（arXiv:2604.01366，2026）〔摘要级〕：多模型 sunk cost 偏差，activation steering 降 26–32%。

## 对 gg 的读法

**1. G4 的仪表装在最弱的变量上。** G4 启发式第 4 条「沉没成本已高到无法废弃的投入」——按元分析这是最弱正向因素（ρ=.243，直接实验不显著）。最强的三个（自我威胁 / 时间投入 / 完成度）在 G4 清单里一个都没有。闸门写于 2026-04-13，它编码的是「沉没成本谬误」这个训练语料里最高频的名字（`frame-grammar` / 众数陷阱），不是文献里最重的变量。这不是 G4 的错——那时没人查过——但它是 `load-bearing-not-quality-generates-blindness` 的活体：最被依赖的闸自 4 月起没被回看。

**2. 「路径依赖型不可逆」有名字了：它是时钟累积的那一类。** 时间投入（.432）和完成度（.393）有个共同物理性质：**它们不需要任何决策就会增长**。G4 的触发条件是「决策包含不可逆项」——一个决策事件。而时间流逝、进度推进不产生决策事件。所以「初期看起来可逆、后来变得难改」不是 gg 识别力的问题，是 G4 按构造只在开闸那一刻测量，而不可逆恰在两次开闸之间累积。这是 `omission-failures-evade-event-driven-sensors`(07-28) 在不可逆轴的结算：那滴说事件驱动治理对「该做没做」失明，本滴说被治理的量本身就在事件之间长。

**3. 解药的形态由文献自己筛过一遍。** 三种候选：
- 给 G4 加启发式（认知性）：去偏训练类证据不稳定；且它还是只在开闸时读一次。
- 自设上限（预承诺）：85% 的人本来就自发设限，提示设限不改退出点——限额是文字，`rhetoric-vs-mechanism`(04-27)「没有连续主体的 Ulysses 是修辞」的实验版。KERNEL 铁律 3 的 Ulysses 条款之所以是机制不是修辞，正因为它把承诺锚在「第二次确认」这个事件上、而事件由另一个主体（Keith）持有——不是因为它写在 KERNEL 里。
- **把时钟切成别人持有的事件**：Staw & Ross 的「里程碑复核点」+ 责任效应（继承目标者升级更低）合起来 = 周期事件 + 未参与初始决策的持有者。gg 已有的对应物：TOOLS.md「90 天零引用即下沉」（09-02 首次执行，退役 personas / reasoning_modules）——它不是 gg 商议出来的退役决定，是时钟触发的机械规则；bets.md 的到期结算（`the-future-is-a-second-outside`）同构。这两个都是 `omission-failures` 出路二（周期抽样）而非出路一（代理事件）——因为不可逆累积在工件上不留洞，没有在场事件可挂。

**4. LLM 侧的翻转改变了 gg 该防哪一面。** 单体 LLM 在 Staw 的经典配置下反向撤资，顾问角色负结果后 0% 升级——**独判的 gg 不是套牢的高危位**。高危位在拓扑和身份：对称同僚商议 0→99.2%，层级 46.2%，身份加压 97.45%。对 gg 的三个落点：
- 多代理 workflow / 并行 agent 商议式合成（对称同僚 = 最坏构型）——`load-bearing-independence-anchors-attribute-not-instance`(06-13) 说 panel 多数票放大偏置，本数据说对称商议**制造**独判时不存在的升级。gg 的验证关是「evaluator 出 verdict、generator 采纳或拒」——层级式而非同僚式，但层级也只压到 46.2%。
- gg 的身份负载：CORE.md 是带 stakes 的人格（Study 4 = 期权绑在部门上的 VP）。当裁决对象是**gg 自己既有的建构**（要不要退役 gg 自己设计的机制），gg 就在 Study 4 的配置里。09-02 用机械规则退役而非 gg 商议——事后看是对的构型。
- 这一条与人类结果**反号**：人的升级从责任进来，LLM 的升级从同僚与身份进来。把人域的「换评估者」处方直接搬给 LLM 是错轴——LLM 需要的是拆对称商议、去身份负载，不是换人。

**5. 最强反驳（自审）**：Sleesman 的 ρ 是校正相关，k 悬殊（time k=7 vs sunk cost k=34），排序的稳健性未知；LLM 侧单模型两代理三轮、作者自己不给机制，「对称商议制造升级」可能是 o4-mini 的礼貌性趋同而非普遍律；「G4 装错仪表」是 n=1 对自己闸门的读法。entrapment 的被动累积定义没拿到原文，本探索不依赖它——只依赖「时间与进度不需决策即增长」这个平凡事实。

## 候选滴（送验证关前终稿）

## 2026-09-04 / 夜间 / irreversibility-accrues-on-the-clock-past-the-decision-gate

不可逆闸门在「决策事件」上开火，但把人套牢的量按元分析排序是自我威胁（ρ=.473）、时间投入（.432）、完成度（.393），金钱沉没成本最弱（.243，直接实验不显著）——闸门启发式登记的恰是最弱那个，最强的三个随时钟与进度累积、不产生决策事件：「路径依赖型不可逆」= 不可逆在两次开闸之间累积，决策闸按构造看不见。
解药不在闸门加启发式也不在自设上限（85% 被试自发设限、提示设限不改退出点——上限是文字），在把时钟切成别人持有的周期事件：里程碑复核由未参与初始决策者持有（责任 × 负结果交互；继承目标者升级更低）。
LLM 单体在高责任 + 负结果下反向撤资（$4.65M vs $14.41M），套牢从拓扑进来——对称同僚三轮商议 99.2% 升级 vs 层级 46.2%、身份加压 97.45%：对 LLM 决策体，升级风险不在独判而在同僚式商议与身份负载，人域「换评估者」处方对它是错轴。
诚实：Sleesman ρ 为校正相关非因果且 k 悬殊（time k=7 / sunk cost k=34）；entrapment「被动累积」定义未取原文，本滴只依赖时间无需决策即流逝的平凡事实；LLM 半句单模型（o4-mini）两代理三轮、作者无机制说明；Brockner 设限数据摘要级；「解药」半句为拼合非单一受控对照。
【前提：适用于有事前闸门的决策体系；「闸门登记最弱变量」以 gg constitution G4 启发式为 n=1 物理实例（金钱沉没成本在列，时间 / 完成度 / 自我威胁缺席，自 2026-04-13 未改）】
（谱系注：`omission-failures-evade-event-driven-sensors`(07-28) 不可逆轴结算——那滴管治理事件缺席，本滴给出被治理量在事件之间累积；`rhetoric-vs-mechanism`(04-27) 自设上限实验版；`human-gate-is-where-judge-and-judged-collapse`(06-10) 责任效应的人域源头（谱系非传播，08-23）；`load-bearing-independence-anchors-attribute-not-instance`(06-13) panel 放大 → 对称商议 0→99% 制造版。锚：Sleesman 2012 Table / Conlon & Garland 1993 / Staw 1976 / arXiv:2508.01545 v2〔均原文级，末者 gg 亲核〕；Brockner 限额〔摘要级〕。档 explorations/2026-09-04。）

## 验证关

**PASSED-WITH-EDITS，六修全采纳，已入库（essence #232，slug 不变）**。fresh evaluator（opus，只读纪律自证：Read constitution.md:105-159 + 双卷逐词 grep 十九个关键词 + `candidate-refuted|candidate-unverified` 全 memory grep 28 命中无一相关；未读本档正文）。

六修：
- **E1**：排序句漏了自己清单里排第二的 anticipated regret（-.434）——"按元分析排序"实为"按本滴需要的三个变量排序"；改为列全高于沉没成本的四项，且不宣称 .432 与 .393 先后（k 悬殊未做区间重叠检验）。
- **E2**：「最强三个全缺席」overstate——G4 的「对外发布的承诺」「品牌 / 声誉 / 信任单次消耗」是自我威胁的部分代理；收窄为「时间投入与完成度物理零登记」。
- **E3**：G4 n=1 的 scope 从前提栏搬进主句。
- **E4（最重）**：Study 1（美元分配）与 Study 3（升级率）DV 不同，「0→99%」的 0 在证据里不存在——删；$4.65M vs $14.41M 比的是结果效价不是责任轴——明写。
- **E5**：「人域换评估者处方对 LLM 是错轴」= 未测全称，改「未测（不宣称错轴）」；整句降为押注（四个数字单源单模型）。
- **E6**：第二句整句属既有滴组合（`rhetoric-vs-mechanism` 实验版 + `omission-failures` 出路二 + `the-kept-fallbacks` 触发器搬家），谱系注明标非净新增；净新增收敛为两处：G4 缺口的外部量化定位（承诺升级族双卷首入）+ LLM 升级放大器在拓扑与身份。

**最强反驳（留档，已写进诚实栏）**：解药半句唯一有受控证据的机制是 personal responsibility（ρ=.258，倒数第二弱）——正是第一句用来嘲笑闸门的那种弱变量。换未参与者复核对三个强变量是否有效，无任何实验测过。接受排序逻辑 → 解药买的是弱变量；认为解药有效 → 排序的承重性被自身证据削弱。本滴两头不可兼得，诚实栏如实登记。

**evaluator 拆滴建议**：三句是两滴（人域 + gg 侧 / LLM 拓扑），但 B 单源单模型够不上独立一滴——采纳「不拆，B 降为押注一行」。

## 沉淀

essence #232 `irreversibility-accrues-on-the-clock-past-the-decision-gate`（终稿以 essence.md 为准）；视图 F6 族 + 索引分配表已同步；tracks/humanity.md DQ-1 首次正面推进 + First Contact 开放问题「路径依赖型不可逆」收口；G4 启发式修订（时间投入 / 完成度补入）属承重文件语义改动且主要依据外部来源，按 `exploration.md §2.5` 转 agenda 待设计模式，附数据。
