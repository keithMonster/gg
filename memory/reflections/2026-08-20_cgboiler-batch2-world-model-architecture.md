---
date: 2026-08-20
slug: cgboiler-batch2-world-model-architecture
summoner: monster / cgboiler
northstar_reach: "#1 二阶效应 / #3 决策超越直觉"
status: substantive-decision
---

# Reflection: cgboiler Batch 2 时态世界模型架构

### 给父会话的最终输出（必填）

**推荐**：不要把 Batch 2 定义成“给现有卡片再加投影层”，而要把承重墙改成**证据支持的时态断言模型**：关系不是图上的边，而是“谁在何时、以何种角色、对谁/什么做了什么或处于何种关系”的 assertion。图、人物 360°、时间线和问答上下文都只是该断言模型的可重建投影。

**目标定义**：“近乎全知”不是收齐所有文件，而是对限定川锅问题能返回已知断言、冲突、来源、有效时间、覆盖边界与未知；“全能”是另一个行动平面，只指基于该世界模型规划并调用已授权工具、验证副作用，不由知识量自动获得。终态是**可审计的川锅时态世界模型 + 授权行动智能体**，dataset 只是底座，不是目标。

**稳定分层**：① 原始来源/证据封套（源系统记录、快照版本）是“当时看见了什么”的 SSOT；② entity registry 是 identity/alias/kind/lifecycle 的 SSOT；③ assertion ledger 是 cgboiler 对事实、事件、状态、评价、业务关系的结构化解释 SSOT，每条须有 perspective、business time、evidence；④ graph、实体卡 L2、冲突/分布、timeline、人物 360°、背景快照联接均为可重建 read model；⑤ reasoning answer 只在查询时组装并输出证据链/冲突/未知；⑥ agent action 与知识层隔离，授权和副作用验证独立治理。现有卡片需按 section 看：frontmatter identity + L1 是 SSOT，L2/distribution/conflict/Related/graph 是派生或导航。

**SCHEMA 最小不可回避改动**：一是稳定 `entity_id`，关系端点不能继续依赖路径/名称；二是把 `relation` 从 wikilink 导航升级为 evidence-backed assertion，最小字段为 assertion_id、predicate、participants+roles、occurred_at/valid_from/valid_to、perspective、evidence_ids；三是 source 从 note_id 单型泛化为可引用 note/chat/db_snapshot/document 的 evidence_ref，并区分记录时间与业务有效时间。不要新增 relation 实体目录、不要先造全局完美谓词表、不要回填 800 卡。`Related` 暂留导航；共同 evidence 只表示同证，不推断关系。五份背景快照先按真实问题逐个接 source adapter，本切片只接 `org-structure.md`。

**Batch 2 唯一首切片**：做“王亮 2026 Q2 人—事—时—关系 360°”查询闭环，而不是做通用 Atlas/UI。范围只含王亮、该时间窗直接触达的组织/人/项目/客户/doctrine，以及 org-structure 2026-04-28 快照；从真实问题反推不超过约 10 个谓词，手工建立小批可审计 assertions，不做历史全量回填。

**验收问题**：1) 截至 2026-04-28 王亮有哪些正式岗位/兼任，来源与有效时间分别是什么？2) 2026 Q2 王亮对 A01 做过哪些动作/交办，涉及谁，哪些仅是同证共现？3) 他把哪些任务交给张吉峰/詹晓东/陈茂义，交办内容、时间、对象、证据是什么？4) 其数字化/制造主张中 self、他者与客观记录有哪些印证或冲突？5) 王亮是否批准 A01 LOT2“未批先建”？若无直接证据必须明确“不知道”，不能从总经理身份推断。每个事实性子句可回证据、每条关系有方向/角色/时间、已知冲突不被抹平、负向题不脑补，才算通过。

**淘汰方向与 trade-off**：卡片+投影优先能快出效果，但只是把现有语义损失做得更好看；通用知识图谱优先理论完整，却会诱发谓词爆炸和无边界回填。断言优先的代价是首批可见关系更少、需要人工定谓词，但它首次让后续任何视图都可证伪、可重建。

**最可能失败的 3 种方式**：① 把 Related/共同 evidence/共现直接当业务关系，生成“连接很多但不知道关系是什么”的假全知；② 一开始设计全川锅本体并回填 800 卡，标注口径漂移，Batch 2 变迁库工程；③ L2、graph 或 agent 推理被写回 SSOT，形成模型引用自己输出的反馈污染，尤其把“未发现”偷换成“不存在”、把岗位偷换成亲自批准。

**行动建议**：父会话应先冻结上述逻辑边界和 5 道 golden questions，再设计物理载体；不要先改 Atlas，也不要一次接五份快照。首切片通过后，按“新真实问题需要且现有谓词装不下”才扩本体。

### 核心假设

真实问题可把首批谓词压到小集合；王亮 Q2 足以同时压测 entity、snapshot、relation、time、perspective。若它只测出人物摘要价值而没有跨实体追问，切片会偏。

### 可能出错的地方

最可能是 relation assertion 人工成本被低估，或把“手工小批”误解成永久人工维护；其次是当前源快照覆盖更新，缺历史版本导致 valid time 只能证明单一时点。

### 本次哪里思考得不够

没有统计王亮 Q2 真实可提取 relation 数与谓词分布；首批约 10 个谓词是封顶建议，不是实测最优值。

### 如果 3 个月后证明决策错了，最可能的根因

首切片被做成王亮专属 dossier，predicate 与 participant roles 没能复用于第二个人/项目；那说明验收只测内容丰富度，没测模型迁移性。

### 北极星触达

#1：把“全知”从覆盖量翻转为可校准的已知/冲突/未知；#3：推翻 projection-first 的直觉，把 assertion 定为承重原语。

### essence 对齐自检（必填）

- **对位**：`ontology-expansion-velocity-needs-cap`、`separation-need-is-not-topology-verdict`、`new-source-as-ontology-not-feature`、`ssot-distillation-vs-buffering`、`backfill-is-the-channels-native-act-not-a-decision`。
- **反着走**：与“先试最轻治理形态”有表面张力；本案已由 `build_graph.py` 物理证明 wikilink 丢谓词/方向/时间/证据，现有层确实装不下业务关系，因此新增 assertion 语义而非先造新目录。
- **关键词**：ontology / 本体 / relation / 关系 / entity / 实体 / evidence / 证据 / graph / view / projection / backfill。

