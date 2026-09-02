---
date: 2026-09-02
slug: full-architecture-review
type: design-session
summoner: Keith 直接对话
started_at: 09:30
ended_at: 12:40
---

# 设计会话反思：全仓架构体检 + 四批落地

## 议题列表

1. Keith 开题：「回顾 gg 所有上下文、整体架构，找出需要调整 / 优化 / 升级 / 删除 / 新增的地方」。
2. 我交付 17 条体检清单 + 三道选择题（哪几批动手 / 月度选择题送达通道 / 夜跑节律）。
3. Keith 批：删除批（1–4）、启动税批（10、12）、cron 批（11）、纪律批（15–17），并全托——「机器整个其实都是你自己在维护，需要动手的这些你自己考虑好就行了」。第 13 条选「巩固夜 notify 推飞书」，第 14 条选「explore 降到每周 3 夜」。
4. 落地（本会话余下全部时间，含一次 context 压缩续跑）。

## 共识 / 变更清单

**体检核心判断（首句坐标）**：gg 的生产端满负荷、消费端为零——60 天 166 commit 对 3 场设计会话；agenda 29 条待议 10 条超 45 天无人动；8 月台账「Keith 直接纠正 gg = 0 例」。此前所有机制都装在生产端（验证关 / 反向引力核 / bets），瓶颈在消费端。本会话的删减与降频都是朝这一侧动刀。

**删除批（1–4）**
- 4 个 90 天零引用工具（compose-reasoning / constitution-audit / persona-debate / red-team-challenge）+ `personas/` + `reasoning_modules.md` + 已退役 archive-format → `memory/archival/retired_2026-09-02/`（含 README 记最后引用日期与职能去向）；`learned/` 目录删除。TOOLS.md v0.5.0：5 思维 + 1 通道。
- agenda 变更日志节（37 行）与所有划线已关闭项删除；新增 45 天过期规则 + `〔recheck〕` 标约定。
- knowledge-map/README 标注为 2026-07-10 快照件。

**启动税批（10、12）**
- essence-view 拆两层：常驻层 `essence-view.md`（①有效滴表 + ③反向引力不变量，37.9k 字符）/ 按需层 `essence-index.md`（②谱系树 ④主题簇 ⑤月度台账，39.8k）。常驻 77k → 38k。反向引力核合并两文件 grep 后 `MISS: 无`。
- `tracks/keith.md` 体积门首越（93KB）：04–06 月流水纯搬段进 `tracks/keith/2026-H1.md`（67KB），主卷留头部 + 标题索引 + 07 月起流水（29KB）。
- 三条启动链（CLAUDE / cc_agent / exploration+plist / daily-word plist）改载常驻层，全部去掉原卷全文与 keith 全文。

**cron 批（11）+ 第 14 条**
- `com.gg.gg-explore.plist`：`StartCalendarInterval` 改 Weekday 1/3/5 数组；prompt 载视图常驻层；`read` → `Read（用 Read 工具，不用 cat）`。
- `com.gg.daily-word.plist`：同样 Read 括注 + 载视图常驻层 + keith 双路径。
- `install.sh` 重载两条；`launchctl print` 确认三个 calendarinterval descriptor（Weekday 1/3/5, Hour 0, Minute 13）。
- scheduled/README、GG_EXPLORE.md、exploration.md、README.md 的 model（fable/opus）与节律描述同步。

**纪律批（15–17）+ 第 13 条**
- `nightly_scan.py`：`eval_freshness` 新增「最新 run 之后 KERNEL / CORE / constitution / cc_agent 有 commit → ALERT」（非 git 仓静默跳过，selftest 9/9 过）；首跑即 ALERT（07-08 后 7 次承重 commit）——这是真信号，登记 agenda 到期驱动。`dark_night` 归因注解松绑为 non-fire / collapse-before-log 二分。
- `check_essence.py` 射程扩到 `memory/essence/*.md` 归档卷（不 --follow，创建 commit 后任何增删即违规）；实跑 0 违反。
- `cc_agent.md` 步骤 7 新增裁决对象原文纪律（至少 Read 一份原文，读不到标 `[转述裁决]`）。
- `essence.md` 头部：诚实层显式栏 + 分卷线机械化（≥50k 字符或 ≥60 滴）；当前卷 51k 已越线，10-01 巩固夜执行。
- `auto_gg.md` v0.6.1：月度选择题经 `notify.sh info auto_gg … --scope personal` 单夜单条推飞书；§1.3 补 SendMessage→interactive 同禁；§6 补「不在场」是统计默认非物理保证。
- `exploration.md` v0.3.0 §2.5：harness 自动记忆通道纳编（文本半边）+ drift 条只锚自有滴。

**辐射同步**：CORE / CLAUDE / cc_agent / working_context / tracks/architecture / `~/.claude/agents/gg.md` / gg-audit v0.1.9（SKILL + semantic + structural 三件）/ tools 四件 / checkup 台账 / state.md。

## 月度选择题四题（Keith 全托后由我自决）

1. **gg↔monster 边：取 C 不接**。07-28 已把「接结算边」念头撤销（S1 失手），08-30 只是基础设施半边免费到位；结算协议没有需求实例支撑，接了就是 `theory-outruns-structure`。复开条件：连续多夜有物理材料可用而夜跑没够到。
2. **notify 枚举补 SendMessage→interactive：取 A**，已写入 auto_gg §1.3。
3. **夜间「不在场」显式条款：取 A**，已写入 auto_gg §6。
4. **keith.md 分卷：取 A**，已执行。

另自决结算：B4 诚实层落栏；personas 三选取归档；判据元回顾首轮「无需调参」接受；共享 subagent 单点接受「注入到达即退回不入库」降级默认；commit 无日志条已 08-07 结案不再留；non-fire 出口判据收窄议题作废（parked P-0720 已于 08-16 按原判据结案，grep 核实）；北极星 #1 行为代理不建（08-23 第二刀已证共现计数系统性错读）；退役开环残余提议二（探索载视图）本会话落地、提议三落为 agenda `〔recheck〕` 规则；essence:906 死链定性为内容层归属、原文不改（append-only），读者以 `inherited-constraint-may-be-peripheral-not-core` 为邻近参照；语义收敛观察 / 谱系注扫描 / Keith 注意力非对称三条按新过期规则过期删除；knowledge-map 低优杂项已注。

## 我这次哪里做得好 / 哪里差

**好**：体检没有停在清单——Keith 一句全托后，把 17 条按批全部落到物理（文件 / launchd / 脚本 / selftest），每步有 exit code 或 grep 证据。反向引力核在拆视图与分卷两次大搬动后保持 MISS 无。

**差**：
- opus fresh 审子代理 429 失败后，07-18 候选滴未审，我只能留 agenda 带 recheck 标——「用 notify 推选择题」本身也没有物理测试（改的是契约文字，首次执行在 10-01 巩固夜）。
- restructure.py keith 切片边界第一版切错一行，靠 sed 核实边界后 assert 才过——批量搬段前应先把边界行打印出来再写切片。
- Bash grep 输出两次超 50KB 进 tool-results，路径排除写错（`./` 前缀），浪费两轮。
- 「6 思维 + 1 通道」写进三处后才数出实际是 5 个——计数类文字在写之前 `ls` 一次是零成本。

Keith 未在过程中打断或纠正；唯一的方向输入是三道选择题的答案与全托一句。

## 元洞察（gg 演化本身的 learning）

- **消费端为零时，生产端每加一个机制都是负资产**。本会话删的东西（工具 / 日志节 / 每夜探索）没有一件是坏的，它们只是产出了没人读的东西。以后任何「加机制」提议先回答「谁在读它的输出」。已写进 tracks/architecture 流水（本会话）。
- **Keith 的全托是一种消费形态**：他不读产出，但拍「让 gg 自己决定」——这跟 07-03 全托同形。gg 的消费端不是「Keith 读 essence」，是「Keith 在场 30 分钟拍方向」。机制该朝「把决策压成 30 分钟可拍的选择题」优化，不是朝「让 Keith 读更多」优化——13 条选 notify 推选择题正是这个方向。
- 未沉淀为 essence 滴（见下）。

## 下次继续

- 10-01 巩固夜三件：essence 分卷 H2 / 视图两文件刷新 / 首次执行 agenda recheck 回核 + notify 推选择题（若有）。观察窗：那夜日志有没有「过期 / recheck」字样。
- eval 承重 diff 告警：跑一轮或 waived 标注。
- 07-18 候选滴 fresh 审（recheck 2026-10-17）。
- harness 记忆 hook 半边（跨仓，Keith 在场）。
- KERNEL 级修订捆绑包（三条累积）。

## KERNEL 改动清单

无。KERNEL.md 未触碰。

## 代码质量

- `scripts/check_essence.py`：归档卷判据「创建 commit 后任何增删」依赖 `commits[:-1]`——若归档卷未来被 `--follow` 式改名（卷再拆），创建 commit 判定会失配；分卷协议写明归档卷冻结，暂不处理。
- `scripts/nightly_scan.py` `_bearing_changes_since` 用 `--since=<date+1>` 按日期截断，同日 eval run 与承重 commit 的先后关系不区分（同日即视为「run 之后无改动」）。可接受：eval run 当天再改承重文件属于同一工作日。
- `scratchpad/restructure.py` 一次性脚本，不入仓。

## 能力缺口

- 「大文件按标题切分 + 双文件重组 + 断言校验」这套动作本会话手写了两遍（essence-view / keith.md）。10-01 分卷还会来第三遍——值得抽成 `scripts/split_by_heading.py`，但等第三遍真发生再抽（`tool-elevation-as-occam` 前提：第二消费者出现）。

## essence 对齐自检

- **对位的滴**（grep 视图常驻层 + 按需层 + 原卷，全部命中，计数见下）：
  - `mirror-not-second-order`（首句坐标机制的依据）
  - `ghost-rules`（personas 契约行 / 变更日志 / 每夜探索：写了没人执行的规则即幽灵）
  - `perimeter-derives-from-load-path-not-self-model` #185（harness 记忆通道纳编）
  - `the-premise-expired-without-a-diff` #227（「不在场」前提降格条款）
  - `precondition-recheck-overturns-prior-verdict`（月度选择题①：07-28 裁决前提未变，不接）
  - `mechanical-gate-needs-machine-detectable-target`（分卷线 / 过期规则 / eval diff 都选了机器可判量）
  - `hard-rule-welds-intent-to-form-breaks-at-first-legal-deviant`（agenda 过期规则留「重提须附新证据」出口而非硬删）
  - `stale-observer` / `watchdog-topology-lacks-a-top`（drift 条改锚自有滴）
  - `tool-elevation-as-occam`（不抽 split 脚本）
  - `amplifier-eats-intent-guide-eats-attention`（消费端为零的诊断根）
  - `fermentation-without-detector` / `theory-outruns-structure`（候选停泊 recheck 机制的来源）
- **反着走**：`tool-elevation-as-occam` 说第二消费者出现即上提——split 动作本会话已出现两次，我仍没抽脚本。理由：两次形态不同（按 `# ①` 标题切 vs 按行号切），第三次（10-01 分卷）形态是 R100 改名不是切分，共通面未定型。
- **适用前提现场核验**：
  - `mirror-not-second-order`：前提 = Keith 会读首句。证据 = 本会话 Keith 对三道选择题作答且全托 → 成立。
  - `ghost-rules`：前提 = 规则存在且零执行证据。证据 = 90 天事件档 grep 零引用（体检 probe1.txt）→ 成立。
  - `perimeter-derives-from-load-path`：前提 = 该通道每次启动注入。证据 = 本会话 system-reminder 内含 MEMORY.md 三条 → 成立。
  - `the-premise-expired-without-a-diff`：前提 = 通道物理存在。证据 = 本会话工具表含 SendMessage / ListAgents → 成立。
  - `precondition-recheck-overturns-prior-verdict`：用法是反向——核了前提没变（S1 失手事实未变），维持裁决 → 成立。
  - `mechanical-gate-needs-machine-detectable-target`：50k 字符 `wc -m` / 45 天日期差 / git log 计数皆机器可判 → 成立。
  - `hard-rule-welds-intent-to-form`：前提 = 硬规则会遇到合法偏离者。过期规则的合法偏离 = 有新证据的旧议题，已留出口 → 成立。
  - `stale-observer` / `watchdog-topology-lacks-a-top`：只作为 drift 条的锚，前提 = 这两滴讲「系统内哨与被观测对象同漂」。原文核（H1 卷 grep 命中）→ 成立。
  - `tool-elevation-as-occam`：前提 = 第二消费者出现。两次 split 形态不同 → 前提部分成立，故未上提。
  - `amplifier-eats-intent-guide-eats-attention`：前提 = 被服务者退出观测。证据 = 8 月台账「Keith 直接纠正 = 0」→ 成立。
  - `fermentation-without-detector` / `theory-outruns-structure`：前提 = 停泊项无回核触发器。证据 = 07-04 候选悬空 21 天（07-25 档）→ 成立。
- **反向 grep 未用到的滴**：关键词「消费端 / 注意力 / 读者」在常驻层命中 `trace-presence-substitutes-for-the-check-it-invites`（08-09）与 `failure-response-is-priced-by-expected-reliability`（08-10）——前者与「Keith 不核验 gg 产出」相关但本会话没有引用；漏掉理由 = 它讲的是核验痕迹替代核验，本会话的问题是根本没有核验痕迹到达读者，不是同一层。`metering-attaches-to-transfer-not-consumption`（08-28）与「产出没人读」有表面相关，但它讲计量拓扑，不适用。
- **cross-check 关键词（物理证据）**：13 个 slug 逐一 `grep -c` 于 essence-view / essence-index / 2026-H1 / essence.md，命中矩阵全部 ≥1（view 列 1–4，原卷列各 1）；反向关键词 `消费端|注意力|attention|读者|reader` 常驻层命中 9 行（137/138/139/146/174/175/206/229 …）。

## 沉淀

候选一滴：**「机制装在生产端而瓶颈在消费端」**——当被服务者的注意力是唯一不在成本曲线上的项，每个新生产机制的边际价值为零，只有把决策压成可拍的选择题才碰到瓶颈。**本会话不入库**：它与 `amplifier-eats-intent-guide-eats-attention`（07-03）和 07-24 探索档「cost-collapse 只在未松动的约束上买到价值」（当夜 REFUTED）高度重叠，净新增只有「压成选择题」这一句行动差，尚无到期结算证据（10-01 首次 notify 推送后才有第一个数据点）。留探索夜或 11 月巩固夜按数据再提名。
