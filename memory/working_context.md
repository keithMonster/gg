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

- **任务**：判断层独立 evaluator 范式 — draft 已落档，待 **2026-06-01 与 Keith 细聊定案**（4 决策点：方向裁决 / MVP 跑不跑 / prior 共盲天花板可接受吗 / done 骨架化顺不顺手）
- **来源**：Keith 2026-05-31 设计模式开放直觉（"感觉有个新范式能大幅提效率和稳定性、还没找到、用于 gg 或 monster"）
- **文档**：`memory/design_sessions/2026-05-31_judgment-layer-evaluator-paradigm.md`（完整推演轨迹见 `state.md` 的 `last_summoned_at`）
- **触发的 tracks**：`architecture`（范式 / evaluator 分离） / `ai`（LLM 自审认识论极限）

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
