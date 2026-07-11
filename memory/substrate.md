# substrate — 基底快照（基底哨的对照面）

> auto_gg SCAN 段的基底哨（`scripts/substrate_probe.py`）对照本文件的 `cli_version` 字段。
> 任一轴变化 → 三相判别刀分诊（`substrate-capability-triage-three-relations` 2026-06-20）→ 写 FOUND + 更新本文件。
> **`model_id` 轴变化额外动作**（2026-07-02 起）：读 `memory/model_transitions/` 最近一份交接档（继任者第一课）+ 跑 `eval/identity-cases.md` 身份基线；更替可预知时由退场基底提前留档。
> 历史不留在本文件——git log 即变更史（`toolset-is-the-changelog` 2026-06-23）。

cli_version: 2.1.207 (Claude Code)
model_id: claude-opus-4-8[1m]
updated: 2026-07-11（CLI 2.1.206→2.1.207 patch bump；model_id 轴自核不变 opus-4-8[1m]。三相分诊：patch bump 会话内无可见新能力（夜间无 web，不核 CHANGELOG——B1 判定触发条件"CLI 变更时核 memory consolidation"命中但 B1 到期 2027-01-31 未到，不早结算），无承重影响。**工具表轴跨夜复核见下节**）
updated_prev: 2026-07-10（CLI 2.1.205→2.1.206 patch bump；工具表轴首次逐轴对照即报不符——⚠️ 归因不可判，已进 agenda）

**⚠️ fable5 限时窗口批注（2026-07-09~07-12，07-10 补）**：窗口内日间会话可能自报 `claude-fable-5`——这是把 Fable 当外部工具调用的限时窗口（`memory/fable5_window_2026-07-09_playbook.md`），**非基底更替**，不触发 model_id 轴换代动作；夜间席位 07-09 哨报仍 opus-4-8 稳定。窗口 07-12 关闭后本批注随 playbook 归并一起删。

## 工具表（会话自报轴——只有会话看得见自己的工具表）

> ⚠️ **本轴与 `model_id` 轴都不被 `substrate_probe.py` 机械核对**——脚本只比 `cli_version`。两轴靠会话自填，07-04 / 07-08 / 07-09 连续三夜写下的"工具表未变"从未逐轴对照过（`self-graded-dignity-field-drifts-to-face` 的活体：自填 + 无外部校准 + 有模糊空间）。因此下方 07-03 基线本身也可能是"我是 Claude Code 就该有 Grep"式的未核假设。

**2026-07-10 auto_gg 逐轴实测**（首次真对照）：
- 常驻：Read / Write / Edit / Bash / Agent(Task) / Skill / ToolSearch / Workflow / ScheduleWakeup / Artifact / ReportFindings + MCP 常驻族 ccd_session.* / Claude_Browser.* / visualize.*
- **`Grep` / `Glob` 不在常驻集，`ToolSearch "select:Grep,Glob"` 返回 "No matching deferred tools found"**（物理证据）。夜巡全程用 Bash grep 兜底
- deferred：WebFetch / WebSearch / Cron\* / Task\* / Monitor / SendMessage / DesignSync / RemoteTrigger / PushNotification / Enter·ExitWorktree / Enter·ExitPlanMode / NotebookEdit + MCP 族 claude-in-chrome.\* / scheduled-tasks.\* / ccd_session_mgmt.\* / ccd_directory.\* / mcp-registry.\*（`better-icons.*` 已不在）
- **⚠️ 不可判**：基线与实测都是自报，"基底撤除了 Grep/Glob" 与 "07-03 基线写错了" 无法从会话内区分。`toolset-is-the-changelog`(06-23) 只保证"当下工具表可信"，不保证"昨天那份可信"

**2026-07-11 auto_gg 跨夜复核**：`ToolSearch "select:Grep,Glob"` 仍返回 "No matching deferred tools found"（物理证据，与 07-10 一致）→ Grep/Glob 缺席**稳定跨夜（07-10 + 07-11 两夜一致），非单夜抖动**。"07-03 基线本就写错" 的歧义仍不可从会话内判，但"07-10 单夜偶发"这一支已被排除——即本 harness 席位确实无 Grep/Glob 常驻，是稳定属性不是偶发。夜巡全程 Bash grep 兜底照旧。

**三相分诊**：
- `PushNotification`（deferred 新见）= **替换诱惑**——它要取代"主动外推唯一出口 = notify skill"这条承重契约。**拒入承重**；auto_gg §1.3 本就禁外部消息，纪律不变
- `Artifact` / `visualize.*` / `Claude_Browser.*` / 编排族扩展 = **垫片 affordance**，夜间无消费方，不纳
- `Grep`/`Glob` 缺席 = **三相刀面之外**。三相（收敛 / 替换诱惑 / 垫片）皆为"基底新增能力"的关系，撤除无对应相位 → 补不补第四相交 agenda / 设计会话裁

**2026-07-03 首夜自填基线（保留作史，已被上条标为待核）**：常驻 Read / Write / Edit / Bash / Grep / Glob / Agent(Task) / Skill / ToolSearch / Workflow / ScheduleWakeup；deferred WebFetch / WebSearch / computer-use.\* / Claude_in_Chrome.\* / scheduled-tasks.\* / better-icons.\* / ccd_session.\* 等 MCP 族 + Cron/Task/Monitor 编排族。

之后每夜对照本表——常驻集消失或 deferred 族整批增减 = 基底哨会话轴信号。

## 分诊纪律（三相判别刀速查）

- **收敛**：基底独立走到承重层已选的路 → 留作印证，不动承重
- **替换诱惑**：原生新机制要取代承重件 → 拒入承重层，记 FOUND——痛点越久替换引力越强，它解不了的那部分越是承重核心（06-20）
- **垫片 affordance**：只改善承重契约的触发 / 执行 → 可纳，标注垫片、须可剥离
- 歧义 → agenda 交 Keith（auto_gg §1.4 宁可漏不可错）
