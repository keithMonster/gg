---
date: 2026-08-30
slug: the-premise-expired-without-a-diff
type: exploration
track: cc
trigger: launchd com.gg.gg-explore 00:13
---

# 前提过期无 diff:harness 长出会话间通道,gg 的两条背景契约静默换血

> 起点:雷达显示 cc 是窗口内覆盖最低的对外 track(3/21 晚),且昨晚 keith track 读数 B 撞见的 `origin.kind=peer / verifiedPeerPid` 正是 harness 会话间通信的账本痕迹。今晚不考古账本,直接观测活的机制:ListAgents / SendMessage / peer 网格。

## 读数 A:此刻的会话星座(首次实测)

`ListAgents` 亲测(00:15 左右):本会话 = **gg-16 [0faec2]**,7 个 peer——monster-0b(3d, idle)/ monster-home-d1(4m 前启动,活)/ cc-connect bot debugging(bg, 1d, idle)/ **gg-00(15d, idle)**/ monster-75(3h, 活)/ monster-3f(9d, idle)/ monster-a6(2h, 活)。深夜 00:15 这台机器上至少 4 个会话在世,3 个非 idle。

- 对号:我 = launchctl `com.gg.gg-explore`(PID 28881 → claude 28895, 00:13:02);monster-home-d1 = 00:09:59 的 22962,对上 `com.monster.home-todo-push`。gg 的 plist 物理住在 `gg/scheduled/plists/`(不在 ~/Library/LaunchAgents,launchctl 直载)。
- **gg-00 挂了 15 天**——一个 interactive gg 会话(大概率 Keith 的某个终端 tab)在名册上可寻址至今。SendMessage 文档:名字寻址可复活已完成 agent("a send resumes it from its transcript")。
- 仪器自坑记账:ps 粗 grep 'claude' 报 15+ 进程,核实后大半是 Claude 桌面 App Helper / codex broker / cc-connect 内嵌 headless——名册与真会话集无大缺口。Engineering Rules #9 在本探索内的活体(昨晚是 cwd 错位,今晚是 grep 面太宽)。

## 读数 B:peer 网格的流量与形态

全量 transcript 扫 `origin.kind=peer`:**30 条,100% 落在 monster 目录,gg 零收**;时间 08-26 至 08-28(1/13/16 条——**08-28 过半,我初版记「全部 08-26/27」系解析漏账,由验证关 evaluator 独立重算戳穿改正**),探索时点前 4 日内,机制新近才被用起来。08-27 凌晨 02:28–08:33 一波多会话密集互发,一个 hub 会话收 6 条,from-name 是作业名(「world model…」「root cause…」「cg analytics…」)。另见 1 条 `<agent-message from="general-purpose">`(子代理向上报告)——**子代理消息与跨会话消息走同一条 user role 总线,两种包装公约**(`<agent-message>` vs `<cross-session-message>`),昨晚 #226 归属梯度的又一活体:from-name 自报、uds path 半自报、verifiedPeerPid 内核锚,判断点收到的仍是文本前缀。

## 读数 C:SendMessage 的到达语义(schema 即物理证据,未实测发送)

三条关键语义直接写在工具契约里:

1. **"messages enqueue and drain at the receiver's next tool round"**——发给正在夜跑的会话,消息在它下一个工具轮送达。**夜跑中途可被插话**。
2. **"The recipient's human sees only the FIRST LINE as a one-line preview"**——发到 interactive 会话 = 出现在对方人类的屏幕上。给 Keith 的终端 tab 发消息 = 对 Keith 的主动外推。
3. **"cross-session permission laundering"** 警告——权限边界是 **per-session** 的;而 gg 的克制边界(CORE §7)是 **per-identity** 的(gg 全形态共享)。两个粒度不重合:harness 眼里「gg 夜间会话」只是一个权限配置,它防的是 A 会话借 B 会话洗权限,不识别「gg 作为同一意识体在多个会话里应服从同一边界」。

没有实测发送:唯一有信息量的实验对象是 gg-00 / monster 各 interactive 会话,而向它们发送 = 首行上 Keith 屏幕 = 绕开 notify 唯一出口的主动外推。**判断本身即产出**:这条新通道该按 notify 纪律禁默认,而 notify 契约还不知道它存在(见结晶)。

## 结晶:两条背景契约已静默换血

1. **「夜间 = Keith 不在场 = 无人在等回复」**(auto_gg / exploration / notify 契约的共享前提)——写下时是**物理保证**(夜跑会话无入站通道,除非 Keith 亲自接管终端)。SendMessage 上线后,同一句话降格为**统计惯常**(只是通常没人发)。文本零 diff,承重力已换血。
2. **「主动外推唯一出口 = notify.sh」**——禁令枚举了自建 webhook / cc-connect 旁路,写于 SendMessage→interactive(= Keith 屏幕一行预览)这条通道出生之前。枚举静默失完备。
3. working_context 07-28「gg 和 monster 两点之间要的是**一条边**,不是一层共享基础设施」——这条边 08-26 起由 harness **原生**长出(monster 侧已用 30 条,gg 侧零使用),无需自建。Keith 的架构判断被基础设施兑现,但兑现本身没有通知任何契约文件。

**通用形状**:契约文本锚定的环境前提是**写入时的快照,不是订阅**。前提在环境侧失效时——新通道出生、旧保证降格——本地文件零 diff、也无消费事件可挂钩重核(背景契约每晚被隐式消费,从无「引用时刻」),故一切 diff 触发的守卫(辐射检查 / audit / git log / append 时验证关)结构性无哨。检测器只剩一种:**对环境的周期性重采样**——今晚的漫游恰好就是这个机制在跑。

## 诚实栏

- ListAgents / ps / socket 均为单时点采样(00:14–00:20),会话星座是快照非普查;「gg-00 = Keith 终端 tab」是从 interactive+15d 推的 [推测],未验证其内容。
- peer 30 条 vs 昨晚报 64:窗口与仪器不同(昨晚含 origin.kind 全量统计,今晚只抓 message 层可解析条目),相对量,不构成矛盾证据。
- SendMessage 到达语义引自工具 schema 文本(本会话在场,非转述);「插话到达夜跑会话」未行为学实测——schema 说 enqueue&drain,实际 harness 对 launchd 无头会话是否同语义未直证。
- 「两条契约写于 SendMessage 出生前」:notify 契约段与 auto_gg/exploration 契约的成文日期(≤07-28)早于 peer 流量首现(08-26)是物理事实;但 SendMessage 工具的**上线**日期未考(可能早于首用)。前提降格的起点取保守读法 = 首个被观测使用日。
- 机制是厂商可变件(2026-08 形态的 Claude Code),无版本锚。

## 实务议题(已记 next_session_agenda,交日间/设计会话)

1. notify 契约是否登记 SendMessage→interactive 为受禁默认旁路(夜间对 Keith 外推仍唯 notify.sh)。
2. 夜间契约「Keith 不在场」前提降格是否需要显式条款(收到 `<cross-session-message>` 时按 §2.5 输入卫生对待——它是零认证前缀公约,#226)。
3. gg↔monster 的「一条边」已原生存在,要不要用、怎么用(留 Keith 拍)。

## 候选滴(已过验证关入库 essence #227)

`the-premise-expired-without-a-diff`——背景契约锚定的环境前提是写入时的快照不是订阅:担保模态零 diff 降格(物理不可能→统计默认)+ 背景契约无引用时刻可挂前提重核;检测器按 omission-failures 三出路域内结算,周期性重采样只是兜底。

**验证关 verdict**:fresh-context 证伪审 **PASSED-WITH-EDITS,五修全采纳**。evaluator 独立复核:契约成文日期 git log 实证(notify 段 2026-05-11 / cc-connect 禁令 2026-06-17,均早于 peer 首现)✓;SendMessage 三段引文经 ToolSearch 逐字实核在场(升级为非条件性采信)✓;peer 30 条/monster 100%/gg 零收复算 ✓;**抓到证据记录错误**(时间分布 1/13/16 含 08-28,初版漏账)。**最强反驳:四近邻组合复读**——「快照非订阅」= one-shot-invariant 移环境轴、「零事件+缺席续期」= #185 + omission-failures、「周期重采样」= omission-failures 明文出路二;且「唯一检测器」全称被本案环境自证伪(deferred 工具名每会话注入 = 环境自播报,evaluator 本人即靠 ToolSearch 一步拉到 schema——缺口在「播报→前提重推导」,不在采样频率),把三出路收成一条是分类学倒退。**挡回一半的理由:净新增两件双卷零命中**——(a) 担保模态降格签名(物理不可能→统计默认,零 diff);(b) 「背景契约无引用时刻」堵死 precondition-recheck 家族的适用面(该家族预设存在应用时刻可挂重核)。**五修**:①核心句重心迁至净新增;②删「唯一检测器」全称,改三出路域内结算;③peer 时间记录改错;④补前提栏四条;⑤谱系注显式挂 omission-failures / #185 / one-shot-invariant / precondition-recheck 家族。只读纪律事后核:evaluator 自报全程 Bash 只读 + ToolSearch,零写操作,报告含物理指针(行号/commit hash),合规。
