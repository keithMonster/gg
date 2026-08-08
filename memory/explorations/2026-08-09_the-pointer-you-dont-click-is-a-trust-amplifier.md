---
date: 2026-08-09
slug: the-pointer-you-dont-click-is-a-trust-amplifier
type: exploration
track: humanity
substrate: claude-fable-5
physical_object: 调研子代理 22 次 WebSearch/WebFetch + 2 次 PDF 逐页亲核（六封闭问题）+ 主会话 WebFetch 亲核 2 处承重引文（arXiv 2501.01303 / 2502.08554）+ grep 全档 overreliance 轴零命中
---

# 你不点开的指针是信任放大器

> 雷达：ai ×1 连击（无塌缩），21 晚窗五 track 3-4 均衡、meta 4。
> 选题：humanity track——06-14 做了 aversion 半边（人对算法扣信任），08-04 做了修复轨迹，**overreliance 半边（人对 AI 产出盖章、解释/证据指针对核验行为的因果效应）全档零命中**（grep：overreliance / automation bias / cognitive forcing / appropriate reliance / Logg / Bansal / Vasconcelos 等，全空）。
> 弃题记录：初念「Workflow 工具自带质量模式库」——grep 后发现 07-18 topic 传感器已拦过一次同题重踏，且 `substrate-ships-the-evaluator-body`(06-27) + `absorption-boundary`(07-11) 组合已覆盖"基底出货 REFUTE 面板"的骨架，弃。

## 一、外部证据

**主会话亲核逐字（2 处承重）**：

1. **Ding et al., "Citations and Trust in LLM Generated Responses"（AAAI 2025, arXiv:2501.01303）**：
   - "We found a significant increase in trust when citations were present, a result that held true **even when the citations were random**"
   - "we also found a **significant decrease in trust when participants checked the citations**"——引用的在场本身增信任（与引用内容无关）；真去核验的人信任反降。论文自铸帧 "trust as anti-monitoring"：引用的在场**替代**了监督行为本身。
2. **Kim et al., "Fostering Appropriate Reliance on Large Language Models"（CHI 2025, arXiv:2502.08554, N=308 预注册）**：
   - "the presence of explanations **increases reliance on both correct and incorrect responses**"
   - "we observe **less reliance on incorrect responses when sources are provided or when explanations exhibit inconsistencies**"——解释无差别抬升采纳；降低错误采纳的只有来源指针与解释自曝的不一致。

**子代理侧证据（22 次工具调用 + 2 次 PDF 逐页亲核，URL 在案）**：

- Bansal et al. CHI'21（亲核摘要）："explanations increased the chance that humans will accept the AI's recommendation, **regardless of its correctness**"——前 LLM 时代原始发现，Kim'25 是其 LLM 复现。
- Buçinca et al. CSCW'21（亲核）：cognitive forcing 显著降 overreliance，但"people assigned the **least favorable subjective ratings** to the designs that reduced the overreliance the most"——有效性与偏好负相关。
- Vasconcelos et al. CSCW'23（亲核摘要，N=731 五实验）：核验是策略性成本-收益选择；"null effects found in literature could be due in part to the explanation **not sufficiently reducing the costs of verifying**"——解释降 overreliance 的边界条件 = 把核验成本压下去，不是信息量。
- Passi & Vorvoreanu（Microsoft 综述，PDF 逐页亲核 pp.1-14）：解释被列为 overreliance 四大机制之一而非缓解手段；"even explanations **with no basis in the AI's actual working** can make users trust AI more"。
- Schemmer et al. IUI'23（Q6 最强反例，PDF 逐页亲核）：解释提升"采纳正确建议"侧（RAIR 29.59%→38.87%, p=0.05），但**识别 AI 错误侧（RSR）无显著变化**（p=0.54）——反例只立半边，判别力关键侧仍失败。
- Si et al. NAACL'24（亲核）：LLM 解释助人核查更高效，"however, they **over-rely on the LLMs when the explanation is wrong**"；contrastive explanation（同给两面理由）缓解。
- **结论层（子代理 Q6 汇总）：文献中不存在"解释直接显著提高人类对 AI 错误识别率"的强实证**——正向效应全部落在解释的衍生属性上：来源指针、内部不一致、对比结构。

## 二、判断（主会话，不外包）

**核验痕迹在读者侧不是中性信息，是抗监督剂：它的在场本身抑制核验动作、无差别抬升采纳；让读者变准的从来不是痕迹的叙事量，而是痕迹把核验成本压进读者的努力预算（来源指针）或当场自曝矛盾（不一致/对比结构）。**

- 这是 `verification-trace-as-camouflage`(06-01) 的**读者侧机制升级**：那滴管痕迹骗过检查者（伪装——痕迹没覆盖承重错误但检查者放行），本滴管痕迹**取消检查动作本身**（麻醉——"trust as anti-monitoring"，随机引用同效证明效应与内容无关）。伪装需要痕迹与错误的错位；麻醉只需要痕迹在场。
- **Keith 全局规则「已验证须附物理指针 / 纯转述不算指针」的实证两面**：半边被坐实——sources 是文献里唯一稳定降低错误采纳的痕迹形态（Kim'25）；半边被警告——**零抽核体制里指针退化为内容无关的信任放大器**（Ding'25：随机引用同效增信）。指针规则的保护力悬在"偶尔真有人点开"或"机器代核"这个边际上，不在指针本身。
- **gg 验证关「留最强反驳点、不留 PASSED 三个字」恰是文献支持的形态**：Kim'25 的 inconsistencies、Si'24 的 contrastive explanation——降低错误采纳的是自曝张力的痕迹，不是宣称通过的痕迹。这不是巧合式自夸：06-01 立那条时的理由（防伪装）与文献理由（破麻醉）不同源，两条独立链指向同一形态。
- **与 06-14 aversion 帧的接缝（gg 归纳，无直接实证，不入滴）**：algorithm aversion 需要**目击**算法犯错才触发；anti-monitoring 恰恰推迟目击——所以全托关系不停在 aversion 侧，而是在 overreliance 侧无痛滑行，直到某次错误以"指针原来是装饰"的形态浮出——那时错误已从 competence 类（早发现可修）漂成 integrity 类（隐瞒被发现，06-14：修复路径双堵）。预防侧结论：抽核不是对 gg 的不信任动作，是把错误钉在 competence 类的机制。
- **Buçinca 悖论对 Keith 场景的读法**：降 overreliance 最狠的设计被用户评分最低——摩擦有效恰因为讨厌。Keith 的「核对不抛回」（gg 自己开 fresh subagent 核，不拿 Keith 当 verifier）把核验成本从 Keith 侧移到 gg 侧，绕开了"有效的设计被弃用"这个坑；代价是 Keith 侧的核验肌肉零练习（`assisted-performance-masks-the-anchors-decay` 07-29 的本案投影）。

**Steelman（诚实边界）**：① "随机引用同效"单源（Ding AAAI'25 一篇）；"解释无差别抬升采纳"多源收敛（Bansal'21 + Kim'25 + Microsoft 综述 + Nature'24 标题级）。② 实验域全部是短时程/中低专业度任务（众包、迷宫、事实核查、酒店评论）；专家高风险域、长期重复协作关系外推未测——Keith×gg 是后者。③ 测量混合自报信任与行为采纳，两者在个别研究中可分裂。④ aversion 悬崖后置链是 gg 自铸综合，两簇文献没有互引。

## 三、与既有滴的对位（写档时自查）

- `verification-trace-as-camouflage`(06-01)：直接上游。伪装（骗过检查）→ 麻醉（取消检查），机制升级不重复——那滴的检查者在场且看了痕迹，本滴的检查动作根本不发生。
- `assisted-performance-masks-the-anchors-decay`(07-29)：邻轴。那滴管锚的无辅助基线衰减零告警（能力轴），本滴管单次决策的核验动作被痕迹抑制（行为轴）；两滴共享"委托栈把自报当地真消费"的底座。
- `confidence-is-a-liability-for-algorithmic-advisors`(06-14)：接缝见判断节——aversion 与 overreliance 由"目击"这个闸连接，gg 归纳不入滴。
- `mechanical-gate-needs-machine-detectable-target`(06-24)：出路呼应——机器代核（hash/exit code 自动验证）把核验从人类努力预算里整个移走，是逃出成本-预算约束的结构解。
- `fluency-as-inverse-signal`(05-31)：同族体感——解释的叙事流畅度增采纳不增判别，是那滴在读者侧的人类版。

## 四、候选滴（过验证关）

初稿 slug `trace-presence-anaesthetizes-the-check-it-invites`；经证伪审后三处修法（E1 删 competence 半句 / E2 反降补单源标注 / E3 题眼动词软化为"替代监督"），slug 随之改名 **`trace-presence-substitutes-for-the-check-it-invites`**。入库全文见 essence.md #195。

## 五、验证关记录

**Verdict: PASSED-WITH-EDITS（E1/E2 硬性 + E3 建议）→ 三处全部采纳，已入库 essence #195，视图 F5 + 分配表同步。**

- **E1（硬性，采纳）**：删正文第二行后半「抽核不是不信任，是把错误钉在 competence 类的机制」——本档 §二 自己三处标注该链「gg 归纳，无直接实证，不入滴」，候选滴却把结论句写进了正文，选择性纪律失守；且引 Kim/Ferrin 2004 分类未带域限定（08-04 已登记「此后引 Kim 2004 须带域限定」规则）。该句降级留在本档 §二，不入滴。
- **E2（硬性，采纳）**：「真核验者信任反降」与「随机引用同效」同为 Ding AAAI'25 单源，初稿前提只标了后者；前提句改为两者均单源，「零抽核→信任放大器」后果句连坐此依赖。
- **E3（建议，采纳）**：题眼动词「麻醉/抑制核验动作」在全部引文里无行为直测（Ding 测信任、Kim 测采纳，无一测「在场→核验频率下降」）；改为「替代监督」（"trust as anti-monitoring" 文献原帧义），前提补「帧层推论无行为直测」。
- **最强反驳点（evaluator 原文，留痕）**：「本滴的题眼动词『麻醉/取消检查动作』是全滴测量最薄的半句——所列全部引文测的是信任与采纳，没有一条是『痕迹在场→核验行为频率下降』的直接行为测量；若把 06-01 的『见核验痕迹就放过』读作已覆盖『在场→不查』，则本候选的机制升级主张塌缩为『06-01 + 外部文献锚定采纳侧』，应改判为带锚精化而非新机制、逼近 REFUTED。未翻面的原因：内容无关性（随机指针同效）与正向校准判据（成本与张力）在 06-01 及全库确实零先例，这两件净新增即使砍掉『麻醉』帧也独立站立。」
- **evaluator 其余要点**：①「无差别抬升采纳」是全滴最硬半句（Bansal+Kim+Microsoft 三源两条亲核逐字）；「只有来源指针与不一致」的全称量词仅在痕迹形态类内成立（Buçinca cognitive forcing 是交互设计不在作用域内），勉强立；② 对 06-01 净新增三件：内容无关性、正向设计判据、核验者信任反降悖论——非重复非换皮；④ 剥掉 Ding 后核心第一行塌一半，存活部分退化为 06-01 带锚精化——单源依赖已在前提登记为已知脆弱点，不构成 REFUTED；⑤ 引文亲核标注分级与承重位置全匹配，无二手引文承重。
- **evaluator 输入清单**：候选全文 + 物理证据 4 组；自取读档 = essence 双卷（06-01/05-31/06-03/06-04/06-14/06-15/07-28/07-29/07-30 原文）+ 视图 F4/F5/F10 + agenda + candidate-refuted/unverified 全档 grep（overreliance 轴无既往候选）+ 本探索档全文；关键词 17 个在案。
- **只读顺核**：evaluator 自报 Read + Bash 只读（grep/sed/wc/ls）零写操作；派单者 git status 物理核——工作树除本会话产物与存量脏文件（auto_gg/2026-08-08.md 尾巴回写）外无新增写痕。
