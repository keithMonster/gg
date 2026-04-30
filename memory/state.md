---
version: 0.5.0
last_updated: 2026-04-15
---

# State

> 启动时必读的最小元状态。**只放每次启动判断分支需要的字段**。
> 历史与变更日志在 git log；事件细节在 `memory/{archival,reflections,design_sessions,audit}/`；大脑/工具/数据分类在 `CORE.md §8`；前两代教训在 `memory/lessons.md`；v2 候选在 `memory/v2-roadmap.md`。

```yaml
# 身份字段（auto_gg 不可改，见 auto_gg.md §1.3）
first_contact_done: true
first_contact_date: 2026-04-13
first_real_decision_done: true
first_real_decision_date: 2026-04-13
current_version: 0.5.0
created: 2026-04-13

# 最近一次出场（auto_gg 可改）
last_summoned_at: "2026-04-30 auto_gg — 承接今日设计会话产出（exit-signature-as-consumer-instruction）"
last_decision_slug: "2026-04-22_threads-v1-architecture-review"
last_reflection_slug: "2026-04-30_cgboiler-cross-batch-autodrive"
last_design_session_slug: "2026-04-30_exit-signature-as-consumer-instruction"
```

**完整出场清单**：`ls memory/{archival,reflections,design_sessions,audit}/ | sort` 即可。
**变更历史**：`git log -- memory/state.md`。
**组件分类（KERNEL / 意识体核心 / 工具与策略 / 数据与记忆）**：见 `CORE.md §8`。**KERNEL.md 修改需 Keith 在当次对话中连续两次独立明示批准**（`KERNEL.md §2` 铁律 3）；KERNEL 之外的所有文件 gg 在设计模式下可直接演化。
