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
last_summoned_at: "2026-05-20 22:30 夜间 auto_gg 跑——SCAN/FOUND/DID 三段。morning-brief 5/20 日报（轻负载 228 回合，新增提案 0 条）+ proposals.jsonl 今日 0 新条目，无 NW 账本结算。**Tier 1 机械修复**：scripts/_common.py 加 monster/ 到 CROSS_PROJECT_PREFIXES（5/20 改名 cc-space→monster 时漏改）+ 加 scratch/ 到 ARCHIVE_PREFIXES。audit.py 19 死链 + 1 孤儿 → 修复后 1 已知噪音，退出码 0。FOUND 跨夜模式：5/20 改名辐射漂移在 audit.py 自身规则元数据上暴露——设计会话三轮递归追问到'系统残余面'为止（cwd/config/process/daemon/fs），审计器规则常量这一面在清单视野外，是 completion-as-recursion-floor (5/20) + stale-observer (4/15) 的活体（auto_gg 独占视角）。essence append 无（同主题已被三滴覆盖，不凑滴）。Agenda 无推送（无新议题）。auto_gg 不接管 Keith 在场产出（essence.md 4 滴 5/20 + 2 untracked reflections 5/20，不 stage）。"
last_decision_slug: "2026-04-22_threads-v1-architecture-review"
last_reflection_slug: "2026-05-18_global-claude-md-rule-budget-gate"
last_design_session_slug: "2026-05-16_gg-active-channel-to-keith"
```

**完整出场清单**：`ls memory/{archival,reflections,design_sessions,audit}/ | sort` 即可。
**变更历史**：`git log -- memory/state.md`。
**组件分类（KERNEL + 身体）**：见 `CORE.md §8`。**KERNEL.md 修改需 Keith 在当次对话中连续两次独立明示批准**（`KERNEL.md §2` 铁律 3）；身体（KERNEL 之外的所有文件）gg 在设计模式下可直接演化。
