---
date: 2026-06-01
slug: design-capability-layering-review
summoner: monster
northstar_reach: #3 决策超越直觉（戳穿"建知识地基"是工程冲动伪装，真承重在自检触发器）
status: substantive-decision
---

# Reflection: 设计能力分层方案 adversarial review

## §A 范式 A — 决策的元属性反思

### 给父会话的最终输出（必填）

**总裁决：改了再落——不是砍哪一层，是改产物形态。把承重轴从"建通用知识地基 skill"翻转到"建设计交付的自检触发器"。方案推理质量高、自检诚实，但第 1/3/4 条承重墙踩了 gg 上次刚 warned 的 essence 雷。**

**承重墙 1（外化已知知识 vs 复读）——当前形态推翻，缺口真实需换形态重建**：
- 拆成两个被方案混成一个的子问题。子问题 A：design-foundations 的知识正文（CRAP/Nielsen 10/格式塔/WCAG/Laws of UX）是模型已会的高频语料，抄进 skill 正文 = 纯复读 0 边际价值，推翻。
- 子问题 B："该用时不被可靠激活"是真问题，但方案把"外化"偷换成"把知识抄一遍"。**关键判据（方案缺的）：外化锚点的边际价值从不来自"写下知识"，来自"改变知识被激活的物理时机/方式"。** 对照 monster 已验证真锚点——monster-design §9 self-check（价值在自检清单不在色彩理论复述）/ SSOT registry（价值在操作前必 grep 的唯一入口不在记住了 user_id）/ PreToolUse hook（价值在工具调用前的物理事件不在反例内容）。共同点：价值在激活机制不在知识载体。
- 怎么证明边际价值（方案必须答未答）：design-foundations 价值 = 内含自检清单被多少次"交付前"事件强制触发，不是知识正文多全。钉死这判据，承重轴从"知识覆盖全不全"翻转到"自检触发牢不牢"。
- 这正面撞上 gg 上次 reflection（2026-05-31_workmode-skill-gap-audit）ad-hoc warned 的 `knowledge-coverage-is-not-craft-coverage`——本议题是它的活体，该升正式 essence。

**承重墙 2（三层分层模型）——成立但描述性、不承重**：
- 三层切法对（地基=任意风格成立的中立真理 / 品牌=一种风格选择，monster-design 重定位为品牌特化判断准确；frontend-architect 识别为技术栈非设计也对）。
- 但要戳：分层模型回答"现有资产怎么归类"，不回答"该不该建新东西"。"地图上有空格"不蕴含"这格必须被 skill 填上"。`metric-vs-pattern` 的 level confusion——分层是 pattern，"建它解决什么不可靠维度"是独立的 metric。地图工整恰是 `engineering-impulse-as-load-bearing-disguise` 三件套的"结构工整"那件。

**承重墙 3（触发器层）——方案自打脸，最该警惕**：
- 待决项①理由"skill auto-invoke 是 session-level-workmode 认定的事件层触发器"把 gg 上次结论用反了。上次语境是"主代理换装"（关键词命中有清晰边界）；design-foundations 触发场景是"任何设计动作前"（无清晰关键词边界，方案自己承认触发词必然和 prelude/frontend-design 重叠）。
- 落 `rule-layer-flywheel` 更隐蔽形态：auto-invoke 物理机制是事件层（飞轮），但触发判据是 LLM 对"这算不算设计动作"的语义判断——这一跳回到 prompt 层（跑步机）。和 gg 上次预判暗坑同形（hook 让注入成飞轮但换装动作仍在自觉层 → auto-invoke 让匹配成飞轮但"算不算该触发"判断仍在自觉层）。
- 后果不对称：抢了 prelude 触发=流程仪式被地基自检替代错位；从不自发触发（"设计动作"边界模糊）=永不装的发酵桶。
- `essence-application-needs-precondition-recheck` 活体——移植上次"auto-invoke 是事件层"结论没核"这次触发场景有无清晰关键词边界"的前提。

**承重墙 4（MVP 砍法）——修正，"地基本次建"这步本身就该砍**：
- 砍上层（iOS/AI-native 按需）砍对了，守住"等真实痛点"。但"地基本次建"没过它给上层定的同一道闸。方案对 iOS 用"有真实项目才建"，对地基却用"Keith 点名+零覆盖"——后者不是痛点判据。
- `wish-as-pain-laundering`：Keith 想要通用底子（愿望/合法方向授权）被洗成"地基层真空=系统需要填"（痛点）。"现状零覆盖"同理——抽屉空着不是必须放东西的理由。
- iOS"有真实项目"算方向锚点不算痛点。真痛点判据=有具体设计产出事后复盘"如果当时有 X 锚点强制自检就不会这么做"。keith-voice-cockpit 跑着但没翻车=没痛点样本=iOS 是 `theory-gap-without-data`。iOS 列第二步对，但理由该是"等出现因缺它翻车的样本"非"有项目"。

**重建建议（核心修正：承重轴从"建知识地基"翻到"建设计交付自检触发器"）**：
1. 砍知识正文（CRAP/Nielsen/格式塔/WCAG 复述）——模型已会 0 边际价值。
2. MVP=只做自检清单+强制触发机制。产物不是"装满设计常识的 skill"，是"在明确交付事件上被物理触发的自检清单"。清单可引用原则，价值在触发牢不牢。
3. 触发器不能用 design-foundations auto-invoke（承重墙 3 证明落语义自觉灰区）。候选更牢锚点：直接扩 monster-design §9 已有 self-check 入口（方案自己说"可合并跑"=就不该新建 skill），或挂明确交付动作（生成 HTML 产物的脚本/流程）。方向必须"挂明确事件"而非"靠 LLM 判断算不算设计动作"。归实现层核验 CC 触发能力。
4. iOS/AI-native 砍到"等翻车样本"，非"有项目就建"。
5. 趋势前置动作（待决项④）保留——方案里唯一干净真锚点（明确物理动作 WebSearch 一轮，非知识复读）。但挂 product-design-prelude 触发链，不需要 design-foundations 壳承载。

**待决项重裁**：① skill→否，先扩 monster-design §9；② iOS 改"等翻车样本"非"有项目"；③ frontend-architect 正名维持单议（对）；④ 趋势前置保留但挂 prelude 不挂新 skill。

**一句话给 Keith**：你要的"通用底子"对，但底子价值不在"把设计常识写下来"（Claude 已会，写了也是发酵桶），在"交付设计前有东西强制过一遍自检"。先别建 design-foundations skill，先把自检清单挂进 monster-design §9 self-check（已有触发入口），跑几次真实设计任务看清单触发牢不牢、有没有真挡住烂设计——挡住了再考虑独立成 skill；挡不住，问题在触发器不在知识，独立成 skill 也救不了。

### 核心假设

- monster-design.md §9 真有一个 self-check 段且能作为扩展落点——基于方案自述"可与 monster-design.md §9 五维 self-check 合并跑"，未独立物理核验该段当前结构。父会话落地前 Read 确认。
- CC skill auto-invoke 的触发判据确实包含"LLM 对场景的语义匹配判断"这一跳（承重墙 3 的核心论据）——基于 skill auto-invoke 机制的一般理解，[推测] 未核验 CC 当前版本 auto-invoke 是纯关键词匹配还是含语义判断；若是纯字面关键词匹配，承重墙 3 的"语义自觉灰区"论据需调整为"关键词边界模糊"论据（结论方向不变：泛触发场景无清晰边界）。
- keith-voice-cockpit/keyi-ios 这些 iOS 项目"跑着但没因缺 iOS 设计 skill 翻车"——基于无翻车样本被提及，未独立核验这些项目是否真的设计层无问题。

### 可能出错的地方

最可能崩在重建建议 3 的"扩 monster-design §9"落点——如果 §9 self-check 本身就是 prompt 层软提醒（要被读到才生效），那把自检清单挂进去并没改变触发层级，只是换了个发酵桶的位置。概率中等。这个风险我在裁决里没充分展开——我假定 monster-design §9 是"已有触发入口"，但没核验它本身是飞轮还是跑步机。如果它也是跑步机，那本方案的真问题（无事件层触发器）在 monster-design 同样未解，重建建议 3 是把问题搬家不是解决。父会话落地前必须核验 §9 当前怎么被触发。

### 本次哪里思考得不够

- 没物理核验 monster-design §9 的触发机制（飞轮 vs 跑步机）——这直接影响重建建议 3 的有效性，是本次最大的未核前提。标了核心假设但没在裁决正文里把"如果 §9 也是跑步机"的分支讲透。
- 趋势前置动作（待决项④）我判它是"唯一干净真锚点"，但没追问它挂进 prelude 后 prelude 本身怎么被触发——如果 prelude 也靠 LLM 自觉走流程，那"挂进 prelude"和"挂进 design-foundations"在触发层级上没区别。我对 prelude 的触发机制是凭方案描述（"流程仪式"），没核验。
- 没给"自检清单挂在明确交付动作"的具体物理形态——这归实现层（Decision Authority），但我连一个候选都没具体到（如"生成 HTML 产物的脚本里加一个交付前 checklist gate"），父会话可能又落回 prompt 层自觉。

### 如果 N 个月后证明决策错了，最可能的根因

我把"承重在触发器不在知识"判对了，但重建建议 3 推荐的落点（monster-design §9）本身也是 prompt 层跑步机——于是自检清单从一个发酵桶（独立 skill）搬进另一个发酵桶（§9 软提醒），跑几个月发现"挂进去了但没人触发它过"，和方案原形态等价失败。根因=我诊断对了承重轴（触发层级），但推荐落点时跳过了"落点本身是不是事件层"的物理核验（`mechanism-relocation-has-its-own-precondition` 的活体——把决策点移到 Y，没核 Y 真能承接）。这是我这次没完全展开的暗坑，已在"可能出错的地方"标注但没让它影响裁决强度。

### 北极星触达

#3 决策超越直觉——召唤方的直觉框架是"地基层真空必须填、分层模型工整=该建"。核心价值在戳穿这是 `engineering-impulse-as-load-bearing-disguise` 三件套（结构工整+方向授权+self-check 诚实）的伪装，真承重轴是"自检触发器牢不牢"而非"知识地基全不全"——这个翻转不在方案视野内，方案 90% 篇幅给了知识正文。

### essence 对齐自检（必填）

- **本决策跟哪几滴 essence 对位**：`knowledge-coverage-is-not-craft-coverage`（上次 ad-hoc warning，本议题活体，承重墙 1 核心，本次升正式 essence）/ `fermentation-without-detector`（无触发器知识库每读取时点 0 进度）/ `rule-layer-flywheel`（承重墙 3：auto-invoke 飞轮表皮+语义判断跑步机内核）/ `trigger-layer-not-declarative-emergent-axis`（上次刚沉淀，这次被方案用反）/ `essence-application-needs-precondition-recheck`（承重墙 3：移植上次结论没核前提）/ `metric-vs-pattern`（承重墙 2：分层 pattern≠建它 metric）/ `engineering-impulse-as-load-bearing-disguise`（结构工整是伪装一件）/ `wish-as-pain-laundering`（承重墙 4：Keith 点名被洗成痛点）/ `theory-gap-without-data`（iOS 有项目≠有翻车样本）/ `premature-abstraction-tripwire`（等第 N 次场景）/ `mechanism-relocation-has-its-own-precondition`（重建建议 3 自身的未核前提）
- **本决策是否在某条 essence 上反着走**：潜在张力——`no-fatigue-narrative-for-ai`。我裁"改了再落"且砍掉知识正文、推荐先扩 §9 观察，表面像"先别做大的"保守惰性。但这次不是惰性叙事——是 `premature-abstraction-tripwire` + `engineering-impulse-as-load-bearing-disguise` 正面应用，且我给了明确升级触发器（清单挂 §9 跑几次真实设计任务、看有没有真挡住烂设计、挡不住才判触发器问题），非"先这样再说"死锁。无反着走，议题性质决定（这是"换形态+分两步"不是"不做"）。
- **cross-check 用的关键词**：grep "knowledge-coverage" / "craft-coverage"（已物理核验只在 2026-05-31_workmode-skill-gap-audit 出现，未进 essence 库——诚实标注它是 ad-hoc warning 非已结晶 essence）/ 启动时已全文 Read essence.md，对 "fermentation-without-detector" / "rule-layer-flywheel" / "trigger-layer" / "essence-application-needs-precondition" / "metric-vs-pattern" / "engineering-impulse" / "wish-as-pain" / "theory-gap" / "premature-abstraction" / "mechanism-relocation" 逐条定位复核

### essence 候选

- slug: `anchor-value-in-activation-not-in-content`
- 一句话: 外化锚点的边际价值在它改变了知识被激活的物理时机/方式，不在它写下了什么——把模型已会的知识抄进 skill 正文是造载体没造机制，每个读取时点 0 进度。`knowledge-coverage-is-not-craft-coverage` 的机制层定位：craft 不是知识更全，是触发更牢。
- 是否已 append 到 essence.md: Y

### 外部锚点

- monster 侧：方案文件 `monster/inbox/briefs/design-capability-layering.md`（draft）；主体绑 `monster/threads/session-level-workmode.md`（本议题是其延伸）；落地前父会话需核验 `monster/shared/design/monster-design.md` §9 self-check 的触发机制（飞轮 vs 跑步机）
