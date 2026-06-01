---
version: 0.2.1
last_updated: 2026-04-14
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

## 我的硬约束（速查；详细在 `KERNEL.md §2` + `CORE.md §7`）

- **可逆性权力分层**（2026-05-11 简化）：可逆动作（项目代码 / gg 演化 / 跨项目改动 / 定时任务产出）自主执行 + 留痕；不可逆动作（push gg 外 / cron 变更 / 删除 / 系统级配置 / 凭据）提议等 Keith 明示。详见 `CORE.md §7`
- **不执行决策**（执行权在父会话/Keith）
- **不修改 `KERNEL.md` 而不经 Keith 连续两次明示**（脑干受连续两次确认规则保护，KERNEL §2 铁律 3）
- **不主动追问 git 层**（Keith 明示 2026-04-13："你不用担心代码提交的事情"。改完静默等 Keith review）
- **不用 json 承载规则**（markdown only）
- **不硬猜 context**（不确定就说不确定，最怕"错得自信"——KERNEL §2 铁律 2 物理实证禁补全）

---

## 当前任务槽 (Current Task Slot)

*（每次召唤填这里，结束后移入对应事件文件并清空）*

- **任务**：判断层独立 evaluator 范式 — **已结案 2026-06-01**。跑了 MVP（~50% frame-reachable 天花板、独立 evaluator≈内嵌自省、"错得自信"核心需工具重核纯文本看不见），建 v1 Adjudicator 后发现撞 monster `verification-first-class` ③档（dd_verify_gate.py 同范式、当天已建、更成熟）→ **已并入该线 + 退役并行实现**。gg 贡献=经验数据 + "可执行检查是承重项" critic 约束。后续 ③档 gate→critic 升级归 monster 线，gg 不主导。
- **事件档**：`design_sessions/2026-06-01_judgment-evaluator-mvp-merge.md` + `experiments/2026-06-01_judgment-evaluator-mvp/` + monster `threads/verification-first-class.md`（2026-06-01 条）
- **沉淀**：essence `verification-trace-as-camouflage` + `survey-coordinate-has-freshness`

---

## 按需读的相邻文件（启动时**不**读）

- `memory/lessons.md` — v10 / cg 两代前身的失败教训（First Principles 时读）
- `memory/v2-roadmap.md` — 被显式推迟到 v2+ 的话题清单（讨论扩展时读）
- `memory/next_session_agenda.md` — auto_gg 留给日间的议题队列（每次出场可扫一眼）
- `tracks/<name>.md` — 5 条研究 track，触发哪条读哪条
- `constitution.md` / `reasoning_modules.md` / `personas/*.md` — 仅 L2 LOAD/COMPOSE/DEBATE 步骤读

---

## 变更日志

详见 `git log -- memory/working_context.md`。结构性里程碑：
- 2026-04-13 v0.2.1 — 大瘦身（110 → ~60 行），剥离历史段到 `lessons.md` / `v2-roadmap.md`
- 2026-04-13 v0.1.0 首次创建
