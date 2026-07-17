---
version: 0.5.1
last_updated: 2026-07-09
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
last_summoned_at: "[2026-07-17 设计模式（07-16 遗留四项拍板）：Keith 逐项裁决——v2 不开、阈值改锚痛感线（档案侧检索失败≥2 外部登记，判别刀入 checkup §2）/ git 杂物两处删+scratch ignore / 全局 CLAUDE.md ghost-rule 回委 gg 判断改条件式 / KERNEL §3 死分支不动改捆绑提醒。执行验证全绿（audit 0 违规），KERNEL 零触碰。详见 design_sessions/2026-07-17_leftover-four-verdicts.md]"
last_decision_slug: "2026-04-22_threads-v1-architecture-review"
last_reflection_slug: "2026-07-16_citation-fabrication-selftrial-append-only"
last_design_session_slug: "2026-07-17_leftover-four-verdicts"
```

**完整出场清单**：`ls memory/{archival,reflections,design_sessions,audit}/ | sort` 即可。
**变更历史**：`git log -- memory/state.md`。
**组件分类（KERNEL + 身体）**：见 `CORE.md §8`。**KERNEL.md 修改需 Keith 在当次对话中连续两次独立明示批准**（`KERNEL.md §2` 铁律 3）；身体（KERNEL 之外的所有文件）gg 在设计模式下可直接演化。
