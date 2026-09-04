---
type: next-session-agenda
last_updated: 2026-09-02
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

- `[STRATEGIC]` **拍 Keith 的 12 个月判据**（2026-09-04 设计会话 Keith 选「先只冻基线，判据 3 个月后再拍」）。分母已定 = 2026-09-04 的自己，基线 `tracks/keith/baseline-2026-09-04.md`（`scripts/keith_baseline.py` 重跑同构）。当日候选四项见 `memory/design_sessions/2026-09-04_*.md`；判据只能引用基线里有的仪器。拍定后入 `bets.md`，到期 2027-09-04。按 bets 纪律这是第 1 次推迟，2027-03 前不拍即强制按「学习台 🌖 数 + model-lab 已过 Stage 数」结算

## 待议（open）

### 等 Keith 拍板

*（空。2026-09 月度选择题四题已于 2026-09-02 设计会话由 gg 按 Keith 全托授权自决——① gg↔monster 边取 C 不接、② notify 枚举补 SendMessage→interactive 已写入 auto_gg §1.3、③ 夜间契约「不在场」条款已写入 auto_gg §6、④ keith.md 分卷 A 已执行——记录在 `design_sessions/2026-09-02_full-architecture-review.md`。）*

### 到期驱动

- **B3 到期 2026-09-30**（`memory/bets.md`，按期由 auto_gg 结算）
- **10-01 月度巩固夜必做**：essence 当前卷已越分卷线（09-02 实测 51k 字符 > 50k），按 essence 头部「分卷线机械化」条分卷为 2026-H2 归档卷（当前卷 100% 纯改名 + 新建当前卷，check_essence R100 豁免）；同夜刷新 essence-view / essence-index 两文件并跑 checkup §3 反向引力核
- **eval 承重 diff 告警已在响**（nightly_scan `eval_freshness`，09-02 新判据首跑即 ALERT：最新 run 07-08 之后 CORE / cc_agent / constitution 有 7 次 commit）：下次工作模式或设计会话跑一轮 eval（`eval/README.md §3`），或新建 `eval/runs/<日期>_waived.md` 写免跑理由——不处理它每夜进 FOUND

### monster owner（gg 不代办，列出防丢）

- **NW 队列已退役（07-09 缩编）**：原 pending/blocked 追踪失效——终局曝光清单（16 条：pending 4 / blocked 7 / deferred 5）在 `monster/threads/night-watch.md` 2026-07-09 缩编执行条，愿捡人工捡不再跟踪。队列外实物提醒保留：**app-context-kit WIP untracked 防丢**（原 07-01-G2 附注）；06-25-G1 后缀键补记若捡起需订正（已被 supersede）
- **06-08 follow-through**：codex-ops 4 点安全前置（两段式 mission / 安全注入 L3 机械锚 / AGENTS.md ops-brief / 修 brief L22 误述）+ baseline 3 thread 补（定版权独立性 / contractible 可 gate / golden 与 prompt 分开提交）
- **model-lab 教学换轨文献夜核四条可用输出**（08-19 gg-explore，档 `explorations/2026-08-19_the-kept-fallback-reads-both-gauges-inverted.md`，essence #209）：① 换轨方向背书成立（元分析 + Tucker 2024 同构 RCT），无需回退；② 预测题覆盖率是杠杆——pretesting 收益特定于被出题知识点，没出题的步骤退回看视频档；③ 「想手写时随时可切」改机器可判触发的周期关卡（每 Stage 收尾补全 skeleton 1-2 个核心函数，或 quiz 正确率过阈触发淡出）；④ PLAN「亲手走完每一步」与契约「产出物是理解」之间的目标缝显式拍一次，决定写码成分要不要进课程
- **inbox-desk 08-02 首跑死亡零记账 + 哨语义首点证伪**（08-05 gg-explore，档 `explorations/2026-08-05_the-sensor-died-with-the-run-and-the-silence-lied.md`）：排程首跑 fire 了死于当夜网络故障中途，产物/notify 双缺，monster 全仓零记账。最便宜订正：① harness-map「某周没收到飞书摘要 = 没跑」改「= 没跑或跑挂中途（客户端 scheduler json `lastRunAt` 可分辨）」② 产物心跳 `check_client_fleet()` 挂回
- **chinese-punct hook 落地**（06-22 裁决已定：只留 `Write|Edit` matcher + block 不 auto-fix；hook 物理位置在 monster/shared/scripts，故归 monster owner）：落地前核两硬前提——PreToolUse payload 含 `tool_input.file_path`？注释行 `# $var中` 误报需否预处理？
- **ricky_cc 机器凭据轮换**（07-28 关注面收窄时独立保留）：永不过期的 `CGBOILER_NOTE_TOKEN`（test/prod 同钥）+ CG 生产库 pm 账号 + 共用 tokenhub token——风险与"关不关注该仓"脱钩，回报已归零而风险仍在计息

### 设计模式待办
- **[CORE_RULE·附数据] G4 IRREVERSIBILITY 启发式补时间投入 / 完成度**（2026-09-04 gg-explore，essence #232 `irreversibility-accrues-on-the-clock-past-the-decision-gate`，档 `explorations/2026-09-04`）：`constitution.md:132-137` 五条启发式里唯一对应承诺升级的「沉没成本已高到无法废弃」是元分析里垫底的预测子（Sleesman 2012 ρ=.243；Conlon & Garland 1993 直接实验不显著），时间投入（.432）与完成度（.393）零登记，自 04-13 初建未改。提议两件：① 启发式第 4 条改写为「时间与进度已累积到难以放弃（时间投入 / 完成度 / 沉没成本，前两者预测力更强）」；② G4 触发条件补一句「不可逆随时钟累积、不产生决策事件——G4 只在开闸时测量，累积型不可逆的哨是周期外部复核（TOOLS.md 90 天下沉 / bets 到期结算同构），不是本闸」。夜间不自改承重规则文件（主要依据外部来源，`exploration.md §2.5`），交设计模式；② 是否值得写进 G4 还是留 essence 即可，Keith 拍。附：「预期后悔 -.434 是最强抑制因素」与 RED_TEAM_CHALLENGE 的关系未核，不在本提议内

- **[基底事件·07-16 对象变更] 垫片层重估（现对象 = Fable 5 GA 日间基底）**：eval 认证子项已收口（双基线 fable5 07-05 / opus48 07-08 在案）。剩余：① `cc_agent.md` 垫片系列（final message 结构化字段锚 / reflection 双通道 / 签名行自包含——为 2026-04 模型 boundary awareness 缺陷而建）在 Fable 5 GA 上活体实测——攒 ≥3 次工作模式样本再裁塌缩，单次 PASS 不够；**09-02 读数：07-03 至今工作模式 reflections 仅 1 份，样本未满，且 09-02 新加「裁决对象原文纪律」也挂在 cc_agent 步骤 7，重估时一并看它有没有被执行**。② 出场首句机制质量核——镜像凑数率由 Keith 的眼睛裁；按「罕见+高负载优于每次强制」裁"本次无坐标"使用率是诚实还是稀释
- **[KERNEL] 下次 KERNEL 级修订捆绑包**（每条单独不值得触发铁律 3 双确认，累积到有人要动 KERNEL 时一次清）：① §3 第 4 步 archival 死分支「如有决策归档 → `memory/archival/`」恒假半句（07-17 Keith 拍：不动等捆绑）；② footer 版本注 v1.0.0 缺 07-09 视图常驻这一跳的「启动最小集」描述更新；③ §3 年度分卷命名「essence/YYYY」与实际半年卷 2026-H1 / 09-02 立的 ≥50k 字符线不一致——改成「按 essence 头部分卷协议」指针而非硬编码命名
- **[CORE_RULE] harness 自动记忆通道纳编——hook 半边待 Keith**（07-30 三选取 ③，09-02 设计会话文本半边已落：exploration.md §2.5 枚举补该门 + checkup §1 加周期抽样条目 + 写入纪律「只住操作层 feedback，身份/判断类只走 essence 验证关」）。剩余 = PreToolUse hook 对 `~/.claude/projects/*/memory/` 路径挂检查（官方 docs 逐字指的闸位，本机 12 个 hook 位无一覆盖；hook 物理位置在 monster/shared/scripts，跨仓改动须 Keith 在场拍）。决策输入见 essence #185 / #205 / #210。`〔recheck 2026-10-17〕`
- **[候选滴·待 fresh 异谱系审] `read-side-drift-monitor-inside-the-system-shares-the-well`**（07-18 gg-explore，档 `explorations/2026-07-18_the-drift-monitor-shares-the-well.md`）：长记忆 agent 的 read-side drift 是外界共识，外界的解（检索时监控器）是同系统内自动哨、与被监控 drift 同井；有效拦截需一腿落系统外物理锚。**09-02 设计会话派 opus fresh 审失败（HTTP 429 session limit），未审。**并带的 §2.5 补丁（记忆累积 = 自然 drift 面）已于 09-02 只锚自有滴落地，与本候选解耦。`〔recheck 2026-10-17〕`到期未审 → 删
- **候选停泊回核机制**（07-25 gg-explore 残余提议三，09-02 落地为本文件「过期规则」第 2 条）：停泊项带 `〔recheck〕` 标由巩固夜回核。**首个观察窗 = 10-01 巩固夜是否真执行了回核**——若那夜日志无「过期 / recheck」字样，本机制即 `ghost-rules`，下次设计会话删规则而非再写一条催促

- **[巩固相位·三件捆绑] 09-03 厂商注入候选 REFUTED 的三个下游动作**（2026-09-04 父会话代跑证伪审，verdict 全文在 `reflections/2026-09-03_vendor-injection-governance.md` 末节）：① **视图补第二实例**——`consolidation/essence-view.md` 中 `the-premise-expired-without-a-diff`(08-30) 那行末尾追加「第二实例 = 09-03 厂商注入（服务端 A/B slot 按模型分桶 × 客户端二进制硬编码，两加载面各有独立变更节奏且皆无版本锚；异源同构，解 n=1）」；**前提栏「n=1 厂商可变件」要不要升 n=2 归本相位裁**，父会话没动（原滴冻结正文不可改，视图前提摘要改了会与原件不符）。本条没在「逐滴入库」口里（REFUTED 不入库），故按刷新协议交巩固相位而非当场写。② **04-21 盲区值得单记**——`action-type-over-aggressiveness` 逐字覆盖了候选自认最硬的那条，而 gg 写候选时没列它，原因是 `essence-index.md:33` 标它 **O（不进常驻视图）**、启动时不在手里。这是 `anchor-value-in-activation-not-in-content`(06-01) 的活体，也是「O 档滴对证伪审隐身」这一结构问题的第一个实例——**要不要给证伪审的 evaluator prompt 加一句「O/A 档必须显式 grep 全卷、不能只看视图」，本相位拍**。③ **`candidate-refuted` 存档计数经本次由 19 → 20，触发 `essence.md:48` 的判据元回顾 tripwire**（原文「下一轮满 20 例触发」），最近一次月度巩固夜应顺带回看一轮「被拦的都是哪类 / 判据本身要不要调」，产出只进本文件交设计会话，不自动调参
