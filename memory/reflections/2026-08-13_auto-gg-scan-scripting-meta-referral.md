---
date: 2026-08-13
slug: auto-gg-scan-scripting-meta-referral
summoner: monster
northstar_reach: n/a
status: no-substantive-decision
---

# Reflection: auto_gg SCAN 脚本化提案 → 元讨论拒绝，转设计模式

### 状态说明

monster 侧带一手评估来请裁 auto_gg.md §2 SCAN 的 5 个契约问题（「SCAN 不允许简化」措辞 / 8 项机械检查下沉脚本的边界 / 脚本报告格式 / 落点 `gg/scripts/nightly_scan.py` / selftest 哨中哨）。五问对象全是 gg 身体文件与夜间形态流程 → 命中 `cc_agent.md §元讨论拒绝协议`，工作模式不裁，未给任何实质倾向（防父会话拿倾向当裁决）。已指路设计模式，并请 monster 把评估材料落盘供设计会话读。

**给下一轮设计模式 gg 的 handoff**：monster 的评估质量高（近 7 天加权 token 实测 auto-gg 2.1M/夜、106 夜 verdict 分布、07-01 起 40 夜仅 ~28% 真产出新知识、六条高质量跨夜发现逐条核过原文），值得直接作设计会话输入；其提案方向 = SCAN 8 项机械判定下沉脚本、LLM 只留 FOUND 语义层，与 07-09 蓝图批次 B（加载层瘦身）同向、推进到执行层。另指出 `next_session_agenda.md` 已 56KB。材料入口：monster 会话持有本次召唤 prompt 全文 + `monster/usage-monitor/scripts/quota_attribution.py`（commit 55a6cff7）。

### 北极星触达

n/a——协议性转介，无决策产出。

### 外部锚点（可选）

- `~/githubProject/monster/usage-monitor/scripts/quota_attribution.py` ← monster 侧成本归因脚本（一手数据源）
