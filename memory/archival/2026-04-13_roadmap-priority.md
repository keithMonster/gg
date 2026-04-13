---
date: 2026-04-13
slug: roadmap-priority
type: decision
summoner: Claude Code 主会话 (cc-space 工作区)
first_real_decision: true
reflection: memory/reflections/2026-04-13_roadmap-priority.md
---

# 决策档：cc-space 自我进化路线图优先级

## 1. 问题陈述

父会话在 cc-space 工作区对照 Hermes Agent 调研后形成 `harness-engineering/docs/self-evolution-roadmap.md`，提出 6 个候选项的新优先级排序（#5 升最高 / #1 #3 #4 降级 / #2 不变 / #0 已定），召唤 gg 做决策型审视。

父会话在召唤提示里自陈了 4 个不确定：
- #5 的 ROI 风险（多天任务密度未知）
- #1 对 CC 原生能力的依赖风险（黑盒）
- #2 的可行性（CC transcript token 分桶字段是否存在）
- 路线图本身的根本质疑（是否都是锦上添花，有没有被遗漏的根本空地）

**本次是 gg v0.1.0 的首次真实决策**，承载双重验证：
- 方案本身是否合格
- 7 步硬流程在真实任务上是否跑得通

## 2. 候选选项（输入空间）

| 编号 | 名称 | 原优先级 | 父会话建议 |
|---|---|---|---|
| #5 | 多天级任务状态机 | 5 | **1（升最高）** |
| #2 | Token 成本分桶 | 2 | **2（不变）** |
| #1 | L2 Session Search (FTS5) | 1 | **3 降为观察位** |
| #3 | periodic nudge (Stop hook) | 3 | **4 合并入 AutoDream** |
| #4 | Skill 蒸馏管道 | 4 | **5 降级** |
| #0 | 持久化策略分裂 | 最先 | **✅ 已定** |

gg 的核心挑战：**这是"新排序 vs 旧排序"的二选一问题吗？还是问题框架本身需要被挑战？**

## 3. 推理结构（本次专属）

**Cynefin 域判定：Complex**（4 条信号命中：核心变量未知 / ROI 依赖使用而非技术 / 效果需实际运行才能验证 / CC 原生能力是黑盒）

**选定 5 个原子模块**（有序）：
1. `CYNEFIN_ROUTING` — 定域
2. `SKETCH_MINIMAL_MVP` — 对每项砍到极致
3. `LIST_FAILURE_MODES` — 对两套方案都跑 pre-mortem
4. `COMPARE_TRADEOFFS` — 6 项矩阵
5. `RED_TEAM_CHALLENGE` — DECIDE 前最强反驳

**刻意不选**：IDENTIFY_QUALITY_ATTRIBUTES（不是技术选型）、INVERSION_DESIGN（与 FAILURE_MODES 重复）、RADIATION_CHECK（不直接改接口）。

## 4. 辩论记录

### 激进派核心主张
- cc-space 的真实目的不是"成为 Hermes"，是让 Keith 3-5 年大幅领先
- #1 #3 #4 全部砍掉——CC 原生水位观察是产品经理的活，gg 不做
- #5 的正确降规格方向是搬进 gg 内部（让 gg 每次被召唤时回读最近 7 天决策档），不是给 cc-space 加一个新 markdown
- #2 是 P0 的真正理由：决定 gg 能否被高频召唤（成本门槛）

### 保守派核心主张
- "砍掉 #1 #3 #4"会让下次决策仍然无信息——观察位 + 硬门槛比砍掉更稳
- "把 #5 搬进 gg"违反 P4 MVP FIRST 和 v0.1 组件锁定——这是 v2 的事
- 真正的不可逆性是心理不可逆（被评价为示弱），通过"建议执行方段的笃定度"消除
- #2 的"1h 一个函数"估计过于乐观——必须前置 30 秒的字段结构验证

### 关键分歧的处置
| 分歧 | 处置 |
|---|---|
| #1 #3 #4 砍掉 vs 观察位 | **接受保守派** 观察位 + 硬门槛（可量化 exit criteria） |
| #5 搬进 gg vs markdown 文件 | **接受保守派** v0.1 不扩权，markdown 够用 |
| 语气笃定度 | **两方融合** 建议执行方段极度笃定，Trade-off 段提供客观 escape hatch |
| #2 是 P0 的理由 | **接受激进派** 成本可见性决定 gg 的生存 |

## 5. 最终方案

### 投资顺序（gg 的正式建议）

**P0 — 立即执行（今日）**
1. **#2 Token 成本分桶 (2 桶版本)** — 作为信息基础设施
   - 前置 30 秒验证：读一条 transcript 打印 usage 字段结构
   - 若支持 `cache_read_input_tokens` 字段 → 2 桶（`固定开销` vs `增量对话`）
   - 若不支持 → 降级 1 桶（总 token）
   - 落地：`harness-engineering/lib/transcript.py` 新增 `token_breakdown(transcript)` 函数，`nightly_report.py` 增加一节输出
   - 工作量：~1-2h

**P1 — 本周执行**
2. **#5-min 多天任务 markdown 登记** — 阶段 0 观察工具
   - 新建 `harness-engineering/analysis/active-tasks.md`
   - 结构：每行一条，格式 `- [YYYY-MM-DD开始] 任务名 | 当前状态`
   - `nw_prepare.py daily` 读该文件，morning-brief 增加一节"跨日任务进展"
   - 不做自动化推进、不做 JSON schema、不做状态机
   - **硬门槛（阶段 0 的 exit criteria）**：
     - 观察期：2 周（截止 2026-04-27）
     - 触发条件 A：期末登记数 ≥ 5 → 升级到完整版 #5（新 JSON schema + 主动推进）
     - 触发条件 B：期末登记数 2-4 → markdown 版保留，不升级
     - 触发条件 C：期末登记数 ≤ 1 → **永久关闭 #5 这条线**，不再讨论
   - **escape hatch**：Keith 若直觉上已知自己跨天任务密度很高，可直接跳过阶段 0，当日升级到完整版
   - 工作量：~1h

**P2 — 并行观察（零行动成本，纯监测）**
3. **#1 + #3 合并为"CC 原生水位观察"**
   - 不做 SQLite FTS5、不做 Stop hook
   - 观察项（3 个可量化指标，阶段 0 期内每次真实触发时记录在 `harness-engineering/analysis/cc-native-watermark.md`）：
     - (a) 一周内"需要回忆上周做了什么"的真实触发次数
     - (b) 触发时 AutoDream memory 文件的直接命中率（命中 / 总触发）
     - (c) 未命中时 Keith 的修复成本（手动查 git log / 翻 transcript 耗时）
   - **阶段 0 exit criteria**：
     - (a) = 0 → **L2 Session Search 是伪需求，#1 永久 kill**
     - (a) ≥ 3 且命中率 < 50% → 启动 #1 完整版（SQLite FTS5）
     - 其他情况 → 继续观察或关闭
   - 工作量：观察纯被动，记录每次 ~30 秒

**P3 — 本周可选执行**
4. **#4 skill 蒸馏降规格** — 在现有 nightly_report 加一行
   - 不做信号识别逻辑、不做专门的报告模板
   - `nightly_report` 的 prompt 里增加一句："本日如发现 skill 蒸馏候选（成功的可复用任务模式），列出 1-2 条"
   - 有就列，没就静默（对齐现有 skill-notes "无发现则静默"原则）
   - 与现有 skill-notes 负面通道构成两条腿
   - 工作量：~15 分钟（改 prompt）

**P4 — 延后**
5. **#5 完整版** — 仅当 P1 阶段 0 触发条件 A 时晋升
6. **#1 完整版 FTS5** — 仅当 P2 观察触发升级条件时晋升

### 辐射检查清单

改动落地时必须同步更新：
- `cc-space/CLAUDE.md` 无需改（已完成 #0）
- `harness-engineering/CLAUDE.md` 「关键文件」表新增 `active-tasks.md` / `cc-native-watermark.md` 行；「操作指南」段新增"如何登记 active-tasks"一句
- `harness-engineering/lib/transcript.py` 新增 `token_breakdown`
- `harness-engineering/analysis/nightly_report.py` 增加成本结构段
- `harness-engineering/scripts/nw_prepare.py` 增加读 `active-tasks.md` 和 `cc-native-watermark.md` 的分支
- `harness-engineering/prompts/nw-daily.md` 增加"skill 蒸馏候选"一句
- 2 周后（2026-04-27）父会话自动读 `active-tasks.md` + `cc-native-watermark.md` 触发 exit criteria 评估

### 执行主体

**父会话今日可独立完成**：#2（P0）+ #5-min（P1）+ #4（P3）
**父会话本周起动**：P2 观察的记录流程启动（被动，每次触发时 30 秒记录）
**阶段 0 评估日（2026-04-27）**：由当时的父会话（或 Keith 直接触发 gg）读数据 + 应用 exit criteria

## 6. Trade-off（代价清单）

| 代价 | 承担者 | 感知时点 |
|---|---|---|
| **如果 Keith 跨天任务密度其实 ≥5/月，#5 完整版升级延误 2 周** | Keith（机会成本） | 2026-04-27 评估日 |
| **观察变借口的风险** | gg 信任资本 | 整个阶段 0 期内，若观察项没被认真记录则失控 |
| **"gg 只会给分阶段方案"的路径依赖** | gg 未来出场可信度 | 第三次召唤时 |
| **P2 的 3 个观察指标可能全是 0**（Keith 根本没有"上周做了什么"这类场景） | cc-space（无实质代价，信息依然有价值） | 2 周内 |
| **父会话如果认为 gg 在躲避干脆答案，信任受损** | gg 信任资本（心理不可逆） | 读到本决策的当下 |
| **2 桶 token 分桶如果字段结构不支持，降级 1 桶信息密度下降** | nightly report 数据精度 | P0 执行当日立刻发现 |

## 7. 可逆性

**方案类型：完全可逆**（所有组件可在 2 周内清零）
- #2 Token 函数：`git revert` 即可
- #5-min markdown：`rm` 即可
- P2 观察记录：`rm` 即可
- #4 prompt 改动：编辑 markdown 即可

**唯一非技术不可逆性**：gg 第二次出场如果被评价为"又是哲学家病"，信任资本消耗是**部分可逆但回滚代价高**（需要多次后续出场重建）

**消除手段**：本决策在"建议执行方"段采用极度笃定的语气，所有不确定性客观前置到本节。这不是示弱，是诚实的代价披露。

## 8. 置信度

**方案内容置信度：4/5**
- 不是 5 的原因：**Keith 跨天任务密度**这个未知变量可能让整个 #5 路径完全失效。我假设"2 周观察 + 5 个登记门槛"是可证伪的，但如果 Keith 根本不按"多天任务"这个概念组织工作，观察方法本身就错了
- 另一扣分点：#2 的 2 桶方案对 CC transcript 字段结构有假设，虽然前置了 30 秒验证但假设本身可能错

**表达笃定度：5/5**
- G4 触发的是表达不可逆性，不是方案不可逆性
- 建议执行方段毫不犹豫给出今日可执行的具体动作

## 9. 反思链接

`memory/reflections/2026-04-13_roadmap-priority.md`（本次续签执行前已写入，续签后追加本次 DEBATE / CRITIQUE / DECIDE 的新反思条目）

## 10. Track 更新（强制 P8）

本次决策产生 4 条 track 级洞察：

1. **tracks/keith.md** 新增开放问题：Keith 日常跨天任务密度（认知空洞，待阶段 0 数据补齐）
2. **tracks/cc.md** 新增开放问题：CC 原生 AutoDream 实际水位未知（待观察）
3. **tracks/architecture.md** 新增洞察：个人工具链 Complex 域识别信号 4 条（作为可复用启发式）
4. **tracks/ai.md** 已有同构洞察（gg v2 sqlite ↔ cc-space #1），本次不新增，但标记为"已被 cc-space 决策暂缓"

所有更新在 ARCHIVE 阶段同步落地。
