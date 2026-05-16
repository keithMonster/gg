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
last_summoned_at: "2026-05-16 22:35 夜间 auto_gg 跑——SCAN/FOUND/DID 三段，NW 5/16 两条结算（G1 L4 blocked = 候选 B 累积第 8 票 / G2 L5 = Bash-hook family 第 3 实证汇聚 5/06-G1+5/12-R1）+ working tree 跨夜累积第 6 天（范围扩大含 5/16 在场产出，仍在 7-10 天容忍窗）。audit.py 0 违规。auto_gg 不接管 Keith 在场 5/16 设计/工作模式产出。"
last_decision_slug: "2026-04-22_threads-v1-architecture-review"
last_reflection_slug: "2026-05-15_cc-gateway-user-workspace-isolation-architecture"
last_design_session_slug: "2026-05-16_gg-active-channel-to-keith"
```

**完整出场清单**：`ls memory/{archival,reflections,design_sessions,audit}/ | sort` 即可。
**变更历史**：`git log -- memory/state.md`。
**组件分类（KERNEL + 身体）**：见 `CORE.md §8`。**KERNEL.md 修改需 Keith 在当次对话中连续两次独立明示批准**（`KERNEL.md §2` 铁律 3）；身体（KERNEL 之外的所有文件）gg 在设计模式下可直接演化。
