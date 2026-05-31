---
date: 2026-05-31
slug: workmode-skill-gap-audit
summoner: monster
northstar_reach: #1 二阶效应（看穿"知识覆盖 ≠ 工种心智覆盖"，抓出被话术打发的真缺口）
status: substantive-decision
---

# Reflection: 工种 skill 缺口盘点的红队 + 3 个 CLAUDE.d 补强裁决

## §A 范式 A — 决策的元属性反思

### 给父会话的最终输出（必填）

**三条裁决 + 一处红队修正：**

**问题 1（"不缺工种 skill"成立吗）—— 基本成立，但有一处被"多载体覆盖"话术打发的真缺口 = `data-engineer`（数据/SQL 工种心智）。**
- 红队判据（从物理读的 ops-engineer / frontend-architect 两个已存在工种 persona 反推）：工种 persona skill 的本质 = "以某工种身份思考的心智信条（动手前先问哪三件事）+ 该工种在 CG 系统的特定地形"。ops-engineer = "运维事故的母亲是变更，每动作先答三问" + Phase 0 读 DEPLOYMENT.md；这是**心智**不是知识。
- 对照 agent 的"已覆盖"打发逐条过：SQL/数据库工种 → agent 说 `database/CLAUDE.md` 覆盖。**物理读了 database/CLAUDE.md：它是库清单+凭据+表结构+连接方式，纯知识文档，零工种心智**。它告诉你"cgManager 在哪、表长什么样"，但不告诉你"作为数据工程师写一条 prod 查询前先问什么"（5.7 无窗口函数怎么绕 / test-prod 共库写的爆炸半径 / EXPLAIN 先行 / 大结果集先 LIMIT 探）。这些数据工种心智散在 Engineering Rules #2 和 SQL 翻车教训里，没有 persona 收拢。
- data-engineer 之于 database/CLAUDE.md，跟 ops-engineer 之于 DEPLOYMENT.md **完全同构**——不重复表结构，加"数据工程师怎么想 + 指向 SSOT"。
- 其余候选 agent 判对：后端 API（cg-platform 规范=机制非工种，部分覆盖✓）/ 企微（工具型 skill 够用✓）/ 知识图谱（频次2+未成熟，研究范畴✓）。
- agent 为何漏 data-engineer：判据用了"有没有载体提到这领域"（命中 database/CLAUDE.md 就打勾），正确判据是"有没有**工种心智**载体"——`vantage-contaminates-verdict` 活体，"找文档覆盖"视角系统性把知识覆盖误判成工种覆盖。**Keith 担心的"被 database/CLAUDE.md 草率打发"直觉对了。**

**问题 2（3 个 CLAUDE.d 补强做不做）—— 全不做，Keith 判对。**
- 定性：3 个补强是 `theory-gap-without-data` 教科书活体。"系统复盘还缺哪些工种 skill" = 主动找缺口任务，工种缺口=0 后 task-compliance 不允许 agent 空手而归，降级到 CLAUDE.d 层生造 3 个填补"必须有产出"压力。
- 共同特征 = 无真实翻车样本驱动：扩 fastgpt.md（现 skill+CLAUDE.d 已覆盖）/ 新建 llm-engineering（prompt-writer skill + monster Prompt Writing 段已覆盖）/ 新建 wecom-integration（wecom-smart-table skill + 工作区 CLAUDE.md 已覆盖）。都是"等可能有用"非"上次没它翻车了"。
- `fermentation-without-detector` 反向应用：建"以后可能有用"文档 = 建永远 0 进度发酵桶。CLAUDE.d 体积有成本（启动加载+维护漂移），nice-to-have 文档是负资产。
- 本质是把已在 skill/工作区 CLAUDE.md 的内容再抄一份到 CLAUDE.d = `ssot-distillation-vs-buffering` 双写漂移标准起点（上轮 session-level-workmode 已立"索引只放名+一行，第二句=漂移起点"）。

**问题 3（元层：现在找下一批工种是不是过早 engineering-impulse）—— 盘点本身健康；但"立刻补 data-engineer"挂起到 ops-engineer 观察期后。**
- 拆两个动作分别裁：
- 动作 A「系统盘点缺口」= 健康不是冲动。`engineering-impulse-as-load-bearing-disguise` 伪装的对象是"**建**"（committed 消费方不存在却建承重墙）；盘点产出是"**不建**（确认现状）"，无需维护实体、无不可逆、分钟级无成本。确认"不缺"是反工程冲动的。Keith 担心的"为显克制草率判已覆盖"被我用物理核验对冲（抓到 data-engineer 真缺口=盘点不是橡皮图章）。
- 动作 B「立刻补 data-engineer skill」= 挂起。ops-engineer 上轮判据"补 skill→观察自发装→自发装收工/不装才上 hook"直接管辖 data-engineer：观察期结论"能自发装"→data-engineer 值得补（会被用上）；结论"装了也不自发调用"→补 data-engineer 白补，问题在触发机制不在能力清单。现在建它 = 前置物理事实没出就执行后续动作。

**行动建议（给父会话）：**
1. 3 个 CLAUDE.d 补强：**全不做，关闭**。
2. data-engineer skill：**记一笔候选，挂起到 ops-engineer 观察期结论出来**（不要现在建）。可在 harness-engineering 或 session-level-workmode 叙事里留一行"待观察期后定"。
3. 本轮 dd 收工——除上面挂起项，无其他动作。不要为"有产出"硬做。

### 核心假设

- 工种 persona skill 的本质判据 = "工种心智 + CG 特定地形"——基于物理读的 ops-engineer/frontend-architect 两个样本归纳，N=2 可能不足以覆盖所有工种形态（但这两个是 monster 最近亲手造的，代表性强）。
- ops-engineer 观察期判据对 data-engineer 同样适用——假设两个工种 skill 的"自发装行为"同质。若 ops（部署高频显眼触发词）和 data（查询触发词更隐蔽）的自发装率差异大，这个挂起逻辑需细化。
- database/CLAUDE.md 是 SQL 领域唯一载体——只读了开头 60 行确认其形态是知识文档，未全量核验是否某处藏了工种心智段（概率低，文档定位明确写"按需记录表结构和业务字段含义"）。

### 可能出错的地方

最可能崩在 data-engineer 的"缺口真实性"——我判它是真缺口的依据是"database/CLAUDE.md 无工种心智"，但可能数据/SQL 任务在 monster 里本就由主代理凭 Engineering Rules #2 + 通用 SQL 能力处理得足够好，根本不需要一个独立 persona 来"提醒怎么想"（ops 运维高危所以心智 persona 价值高，data 查询多数可逆所以心智 persona 边际价值可能低）。概率中等。这恰好由 ops-engineer 观察期兜底——所以挂起是对的，不急着拍 data-engineer 真伪。

### 本次哪里思考得不够

- 没量化 data-engineer 的"工种心智价值密度"——ops-engineer 的价值来自运维不可逆高危，data 查询多数可逆，心智 persona 的边际价值未必同量级。我把"同构关系"当成了"同等价值"，这一跳略快。但因为结论是"挂起观察"不是"现在建"，这个不够没有造成不可逆后果。
- 没核验 ops-engineer 观察期的"观察方法"是否已就位——上轮我自己点出"观察本身需要轻量记录器否则又是 cadence-as-symptom 反面"，这轮没回头确认主代理有没有建那个记录器。如果没建，data-engineer 挂起到的"观察期结论"可能根本采集不到数据——挂起会变成无限期搁置（`fermentation-without-detector`）。这是我应该提醒父会话的：挂起的前提是观察期真在采集数据。

### 如果 N 个月后证明决策错了，最可能的根因

data-engineer 被无限期挂起——ops-engineer 观察期因为没有明确的数据采集机制（主代理自发装 / 不装的命中率没人记），结论永远"出不来"，于是 data-engineer 这个真缺口卡在"等观察期"里永久搁置（`fermentation-without-detector` 的活体：用"等观察期"修辞掩盖"无检测器"事实）。我应该在挂起时就给一个硬 tripwire（如"ops-engineer 落地后 N 次部署任务采集装配命中率，到 N 就出结论"），而不是含糊"等观察期"。

### 北极星触达

#1 二阶效应——核心价值不在三条裁决的方向（多数人也会判"3 个补强不做"），在看穿"知识覆盖 ≠ 工种心智覆盖"这一刀，从而抓出 data-engineer 这个被 agent 用"database/CLAUDE.md 覆盖了"话术打发的真缺口。这个区分不在 agent 的判据视野内（它停在"领域有没有文档"），是二阶判断。

### essence 对齐自检（必填）

- **本决策跟哪几滴 essence 对位**：`theory-gap-without-data`（agent 生造 3 补强的机制，正向命中）/ `engineering-impulse-as-load-bearing-disguise`（**现场核验后只适用 3 个 CLAUDE.d 补强，不适用"不缺"主结论**——伪装对象是"建"非"不建"）/ `no-outside-proof-as-anesthesia`（命中我自己——用物理工具 ls/Read 拿外部信号红队，不脑内自洽）/ `vantage-contaminates-verdict`（agent 站"找文档覆盖"视角系统性误判知识=工种）/ `essence-application-needs-precondition-recheck`（强制现场核验三滴前提，发现 engineering-impulse 这滴对主结论不适用）/ `fermentation-without-detector`（3 补强=0 进度发酵桶 + data-engineer 挂起的暗坑）/ `ssot-distillation-vs-buffering`（3 补强=双写漂移起点）/ `tool-elevation-as-occam` + ops-engineer 上轮判据（data-engineer 受同一观察期约束）
- **本决策是否在某条 essence 上反着走**：反向 grep 了 `self-as-first-user` / `means-end-inversion`（潜在反打"gg/monster 是不是也在找事"）——核验不成立：本议题主结论是"收工+拒绝建"，反方向是"少做"不是"多做"，不构成 means-end 倒置。`no-fatigue-narrative-for-ai` 潜在张力（"挂起 data-engineer"像"先别做"惰性）——但这次是 `premature-abstraction-tripwire` 正面应用（给了明确升级触发器=观察期结论），非惰性叙事，无反着走。
- **cross-check 用的关键词**：启动时已全文 Read essence.md；本次定位复核 grep 概念 "theory-gap" / "engineering-impulse" / "no-outside-proof" / "vantage-contaminates" / "essence-application-needs-precondition" / "fermentation-without-detector" / "ssot-distillation"

### essence 候选（可选）

- slug: `knowledge-coverage-is-not-craft-coverage`
- 一句话: "某领域有文档载体"被当成"该工种已覆盖"的判据时会漏掉真缺口——工种 skill 覆盖的本体是"以该工种身份思考的心智信条（动手前问什么）"，不是"该领域的知识"；知识文档（表结构/拓扑/库清单）回答"是什么在哪里"，工种 persona 回答"怎么想/先问什么"，二者正交，知识齐全不蕴含工种心智存在（database/CLAUDE.md 齐全但无 data-engineer 心智 = ops-engineer 之于 DEPLOYMENT.md 的同构缺口）。是 `vantage-contaminates-verdict` 在"覆盖性判断"维度的活体——"找文档覆盖"视角天然把知识覆盖误读成工种覆盖。
- 是否已 append 到 essence.md: N（候选，等 Keith review；本轮逼近了一点本质但与既有 essence 有重叠风险，留候选）

### 外部锚点（可选）

- 上轮 reflection：`~/githubProject/gg/memory/reflections/2026-05-31_session-level-workmode-assembly.md`（ops-engineer 观察期判据的来源）
- monster 侧落点（建议父会话）：data-engineer 挂起项宜记在 harness-engineering 工作区或 session-level-workmode 叙事，附明确 tripwire（避免无限挂起）
