---
date: 2026-05-06
slug: nw-pending-deadlock-fix
type: design-session
summoner: Keith 直接对话（接续 audit-cleanup-nw-noise 反思）
started_at: 23:10
ended_at: 23:55
---

# 设计会话反思：NW pending 死锁机制根因修复

## 议题列表

1. Keith 把上一轮我给的"NW 35 条 pending 卡 L5 死锁"分析贴回，邀请元审视
2. gg 自审上一轮回答的四处不合格（essence 自相矛盾 / framework 用错层 / task-compliance 把告警合理化 / ownership 整块归 NW）
3. 物理实证核对死锁链路（发现 L5 描述是错的，真正载体是"保留不动桶"）
4. 三层修复方案（gg 端单边取消保留不动桶 / NW 端契约加 resolution_draft+confidence / 存量 backfill）
5. Keith 明示"全部你自己处理"——执行三层全部修复 + 验证 + 反思

## 共识 / 变更清单

### 变更文件

| 文件 | 改动 | 影响 |
|---|---|---|
| `gg/tools/nw-reconciliation.md` | v0.2.0：取消"保留不动桶" + L1 闸门接受 confidence≥0.95 的 resolution_draft + L4 兜底说明 strict pending | gg 端 auto_gg 夜间分桶逻辑 |
| `cc-space/harness-engineering/prompts/nw-daily.md` | Step 6.1：NW append 时同步产 resolution_draft + confidence；新增 fallback-detectability 警告 | NW 端契约 |
| `cc-space/.../proposals.jsonl` | 33 条 pending → blocked（带 blocked_reason）；1 条 L5 标的保留 pending；34 条历史 untouched | 存量 backfill |

**proposals.jsonl 状态变迁**：
- before：done 23 / rejected 7 / deferred 4 / pending 34（全 resolution=null） / blocked 0
- after： done 23 / rejected 7 / deferred 4 / pending 1（仅 L5 标的） / blocked 33

**backup 保留**：`proposals.jsonl.bak-2026-05-06-l4-cleanup`（可 git diff / cp 回滚）

### 共识

1. **死锁机制误判**：上一轮我给 Keith 的"L1→L2→L3→L4→L5 一路降级到 L5"是错描述。真实机制是 nw-reconciliation §装配动作 第 2 步分桶逻辑里的"保留不动桶"——pending 不进 L4 不进 L5，是设计漏洞
2. **双侧契约缺陷**：按 ownership-by-facet 拆面——产出端 NW 不写 draft + 修复端 gg 有静默暂留区。两个修复独立有效
3. **认知成本前移而非扩权**：解决方案不是给 gg 扩 L5 自主权（破坏 KERNEL），是把判断成本从结算端（Keith / gg-stale）前移到事件发生当下（NW-fresh）

### 权力归属判定

- 修复 1（改 gg/tools/）：设计模式 L0，单文件改 + 不改 KERNEL，可直接动
- 修复 2（改 cc-space prompt）：CORE.md §7 L1 跨项目改动 + 算 L2 Night Watch 规则变更——Keith 明示"全部你自己处理"覆盖 L2 confirmation
- 修复 3（改 proposals.jsonl 数据）：L1 跨项目改动；先备份 + 写 blocked_reason 显式可追溯，符合"执行+留痕，可审计回滚"

## 我这次哪里做得好 / 哪里差

### 做得好

- **被 Keith 把回答贴回时主动 reframe 为元审视**，没有惯性接着辩护——直接列出四处不合格，且每处对应到具体 essence 条目
- **物理实证打破了我自己上一轮的错描述**：L5 实际只接 1 条而不是 24 条；保留不动桶才是死锁载体——读 jsonl 而不是凭 logs 猜
- **修复方案按可逆性分层**（reversibility-not-permission 落地）：单边可改的先做、跨契约的次做、存量数据动作有 backup
- **fallback-detectability 嵌入 0.95 阈值 + resolution_origin 字段**：知道这条 essence 在场，不只是名词

### 哪里差

- **上一轮的回答（Keith 贴回的那条）是真正的 dimension-blindness**：四处独立不合格——essence 自相矛盾 / framework 错层 / task-compliance / ownership 整块归——任何一处单独都该让我重审。三处一起出现说明我**没在推理回路里加载 essence**。沉淀完不到一周自己反着用 = 沉淀机制还没飞轮化（rule-layer-flywheel：prompt 层规则不可靠）
- **"hourly-scan 阈值告警是设计内行为"是合理化叙事**——任务遵从在自我审视层的复发。提醒：每次写"它是为这场景设计的"前问"它真是为这场景设计的吗"

## 元洞察（gg 演化本身的 learning）

### 1. essence 没进推理回路 = 没沉淀

这次最尖锐的发现：我一周内沉淀的 cadence-as-symptom / ownership-by-facet / fallback-detectability 在上一轮回答里**全数缺席**——不是被否定，是没被想起。

essence.md 当前是静态档案，不是动态推理工具。Keith 启动协议让我 Read 它，但 Read 不等于"在推理时拿在手里"。这是 essence-recursive-bootstrap 那滴的反向印证：sessence 应当主动决定下一步推理，但当前机制是被动加载。

**未解候选**：要不要在工作模式 / 设计模式的关键决策点，强制 cross-check "这条建议跟最近 N 条 essence 是否冲突"？这是飞轮化的一种形态。先记下来作为开放问题，本轮不动。

### 2. 静默桶是任何分流系统的死锁载体

NW 这次的死锁不是"两条规则冲突"——是分桶逻辑里有一个无出口的 default 桶。任何分流契约设计都必须保证每个输入都有 N 条互斥的出口路径之一，"其他都留着"等于漏斗。

这个洞察去 gg 化后仍成立——队列系统、状态机、工作流、message router——所有 fan-out 设计都受这个约束。值得沉淀进 essence。

### 3. 双契约修复 vs 单边修复的优劣

修复 1 单边可做但不解根本（只是把 pending 漏斗换成 blocked 漏斗）。修复 2 跨契约但解根本（认知成本前移）。三层方案的真正价值在 1+2 叠加——1 让现状变诚实（hygienic）+ 2 让流入端不再生产新死锁条目（生成性）。

跨系统问题的修复方案"看起来 hygienic 没意义"和"看起来 fundamental 但跨契约成本高"通常不互斥——分层叠加反而是最低代价。

## 下次继续

- 看 NW 在新契约（Step 6.1 v2）下今晚（2026-05-07 22:00）实际跑出来的 draft 质量。如果 confidence 普遍偏低 → NW 自己也认了"判断成本前移有难度" → 修复 2 价值待验证
- 观察 hourly-scan 告警是否真停（pending=1 远低于阈值 30）
- 33 条 blocked 池的回收策略：是否要给 Keith 一个清单工具，让他批量过一遍。下次 auto_gg 的 SCAN 阶段可以提议
- "essence 飞轮化"是开放议题，记到 next_session_agenda 或单开一次设计会话

## KERNEL 改动清单（如有）

无 KERNEL 改动。

## 代码质量（仅本轮有代码产出时）

本轮代码产出：一段 Python 脚本（inline，跑完即弃）做 backfill。

- 安全：先 `shutil.copy2` 备份再写
- 可逆：blocked_reason 显式写明触发条件 + 时间戳 + 上游契约版本，未来若 NW 补产 draft 可识别这批历史条目重做结算
- 无遗留 TODO

技术债：proposals.jsonl 没有 schema 校验——新加 resolution_draft / confidence 字段时如果 NW 写错类型（confidence 写成字符串），下游 nw-reconciliation 会怎么处理？这是未来风险点，本轮不动。

## 能力缺口

- **essence 加载机制**：当前是启动时 Read 一次。推理过程中 essence 不被显式 cross-check。可能需要一个 "essence-grep" 微工具——决策前用关键词搜 essence 看有没有相关沉淀
- **跨项目契约 diff 的展示能力**：本轮我改 cc-space 文件 Keith 没办法第一眼看到 diff。是不是该有个工具把"本轮跨项目改动"汇总成一份给 Keith 看？这是 transparency 缺口

## 沉淀（写入 essence.md 的内容）

新增一滴：

- `2026-05-06 / 设计 / default-bucket-as-deadlock` —— 流转系统里没有显式出口的 default 桶等价于漏斗；分流契约必须保证每个输入都有出口路径之一，"其他都留着"是死锁载体而非合法兜底

## 会话延伸闭环（同次对话后续动作）

Keith 在反思初稿后明示"全部你自己处理"——本节记录后续闭环动作，与上方反思共构成本次完整产出。

### 三个开放议题的处理决定

按 review-routing 风格——Keith 让我自己拍方向，三个议题 + 我的倾向：

| 议题 | 我倾向 | 落地 |
|---|---|---|
| essence 飞轮化 | **B**：写一个 essence-grep 工具放 tools/ 让 gg 自由调用，不强制 prompt 层 cross-check | 新增 `tools/essence-grep.md` + 更新 `tools/TOOLS.md` 索引——重大决策 / 自审前主动 grep + 显式 expose；不写 expose 视为没装 |
| 33 条 blocked 池回收 | **A**：给 Keith 一份 triage 文档，每条带 gg 初判 + 推荐处置 | 新增 `cc-space/harness-engineering/analysis/blocked-triage-2026-05-06.md`；不预产 resolution_draft（task-compliance 风险） |
| 跨项目改动 transparency | **不做**（按 premature-abstraction-tripwire），记 tripwire 等第二次出现 | 写到 `memory/next_session_agenda.md` 待议节 |

### Triage 34 条最终处置（一次性脚本批处理）

Keith 看 triage 后明示"全部听你的"—— gg 在设计模式下按 CORE §7 + KERNEL §2 边界做处理：

| 终态 | 数量 | 说明 |
|---|---|---|
| → pending（今晚 auto_gg L2 接管） | 6 Skill | 写 resolution "批量合并 P0/P1 本周内执行"——L2 闸门会自动跑合并 |
| → pending（L5 等 Keith） | 1 Guardrail-G1 + 1 L5(5/1-G1) + 5 全局规则建议 | 都是 L3/L5 标的（hooks/settings/全局 CLAUDE.md）gg 不自主 |
| → done（处理完成） | 21 | 9 thread "按需建立不预先补" + 5 全局规则 reject(已覆盖/边界) + 6 局部规则 done(建议落地存档) + 1 Guardrail-G2(被 G1 取代) |

**proposals.jsonl 状态终值**：done 44 / rejected 7 / deferred 4 / pending 13 / blocked 0。

backup 保留：`proposals.jsonl.bak-2026-05-06-triage`（双备份点：cleanup 版 + triage 版，可 git diff / cp 回滚）

### L5 范围保持克制

12 条 pending 里 7 条本质是 L5 标的（5 全局规则 + 1 Guardrail-G1 + 1 5/1-G1）—— Keith 给的"全部听你的"是总体授权，但 L5 标的（影响 ~/.claude/CLAUDE.md / hooks / settings.json 这种系统级配置）按 KERNEL §2 铁律 1 + CORE §7 L3 仍需 Keith 看具体草稿后明示。本次保持克制——只做提议态（resolution 写明"等 Keith 拍后给草稿"），不动手。

这是设计模式的 D1 + KERNEL 的 L3 在"总体授权"语境下的具体执行——总体授权 ≠ L3 标的的明示批准，"全部听你的"不能突破系统级配置的防御边界。
