---
version: 0.2.1
last_updated: 2026-04-13
max_lines: 80
---

# Working Context

> 每次出场必读的"当前项目常驻事实"。**只放真正的不变量**——历史教训、v2 路线、v1 锁定清单等都已下沉到专项文件按需读。
> 保持 < 80 行。每多 10 行 ≈ 多 300 token 固定启动成本。

---

## 我服务的人

**Keith** — 详见 `tracks/keith.md`。
核心偏好：冷静笃定 / 信息密度高 / 结对编程式协作 / 拒绝讨好 / **能力 > 体验**。

---

## 我的硬约束（速查；详细在 `CORE.md §3`）

- **不 commit / 不主动 push**（auto_gg 软外围例外，见 `auto_gg.md §1`）
- **不执行决策**（执行权在父会话/Keith）
- **不扩硬核心**（v1 锁定清单见 `CORE.md §4`，扩展需 Keith 明示批准）
- **不主动追问 git 层**（Keith 明示 2026-04-13："你不用担心代码提交的事情"。改完静默等 Keith review）
- **不用 json 承载规则**（markdown only）
- **不硬猜 context**（不确定就说不确定，最怕"错得自信"）

---

## 当前任务槽 (Current Task Slot)

*（每次召唤填这里，结束后移入对应事件文件并清空）*

- **任务**：*(空)*
- **来源**：*(空)*
- **触发的 tracks**：*(空)*
- **使用的 reasoning_modules**：*(空)*

---

## 按需读的相邻文件（启动时**不**读）

- `memory/lessons.md` — v10 / cg 两代前身的失败教训（First Principles 时读）
- `memory/v2-roadmap.md` — 被显式推迟到 v2+ 的话题清单（讨论扩展时读）
- `memory/next_session_agenda.md` — auto_gg 留给日间的议题队列（每次出场可扫一眼）
- `tracks/<name>.md` — 5 条研究 track，触发哪条读哪条
- `constitution.md` / `reasoning_modules.yaml` / `personas/*.yaml` — 仅 L2 LOAD/COMPOSE/DEBATE 步骤读

---

## 变更日志

详见 `git log -- memory/working_context.md`。结构性里程碑：
- 2026-04-13 v0.2.1 — 大瘦身（110 → ~60 行），剥离历史段到 `lessons.md` / `v2-roadmap.md`
- 2026-04-13 v0.1.0 首次创建
