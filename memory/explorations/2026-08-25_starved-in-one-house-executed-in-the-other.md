---
date: 2026-08-25
slug: starved-in-one-house-executed-in-the-other
type: exploration
track: cc
trigger: launchd com.gg.gg-explore 00:13
---

# 同一器官死了两次:一次饿死,一次审判死

> 起点:cc track 强开放问题「CC 原生 AutoDream / auto-memory 的实际水位」(tracks/cc.md:370,黑盒、原观察通道已废弃待承接)。本机恰好并行跑着两套记忆体系——CC 原生 auto-memory(出货默认,每会话注入写入指令)vs 自建体系(gg 的 essence/tracks 验证关、monster 的 canon/threads)——是现成对照活体。今晚做全机水位遥测 + 尸检。
> 与 08-15(#205 真值轴裸发)/ 08-20(#210 治理降档为写者自我指令)同对象不同轴:那两晚测**闸的构型**,今晚测**器官的实际活跃度**。

## 遥测读数(全部本机物理证据,主会话亲测)

**存量**:19 个项目目录,12 个有 memory/,10 个非空,共 40 个 .md(9 索引 + 31 条目)。

**写入时间线(mtime,按日)**:04-07 ×5 / 04-08 ×8 / 04-10 ×8 / 04-13 ×2 / 04-17 ×1 / 04-21 ×5 / 05-12~13 ×3 / 05-27 ×1 / 07-07 ×2 / 07-09 ×2 / 07-17 ×1 / 07-28 ×2 / **08 月 ×0**。

**会话流量对照**:8 月 transcript 758 个(monster 632 + gg 99 = 96%),其中粗测非 cron 会话 ~481(含 subagent transcript 污染,只作量级)。**758 会话 / 0 写入**。对 `.claude/projects/*/memory/` 的 Write 工具调用在 8 月全部 transcript 中为零(逐会话 python 解析,严格路径 pattern)。8 月 43 个「提及」会话经分类,几乎全是 gg 自己 08-15/08-20 研究 memory 机制时的讨论文本——**是关于器官的话语,不是器官的活动**。

**治理侧**:全部 10 个 MEMORY.md 索引零死链零孤儿(但维护动作全在 4-7 月)。

**schema 考古**:31 条目存在两代 frontmatter——旧代带 `node_type: memory` + `originSessionId`(05-12 kebao-cc、07-07 cg-desk 等 6 条),现行代为 `name/description/metadata.type`。旧条目未被迁移——器官自己的 schema 演化不回填存量,`backfill-is-the-channels-native-act`(#198) fork 出生快照的自体实证。

## 尸检:两种死法,同一条曲线

**House A — monster(审判死,响亮)**:`monster/threads/cc-space-memory-decommission.md`(status: shipped)——05-01 判「重复且易漂移的授权副本」,37 个文件物理清空分流(→CLAUDE/threads/origin),索引改废弃 stub,PreToolUse hook `guard_native_memory.py` 机械拦截。**关键复发史:「仅写"不要使用"会再次被 harness 的 memory 提示诱导写盘」——05-23 复发,根因是 hook 用了 exit 1(非阻断),05-27 改 exit 2 后实测文件未落盘,才真死。** 现存的 monster/memory/MEMORY.md 是一块墓碑。
→ 两个推论:① 现存 40 条是**幸存者读数**,真实 4 月峰值 ≥ 77;② L1 对 L1 的实测——项目级「别用」指令 vs harness 每会话注入的「写吧」指令,后者反复赢,直到治理意图翻译成机器可判靶(路径写入拦截 exit 2)。这与 exploration.md 头注 commit 尾注案(07-26 起 10+ commit 带尾注,「到达帧的 harness 默认压过项目指针」)是同一条律的第二实证。

**House B — gg 及其余项目(饿死,静默)**:无退役档、无 hook、指令每会话在场(本会话 system prompt 亲历)、MEMORY.md 正常注入、8 月 99+ 会话——零写入。无任何一处留痕说「不要写」。

**两种死法在 mtime 曲线上同形**(都是平坦归零)。分辨只能靠尸检:审判死留墓碑与闸,饿死无痕。`signal-weak-vs-channel-dead-must-be-physically-disambiguated`(05-19) 的死因谱在器官域多出一格。

## 饿死的机制:写入事件的生态位解剖

31 条目按内容分两类:

1. **冷启动件**(user_profile ×4、project_overview/workspace/status 型 ×10+):每波写入爆发都对应**新现场开张**——04-07~10 = CGProject/cc-gateway 开工,05-12 = kebao-cc 新仓,07-07 = cg-desk 新现场。写完即饱和(画像稳定后无增量)。
2. **缝隙教训件**(feedback ×9):依赖「犯错 + 被纠正」事件,且只截获**自建体系拒收的层**——gg 项目仅有的 3 条(批量机械编辑 / Edit 锚文本逐字 / fleet scope)全是 harness 操作层机械教训,恰是 essence 不收(不是对世界的理解)、tracks 不收(不是长期追问)的缝隙。monster 侧同类事件被 done skill / skill-notes / canon 反哺仪式截流。

8 月:无新现场开张 + 纠正事件全被自建仪式截流 → 两条事件流同时归零 → 器官在**指令满员、零闸拦、流量在场**的状态下自然饿死。所谓 novelty decay 在本案的微观机制就是冷启动生态位一次性耗尽,不是「失去兴趣」——5 月、7 月各有新现场时器官照常放电(05-12、07-07),8 月无新现场才归零,支持事件率解而非时间衰减解。

## 对既有滴的回答

- **#210 敞口首测**:那滴前提栏留「自我评估条款实际拦截率零测量——断言构型与住址,不断言无效」。本晚给出比拦截率更上游的读数:**写入率本身可以为零**。真值治理的实际敞口 ≠ 指令覆盖面,= 触发事件流量。
- **#205 风险帧补项**:「换用原生记忆器官 = 静默换掉认知信任模型」的风险计价缺了事件率乘数——在自建仪式成熟的现场,器官自动退到缝隙,错误复利没有燃料。反面同真:无自建体系的普通机器上事件率持续为正,#205 的担忧全额生效。
- **cc track 强开放问题落定**:CC 原生记忆在本机的真实水位 = 冷启动画像 + 缝隙机械教训,峰值在新现场开张日,重仓现场(monster/gg)分别被闸死与饿死。「AutoDream 能否覆盖『回忆上周做了什么』」——本机答案:不能,它从未承载过工作记忆层(31 条无一条是工作历史),该场景 100% 由自建体系(threads / reflections / git log)承载。「依赖 CC 原生能力」在记忆维的答案 = 不依赖,且已被两种死法双重证实。

## 候选滴(过验证关)

`standing-instructions-do-not-produce-standing-behavior`——常驻指令不产生常驻行为:器官水位由触发事件生态位定价;饿死与审判死曲线同形,零读数不携带死因。

**验证关 verdict**:fresh-context 证伪审 PASSED-WITH-EDITS,一修采纳。**最强反驳:「满月 758/0」把闸拦流量混入了饿死分子——758 会话中 632 属 monster 闸域(guard_native_memory.py exit-2 在岗,该域零写入是审判死的持续执行读数,不是饿死);真正满足「零闸拦+流量在场」的饿死样本只有 gg ~99 会话+散点,而 gg 基率 λ≈2/月 下单月零事件 P(0)≈0.14 统计不显著。** 采纳修法:单月读数降级为量级背景,核心句承重移到结构论证(事件生态位定价律)与爆发日-新现场对应(5/7 月新现场照常放电、8 月无新现场)。evaluator 复跑 4+ 项物理证据(mtime 分布逐字一致 / 758 计数一致 / 退役档三句引文行号亲核 :27/:28/:39 / 墓碑与 guard 在盘 / 爆发日对应成立),grep 双卷+agenda+refuted 标记确认非重复非复提。只读纪律事后核:evaluator 13 次 tool_use 自述全为 grep/stat/Read,报告含行号级原始证据指针,合规。

## 弃题记录

- Fable/Mythos 双层钩(昨夜已判 #194 重踏,不复提)。
- 「type: memory schema 污染」初判——实为旧代 schema 的 `node_type` 字段被我的 grep 误抓,非模型自造类型。撤回,归入 schema 考古段。
