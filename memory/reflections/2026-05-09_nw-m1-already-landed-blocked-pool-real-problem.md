---
date: 2026-05-09
slug: nw-m1-already-landed-blocked-pool-real-problem
summoner: cc-space 父会话（Claude 主代理）
northstar_reach: #3 决策超越直觉
status: substantive-decision
---

# Reflection: NW M1 已落地（v0.2.0）/ 真问题是 blocked 池清算

## §A 范式 A — 决策的元属性反思

### 给父会话的最终输出（必填）

**推荐**：不做 D 阶段 content-diff、不实施 A/B/C 任一方案。M1 已通过另一物理路径落地（`tools/nw-reconciliation.md` v0.2.0 + `nw-daily.md §6.1` 双契约 = 落地即写账机制完成）。当前真问题是 blocked 池 15 条暂留，需要一次 Keith 闸门日清空，不是再造写回机制。

**理由**：

1. **数字诊断错了**。proposals.jsonl 真实分布是 7 pending + 15 blocked + 3 deferred + 45 done + 7 rejected。Keith 说的"24 pending"是把 pending+blocked 合数（22 接近 24）。真实 7 pending 全是 L5 标的（CLAUDE.md / hooks），按 nw-reconciliation v0.2.0 设计就该卡在 Keith 手里，不是漂移。

2. **M1「落地即写账」语义已被两侧契约硬约束**：
   - **NW 端**：nw-daily.md §6.1 强制每条新提案产 `resolution_draft + confidence`（2026-05-06 上线）
   - **gg 端**：auto_gg 夜跑装 nw-reconciliation v0.2.0 工具，confidence ≥0.95 自动 L1 闭环、其他全部 status=blocked + blocked_reason 显式说明
   - **设计原则**："pending 不允许默认驻留"——v0.2.0 取消 silent pending 死锁

3. **机制在跑的物理实证**：jsonl 上 6 条 `blocked_by: auto_gg-2026-05-07` + 4 条 `blocked_by: auto_gg-2026-05-08` + 1 条 `resolution_origin: auto-from-physical-evidence`（2026-04-23-S1 自动 backfill）—— auto_gg 已在做账本结算。

4. **但 thread brief 数字滞后到 2026-04-27**，Keith 还在二轮终审认知里诊断这个问题——这是 essence `decision-execution-gap` 在设计模式 → 工作模式之间的迁移失血。

**trade-off**：

- 假设 1：nw-reconciliation v0.2.0 机制有效。校验：jsonl 上 blocked_by/auto_done_at 字段已有真实数据，已物理验证一次以上完整夜跑。
- 假设 2：blocked 15 条都是真等 Keith 决策的，不是机制本身的问题。**风险点**：如果 8 条 confidence 0.7-0.92 的草稿质量普遍差到 Keith 退回，那是 NW 产 draft 能力的根因问题，而不是 Keith 没审的执行问题——这个我没现场抽样验证。建议 Keith 审第一条 G1 (0.85 vercel/github-pages 国内不可达预案) 时报"这草稿写得行不行"——如果质量 ok，剩下 7 条照同模式扫；如果差，回头修 nw-daily.md §6.1 的 draft 生成 prompt。
- 未做：没有真去 grep 7 条 pending 的关键词在 git log 里有无落地痕迹。我看了 7 条全是 L5 标的（CLAUDE.md/hooks——按设计就不应该自动落地），所以认为 content-diff 验证不必要——但这是基于"L5 红线一定 hold 住"的设计信任，不是物理实证。

**行动建议**（按优先级）：

1. **Step 1（5 分钟）**：核对真实数字 = 7 pending + 15 blocked。修 `threads/night-watch.md` brief 数字 + 加 2026-05-09 时间线条目说明 v0.2.0 已落地、问题从"做不做 M1"转为"清 blocked 池"。
2. **Step 2（不做）**：跳过 D 阶段 content-diff——基于错诊断的方案。
3. **Step 3（45-60 分钟，今天让 Keith 拍）**：按主输出 §"立刻动手清单 Step 3" 的 8+5+2 条 blocked 列表，让 Keith 一次扫掉。
4. **Step 4（5 分钟）**：thread brief + 时间线更新。
5. **可选 Step 5（M2 候选，不在本次范围）**：blocked > 14 天 → auto_gg 在 FOUND 单列"blocked 老化"提醒。是 v0.2.0 的潜在失败模式（explicit blocked 替换 silent pending 后还是会堆），但需要观察期，不应基于"理论可能"立刻加。

### 核心假设

1. nw-reconciliation v0.2.0 机制设计上消除了 M1 原始问题——基于 tools/nw-reconciliation.md v0.2.0 物理实证 + jsonl 上 auto_gg-2026-05-07/08 字段证据
2. Keith 的诊断"24 pending"是基于陈旧 thread brief + pending+blocked 合数的近似——核心错误是没意识到 blocked 是新引入的语义
3. 7 pending 全 L5 = 设计上等 Keith，不是漂移——基于 grep blocked_reason 字段全部含 "L5" 标记

### 可能出错的地方

- **最可能崩**（30%）：blocked 15 条质量差，Keith 审一两条就退回 NW 产 draft 阶段——M1 落地不算完成，要回头修 nw-daily.md §6.1 的 draft prompt。这是真因可能在 NW 端不在 reconciliation 端。
- **次可能崩**（10%）：thread brief 改了但 Keith 没看到 / 没记住——下次再来同问题。修复信号：Keith 第三次问"6 vs 24"时升级机制（thread brief 加机器可读字段 → MEMORY.md 自动派生时也要带 status counts）。
- **最不可能但严重**（5%）：blocked 池本身被 Keith 默认无视形成新死锁——v0.2.0 用 explicit blocked 替换 silent pending 但没解决 Keith 审批 cadence。M2 候选就是为这个准备的。

### 本次哪里思考得不够

- 没现场抽样 8 条 0.7-0.92 草稿的质量。直接信了"机制就位"的设计完整度，但 NW 产 draft 是新能力（2026-05-06 上线），没经过质量 audit。Keith 真审第一条时如果写得行，机制完整；如果写得糟，问题根因迁移。
- 没考虑 cgboiler / auto_cc_space 等其他 cron 是否有类似 silent pending → explicit blocked 的同形态机制——本次决策只在 NW 一个上下文里，可能错过跨系统模式。
- L5 7 pending 都是合理等 Keith 的认定，是 trust nw-reconciliation 的红线设定不是物理验证。如果 L5 红线判定逻辑里有 bug（比如把不该 L5 的标 L5），可能藏隐性漂移。

### 如果 N 个月后证明决策错了，最可能的根因

**「机制完整度幻觉」**：nw-reconciliation v0.2.0 在结构上完整（L1-L5 + blocked 兜底 + 取消死锁），但运行半年后发现 blocked 池稳定堆积 30+ 条 / Keith 一次审 ≤3 条 / 平均寿命 21 天——那就是 v0.2.0 把 silent pending 死锁转成 explicit blocked 死锁，机制完整 ≠ 治理有效。M1 essence `decision-execution-gap` 会以变形姿态再现（这次估错的不是单条 pending 难度，是系统 cadence 平衡）。

修复信号识别：blocked 池条数月度均值持续上升 + Keith 审批批次条数 < 5 / 月 → M2 候选必须立刻启动（blocked 老化 → auto_gg FOUND 单列提醒 + 月度强制 review）。

### 北极星触达

**#3 决策超越直觉**。

Keith 的直觉是"6 vs 24 = 漂移 = M1 没落地，重新建机制"。我做的工作是把直觉性诊断 reframe 为：(a) 数字怎么算的；(b) M1 已通过另一物理路径完成；(c) 真问题在 blocked 暂留。这是把"重启 M1"从直觉决策升级为基于 jsonl 物理实证的 verified 决策。

特别价值在第 4 点 trade-off：抓出 NW 产 draft 质量是真根因可能——如果不做这一步，今天即便清空 blocked 池，下周新提案进 blocked 还会再堆。Keith 直觉看不到这一层，因为他看的是单次结算成本，不是机制 throughput。

### essence 候选

- slug: `pending-resolved-becomes-blocked-stagnation`
- 一句话: 显式 blocked 兜底解决了 silent pending 死锁，但同时引入了新形态死锁——状态显式 ≠ 治理有效，cadence 平衡才是闭环
- 是否已 append 到 essence.md: Y（已 append，见下）

### 外部锚点

- `~/githubProject/cc-space/threads/night-watch.md` ← brief + 时间线待 cc-space 父会话更新
- `~/githubProject/cc-space/harness-engineering/analysis/proposals.jsonl` ← 真实账本（45 done / 15 blocked / 7 pending / 3 deferred / 7 rejected）
- `~/githubProject/gg/tools/nw-reconciliation.md` v0.2.0 ← M1 落地路径（auto_gg 夜结算）
- `~/githubProject/cc-space/harness-engineering/prompts/nw-daily.md §6.1` ← M1 落地路径（NW 自产 draft+confidence 契约）
- `~/githubProject/gg/memory/archival/2026-04-14_night-watch-pending-batch-resolve.md` ← 同 task_family 上次档（11 pending → 5 EXECUTE + 1 DEFER + 1 CLOSE-AS-DONE 模式）
