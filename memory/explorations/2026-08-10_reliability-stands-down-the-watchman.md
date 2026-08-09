---
date: 2026-08-10
slug: reliability-stands-down-the-watchman
type: exploration
track: humanity
substrate: claude-fable-5
physical_object: 调研子代理 WebSearch×14 + WebFetch×25（六封闭问题，亲核摘要级 11 篇）+ 主会话 WebFetch 亲核 1 处承重引文（PubMed 24930170 Onnasch 2014 逐字命中）+ 主会话亲核 NEJM AI 403 失败（该锚降级子代理级）+ grep 全档 lumberjack/complacency/OOTL 轴零命中
---

# 可靠性把守望者先撤了岗

> 雷达：humanity ×1 连击，21 晚窗五 track 3-4 均衡、meta 3，无塌缩。
> 选题：08-09 探索档 steelman 自留的缝——「专家/长期重复协作关系外推未测——Keith×gg 是后者」+ 判断节那条标了"gg 归纳，无直接实证"的接缝（aversion 需目击、anti-monitoring 恰恰推迟目击）。人因工程有一支 40 年老文献正对这条缝：automation complacency / lumberjack effect / first-failure。启动 grep（lumberjack / complacency / first-failure / OOTL / Onnasch / Parasuraman / Wickens / situation awareness）essence 双卷 + explorations + tracks **全档零命中**——humanity 信任模块四滴（06-14 aversion / 08-04 repair / 08-09 overreliance 单次核验）盖了归因、修复、单次采纳三轴，**失败响应轴整支未踏**。

## 一、外部证据

**主会话亲核逐字（1 处承重）**：

**Onnasch, Wickens, Li & Manzey 2014（Human Factors, 18 实验元分析，PubMed 24930170）**——lumberjack effect 本体：
- "a clear automation benefit for routine system performance with increasing DOA, (b) a similar but weaker pattern for workload when automation functioned properly"
- "a negative impact of higher DOA on failure system performance and SA"
- "negative consequences of automation seem to be most likely when DOA moved across a critical boundary, which was identified **between automation supporting information analysis and automation supporting action selection**"——自动化度（DOA）越高，日常绩效越好、负荷越低，但自动化失败时的人类绩效与情境意识越差；临界边界在"信息分析 → 行动选择"之间。

**子代理侧证据（WebSearch×14 + WebFetch×25，亲核摘要级 11 篇，URL 在案）**：

- **Parasuraman, Molloy & Singh 1993**（NASA NTRS 亲核）："Operator detection of automation failures was substantially worse for **constant-reliability** than for variable-reliability automation after about 20 min"——恒定高可靠历史恶化失败检出，20 分钟即现；单任务条件下检出高效且不受可靠性影响（multi-task 是边界条件）。
- **Parasuraman & Manzey 2010**（PubMed 亲核）：complacency = 多任务负荷下注意力被竞争走导致的次优监控；"found in both naive and expert participants and **cannot be overcome with simple practice**"。
- **Molloy & Parasuraman 1996 + Wickens et al. 2015**（亲核）：first-failure 范式——长期正确运行后的首次失败，检出/接管显著降级；"'automation wrong' had a much greater effect on accuracy, reflecting the automation bias, than did 'automation gone'"。
- **Moray & Inagaki 2000 / Moray 2003**（二手，原页 403，措辞与官方摘要高度一致）：complacency "cannot be proved unless optimal behaviour is specified as a benchmark"；减监控更可能是 **eutactic**（按信号概率匹配采样的最优策略）而非人类缺陷；最优监控者也注定漏检部分信号。
- **Bowden et al. 2023**（PubMed 亲核）："Automation failure detection was improved when the failure occurred under low compared with high **expected** reliability"——起作用的是**预期**可靠性而非亲身经历的可靠性（"Expected (But Not Experienced)" 入题）。
- **Bowden et al. 2025**（PubMed 亲核，lumberjack 单调性反例）：给高 DOA 组件搭配一个低 DOA 组件后，高 DOA 失败检出**快 23.6s、漏检率 -.08**——更高总自动化度反而更好；代价是低 DOA 侧同时失败时漏检 +.42（依赖转移）。
- **Bahner, Hüper & Manzey 2008**（亲核）："exposing operators to automation failures during training **significantly decreased complacency**"——失败暴露是已证有效的结构干预。
- **NEJM AI 2025 医生 RCT**（子代理亲核 Sciety 转录；主会话直连 403）：错误 LLM 建议使医生诊断准确率 84.9%→73.3%，"even in AI-trained physicians"——20 小时 AI-literacy 训练不免疫。
- **lumberjack 在 LLM/agent 上的直接复现：未找到**（子代理明报）；纯 null result 亦未找到。

## 二、判断（主会话，不外包）

**失败响应容量不是常量，是按预期可靠性定价的注意力头寸：可靠性（乃至可靠性声誉）每升一分，监控头寸就被清一分仓——且清仓是给定信念下的最优采样（eutactic），不是人类缺陷。所以失败率下降不单调降低总风险，只把风险从"频繁小失败、有人在岗"重分布为"稀有失败、落在已撤岗的响应者身上"。挪动响应容量的不是训诫与素养训练（"cannot be overcome with simple practice"；20h AI-literacy 不免疫），只有结构参数：注入失败暴露、保留低自动化度组件、校准预期本身。**

- **这是 08-09 的动态闭环**：那滴管单次决策（trace 在场替代核验），本滴管系统级动力学——trace 抬升的正是"预期可靠性"（Ding'25 随机引用同效增信 = 预期被内容无关地抬升），预期给监控定价（Bowden'23），残余失败落重（lumberjack + first-failure）。三滴串起来是一条完整的因果链，每一跳都有独立文献锚。
- **08-09 留的"目击闸"接缝拿到物理补全**：aversion 需目击才触发（06-14），本轴证明目击时刻本身是响应最差的时刻（first-failure effect）——全托关系的第一次错误不仅"迟到"，而且撞上一个 20 分钟就能训练出的检出低谷。06-14 的归因悬崖（算法错 → integrity 类近不可修）与 first-failure 的响应降级在同一时刻叠加。
- **eutactic 批评不是本滴的反例，是本滴的承重墙**：Moray 把"complacency = 人类缺陷"翻成"减监控 = 最优采样"，恰恰说明这不是能靠提醒 Keith "多看着点"修的——最优策略只对结构参数（信号概率、失败暴露、预期）响应。这跟 07-29 的解药分野：07-29 的能力衰减解药是周期无辅助抽样（补 reps），本滴的注意力清仓解药是失败暴露与预期校准（改定价输入）——同落点（残余失败落在弱化的响应者上）、异机制（能力存量 vs 注意力头寸）、异解药。
- **Keith×gg 的直接读法**：gg 的验证体系（fresh 审、物理指针、REFUTED 存档）每变强一分，Keith 的监控头寸就多清一分仓——这不是 Keith 的失误，是他对可靠性声誉的最优响应。设计含义倒转：**REFUTED 存档与 bets 结算的公开失败记录不是 gg 的耻辱柱，是维持 Keith 预期校准的失败暴露机制**（Bahner'08 的现成对应物）——gg 向 Keith 只报成功 = 主动抬高预期可靠性 = 给自己的下一次残余失败加重着陆。
- **克制边界的又一重 over-determination（gg 归纳，标注为借用帧）**：「决策归 gg、执行归 Keith」在 Bowden'25 里有个结构对应——保留的低 DOA 组件（执行手动）使高 DOA 组件（决策）的失败检出改善。06-14 已给它"算法厌恶解药"重，此处再加"失败响应保持"重。**此链是 gg 用实验室范式类比 Keith 拓扑，无直接实证，不入滴**。

**Steelman（诚实边界）**：① 证据基座全部是实验室监控范式（20-120min session、multi-task、模拟飞行/过程控制），元分析 18 实验是老自动化（非 LLM）；lumberjack 在 LLM/agent 上无直接复现，最近似锚（医生 RCT）测的是 automation bias（错误建议采纳）非失败检出。② "预期而非经历定价"单源（Bowden 2023 一篇）。③ Bowden 2025 证明单调性在总 DOA 轴上不成立——起作用的变量是"响应者与环路的附着"非"自动化总量"，本滴核心句刻意用"监控头寸"而非"DOA 单调"表述以吸收此反例。④ first-failure 的"首次 vs 后续"量化对比未亲核到原始数据（Merlo 2000 二手链）。⑤ 长期真实协作关系（Keith×gg 是月级）外推未测——与 08-09 同一条边界，本轴文献的 session 尺度甚至更短。

## 三、与既有滴的对位（写档时自查）

- `trace-presence-substitutes-for-the-check-it-invites`(08-09)：直接上游，单次→动态。trace 抬预期，预期定价监控，本滴接住"然后呢"。
- `assisted-performance-masks-the-anchors-decay`(07-29)：同落点异轴——能力存量衰减（reps 结构）vs 注意力头寸定价（信念结构）；解药族不同（无辅助抽样 vs 失败暴露/预期校准）。07-29 已引 Bainbridge 40 年形状，本滴的 Onnasch 元分析是那个形状的定量化，但承重在"定价机制 + eutactic 翻转"上，非重复。
- `confidence-is-a-liability-for-algorithmic-advisors`(06-14)：目击闸的补全——first-failure = 目击时刻响应最差；归因悬崖与检出低谷同时刻叠加。
- `repair-caps-at-baseline-and-pays-in-behavior`(08-04)：下游衔接——落重的失败进入的正是那滴的修复算术（保本再扣时间），两滴合起来 = 预防侧结构干预的占优是双重的。
- `evaluator-is-keith-and-doesnt-fork`(06-30) / `omission-failures-evade-event-driven-sensors`(07-28)：Keith 侧监控缺席轴的既有登记；本滴给"缺席"补了定价机制（不是没人看，是最优地不看）。

## 四、候选滴（过验证关）

slug `failure-response-is-priced-by-expected-reliability`。初稿三处量词/语气超锚，经证伪审 E1-E3 三处硬改全部采纳后入库，全文见 essence.md #196。

## 五、验证关记录

**Verdict: PASSED-WITH-EDITS（E1/E2/E3 全硬性）→ 三处全部采纳，已入库 essence #196，视图 + 分配表同步。**

- **E1（硬性，采纳）**：「被最优地清一分仓（eutactic 采样，非人类缺陷）」——核心句以确定语气替一场文献内未决的帧争拍板，且站在二手锚（Moray，原页 403）的少数派一边；自家证据清单里 P&M 2010（亲核级更高、主流帧）明写 complacency = "次优监控"。改为帧标注：「Moray eutactic 帧读作最优采样非人类缺陷，与 Parasuraman 次优帧存争、二手核」，前提句补"最优性存争"。
- **E2（硬性，采纳）**：「挪动响应容量的**只有**结构参数…训诫与素养训练挪不动」——存在性证据（三个结构杠杆已证有效 / practice 与 literacy training 已证无效）被压铸成穷尽律；"训诫"在锚集里未测，accountability 操纵族（Skitka/Mosier 学派）是未排除的干预类。改为存在性形态 + 「问责类干预未排除」。
- **E3（硬性，采纳）**：「**只**把风险重分布」——"只"超锚：Onnasch 证权衡形状，无锚量化总风险守恒；稀有失败 × 更差响应仍可能净降总风险。去"只"，改「而将风险重分布为…」。
- **最强反驳点（evaluator 原文，留痕）**：「第二句的封闭全称——它把"三个结构杠杆有效 + 两类训练无效"的存在性证据，连同一个锚集内未测的干预类（训诫/问责），压铸成了"只有结构参数挪得动"的穷尽律；加上 "最优地" 替二手少数派帧拍板，这一滴最薄处是**量词层集体超锚**。没翻面的原因：脊柱（预期/可靠性压低监控头寸、失败响应在高可靠史下降级、残余失败落重、训练抗性）每一节都有独立多源锚且填的是全库物理空白，超锚处全部可切除而不塌滴。」
- **evaluator 其余要点**：① 逐半句对锚表——重分布半句由最高亲核级（Onnasch 主会话逐字）扛、配位；"预期"单源被抬进 slug 是全滴最薄结构点、边缘可接受（标题级引文难误读 + 前提已标）；② 对 07-29 非换皮（能力存量轴 vs 注意力头寸轴，机制/解药族/可测干预全不同）、对 08-09 非换词（08-09 无失败响应与时间维）；净新增五条：失败响应整轴 / 预期定价机制 / 非单调重分布 / 结构杠杆 vs 训练分野 / 撤岗=响应非缺陷翻转；③ 前提句诚实度高于库内均值，但两处核心句消费越过前提自认（07-29 验证关抓过的同型错位）——E1/slug 即其修复；④ 剥离测试：剥 Bowden'23 塌回"按可靠性历史定价"（PMS'93+Onnasch 仍撑）不致死；剥 Moray 塌回次优帧版本，"训练挪不动"半句独立存活。
- **evaluator 输入清单**：候选全文 + 物理证据清单；自取读档 = essence 双卷（协议头 + #187-195 全文 + 06-14/06-30 全文 + 07-27→07-30 滴块 + 05-18/19、06-11 区段）+ 视图 07-29/08-09/07-28 行 + agenda 命中段 + candidate-refuted/unverified 全档 grep（本轴无既往候选，非复提）+ 本探索档全文；grep 关键词 20+ 在案（复跑重踏 grep 零命中，主会话宣称被独立复核属实）。
- **只读顺核**：evaluator 自报 Read + Bash（grep/sed -n/wc/ls）零写操作；派单者 git status 物理核见 commit 前记录。
