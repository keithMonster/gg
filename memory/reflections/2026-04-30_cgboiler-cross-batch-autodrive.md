---
date: 2026-04-30
slug: cgboiler-cross-batch-autodrive
summoner: cc-space (cgboiler 架构主会话)
northstar_reach: #3 决策超越直觉（红线护栏 vs 自动化诱惑的张力，认知代价已付不能用"也许"对冲）
status: substantive-decision
---

# Reflection: cgboiler 跨 batch 自驱架构决策

### 给父会话的最终输出（必填）

**推荐**：路径 A（配置就绪触发自启），但用 **Keith ack flag 收紧"就绪"语义**——把 ready 从语法层（配置文件存在）升级为治理层（Keith 看过 sample 显式 ack）。不选 B（自动化诱惑，用质量换便利）、不选 C（用户期望落空）、不选 D（最危险——把 prompt 设计主体一致性这条偶对红线砍了，用 sample 验收做安慰剂）。

**理由**（穿透红线 §6 §7 + essence 三连验证）：
1. batch 切换的本质是治理决策——batch2-5 数据形态差异（决策内参/周报/会议/常规）决定 prompt 设计，prompt 设计是认知代价层（v0_lessons §2 + PRINCIPLES §4 已付过的代价），不是 LLM 能稳定自决的层
2. 路径 B 是 `wish-as-pain-laundering` 同形态——把"想自动化"洗成"也许差不多"，用已付认知代价换便利
3. 路径 D 比 B 更危险——arch tick 拟 prompt = 主体一致性（PRINCIPLES §6 偶对原则）被砍，5-10 sample 验收是安慰剂（盲点恰在 sample 没覆盖的样本类型里），50 sample 验收 = Keith 亲自做 prompt = D 没省任何东西
4. 路径 A 真价值不在"省 5 次决策"，在"省 5 次决策之间所有 idle/maintenance/L2 回炉/议题评估的等待"——占总工作量 ≥80%，决策瞬间留给 Keith 是 §6 §7 的必然代价

**Trade-off**：
- 接受：Keith 仍做 5 次实质架构动作（prompt 设计 + sample review + ack 启动）
- 换得：每次 batch 切换有强制 review gate，§4 边界 + §7 效果优先 不被"也许差不多"侵蚀
- 用户期望降级："自驱"从手段层降级为"半自驱"，但目的层（stage3 完结）可达
- 未核验假设：用户对"半自驱"是否买账（gg 判断目的层达成 > 手段层完整）

**行动建议**：
1. STAGE3_STATE.md 加 `## Stage3 总进度` 段——5 batch × 4 flag (fetch_ready / prompt_ready / sample_validated / authorized) 矩阵
2. POST_TICK_REVIEW.md §Step 9 改：当前 batch 全 ✅ → 检查 next batch 4 flag → 全 ✅ 自启 / 任一 ❌ 写 PENDING_DECISIONS + idle_complete
3. PENDING_DECISIONS.md 锁 batch 启动 ack 模板（Keith 改 yaml `authorized: true` 即解锁）
4. archive_progress.py 自然边界切（不切固定行数），size > 100K 触发，挂 arch tick §Step 7 末尾——架构主会话维度自决即可，但语义切点要选自然边界（batch 完结/议题闭环），不在 batch 跑半截切
5. STAGE3_ARCHITECT.md §4 明确：batch2-5 prompt 设计永远保留为 Keith 决策点，不工程化

### 核心假设

1. PRINCIPLES §6 §7 红线是真红线（不是建议）——已经验证（v0_lessons 是付过认知代价的产物）
2. Keith 异步备料工作流可行——他能在 batch1 跑的时候并行写 batch2 配置（基于"5-phase 自驱状态机已跑通"的事实推论）
3. cron 自驱的真价值在 idle/maintenance/review 而非 batch 切换——基于"4/26 片跑了"+5-phase 中 4 phase 是非决策类的事实

### 可能出错的地方

1. **Keith 真实诉求被我误判**——他说"希望整个 stage3 完结，cron 一直跑下去"，我把"自驱"当手段、"完结"当目的；但也可能他真的就是要"零介入跑完"，那 A 不达预期。概率 25%——但即便如此，也不能用 B/D 解决（红线在那），出口是回到对话层重新对齐目的层
2. **"配置就绪"的 4 flag 设计在工程层细节出 bug**——比如"sample_validated"具体怎么物化（写哪、谁验证、ack 形态），这层我没下钻，留给 arch tick 实现层。如果 flag 设计不当会退化成"ack 仪式化"
3. **"自然边界 archive"在 PROGRESS.md 当前结构里可能找不到清晰边界**——81.8K 文件如果是混合叙事（执行+议题+回炉穿插），切点选择本身可能成 sub-decision

### 本次哪里思考得不够

1. 没下钻 STAGE3_STATE.md 的 yaml 现状——`## Stage3 总进度` 段是不是已存在、和现有 batch1 进度字段如何对接，没去验
2. 路径 D 的 sample 验收方案我直接判死，但没量化"50 条 stratified sample"是不是真的 = "Keith 亲自做 prompt"——可能存在中间形态（如 30 条 + 红队抽查）我没展开，但展开 ROI 不划算（红线层判断已穿透）
3. 用户工作流的并发性假设没核验——Keith 在 batch1 跑的几小时里是不是真的会去写 batch2 配置（也可能他根本不在场，cron 触发时 batch2 永远 not ready，A 退化成 C）

### 如果 N 个月后证明决策错了，最可能的根因

**最可能根因**：用户的"自驱"诉求里"零介入"权重高于我估的——他不是想"批切换 review gate"，是想"跑完了告诉我"。如果是这样，A 路径每个 batch 切换 idle_complete 等 ack 会被体感为"还是要管"，flag 矩阵被觉得是仪式累赘。

那时的修复路径**不是**滑向 B/D（红线还在），是**承认半自驱是 §6 §7 的代价**，并把这个代价物化进 PLAN——让"5 batch 跨多周协作"作为设计承诺写在文档里，而不是埋在"想自动化但没做到"的张力里。这本身回到 essence `wish-as-pain-laundering` 的反面——把"红线代价"诚实命名，不洗成"功能"。

次根因：4 flag 矩阵在工程实现里退化为机械 checklist（Keith 不真看 sample，直接 ack），那 A 退化为 B。防御机制是 sample_validated 必须有物理产出物（≥10 条 sample 抽取报告 + 红线检查清单），不是单字段 bool。

### 北极星触达

**#3 决策超越直觉**——本决策的核心张力是"用户诉求 vs 红线护栏"，直觉做法是"找一个 elegantly 的中间路径"（D 就是这个直觉的产物）。穿透直觉需要承认：红线 §6 §7 是付过认知代价的产物，认知代价不能用"也许差不多"对冲——这是 essence `wish-as-pain-laundering` + `extraction-meta-inheritance` 的合并应用。

也部分触达 #1 二阶效应——B/D 的二阶效应是"污染 entity 卡片需机械摘除 + 重抽"，不是"抽得不那么精"，二阶代价 >> 一阶便利。

### essence 候选（可选）

- slug: red-line-cost-cannot-be-hedged
- 一句话: 已付过认知代价的红线不能用"也许差不多"对冲——hedge 的本质是把代价递延到下游不可见处。
- 是否已 append 到 essence.md: N（涌现度待评——这条跟 `wish-as-pain-laundering` + `extraction-meta-inheritance` 是同一根问题的不同切面，可能是已有结晶的衍生而非新结晶。本次先不沉淀，留待跨议题验证后再判断）

### 外部锚点（可选）

- `~/githubProject/cc-space/cgboiler/PRINCIPLES.md` §6 §7 — 红线物理底座
- `~/githubProject/cc-space/cgboiler/_pipeline/STAGE3_STATE.md` — 决策落地点（## Stage3 总进度 段）
- `~/githubProject/cc-space/cgboiler/_pipeline/POST_TICK_REVIEW.md` §Step 9 — 决策落地点（next batch ready 检查分支）
- `~/githubProject/cc-space/cgboiler/_pipeline/PENDING_DECISIONS.md` — batch ack 模板锁定点
- `~/githubProject/cc-space/threads/cgboiler-self-model.md` — 主体协作叙事（本决策应在此 thread append 一条 cross-batch-autodrive 决策记录）
