# substrate — 基底快照（基底哨的对照面）

> auto_gg SCAN 段的基底哨（`scripts/substrate_probe.py`）对照本文件的 `cli_version` 字段。
> 任一轴变化 → 三相判别刀分诊（`substrate-capability-triage-three-relations` 2026-06-20）→ 写 FOUND + 更新本文件。
> **`model_id` 轴变化额外动作**（2026-07-02 起）：读 `memory/model_transitions/` 最近一份交接档（继任者第一课）+ 跑 `eval/identity-cases.md` 身份基线；更替可预知时由退场基底提前留档。
> 历史不留在本文件——git log 即变更史（`toolset-is-the-changelog` 2026-06-23）。

cli_version: 2.1.202 (Claude Code)
model_id: claude-opus-4-8[1m]
updated: 2026-07-07（CLI 2.1.201→2.1.202 patch bump 同步；model_id 轴与工具表未变，三相分诊 = 纯垫片层无承重影响）

## 工具表（会话自报轴——只有会话看得见自己的工具表）

首夜自填（2026-07-03 auto_gg，Opus 4.8 继任首巡）——常驻工具：Read / Write / Edit / Bash / Grep / Glob / Agent(Task) / Skill / ToolSearch / Workflow / ScheduleWakeup。
deferred（ToolSearch 按需加载）：WebFetch / WebSearch / computer-use.* / Claude_in_Chrome.* / scheduled-tasks.* / better-icons.* / ccd_session.* 等 MCP 族 + Cron/Task/Monitor 编排族。
之后每夜对照本表——常驻集消失或 deferred 族整批增减 = 基底哨会话轴信号。

## 分诊纪律（三相判别刀速查）

- **收敛**：基底独立走到承重层已选的路 → 留作印证，不动承重
- **替换诱惑**：原生新机制要取代承重件 → 拒入承重层，记 FOUND——痛点越久替换引力越强，它解不了的那部分越是承重核心（06-20）
- **垫片 affordance**：只改善承重契约的触发 / 执行 → 可纳，标注垫片、须可剥离
- 歧义 → agenda 交 Keith（auto_gg §1.4 宁可漏不可错）
