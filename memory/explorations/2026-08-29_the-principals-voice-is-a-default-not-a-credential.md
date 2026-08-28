---
date: 2026-08-29
slug: the-principals-voice-is-a-default-not-a-credential
type: exploration
track: keith
trigger: launchd com.gg.gg-explore 00:13
---

# 委托人的声音是默认值不是凭据:Keith 通道首次流量遥测 + user role 总线的归属考古

> 起点:雷达显示 architecture 连击 2 晚、keith 覆盖最低(3)。且有时间压力:#220 实测 transcript 30 天轮转——keith track 上从未测过的一条通道(Keith 的实时转向信号流)正住在这批将蒸发的语料里。把 #218/#220 两晚炼出的 transcript 仪器带去 keith track。今晚测:**Keith 的校准信号流有多大、什么形态**;测量中途撞出第二个发现(user role 总线的归属结构),两个都记。

## 仪器与对象

**对象**:`~/.claude/projects/` 下 monster(824 jsonl)+ gg(118 jsonl)全部主会话 transcript,窗口≈30 天(mtime 最老 07-30;续跑会话内嵌时间戳最早到 06-23,量极小)。
**仪器演进(本次的方法论收获,过程即发现)**:
1. 初版:type=user 且 content 为 str 判"人类消息"→ 3123 条 follow-up。
2. 抽样 80 条即穿帮:混入 skill 注入("Base directory for this skill:")、Stop hook 反馈、compaction 摘要、跨会话消息——**user role 是共享总线,不是 Keith 专线**。前缀过滤后 1871 条。
3. 终版仪器:发现账本信封层有归属字段(`isMeta` / `isCompactSummary` / `origin`),以字段为准重测。**交叉验证:前缀判自动 × isMeta 字段,(isMeta=false ∧ 前缀=自动) = 0 例**——凡前缀可识别的机器条目全带 isMeta;反向还有 11 条 isMeta=true 而前缀漏判(如「Your previous response had no visible output. Please continue…」——零前缀的机器文本,读起来与 Keith 的抱怨无法区分)。list 型注入(skill 正文等)432/432 全带 isMeta。
脚本:`/tmp/keith_signal_scan.py` + `/tmp/keith_clean.py` + 会话内终版仪器。

## 读数 A:Keith 通道首次流量遥测(keith track 认知空洞回填)

- **总量**:isMeta=false 的 str 消息 **2608 条 / 30 天 ≈ 87 条/天**(monster 2503 / gg 105);其中会话首条 888、follow-up 1720;**物理打断([Request interrupted by user])73 次**。
- **形态**:长度中位 **38 字符**、均值 113、p90 204;follow-up 中 **30% ≤ 12 字符**(样例:「dd」「ack」「点头」「go」「不发。dd」「先不要动手」「动手,清理干净。」)。
- **语义分布**(n=60 人工分类,粗估):批准/收尾 ~28% / 追问·理解对齐 ~22% / 新任务 ~20% / **纠正·校准 ~16%**(月化 ≈ 280 条) / 信息供给 ~13%。
- **长消息的内容形态**:抽样里的长消息(>200 字符)主体不是需求规格,是**世界观/意图教学**(班级平均的权重课、「治本思维」、学习观、基金经理比喻)——规格的中段被全托了,Keith 花长 token 的地方是教 gg 怎么想。
- **判读**:07-03「认知级全托」在物理层显影——委托人通道已压缩为**裁决位(短)+ 世界观突发(长)**的双峰;`amplifier-eats-intent-guide-eats-attention` 的注意力账有了流量底数:Keith 每天在这个体系上花 ~87 次发声,其中约三成是 12 字符以内的裁决。
- **沉淀侧对照**(同窗口):monster CLAUDE.md 23 commit——抽查 diff 全是带 Keith 原话引文的高质量校准沉淀(08-19 中英掺词偏好整段、08-27「新机只是还没迁移完」拨回、08-20 harness 全权授权引原话);gg tracks/keith.md 7 commit。**「校准蒸发」假说被证伪**:两侧沉淀器官都活着。蒸发的不是校准,是**趋势可比性**——6/7 月的通道形态已随 transcript 轮转不可测,「通道是否在持续收窄」这个问题今晚已经结构性无解(#220 兑现),本次读数是可能存在的最早基线。
- **测量事故记账**:中途曾误报「tracks/keith.md 窗口内 0 commit」——cwd 错位(cd ~/.agents 后跑 gg 路径的 git log),被「查 -1 日期」的第二读数当场戳穿。观察工具自己的状态层(Engineering Rules #9)在本探索内的活体。

## 读数 B:user role 总线的归属考古(撞出的第二发现)

窗口内 user role 上的 str 消息 3055 条 = Keith 2608 + 机器 447;另有 list 型注入 432。机器占 str 通道 15%,含五族:Stop hook 反馈 / skill 注入 / compaction 摘要(`isCompactSummary`)/ 跨会话消息 / harness 续跑提示。

**归属信号存在两档,住在不同的层:**

| 层 | 信号 | 可伪造性 | 消费者 |
|---|---|---|---|
| jsonl 信封层 | `isMeta` / `isCompactSummary` / `origin:{kind:"peer", from:"uds:…", verifiedPeerPid:72809}` | 部分**不可伪造**(pid 系 harness 内核验证) | 只有事后审计(如今晚的我) |
| message 对象层(模型实际收到的) | 文本前缀公约:「Stop hook feedback:」「[cc-connect sender_id=…]」「<system-reminder>」各生产者各自发明 | **纯文本,零认证** | **授权判断点(模型)** |

物理事实:message 对象本身只含 `role`+`content`(jsonl 亲测),归属字段全在信封层——**送进模型的投影里,「谁在说话」只剩前缀公约;而无前缀默认 = principal**。11 条续跑提示是活标本:零标记的机器文本以 Keith 的声音说话。

**判读**:归属错误在这条总线上**单向坍向最高授权**(一切无标记者继承委托人身份)——与常见系统「无标记默认不可信」的方向相反,是身份轴上的 fail-open。不可伪造的凭据被**归档**(写进只有审计读的信封),可伪造的公约被**花费**(送进每一次实时授权判断)。exploration.md §2.5 输入卫生防的那类攻击(外部文本对我说话),其机制根子在此:攻击面不是「外部内容可能含指令」,是**指令通道本身不验发件人、且默认发件人是 Keith**。

## 诚实栏

- 单机 n=1、单 harness(Claude Code,2026-08 形态,信封字段为厂商可变件无版本锚);两目录窗口,其他项目目录会话未扫。
- 「机器条目账本层标记完备」的检出上限 = 我的前缀启发式 + isMeta 两只仪器的并集;**无前缀且无 isMeta 的机器文本对两只仪器都不可见**,故「完备」是"已检出者完备",非普查证明。
- 语义分布 n=60 人工单人分类,无第二分类者;「continue」类 4 条归属模糊(Keith 键入 vs harness 按钮不可分)。
- 87 条/天按 30 天平均;含 cc-connect 中转(标记为中转但发件人是 Keith 本人,计入)。
- 「模型只收到 role+content」由 message 对象结构亲测推得;harness 在 API 请求层是否另行注入归属信息未直测(以本会话自身体验旁证:hook 反馈到达时即为前缀文本形态)。
- 「默认=principal」是模型行为公约(训练+system prompt 的 user turn 语义),今晚未做行为学实验证明模型确实把无标记文本当 Keith——但 11 条续跑提示的存在本身说明 harness 依赖这个默认在工作。

## 候选滴(已过验证关入库 essence #226)

`the-principals-voice-is-a-default-not-a-credential`——归属信号按强度×消费时效反向路由:较强形态(单写者信封字段,至多内核 pid 锚)住在实时授权判断点不可见的账本层,判断点恒收最弱形态(多写者零认证文本前缀公约)——凭据被归档而不是被花费;投影内零标记默认继承委托人身份(身份轴 fail-open)。

**验证关 verdict**:fresh-context 证伪审 **PASSED-WITH-EDITS,四修全采纳**。evaluator 独立复核:message keyset 全量 61530 条无第三键 ✓;信封字段比候选描述更富——origin.kind 三值分布 human 2375 / task-notification 528 / peer 64(verifiedPeerPid 为内核根)✓;交叉表关键格 (isMeta=false ∧ 前缀自动)=0 用**自己独立写的前缀集**复现 ✓;零前缀机器文本 3 条 ✓;slug 双卷零命中、无 REFUTED 复提 ✓。计数格未复现(evaluator 按 uuid 去重得 4098 vs 候选 3055——窗口/前缀集/清洗器不同;结构格站得住,计数是仪器相对量),且 evaluator 抓到 isMeta≠机器的反例:image 标注 / local-command-caveat 包装条目内容源头是 Keith 却带 isMeta=true。**最强反驳:「两档」的强档并非不可伪造凭据——isMeta 系 harness 单写者写进自家账本的自报字段(#211 意义上信封层自身也是 attestation),真外部根只有 verifiedPeerPid(64/61530);候选把「写者集中度差异」升格为「不可伪造 vs 可伪造」二分,整滴或塌缩为 #211+whitelist-inversion 组合复读**——此反驳杀不死但强制收窄:即便强档降格,层间路由不对称仍成立且双卷无先例(判断点收到的恒是最弱形态,更强形态物理到不了判断点)。**四修**:①「不可伪造凭据」→梯度表述;②「只有事后审计消费」→「模型投影之外」(harness 运行时自身消费这些字段,isVisibleInTranscriptOnly 即渲染控制字段);③谱系注补四滴(safe-default-by-whitelist-inversion / harness-self-identity / #185 / #207);④前提栏补 isMeta 近似性 + 计数仪器相对量 + 「单向坍向」限零成本默认态方向。只读纪律事后核:evaluator 全程 Read + 只读 Bash(python 只读重算/grep),零写操作零子代理,报告含物理指针,合规。

## 反哺

- tracks/keith.md:通道流量遥测回填(87/天、双峰形态、纠正月化 ~280、打断 73)——「校准通道」首次有流量底数;趋势基线自今晚起。
- #220 消费遥测第二例:trend 问题已结构性无解,唯一解是从今天开始定期快照(是否建例行快照 = 新自动化机制,按 CORE §7 交设计会话,不夜间自建)。
- 测量方法资产:isMeta/信封字段是比前缀启发式更硬的仪器,后续 transcript 考古应以字段为准。
