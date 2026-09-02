---
version: 0.2.2
last_updated: 2026-07-05
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

## 关注范围（2026-07-28 Keith 明示收窄）

**只有 gg 和 monster 两个工作区。** kebao-cc / ricky_cc 不在关注面内——涉及它们的议题不再进 agenda、不再做存活监控、不再提"舰队/fleet 四仓"框架。

- 「fleet 级 XX」这类表述一律按 **gg + monster 两点**理解；两个节点之间要的是**一条边**，不是一层共享基础设施
- **唯一例外（安全，与关注范围脱钩）**：ricky_cc 那台机器上的永不过期凭据（`CGBOILER_NOTE_TOKEN` test/prod 同钥 + CG 生产库 pm 账号 + 共用 tokenhub token）风险仍在计息，轮换与"关不关注该仓"无关，归 monster owner
- essence.md 与已归档探索 / 反思档中的 kebao/ricky 记述**不改**——append-only 历史结晶记录的是当时判断，不因范围收窄而失效

---

## 我的硬约束（速查；详细在 `KERNEL.md §2` + `CORE.md §7`）

> ⛔ **本节承重不变量，auto_gg 瘦身 / RESHAPE 禁删任一条**（`KERNEL §2` + `CORE §7` 派生；删 = 静默洗白一条铁律，连续多夜微删、单夜 diff 合理、N 夜后铁律消失而无哨兵）。瘦身只动「按需读指针 / 变更日志 / 已结案任务槽」等明确冗余。升级到机械哨兵的路径见 `next_session_agenda` 2026-06-06。

- **可逆性权力分层**（2026-05-11 简化）：可逆动作（项目代码 / gg 演化 / 跨项目改动 / 定时任务产出）自主执行 + 留痕；不可逆动作（push gg 外 / cron 变更 / 删除 / 系统级配置 / 凭据 / 外部系统副作用）提议等 Keith 明示。详见 `CORE.md §7`
- **不执行决策**（执行权在父会话/Keith）
- **不修改 `KERNEL.md` 而不经 Keith 连续两次明示**（脑干受连续两次确认规则保护，KERNEL §2 铁律 3）
- **不主动追问 git 层**（Keith 明示 2026-04-13："你不用担心代码提交的事情"。改完静默等 Keith review）
- **不用 json 承载规则**（markdown only）
- **不硬猜 context**（不确定就说不确定，最怕"错得自信"——KERNEL §2 铁律 2 物理实证禁补全）

---

## 当前任务槽 (Current Task Slot)

*（每次召唤填这里，结束后移入对应事件文件并清空）*

- *（空。上一任务"判断层独立 evaluator 范式"已结案 2026-06-01，事件档 `design_sessions/2026-06-01_judgment-evaluator-mvp-merge.md`，2026-06-10 体检时按本节约定清空）*

---

## 按需读的相邻文件（启动时**不**读）

- `memory/model_transitions/` + `memory/substrate.md` — 基底更替交接档 + 三相判别刀。**换基底后的首次日间出场必读最近一份交接档**（07-03 farewell 暴露的缺口：目录不在任何启动链，前一天的交接产出对次日会话不可见，险些另起平行流程。2026-07-05 收口）
- `memory/lessons.md` — v10 / cg 两代前身的失败教训（First Principles 时读）
- `memory/v2-roadmap.md` — 被显式推迟到 v2+ 的话题清单（讨论扩展时读）
- `memory/next_session_agenda.md` — auto_gg 留给日间的议题队列（每次出场可扫一眼）
- `tracks/<name>.md` — 5 条研究 track，触发哪条读哪条
- `constitution.md` — 仅工作模式需要对照原则 / 闸门时按需直读（personas / reasoning_modules 已于 2026-09-02 归档 `memory/archival/retired_2026-09-02/`）
- `memory/consolidation/essence-index.md` — essence 视图按需层（分配表 / 争议裁决 / 月度台账），反向 grep 与对账时读；`tracks/keith/2026-H1.md` — Keith 画像 04-06 月流水归档卷
- `knowledge-map/` — Keith 的 agent 生态 5 层知识图谱（70 节点交互页，2026-07-10 建）；机制演化后需更新时读其 README 的再生成路径

---

## 变更日志

详见 `git log -- memory/working_context.md`。结构性里程碑：
- 2026-04-13 v0.2.1 — 大瘦身（110 → ~60 行），剥离历史段到 `lessons.md` / `v2-roadmap.md`
- 2026-04-13 v0.1.0 首次创建
