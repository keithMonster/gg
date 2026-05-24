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
last_summoned_at: "2026-05-24 22:24 Keith 在场召唤 auto_gg 模式补跑（手动触发 SCAN/FOUND/DID）。working tree = 5/24 设计模式产物未收尾：M memory/essence.md（+1 滴 self-as-only-reference）+ M tracks/keith.md（+177 行 4-9 节 Keith 主动反馈窗口落地）+ untracked 2026-05-24_keith-inquiry-and-overprojection 设计反思。audit 退 0 / 0 违规。morning-brief 5/24 周报形态（本周三大发现：cc-assistant 2.0 收敛 / cg-platform 上线 dogfood / NW blocked 池二次涨满触发 v0.3.0），proposals.jsonl 5/24 无新条目（grep 0 匹配）。**本夜核心动作**：把 5/24 设计模式 working tree 三件一并归档 commit（按 auto_gg §1.2 KERNEL 外 commit ✅；同 5/16 last_design_session b16f9d6 先例）。**FOUND**：跨夜模式无累积 / 辐射死链无 / 跨 track 反哺已完整下沉无需补写 / NW 账本 5/24 全 0。**Keith 主动反馈窗口落地结构性增量**：(a) gg 第三条主动通道明示登记（对话内主动追问权，跟 push-last-run / daily-word 并列）(b) 项目寿命分层（monster 长期载体 / cgboiler+Voca 临时）修正 4/14 蓝图 ROI 框架 (c) Keith 时间结构首次明示（周末完全休 / 7:30-8:30 自由 / 8:30-17:30 工作）(d) `self-as-only-reference` 重型画像 essence 沉淀（外部偶像系统 ill-formed，决策锚点=自我累积+第一性原理）。Agenda 推送 2026-05-24 段。"
last_decision_slug: "2026-04-22_threads-v1-architecture-review"
last_reflection_slug: "2026-05-18_global-claude-md-rule-budget-gate"
last_design_session_slug: "2026-05-24_keith-inquiry-and-overprojection"
```

**完整出场清单**：`ls memory/{archival,reflections,design_sessions,audit}/ | sort` 即可。
**变更历史**：`git log -- memory/state.md`。
**组件分类（KERNEL + 身体）**：见 `CORE.md §8`。**KERNEL.md 修改需 Keith 在当次对话中连续两次独立明示批准**（`KERNEL.md §2` 铁律 3）；身体（KERNEL 之外的所有文件）gg 在设计模式下可直接演化。
