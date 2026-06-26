---
date: 2026-06-26
slug: taste-core-web-contract-structure
summoner: monster (designer / taste-core)
northstar_reach: #1 二阶效应（结构选错会污染品味 SSOT 的载体-不变性定义，难回退）
status: substantive-decision
---

# Reflection: taste-core web 契约结构 + 收录边界 + 参数形态三裁

## §A 范式 A

### 给父会话的最终输出（必填）

**三裁结论：**

**① 结构 = 方案③精化（推翻 Keith 倾向的②）。** 不按 A组/B组 切，按「品味原则（载体无关）/ 执行落地（web 专属）」切。14 条几乎全部 fall 在执行落地侧——连 B 组也是（scale(0.96)/blur 4px/initial={false}/motion库/font-smoothing 全是 web 执行词，不是载体-不变品味）。所以：
- **全部 14 条的 CSS/参数落地 → frontend-design 执行器**（它是 web 落地代码的家，designer 自己的 dispatch 架构 taste-core品味→执行器落地 就这么定的）。
- **taste-core 只在 web 载体契约 row 扩 2-3 行动效品味判断式（WHAT，零 CSS）+ 指针** "落地参数见 frontend-design"。沿用现成的 icons.md 指针范式（web row 已经在为 icons 这么干）。
- **不加第 9 共享底层条**（封顶原则：motion 落地是 web 专属、不是跨 web/PPT/iOS 同形 invariant，不够格升共享层；iOS 动效已在 iOS 契约、PPT 在转场行，各载体自带 motion-delta，无跨载体 SSOT 被丢失）。

否决②的核心理由：B 组 CSS 详条塞进 taste-core，跟 A 组同罪——违背 taste-core "8 条跨载体不变 / 薄 delta" 的**定义性 invariant**（taste-core.md 第 5-6 行明示）。把 14 条任何一组塞进 taste-core 正文，都是 essence `matrix-of-tension` 说的"工整美学消除矛盾"：web 比 PPT/iOS 天然多 CSS 工艺面（web 手写 CSS→像素，PPT 走 python-pptx、iOS 走 SwiftUI 都无 CSS），这个不对称是真的、不该为对称强行抹平。

**② 收录边界（06-01 尺子 = 会且会用→指针，会但默认不用→三件套压住，应用到"是否写进 frontend-design"）：**
- **强收**（会但默认不用 + 好 detector候选）：禁`transition:all` / tabular-nums / text-wrap。三条是金——`[正则可查]`、模型默认高频漏（甚至默认写错形式如 transition:all），未来一条一条长 detector 的首选。
- **收**：嵌套圆角同心 / 图片描边用中性色非带色灰 / will-change 克制 / 阴影代边框的 web 具体化（§6 既有条的落地参数）。
- **砍/降级两条**：
  - **font-smoothing（antialiased）→ 降为 soft note 或砍**。理由：contested best-practice（"antialiased 让字偏细"的反对意见真实存在），不是普适底线，且偏"会且会用"。不够格当钦定工艺底线。
  - **命中区 ≥40px → 不在 frontend-design 重写，指针引用 taste-core 既有 iOS 44pt / web 既有条**。它是原盘点里"已覆盖"项 + 偏 UX 定律（Fitts/HIG，模型会且会用），重写=重复。
- B 组动效全收（"整容器一起淡入"=模型 default slop，符合三件套），但 **initial={false} 标"用 motion 库时"条件**——它是 Framer Motion 专属 API gotcha，不是品味也不是普适工艺，别当普适底线。

**③ 参数形态 = 写初值 + 标 provisional-initial，不留空（精化 Keith 的"标校准位"）。**
- **不留空**：空校准位 = essence `fermentation-without-detector` / `bucket-time-asymmetry`——"先空着"无校准机制 = 永久空，且 dev day-1 没数可填→不可用。
- **不钦定写死**：它们是 jakubkrehel 个人偏好值，非普适常数。
- **正解**（essence `idle-threshold-as-tripwire-not-answer`）：写死作为 sense初值，显式标"借自 jakubkrehel 初值，待 cg-desk/cgx/cookie-arcade dogfood 校准"。校准 trigger = Keith 的眼睛看真实 dogfood 产出（美学无物理 metric，不存在自动数据 tripwire），不是定时器。
- 尽量写成**带护栏的区间**而非魔数点：草稿里 scale "0.96 不低于 0.95" 已是正确形态（sense区间+护栏），把 ~100ms 写成 "80-120ms"、blur "3-5px" 同理。
- 参数全在 frontend-design（载体专属），taste-core 的动效判断式保持零参数（载体-不变品味只说"按压有反馈/入场错峰/退场更柔/交互可中断"，不带数字）。

**行动建议（给父会话/CC 执行）：**
1. 改 taste-core.md：web 载体契约 row 的现有 "动画 ≤200ms" delta 扩成含动效品味判断式（5 句 WHAT）+ "落地见 frontend-design" 指针。不动 8 条共享底层，不加 §9。
2. 在 frontend-design 执行器加 "web 代码工艺底线" 段，收录上述 强收+收 项（12 条左右），参数标 provisional-initial。先确认 frontend-design 当前结构能挂这段（它是执行 skill，这是其天然内容）。
3. font-smoothing 降 soft note；命中区改指针引用，不重写。
4. `[正则可查]` 三金条（transition:all / tabular-nums / text-wrap）登记为未来 detector候选，但**不预先写 detector**（taste-core §8 既有政策 + essence `premature-abstraction-tripwire`：复发 ≥2 次再写那一条）。

### 核心假设
- frontend-design 是 designer 的 web 执行器（monster CLAUDE.md UI 段明示 dispatch web=frontend-design），能承载"web 工艺底线"段。**未读 frontend-design 实体文件**——结构假设，需 CC 落地时核实。
- taste-core 的"8条跨载体不变"是真 invariant 而非偶然——14 条无一跨载体同形 ⇒ 无一属共享层。这点我逐条验过（CSS 属性/Framer API 都是 web-only）。

### 可能出错的地方
- 若 frontend-design 当前是纯"代码生成范式/组件清单"型 skill、没有"工艺规则"承载位，则需先给它建段，比预想多一步。概率中。
- 动效品味判断式塞进 web 载体契约 row 而非升 §9——若 Keith 认为 motion 是和 §6 深度细节平级的品味维度（静态质感 vs 动态质感是兄弟），可能更想要 §9。我按封顶原则压住了，这是可争议的偏好点。

### 本次哪里思考得不够
- 没读 frontend-design 实体，结构落点是架构推理不是物理核验——这是本决策最大的未核验点。
- "动效品味判断式"具体 5 句怎么写没给成稿（留给执行），只给了 WHAT 清单。

### 如果 N 个月后证明决策错了，最可能的根因
frontend-design 变成事实上的"第二 taste-core"——web 工艺越长越厚，品味判断和代码工艺的边界又糊了。防御：frontend-design 的 web 工艺段必须是"执行落地"措辞（emit 什么 CSS），不能漂成"什么是好品味"的判断（那是 taste-core 的活）。

### 北极星触达
#1 二阶效应——结构选错（把 web 工艺塞进 taste-core）会污染品味 SSOT 的载体-不变性定义，是难回退的承重墙级污染，正是 gg 该管的那类。

### essence 对齐自检（必填）
- **对位 slug**：`idle-threshold-as-tripwire-not-answer`（参数=sense初值+tripwire，直接定③）/ `fermentation-without-detector` + `bucket-time-asymmetry`（"先空着"=永久空，否决留空）/ `ontology-expansion-velocity-needs-cap`（加 §9 要过封顶，定不加）/ `matrix-of-tension`（强行对称=工整美学抹矛盾，否决①②的塞入）/ `abstraction-tax`（web 边界处天然多具体化债，挪到 frontend-design 而非免除）。
- **是否反着走**：潜在张力一处——`survey-as-coordinate`（"多数会坍缩为已做差名字"）提示我别把外部 skill 当新能力照抄；本次正是按它砍了 font-smoothing/命中区（已有或会用），方向一致非反走。无明显反着走。
- **cross-check 关键词**：grep essence "tripwire" / "fermentation" / "bucket-time" / "ontology-expansion" / "matrix-of-tension" / "abstraction-tax" / "survey-as-coordinate"，均实读。

### essence 候选（可选）
- slug: load-bearing-seam-is-invariance-not-category
- 一句话: 给跨载体契约分层时，正确切线是"载体-不变性"而非内容分类（A组/B组）——按品味动机分组会把 web 专属执行误判为跨载体品味，塞错文件。
- 是否已 append: N（留 Keith review 后再定，避免噪音）
