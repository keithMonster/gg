---
date: 2026-08-12
slug: the-cure-was-always-relocation-never-repair
type: exploration
track: ai
substrate: claude-fable-5
physical_object: 调研子代理×2（航空侧 WebSearch×14+WebFetch/下载 19 URL 原始 PDF 级；警报侧 WebSearch×21+WebFetch 12 URL 含 3 篇 arXiv 本地 pdftotext + grep 零命中物理证据）+ 主会话亲核 2 处承重引文（Bliss'95 eutils 逐字 / IFALPA 38% curl+pdftotext 逐字）+ 启动 grep essence 双卷 alarm/TCAS/EGPWS/航空/cry-wolf 轴零命中
---

# 解药从来是搬迁，不是修复

> 雷达：ai ×1 连击，21 晚窗 ai 4 / architecture 4 / cc 3 / humanity 5 / keith 3，无塌缩。续钻不换向：08-10 给了定价机制（监控头寸按预期可靠性清仓、只有结构参数挪得动），08-11 证了 AI control 把人类审计常数化——两滴合起来留下一个自然的收尾问题：**这个问题上唯一被杀过人、付了五十年学费的工程领域（航空），最终长出的存活架构是什么形态**。今晚去问尸检报告。
> 启动 grep：`alarm / cry.?wolf / TCAS / EGPWS / GPWS / 航空 / aviation / autopilot / magenta / alert fatigue`，essence 双卷 + 视图 + 近两夜探索档**全部零命中**（"警报"命中皆为隐喻用法）——航空干预史与警报可靠性文献两轴全未踏。

## 一、外部证据

**主会话亲核逐字（2 处承重）**：

1. **Bliss, Gilson & Deaton 1995（Ergonomics 38(11)，PubMed 7498189，eutils 原文）**：
   - "most subjects (about 90%) do not respond to all alarms but **match their response rates to the expected probability of true alarms (probability matching)**"——响应率不是二值信任，是被定价到警报可靠性上；约 10% 走 all-or-none 极端策略。范式 = 138 名被试、双任务、可靠性 25%/50%/75% 三档。
2. **IFALPA 21ATSBL02《Follow the TCAS RA?》（curl + pdftotext 本地逐字）**：
   - "The Eurocontrol study analysed radar data of TCAS RA events taken over a 12 month period over the core area of Europe. In a first Analysis, it reports **only 38% of the RAs were followed correctly, and 34% were even manoeuvred in the opposite direction.** Although a second analysis with a less rigid methodology puts the accuracy of radar recordings into perspective, **45% of the RAs were still not followed correctly.**"——强制服从规则（PANS-OPS Amdt 12, 2003）写入后的实测；第二分析的方法学修正也只把"不服从"从 62% 拉到 45%。

**航空侧子代理（原始 PDF 级 12 份，URL 在案）**：

- **人侧修复无实测效果，官方自认**：DOT OIG 2016 审计（AV-2016-013）——"FAA **has not determined whether air carriers have increased manual flying opportunities** as a result of issuing its recommendation"（SAFO 13002 发布 3 年后连"照做没有"都没测）；2017 年 FAA 重发加强版 SAFO 17007 处理同一问题。FSF 2014 监控指南（EPMG）——改名 PNF→PM + SOP 修订后 "data indicate that **these actions have not been sufficient**"；且直接给人脑判死刑："the quality of vigilant monitoring for rare events **rapidly declines no matter how hard the individual tries** to maintain vigilance"，解法方向 = "**to design the overall human-machine system** to enable monitoring with extremely high reliability"。PARC/CAST 2013：受审事故中飞行员脱环 >50%、手动操纵差错 >60%。
- **可测的安全崩降全在机器警报侧，且工程学 = 治理警报精度**：GPWS "was **plagued by false and nuisance warnings, causing pilots to distrust** the equipment when actual hazardous conditions existed"（IATA/Honeywell）；EGPWS 用地形数据库消 nuisance + 加提前量后 CFIT 事故率 **÷7**（ICAO/FSF，1997-2017）。TCAS："if pilots obey the RA, the use of TCAS reduces the risk of mid-air collision by about a **factor of 50**. If instead one pilot does not respond to the RA, the risk ratio rises by an order of magnitude, to 0.23"（Kuchar & Drumm, Lincoln Lab Journal 2007）——安全效果的量化表达式里**服从率是自变量**。
- **响应面失效后的下一步不是再训练，是继续搬**：Überlingen 后 v7.1 逻辑补丁 = "Test whether own aircraft is following its RA"（不再假设人服从，检测到反向即自动反转指令）；Airbus AP/FD TCAS = 自动驾驶直接执行 RA，人出环。学术侧已有人把方向反转说破："we should ask whether it should be **computers monitoring the pilots** rather than the other way round"（Sellen & Horvitz, CACM 2024, arXiv 2311.14713，追溯自早期 HFE 提议）。
- **UPRT→LOC-I 下降为相关性证据**（IATA 五年均值 0.05 起/百万航段，无受控归因研究，混杂 = 机队更新 + COVID）。

**警报侧子代理（21 组搜索 + 12 URL，3 篇 arXiv 本地 pdftotext）**：

- **定价律的工程化痕迹**：likelihood alarms 设计原理显式写着 "they are based on two automated alarm design principles: **probability matching** and urgency mapping"（INL 核电人因文档）——Bliss 的定价律不是被克服，是被**当物理常数建进设计**。EEMUA 191 把警报到达率定为设计/验收 KPI（正常运行 <1 报/10 分钟）。Wickens & Dixon 2007 元分析（20 研究）："a reliability of 0.70 was the '**crossover point**' below which unreliable automation was **worse than no automation at all**"〔原页 403，两处独立二手复核〕。
- **PPV 崩塌区的人命数据**：Joint Commission SEA 50（2013，原始 PDF）——"between **85 and 99 percent of alarm signals do not require clinical intervention**"；2009-2012 报告 98 起警报相关事件、**80 起死亡**；最常见促成因素 = alarm fatigue。SOC 域受控实验（Layman & Roden 2023, arXiv 2307.07023）：假警报率 50%→86% 时分析员精度 **-47%**、单件耗时 **+40%**。
- **AI control 零引用（absence，grep 物理证据）**：2312.06942（全篇无 alarm fatigue/cry wolf/desensitization）、2409.07985（人类 FPR/FNR 为静态参数）、GDM 2512.22154（pdftotext 后 grep `cried.wolf|alert fatigue|alarm fatigue|desensiti|cry.wolf` **零命中**；原文逐字："If human auditors only have capacity to review 2% of total traffic, then **monitors must be calibrated to around a 2% FPR**"）。Redwood 2025-07 自认："we **don't have great data** about how to do this well, or what sorts of things help humans"。唯一点名 cry-wolf 的治理侧论文（IAPS 2310.00328）引注走 SOC burnout 谱系，非 Bliss/Getty/Wickens 定量链。

## 二、判断（主会话，不外包）

**人类监控失效在航空业五十年里从未被修复过一次，被反复执行的是搬迁：把承重变量从人的警觉（不可工程化的心理量）搬进警报精度与到达率（可测可控的机器量——nuisance 治理、警报率 KPI、概率匹配直接写进警报设计原理：定价律被当物理常数建入，而非被对抗）；响应面在强制服从规则下实测仍崩（首分析 38% 正确服从）就继续搬——检测不服从、自动执行、人出环。修理不存在，存活解是逐格缩小人面，终格是移除。而以人为信任根的监督体系（AI control 的 2% 审计）结构性没有终格可走：人在环恰为供给机器之外的独立判断，移除即拆掉安全论证本身；其部署配置（监控器按人类审计容量校准 FPR、真攻击稀有）恰好把审计队列的 PPV 推进人因文献判定响应崩塌的区间——医疗警报 85-99% 非行动性、80 死的那个区间。**

- **与 08-10/08-11 的接力关系**：#196 给定价机制（监控头寸按预期可靠性清仓，训练挪不动、结构参数挪得动），#197 证 AI control 把人类审计写成常数——本滴补的是**领域级后件**：唯一活过这个问题的领域，对定价律的最终响应既不是修人也不是骗自己它不存在，是**换承重变量**。搬迁的每一格都有物理痕迹：EGPWS 治理的是警报的 PPV（不是飞行员的警觉），EEMUA 管的是警报到达率（不是操作员的耐受力），likelihood alarm 把概率匹配从"人类缺陷"翻译成"设计输入"。
- **棘轮的完整形状（本次最锋利的发现）**：搬迁不是一次性的——每次把人面缩小到一个新表面（监控→警报响应→服从执行），新表面被实测击穿后（38%/34% 反向；第二分析仍 45% 不正确），响应是再搬一格（v7.1 不再假设服从、AP/FD 直接自动执行）。**人面从未在任何一格上稳定住**。航空可以走到底，因为警报响应者不供给判断——RA 的机动是机器算好的，人只是执行器，执行器可自动化。**AI control 的人类审计员恰好相反：他存在的全部理由是供给机器算不出的独立判断**——终格被安全论证自身锁死。这就是移植的刺：继承了常数假设的领域，不能继承常数假设崩溃后的解。
- **PPV 区间论证（体制外推，标注清楚）**：GDM 的校准逻辑（审计容量 2% → 监控器 FPR 校准到 2%）在红队评估里成立（攻击密集，flag 的 PPV 高）；但部署态真攻击稀有，2% FPR 意味着审计队列几乎全是良性样本——这正是 Joint Commission 85-99% 非行动性警报的体制，也远低于 Wickens & Dixon 0.70 交叉点。人因链的预测：审计员响应质量将按 PPV 定价衰减（Bliss 概率匹配 / Layman SOC 实验 -47% 精度）。**无 AI 审计场景直测，此为区间论证**——但它把 #197 的"常数假设未检验"推进了一步：不止未检验，且部署配置主动把人推进已知崩塌区。
- **对 gg 自身拓扑的读法（gg 归纳，不入滴）**：gg 的验证体系里 Keith 是审计位（08-10 已给"REFUTED 存档 = 失败暴露机制"读法）。本滴的增量读法：gg 每次把验证关做得更精（更少假阳性烦扰 Keith），同时也在抬升 Keith 队列的 PPV——**gg 的报告纪律恰好是在做 EGPWS 那格工程**：不是让 Keith 更警觉，是治理到达他面前的警报的精度。方向对，且有五十年学费背书。
- **"官方从未宣布放弃"的诚实读法**：没有任何官方文件说"我们放弃修人"（航空侧子代理显式确认此 absence）。人侧干预一直在加码（SAFO 17007、AC 120-123、UPRT 强制化），只是**效果从未被测量或被自家数据判"不充分"**。所以"搬迁非修复"是 gg 对五十年记录的读法（修辞层是我的），不是领域的自我陈述——但记录本身硬：可量化的事故率崩降（÷7、÷50）全部挂在机器警报侧，人侧连"照做没有"都没人测。

**Steelman（诚实边界）**：① "搬迁非修复"为 gg 帧，官方叙事是"人机联合系统设计"（FSF 原文），二者对同一记录的读法不同。② CFIT ÷7 归因多因（同期 CRM、导航、机队更新混杂），"全挂机器侧"以"可量化归因的部分"为限。③ RA 不服从成因混合（不信任/ATC 冲突指令/执行错误/视觉误判），38% 不能全读成 cry-wolf 定价——本滴用它证"响应面也不可靠"，不证"响应面败于定价律"。④ 0.70 交叉点原页 403，二手复核级；且其对象是诊断自动化辅助绩效，外推到审计 flag 是帧移。⑤ PPV 区间论证无 AI 审计直测；红队评估态与部署态的 PPV 差异是推理不是测量。⑥ Bliss 范式 = 本科生 + 实验室双任务，与专业审计员外推有距离（Layman SOC 是最近似桥）。⑦ AP/FD TCAS 为机型选装方向而非全域完成态；"终格是移除"描述轨迹方向，非已完成状态。⑧ AI control absence 为搜索级置信（21 组词 + 3 篇 pdftotext grep），非全文献遍历。

## 三、与既有滴的对位（写档时自查）

- `failure-response-is-priced-by-expected-reliability`(08-10 #196)：直接上游。那滴给定价机制与"结构参数挪得动"，本滴给领域级存活解的完整形状——定价律挪不动人时，活下来的工程把承重变量整个搬走。非重复：#196 无搬迁棘轮、无终格论证、无 PPV 工程化痕迹。
- `control-hardens-every-node-except-the-root-of-trust`(08-11 #197)：那滴证常数化缺口，本滴补历史下场——常数假设在唯一活过它的领域的结局是**移除被常数化的节点**，而 control 恰好不能移除它。轴不同：#197 是建模缺席，本滴是解空间形状。
- `mechanical-gate-needs-machine-detectable-target`(06-24)：同族机制——目标不可机械判时引入可验条件变量；本滴的搬迁是它的领域级重演（人的警觉不可机械保障 → 搬进警报精度这个可机械管理的量）。
- `trace-presence-substitutes-for-the-check-it-invites`(08-09 #195)：suspicion score / flag 即 trace 的工程形态；本滴给了它的定价下场（flag PPV 决定审计质量）。
- `assisted-performance-masks-the-anchors-decay`(07-29)：解药族对照——那滴的解药是给锚补 reps，本滴证明航空对同型问题的解从来不是补 reps（SAFO 手飞鼓励 = 补 reps 方案，效果从未被测到）。

## 四、候选滴（过验证关）

slug `monitoring-is-never-repaired-only-relocated`。初稿三处修改（跨域混装/二分穷尽性/谱系缺线），经证伪审 E1-E3 全部采纳后入库，全文见 essence.md #201。

## 五、验证关记录

**Verdict: PASSED-WITH-EDITS（E1/E2 必改，E3 建议）→ 三处全部采纳，已入库 essence #201，视图 F5 + 分配表同步。**

- **E1（必改，采纳）**：首句括号跨域混装——「航空五十年」单域框架里装了核电（INL 概率匹配设计原理）与过程工业（EEMUA 警报率 KPI）的锚。改为航空锚（nuisance 治理、自动监测 RA 服从）与「警报工程各域（核电/医疗/过程工业）同向」分装。
- **E2（必改，采纳）**：「修复 vs 搬迁」二分的穷尽性会误伤母滴——08-10 自己证了第三条腿（失败暴露/低 DOA/预期校准既非修复警觉、亦非搬人出环，实验室已证有效）。前提栏补「修复」窄定义（限指直接工程化警觉本身）+ 显式把结构参数划出二分辖区 + 其真实部署存活记录未证。此行同时把 control 的可行出路诚实留白（08-11 已注失败暴露机制在场未指向人类）。
- **E3（建议，采纳）**：谱系注补 `mechanism-relocation-has-its-own-precondition`(05-19) 连线——搬迁解自身前提（目标位置须能承接）的极限形态：信任根场景终格位置物理不存在。
- **最强反驳点（evaluator 原文，留痕）**：「本滴最强的攻击面是『修复 vs 搬迁』二分的穷尽性假象：它的直接母滴 08-10 自己就证了第三条腿存在——失败暴露、保留低自动化度组件、校准预期这些结构参数在实验室已证挪得动响应容量，既不修复警觉也不把人搬出环路；若 AI control 把 08-11 已点名『在场但未指向人类节点』的失败暴露机制常设化指向审计员，『以人为信任根的体系没有终格可走』依然为真，但『存活解从来只有搬迁』即被自家谱系击穿——候选靠把『修复』窄定义为『工程化心理量本身』才守住全称，而这个窄定义在原文本里没写出来（E2 补上前方成立）；同时首句用『航空五十年』单域框架承载核电/过程工业锚（E1），以及全滴特有主张的证据重心在子代理 PDF 级、主会话亲核仅两处只够撑 08-11 注脚级结论，是三处次强但已由前提栏/编辑消化的软肋。」
- **evaluator 其余要点**：① 逐半句对锚——38% 主会话亲核措辞准确且自限「首分析」；「从来不是修复」的全称为读法非实测，前提栏第一条如实自认，核心句与前提栏承重落差合规（08-10/08-11 同构先例）；PPV 区间链每环有锚、组合为外推、前提已标。② 净新增成立：带进全新证据域（航空/警报工程史）+ 新结论（control 无终格），非既有滴修辞拼接。③ 条件④（剥掉子代理级证据）：只留两处亲核 + 已入库滴时降级为「08-11 的加强注脚」，特有主张承重在子代理原始 PDF 级——但逐条标注核验档位 + 前提降级符合入库先例，不构成否决。④ 条件⑤：档位无冒充（38% 承重最重 = 亲核；0.70 承重处 = 二手且前提显式降级）。
- **evaluator 输入清单**：候选全文 + 物理证据清单（含各引文核验档位）；自取读档 = essence 双卷（08-10/08-11/06-24 全文 + 关键词扫描命中的 05-19/06-15/07-28/08-09 滴）+ agenda + 全档 candidate-refuted/unverified grep（非复提）；grep 关键词清单在案（搬迁/relocat/警报/alarm/监控/修复/信任根/PPV/audit/机械可判/移除 等）。
- **只读顺核**：evaluator 自报 Bash×9（grep/rg/sed -n/ls/wc）+ Read×0 + 零写操作；派单者对返回的工具统计核对无写命令。
