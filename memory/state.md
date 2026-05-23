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
last_summoned_at: "2026-05-23 22:26 夜间 auto_gg——SCAN/FOUND/DID 三段。working tree：M memory/essence.md（+1 滴 rule-with-half-pattern-self-violates，5/23 Keith 工作模式 reflection 产出）+ untracked 2026-05-23_communication-style-rule-review reflection。morning-brief 5/23 在场（纠正率 17% / 满意 83%，cookie-arcade 两轮迭代拉低；关键发现 1 = communication style 自违被 Keith 反问、已合入 G2 待评议）。audit 退 0 / 0 违规。**NW 账本**：5/23 NW 2 新 pending 全 L4——回写 monster proposals.jsonl status=blocked + blocked_reason（5/23-S1 done 衍生规则到 skill-auditor conf 0.75 但落点 references/ 非 SKILL.md / 5/23-S2 CDP Proxy 常驻方案 conf 0.3 研究方向类等根因），不 push monster。L1/L2/L3 全 0；L5 0 新（4 历史 L5 标的已在 agenda）。**auto_gg 独占视角**：5/23-S1 暴露 v0.3.0 候选 A scope 缺口（SKILL.md only vs +references/）+ NW draft 能力上限累积（5/6-5/23 confidence ≥ 0.95 占比 0%，L1 自动闭环路径零激活）。**跨场景反哺**：5/19→5/23 信息密度偏好升级链路 4 天完成（隐式偏好→跨场景实证→硬规则升级→元层 review），tracks/keith.md 补 dual-pattern 元规则层段。essence append 无（5/23 Keith 工作模式产出已含 rule-with-half-pattern-self-violates，不仪式性凑滴）。Agenda 推送 2026-05-23 段。"
last_decision_slug: "2026-04-22_threads-v1-architecture-review"
last_reflection_slug: "2026-05-18_global-claude-md-rule-budget-gate"
last_design_session_slug: "2026-05-16_gg-active-channel-to-keith"
```

**完整出场清单**：`ls memory/{archival,reflections,design_sessions,audit}/ | sort` 即可。
**变更历史**：`git log -- memory/state.md`。
**组件分类（KERNEL + 身体）**：见 `CORE.md §8`。**KERNEL.md 修改需 Keith 在当次对话中连续两次独立明示批准**（`KERNEL.md §2` 铁律 3）；身体（KERNEL 之外的所有文件）gg 在设计模式下可直接演化。
