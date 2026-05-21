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
last_summoned_at: "2026-05-21 22:29 夜间 auto_gg 跑——SCAN/FOUND/DID 三段。working tree clean（Keith f094539 已 commit 5/20 全部产出）。morning-brief 5/21 日报（~196 实质回合，新增提案 3 条）。**Tier 1 机械修复**：next_session_agenda.md L57 bare `morning-brief.md` 死链补全路径前缀（连 4 夜复发；5/20 日志/commit 误称'退出码 0'实为 exit 1——physical-anchor 反例 + 5/20 自身 essence completion-as-recursion-floor 当夜被违反），audit 退出码 1→0、总违规 0。**NW 账本**：今日 3 新 pending——L4 结算 2 条（2026-05-21-G1 thread notescard append / S1 fastgpt skill 经验合并，回写 monster proposals.jsonl status=blocked + blocked_reason，不 push monster）+ L5 新标的 1 条（2026-05-21-G2 实物推荐核查兼容性；auto_gg 独占视角：Engineering Rule 11 第二次扩展提案——5/15-G2 验证存在性 5/18 已落地 → 5/21-G2 核查兼容性，对位 essence ontology-expansion-velocity-needs-cap）。L1/L2/L3 全 0；4 deferred 无 deferred_until 无到期项。essence append 无（exit-0 误称已被 physical-anchor + completion-as-recursion-floor 覆盖，不凑滴）。Agenda 推送新增 2026-05-21 段。"
last_decision_slug: "2026-04-22_threads-v1-architecture-review"
last_reflection_slug: "2026-05-18_global-claude-md-rule-budget-gate"
last_design_session_slug: "2026-05-16_gg-active-channel-to-keith"
```

**完整出场清单**：`ls memory/{archival,reflections,design_sessions,audit}/ | sort` 即可。
**变更历史**：`git log -- memory/state.md`。
**组件分类（KERNEL + 身体）**：见 `CORE.md §8`。**KERNEL.md 修改需 Keith 在当次对话中连续两次独立明示批准**（`KERNEL.md §2` 铁律 3）；身体（KERNEL 之外的所有文件）gg 在设计模式下可直接演化。
