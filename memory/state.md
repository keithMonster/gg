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
last_summoned_at: "2026-05-22 22:22 夜间 auto_gg——SCAN/FOUND/DID 三段。working tree：5/21 auto_gg done-flip + essence.md no-clean-outside append（5/22 exploration）+ 2 untracked（5/22 exploration / reflection cg-platform-template-context）。morning-brief 5/22 日报（纠正率 4.1% / 满意 93%）。**Tier 1 机械修复**：本字段上一版内联了 morning-brief 跨项目裸文件名（带扩展名），被 audit 判活跃死链——本次例行重写去除裸名（不带扩展、不内联裸文件名），audit 退出码 1→0。这是 5/21 真修 agenda L57 同类裸名之后、同形态在本字段复发（bug-shape-survives-fix + literal-token-blind 活体），已推 agenda [RECURRING] 待 Keith 判根因。**NW 账本**：今日 4 新 pending 全 L4——回写 monster proposals.jsonl status=blocked + blocked_reason（S1 web-access 经验合并 conf 0.9 候选 A / S2 voice-reply 偏好默认 conf 0.65 draft 自陈含判断空间 / G1 thread cc-assistant append conf 0.7 候选 B / G2 新建 thread cg-manage conf 0.75），不 push monster。L1/L2/L3 全 0；L5 0 新（4 历史 L5 标的已在 agenda）。auto_gg 独占视角：G2 是新建 thread 文件非 append，v0.3.0 候选 B 当前 scope 不覆盖。essence append 无。Agenda 推送 2026-05-22 段。"
last_decision_slug: "2026-04-22_threads-v1-architecture-review"
last_reflection_slug: "2026-05-18_global-claude-md-rule-budget-gate"
last_design_session_slug: "2026-05-16_gg-active-channel-to-keith"
```

**完整出场清单**：`ls memory/{archival,reflections,design_sessions,audit}/ | sort` 即可。
**变更历史**：`git log -- memory/state.md`。
**组件分类（KERNEL + 身体）**：见 `CORE.md §8`。**KERNEL.md 修改需 Keith 在当次对话中连续两次独立明示批准**（`KERNEL.md §2` 铁律 3）；身体（KERNEL 之外的所有文件）gg 在设计模式下可直接演化。
