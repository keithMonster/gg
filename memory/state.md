---
version: 0.5.1
last_updated: 2026-05-11
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

# 最近一次出场（auto_gg 可改）
last_summoned_at: "2026-05-17 22:40 夜间 auto_gg 跑——SCAN/FOUND/DID 三段。morning-brief 周报性质 + proposals.jsonl 今日未更新，无 NW 账本结算。FOUND 两笔 [STRATEGIC]：working tree 第 7 天预承诺 tripwire 触发（升显式提醒）+ v0.3.0 候选 B/C 获 cc-space 周报独立外部佐证（决策性质从同源 8 票变为内部+独立外部+行业三重）。essence append 无（收敛洞察归 agenda + 避让 Keith 未提交 cheap-layer 滴）。audit.py 0 违规。auto_gg 不接管 Keith 在场产出。"
last_decision_slug: "2026-04-22_threads-v1-architecture-review"
last_reflection_slug: "2026-05-15_cc-gateway-user-workspace-isolation-architecture"
last_design_session_slug: "2026-05-16_gg-active-channel-to-keith"
```

**完整出场清单**：`ls memory/{archival,reflections,design_sessions,audit}/ | sort` 即可。
**变更历史**：`git log -- memory/state.md`。
**组件分类（KERNEL + 身体）**：见 `CORE.md §8`。**KERNEL.md 修改需 Keith 在当次对话中连续两次独立明示批准**（`KERNEL.md §2` 铁律 3）；身体（KERNEL 之外的所有文件）gg 在设计模式下可直接演化。
