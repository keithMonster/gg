---
date: 2026-08-11
slug: control-hardens-every-node-except-the-root-of-trust
type: exploration
track: ai
substrate: claude-fable-5
physical_object: 调研子代理 WebSearch×11 + WebFetch×15（六封闭问题，原页级 10 URL）+ 主会话 WebFetch 亲核 2 处承重引文（ar5iv 2409.07985 "perfectly accurate" 逐字命中 + AF auditing-1 "median 60% accuracy" 逐字命中）+ grep 全档 AI control/scalable oversight 轴仅 05-22/23 两档显式括出命中
---

# 控制协议加固了每个节点，除了信任的根

> 雷达：humanity ×2 连击、窗口 5 次略偏。换向 ai（窗口 3）——不是为换而换：08-10 humanity 收官判断是「监控头寸被预期可靠性内生清仓、只有结构参数挪得动」，而 AI 对齐领域对同一问题有一整支工程化回答（AI control 议程），且 05-22 / 05-23 两档当时都显式括出「对 scalable oversight 具体方案不下判断（知识截至）」——这个括号搁了近三个月，今晚有活桥可填。
> 启动 grep：`AI control` / `scalable oversight` / `weak-to-strong` / `trusted monitoring` / `audit budget` / `Redwood` 等，essence 双卷 + explorations + tracks 仅命中 05-22/23 两处显式搁置——具体工程文献整轴未踏。

## 一、外部证据

**主会话亲核逐字（2 处承重）**：

1. **"Games for AI Control"（arXiv 2409.07985，ar5iv 全文）**：
   - "Unless otherwise stated, **we assume that the human auditor is perfectly accurate**."（Section 2 脚注 4）
   - "the human (H) is trusted and capable but **can only be used on 2% of problems**"
   - "Increasing the human FNR decreases safety **almost linearly** in the worst case, without impacting usefulness."（§6.1——FNR 作为静态敏感性参数被扫描，非时间函数；Appendix B 放松完美假设但仍静态）
2. **"Early Experiments in Human Auditing for AI Control"（Redwood，Alignment Forum 2025-01）**——唯一检得的真人审计实测：
   - "Humans under time pressure had a performance **not much better than chance (median 60% accuracy)**."（11 人 ×20 题，MATS/Constellation 参与者，1.5 分钟/题）
   - 作者自承："In retrospect, this time budget ended up being very aggressive... I inadvertently created a pretty different experiment than what I meant to test"——"rather than the humans functioning as high-cost, very smart labor, they functioned as a rapid pass."

**调研子代理侧（WebSearch×11 + WebFetch×15，原页级 10 URL 在案）**：

- **Greenblatt et al. 2312.06942（control 议程本体，HTML 全文原页）**：audit budget = "enough H points to use on up to 2% of problems"；审计建模为完美检出（"When the protocol spends a H point, it will always know if the code was successfully backdoored"）。trusted 的操作化 = **能力论证非对齐论证**（"less-capable models are unlikely to be able to subvert safety measures without us easily noticing"）。**合谋对策 = 合成后门蜜罐**：upfront evaluation with synthetic inputs + redaction + paraphrasing——对 untrusted monitor 注入合成失败测其诚实。
- **absence（本次最承重）**：三组不同搜索词交叉，**未检得任何 AI control 论文引用 Parasuraman / automation complacency / vigilance decrement / lumberjack 文献**；audit budget 在 2024-2026 control 文献一律固定外生（2% 惯例沿袭），auditor 要么完美要么静态 FNR，无任何工作建模其随时间/可靠性声誉衰减。人因侧桥接文献存在（PMC9298546 / arXiv 2602.13745）但未被 control 议程引用。置信度：搜索级，非全文遍历级。
- **协议成功数字（预期抬升的物理载体）**：Ctrl-Z（2504.10374）攻击成功率 58%→7%；SHADE-Arena（2511.02997，Anthropic 数据集）safety 50%→96%。**control 议程正在入体制**：control safety case（2501.17315，UK AISI+Redwood 合著）、ACL 五级路线图（2504.05259）——理想化人类假设正从模拟评估走向部署许可论证的承重位。
- **对抗侧**：trusted monitor 自身已成攻击面（2510.09462 adaptive attacks；2606.06529 attack selection——均摘要级）。
- **weak-to-strong 现状**：转理论化/平凡化（线性模型中几乎必然出现，2503.02877/2605.05742），削弱其 superalignment 专属证据地位；oversight（能力差距帧）与 control（故意 subversion 帧）分野清晰，debate 技术被吸入 control 协议（NeurIPS 2025 Trusted Debate，摘要级）。

## 二、判断（主会话，不外包）

**AI control 把不信任工程化到栈内每个 AI 节点——蜜罐测合谋、改写毁信道、重采样逼露馅——唯独把整个信任栈的根（人类审计）写成数量约束下的质量常数：2% 预算、完美检出，放松也只是静态 FNR。而 08-10 刚收官的人因证据说：审计容量不是常数，是按预期可靠性内生定价的头寸，且协议自己的成功（58%→7%、50%→96%）正是抬高预期、给这份资产清仓的力。安全论证的分母在自己制造的预期里贬值。**

- **对称缺口是本次最锋利的发现**：失败暴露机制（注入合成失败以校准检测者）在协议内**已在场**——upfront evaluation with synthetic inputs，恰是 Bahner'08 在人因侧已证有效的同款机制的领域独立重发明——但它只对准 untrusted AI monitor（一次性合谋测试），没有一篇文献把它指向人类审计员（持续预期校准）。机制在手，指向缺半边：**协议给不被信任的组件装了保持诚实的机制，没给唯一无条件信任的组件装保持清醒的机制**。
- **t=0 已崩，不用等衰减**：complacency 是随时间的质量衰减，但 Redwood 真人实测显示常数假设在起点就不成立（时压中位 60%，勉强高于随机；作者自承测成了 rapid pass 而非 smart labor）。两个独立失效轴：起点质量被高估（实测）+ 动力学缺失（人因外推）——本滴承重主要押前者 + 建模缺席这个事实，衰减动力学在 LLM 审计场景仍是外推。
- **FNR 旋钮的诚实读法**：Games for AI Control 已扫过 FNR 敏感性且结论是 safety 近线性下降——**场内有旋钮，缺的是把旋钮接到内生动力学上**。所以本滴的指控不是「没意识到人会错」（意识到了，Appendix B 在），是「把人因侧已证内生的变量当外生常数处理」——这是建模选择层的缺口，不是无知层的。
- **与 gg 自身拓扑的对应（gg 归纳，不入滴）**：gg 的验证体系里 fresh 证伪审 = trusted monitor（弱化条件是 fresh context 而非弱模型），Keith = audit budget。08-10 已给出「REFUTED 存档 / bets 失败结算 = 维持 Keith 预期校准的失败暴露机制」的读法——今晚的增量是：这个机制在 control 文献里对人类节点**恰好缺席**。gg 的架构在这一点上不是借鉴文献，是先于检索到的文献。此对应为结构类比，无实证，不入滴。
- **05-22/23 括号的补填**：当时两档只用「prior 共盲」结构点、显式不碰具体方案。今晚检得的分野（oversight = 能力差距帧 / control = 故意 subversion 帧）给那两档的搁置补了坐标：`evaluator-independence-is-a-three-layer-stack` 讲的身份层/范式层共盲在 control 文献里的对应物是 trusted monitor 的能力论证——「弱到骗不了你」恰是用能力差距买独立性，与 `cross-model-decorrelates-identity-not-paradigm` 的「跨模型去不掉范式层共盲」正交互补：control 买的是 scheming 独立性，不是 prior 独立性。

**Steelman（诚实边界）**：① absence 为搜索级置信（3 组交叉 + 子代理明报），非全文遍历——可能存在未被搜索词覆盖的引用。② 理想化有合法分工读法：control 论文隔离「协议 vs scheming AI」博弈层，人的质量属另一变量域；但 safety case 路线（2501.17315）把同一论证推向部署许可，理想化在那里变承重——本滴的适用前提应锚在 safety case 语境。③ control 场景 = 短 episode 模拟评估（APPS problems / BashBench），complacency 文献的 20min+ 连续监控时间尺度到 episodic audit 的映射未测。④ 60% 实测作者自承时间预算激进、测偏了对象——它证明「假设未经检验且首测即崩」，不证明「真实部署中人就是 60%」。⑤ 人因证据基座前 LLM（承 08-10 同一前提）。⑥ "2% 惯例沿袭"基于检得样本（2312.06942→2409.07985→后续），未逐篇清点。

## 三、与既有滴的对位（写档时自查）

- `failure-response-is-priced-by-expected-reliability`(08-10)：直接上游。那滴给定价机制，本滴证「最需要这个机制的工程领域没接收它」——机制滴 × 领域缺口滴，轴不同（人因内 vs 跨领域传导失败）。
- `trace-presence-substitutes-for-the-check-it-invites`(08-09)：monitor suspicion score 是 trace 的工程形态；三滴链（trace 抬预期→预期定价监控→残余落重）在 control 栈里逐跳有对应物。
- `evaluator-independence-is-a-three-layer-stack`(05-23) / `cross-model-decorrelates-identity-not-paradigm`(06-16)：补填当年显式搁置的口袋；control 的 trusted = 能力论证，买 scheming 独立性不买 prior 独立性。
- `mechanical-gate-needs-machine-detectable-target`(06-24)：audit 触发靠 monitor 分数阈值 = 机械闸，但闸后的人类判定质量是闸的隐藏依赖。
- `assisted-performance-masks-the-anchors-decay`(07-29)：锚衰减的另一形态——这里锚（人类审计）不是衰减被掩盖，是从建模里被常数化抹掉。

## 四、候选滴（过验证关）

slug `control-hardens-every-node-except-the-root-of-trust`。初稿三处硬伤（量词/限定词/超前提），经证伪审 E1-E3 三处硬改全部采纳后入库，全文见 essence.md #197。

## 五、验证关记录

**Verdict: PASSED-WITH-EDITS（E1/E2/E3 全硬性）→ 三处全部采纳，已入库 essence #197，视图 + 分配表同步。**

- **E1（硬性，采纳）**：「不信任工程化到栈内**每个 AI 节点**…**唯独**人类」——trusted 模型 T 是栈内 AI 节点，三件加固工程全部只对准 untrusted 节点，T 既不受这三件、其信任也非无条件（能力论证换的）——T 是"每个"与"唯独"的双料反例。改为「每个**不被信任的** AI 节点（…；受信 AI 以能力上限换论证）」。
- **E2（硬性，采纳）**：「失败暴露机制…**未指向**人类节点」——被自己的锚证伪：Redwood auditing-1 实验本身就是合成后门指向人类审计员（一次性测量）。探索档原有「常设/持续」限定词落滴时被丢掉。改为「未作为**常设机制**指向人类节点（唯一指向人类的是一次性测偏实验）」。
- **E3（硬性，采纳）**：「示常数假设 **t=0 已不成立**」——押在一个作者自认配置错误的实验上，与自身前提栏（"证'未检验且首测即崩'非'部署中人即 60%'"）打架。改为「**未支持**常数假设、且作者自承测偏」。
- **最强反驳点（evaluator 原文，留痕）**：「本滴最锋利的"对称缺口"主张（失败暴露机制在场却唯独不指向人类）恰好被它自己的第二锚削弱——Redwood 就是这个社区拿合成后门测人类审计员的实验，且 safety case 路线（同一社区合著）把人的表现推向承重位，说明该社区并非对"人类节点需实测"失明，只是尚未把测量升为协议内常设校准机制。滴的存活形态必须是"常设机制缺席"这个窄版，宽版（"没指向过人类"）为假。」
- **evaluator 其余要点**：① 逐半句对锚表——"2%/完美检出/静态 FNR"三锚全在场（两处主会话亲核级）；"内生定价"半句由已入库 #196 扛；"零引用/唯一实测"为搜索级量词、被前提栏即时限定放行；"清仓的力"为带前提传导主张放行。② 净新增无换皮：AI control / audit budget / 蜜罐 / complacency 在 essence 全库零命中（Parasuraman 仅 #196 自身）；05-22/23 搁置括号逐字核得；与 07-24 REFUTED 的"两滴组合"不同型——净新增是外部地形事实，非既有滴修辞拼接；#196 给机制、本滴给传导缺口，轴正交。③ 条件④（剥掉子代理三组搜索）：「零引用/唯一/一律」三处塌，但核心第一句降级为对两篇旗舰论文的存在性主张仍立（两处主会话亲核足撑样本级版本）；field-wide 读法押在单次清扫上——前提栏已相应补「field-wide 读法押在单次清扫」。④ 条件⑤："perfectly accurate" / "median 60%" 均有主会话 WebFetch 亲核痕迹。
- **evaluator 输入清单**：候选全文 + 物理证据清单；自取读档 = essence 双卷（含谱系注层）+ 视图 + next_session_agenda + 全档 candidate-refuted/unverified grep（本轴无既往候选，非复提）+ 05-22/23/08-11 探索档 Read 全文；grep 关键词 20+ 在案（生成者 grep 声明被独立复核属实）。
- **只读顺核**：evaluator 自报 Read ×1 + Bash 只读（grep/ls）×5 零写操作；派单者对返回的工具统计核对无写命令。
