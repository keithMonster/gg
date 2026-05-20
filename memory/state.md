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
last_summoned_at: "2026-05-19 22:22 夜间 auto_gg 跑——SCAN/FOUND/DID 三段。morning-brief 5/19 日报（高负载 326 回合）+ proposals.jsonl 今日已更新。NW 结算：L4 2（2026-05-19-S1 与 blocked 2026-05-18-S1 同 bg 问题族标 blocked / 2026-05-19-G1 thread append conf0.8 = v0.3.0 候选 B 累积票标 blocked，proposals.jsonl 回写不 push monster）/ L5 3（2026-05-19-G2 全局 CLAUDE.md + 2026-05-18-G1 monster/CLAUDE.md + 2026-05-01-G1 guardrail pending 18 天，只提议不动手）。跨场景关键发现：'一句话优先'偏好同日两侧同构（monster NW ≥4 次 + gg 设计会话 Keith 双重叫停）——auto_gg 独占视角，已补写 tracks/keith.md（gg 自域可逆）+ agenda STRATEGIC 推送。essence append 无（curated-memory/mirror-not-second-order 已覆盖，设计会话已沉淀 evaluator-input-ownership，不仪式性凑滴）。audit.py 1 噪音（agenda bare filename，非真实辐射）。auto_gg 不接管 Keith 在场产出（essence.md 8 滴 + 8 untracked reflections 5/19，不 stage）。"
last_decision_slug: "2026-04-22_threads-v1-architecture-review"
last_reflection_slug: "2026-05-18_global-claude-md-rule-budget-gate"
last_design_session_slug: "2026-05-16_gg-active-channel-to-keith"
```

**完整出场清单**：`ls memory/{archival,reflections,design_sessions,audit}/ | sort` 即可。
**变更历史**：`git log -- memory/state.md`。
**组件分类（KERNEL + 身体）**：见 `CORE.md §8`。**KERNEL.md 修改需 Keith 在当次对话中连续两次独立明示批准**（`KERNEL.md §2` 铁律 3）；身体（KERNEL 之外的所有文件）gg 在设计模式下可直接演化。
