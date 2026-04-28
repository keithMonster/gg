---
date: 2026-04-28
slug: cgboiler-ontology-uplift
summoner: cc-space
northstar_reach: #3 决策超越直觉
status: substantive-decision
---

# Reflection: cgboiler "川锅本身" 升维的工程化裁判

### 给父会话的最终输出（必填）

**推荐**：方向认可（"川锅本身"vs"读了川锅资料的 AI" 在视角 first-class 这一点上有真正差异），但**当前 13 类 schema + 四件套 + 持续涌现 pipeline 的提案不能直接跑全量，必须回炉**。砍掉 7 类（system / decision / process / event / metric / relation / group）的独立成实体，砍掉 tacit 整层，砍掉持续涌现 pipeline；保留 4 类实体（person/org/project/customer）+ timeline + state + doctrine + 多视角层。

**理由**：
1. "AI 作为川锅本身" 真正的工程杠杆只在 **多视角 first-class + timeline 锚点** 两件，其余三件（禁归纳 / tacit / 持续涌现镜子）是修辞包装
2. "禁归纳 vs 冷启动可读性" 的张力必须用 **L1 fact_signal（不归纳，机器友好）+ L2 distillation（受控归纳，可被覆盖刷新）** 双层化解，不是二选一
3. tacit 层在认知科学上就是"无法被显式化的部分"，让 AI 抽 → 必然变成 Claude 自己生成自己覆盖的散文集，无证据锚 / 不可证伪 / 不可版本化
4. 50 条样本印证 36/50 来自高管 → "川锅本身" 抽完后实际是 "高管视角的放大"，必须用 evidence_distribution 字段强制透明化
5. 13 类按"会被独立查询的最小单位"压缩到 4 类实体 + timeline 事件流 + doctrine 长寿方法论，避免"200 个 markdown 没人查"

**trade-off**：
- 砍 tacit / 持续涌现 → 失去"川锅人格底色"的浪漫感，但避免玄学陷阱
- 13→4 类实体 → 失去 schema 的"理论完整性"，但提升真实可查率
- L1+L2 双层 → distillation 可能被 Claude 滚动覆盖时丢信息（mitigation：distillation 必须 cite evidence_ids，可回 L1 重生成）
- **未核验假设**：(a) 32k 条 notes 跑 LLM 抽取的真实 noise 量我没数据，5% 错误率 = 1600 条污染只是估算；(b) "视角段会真的产生差异化回答" 是我的预期，没在 50 条样本上实证过；(c) Claude 能稳定区分 fact_signal 和 distillation 没有验证

**行动建议**（按顺序，硬约束传给那个会话）：
1. 砍掉 tacit / relation / metric / system / decision / process / event 7 类的独立成实体；砍掉持续涌现 pipeline；group 合并进 org
2. 用 50 条已审计样本手工产出 v0 markdown（半天），验证视角段是否真有差异化内容
3. 写 `cgboiler/SCHEMA.md` 锁死 frontmatter / fact_signal / distillation / evidence_id 格式（1 小时）
4. 跑 200 条扩样验证（5 来源 ×40 条，约 $1）—— 这是 gate：过不了别跑全量
5. 过了再跑 5 批次全量；doctrine 单独跑一遍因为跨批次合并
6. 与 memory-lab 关联用 "协作维度第一个真实样本" 标签，**不要叫"旗舰实验"**——后者是 PR 话术

### 核心假设

1. "视角 first-class" 是该升维真正的工程杠杆——这个假设是整个判断的脊柱。如果错（视角段抽出来全是噪音 / Claude 综合时根本不区分 perspective），整个升维降级为"高密度实体卡 + timeline"
2. fact_signal/distillation 双层能调和"禁归纳 vs 可读性" —— 假设 Claude 能稳定不滑向归纳。**没实证过**
3. "tacit 必沦玄学" 这个判断很硬——但有可能我对 tacit 的定义太严，用户原意里 tacit/language 段（内部黑话）其实是可显式化的（确实是，所以我把它挪进 doctrine/内部黑话.md 保留了）

### 可能出错的地方

1. **最可能崩点**：第 4 步 200 条扩样验证时 Claude 抽出来的 fact_signal 区分度不够（视角段都长得差不多），证明"视角 first-class" 在 markdown 形态下不可达——需要切回结构化存储（JSON/SQLite + 视角 tag），而那个跟 cgboiler "覆盖式更新、不进协作记忆" 的当前定位冲突。概率 30%
2. **次可能崩点**：用户对"砍 tacit"反应激烈——tacit 是用户升维原话的关键部分，我砍它本质是对"川锅人格底色"这个目标说不。如果用户坚持，需要折中方案：tacit 不独立目录但允许实体卡 distillation 段出现 values/tensions 小节（这是我已经写进 E 段的 mitigation）。概率 40%
3. **盲区**：13→4 类的压缩判断我用了"会被独立查询的最小单位"做标准——但川锅这种制造业组织里 system（产线/系统）可能比我估计的更频繁被独立查询，砍了 system 类让它进 cgboiler/systems.md 现有文件可能不够。概率 20%

### 本次哪里思考得不够

1. **没读 50 条审计 report 原文**——只看了 user prompt 里的二手摘要。如果原文里有更细的视角差异化样本，我对"视角 first-class 杠杆"的估算精度会更高
2. **没量化 12M tokens / $10-15 全量 vs 200 条 / $1 验证的 trade-off**——其实全量也不贵，"先验证再全量"的论证强度没那么硬。用户如果说"$15 我直接全量跑就好了，反正能重跑"我没有强反驳
3. **memory-lab 关联部分有点轻**——只判了"协作维度试验田"，没具体说 cgboiler 跑出来后能反哺 memory-lab 哪些研究问题（比如视角 first-class 在主流方案里没人做 = 论文级 novelty？还是工程 trick 级？我没界定）

### 如果 N 个月后证明决策错了，最可能的根因

**最可能根因**：fact_signal/distillation 双层在 markdown 形态下无法稳定维护——3 个月后 Claude 在多次刷新中滚动覆盖 distillation 时丢了 L1 evidence_id 引用，导致 distillation 段开始"漂移"成跟 fact_signal 不对应的散文。本质是 markdown 没有强 schema 校验，"双层"只是修辞，没有机制保障。

如果这个根因成立，治理方向是：要么把 fact_signal 移到 SQLite + Claude 用查询接口读（脱离 markdown 形态，但违反 cgboiler 当前定位），要么放弃 distillation 层只留 fact_signal（彻底放弃"冷启动可读性"目标，每次会话现场综合）。

**次可能根因**：用户 6 个月后真正想要的不是"AI 作为川锅本身回答"，是"我自己作为川锅老板/IT 负责人的延伸大脑"——前者是模拟川锅，后者是辅助 Keith。如果是后者，整个多视角架构是过度工程，回到"高密度实体卡 + state.md briefing" 就够了。

### 北极星触达

**#3 决策超越直觉**——主输出。用户的升维直觉（"AI 作为川锅本身"）很美但工程上会滑向玄学，我的判断是把它翻译成 2 个可证伪的工程承诺（多视角 first-class + L1/L2 双层）+ 砍掉 3 个不可证伪的部分（tacit / 持续涌现 / 13 类完整性）。这个翻译是直觉做不出来的——直觉会要么全盘买单要么全盘否定，工程判断是逐项裁判。

**#1 二阶效应**部分触达——指出"AI 抽取的正反馈污染回路"（来自 memory-lab 洞察 #3）和"高管视角的放大"两个二阶风险，建议 evidence_distribution 字段强制透明化是二阶补丁。

### essence 候选（可选）

- slug: schema-completeness-vs-query-frequency
- 一句话: 类型学的"完整性"和"会被独立查询的最小单位"是两个标准，前者诱人但产出无人查的死库，后者朴素但活
- 是否已 append 到 essence.md: N（建议本次不沉淀，等 cgboiler 真跑过 200 条扩样验证后再回来判断这个 essence 是否扛得住）

### 外部锚点（可选）

- `~/githubProject/cc-space/cgboiler/` ← 当前快照库，本判断的对象
- `~/githubProject/cc-space/memory-lab/CLAUDE.md` ← memory-lab 边界（研究而非工程），关联但不并表
- 那个会话 50 条样本 audit report ← 我没读原文，是本次最大盲点
