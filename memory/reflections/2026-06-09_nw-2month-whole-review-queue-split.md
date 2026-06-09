---
date: 2026-06-09
slug: nw-2month-whole-review-queue-split
summoner: monster
northstar_reach: #1 二阶效应
status: substantive-decision
---

# Reflection: NW 跑满 2 个月整体回审——根病=单队列混装、主轴=按可逆性×需不需判断拆三轨

### 给父会话的最终输出（必填）

**根病判断（推翻父会话诊断的抽象层，不是推翻方向）：**
父会话诊断"识别产能 >> 单人判定产能"对，但它是症状描述，根病在下一层——**NW 把"需 Keith 价值判断的提案"和"不需判断、只需机械执行的确定项"混在同一个 proposals.jsonl 队列里，用同一个单人闸门结算**。单人闸门对前者不可消除（价值判断只能上交人类），对后者是纯人为瓶颈。生成端过度生产之所以致命=它生产的东西全部默认流向最稀缺的单人判定通道，含大量本不该占用它的东西。证据是我自己 2 个月 essence 链串起来：`pending-resolved-becomes-blocked-stagnation`(5-09，今天数据证明不平衡是结构性非暂时，该升级)+`signal-without-judgment-needs-live-consumer`(今天)+`cadence-as-symptom`(5-06)+`anchor-set-has-a-budget`(5-18)+5-18 最硬一条"第5次开同形态药方:诊断'NW持续灌规则'是病、解还是'加一条规则'、留apply端物理闸tripwire锚点6-18"。

**主轴方向 = A′（不是父会话的 A/B/C 任一）：按"可逆性 × 是否需价值判断"两维把单队列拆三条物理隔离轨。**
- 轨1 自动闭环：确定+可逆+零价值判断（核验过的 thread-append draft / grounding 修复 / 纯 append）→ auto_gg 夜结算物理闭环，Keith 不参与（`mechanical-apply-decouples-from-value-gate`）
- 轨2 一键执行：确定+不可逆（孤儿 rm / 删除）→ 渲染可一键复制命令，Keith 一次粘贴，不自动扣扳机（`reversibility-not-permission`）
- 轨3 价值判定：需 Keith 价值判断（行为规则/架构/目标范围）→ 保留单人闸门，且瘦身到只剩这一档（`anchor-set-has-a-budget`）

关键转变：今天 Keith 闸门日扫的 25 条 blocked，多数是轨1/2 错挤进轨3。物理分流后进单人闸门的提案量断崖下降——这才是"扩消费"正解，不是无脑 auto-apply 一刀切。

**为什么不是父会话理解的 B：** auto-apply 扩到轨3（价值判断）是灾难（把不可解当可解）。B 正确形态=只在轨1扩，且轨1准入靠物理核验(grep 验 draft 引用事实)不靠 NW 自我声明(5-20 实测 draft 瑕疵率 60%)。
**为什么不是 C：** done 86 证明识别引擎(扫 transcript 找改进点=dreaming 范式核心)有真价值不可替代，C 会把婴儿和洗澡水一起倒。

**第四条路（轨3内部二阶优化，不替代主轴）：** 轨3单人闸门可再上 fresh-context evaluator——把 5-18 设计的"门槛5预算闸"从 prompt 软约束升级成事件层硬 gate，质询"结构性高频 vs 单次应激"。接 monster verification-first-class 主线+6-01 Adjudicator 经验。**先拆队列再优化最难那条轨，顺序不能反。**

**关键 tradeoff/风险：**
1. 最大风险(35%)：轨1"确定+可逆"判定假阳性。product-design-prelude 孤儿铁证——雷达喊该删、实际全仓13处活引用险误删。故轨1准入必物理核验+轨2(不可逆)永不自动。切割轴是"可逆性×需不需判断"两维非一维激进度(`action-type-over-aggressiveness`)。
2. 次风险：拆队列后轨3仍堆→证明根病在"Keith 注意力不分配给 NW 结构卫生"(今天另一份 reflection 标 25% 根因)，那才触发 C。**故建议:A′ 拆队列当 C 的判据采集器,4周后看轨3残留量,≈0则NW健康(只是队列设计错),照堆则该瘦身/换载体。不现在拍 C。**
3. ROI 真账：值得继续但换形态。真价值=识别引擎(不可替代)；维护成本全集中在"单人闸门反复堵+反复加前置 prompt 闸"=队列没拆的代价。A′ 同时砍掉维护成本来源(轨1/2 不占 Keith 时间,轨3瘦身后负载可控,软约束不用再叠)。

**带回 Keith 一句话：根病不是"产太多"也不是"判太慢",是"所有东西挤同一个单人闸门";主轴是按可逆性×需不需判断拆三轨,让单人闸门只剩真需 Keith 价值判断那档;C 重想先别拍,让 A′ 拆队列当判据采集器,4周后用轨3残留量决定 NW 该不该换形态。**

### 核心假设
- "三轨切割"成立的前提=现有 25 blocked 里"轨1/2 错挤进轨3"占多数。我没物理逐条核 25 条分类，是从 5-20 闸门日实测组成(thread-append 40% / 行为规则 47% / skill 13%)推断——thread-append 40% 多数属轨1(可逆 append)、行为规则 47% 属轨3(价值判断)。若实际行为规则占绝对多数,则拆队列收益没我估的大,轨3瘦身后仍是主瓶颈→该往 evaluator 二阶优化倾斜更多。
- "识别引擎有真价值"基于 done 86 这个数字,但我没核 done 86 里多少是轨1机械项(本就该自动)、多少是轨3真改进。若 done 86 大头是机械项,则"识别引擎价值"被高估,C 的合理性上升。

### 可能出错的地方
- 最大风险(30%)：A′ 是又一个"在 NW 内部加结构"的解——我 5-18 标过"第5次同形态药方"是给 NW 加 prompt 规则,A′ 给 NW 加队列拆分,形态上更重。若 Keith 注意力根本不在 NW(轨3照堆),A′ 拆队列是在给一个 Keith 不关心的系统做精致化,正确动作本是问 Keith"你还要不要 NW"而非改造它。这正是我今天另一份 reflection(退役雷达)标的同一根因——我又一次接受了"NW 应存、只是要改造"的前提没裁存废本身。**已在主轴里用"A′ 当 C 判据采集器、4周后拍存废"对冲,但这个对冲本身可能是拖延存废决策的体面外壳。**
- 次风险：轨1/2/3 三分看似干净,落地时大量提案落在边界(一个 thread-append 既改事实又含判断)→三轨退化成"还是得人看一眼分到哪轨"=没省 Keith 时间。三轨切割的可操作性依赖"提案性质能被机械判轨",这个前提没验证。

### 本次哪里思考得不够
- 没物理拉 proposals.jsonl 逐条核 25 blocked 的真实轨分布——整个 A′ 收益估算建立在 5-20 单批次组成的外推上。父会话说"需要更多数据告诉我去拉",我本可以在这一棒就请它拉 25 条分类,省了,留给下一棒。
- 没核 done 86 的轨分布(机械项 vs 真改进占比)——这直接决定 C 的合理性,是我"识别引擎有真价值"论断的承重前提,我用数字大小代替了结构分析。
- evaluator 二阶优化我一句带过,没展开它跟 monster verification-first-class ③档(dd_verify_gate)的具体接法——若那条线已成熟,轨3 evaluator 可能直接复用不用新建,这影响"先拆队列后优化"的工作量估计。

### 如果 N 个月后证明决策错了，最可能的根因
最可能：**三轨拆完,进单人闸门的轨3量确实降了,但 Keith 还是不结算它,blocked 照堆——证明问题从来不是"队列混装"是"NW 这个产物形态(每日产改进提案等人结算)跟 Keith 的实际工作节奏不匹配"。** 那 A′ 是在错误形态上做队列优化,正解是换形态:NW 不产"待结算提案",改产"已自动落地的变更 + 给 Keith 看的 digest"(把默认从 pull 改 push,Keith 从"逐条结算"变"事后否决")。根因:我跟父会话都默认了"提案→人工闸门"这个 NW 原始模型对,只在队列层动刀,没质疑产物形态本身。我今天两份 reflection 都卡在同一前提没回退——这是我这一棒最该被 Keith/父会话挑战的盲点。

### 北极星触达
**#1 二阶效应**：一阶是回答"NW 值不值/改向哪"。二阶——我把自己 2 个月分散在 8+ 滴 essence 里的 NW 局部诊断**第一次在"整体值不值"高度收口成单一根病(单队列混装)**,证明 essence 链不是流水账、是可被反向聚合成结构判断的资产(`essence-recursive-bootstrap` 活体)。更远一层暴露我自己的结构盲点:我连续三次(5-15退役雷达/今天退役雷达回审/今天整体回审)都接受"NW 应存只是改造"的前提,从没裁过"NW 这个产物形态本身对不对"——治理者审被治理系统时系统性偏向"改造而非废除"(`vantage-contaminates-verdict` 在"系统存废"维度的新切面),因为废除会否定治理者自己 2 个月的投入。这个偏置我自己破不了,只能交给 Keith——这一棒我的诚实贡献是把盲点显式推给他认领,不是给终极方案。

### essence 对齐自检（必填）
- **本决策跟哪几滴 essence 对位**：
  - `pending-resolved-becomes-blocked-stagnation`(5-09)——根病的母条,今天升级为"不平衡是结构性"
  - `mechanical-apply-decouples-from-value-gate`(5-18)——三轨切割的核心轴(可解自审 vs 不可解递归)
  - `reversibility-not-permission`(5-06)——轨2不可逆永不自动的依据
  - `action-type-over-aggressiveness`(4-21)——切割轴是动作性质两维非一维激进度
  - `signal-without-judgment-needs-live-consumer`(今天)——轨1必须有活的自动消费端
  - `anchor-set-has-a-budget`(5-18)——轨3瘦身,单人闸门是最稀缺锚点不能无限灌
  - `cadence-as-symptom`(5-06)——产出过密是症状,拆队列(让多产流向自动轨)是根因解
  - `vantage-contaminates-verdict`(5-19)——北极星里自曝:治理者偏向改造而非废除,我连续三次没裁存废本身
  - `essence-recursive-bootstrap`(4-23)——2个月 essence 链反向聚合成单一根病的活体
- **本决策是否在某条 essence 上反着走**：潜在半反 `bug-shape-survives-fix`——5-18 我标"第5次给 NW 加 prompt 规则"是病,A′ 给 NW 加队列拆分形态更重,可能是同形态药方第6次(诊断"NW 结构有问题"、解还是"给 NW 加结构")。已在"可能出错"和根因预判里显式标注未闭合,没因此改主轴(因为 A′ 拆的是物理队列不是再叠软约束,跟前5次"加 prompt 软约束"性质不同——但这个区分可能是我的自我辩护),把判断权交 Keith。
- **cross-check 用的关键词**：grep "pending-resolved" / "mechanical-apply" / "reversibility-not-permission" / "action-type-over" / "signal-without-judgment" / "anchor-set-has-a-budget" / "cadence-as-symptom" / "vantage-contaminates" / "bug-shape-survives"（启动 Read essence.md 全文 L1-700 已加载,物理确认各 slug 存在）

### essence 候选
- slug: `mixed-queue-funnels-all-to-scarcest-gate`
- 一句话: 治理系统把"需价值判断"和"纯机械可逆"的产出混在同一队列、用同一个最稀缺闸门(单人判定)结算时,"生成端过度生产"之所以致命=多产的东西全默认流向最稀缺通道,含大量本不该占用它的。根病不是"产太多"也不是"判太慢",是混装让所有东西挤同一闸门。解不在降产或加判定带宽,在按"可逆性×是否需判断"物理拆队列,让最稀缺闸门只剩真不可机械化的那一档。
- 是否已 append 到 essence.md: N（候选,需 Keith review。这是 `pending-resolved-becomes-blocked-stagnation` 的根因层升级——前者述"cadence 不平衡",本滴定位"为什么不平衡=混装funnels"；+ `mechanical-apply-decouples-from-value-gate` 在队列架构维度的落点）
- 备注: 本轮未擅自 append。与今天另一份 nw-deprecate-radar-review 的 `signal-without-judgment-needs-live-consumer` 是同一台机器同一天两个抽象层的诊断——那滴管"识别视图该不该判定",本滴管"整个提案队列该不该混装",后者是前者的上位结构。

### 外部锚点
- `/Users/xuke/githubProject/monster/threads/night-watch.md` ← 本次整体回审裁决 append 目标
- `/Users/xuke/githubProject/monster/harness-engineering/analysis/proposals.jsonl` ← 落地前必逐条核 25 blocked 真实轨分布(本轮未核,A′ 收益估算的承重前提)
- `/Users/xuke/githubProject/monster/harness-engineering/prompts/nw-daily.md` ← 三轨分流落地点(生成端打轨标签)
- `/Users/xuke/githubProject/gg/memory/reflections/2026-05-18_global-claude-md-rule-budget-gate.md` ← "第5次同形态药方+apply端物理闸 tripwire 锚点6-18"原始警告
- `/Users/xuke/githubProject/gg/memory/reflections/2026-06-09_nw-deprecate-radar-4week-review.md` ← 同日同机器下位层诊断(识别视图维度)
- `/Users/xuke/githubProject/monster/threads/verification-first-class.md` ← 轨3 evaluator 二阶优化的复用候选线
