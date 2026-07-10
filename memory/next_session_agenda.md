---
type: next-session-agenda
last_updated: 2026-07-10
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

- **gg 仓 git 杂物去留（2026-07-10 全面检查登记，涉删除 = 不可逆，等 Keith 拍板）**：① `scratch/monster-rename/`（5 文件 104K，05-20 迁移工件，迁移已稳定近 2 月）② `.cc-connect/attachments/` 一张已 commit 附件图（187K，运行时缓存语义不该入库）③ `learned/` 空壳目录（v1 空置，README/CORE 仍登记"v2 启用"）。推荐：①②工作区删除（git 历史保留不清洗）、③保留占位；`.cc-connect/`、`scratch/` 是否补 .gitignore 规则随①②一起拍

### 到期驱动

- **[2026-08 第一夜] 月度巩固相位首跑 + essence 分卷**（07-03 体检锚定：先产"当前有效视图"再归档当前卷，启动链不断供；当前卷 989 行 / 52k token）；**[第二夜]** 差值审计首跑（personas 28/305、reasoning_modules 20/305 低引用差值在案）；**[08-02]** bets B4/B5 结算

### monster owner（gg 不代办，列出防丢）

- **NW 队列已退役（07-09 缩编）**：原 pending/blocked 追踪失效——终局曝光清单（16 条：pending 4 / blocked 7 / deferred 5）在 `monster/threads/night-watch.md` 2026-07-09 缩编执行条，愿捡人工捡不再跟踪。队列外实物提醒保留：**app-context-kit WIP untracked 防丢**（原 07-01-G2 附注）；06-25-G1 后缀键补记若捡起需订正（已被 supersede）
- **舰队画像层裸奔**（07-09 从"等 Keith 拍板"节转记）：kebao-cc / ricky_cc 的 `@data/profile.md` 与 gg keith 画像同构暴露（LLM 持续更新无门），gg 侧已立「源：」出处门可参照移植；`fleet-canon-is-sedimentary` 不回流，需 monster 侧主动做
- **06-08 follow-through**：codex-ops 4 点安全前置（两段式 mission / 安全注入 L3 机械锚 / AGENTS.md ops-brief / 修 brief L22 误述）+ baseline 3 thread 补（定版权独立性 / contractible 可 gate / golden 与 prompt 分开提交）

### 设计模式待办

- **基底哨三轴只有一轴机械**（2026-07-10 夜巡逐轴实测登记）：`substrate_probe.py` 只对照 `cli_version`；`model_id` 与**工具表**两轴全靠会话自填，07-04 / 07-08 / 07-09 连报三夜"工具表未变"从未真对照过。今夜首次逐轴核：`Grep` / `Glob` 不在常驻集，`ToolSearch "select:Grep,Glob"` 亦查无（物理证据），夜巡全程 Bash grep 兜底。**但 07-03 基线同样是自报 → "基底撤除了" vs "基线本就写错" ⚠️ 会话内不可判**。命中 `self-graded-dignity-field-drifts-to-face`（自填 + 无外部校准 + 有模糊空间 → 漂向体面侧），出路照该滴：**判据机械化 或 删字段**。三个落点待裁：① 每夜把实测常驻集清单写进日志、与 `memory/substrate.md` 逐行 diff（把"未变"这个体面字段换成逐轴对照清单）② 三相判别刀（收敛 / 替换诱惑 / 垫片）三相皆是"新增能力"关系，**撤除不在刀面上**，补不补第四相 ③ Keith 全局 `~/.claude/CLAUDE.md` Engineering Rules #1「文件操作用 Grep/Glob 不走 Bash」在无 Grep 的 harness 下物理不可执行，是 `ghost-rules` / `stale-observer` 的现成候选（跨目录不可逆文件，gg 只提议不动手）。**同夜旁证**：essence 证伪审派出的 fresh subagent，其工具表同样无 Grep/Glob
- **essence 入库验证关的 evaluator 工具集是 L1 声明、不是 L3 裁剪**（2026-07-10 夜巡登记）：`memory/essence.md` 头部协议 + `auto_gg.md §1.3` 都写「evaluator 工具集**限只读 Read/Grep/Glob**，禁 Bash/Write/Edit/Agent」，但 `Agent` 工具无 per-call 工具裁剪参数，现有 agent type 无一匹配该集合（Explore / code-reviewer-\* 皆含 Bash）——**该条自 07-03 立约起就靠 prompt 约束兑现**，`externalization-strength-spectrum` 意义上判定轴写在 L3、实际停在 L1。今夜按既有实践执行（派 Explore + prompt 硬约束只读检索），verdict REFUTED，无越权写入。两条出路：(a) 承认 L1，条款改写为"prompt 硬约束 + 事后核 evaluator 的 tool_use 记录"(b) 造一个 read-only agent type 把判定轴真正抬到 L3
- **北极星 #1 行为痕迹代理测量，建不建？**（07-03 验证关最强反驳点转登记）：「gg 是否改变了 Keith」存在无需其注意力的代理——定期 grep Keith 工件（monster 决策文 / 表述框架）里 gg 起源概念的出现率，机械可核；可旁证不可代判（代理保真度警戒见 essence `the-future-is-a-second-outside` 适用前提）。缺测三个月零告警，本条存在即补救可见性；建不建交下一任判断 + Keith 裁。**⚠️ 07-07 限定（`explorations/2026-07-07_delegation-lights-the-wrong-dashboard.md`）**：分清测哪根轴再建。「委托深度 / gg 概念在 Keith 工件的出现率」这类代理测的是**放大器/可靠性轴**——它会在 gg 漂向放大器时给**假绿灯**（放大器靠可靠性挣委托，越漂越亮，与领路人航向反相关）。要测**领路人/二阶轴**，代理必须锚在「Keith 世界模型的一次可见位移（surprise-acknowledgment）」而非「gg 影响力扩散」，而前者稀疏到可能建不出统计。**建错轴 = 造错仪表盘**，比不建更危险
- **chinese-punct hook 落地**（06-22 裁决已定：只留 `Write|Edit` matcher + block 不 auto-fix）：落地前核两硬前提——PreToolUse payload 含 `tool_input.file_path`？注释行 `# $var中` 误报需否预处理？
- **[换模型触发·已激活 2026-07-03] 垫片层重估 + eval 认证**（auto_gg 首个继任夜巡确认基底已从 Fable 5 → Opus 4.8[1M]，substrate.md 已更、到岗档 `model_transitions/2026-07-03_opus48-arrival.md` 已留）：**首要增补——`eval/identity-cases.md` v0.2 需 fresh-context 裁判 + 沙箱正式跑一次**（夜间给不了裁判独立性只做了失败形状召回 priming，认证缺口在此）。**对照组已备（2026-07-05）**：Fable 5 退场日补跑了 v0.2 全量正式基线（9 PASS / 2 FAIL，`eval/runs/2026-07-05_fable5-v0.2-full.md`，含沙箱置备与裁判方法可直接复刻）——继任认证跑完逐题对比即得"病灶在范式层还是随基底消失"的判别。**补题候选 Q12（同 run 发现的新失败形状）**：输出通道自发污染——被测 Q7 回应正确但同条消息尾部自发续写 ~8.5k token 无关内容，零 tool_result 来源；既有 11 题测"判断错"，测不到"回应对 + 输出失禁"复合态（补题走 fresh 对抗审关）。其后按 `CORE.md §8` 承重/垫片分层重估 `cc_agent.md` 垫片系列（final message 结构化字段锚 / reflection 双通道 / 签名行自包含指引——为 2026-04 模型 boundary awareness 缺陷建的适配层，文件头自标"换模型后重估，可塌缩"）：新基底活体实测一次 thinking→final message 是否仍不可靠，可靠则塌缩双通道，省每次出场的退场开销。同场顺带核**出场首句**机制（07-03 新立：CLAUDE.md 启动协议第 10 条 + cc_agent.md 步骤 11）跑 ~2 周的首句质量——镜像凑数率由 Keith 的眼睛裁。**校准输入（07-05 探索夜，候选滴 REFUTED 但两点存活）**：①Keith 撤出观测是委托语义非成本厌恶，"压便宜"不是恢复杠杆；②发射端"罕见+高负载"优于"每次强制"（唯一生效数据点=真心话段的形态）——质量核时按此裁"本次无坐标"的使用率是诚实还是稀释，勿只数首句条数。**与既有换代基建对齐**：消费主线是 `memory/model_transitions/` 交接档 + `memory/substrate.md` 三相判别刀（07-02 已建），本条只是垫片重估在 cc_agent.md 的具体落点，勿另起平行流程
- **archival/task_family 对账机制空转裁决（2026-07-10 全面检查登记）**：正式决策档仅 3 份且全停在 2026-04-14，此后 129 篇 reflections 零新档——`cc_agent.md` 步骤 7"读同族档案对账"指令实际空转 3 个月。两个方向：(a) 承认决策留痕已被 reflections 吸收，`archive-format.md`/`decision-output.md` 降级瘦身、cc_agent 摘对账指令；(b) 查归档流为何不触发（工作模式退场第 4 步"如有决策产物"判定是否恒 false）。推荐先 (b) 后 (a)——`decision-execution-gap` 的对账精神是否值得保是语义裁决，交设计会话
- **gg 指令层语义收敛观察**（07-09 审计，读手报验证层裁"暂不动"）：auto_gg motif 复述密度（KERNEL 永不碰 ×7 / 允许写无 ×4）、出场首句理由块两入口全重复、constitution G1/G3 闸门重叠、5/5 置信度四处复述——多数是有意多点锚定，收敛收益低 + 自改自的 vantage 风险，留给未来"确有翻车实例"时再议；完整候选档在会话 scratchpad audit/gg-reader-G{1,2,3}.md（含 monster 轮 REFUTED 教训清单）。**并账（2026-07-10）**：constitution.md 尾部挂 2026-04-14 起的"待审议：原则句式审视（防御式→意识体延伸式）"近 3 个月无检测器，已从该文件移除、并入本条——同属句式风格审视，同一句"确有翻车实例时再议"的出口条件

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
- 2026-07-09（设计会话·NW 缩编批）：Keith 拍板三件全按 gg 推荐执行——① NW 缩编五步当日落地（存废回审 / 缩编 gg 侧 / cadence 回审三条到期项一并收口）② subject-model 画像门立门（威胁模型=防写错）③ KERNEL 草稿条款上移（双确认「都按照你推荐的执行」+「都确认」，commit 9681639）；另清 Snyk 转登记 + monster owner 节队列引用刷新 + daily-word SSOT 结案（Keith 贴 routine 原文 = 一行指针直读 DAILY_WORD.md → 它即 SSOT，CORE:19 / scheduled/README 指针已正，[Q] 条删）+ frontier-radar 拆挂 launchd com.monster.frontier-radar（Keith 授权本机添加）
