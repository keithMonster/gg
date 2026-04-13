---
version: 0.2.1
last_updated: 2026-04-13
---

# State

> 启动时必读的最小元状态。**只放每次启动判断分支需要的字段**。
> 历史与变更日志在 git log；事件细节在 `memory/{archival,reflections,design_sessions,audit}/`；v1 锁定清单在 `CORE.md §4`；前两代教训在 `memory/lessons.md`；v2 候选在 `memory/v2-roadmap.md`。

```yaml
# 身份字段（auto_gg 不可改，见 auto_gg.md §1.3）
first_contact_done: true
first_contact_date: 2026-04-13
first_real_decision_done: true
first_real_decision_date: 2026-04-13
current_version: 0.2.1
created: 2026-04-13

# 最近一次出场（auto_gg 可改）
last_summoned_at: "2026-04-13 auto_gg 首次夜间执行"
last_decision_slug: "2026-04-13_skill-auditor-coding-dimension"
last_reflection_slug: "2026-04-13_skill-auditor-coding-dimension"
last_design_session_slug: "2026-04-13_v0.2.1-context-economy"
```

**完整出场清单**：`ls memory/{archival,reflections,design_sessions,audit}/ | sort` 即可。
**变更历史**：`git log -- memory/state.md`。
**v1 组件锁定清单**（5 tracks / 2 personas / 8 原则+5 闸门 / 8 reasoning_modules）：见 `CORE.md §4`，扩展需 Keith 明示批准。
