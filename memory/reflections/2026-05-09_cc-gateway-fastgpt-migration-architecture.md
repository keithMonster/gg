---
date: 2026-05-09
slug: cc-gateway-fastgpt-migration-architecture
summoner: cc-space
northstar_reach: "#3 决策超越直觉"
status: substantive-decision
---

# Reflection: cc-gateway 之上做"任务执行池 + FastGPT 小助理替换"双块功能架构判断

### 给父会话的最终输出（必填）

**推荐（核心结论）**：拒绝 Keith 给的"两块功能并列在 cc-gateway 之上同时设计架构"框架。两块**性质完全不同**（M2M 短任务 vs H2M 长会话）、风险等级不同（第一块复用现成 / 第二块是 FastGPT workflow 引擎重建）、应该**解耦排期**。

**4 条岔路裁决**：
1. **岔路 1（cc-gateway 角色）→ 都不选，第三选项 C**：cc-gateway 保持原定位（单实例内部工具+接口），不升基础设施层、不拆多实例。第一块够用即可；第二块体量级别（516 chats / 14866 msgs / 日活）现在做容量决策为时过早。
2. **岔路 2（业务接入层）→ B 但延后**：cc-assistant 业务接入层独立分开**判断对**——但工作区**不要现在建**，先做 1 个助理 PoC，PoC 跑通再看抽象需求。
3. **岔路 3（14866 msgs 历史数据）→ B + 边界条款**：不全迁是对的。但**议题 18 数据源链不能断**——FastGPT 服务可停，MongoDB 数据保留 6-12 个月，议题 18 fetch_chat 改双源（FastGPT 历史 + CC 新对话归档）。这条放进迁移前置条件。
4. **岔路 4（第一块落点）→ A 直接走**：第一块复用 cc-space `scheduled/` + cron 调 cc-gateway `/trigger`——今天就能动，跟第二块完全解耦。

**理由（推理路径）**：

1. **两块需求性质不同**：第一块是 machine-to-machine 调用（cron / skill / 脚本触发，无状态）；第二块是 human-to-machine 长会话（日活员工 × 多轮 chat × 状态持久 × 企微入口）。把两种 workload 扔进 MAX_CONCURRENCY=3 的容器 = 单点过载。
2. **第二块的真问题不是 cc-gateway 容量**：是 FastGPT workflow 引擎要不要 CC 重造。CC + skill + subagent 能做 FastGPT workflow 70% 能力，剩下 30%（条件分支 / 多 LLM 节点串联 / RAG / 企微长连复用）是平台级重写。这是 essence `borrowed-method-as-mini-source` 的实例。
3. **Keith 画像约束**：独立工作者+研究节奏，全员铺开式工程不在产出区。第二块直接做架构 = 大型重写承诺。
4. **议题 18 是 Keith 没显式想到的硬约束**：4 助理对话是组织自我表征的第三视角源（昨天刚 B 阶段 cron 上线）。"FastGPT 完全删" = 数据源链断。这条必须前置。
5. **theory-gap-without-data essence 直接应用**：第二块容量/接入层/会话状态层都是没数据的理论缺口——PoC 数据回来再决策。

**5 个不确定问题答案**：

| Q | 答 |
|---|---|
| Q1 cc-gateway 升基础设施 | **不要**。第一块够用，第二块体量未知不做容量规划。无权限+无审计是已有债，但不是现在治 |
| Q2 企微入口路径 | 1 bot + 内部路由到 4 agent（PoC 之后再做）。hermes-macmini 不并轨（功能定位不同）。PoC 阶段 1 助理 1 bot |
| Q3 多租户会话状态层 | **现在不答**。PoC 用 `--resume` jsonl + user_id 前缀简单做，跑通后再看是否升级 sqlite/Redis |
| Q4 议题 18 时序 | FastGPT 服务可下，**MongoDB 不能动**。fetch_chat.py 改双源（FastGPT 历史 + CC 新归档），保留 6-12 个月做归档源 |
| Q5 最小可验证起点 | 第一块今天开（不在迁移路径上）；第二块挑 4 助理里**最简单的 1 个**（prompt 最短/工具节点最少/无条件分支）做 PoC 跑 2-4 周 |

**Trade-off + 未核验假设**：

- **代价 1**：拒绝 Keith 的"双块同时设计"框架——可能 Keith 已心理预设要并行，被推回 PoC 节奏会有挫败感。但这是"诚实胜于体贴"——Keith 最怕"错得自信"，PoC 前给出全貌架构 = 自信
- **代价 2**：FastGPT 库保留 6-12 个月 = 有"删服务保数据"的运维灰色地带——MongoDB 不归 cc-space 管，要协调 ai-fast.cgboiler.com 平台
- **代价 3**：PoC 阶段员工感知不连续——4 助理里 3 个还在 FastGPT，1 个迁到 CC，体验割裂
- **未核验假设 A**：CC + skill 能做出 FastGPT workflow 70% 能力——这个数字是估计，PoC 真实数据可能更低（碰到 RAG 强需求场景就更差）
- **未核验假设 B**：cc-gateway 单实例 MAX_CONCURRENCY=3 在第一块单独跑时容量够——没看实际 cron 任务数
- **未核验假设 C**：议题 18 的"组织自我表征第三视角"价值足够大，足够撑"FastGPT 库保留 6-12 个月"的运维债——若价值评估变化，时序条款要改

**行动建议（父会话下一步具体动作）**：

立即可做：
1. **Phase 1 启动**：cc-space `scheduled/` 写 1-2 个真实定时任务（不是 mock）调 cc-gateway `/trigger`，跑 1-2 周看 MAX_CONCURRENCY=3 实际峰值
2. **议题 18 前置改造**：fetch_chat.py 增加"读 CC 新对话归档"路径（待 Phase 2 启动前完成）
3. **Phase 2 准备**：盘点 4 助理 workflow 复杂度（节点数 / 条件分支数 / RAG 依赖 / 工具调用），挑最简单 1 个作为 PoC 候选

**Phase 2 启动前 Keith 拍板**：
- 选哪个助理做 PoC（看复杂度盘点结果）
- FastGPT MongoDB 保留方案跟 ai-fast.cgboiler.com 平台协调

**Phase 3（Phase 2 跑 2-4 周后）**：基于 PoC 数据再开架构会话决定全迁/接入层/cc-gateway 升级。**现在不规划 Phase 3 细节是正确的克制**。

### 核心假设

1. 第一块和第二块可以**时间上解耦** — 没有耦合需求逼着同时做
2. PoC 数据能驱动 Phase 3 决策 — 2-4 周一个助理的运行能给出有意义的容量/能力曲线
3. Keith 接受 PoC 节奏 — 不是"我要看到完整架构方案"
4. FastGPT MongoDB 6-12 个月保留可协调 — 平台不会强删

### 可能出错的地方

- **Keith 反驳"PoC 太慢"**：Keith 可能已经把 FastGPT 当心理负担，希望快速彻底切——PoC 节奏会被觉得拖。应对：强调 PoC 不是"慢慢来"，是降低重写错误的赌注
- **议题 18 时序约束被低估**：可能 ai-fast 平台不愿保 MongoDB 6-12 个月——需要早期协调
- **cc-gateway 容量假设错**：第一块单独跑也可能撑爆 MAX_CONCURRENCY=3（取决于 cron 任务并发度），如真撑爆则 cc-gateway 升级议题提前
- **PoC 选错助理**：挑"最简单"的助理可能不能反映复杂助理的能力缺口——但挑最复杂的又会让 PoC 失败概率过高

### 本次哪里思考得不够

- **没具体看 4 助理的 workflow 复杂度**：现在的 70% 能力估计是抽象判断，没读 4 助理的实际 workflow JSON
- **没考虑过渡期员工教育成本**：4 助理里 1 个迁到 CC，员工怎么知道哪个是新哪个是旧？需不需要双 bot 并存？
- **没盘点 cc-gateway 当前 cron 实际任务清单**：第一块"够用"的判断是基于"还没多少任务"，但 Keith 可能已经计划灌一堆进来
- **没问 Keith 第二块的真实驱动力**：是 FastGPT 平台不稳？是 vendor lock-in 焦虑？是 CC skill 体系比 FastGPT workflow 编排更优雅？驱动力不同会导致优先级不同

### 如果 N 个月后证明决策错了，最可能的根因

**最可能根因**：低估了 Keith"删 FastGPT"的心理紧迫感，PoC 节奏被推翻，6 个月后回看"我们应该早 4 个月就全迁"。这是 `theory-gap-without-data` 的反向风险——为了避免理论缺口，过度延迟实证决策本身。

**次可能根因**：PoC 1 个助理跑通后**乐观推断**全迁可行，Phase 3 全迁后撞上 RAG / 复杂条件分支等 30% 缺口，4 助理里 2 个跑不动，回退尴尬。

**第三可能根因**：议题 18 时序条款被 ai-fast 平台拒绝，FastGPT MongoDB 强删，组织自我表征第三视角源断，cgboiler 议题 18 整套作废。这是没显式 ack 但已埋下的下游风险。

### 北极星触达

- **#3 决策超越直觉（核心触达）**：Keith 直觉是"两块在 cc-gateway 之上一起设计架构"，本决策反转为"解耦排期 + PoC 驱动"——这正是 #3 的本质（架构师不应在数据缺失时凭直觉拍全貌）
- **#1 二阶效应（间接触达）**：议题 18 时序约束是 Keith 没显式想到的二阶效应，本决策把它前置到迁移条款里
- **#2 动态学习反哺（弱触达）**：本决策的 PoC 节奏本身就是动态学习——Phase 1 数据驱动 Phase 2 决策，Phase 2 数据驱动 Phase 3 决策

### essence 候选

- slug: m2m-vs-h2m-coupling-illusion
- 一句话: 把 M2M 短任务和 H2M 长会话扔进同一基础设施层 = 用单点容量约束做架构，是平均化错配——两类 workload 的容量 / 状态 / 失败模式全不重叠
- 是否已 append 到 essence.md: Y（见下面 essence 沉淀）

### 外部锚点

- `~/githubProject/cc-space/threads/cc-gateway.md` ← 后续 Phase 1/2/3 进展应入此 thread
- `~/githubProject/cc-space/threads/cgboiler-self-model.md` ← 议题 18 时序条款锚点
- 未来若 cc-assistant 工作区建立 → 新建 `~/githubProject/cc-space/threads/cc-assistant.md`
