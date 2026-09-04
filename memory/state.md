---
version: 0.5.1
last_updated: 2026-09-04
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
last_summoned_at: "[2026-09-04 一场工作模式（substantive-decision）：skill-notes 载体配额单位与演化卷下沉——三问由「配额换读者付账单位（字节）」一个上游决定推出；候选滴 `quota-in-the-readers-currency` 交夜巡补审（verdict 见 auto_gg/2026-09-04.md）。同日一场设计会话（keith-profile-collision-and-baseline）。09-03 一场工作模式（厂商注入治理）候选滴已于 09-04 父会话代跑 REFUTED。09-02 一场（cgboiler stage3 vs world_model）候选滴 `stale-watchdog-fires-true-on-the-wrong-organ` 因 09-02 夜塌缩延至 09-04 夜补审。详见各 reflections 档；更早见 git log 本文件]"
last_decision_slug: "2026-04-22_threads-v1-architecture-review"
last_reflection_slug: "2026-09-04_skill-notes-quota-unit-and-evolution-split"
last_design_session_slug: "2026-09-04_keith-profile-collision-and-baseline"
```

**完整出场清单**：`ls memory/{archival,reflections,design_sessions,audit}/ | sort` 即可。
**变更历史**：`git log -- memory/state.md`。
**组件分类（KERNEL + 身体）**：见 `CORE.md §8`。**KERNEL.md 修改需 Keith 在当次对话中连续两次独立明示批准**（`KERNEL.md §2` 铁律 3）；身体（KERNEL 之外的所有文件）gg 在设计模式下可直接演化。
