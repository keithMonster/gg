---
version: 0.5.1
last_updated: 2026-09-02
---

# State

> 启动时必读的最小元状态。**只放每次启动判断分支需要的字段**。
> 历史与变更日志在 git log；事件细节在 `memory/{archival,reflections,design_sessions,audit}/`；KERNEL + 身体二分见 `CORE.md §8`；前两代教训在 `memory/lessons.md`；v2 候选在 `memory/v2-roadmap.md`。

```yaml
# 身份字段（auto_gg 不可改，见 auto_gg.md §1.3）
first_contact_done: true
first_contact_date: 2026-04-13
first_real_decision_done: true
first_real_decision_date: 2026-04-13
current_version: 0.5.1
created: 2026-04-13

# 最近一次出场（auto_gg 可改）。**单行摘要——值不被任何启动分支消费**（分支只读 first_contact_done，2026-07-09 全仓核实：其余 last_* 全是写方 / audit 存在性检查，无读值方），故只留可读指针 + git log 溯史。**禁套娃**（曾嵌 8 场原文、单次 30KB diff，2026-07-03 立约；2026-07-09 从 ~2.5KB 单行 blob 压成本行）。更早各场：git log -- memory/state.md
last_summoned_at: "[2026-09-01 一场工作模式（substantive-decision）：cgboiler sealed interpretation receipt 遇正确 amendment 的演化模型——裁决单链全状态快照 revision（`<batch>/revisions/rNNNN/receipt.json`），拒 overlay；root receipt 字节永不改、唯一 leaf 由图推导、每 revision 自带 parent snapshot ref、leaf 逐字节等于 live；首个 revision 允许一次 git 考古 bootstrap（6dc83b31 hash 已核）。无候选滴。详见 reflections/2026-09-01_cgboiler-interpretation-receipt-revision-chain.md；前一日 08-31 五场见 git log 本文件]"
last_decision_slug: "2026-04-22_threads-v1-architecture-review"
last_reflection_slug: "2026-09-01_cgboiler-interpretation-receipt-revision-chain"
last_design_session_slug: "2026-09-02_full-architecture-review"
```

**完整出场清单**：`ls memory/{archival,reflections,design_sessions,audit}/ | sort` 即可。
**变更历史**：`git log -- memory/state.md`。
**组件分类（KERNEL + 身体）**：见 `CORE.md §8`。**KERNEL.md 修改需 Keith 在当次对话中连续两次独立明示批准**（`KERNEL.md §2` 铁律 3）；身体（KERNEL 之外的所有文件）gg 在设计模式下可直接演化。
