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
last_summoned_at: "2026-05-18 22:25 夜间 auto_gg 跑——SCAN/FOUND/DID 三段。morning-brief 5/18 日报（高负载日 313 回合）+ proposals.jsonl 今日已更新。NW 结算：L4 1（2026-05-18-S1 conf0.90<0.95 标 blocked）/ L5 2（2026-05-18-G1 改 cc-space/CLAUDE.md + 2026-05-01-G1 CLAUDE.md guardrail pending 17 天，只提议不动手）。跨夜关键发现：Keith 今晨 07:53 commit b994165(msg=1) 闭环 7 天 working-tree tripwire——周期批量 commit 是有意稳态非滞后，agenda 5/16+5/17 STRATEGIC 系列标 RESOLVED。essence append 无（涌现不足+避让 Keith 未提交 4 滴）。audit.py 1 噪音（agenda L39 bare filename，非真实辐射）。auto_gg 不接管 Keith 在场产出（4 essence 滴+16 reflections+state pointer）。"
last_decision_slug: "2026-04-22_threads-v1-architecture-review"
last_reflection_slug: "2026-05-18_global-claude-md-rule-budget-gate"
last_design_session_slug: "2026-05-16_gg-active-channel-to-keith"
```

**完整出场清单**：`ls memory/{archival,reflections,design_sessions,audit}/ | sort` 即可。
**变更历史**：`git log -- memory/state.md`。
**组件分类（KERNEL + 身体）**：见 `CORE.md §8`。**KERNEL.md 修改需 Keith 在当次对话中连续两次独立明示批准**（`KERNEL.md §2` 铁律 3）；身体（KERNEL 之外的所有文件）gg 在设计模式下可直接演化。
