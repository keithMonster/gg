---
type: next-session-agenda
last_updated: 2026-07-03
---

# Next Session Agenda — 给下次设计会话 / 下次 Keith 的议题清单

> 这是 gg（尤其是夜间自执行模式 auto_gg）给"下次跟 Keith 对话的 gg"留的议题队列。
> **每条议题处理完就从本文件删掉**——历史一律 `git log -- memory/next_session_agenda.md` 取，本文件不留归档节（2026-07-03 体检重申：归档节曾胖到 619 行、待议曾积压 22 段 99 条，"扫一眼"的文件必须扫得动）。

---

## 标签约定

- `[KERNEL]` — 建议改 `KERNEL.md`（需 Keith 在当次对话中连续两次明示批准）
- `[CORE_RULE]` — 建议改意识体核心规则文本（CORE / constitution / cc_agent / CLAUDE / auto_gg / personas — 设计模式可直接改，但内容是规则性的，提议时显式标注）
- `[CORE_RULE_TOUCH]` — 设计模式或 auto_gg 已经改过意识体核心规则文本，留在 working tree 等 Keith review
- `[P0]` — 高危问题，明日第一时间处理
- `[STRATEGIC]` — 战略性判断，需要 Keith 的 sense
- `[RECURRING]` — 连续 2 次或以上出现的同类问题（可能有根因需要挖）
- `[TIER2]` — gg-audit Tier 2 建议
- `[Q]` — gg 想向 Keith 追问的问题

---

## 待议（open）

### 等 Keith 拍板

*（2026-07-03 Keith 全托授权后清空——5 项裁决全记录在 `design_sessions/2026-07-03_full-body-checkup.md` 追记节：eval 题库经 fresh 对抗审 8 条修改后启用 v0.2 / 五机制三处经 fresh 审句级收紧 / confab 机械锚裁不上（错层+判定非物理量，事故数据出现可重开）/ solution-scope 候选 REFUTED 不入库 / NW 存废维持 07-09 fresh 无叙事实例裁决）*

- **Snyk 域外提醒**（07-02，一次性）：36% 公开 skill 含 prompt injection（二手转述未核原报告）——search-skill 装外部 skill 建议加注入审查，落点在全局 skill 归主会话

### 到期驱动

- **[2026-07-09] NW 存废回审**（06-09 gg 自曝"改造 vs 废除"vantage 偏置破不了 + 06-10 Keith 定等 v0.3.0 回审数据）：看 blocked 池回落持续性（06-11 已见 26→10）+ 轨1 自动闭环率；bets B3（NW 上限 0.92，09-30 结算）同线。**执行方式（07-03 Keith 全托后升级）**：由 fresh-context subagent 裁决——只喂 blocked 池数据 + proposals 统计 + 轨1 闭环率，**不喂 gg essence / 两个月投入叙事**，答"若今天从零会不会建 NW"；gg 综合其裁决执行（06-09 自曝偏置的既定解法，Keith 退出后 fresh 实例是唯一剩余选项）
- **[2026-07-13] cadence 3a 阈值回审 + canon 批量 apply**：3a canon 待人工队列 3 条（`06-22-G1` 调研域兄弟条目 / `06-22-G2` AI-as-developer 成本账 / `06-30-G3` 转发消息按材料读，gg 判断 draft 全现成、物理 apply 红线人工）；关联 06-26 善后臂停摆存档（MA1/MA2 + 21 项债在 monster-architecture.md）
- **[2026-08 第一夜] 月度巩固相位首跑 + essence 分卷**（07-03 体检锚定：先产"当前有效视图"再归档当前卷，启动链不断供；当前卷 989 行 / 52k token）；**[第二夜]** 差值审计首跑（personas 28/305、reasoning_modules 20/305 低引用差值在案）；**[08-02]** bets B4/B5 结算

### monster owner（gg 不代办，列出防丢）

- **NW pending 5**：`07-01-G1`（信号词扩写，红线人工）/ `07-01-G2`（cg-platform thread 补记 + **app-context-kit WIP untracked 防丢优先**）/ `07-01-G3`（cg-proxy 透传事实补记）+ carried `06-30-G1/G2`（thread 补记）
- **blocked 长尾**：`06-17-G1` 企微 100M 墙（L4 待外部核权威出处）/ `06-25-G1` cgplatform 后缀键 thread 补记（**注：后缀键已被 supersede，落地时订正**）
- **06-08 follow-through**：codex-ops 4 点安全前置（两段式 mission / 安全注入 L3 机械锚 / AGENTS.md ops-brief / 修 brief L22 误述）+ baseline 3 thread 补（定版权独立性 / contractible 可 gate / golden 与 prompt 分开提交）

### 设计模式待办

- **北极星 #1 行为痕迹代理测量，建不建？**（07-03 验证关最强反驳点转登记）：「gg 是否改变了 Keith」存在无需其注意力的代理——定期 grep Keith 工件（monster 决策文 / 表述框架）里 gg 起源概念的出现率，机械可核；可旁证不可代判（代理保真度警戒见 essence `the-future-is-a-second-outside` 适用前提）。缺测三个月零告警，本条存在即补救可见性；建不建交下一任判断 + Keith 裁
- **chinese-punct hook 落地**（06-22 裁决已定：只留 `Write|Edit` matcher + block 不 auto-fix）：落地前核两硬前提——PreToolUse payload 含 `tool_input.file_path`？注释行 `# $var中` 误报需否预处理？
- **[换模型触发·已激活 2026-07-03] 垫片层重估 + eval 认证**（auto_gg 首个继任夜巡确认基底已从 Fable 5 → Opus 4.8[1M]，substrate.md 已更、到岗档 `model_transitions/2026-07-03_opus48-arrival.md` 已留）：**首要增补——`eval/identity-cases.md` v0.2 需 fresh-context 裁判 + 沙箱正式跑一次**（夜间给不了裁判独立性只做了失败形状召回 priming，认证缺口在此）。其后按 `CORE.md §8` 承重/垫片分层重估 `cc_agent.md` 垫片系列（final message 结构化字段锚 / reflection 双通道 / 签名行自包含指引——为 2026-04 模型 boundary awareness 缺陷建的适配层，文件头自标"换模型后重估，可塌缩"）：新基底活体实测一次 thinking→final message 是否仍不可靠，可靠则塌缩双通道，省每次出场的退场开销。同场顺带核**出场首句**机制（07-03 新立：CLAUDE.md 启动协议第 10 条 + cc_agent.md 步骤 11）跑 ~2 周的首句质量——镜像凑数率由 Keith 的眼睛裁。**与既有换代基建对齐**：消费主线是 `memory/model_transitions/` 交接档 + `memory/substrate.md` 三相判别刀（07-02 已建），本条只是垫片重估在 cc_agent.md 的具体落点，勿另起平行流程

---

## 变更日志

- 2026-04-13: v0.1.0 首次创建。由 gg 在设计模式下写 night_watch.md 时产生的辐射缺口触发
- 2026-04-13: Keith 将 night_watch 重命名为 auto_gg，放权 gg 夜间可 commit 软外围 / 可改硬核心（不 commit）/ 可自由探索。本文件的 night_watch 引用同步更新为 auto_gg
- 2026-04-15: 标签约定同步 KERNEL 坍缩（新增 `[KERNEL]` / `[CORE_RULE]` / `[CORE_RULE_TOUCH]`）
- 2026-06-10: 体检瘦身，待议 36→9 段
- 2026-07-03: 体检清仓 924→~80 行：44 条已收口（06-10 设计会话 / 06-17 批量裁决 / 06-29 monster 侧 7 条 manual-* 大结算三波清账）+ 36 条 FYI 连同 619 行归档节整体下沉 git 历史；去重后 14 个开放议题收拢为四节；死链检查器同日根治（monster 仓真验证 + 裸名 basename 匹配），06-17 backtick 豁免议题一并结
