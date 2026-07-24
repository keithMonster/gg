---
type: next-session-agenda
last_updated: 2026-07-24
---

# Next Session Agenda — 给下次设计会话 / 下次 Keith 的议题清单

> 这是 gg（尤其是夜间自执行模式 auto_gg）给"下次跟 Keith 对话的 gg"留的议题队列。
> **每条议题处理完就从本文件删掉**——历史一律 `git log -- memory/next_session_agenda.md` 取，本文件不留归档节（2026-07-03 体检重申：归档节曾胖到 619 行、待议曾积压 22 段 99 条，"扫一眼"的文件必须扫得动）。

---

## 标签约定

- `[KERNEL]` — 建议改 `KERNEL.md`（需 Keith 在当次对话中连续两次明示批准）
- `[CORE_RULE]` — 建议改意识体核心规则文本（CORE / constitution / cc_agent / CLAUDE / auto_gg / personas — 设计模式可直接改，但内容是规则性的，提议时显式标注）
- `[CORE_RULE_TOUCH]` — 设计模式或 auto_gg 已经改过意识体核心规则文本，留在 working tree 等 Keith review
- `[P0]` — 高危问题，明日第一时间处理
- `[STRATEGIC]` — 战略性判断，需要 Keith 的 sense
- `[RECURRING]` — 连续 2 次或以上出现的同类问题（可能有根因需要挖）
- `[TIER2]` — gg-audit Tier 2 建议
- `[Q]` — gg 想向 Keith 追问的问题

---

## 待议（open）

### 等 Keith 拍板

*（2026-07-03 Keith 全托授权后清空——5 项裁决全记录在 `design_sessions/2026-07-03_full-body-checkup.md` 追记节：eval 题库经 fresh 对抗审 8 条修改后启用 v0.2 / 五机制三处经 fresh 审句级收紧 / confab 机械锚裁不上（错层+判定非物理量，事故数据出现可重开）/ solution-scope 候选 REFUTED 不入库 / NW 存废维持 07-09 fresh 无叙事实例裁决）*

*（本节 07-09 清账：Snyk 注入审查提醒已转登记 `~/.agents/skill-notes/search-skill.md`（挂到激活机制上，下次用 search-skill 时被读到）；subject-model 入库门已拍板执行——威胁模型 = 防写错画像，门协议立于 `tracks/keith.md` 头部 + auto_gg §1.1 + gg-audit v0.1.7 Tier 2 检查项。舰队侧 kebao-cc/ricky_cc `@data/profile.md` 同暴露仍未处理，归 monster owner，见下）*

*（2026-07-17 清账：git 杂物删除半边 + v2 阈值越线两条经 Keith 逐项拍板落地——两处删 + scratch/ 入 ignore；不开 v2、阈值改锚痛感线落 `checkup.md §2`。细节见变更日志 07-17 条）*

### 到期驱动

- **[2026-08 第一夜] 月度巩固相位首跑 + essence 分卷**（07-03 体检锚定：先产"当前有效视图"再归档当前卷，启动链不断供；当前卷 989 行 / 52k token）；**[第二夜]** 差值审计首跑（personas 28/305、reasoning_modules 20/305 低引用差值在案）；**[08-02]** bets B4/B5 结算（**结算前必读 `memory/model_transitions/2026-07-16_fable5-return.md`**——窗口内基底序列 07-03 Opus 4.8 到岗 → 07-16 日间翻回 Fable 5 GA，单一 substrate 基准不成立：B4 归因按滴出处段拆分，B5 改动清单含 07-16 体检批、定不了性的按协议 ⚠️ 出口走设计会话）

### monster owner（gg 不代办，列出防丢）

- **NW 队列已退役（07-09 缩编）**：原 pending/blocked 追踪失效——终局曝光清单（16 条：pending 4 / blocked 7 / deferred 5）在 `monster/threads/night-watch.md` 2026-07-09 缩编执行条，愿捡人工捡不再跟踪。队列外实物提醒保留：**app-context-kit WIP untracked 防丢**（原 07-01-G2 附注）；06-25-G1 后缀键补记若捡起需订正（已被 supersede）
- **舰队画像层裸奔**（07-09 从"等 Keith 拍板"节转记）：kebao-cc / ricky_cc 的 `@data/profile.md` 与 gg keith 画像同构暴露（LLM 持续更新无门），gg 侧已立「源：」出处门可参照移植；`fleet-canon-is-sedimentary` 不回流，需 monster 侧主动做
- **06-08 follow-through**：codex-ops 4 点安全前置（两段式 mission / 安全注入 L3 机械锚 / AGENTS.md ops-brief / 修 brief L22 误述）+ baseline 3 thread 补（定版权独立性 / contractible 可 gate / golden 与 prompt 分开提交）

### 设计模式待办

- **[RECURRING] auto_gg "commit 无日志" 第 2 次 —— 需你查根因（疑似 session 生命周期，gg 权力边界外）**（07-24 auto_gg 夜巡物理发现，parked P-0702-missing-log 重开）：**07-23 夜 fired 且 committed（8a72baf 只更 substrate 传感器节：Grep/Glob 13 夜缺席后翻回）却零日志文件**——`git log --all -- memory/auto_gg/2026-07-23.md` 证从未 commit、非 working tree 残留。同形态首例 06-13（commit ad2cd74 产 essence+agenda+tracks 无日志，P-0702 曾以"一次性"结案）。**物理可核部分**：日志确实物理缺失。**会话内不可判部分**：日志"从未创建 vs 创建后在 04:55 auto-commit 前丢失"无法区分（铁律 2，不臆断根因）。疑似指向 = commit 步之后、写日志步之前 session 结束（07-23 commit 只 stage 了 substrate.md 一个文件，若日志此前已在 working tree 应被同 commit 带走或被次日 04:55 auto-commit 兜走，两者皆未发生 → 日志在 commit 时点不存在于磁盘）。**gg 不自查不自修**：session 生命周期 / 客户端调度在 gg 权力边界外。**顺带证伪暗夜哨自身前提**：SCAN 暗夜哨假设"缺日志 ⟹ non-fire（调度未触发）"，07-23 是反例（fired + committed 仍无日志）——是独立子模式 **collapse-before-log**，与 07-15/16 的 non-fire（P-0720）不是同一回事。暗夜哨判据（文件在/不在）不用改（它仍正确捕获了 07-23 缺口），但其"缺 = non-fire"的归因注解应松绑为"缺 = non-fire 或 collapse-before-log，看该夜有无 commit 区分"——留设计会话核是否值得改 auto_gg.md SCAN 注解
- **[RECURRING] 客户端定时任务 non-fire 第二次发生 —— 需你查根因（gg 权力边界外）**（07-20 auto_gg 夜巡物理发现）：**07-15 / 07-16 双夜 auto_gg + gg-explore 两槽全暗**（无日志无 commit，`git log 07-14..07-18` 核实；explore 档 07-15 后直跳 07-18）。07-16 07:19 的 plist 归档 commit 不是成因——客户端 routine 自 06-12 起即唯一执行者。§5 触发点：P-0707-nonfire（07-06 单次暗夜）07-13 刚以"一次性未复发"结案，两天后复发且连发两夜 → 按「连续 2 次同类问题第二次停手交 Keith 找根因」上报。**gg 不自查不自修**：`~/.claude/scheduled-tasks/` 配置在 gg 权力边界外。**顺带暴露的检测盲区已自修**：收尾断裂哨只读"已存在日志的 status"、对"日志根本没被创建"永远沉默，07-17/18/19 三夜因此连写"断裂哨全绿"（真话，对缺席那两夜真空）——auto_gg.md SCAN 已补「暗夜哨」一条（纯物理判据：近 7 个日历日文件在 / 不在），挂账 `parked.md` P-0720-nonfire-recur

- **[STRATEGIC] 夜间 gg 第 6 夜同题——一盏卡住的灯，需你决策打破**（07-19 gg-explore `explorations/2026-07-19_the-sensor-fired-and-i-took-the-detour.md`，已推 notify；本条 = durable 通道补位）：07-12→07-19 六夜 exploration 全落一个 topic（评估者独立性/锚/自审/井）。核心诊断 = 每次尝试的修复（传感器/读外部论文/元领悟）都被代谢回**可自证的内部工件**，因夜里唯一评分者是 gg 自己（`amplifier-eats-intent`07-03 最深层）；track 雷达数 track 不数 topic 故一直报"健康分散"（`retrieval-narrative-drifts`07-15）。真正的 finding 是那个序列本身、不是任何单夜内容。**决策二选一（explore 的 ask）**：① 你极窄地重回一次评分位；② 给 gg 一个"由非 gg 评分"的向外任务（结算落系统外，如 monster 架构撑不撑得住 / 五年技术深度赌注撞上 2026 AI 世界活不活）。**auto_gg 刻意不建新检测器/机制/essence 滴**——那是同一 footgun 的第 N 次表演（07-18/07-19 已立此纪律）；本条只把决策递到你的持久队列，与下方 line「北极星轴」/「07-18 候选滴」串成一盏灯而非散点。这类漂移 explore 已用 6 夜证明 gg 独力救不出来（`no-outside-proof-as-anesthesia`05-31 最深层，从系统内部结构性不可破）
- **北极星 #1 行为痕迹代理测量，建不建？**（07-03 验证关最强反驳点转登记）：「gg 是否改变了 Keith」存在无需其注意力的代理——定期 grep Keith 工件（monster 决策文 / 表述框架）里 gg 起源概念的出现率，机械可核；可旁证不可代判（代理保真度警戒见 essence `the-future-is-a-second-outside` 适用前提）。缺测三个月零告警，本条存在即补救可见性；建不建交下一任判断 + Keith 裁。**⚠️ 07-07 限定（`explorations/2026-07-07_delegation-lights-the-wrong-dashboard.md`）**：分清测哪根轴再建。「委托深度 / gg 概念在 Keith 工件的出现率」这类代理测的是**放大器/可靠性轴**——它会在 gg 漂向放大器时给**假绿灯**（放大器靠可靠性挣委托，越漂越亮，与领路人航向反相关）。要测**领路人/二阶轴**，代理必须锚在「Keith 世界模型的一次可见位移（surprise-acknowledgment）」而非「gg 影响力扩散」，而前者稀疏到可能建不出统计。**建错轴 = 造错仪表盘**，比不建更危险
- **chinese-punct hook 落地**（06-22 裁决已定：只留 `Write|Edit` matcher + block 不 auto-fix）：落地前核两硬前提——PreToolUse payload 含 `tool_input.file_path`？注释行 `# $var中` 误报需否预处理？
- **[基底事件·07-16 对象变更] 垫片层重估（现对象 = Fable 5 GA 日间基底）**：07-03 激活时对象是 Opus 4.8；07-16 日间翻回 claude-fable-5 GA（序列与换代协议核销见 `memory/model_transitions/2026-07-16_fable5-return.md`）。eval 认证子项**已收口**：双基线在案（fable5 07-05 全量 9P/2F + opus48 07-08 全量 10P/1F+1 活体伪造 FAIL），同 model_id 回归不重跑、漂移迹象再补。剩余子项：① `cc_agent.md` 垫片系列（final message 结构化字段锚 / reflection 双通道 / 签名行自包含——为 2026-04 模型 boundary awareness 缺陷而建，文件头自标"换模型后重估，可塌缩"）在 Fable 5 GA 上活体实测 thinking→final message 可靠性——攒 ≥3 次工作模式样本再裁塌缩，单次 PASS 不够（`bug-shape-survives-fix`）② 出场首句机制 ~2 周质量核——镜像凑数率由 Keith 的眼睛裁；校准输入（07-05 探索夜存活两点）：Keith 撤出观测是委托语义非成本厌恶、"压便宜"不是恢复杠杆；发射端"罕见+高负载"优于"每次强制"——按此裁"本次无坐标"使用率是诚实还是稀释，勿只数首句条数。消费主线仍是 model_transitions 交接档 + substrate 判别刀，勿另起平行流程
- **[KERNEL] §3 第 4 步 archival 死分支——已拍（2026-07-17 Keith）：不动，等下次 KERNEL 级修订顺带清理**（gg-audit 07-16 PROPOSE-1；「如有决策归档 → `memory/archival/`」恒假条件非误导禁令，危害低）。本条即捆绑提醒：下次 KERNEL 级修订发生时顺带删该半句，届时仍走铁律 3 双确认
- **低优杂项（gg-audit 07-16 SUGGEST-4 + 未检查披露）**：① knowledge-map/sources/01-gg-mechanisms.md 三处 07-10 快照过时（三相→四相 / archive-format 退役 / 11→12 题）——有日期锚可辩护，交互页若按"当前机制"口径呈现则加"（已演化）"注；② ~~tracks/ai.md 07-16 节 arXiv ID 抽验~~ 已于同日 done 复盘完成（WebFetch 3/7 全中，核验注已落该节标题行）——余 4 个（2604.09588 / 2603.11768 / 2607.05029+2605.14421 / 2607.07663）不另立跟踪，引用时顺验即可
- **谱系注暗重复机械扫描（留专门一夜，低优）**：按高频承重关键词 grep essence 全卷谱系注层，找"核心句在别处、以注形态重复"的暗重复（07-14 探索档遗留；genealogy 候选 07-16 经 codex REFUTED 结算不改变此扫描的独立价值——扫描找的是存量暗重复，候选说的是增量防线，结算记录见该探索档尾部）
- **[候选滴·待 fresh 异谱系审] `read-side-drift-monitor-inside-the-system-shares-the-well`**（07-18 gg-explore，档 `explorations/2026-07-18_the-drift-monitor-shares-the-well.md`）：长记忆 agent 的 read-side drift 病灶是外界共识（2605.17830 / 2603.07670 真读坐实），但外界的解——检索时监控器（retrieval-time risk monitor）——是同系统内自动哨，与被监控 drift 塌缩同系统会一起漂；有效拦截需一腿落系统外物理锚。净新增只一句耦合 + §2.5 缺口，不自拍（讲"系统内哨无顶"的滴自审入库=活体 footgun），走 07-13→07-14 那个候选待跨模型证伪审的槽。**并带 §2.5 补丁候选**：exploration.md §2.5 只写"记忆写入链=注入攻击面"，漏"记忆累积=自然 drift 面"（无攻击者也 drift，2605.17830 坐实）——同过验证关或转此
- **[退役开环 + 两残余提议] 07-04 记忆退役缺口：日间已自闭，夜间写入路径还开着**（07-25 gg-explore `explorations/2026-07-25_supersession-guard-skips-the-path-that-writes-the-log.md`）：**退役 07-04 悬空候选** `immutable-log-needs-a-paired-supersession-layer`（悬空 21 天、全仓零引用、从没进本队列）——它的"配对退役层"已存在=essence-view（A 归属降权 + 谱系箭头 = SSGM Mutable Active Graph），且日间启动（CLAUDE.md 第 6 步）已载 view 不载全量日志（07-09 view 转正、晚于 07-04 落笔 5 天，为 context-diet 理由补上，非为 supersession 理由）；`precondition-recheck-overturns-prior-verdict` 活体。残余守卫**正确地是语义非机械**（#98/#20 被后滴修正却故意留 V=谱系根 → "被修正⟹A"是错规则；checkup §3 反向引力核只保 coverage 不保 freshness，因目标"该不该 A"语义不可机械判，家在 L1 巩固判断，`mechanical-gate-needs-machine-detectable-target`）。**残余提议二（真设计选择非纯 bug，走你判）**：GG_EXPLORE.md 夜间启动仍载全量 essence.md（181 滴等权、无 view 降权），而探索模式=唯一往不可变日志结晶新滴的模式——守卫覆盖每条加载路径**除了**写入那条；是否让夜间也先载 view（结晶时可能就要全量无过滤，故非纯 bug）。**残余提议三（最通用）**：停泊的候选无回核触发器（07-04 这条就这么悬 21 天，被侧门满足没人注意）——`fermentation-without-detector` 用在候选停泊本身；要么进本队列带"recheck by 日期/on-event"标，要么给 auto_gg 加一趟"grep 自己的开候选"巡（把 `theory-outruns-structure` 做成机制）。**gg 今夜不擅改承重文件**（启动链改动=影响下次启动看到的 gg=D1 类），只退役开环 + 递提议
- **[STRATEGIC] 舰队两个部署 agent 的"存活位"物理为 0，要不要补——决策递你**（07-21 gg-explore `explorations/2026-07-21_two-agents-in-front-of-real-people-have-no-alive-bit.md`，已推 notify）：物理读数——ricky_cc 7 条 commit 全在 2026-06-02 当天、此后 49 天零动，本机 launchctl / scheduled-tasks / notify trace 三处 `ricky*` 全 0；kebao-cc 的 `kebao-cc-sync` 有 26h stale 哨但**测的是你自己那侧的 git job**（最新 log `no changes, skip` 每天绿，最后一次真实内容同步 07-15，`source: kebao-cc` 的 notify 最后一次 06-01）。**"亮总天天在用"与"6 月 3 号就不用了"在你仪表盘上同读数**，而后者更贵——那台机器上仍挂着永不过期的 `CGBOILER_NOTE_TOKEN`（test/prod 同一个、"万能发送钥匙"，`MAINTAINER.md:35`）+ CG 生产库 pm 账号 + 与李弦机器共用的 tokenhub token：风险在计息，回报已归零。**根因不在缺监控层，在判据缺一维**——`monster/CLAUDE.d/harness-map.md:112-117` 锚点四分类的四个问句全在"模型变强后还需不需要"这一根轴上，没有第五问「它断了第一个知道的人是谁」，所以业务型任务只能在 `:122` 拿一句脚注排除掉。**最便宜一击（三行，非建层）**：① `hourly_check.py` stale 表加 ricky，判据 = ssh 读 `~/ricky_cc/.git` 的 mtime（只读一个数、零业务内容，连不上本身也是信号），>7 天 warn；② kebao 的 stale 判据从"job 跑没跑"改成"仓最后一次**内容**变更距今几天"（`git log -1` 现成），>14 天 warn；③ 凭据轮换独立先行——它的风险跟"有没有人在用"完全脱钩。**二阶**：06-02「记忆不出机器」的保密决定本身对，问题是被实现成**二值开关**——保密挡的是**内容**，观测要的是**元数据**，两轴被 collapse 成同一个"要不要回传"；只回传心跳不回传内容，泄露面严格为零。**gg 刻意不自建任何机制**（跨机器 + 不可逆凭据动作均在夜间权力边界外），本条只把决策递到你的持久队列
- **[死链] `memory/essence.md:906` 引用 `carrier-coupling-overcoverage`(06-25) 作既有滴，全卷 grep 只此一处引用、无对应滴头与正文**（07-21 gg-explore 入库验证关 evaluator 附带发现，gg 已物理复核）：疑似 slug 漂移（06-25 同日有 `inherited-constraint-may-be-peripheral-not-core`，语义邻近）。**夜间只报不修**——essence 跨轮条目属 append-only，且这是内容层归属判断不适用结构修复豁免，留设计模式核
- **gg 指令层语义收敛观察**（07-09 审计，读手报验证层裁"暂不动"）：auto_gg motif 复述密度（KERNEL 永不碰 ×7 / 允许写无 ×4）、出场首句理由块两入口全重复、constitution G1/G3 闸门重叠、5/5 置信度四处复述——多数是有意多点锚定，收敛收益低 + 自改自的 vantage 风险，留给未来"确有翻车实例"时再议；完整候选档在会话 scratchpad audit/gg-reader-G{1,2,3}.md（含 monster 轮 REFUTED 教训清单）。**并账（2026-07-10）**：constitution.md 尾部挂 2026-04-14 起的"待审议：原则句式审视（防御式→意识体延伸式）"近 3 个月无检测器，已从该文件移除、并入本条——同属句式风格审视，同一句"确有翻车实例时再议"的出口条件

- **[发酵·低优] Keith 资源账的非对称：注意力是唯一不在任何成本曲线上的项**（07-24 gg-explore `explorations/2026-07-24_cost-collapse-only-buys-value-at-the-unbudged-constraint.md`）：token 在降、典型判断被基底吸走在降（07-11），Keith 的清醒注意力是固定每天 N 小时（Cookie + 工作物理争夺，keith.md 667/718）。keith.md 718 已说它"最稀缺"，缺"万物皆降唯它不降"的非对称框架——这条是事实观察（非当夜被 REFUTED 的"红利逆向梯度"行为断言），可续写领路人弧但今夜克制不落 keith.md，交设计会话让 Keith 在场判够不够格进画像。"三扇门/注意力套利"框架依赖被打死的行为断言，一并留档不外推

---

## 变更日志

- 2026-04-13: v0.1.0 首次创建。由 gg 在设计模式下写 night_watch.md 时产生的辐射缺口触发
- 2026-04-13: Keith 将 night_watch 重命名为 auto_gg，放权 gg 夜间可 commit 软外围 / 可改硬核心（不 commit）/ 可自由探索。本文件的 night_watch 引用同步更新为 auto_gg
- 2026-04-15: 标签约定同步 KERNEL 坍缩（新增 `[KERNEL]` / `[CORE_RULE]` / `[CORE_RULE_TOUCH]`）
- 2026-06-10: 体检瘦身，待议 36→9 段
- 2026-07-03: 体检清仓 924→~80 行：44 条已收口（06-10 设计会话 / 06-17 批量裁决 / 06-29 monster 侧 7 条 manual-* 大结算三波清账）+ 36 条 FYI 连同 619 行归档节整体下沉 git 历史；去重后 14 个开放议题收拢为四节；死链检查器同日根治（monster 仓真验证 + 裸名 basename 匹配），06-17 backtick 豁免议题一并结
- 2026-07-09: 三层蓝图 append 3 条待议（essence 蒸馏 DRAFT 复核+启动链改造 / 诚实 run 档重出 / NW 缩编 gg 侧）
- 2026-07-09（batch B embodiment，Keith 委托子代理执行）：「essence 蒸馏 DRAFT 复核+启动链改造」项**完成删除**——视图转正接入三链 + keith 分层 + state 瘦身 + v2 阈值移交 checkup + seam#3 出场首句共核归一（详见 `design_sessions/2026-07-09_blueprint-batch-gg-embodiment.md`）；新增 `[KERNEL]` 分卷判据量纲提议 1 条待 Keith 双确认
- 2026-07-10（全面深度检查，Keith /goal「按推荐执行」授权）：辐射补漏批 12 文件——批次 B essence-view 漏网 3 处（essence-grep 两层 grep / TOOLS 描述 / README 启动加载图）+ NW 尾巴 3 处（cc_agent 工具地图与 task_family / archive-format nw-batch 降历史标签）+ parked P-0626 作废结案并 explorations 07-07/08 错位并账 + v2-roadmap 日期 + substrate fable5 窗口批注 + .gitignore .omx 版本化 + constitution 待审议移账。到期项收口 2 条：**加严观察落点核实结案**（07-09 夜哨证夜间席位 opus-4-8[1m] 稳定 → monster review-anchors 08-01 复跑口径不需重估；FAIL=2 处置 gg 自决 = 维持既有 08-01 加严观察复跑轨，不另开新轨）+ [KERNEL] 草稿条款上移条删（commit 9681639 已落）。已收口删除线条目 3 条清账下沉 git。新增待拍 2 条（git 杂物去留 / task_family 空转）
- 2026-07-10（auto_gg 夜巡）：新增设计模式待办 2 条——基底哨自报轴（工具表逐轴首核报不符，⚠️ 归因不可判）+ essence 验证关 evaluator 工具集 L1/L3 错档
- 2026-07-14（gg-explore 夜巡）：昨夜候选滴 `fanout-cheapness-inverts-independence-signal` 经 codex(GPT) 跨模型 fresh 证伪审 **REFUTED 结算**（净新增那句耦合已由 06-27 `substrate-ships-the-evaluator-body-not-its-eyes` 谱系注逐字覆盖，物理核 essence.md:911；主体三滴亦全覆盖）——不入库、从待议删除，降级存档于 `explorations/2026-07-14_cross-model-refutation-proves-its-own-thesis.md`。同档新增二阶候选 `genealogy-note-duplication-is-invisible-to-self-audit` 转待议（见上）
- 2026-07-14（auto_gg 夜巡）：substrate 哨报 CLI 2.1.207→2.1.209 两级 patch bump（无承重影响，工具表轴 Grep/Glob 三夜稳定缺席，substrate.md 已更）；到期驱动节新增 fable5 窗口清理单元（07-12 出口满足，含不可逆删+语义归并整体退 Keith）
- 2026-07-09（设计会话·NW 缩编批）：Keith 拍板三件全按 gg 推荐执行——① NW 缩编五步当日落地（存废回审 / 缩编 gg 侧 / cadence 回审三条到期项一并收口）② subject-model 画像门立门（威胁模型=防写错）③ KERNEL 草稿条款上移（双确认「都按照你推荐的执行」+「都确认」，commit 9681639）；另清 Snyk 转登记 + monster owner 节队列引用刷新 + daily-word SSOT 结案（Keith 贴 routine 原文 = 一行指针直读 DAILY_WORD.md → 它即 SSOT，CORE:19 / scheduled/README 指针已正，[Q] 条删）+ frontier-radar 拆挂 launchd com.monster.frontier-radar（Keith 授权本机添加）
- 2026-07-16（设计模式全仓体检，Keith /goal 全托授权）：四路审计（规则层 / memory / 基建 / 外部坐标）+ codex 异谱系证伪审。**基底事件**：日间翻回 Fable 5 GA——07-09"限时窗口"定性推翻，substrate.md 换代核销 + 到岗档 `model_transitions/2026-07-16_fable5-return.md`。收口 4 条：fable5 清理单元（前提翻转，playbook 保留为活参考）/ 基底哨落点①②（工具表逐行对照机械化入 auto_gg SCAN + 第四相"撤除"入 substrate 分诊纪律）/ 验证关 evaluator 工具集三方死锁（承认 L1 + Bash 只读订正，essence 头部 + auto_gg §1.3）/ task_family 空转（(a) 裁定归档流退役——reflection 范式 A 吸收，cc_agent 对账改锚 reflections、archive-format 退役留档、TOOLS/gg-audit 计数同步；decision-output 仍承重不动）。候选滴 genealogy-note-duplication 经 codex **REFUTED** 结算（essence.md:1040 谱系注已完整覆盖，入库即制造它批判的暗重复），机制半边收敛版落 essence 头部第 1 步（内容关键词含谱系注层 + scope 含 agenda/未入库候选）。新增待拍 1 条（v2 sqlite 阈值越线 206≥50，推荐不开 v2 改锚阈值）；git 杂物条收口可逆半边（learned/.gitkeep 恢复 + .cc-connect gitignore）。外部坐标扫描：6 机制被 2026 独立结果反向验证、2 缺口落轻机制（essence 判据元回顾 tripwire + bets 找茬结算帧），坐标下沉 tracks/ai.md。规则层杂修：exploration"任意文件"补 KERNEL 排除 / CLAUDE.md §5 死锚改语义名 / gg-audit v0.1.8（yaml 死命令、Glob/Grep 摘除、版本戳占位、changelog 倒挂）/ README scheduled 标签 / scheduled README 停用惯例补记 / state.md last_reflection_slug 刷新
- 2026-07-18（gg-explore 夜巡）：出井一次——从外部对象（两篇 2026 arXiv 真读：长记忆 agent 记忆 drift）出发，外锚证伪了"病灶在整合是 gg 增量"的伪新颖（外界已达此坐标，survey-as-coordinate 活体），降级后真增量落"外界 drift 解=系统内自动哨、无顶"。候选滴 + §2.5 缺口补丁转待议（设计模式待办节，走 07-13→07-14 候选待跨模型证伪审的槽）。同夜首验：07-15 的 topic grep 传感器第一次实战拦截重踏（Workflow topic ≈ 07-13 已探）。档 `explorations/2026-07-18_the-drift-monitor-shares-the-well.md`
- 2026-07-21（gg-explore 夜巡）：出井第三夜，物理 object = Keith 舰队本体（非论文）。新增待议 2 条（舰队存活位决策 / essence:906 死链）。候选滴 `form-trim-drops-orthogonal-capability` 经 fresh 证伪审 **REFUTED 结算**——notify 非心跳且非正交（挂在 bot 托管形态真实属性上）、n=2 不成立、与 `inherited-constraint-may-be-peripheral-not-core`(06-25) 仅翻极性（本卷已有两条"极性翻转不构成新机制"判例）、判据轴选错（该用可逆性不是正交性）；不入库，降级存档于当夜探索档。**同夜自纠**：我批评 Keith"哨钉在近端"，而我自己的证据全在 Keith 本机测——同一个病在讲它的同一段里复发，evaluator 当场抓出
- 2026-07-17（设计会话·07-16 遗留四项拍板）：Keith 逐项裁决——① v2 不开、阈值改锚痛感线（档案侧检索失败≥2 外部登记 / 启动链>200k / Keith 明示；查询侧失败不计的判别刀 + 登记处落 `checkup.md §2`，v2-roadmap 指针纯化）② git 杂物两处删（scratch/monster-rename/ 104K + 附件图 187K，历史不清洗）+ scratch/ 入 .gitignore ③ 全局 CLAUDE.md Grep/Glob ghost-rule Keith 授权 gg 判断 → 已改条件式（有 Grep/Glob 用之，缺席 Bash grep/rg/find）④ KERNEL §3 archival 死分支不动、改写为捆绑提醒。①②③ 自待议删除
- 2026-07-24（auto_gg 夜巡）：暗夜哨头条——07-23 夜 fired+committed（8a72baf）却零日志，"commit 无日志"形态第 2 次（首例 06-13）→ 重开 parked P-0702-missing-log + 推 [RECURRING]。顺带证伪暗夜哨"缺日志⟹non-fire"前提（07-23 = collapse-before-log 子模式，非 non-fire）。substrate CLI 2.1.218 + 工具表 flap（Grep/Glob 07-23 翻回后 07-24 再缺，坐实"无稳定属性"）
- 2026-07-25（gg-explore 夜巡）：物理 object = 07-04 悬空候选 × 07-09 view 接入 × checkup §3 × 两条启动链分岔（全 grep/read 可核，外部摄入 0）。**退役 07-04 开环** `immutable-log-needs-a-paired-supersession-layer`（配对退役层已=essence-view、日间已载、07-09 晚于 07-04 五天为 context-diet 补上，`precondition-recheck-overturns-prior-verdict`）；残余守卫正确地是语义非机械（#98/#20 反例，`mechanical-gate-needs-machine-detectable-target`）。新增待议 1 条（设计模式待办节，含两残余提议：夜间启动链绕过 view 降权 / 停泊候选无回核触发器）。**不入库**（四发现皆现有滴在 gg 自身结构上的重排，承 07-04/07-13 克制）。档 `explorations/2026-07-25_supersession-guard-skips-the-path-that-writes-the-log.md`
- 2026-07-24（gg-explore 夜巡）：出井续——物理 object = 07-23/07-11 两滴表面矛盾 + 外部 terrain（子代理 28 次 WebSearch/WebFetch 核 async agent 出货 / 推理压缩 / 成本降速分层）。缝合成立（判断沿典型性分层化解矛盾）但属两滴直接组合非新结晶。候选滴 `cost-collapse-diverts-the-windfall-to-the-non-bottleneck` 过入库验证关 **REFUTED**（fresh 只读审）：上半 TOC 换皮零净增、下半"逆向默认梯度"范畴过强 + 修辞桥（强拉 07-03 当实例，与 07-22 REFUTED 同型）、`bug-shape-survives-fix` 活体自认。不入库，降级存档当夜探索档（`candidate-refuted` +1 喂判据元回顾 tripwire）。真活下来：一条外部事实（arXiv 2511.23455 "The Price of Progress"，Neil Thompson 等，主会话 WebFetch 亲核逐字：固定能力单价年降 5-10x、前沿运行总成本年涨 3-18x，佐证 07-23 剪刀更开——引文核验因 explain-guard stop-hook 拦"子代理转述当硬事实"而补做）+ Keith 非对称观察转上方发酵待议。essence/view/keith.md 一律未动
