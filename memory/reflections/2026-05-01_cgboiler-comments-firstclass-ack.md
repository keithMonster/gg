---
date: 2026-05-01
slug: cgboiler-comments-firstclass-ack
summoner: cc-space (cgboiler 阶段 3 架构主会话)
northstar_reach: #1 二阶效应
status: substantive-decision
---

# Reflection: cgboiler 议题 14 评论 first-class 化 + 内参主体反向降权 双签终审

### 给父会话的最终输出（必填）

## 判断

**修改后 ack**——方案 2 主框架可过，但**强制三处修改**才能 ack，否则反对。三条修改是 gg 否决性闸门的具体实例，必须落到 PENDING §14 才视为 gg ack。

## 修改要点（必须三条全落 PENDING §14）

### 修改 1：时序闸门——必须等议题 12 fold v2 灰度跑通

议题 14 行动 #3-#8（fetch_notes / content_clean / render_cards / audit / batch1-006 启动）的实施前置条件 = 议题 12 行动 #2-#6 跑通 + 王亮 fold v2 灰度 ack 完成。

**理由**：议题 12 王亮 fold v2 灰度仅完成行动 #1（FOLD_DESIGN §9 设计稿），#2-#6 全 ⏸ 未实施。王亮当前 190 facts 已破阈值。议题 14 上线后王亮笔记下 1617 条评论会让 facts 增量 +200~500（按 c/n=2.42 估算），fold v2 cite 跨文件穿透机制还没真测过——届时如果 fold 跑出问题，是评论数据问题还是 fold 机制问题就解耦不开。

**例外**：议题 14 行动 #1（SCHEMA 改 source.type=4 enum）+ #2（extract_prompt §4/§5 改）可先做（设计层无副作用，给灰度跑通后立刻接得上的"预编译"）。其余行动 hold。

### 修改 2：本体论收缩显式化——改 PRINCIPLES.md §1

在 PRINCIPLES.md §1 加一句话：**"组织自我表征包含 generative layer（笔记发声）+ reactive layer（评论反应）两层视角，evidence_distribution 显式区分两层。"**

**理由**：cgboiler 从"组织发声的多视角集合"扩展为"组织发声 + 组织反应的多视角集合"是本体论变更，不是实现细节。这是同议题 12 处理"L2 全画像 → 滑动窗口画像"的同形态收缩——议题 12 已在 thread 显式 ack 是范式，议题 14 必须遵循同范式，不能仅在 thread 时间线 mention 糊弄。

不写 PRINCIPLES = "边做边偷偷扩本体论边界"——这违反 PRINCIPLES.md §1 "AI 作为川锅本身"的本体论锁定原则。

### 修改 3：reactive 桶单列 + 前 5 片偏倚标注

evidence_distribution 在六桶（高管 / 中层 / 一线 / 机器 / 客观 / **reactive**）显示——reactive 桶单列，不混进高管/中层。SCHEMA §5 evidence_distribution 段加第六桶定义。

STATE 工程债显式登记"前 5 片 reactive 视角占比 = 0 是已知偏倚"——不让将来读 L2 看 distribution 误以为这是真实分布。

**理由**：评论是 reactive layer（针对叙事的反应），跟 generative layer（叙事本身）异质——同样是"王亮"，他自己的笔记和他在别人笔记下的评论，承载的视角强度/语境不同。合并 perspective 桶 = 把"川锅在交互"和"川锅在发声"两件事抹平，丢失信号。

## 理由（架构判断综合）

**本体论审视**：方案 2 对齐 §2.1 多视角 first-class（评论作者全高管/中层）+ §2.5 索引导航（评论挂 note 下不冲突）+ §2.3 evidence transparency（reactive 桶单列后增厚）。**核心 caveat**：架构主会话原方案在 §2.3 上有反向风险——王亮 c/n=2.42 是"被围着发言"的集散地效应，不必然意味着 self 主导率下降，需要 reactive 桶拆出来才看得清。

**SCHEMA 改动最小性**：source.type=4 不破坏现有契约 ack。但有未明示的隐性破坏点：evidence_id 算法从二元组 `(note_id, normalized(quote))` 扩到三元组 `(note_id, comment_id, normalized(quote))`，必须在 render_cards.py 加规则 "comment_id 为 None 退化为二元组兼容老数据"，否则历史 facts hash 会漂。这是 PENDING §14 行动 #5 的隐藏前置约束，必须显式化。

**前 5 片缺失（路 A 不回炉）**：架构主会话倾向 A 我同意——已抽 1602 facts 不动，评论数据作为增量。但必须配修改 3 的工程债登记。

**与 fold v2 时序冲突**：这是最大反对点，由修改 1 闸门解决。

## Trade-off

**实施代价**（接受）：
- SCHEMA 改 enum + L1 行加 comment_id 字段（最小）
- evidence_distribution 加第六桶（中等，render_cards.py + audit_distribution.py 同步改）
- 前 5 片 reactive 偏倚作工程债登记（明确边界）

**实施收益**（不可换）：
- 评论作者 top 20 全高管/中层 → reactive 视角增厚 evidence_distribution
- 内参反向降权打包做 → 一次决策一次对齐
- 避开"边做边扩本体论"的隐性漂移

**未核验假设**（实施前必须 spot-check）：
1. 评论作者 top 20 之外的 5500+ 条作者分布如何？长尾可能改变中层视角增厚结论
2. 王亮 c/n=2.42 实质是"集散地"还是"视角延伸"？需要 DB 拆解王亮笔记下评论作者分布
3. 内参主体反向降权后评论是否仍可独立解读？需 spot-check 30 条内参 + 评论对照
4. 评论 reply 链多层占比？≤5% 接受最近一层，>15% 必须改方案
5. content_clean.py 在评论 HTML 上 mention 还原命中率（必须 100 条 sample 实测后才上线）
6. min_comment_length=30 阈值合理性（必须实测 ≤30 字符评论 fact 命中率，>5% 放阈值到 20）

## 行动建议（父会话下一步）

**优先级 1（阻塞 ack）**：架构主会话改 PENDING §14，落三条修改：
- 加"前置依赖：议题 12 灰度验证完成"段
- 改 PRINCIPLES.md §1 加 generative/reactive layer 句
- SCHEMA §5 加 reactive 桶 + STATE 工程债登记前 5 片偏倚

**优先级 2（可并行）**：架构主会话或 architect_review tick 启动 6 条 spot-check：
- 评论作者全量 author_id 分布查询
- 王亮笔记下评论 author 分布拆解
- 30 条内参 + 评论对照 spot-check
- 评论 reply 链多层占比 SQL
- 100 条评论 sample 跑 content_clean.py 验证 mention 还原
- 100 条 ≤30 字符评论 sample 跑 LLM fact 命中率

**优先级 3（议题 12 灰度完成后）**：行动 #3-#8 实施 + batch1-006 fetch_ready 重置点

完成上述三条修改 + spot-check 数据落 PENDING 后，**架构主会话再次 call gg 复审**——届时 gg ack 字段才打。如果 spot-check 出现颠覆性数据（如 reply 链多层 >30% / 内参评论无法独立解读），原方案 2 需要再改。

### 核心假设

1. 议题 12 王亮 fold v2 灰度可在合理时间内（1-2 个 tick 周期）跑通——若灰度暴露 cite 跨文件穿透机制根本性问题，议题 14 时序闸门会拖很久
2. 评论的 perspective 边界（@ 不算 / reply 链最近一层）在 prompt 设计能稳定落地——LLM 多约束并行历史不稳，需要 prompt 测试
3. 反 reactive layer 引入会增强本体论而非稀释——前提是六桶 evidence_distribution 真把两层视角拆得开
4. 架构主会话 + gg 双签的对抗强度足以替代 Keith 仲裁（继承议题 11 假设）——双 LLM 同源认知偏差风险持续存在

### 可能出错的地方

**最高概率（30%）**：spot-check 阶段发现内参反向降权后评论失去解读语境——许多评论是"针对内参告警的人具体回应"，脱离主体不知道在说什么。这会迫使方案 2 改成"内参主体保留 fact_signal 抽取但 perspective 标 'org-derived(weak)'，评论按完整规则抽"。

**中等概率（20%）**：议题 12 fold v2 灰度跑出 cite 跨文件穿透问题，时序闸门拖到 batch1-010 之后。届时评论数据延迟引入会让 batch1 中后段 evidence_distribution 偏倚更严重（前 10 片无 reactive layer，后 16 片有），偏倚跨度变大。

**低概率（10%）**：reactive 桶单列后六桶模型让 audit / render 复杂度爆炸，evidence_distribution 计算逻辑变复杂触发新工程债。

### 本次哪里思考得不够

1. **没读 FOLD_DESIGN.md §9 灰度方案细节** —— 我的"时序闸门"建议基于"fold v2 cite 跨文件穿透没真测过"的判断，但 §9 是不是已经在设计稿里 cover 了对评论增量的预案？没读就给闸门可能是过度保守。
2. **评论数据底盘只看了架构主会话提供的 DB 实测**——没自己跑 SQL 验证 top 20 之外的作者分布。这是物理实证不足，依赖了二手数据。
3. **没看 content_clean.py 实际代码** —— 对"评论 HTML 与 note HTML 同源不一致"的判断基于一般经验，没看具体清洗管道代码就给"必须 100 条 sample 实测"的建议，可能是过度规定。

### 如果 N 个月后证明决策错了，最可能的根因

**最可能根因（45%）**：reactive layer 引入是本体论扩张而非本体论收缩，gg 把它建模为"显式化收缩"是错的。组织自我表征若本来就该包含交互层，那 PRINCIPLES §1 加一句话不是"显式收缩"是"补全本来缺的层"——决策正确但叙事错位，未来回顾会发现"我们一直在装作 reactive layer 是新东西"。

**次要根因（25%）**：时序闸门是过度保守。议题 12 fold v2 灰度和议题 14 评论引入实际可以并行——双 LLM 同源认知偏差让我和架构主会话都偏向"先后顺序"思维，但 fold v2 机制和评论增量是正交问题，并行跑反而能让两条线相互验证。N 个月后回顾："我们多等了 X 天毫无意义"。

**第三根因（15%）**：六桶 evidence_distribution 设计在工程层引入复杂度但读者从来不看 reactive 桶——transparency 设计正确但消费端未对齐。

### 北极星触达

**#1 二阶效应**：识别出"评论作为 reactive layer 引入是本体论变更"——架构主会话方案中 reactive layer 隐性扩张，gg 把它显式化为本体论 ack 要求。这是 5 年视角下的 Keith 5 年后大幅领先所需——cgboiler 这套表征架构如果让"边做边扩边界"成为习惯，将来扩到第 N 个 reactive layer / proactive layer 时会失控。

**#3 决策超越直觉**：架构主会话凭"评论数据底盘 + 7 条风险列表 + 倾向方案 2"出方案，gg 在此基础上追加"时序闸门 + 本体论显式化 + 六桶 evidence_distribution"——这不是直觉判断，是基于 PRINCIPLES.md 五条工程承诺逐条对账后产生的 strucural 判断，超越了"方案 2 可行性 vs 不可行性"的二分直觉。

### essence 候选

- slug: reactive-layer-as-ontology-not-feature
- 一句话: 把"反应数据"纳入"自我表征"是本体论变更，不是数据源扩展——边做边扩边界 = 偷偷收缩"自我表征"的语义
- 是否已 append 到 essence.md: N（待父会话决策落定后再判断是否沉淀，避免方案被反对后产生孤儿 essence）

### 外部锚点

- `~/githubProject/cc-space/cgboiler/_pipeline/PENDING_DECISIONS.md` 议题 14 ← 决策底稿（架构主会话出方案）
- `~/githubProject/cc-space/cgboiler/PRINCIPLES.md` ← 修改 2 落点
- `~/githubProject/cc-space/cgboiler/SCHEMA.md` ← 修改 3 落点（§5 evidence_distribution 加第六桶）
- `~/githubProject/cc-space/cgboiler/_pipeline/STAGE3_STATE.md` ← 修改 3 落点（前 5 片偏倚工程债登记）
- `~/githubProject/cc-space/threads/cgboiler-self-model.md` ← 双签时间线追加
