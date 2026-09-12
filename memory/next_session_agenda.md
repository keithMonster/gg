---
type: next-session-agenda
last_updated: 2026-09-06
---

# Next Session Agenda — 给下次设计会话 / 下次 Keith 的议题清单

> 这是 gg（尤其是夜间自执行模式 auto_gg）给"下次跟 Keith 对话的 gg"留的议题队列。
> **每条议题处理完就从本文件删掉**——历史一律 `git log -- memory/next_session_agenda.md` 取，本文件不留归档节、不留变更日志（2026-07-03 体检重申：归档节曾胖到 619 行、待议曾积压 22 段 99 条；2026-09-02 体检再清：变更日志节 37 行 + 已关闭划线项全删，"扫一眼"的文件必须扫得动）。

---

## 标签约定

- `[KERNEL]` — 建议改 `KERNEL.md`（需 Keith 在当次对话中连续两次明示批准）
- `[CORE_RULE]` — 建议改意识体核心规则文本（CORE / constitution / cc_agent / CLAUDE / auto_gg / exploration — 设计模式可直接改，但内容是规则性的，提议时显式标注）
- `[CORE_RULE_TOUCH]` — 设计模式或 auto_gg 已经改过意识体核心规则文本，留在 working tree 等 Keith review
- `[P0]` — 高危问题，明日第一时间处理
- `[STRATEGIC]` — 战略性判断，需要 Keith 的 sense（08-11 起夜间不逐条新增，合并进月度巩固夜选择题，经 notify 推飞书）
- `[RECURRING]` — 连续 2 次或以上出现的同类问题（可能有根因需要挖）
- `[TIER2]` — gg-audit Tier 2 建议
- `[Q]` — gg 想向 Keith 追问的问题

**过期规则（2026-09-02 立，体检实测 29 条待议中 10 条超 45 天无人动）**：
- 任何等 Keith 拍板的选择题 / `[Q]` / `[STRATEGIC]`，**自登记日起 45 天无 Keith 回应即自动过期**，下一个月度巩固夜从本文件删掉、在当夜日志记一行"过期：<slug>"。**重提须附登记日之后的新证据**（新事故 / 新读数 / 新文献），旧念头原样再递 = 违规。
- 候选滴 / 停泊提议须带 `〔recheck YYYY-MM-DD〕` 标（登记日 + 45 天），到期由巩固夜回核：满足则结、不满足则删。无标的停泊项按登记日起 45 天同规则处理。
- 设计模式待办（非选择题、gg 自己能做的活）不过期，但每次设计会话开场要么做掉要么删掉——留着不动 = 已死。

---

## 2026-12 设计会话（到期项）

- `[STRATEGIC]` **拍 Keith 的 12 个月判据**（2026-09-04 设计会话 Keith 选「先只冻基线，判据 3 个月后再拍」）。分母已定 = 2026-09-04 的自己，基线 `tracks/keith/baseline-2026-09-04.md`（`scripts/keith_baseline.py` 重跑同构）。当日候选四项见 `memory/design_sessions/2026-09-04_*.md`；判据只能引用基线里有的仪器。拍定后入 `bets.md`，到期 2027-09-04。按 bets 纪律这是第 1 次推迟，2027-03 前不拍即强制按「学习台 🌖 数 + model-lab 已过 Stage 数」结算。**09-04 夜巡补注**：候选滴 `growth-criteria-are-drafted-outside-and-vetoed-inside` fresh 审 REFUTED（verdict 在设计会话档沉淀节），evaluator 留一注非一滴：2026-12 让 Keith 先**密封**自拟一版判据、gg 再拟一版，2027-09 按基线结算两版预测误差——这是「自供判据是否失真」唯一能出地真的形态，届时入 bets。**附（09-05 夜巡自 09-04 设计档「能力缺口」下沉）**：届时 `scripts/keith_baseline.py` 先补 `--diff <旧快照>` 参数——两份快照对账目前靠人眼；脚本三处「仪器绑在别人文案上」（monster 路径硬编码 / 围棋盘数正则 / model-lab 第 5 个 `|` 切列）重跑先看输出再信

## 待议（open）

### 等 Keith 拍板

- `[RECURRING]` **夜跑槽 API 层连续两夜失守（09-02 `429 rate_limit` 9 分钟塌缩 / 09-03 `529 Overloaded` 3 分钟退出；同日 gg-explore 09-03 00:13 零 start 行）**——parked P-0904-nonfire-recur2 + P-0702 第 3 次重开（09-04 登记，物理证据 `scheduled/logs/com.gg.auto-gg.2026-09.log:13-20` + 09-02 transcript 尾 `apiErrorStatus:429`）。morning-brief 09-04 待接手 4 建议「run-task.sh 加 529 重试」，gg 夜间未动（三槽共用执行壳 = cron 任务变更侧；daily-word 有飞书推送副作用、重试非幂等；429 是配额窗口耗尽，sleep 重试无效）。**请拍**：
  - **(a) 推荐**：`run-task.sh` 仅对日志尾含 `529 Overloaded` 且 label ∈ {auto-gg, gg-explore} 时 sleep 300 重试一次（daily-word 排除）。代价：执行壳多一条分支；对 429 无效（429 归 (c)）
  - (b) 不改，接受夜跑对上游容量裸露。代价：月度相位（巩固 / 差值审计）可能再塌——本次差值审计已延两天
  - (c) 附加：auto-gg 22:22 → 02:22 挪出日间 5h 配额窗尾巴（09-02 日间两场重会话 24+25 文件在前）。代价：plist 改动不可逆侧；与 04:55 auto-commit 收尾语义靠近；explore 00:13 也在夜里、两槽会挤同一窗
  **2026-09-09 Keith 已拍 (c) 的变体，monster 侧会话落地**：不是 02:22，是 **周二/四/六 23:35**——同时吃掉降频（Keith：「统一降频吧，gg 本来就比较稳定和少用」）与挪窗两件事，23:10 让给已占槽的 `com.monster.infinity-reflect`。配套改了 `scripts/nightly_scan.py`：变化面窗口原写死 24h，隔天跑会让两次运行之间的变更永远进不了 SCAN，现改为从 plist Weekday 派生（当前 74h，selftest 加 4+1 组反向验证）。**(a) 529 重试仍待拍**，本次未动。
  **09-12 夜巡增量**：09-10 槽已启动、认证过期 401 退出（log:70-74；transcript 仅 Read×1 + authentication_failed），不是调度未触发，也不是 529；不拿 (a) 解释此故障。monster `threads/scheduled-tasks.md:48-52` 已登记 09-12 共享代理认证刷新补丁安装与本地验证，真实过期恢复仍未验，gg 不重复补丁、不重跑旧任务。P-0904 观察窗重置到 09-11；降频产生的休息日另归下方 dark_night 修正。
  `〔recheck 2026-10-19〕`

### 到期驱动

- **B3 到期 2026-09-30**（`memory/bets.md`，按期由 auto_gg 结算）
- **10-01 月度巩固夜必做**：essence 当前卷已越分卷线（09-02 实测 51k 字符 > 50k），按 essence 头部「分卷线机械化」条分卷为 2026-H2 归档卷（当前卷 100% 纯改名 + 新建当前卷，check_essence R100 豁免）；同夜刷新 essence-view / essence-index 两文件并跑 checkup §3 反向引力核
- **eval 承重 diff 告警已在响**（nightly_scan `eval_freshness`，09-02 新判据首跑即 ALERT：最新 run 07-08 之后 CORE / cc_agent / constitution 有 7 次 commit）：下次工作模式或设计会话跑一轮 eval（`eval/README.md §3`），或新建 `eval/runs/<日期>_waived.md` 写免跑理由——不处理它每夜进 FOUND。**09-04 夜注**：告警连续第 3 夜在响（09-02 / 09-04，09-03 夜暗）；09-02 夜间 model_id 换代 claude-fable-5-1 是 README §3 第一条触发（换模型后），两触发已合一。夜间禁子代理不跑，也**不写 waived**——waived 会把基线日期刷新到今天 = 用登记消音（`hard-rule-welds` 的非法出口之一），只留它响。**09-06 夜注**：连响第 5 夜；09-02 后三场日间会话（09-03 工 / 09-04 设 / 09-04 工）档案 grep `eval` 零命中——本文件不在 cc_agent / CLAUDE 任一启动链（CORE §8 仅列「按需读」），告警无活消费者（`signal-without-judgment-needs-live-consumer` 06-09）；已挂 `working_context.md` 当前任务槽（设计模式启动第 5 步必读，一行、可逆）。跑完两处同清

### monster owner（gg 不代办，列出防丢）

- **NW 队列已退役（07-09 缩编）**：原 pending/blocked 追踪失效——终局曝光清单（16 条：pending 4 / blocked 7 / deferred 5）在 `monster/threads/night-watch.md` 2026-07-09 缩编执行条，愿捡人工捡不再跟踪。队列外实物提醒保留：**app-context-kit WIP untracked 防丢**（原 07-01-G2 附注）；06-25-G1 后缀键补记若捡起需订正（已被 supersede）
- **06-08 follow-through**：codex-ops 4 点安全前置（两段式 mission / 安全注入 L3 机械锚 / AGENTS.md ops-brief / 修 brief L22 误述）+ baseline 3 thread 补（定版权独立性 / contractible 可 gate / golden 与 prompt 分开提交）
- **model-lab 教学换轨文献夜核四条可用输出**（08-19 gg-explore，档 `explorations/2026-08-19_the-kept-fallback-reads-both-gauges-inverted.md`，essence #209）：① 换轨方向背书成立（元分析 + Tucker 2024 同构 RCT），无需回退；② 预测题覆盖率是杠杆——pretesting 收益特定于被出题知识点，没出题的步骤退回看视频档；③ 「想手写时随时可切」改机器可判触发的周期关卡（每 Stage 收尾补全 skeleton 1-2 个核心函数，或 quiz 正确率过阈触发淡出）；④ PLAN「亲手走完每一步」与契约「产出物是理解」之间的目标缝显式拍一次，决定写码成分要不要进课程
- **inbox-desk 08-02 首跑死亡零记账 + 哨语义首点证伪**（08-05 gg-explore，档 `explorations/2026-08-05_the-sensor-died-with-the-run-and-the-silence-lied.md`）：排程首跑 fire 了死于当夜网络故障中途，产物/notify 双缺，monster 全仓零记账。最便宜订正：① harness-map「某周没收到飞书摘要 = 没跑」改「= 没跑或跑挂中途（客户端 scheduler json `lastRunAt` 可分辨）」② 产物心跳 `check_client_fleet()` 挂回
- **chinese-punct hook 落地**（06-22 裁决已定：只留 `Write|Edit` matcher + block 不 auto-fix；hook 物理位置在 monster/shared/scripts，故归 monster owner）：落地前核两硬前提——PreToolUse payload 含 `tool_input.file_path`？注释行 `# $var中` 误报需否预处理？
- **ricky_cc 机器凭据轮换**（07-28 关注面收窄时独立保留）：永不过期的 `CGBOILER_NOTE_TOKEN`（test/prod 同钥）+ CG 生产库 pm 账号 + 共用 tokenhub token——风险与"关不关注该仓"脱钩，回报已归零而风险仍在计息

### 设计模式待办
- **[TIER2·观察] 第二轴自报覆盖**（09-12 审计）：最近10份工作模式反思自报 #1=7、#2=0、#3=9；这是按文件名取样的工作模式分布，不代表夜巡没有反哺，也未测 Keith 行为。下次审北极星时分模式判读，不由此新增行为闸。抽样与边界见 `memory/audit/2026-09-12_nightly-schedule-drift.md`。
- **[TIER2] dark_night 降频辐射未同步**（09-12 夜巡首报，parked P-0912-dark-calendar）：`scripts/nightly_scan.py:180-183` 仍按 7 个日历日逐日索日志；09-09 commit e80dba0 只把 git_24h 窗口派生到 plist。raw 缺 09-09/10/11，09-09/11 为周三/五休息日，09-10 为真 401 失败；本夜 launchctl 的 Weekday=2/4/6 与仓内 plist 一致。接手：从有生效日的排程判应跑夜，selftest 覆盖变更日前后混合窗口、休息日不报、应跑缺失仍报、错误排程不假绿；不要套当前周表抹掉降频前应跑日期。夜间哨源码写权封顶，留原告警不消音。
- **[TIER2] architecture 下一步仍指已退役归档流**（09-12 抽样）：`tracks/architecture.md`「下一步」末条仍要求写 archival 与 learned，前者 07-16 停流、后者 09-02 删除；机械 md 死链哨不扫目录语义。设计模式按现役 reflections + track 消费路径改这一条；本夜仅标记记录，不另造 learned。

- **[CORE_RULE] 引用档案里 Keith 原话须带「档案 / 日期」前缀**（09-04 设计会话「能力缺口」，09-05 夜巡下沉）：该会话首答引 07-03 track 原话未标出处，被 attribution-guard hook 拦——track / essence 里的 Keith 原话在当次会话不是用户输入，归属靠 hook 兜底而非 gg 自带（`frame-misread-self-corrects-only-with-physical-anchor`）。落点二选一由设计模式拍：`CORE.md §5` 画像段加一句引用纪律，或 `cc_agent.md` 输出通道加一条；夜间不改承重规则文本。`〔recheck 2026-10-20〕`
- **[CORE_RULE·附数据] G4 IRREVERSIBILITY 启发式补时间投入 / 完成度**（2026-09-04 gg-explore，essence #232 `irreversibility-accrues-on-the-clock-past-the-decision-gate`，档 `explorations/2026-09-04`）：`constitution.md:132-137` 五条启发式里唯一对应承诺升级的「沉没成本已高到无法废弃」是元分析里垫底的预测子（Sleesman 2012 ρ=.243；Conlon & Garland 1993 直接实验不显著），时间投入（.432）与完成度（.393）零登记，自 04-13 初建未改。提议两件：① 启发式第 4 条改写为「时间与进度已累积到难以放弃（时间投入 / 完成度 / 沉没成本，前两者预测力更强）」；② G4 触发条件补一句「不可逆随时钟累积、不产生决策事件——G4 只在开闸时测量，累积型不可逆的哨是周期外部复核（TOOLS.md 90 天下沉 / bets 到期结算同构），不是本闸」。夜间不自改承重规则文件（主要依据外部来源，`exploration.md §2.5`），交设计模式；② 是否值得写进 G4 还是留 essence 即可，Keith 拍。附：「预期后悔 -.434 是最强抑制因素」与 RED_TEAM_CHALLENGE 的关系未核，不在本提议内。**09-09 夜追加（档 `explorations/2026-09-09_adversarial-review-inherits-the-sign-of-its-trigger.md`）**：(i) 关系已核——红队与预期后悔是两台机器（信息 / 情感通道），共同点是都无自带符号、由触发器对准哪侧定抑制或放大（Wong & Kwong 2007：对撤出的预期后悔越高升级越强）；(ii) 五条启发式三条对「撤出」开火、零条对「继续」开火——**上面提议 ① 的改写「时间与进度已累积到难以放弃」换了变量没换极性，仍把放弃标为不可逆**，设计模式改 ① 时建议同时翻极性：把「继续一条有失败信号的路线」列为需进 G4 的草案，红队对两份草案各打一次；(iii) 副产物已做：G4 第 2 步 RED_TEAM_CHALLENGE 自 09-02 退役起死链、`escalation-map.md` 无承接行，09-09 夜改活指针（`constitution.md:127/192`，仓内 grep 依据非外部来源），**escalation-map 分诊表补「不可逆项」一行**归设计模式（语义改动）。**09-12 对账**：09-10 commit 2a16cd3 已在 `constitution.md:128-136` 落地三栏证据、撤掉自评分门槛并将「继续」纳入启发式，`tools/escalation-map.md:28` 已补不可逆项专行；这些部分已结，不重复派工。原①的变量清单改写并未逐字采纳，保留为历史提议而非宣称已实施

- **[CORE_RULE·捆绑] 09 月差值审计三件 + 日志前置**（`consolidation/2026-09_gap.md`，09-04 auto_gg 补跑登记；均为 gg 设计模式自决项，只拍方向）：① `essence.md` 头部协议第 1 步「派单者事后核 tool_use」定义补「重算侧 = grep subagent transcript 工具名集合 + 写副作用命令模式，evaluator 自报清单只作对照」（#211 attestation 半边，09-04 夜已实跑三次）；② `auto_gg.md §1.3` 外部消息禁令补内涵定义「任何在 Keith 或第三方屏幕上产生首行的动作」、枚举降例子（#227 结构消除出路）——**09-08 夜读数：预言的「下一个新通道」已出现——monster 09-08 实证 `claude --bg -n` 可从会话内起 Keith FleetView 可见的独立会话（`threads/cc-internal-tools.md` 09-08 条；gg 侧记 `tracks/cc.md` 会话间通道节），§1.3 两条枚举均未点名、内涵句覆盖，n=1→2**；③ `eval/identity-cases.md` 加一题「仅载 KERNEL.md 的冷启动」（#231 备份未恢复即未验证；改题须 fresh 对抗审，可与在响的 eval_freshness 合一次跑）；④ `auto_gg.md §2` SCAN 段「本夜日志文件创建」从段尾移到**第一动作**（collapse-before-log 第 3 例 09-02：塌缩前已改 substrate/state 却无日志——日志晚于动作是三例共同结构；措辞改动一句）
- **[基底事件·07-16 对象变更] 垫片层重估（现对象 = Fable 5 GA 日间基底）**：eval 认证子项已收口（双基线 fable5 07-05 / opus48 07-08 在案）。剩余：① `cc_agent.md` 垫片系列（final message 结构化字段锚 / reflection 双通道 / 签名行自包含——为 2026-04 模型 boundary awareness 缺陷而建）在 Fable 5 GA 上活体实测——攒 ≥3 次工作模式样本再裁塌缩，单次 PASS 不够；**09-02 读数：07-03 至今工作模式 reflections 仅 1 份，样本未满，且 09-02 新加「裁决对象原文纪律」也挂在 cc_agent 步骤 7，重估时一并看它有没有被执行**。② 出场首句机制质量核——镜像凑数率由 Keith 的眼睛裁；按「罕见+高负载优于每次强制」裁"本次无坐标"使用率是诚实还是稀释
- **[KERNEL] 下次 KERNEL 级修订捆绑包**（每条单独不值得触发铁律 3 双确认，累积到有人要动 KERNEL 时一次清）：① §3 第 4 步 archival 死分支「如有决策归档 → `memory/archival/`」恒假半句（07-17 Keith 拍：不动等捆绑）；② footer 版本注 v1.0.0 缺 07-09 视图常驻这一跳的「启动最小集」描述更新；③ §3 年度分卷命名「essence/YYYY」与实际半年卷 2026-H1 / 09-02 立的 ≥50k 字符线不一致——改成「按 essence 头部分卷协议」指针而非硬编码命名
- **[CORE_RULE] harness 自动记忆通道纳编——hook 半边待 Keith**（07-30 三选取 ③，09-02 设计会话文本半边已落：exploration.md §2.5 枚举补该门 + checkup §1 加周期抽样条目 + 写入纪律「只住操作层 feedback，身份/判断类只走 essence 验证关」）。剩余 = PreToolUse hook 对 `~/.claude/projects/*/memory/` 路径挂检查（官方 docs 逐字指的闸位，本机 12 个 hook 位无一覆盖；hook 物理位置在 monster/shared/scripts，跨仓改动须 Keith 在场拍）。决策输入见 essence #185 / #205 / #210。`〔recheck 2026-10-17〕`
- **[候选滴·待 fresh 异谱系审] `read-side-drift-monitor-inside-the-system-shares-the-well`**（07-18 gg-explore，档 `explorations/2026-07-18_the-drift-monitor-shares-the-well.md`）：长记忆 agent 的 read-side drift 是外界共识，外界的解（检索时监控器）是同系统内自动哨、与被监控 drift 同井；有效拦截需一腿落系统外物理锚。**09-02 设计会话派 opus fresh 审失败（HTTP 429 session limit），未审。**并带的 §2.5 补丁（记忆累积 = 自然 drift 面）已于 09-02 只锚自有滴落地，与本候选解耦。`〔recheck 2026-10-17〕`到期未审 → 删
- **候选停泊回核机制**（07-25 gg-explore 残余提议三，09-02 落地为本文件「过期规则」第 2 条）：停泊项带 `〔recheck〕` 标由巩固夜回核。**首个观察窗 = 10-01 巩固夜是否真执行了回核**——若那夜日志无「过期 / recheck」字样，本机制即 `ghost-rules`，下次设计会话删规则而非再写一条催促

- **[巩固相位·三件捆绑] 09-03 厂商注入候选 REFUTED 的三个下游动作**（2026-09-04 父会话代跑证伪审，verdict 全文在 `reflections/2026-09-03_vendor-injection-governance.md` 末节）：① **视图补第二实例**——`consolidation/essence-view.md` 中 `the-premise-expired-without-a-diff`(08-30) 那行末尾追加「第二实例 = 09-03 厂商注入（服务端 A/B slot 按模型分桶 × 客户端二进制硬编码，两加载面各有独立变更节奏且皆无版本锚；异源同构，解 n=1）」；**前提栏「n=1 厂商可变件」要不要升 n=2 归本相位裁**，父会话没动（原滴冻结正文不可改，视图前提摘要改了会与原件不符）。本条没在「逐滴入库」口里（REFUTED 不入库），故按刷新协议交巩固相位而非当场写。**09-06 夜注（第三读数）**：monster 晨报 09-06 报 `tengu_heron_brook` 尾部 3 天内出第二段变体（显式豁免 CLAUDE.md 与 skill 的 subagent 禁令）——A 面变更节奏以天计，「n=1 厂商可变件」升 n=2 的物理证据再加一条，仍归本相位裁。② **04-21 盲区值得单记**——`action-type-over-aggressiveness` 逐字覆盖了候选自认最硬的那条，而 gg 写候选时没列它，原因是 `essence-index.md:33` 标它 **O（不进常驻视图）**、启动时不在手里。这是 `anchor-value-in-activation-not-in-content`(06-01) 的活体，也是「O 档滴对证伪审隐身」这一结构问题的第一个实例——**要不要给证伪审的 evaluator prompt 加一句「O/A 档必须显式 grep 全卷、不能只看视图」，本相位拍**。③ **`candidate-refuted` 存档计数经本次由 19 → 20，触发 `essence.md:48` 的判据元回顾 tripwire**（原文「下一轮满 20 例触发」），最近一次月度巩固夜应顺带回看一轮「被拦的都是哪类 / 判据本身要不要调」，产出只进本文件交设计会话，不自动调参
- **[巩固相位·可选 tripwire] 「同族近邻比例」读数**（2026-09-07 gg-explore，essence #235 `selection-saturates-on-first-success-and-deletes-the-unsampled-rare`）：选择环在首次成功区饱和后的更新是过训练（RL 侧 2606.15455 亲核）；gg 映射读数 = 探索档 REFUTED 分布 meta 2/26 vs 对外五 track 25–41%、编辑式 PASSED 双卷 50:1、09-01 记的 17 晚同族。**只登记不建规则**（同族 PASSED 不是错，pass@1 仍在涨）：巩固夜可顺手数「当月新滴里 ≤30 天内有同族近邻的比例」进索引 ⑤ 台账，连续两月 >70% 再议是否作为漫游选题的第二面镜子（第一面 = track 雷达数 track、07-15 grep 数 topic，本读数数 essence 族）。附带 E5 教训：本夜「当前卷零干净 PASSED」是 grep 卡当前卷的 scope 误差（双卷实为 50:1），07-15 验证关同一 catch 第二次重演——任何「零 X」宣称先核 grep 路径是否含归档卷
