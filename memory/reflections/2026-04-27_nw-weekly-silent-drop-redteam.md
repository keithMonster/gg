---
date: 2026-04-27
mode: 工作
slug: nw-weekly-silent-drop-redteam
status: substantive-decision
parent_session: cc-space NW 周报第三轮根因复盘
---

# 反思

## 问题
父会话第三次定位 NW 周报核心指标失语根因（前两次：采集管线缺失 / 周报作者懒读），这次定位到 nw_prepare.py L297-315 的 split 切片主动丢弃「核心指标」「满意度分布」「回合类型分布」三段——装配层 silent drop。要红队挑战完整修复方案 A+B+C。

## 装配
- tools/red-team-challenge.md（同形态盲点检测 + 反例构造）
- personas/conservative.md（压一压"过激降级是否矫枉过正"）
- 物理实证（必备）：Read nw_prepare.py L1-346 / daily/2026-04-24-proposals.md / prompts/nw-weekly.md / nw-daily.md / Bash grep 7 天 daily section header / Read 04-25-proposals 验证 N/A 边界

## 判断关键
1. 父会话根因定位这次站住——L307-309 split 确实只截「行动优先级」段，主动丢弃指标段。物理证据成立
2. 方案有 6 处弱点 + 1 处新盲点：
   - 周度聚合算法没区分 micro/macro，N/A 日处理缺失
   - "段存在 → 降级"硬校验会被 04-25 N/A 合法情况和 04-20 前旧 schema 误触发
   - 同形态隐患没扫干净——prepare_daily 也丢 tool_error_rate
   - 周报作者真实失败模式是跳段，光调顺序压不住
   - 周回合类型应输出占比 trend，不是总量
   - daily 文件合并争议——保持分离（fast-slow-divide essence 直接对应）
   - 新盲点：Desktop Scheduled Task 独立会话，下游对装配漂移完全无感知 → 需要 schema 版本号显式化
3. 方向背书 + 精度不足。主要是降级阈值（核选项 vs 软标注）和算法（micro vs macro）这两处需要重写

## 输出
逐条 6 大挑战 + 1 新盲点 + 综合修订表 + 关键文件路径。修订表每行明确"保留 / ❌改 / 新增"，不模糊。

## essence 候选
**装配契约的 silent drop 不是 bug，是"切片视角默认丢弃所有未指定字段"的架构选择**——区别于"主动 filter"（明示丢弃）。同形态出现在 prompt section split / API response field selection / config TOML key drop。修复方向不是更多 guardrail，是把契约 schema 版本化、把"装了什么 / 丢了什么"显式化。

候选形态："schema-as-contract"——隐式装配是债，显式 schema 是资产。已有 04-21 transparent-rewrite-breaks-contract 在更底层，本滴是它在装配层的对偶。**但不强写 essence**——这一滴还需要再次出场验证是不是真"逼近一切的本质"，今天先不沉淀。

## 北极星触达
✅ 物理实证铁律守住——所有证据 Tool 核验，无补全
✅ 不附议——直接挑出 6 处弱点，不纵容
✅ 透明 expose 装配理由（红队 + 保守视角 + 物理证据）
✅ 跨项目边界处理——绝对路径写本 reflection 到 gg 项目

## 外部锚点指针
- cc-space/harness-engineering/scripts/nw_prepare.py（L297-315 silent drop 现场 / L232-244 同形态隐患 B）
- cc-space/harness-engineering/analysis/daily/2026-04-24-proposals.md（schema 完整样本）
- cc-space/harness-engineering/analysis/daily/2026-04-25-proposals.md（N/A 边界样本）
- cc-space/harness-engineering/prompts/nw-weekly.md（Step 1 / 2.1 / 5.1 修改点）
