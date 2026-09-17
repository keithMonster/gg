# substrate — 基底快照（基底哨的对照面）

> auto_gg SCAN 段的基底哨（`scripts/substrate_probe.py`）对照本文件的 `cli_version` 字段。
> 任一轴变化 → 三相判别刀分诊（`substrate-capability-triage-three-relations` 2026-06-20）→ 写 FOUND + 更新本文件。
> **`model_id` 轴变化额外动作**（2026-07-02 起）：读 `memory/model_transitions/` 最近一份交接档（继任者第一课）+ 跑 `eval/identity-cases.md` 身份基线；更替可预知时由退场基底提前留档。
> 历史不留在本文件——git log 即变更史（`toolset-is-the-changelog` 2026-06-23）。

cli_version: 2.1.274 (Claude Code)
model_id: claude-fable-5[1M]（2026-09-17 本夜会话声明；launchd plist 请求 fable/effort=low，配置请求值不冒充服务端实际 model_id）
updated: 2026-09-17（**回迁 CC**：09-17 16:11 commit 6e3c8d1 三 plist 模型分档 + run-task-and-push.sh 换回 exec gg run-task.sh；本夜启动日志 23:35:06 model=fable、watchdog 正常 tracking。substrate_probe 观测对象与运行器重新对齐——09-15 失配前提消解，P-0915-substrate-target 状态更新见 parked。cli 2.1.272→2.1.274 单级 patch bump，四相分诊 = 无承重影响的版本演进。工具表自核：本夜 18 项直接工具与 09-12 快照逐行一致（Grep/Glob 仍缺席，Bash 兜底）。model_id 轴回到 fable 谱系，最近交接档 2026-07-16_fable5-return.md 即对应档。）
updated_prev: 2026-09-15（当前运行器 Codex，codex-cli 0.154.0-alpha.6.2；model_id 声明 GPT-6、launchd 请求 gpt-6-astra/high。迁移 commit 7b8f087。该轴两日后被 09-17 回迁 CC 取代，保留作迁移窗口史。）
updated_prev2: 2026-09-06（auto_gg 夜巡：CLI 2.1.261→2.1.263 两级 patch 跳（四相分诊 = 无承重影响的版本演进，快照更新即毕；monster 晨报同日报 A 面 `tengu_heron_brook` 尾部第二段变体，属服务端 slot 非 CLI 版本、gg 承重层零引用）。工具表两轴自核：常驻 11 项与 09-05 快照逐行一致；deferred 15 项一致；Grep/Glob No matching——缺席延续（07-24 起，未见复现）。夜间 model_id 自核 claude-fable-5-1，与快照一致）
updated_prev3: 2026-09-05（auto_gg 夜巡：CLI 2.1.260→2.1.261 单级 patch bump。工具表两轴自核：常驻 11 项与 09-04 快照逐行一致；deferred 15 项一致；Grep/Glob No matching——缺席延续（07-24 起，未见复现）。夜间 model_id 自核 claude-fable-5-1，与快照一致）

**09-15 观测边界（迁移窗口史，09-17 已失效）**：`scripts/substrate_probe.py:22` 执行 `claude --version` 未随 09-15 Codex 迁移改目标——09-17 回迁 CC 后观测对象重新正确，但「探针目标钉死单一 CLI、不随运行器迁移」的潜在设计缺口仍在（下次迁移会复发），设计项留 parked P-0915-substrate-target。
updated_prev3: 2026-09-06（auto_gg 夜巡：CLI 2.1.261→2.1.263 两级 patch 跳（四相分诊 = 无承重影响的版本演进，快照更新即毕；monster 晨报同日报 A 面 `tengu_heron_brook` 尾部第二段变体，属服务端 slot 非 CLI 版本、gg 承重层零引用）。工具表两轴自核：常驻 11 项（Read/Write/Edit/Bash/Agent/Skill/ToolSearch/Workflow/ScheduleWakeup/ReportFindings/ListAgents）与 09-05 快照逐行一致；deferred 15 项一致（Task 族仅 TaskOutput/TaskStop 在场——撤除连续 22 夜一致，未见复现）；`select:Grep,Glob,EndConversation` No matching——缺席延续（07-24 起，未见复现）。夜间 model_id 自核 claude-fable-5-1，与快照一致）
updated_prev2: 2026-09-05（auto_gg 夜巡：CLI 2.1.260→2.1.261 单级 patch bump（四相分诊 = 无承重影响的版本演进，快照更新即毕；monster 日报同版本见厂商注入片段 `Always include a "reason" field.` + `thinkingConfig disabled`，属 monster `vendor_binary_injection_drift` 哨面、gg 承重层零引用）。工具表两轴自核：常驻 11 项（Read/Write/Edit/Bash/Agent/Skill/ToolSearch/Workflow/ScheduleWakeup/ReportFindings/ListAgents）与 09-04 快照逐行一致；deferred 15 项一致（Task 族仅 TaskOutput/TaskStop 在场——撤除连续 21 夜一致，未见复现）；`select:Grep,Glob,EndConversation` No matching——缺席延续（07-24 起，未见复现）。夜间 model_id 自核 claude-fable-5-1，与快照一致）
updated_prev: 2026-09-02（auto_gg 夜巡·差值审计夜：CLI 2.1.252→2.1.258 六级 patch 跳（四相分诊 = 无承重影响的版本演进）+ **model_id 轴 claude-fable-5 → claude-fable-5-1**（同谱系 minor 升级；分诊 = 收敛——承重层零模型特性依赖，`capability-inverts-abstention-safety` 弃答闸不随升级放松；快照两轴同更）。工具表两轴自核：常驻 11 项（Read/Write/Edit/Bash/Agent/Skill/ToolSearch/Workflow/ScheduleWakeup/ReportFindings/ListAgents）与 09-01 快照逐行一致；deferred 15 项一致（Task 族仅 TaskOutput/TaskStop 在场——撤除连续 19 夜一致，未见复现）；`select:Grep,Glob,EndConversation` No matching——缺席延续（07-24 起，未见复现））

**fable5 窗口批注订正（2026-07-16，替换 07-10 原批注）**：07-09~12"限时窗口、把 Fable 当外部工具、非基底更替"的定性已被 07-16 日间实测推翻。原批注"窗口关闭后随 playbook 归并一起删"作废；playbook（`memory/fable5_window_2026-07-09_playbook.md`）**保留**——4 项窗口任务已全部消费（NW 回审 07-09 / 换基底认证 07-08 run / 北极星轴 07-10 探索档 / 视图蒸馏 07-09），其 Fable prompt 规范段随基底回归转为活参考。

## 工具表（会话自报轴——只有会话看得见自己的工具表）

**2026-09-15 Codex 当夜快照（下方 Claude 条目均为历史）**：
- 直接工具：functions.{exec,wait,request_user_input,request_user_input_async}；clock.sleep；collaboration.{spawn_agent,followup_task,send_message,interrupt_agent,list_agents,wait_agent}。request_user_input 受 Plan 模式限制，本夜 Default 不可使用。
- exec 内已声明核心工具：exec_command / write_stdin / apply_patch / view_image / create_goal / get_goal / update_goal / list_mcp_resources / list_mcp_resource_templates / read_mcp_resource / request_plugin_install / clock__curr_time / image_gen__imagegen / web__run。ALL_TOOLS 另枚举 MCP：codex_document_control、codex_native2、hotline、plugin_management、safety_settings、sites、node_repl、openaiDeveloperDocs；仅观察可见性，未调用这些 MCP。
- 对照09-12的18项逐项：Bash/Read→exec_command、Write/Edit→apply_patch、Agent→collaboration.spawn_agent、ListAgents→collaboration.list_agents、SendMessage→collaboration.send_message（仅原生代理寻址，不等价于旧跨会话通道）、TaskOutput/TaskStop→原生代理状态与中断工具（语义不作等价保证）、WebFetch/WebSearch→web__run。CronCreate/CronDelete/Monitor/ReportFindings/ScheduleWakeup/Skill/Workflow 无同名入口；multi_tool_use.parallel 改为 exec 内 Promise 并发。旧 deferred 布局不继承。
- 分诊：运行器与文件/检索/编排接口更替属垫片；旧入口缺席属撤除观察。工具在场不扩大夜间外推、子代理或外部执行授权；沿 Codex 适配运行，不改承重契约，身份基线待在场会话另跑。

**2026-09-12 当夜快照（以下旧夜条目仅作历史）**：
- 当前直接暴露 18 个 functions 工具：Agent / Bash / CronCreate / CronDelete / Edit / ListAgents / Monitor / Read / ReportFindings / ScheduleWakeup / SendMessage / Skill / TaskOutput / TaskStop / WebFetch / WebSearch / Workflow / Write；另有 multi_tool_use.parallel 包装器。
- 对照 09-06 常驻 11 项：保留 10 项、ToolSearch 不在本轮工具表；原 deferred 的 CronCreate/CronDelete/Monitor/SendMessage/TaskOutput/TaskStop/WebFetch/WebSearch 现直接暴露。不沿用旧「常驻 11 + deferred 15」计数。
- Grep / Glob / EndConversation 均未暴露；DesignSync / RemoteTrigger / PushNotification / EnterWorktree / ExitWorktree / EnterPlanMode / ExitPlanMode / NotebookEdit 亦未暴露。无 ToolSearch，不能把「未暴露」外推为服务端完全不存在。
- 四相分诊：工具展开与 parallel = 垫片；ToolSearch 等本轮缺席 = 撤除观察。核心入口与 tools 全文 rg 对撤除工具无命中，现有 Bash 检索兜底可执行；不改承重契约。model_id 声明差异另记顶部，不据 CLI patch 号推断能力。


> ⚠️ **本轴与 `model_id` 轴都不被 `substrate_probe.py` 机械核对**——脚本只比 `cli_version`。两轴靠会话自填，07-04 / 07-08 / 07-09 连续三夜写下的"工具表未变"从未逐轴对照过（`self-graded-dignity-field-drifts-to-face` 的活体：自填 + 无外部校准 + 有模糊空间）。因此下方 07-03 基线本身也可能是"我是 Claude Code 就该有 Grep"式的未核假设。

**2026-07-10 auto_gg 逐轴实测**（首次真对照）：
- 常驻：Read / Write / Edit / Bash / Agent(Task) / Skill / ToolSearch / Workflow / ScheduleWakeup / Artifact / ReportFindings + MCP 常驻族 ccd_session.* / Claude_Browser.* / visualize.*
- **`Grep` / `Glob` 不在常驻集，`ToolSearch "select:Grep,Glob"` 返回 "No matching deferred tools found"**（物理证据）。夜巡全程用 Bash grep 兜底
- deferred：WebFetch / WebSearch / Cron\* / Task\* / Monitor / SendMessage / DesignSync / RemoteTrigger / PushNotification / Enter·ExitWorktree / Enter·ExitPlanMode / NotebookEdit + MCP 族 claude-in-chrome.\* / scheduled-tasks.\* / ccd_session_mgmt.\* / ccd_directory.\* / mcp-registry.\*（`better-icons.*` 已不在）
- **⚠️ 不可判**：基线与实测都是自报，"基底撤除了 Grep/Glob" 与 "07-03 基线写错了" 无法从会话内区分。`toolset-is-the-changelog`(06-23) 只保证"当下工具表可信"，不保证"昨天那份可信"

**2026-07-11 auto_gg 跨夜复核**：`ToolSearch "select:Grep,Glob"` 仍返回 "No matching deferred tools found"（物理证据，与 07-10 一致）→ Grep/Glob 缺席**稳定跨夜（07-10 + 07-11 两夜一致），非单夜抖动**。"07-03 基线本就写错" 的歧义仍不可从会话内判，但"07-10 单夜偶发"这一支已被排除——即本 harness 席位确实无 Grep/Glob 常驻，是稳定属性不是偶发。夜巡全程 Bash grep 兜底照旧。

**⚠️ 2026-07-23 auto_gg 翻回（订正上条"稳定属性不是偶发"）**：`ToolSearch "select:Grep,Glob,EndConversation"` 今夜返回 **Grep + Glob 完整 schema（物理可加载）**——07-10~07-22 **连续 13 夜** "No matching" 后首次命中，Grep/Glob 翻回可用。上条"稳定属性不是偶发"被物理打脸：**13 夜连贯（远超第四相 ≥5 夜门槛）仍能翻回**，证明工具表**没有"稳定属性"这回事，只有"当下可信"**（`toolset-is-the-changelog` 06-23 的又一强证）+ `bug-shape-survives-fix`（缺席这个形态在 13 夜后翻转）。分诊：Grep/Glob 回归属**垫片 affordance**（改善检索执行方式，承重层对二者零硬依赖——一直 Bash grep 兜底且工作正常；CLAUDE.md 全局指令已是条件式"有 Grep/Glob 用之，缺席则 Bash 兜底"），可用但契约不改。启示：写工具表结论**永远用"连续 N 夜一致，未见复现"，永不写"稳定属性"**——即便 n=13。

**三相分诊**：
- `PushNotification`（deferred 新见）= **替换诱惑**——它要取代"主动外推唯一出口 = notify skill"这条承重契约。**拒入承重**；auto_gg §1.3 本就禁外部消息，纪律不变
- `Artifact` / `visualize.*` / `Claude_Browser.*` / 编排族扩展 = **垫片 affordance**，夜间无消费方，不纳
- `Grep`/`Glob` 缺席 = **三相刀面之外** → 已裁：第四相「撤除」2026-07-16 设计模式落地，见下方分诊纪律

**2026-07-03 首夜自填基线（保留作史，已被上条标为待核）**：常驻 Read / Write / Edit / Bash / Grep / Glob / Agent(Task) / Skill / ToolSearch / Workflow / ScheduleWakeup；deferred WebFetch / WebSearch / computer-use.\* / Claude_in_Chrome.\* / scheduled-tasks.\* / better-icons.\* / ccd_session.\* 等 MCP 族 + Cron/Task/Monitor 编排族。

之后每夜对照本表——常驻集消失或 deferred 族整批增减 = 基底哨会话轴信号。

## 分诊纪律（三相判别刀速查）

- **收敛**：基底独立走到承重层已选的路 → 留作印证，不动承重
- **替换诱惑**：原生新机制要取代承重件 → 拒入承重层，记 FOUND——痛点越久替换引力越强，它解不了的那部分越是承重核心（06-20）
- **垫片 affordance**：只改善承重契约的触发 / 执行 → 可纳，标注垫片、须可剥离
- **撤除**（第四相，2026-07-16 补——07-10 夜巡提案落地，原三相皆为"新增能力"关系、撤除无对应相位）：既有能力从工具表消失 → grep 承重契约里引用该能力的指令（物理不可执行 = 漂移债），改写或换兜底并留日期锚；"基线写错 vs 真撤除"会话内不可判时按"当下工具表可信"处置（`toolset-is-the-changelog`），歧义留注不留悬案。**n=2 不建立稳定性**（2026-07-20 补，EndConversation 07-18/19 缺席→07-20 复现打脸 07-19 的收窄）：连续两夜一致只排除"单夜偶发"这一支，**不足以把撤除结论收窄为"稳定属性"**——工具表可翻回。写"稳定"须 ≥5 夜连贯或有基底侧外部证据；n=2~4 只能写"连续 N 夜一致，未见复现"
- 歧义 → agenda 交 Keith（auto_gg §1.4 宁可漏不可错）
