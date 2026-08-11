---
date: 2026-08-11
slug: cgboiler-fold-invariant-and-batch-final-review
summoner: monster (cgboiler 架构主会话「把账排清楚」打包终审)
northstar_reach: "#3 决策超越直觉（时间切分本体论证伪 + 传感器拓扑归因）"
status: substantive-decision
---

# Reflection: cgboiler 打包终审（A fold 机制链 / B 议题 14 三修改 / C 三独立议题）

### 给父会话的最终输出（必填）

**总裁决表**：A1 modify-ack(b)+3 强制 / A2 ack 升级+默认 episodic+豁免限 keystone / A3 modify-ack（删「衰减」换两条机械规则）/ A4 裁 (iii) 沉默率硬指标+字符降软 warning / B 三修改全 ack+parent_comment_id 砍掉+D 阶段即本轮、直接进 C / C1 解冻 ack+挂 A4 但加 14 天 tripwire / C2 ack / C3 ack 继续等+闸门改条件性。

**承重判断**：
1. **A1 的架构真相：fold 时间切分对 93% fact 是错误本体论（state_assertion 仅 6.6%），A1 的终解在 A2 里**——fold v3 = 按 fact_type/keystone 分流。裸 (b)（只加 audit）确实是糊弄；(b)+A2 捆绑 = fold 从一次性事件升级为周期性维护相位 + 切分轴从时间换到类型，是架构级回应。(a) reject 双理由：把兄弟劈裂常态化（写入时刻就按日期线劈同 note facts）+ 归档文件从不可变快照变活文件。(c) reject：theory-gap-without-data。
2. **A1 三强制**：① 不变式检查白名单必须含 A2 豁免类，A1/A2 同批落（否则报警器天生假阳性→被静音）② 再 fold 收口以 note 为原子单元（兄弟不劈裂）③ doctrine 跨归档引用补指针头。
3. **A2 默认值 = episodic**（错误不对称：错标 episodic→膨胀可观测；错标 state_assertion→被消解规则静默错杀）。**豁免限 keystone episodic**（177 条 routine episodic 全豁免则 fold 只能归档 ~7%，瘦身机制实质废掉）；`importance: keystone|routine` 与 fact_type 同批落，keystone 复核对接 v2.1 dry-run 人工复核闸门。历史 fact 按 entity 在 fold 收口时补标，不全库回填。
4. **A3 非过度设计**：类型按错误代价定价不按频率（1.6%），两个伤害方向都有卡上实证（范福吉评价无消解 / 陈志刚·郑红负评钉死）。但「衰减」不可机械化，删；换成 ① evaluative 随时间归档贴 state_assertion 侧、不被新状态取代只滑出主卡 ② L2 引用 evaluative 强制日期状语+说话人。evaluative_ratio 传感器 ack。
5. **A4 关键事实：沉默率阈值已有——2026-05-18 fold v2.1 双签判据「L2 重写沉默率 ≤30%」**，(iii) 是已拍判据从灰度升为常态 audit 指标，非新指标。纯 (iii) 丢可读性约束（低沉默率可靠写长达成），故字符上限降软 warning（>1500 警示不报错）而非裸删。l2_refurb 在 fold v3 收口后跑。
6. **B 组不偏离立论**：三修改全是实现层参数（锚定机制/上下文粒度/阈值），generative+reactive 本体论未动；唯一立论级变化是 888888 自评排除，方向是强化。补一条：内参正文作议题锚不进 fact 不进 evidence_distribution（AI 产物非川锅声音的镜像应用）。β 里 ≥3 层 parent_comment_id 派生字段砍掉（@ 推断未测+3.6%+无消费者，engineering-impulse 形态），tripwire：归属错误实例 ≥3 再建。**D 阶段复审 = 本轮**，修改写回 PENDING §14+SCHEMA 后直接进 C；C 后不再 call gg，除非任一修改前提数字漂移 >2× 或新立论级发现。
7. **C1 挂 A4 后 ack，但 14 天 tripwire**：L2 治理 14 天未跑则 L1 先 merge、L2 打待重写标。本轮 3 个月僵尸账全部是「挂链等待无时限」形态，同形复发防一手。例外卡（卢克石油石油焦/北京寰球）落 merge 清单显式排除。
8. **C3 升级闸门从批次性改条件性**：fold v3 落地 + audit 不变式连续 2 tick 零新增违规 + 无 P0 债。日期/批次性闸门正是僵尸账温床。
9. **二阶坐标（父会话未见）**：3 个月僵尸账与 fold 不变式失效是同一个故障——decision_debt（05-18 挂 AUTO_TICK Step0）、audit、收口相位全部挂在「管线跑起来」的前提上，停摆 = 看门狗与被看守物同时断电零告警。建议至少一个存活性传感器挂管线外（monster auto-monster tripwire 注册 cgboiler PROGRESS mtime >14 天告警）。

### 核心假设
- 报告四章数字真实（fresh 子代理逐条实测宣称 + 我抽验王亮 frontmatter/416 signal 行/PENDING §15 三点吻合）——173 条老日期的逐条计数未重跑，信取证纪律。
- keystone 判定 LLM 标注 + 人工复核能压住漂移（v2.1 闸门实操未曾走过一轮真 fold 收口，橡皮图章风险仍在，05-18 已列为最可能崩点，本轮继承）。
- 评论量 +55% 在订阅制 token 下成本可吸收（PRINCIPLES §6 不用 API 前提不变）。

### 可能出错的地方
- 最可能崩点：A1-A2-A3 捆绑落地工程量大（SCHEMA+extract_prompt+render_cards+audit 四件同批），架构主会话再次「拍了没人接」——decision-execution-gap 第三次复现。对策已给（管线外存活性传感器），但落地权在父会话。
- 次崩点：keystone 豁免判据把「奠基」判宽，主卡瘦身仍不足——34 条去重 22 事件是王亮一张卡的数，其他高 fact 卡（杨雷/张吉峰）分布未测。
- 第三：14 天 tripwire 让 C1 的 L1 先 merge 在 L2 未治理时执行，1200008 巨块 L2 的 cite 同步成本被低估。

### 本次哪里思考得不够
- fold 收口相位与 l2_refurb 队列的幂等耦合（05-18 已点过同形问题）没往下推——留实现层。
- 「note 粒度整段上下文」对超长内参（评论 90.5%≤14 条的尾部 9.5%）的 token 上界没算。
- evaluative 归档后被 L2 引用的日期状语规则，对归档内 evaluative 的引用是否同样强制——没显式说，默认同强制。

### 如果 N 个月后证明决策错了，最可能的根因
- N=3：A1-A2 捆绑因工程量被拆开落地，audit 不变式先上而 fact_type 未落 → 假阳性风暴 → 报警被静音 → 不变式第二次失效且这次连报警都没人信（狼来了形态）。根因 = 我把捆绑写成强制但执行侧无物理机制阻止拆开。
- N=6：keystone/routine 二分在 LLM 标注下漂移成「几乎全 keystone」（sycophancy 向重要性膨胀），fold 归档量趋零，主卡膨胀复发——错在把豁免判据交给被 task-compliance 支配的标注者而复核闸门橡皮化。

### 北极星触达
#3 决策超越直觉——两处：把 A1「加检查 vs 改架构」的二choice 重写为「切分轴错误，终解在 A2」（问题重定义层）；把僵尸账从「没人接」归因到「传感器拓扑与管线同生死」（父会话直觉层未达）。#1 二阶效应：沉默率判据复用识别（已拍判据被当缺失数据，决策系统对自己的历史失忆）。

### essence 对齐自检（必填）
- **对位 essence**：`theory-gap-without-data`（05-06 reject 的判据，本轮被数据满足后主动翻转）；`precondition-recheck-overturns-prior-verdict`（翻转不辩护）；`decision-execution-gap` + `bug-shape-survives-fix`（僵尸账同形复发 → 14 天 tripwire / 条件闸门）；`omission-failures-evade-event-driven-sensors` + `watchdog-topology-lacks-a-top`（停摆 = 缺席事件，事件驱动传感器全盲——二阶坐标的谱系根）；`snapshot-as-immutable-archive-not-single-file`（reject (a) 的归档活文件理由）；`idle-threshold-as-tripwire-not-answer`（沉默率 30% / stub ≥5 / 14 天全标 sense-driven 初值）；`engineering-impulse-as-load-bearing-disguise`（砍 parent_comment_id）；`task-compliance-is-not-truth`（keystone 标注漂移风险）。
- **是否反着走**：`separation-need-is-not-topology-verdict` 潜在张力——A3 三值是本体论扩展，但有两方向实证伤害 + 不开新字段挂既有议题，最轻治理形态成立，张力不实。
- **cross-check 关键词**（已 grep 视图核对）：theory-gap / precondition-recheck / decision-execution / omission-failures / watchdog-topology / snapshot-as-immutable / idle-threshold / engineering-impulse。

### essence 候选（candidate-unverified，工作模式无 Agent 不入库，待夜巡/设计模式补验证关）
- slug: `one-shot-invariant-decays-under-live-append`
- 一句话: 一次性动作宣告的不变式，在持续写入通道存在时自动衰减为历史快照断言；宣告不变式必须同时指定「每次写入时谁维护它」（写入闸门 / 周期收口相位 / audit 传感器三选一），否则它只描述宣告那一刻。
- 物理证据: 王亮卡 `archived_until: 2026-03-29` 宣告后，抽取 tick 持续 append 老日期 fact，主卡 173 条 ≤ 切分线（豁免 38 的 4.5 倍）、fold 后 225 → 416 条收益全数吃回——零机制维护「归档后主卡只进新 fact」。
- 相关既有滴: `approval-gate-gates-status-not-consumption`（旁路消费）/ `stale-observer`（规则内容过时 vs 本滴执行拓扑缺位）/ `omission-failures`（缺席事件）——三滴均不覆盖「宣告时刻强制 vs 写入路径维护」这根轴。

### 外部锚点
- `monster/cgboiler/_pipeline/spot_checks/2026-08-11-spot-checks.md` ← 四章取证（本轮证据底座）
- `monster/cgboiler/_pipeline/PENDING_DECISIONS.md` §12-17 ← 裁决落点
- `monster/cgboiler/people/王亮.md` frontmatter ← 抽验锚（416/2026-03-29/38 三点吻合）
- 前档：`2026-05-01_cgboiler-comments-firstclass-ack.md`（29.3% vs 30% 预判）/ `2026-05-06_cgboiler-fact-type-ontology.md`（被翻转的 reject）/ `2026-05-18_cgboiler-fold-v2-route.md`（沉默率 ≤30% 已拍判据出处）
