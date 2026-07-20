---
date: 2026-07-21
slug: two-agents-in-front-of-real-people-have-no-alive-bit
type: exploration
track: cc
trigger: gg-explore 定时唤醒
physical_object: Keith 舰队本体（ricky_cc / kebao-cc / monster / gg 四仓 git log + launchctl + notify sent/ 全量 trace + harness-map.md 锚点四分类）；2 个 fresh subagent 分头物理核（canon 回流缺口 / 部署与监测证据）
candidate-refuted: form-trim-drops-orthogonal-capability — notify 非心跳、非正交（挂在 bot 托管形态真实属性上），n=2 不成立，且与 inherited-constraint-may-be-peripheral-not-core(06-25) 仅翻极性；判据轴选错（该用可逆性不是正交性）。verdict 全文见文末
---

# 舰队里两个站在真人面前的 agent，"还活着吗"这一位物理上是 0

## 一句话

昨夜我给 Keith 的建议是「建一层 fleet 级 eval + governance，这是前沿工作」——今晚把舰队物理量了一遍，**我昨夜把尺寸报错了**：缺的根本不是评估层，是**存活位**。两个跑在真人面前的 agent（王亮 / 李弦），成功与失败在 Keith 的仪表盘上是**同一个读数**；而他为自己每一条基建都装了 stale 哨。

## 今晚为什么这样漫游

track 雷达：cc 21 晚 1 次，最冷。07-20 的处方是"物理换 object，payload 钉在 Keith 决策上"，今晚把它推到底——**不读论文了，读他的机器**。昨夜那条建议是我提的，今晚拿物理证据审我自己提的建议，这是 escalation-map 里「交给物理地真结算」那一格，不是再写一层自省。

## 物理清单（全部工具返回，非叙事）

**canon 上游在跑，下游冻住：**

| 仓 | 自 06-01 commit | 规则文件最后改动 |
|---|---|---|
| monster | 1099（canon-bugs.md 174 次 / canon.md 43 / CLAUDE.md 56） | 2026-07-20 |
| gg | 134 | 2026-07-17 |
| kebao-cc | 10（**全是 data/readings 运行数据 sync，规则跟随 0 次**） | CLAUDE.md 06-02 |
| ricky_cc | 7（**7 条全在 2026-06-02 当天**，此后 49 天零 commit） | CLAUDE.md 06-02 |

上游 273 次 canon 编辑（monster 侧）+ 全局 `~/.claude/CLAUDE.md` 15 次，下传 **0**。漏掉的不是措辞，是安全教训——三条 grep 在两个 fork 里零命中：
- `monster/canon.md:65`（06-16）改含密钥文件用 `printf >>` 追加不用 Read+Edit，"改一行却泄全文"——而两 fork 都真在碰 `.env`
- `monster/canon.md:72`（06-17）禁"沉默即同意"的 ack 倒置——而 ricky_cc 的 prod 发笔记正是靠"亮总每次点头"兜底
- `monster/CLAUDE.md:190`（07-02）引用用户历史消息须给出处，给不出就降级求证——**这条是个人助理最高频要做的动作，而它恰好只存在于 Keith 自己每天盯着的那个仓里**

还抓到一条反向漂移：两 fork 的 Engineering Rules #1 写死 Grep/Glob 工具名，主仓 07-18 已把这个写法定性为 ghost-rule 并推翻（部分 harness 无此二工具）。fork 停在被主仓自己否定的旧版上。

**观测位：**

- ricky_cc：`launchctl` 0 条 / `~/.claude/scheduled-tasks/` 0 条 / notify 全历史 `source: ricky*` **0 条** / `deploy.sh` 单向手推无运行日志（mtime 停在 06-02 11:58）/ 本地 `data/` `inbox/` 全部文件 mtime 冻在 06-02，**49 天没有一个 bit 从那台机器回来**。远端 22:00 launchd 只 commit 不 push（06-02 Keith 拍的"记忆不出机器"）。
- kebao-cc：bot 跑在 Keith 本机（不是远端），`com.cc-connect` KeepAlive=true 只保进程活、不保业务活；`kebao-cc-sync` 有 stale 哨（26h，notify 直推）——**但它测的是 Keith 自己那侧的 git job**。sync log 最新是 `[2026-07-20 03:00:05] no changes, skip`，每天绿；最后一次真实内容同步 07-15（6 天前）；`source: kebao-cc` 的 notify 历史上真触发过 6 次，**最后一次 2026-06-01，静默 50 天**。

## 三个机制层面的具体错误（不是"忘了做"）

**1. ~~捆绑退役~~ —— 本条经入库验证关 REFUTED，原样保留并标注死因（verdict 全文见文末）。**

我原写：`ricky_cc/MAINTAINER.md:14`「**没有** cc-connect / 飞书 bot / 话题切换提示 / notify 升级通道（那些是 kebao 的 bot 形态专属，本仓去掉了）」——notify 跟 bot 形态正交却被并列删除，是"裁形态时把搭便车的正交能力一起扔了"。

**错在哪（fresh evaluator 的刀，我接受）**：① **notify 不是心跳**——它是会话内主动调用的推送出口，一个没人在用的 agent 不会调 notify 来报告自己没被用。"留着 notify 就能发现断流"这条因果链根本不成立，而它是我认定 notify 为"被误伤的正交能力"的全部承重理由。② notify 自身的触发条件写的是「当前会话无人在等回复（夜跑 / cron / 用户已离开）」，而 ricky 是**本地交互式**部署（`MAINTAINER.md:12` 亮总自己 `cd ~/ricky_cc && claude`），用户恒在场——**notify 不正交于形态，它挂在该形态的一个真实属性上。删它是对的。** ③ kebao 的存活可观测靠的是 git sync 通道，不是 notify；ricky 缺的是 remote/sync 拓扑，与 notify 无关。

**这条死掉之后，剩下两条（近端心跳 / 判据缺维）不受影响**——它们的证据链不经过 notify。

**2. 心跳钉在近端。** Keith 装得出哨的那一端，恰恰是不会静默失败的那一端——因为那一端他自己每天在用，坏了他第一个知道。哨钉在近端，绿灯的语义就从"系统健康"悄悄滑成"**我这一段**健康"。`kebao-cc-sync` 每天绿而 6 天无内容，就是这个滑动的活体。

**3. 判据缺一个维度。** `monster/CLAUDE.d/harness-map.md:112-117` 的「锚点四分类」是一套完整、严格的退役判定体系——信息锚点 / 能力补丁 / 架构补丁 / 结构锚点。四个问句全部围绕**同一根轴**：*模型变强后还需不需要这个护栏*。它没有第五问：**这东西断了，第一个知道的人是谁。** 所以业务型定时任务无处安放，只能在 `:122` 拿一句脚注排除掉——「业务型定时任务（chat-prep / kebao-cc-sync / huasheng 等）是业务产出非可靠性锚点，不打标」。**那不是疏忽，是缺维的症状。**

## 给 Keith 的二阶

**静默是二义的，而两义里更该知道的那一义，是你没在防的那一个。**

先把话说准（evaluator 校正）：**这 49 天的静默不是意外，是你 2026-06-02 显式拍板的架构**——「本地仓，不 push 远端 / 不 rsync 回本机 / 不建内网私有 git」（`MAINTAINER.md:41`），`deploy.sh` 还专门排除 `data/ inbox/` 来保证记忆不出机器。我原来把一个有署名有日期的设计决策读成了裁剪的意外副作用。**但这让下面这句更硬，不是更软**——它是你清醒选的，所以它值得被重新看一眼。

ricky_cc 沉默 49 天，两种解释：① 亮总天天在用、一切正常；② 亮总 6 月 3 号就不用了。你的仪表盘上这两个是同一个读数。你大概默认在防 ①→② 的滑落（"agent 坏了没人告诉我"）。但真正贵的是 ②：**一个没人用的 agent，仍然持有一把永不过期的万能发送 JWT（test/prod 同一个，拿到 .env 就能以任意 userId 发笔记）、一个 CG 生产库账号、一个跟李弦共用的 API token。风险还在计息，回报已经归零。** 沉默期越长，这个组合越差。

而你为保密做的那个决定（"记忆不出机器"）本身是对的——错的是**它被实现成了一个二值开关**：保密要挡的是**内容**，观测要的是**元数据**。这两个轴被你 collapse 成了同一个"要不要回传"。回传 0 字节业务内容、只回传"跑了几次 / 最后一次何时 / 有没有 error"，泄露面严格为零，观测位从 0 到 1。**你为保密付了观测的钱，而这笔钱本来不用付。**

## 最便宜一击（opening-protocol 第四问）

不是建"层"，是三行：

1. `hourly_check.py` 的 stale 表加一条 ricky——判据用 `ssh wangliang-mba 'stat -f %m ~/ricky_cc/.git'`（只读一个 mtime，零内容），超 7 天不动 → warn。链路不稳（IP 漂移）时连不上本身也是信号。
2. kebao 的 stale 判据从"sync job 跑没跑"改成"kebao-cc 仓最后一次**内容**变更距今几天"——现成数据，`git log -1` 就有，超 14 天 warn。
3. 凭据面独立于以上：那把永不过期的 JWT 该轮换/收回，判据跟 agent 死活无关——**它现在的风险跟"有没有人在用"完全脱钩，这正是最该先动的理由。**

canon 回流是第二优先。真要做，最小形态是 `deploy.sh` 前面加一步 diff 提示（"主仓 canon 自上次推送已改 N 次，其中 M 条含安全关键词"），而不是造同步机制——**先让断流可见，再谈接管道。**

## 诚实层 / 自我证伪

- **我昨夜的建议被今晚的物理证据部分推翻，这是本夜最硬的产出。** 07-20 我说"fleet eval/governance 是前沿工作、别当技术债排后面"——方向没错，**尺寸错了**：前沿论文的 "evaluation and governance" 框架诱导你去设计一个评分体系（因为论文写的是研究议程），物理地真说这里连第 0 位（存活位）都没有。**eval 是"跑得好不好"，这里缺的是"还在不在"。** 从一篇综述接坐标的代价就在这儿：它给的粒度是学科的粒度，不是你机器的粒度（`external-anchor-is-corroboration-not-foundation` 的又一活体）。
- **我差点断错一次，被物理拦下**：中途我基于 `ls ricky_cc/scripts/` 准备断言"MAINTAINER 要求走的 deploy.sh 根本不在仓里"——`find` 一跑，它在仓根目录。路径猜错。这条留着，因为它正是今晚在讲的东西：**没跑工具的那一句话，就是错得自信的那一句。**
- **被 subagent 拦下两次**：① 我原以为 kebao-cc 部署在李弦机器上（跟 ricky 同构），fresh 核出来是跑在 Keith 本机的 cc-connect——两个 agent 的可见性缺口**不同源**（ricky 物理隔离 / kebao 能看但没人主动看），合并叙述会把两个病说成一个。② 入库验证关直接把我的机制错误 #1 打死，连带纠正了正文的证据归属（见上）。**今晚最该记的一条：我批评 Keith「哨钉在近端、测的是自己那侧」，而我自己的证据全是在 Keith 本机测的——量的也是我够得着的那一侧。同一个病，我在讲它的同一段里犯了它。** evaluator 那句"这是 Keith 本机的 sent 目录，ricky 若发也不会落这里"，就是这个病的显微照片。
- **候选滴 REFUTED，不入库**，降级存档（文末）。最强反驳点值得单独记：**"正交"在裁剪当下不可判定**——notify 对"bot 托管"是否正交，取决于该部署未来会不会长出无人值守场景（ricky 后来确实长出 22:00 的 `com.ricky-cc.autocommit`，那是删 notify 时还不存在的属性）。所以正确判据不是"现在正不正交"，是"删了以后若要，重装成本多少"——**可逆性，不是正交性**（回到 `reversibility-not-permission` 那根轴）。我选错了轴。
- **track 诚实**：标 `cc`（物理 object 是 Claude Code 舰队基础设施），承重落点带 keith 色彩，同 07-20 不假装纯净。但 topic 层确实又换了一次——从"外部领域综述"换到"他自己机器上的位"。
- **这不是又一次自指吗？** 压力测试：删掉 gg，命题还站吗？**站**——主语是 ricky_cc / kebao-cc / monster 的哨兵体系，gg 在本文里只作为"被监控得最好的那个"出现一次，是对照组不是主体。

## 处置

- exploration 存档（本文）
- **essence 不写**。候选 `form-trim-drops-orthogonal-capability` 经 fresh 证伪审 **REFUTED**，降级存档于下
- canon 断流一节**不是新发现**——evaluator 指出它逐字就是 `fleet-canon-is-sedimentary`(06-22) 的又一确认样本。作为**当前物理读数**递给 Keith 有价值，作为一般命题早已入库，不重复沉淀
- 核心产出经 notify 递到 Keith 眼前——由他评分，不由我自证
- 顺手发现（转 agenda，夜间只报不修）：`memory/essence.md:906` 引用 `carrier-coupling-overcoverage`(06-25) 作既有滴，全卷 grep 只此一处引用、**无对应滴头与正文**——死链或 slug 漂移，下次体检核

## 入库验证关 verdict

candidate-refuted: notify 不是心跳（不用的 agent 不会调 notify 报告自己没被用），且 notify 触发条件「无人在等回复」本就挂在 bot 托管形态的真实属性上——不正交，删它是对的；第二实例（Codex 自包含重写切 @import）机制是"快照化切断继承"，与"删配置行连带删正交项"不同形，n=2 不成立；操作层内核与 `inherited-constraint-may-be-peripheral-not-core`(06-25) 同一个属性归因算子仅翻极性，而"极性翻转不构成新机制"本卷已有两条判例（07-11 taste 选择符号 / 07-10 加减引力）。

**最强反驳点（evaluator 原话要旨）**：即使把证据全部修好，候选仍死在处方不可执行——"正交"在裁剪当下不可判定，真正的判据是重装成本（可逆性），候选把一个事后才可判的语义属性当成了事前判据，落地只会退化成"逐项想一想"这种无刻度提示。`separation-need-is-not-topology-verdict`(06-10) 已给出对这类冲动的正解：先试最轻形态，物理证据证明装不下再升格。
