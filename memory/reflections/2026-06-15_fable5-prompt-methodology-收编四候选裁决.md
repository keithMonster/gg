---
date: 2026-06-15
slug: fable5-prompt-methodology-收编四候选裁决
summoner: monster (studio Fable-5 prompt 对照研究)
northstar_reach: #2 动态学习反哺
status: substantive-decision
---

# Reflection: Fable 5 prompt 方法论收编四候选逐条裁决

### 给父会话的最终输出（必填）

**总裁决：1=adopt（措辞收紧）/ 2=adjust（你的 lean 偏轻，改"原则 + 一次性最小 sweep 限红线区"）/ 3=REJECT 你的语言学主张但 adopt 一个更强的修订 / 4=archive 为概念但比你的 lean 更明确地写进归因层。**

---

**候选 1【范例驱动收编】→ adopt，但收紧落点。**

你的 lean（加第 6 条"L1 漂移时 worked example > 叠规则"）方向对，但落点错了一层。worked example 的威力不是"prompt 手法第 6 条"，是**归因层 L1 的解药**——monster CLAUDE.md「动结构前先归因到层」已经写明 L1（没懂 Keith 要什么）的解是"说清 / 给例"，L2 才是 prompt 锚词的主场。你提的"L1 漂移加 example"恰好是 L1 解法，把它塞进 prompt-writing 5 条（L2 工具箱）是**层错配**——会让人误以为 example 是一种锚词技巧，其实它是越过锚词、直接示范目标输出形态的更高带宽通道。

正确落点：不加 prompt-writing 第 6 条，而是在 prompt-writing 段**统领句之后加一句桥接**——"锚词激活不动时（L1 需求本身没传达清），换 worked example 直接示范目标输出——example 是比锚词更高带宽的引力源（直接把目标点出来，不靠周围种锚牵引）"。一句话，挂在世界模型统领句下，既收编了 Fable 的真经验，又不污染 5 条 L2 手法的纯度。低风险加法成立，但别加成第 6 条。

理论自洽：在你们的语义场域模型里，锚词 = 从周围种锚牵引目标；worked example = **直接把目标点亮**（不是牵引，是示范坐标）。两者不同机制，不该并列成"第 6 条手法"。

---

**候选 2【强调通胀】→ adjust，你的 lean 偏轻。**

真问题成立（满屏 bold + 🚫 稀释真红线，这是 essence `field-gravity-over-prompt` 的反面：强调词是物理引力，每个 bold 都在抢注意力，全 bold = 全不 bold）。但你的 lean"只立分级原则 + 增量执行，不做全量 sweep"**低估了通胀的自我繁殖性**——增量执行治不了存量通胀，因为新写的人看到的是满屏 bold 的现状，会按现状的密度水平继续加（锚定效应），原则文字劝不动既成的视觉基线。这是 essence `rule-layer-flywheel`：纯 prompt 层原则是跑步机，靠"被读到 + 被遵守"，对抗不了已经铺满的视觉事实。

但全量 emphasis 大扫除我也 reject——成本高、且 bold 的"对错"很多是主观的（哪条算真红线有判断空间），全量 sweep 会陷进逐条争论。

**正确解 = 原则 + 一次性最小 sweep，但 sweep 范围只锁"安全红线区 + Decision Authority 强制语法区"两块**。理由：① 这两块是真红线密度最高、且通胀危害最大的区（红线被稀释 = 真出事）② 范围小、判据清（🚫 是不是真不可逆 / 真红线，二元好判），不会陷主观争论 ③ 扫完这两块就建立了"红线区强调密度"的新基线，增量执行才有锚可依。**分级原则单独立**："SEVERE/红线级强调（🚫 + bold 并用）全局限 X 条以内，普通强调用单一信号（bold 或 🚫 择一不叠加）"——给个软上限当 tripwire，不是硬数字。

一句话：原则立（你对），但必须配一次锁定红线区的最小 sweep 把基线打下来，否则原则是空头支票。这比你的"纯增量"重一点，比"全量大扫除"轻得多。

---

**候选 3【prompt-writing 第①条措辞修订】→ 你的语言学主张 REJECT，但 adopt 一个更强的修订。**

你的 lean 是"真正该禁的是因果论证段、不是否定句本身，所以 adopt 修订"。**方向对了一半，但你的证据链和结论强度都站不住，而且 monster 内部早有比你这版精细得多的裁决你没接上。**

三个问题：

① **你对 Fable 的归纳过度了。** 我抽样了 Fable 的否定句实写，多数**不是**"否定句删因果尾巴"，而是 `avoids X and offers Y`（否定 + 正面替代，L62/L130）、`does not suggest X that use Y. Substitutes that recreate... reinforce the pattern`（否定**后面紧跟 why**，L88——Fable 这里没删因果）、`Urgency is not an exception`（否定句主语是抽象规则不是被禁的具体行为，L260）。Fable 的真规律是**"否定 + 同句绑定正面替代行为"**，不是"删因果留否定句"。你看到"几百处否定句"就推"否定句本身不激活、只删因果尾巴"——这是把现象的一个侧面当成了机制。

② **"否定句到底激活不激活被否定概念"——这条经验主张已经被 monster 自己的物理证据更新过，强度比你写的弱很多。** 关键 grounding 你没读到：`threads/prompt-writer.md` 2026-06-10 条 + `threads/llm-foundations.md` 2026-05-27/06-10 勘误——arXiv 2510.17941《Believe It or Not》（**Anthropic 自家 Fellows Program 研究**）的真实结论是 disclaimer **选择性失效**（只压"离谱级"虚假事实，对"貌似合理"类几乎无效），**不是全盘失效**；更关键的范畴区分——**训练层信念植入 ≠ 推理层指令遵从**，对齐模型对"清晰的负面指令"的遵从是**被显式训练过的**。所以"写'不是 X'会激活 X"这条 prompt-writing 第①条的现行措辞，在推理层（指令遵从）其实是**被夸大的**——它把训练层的合成文档实验结论跨层外推到了指令遵从场景。

③ 因此现行第①条已经有内部矛盾：它说"论证否定会把被否定的概念引进上下文"（这部分对——增加 token 共现），但又被理解为"禁否定句"（这部分错——清晰负面指令的遵从被训练过）。SKILL.md 6-10 已经因为这个矛盾把对应节从"硬约束删所有负面表述"降级重写为「负面表述分层规则」，**但全局 CLAUDE.md 第①条至今没同步**（6-10 那条明确写了"全局 CLAUDE.md Prompt Writing #1 未动"）。

**所以正确动作不是 adopt 你那版"禁因果段不禁否定句"——而是把全局第①条直接对齐到 SKILL.md 已经裁决过的「分层规则」，关掉这个跨文件不一致。** 修订后的第①条应该是三层而非二元：

> **激活而非描述**——正面锚定优先（直接写要什么）。负面表述分层：① **硬禁止**保留（"绝不 X / 禁止 X"——清晰负面指令的遵从是被训练过的，留着，但**同句绑定替代行为**："不 X，而是 Y"）② **删的是因果论证尾巴**——"不要 X（因为 X 会引发 Z）"里删括号内 Z，留禁令 + 替代锚 ③ **真正高激活风险的是"软否定 + 详细展开被否定概念"**（"我们避免那种 A、B、C 式的做法"——A/B/C 全被引进上下文）。判别：负面词后面跟的是替代行为（留）还是被否定概念的细节（删）。

这版比你的"禁因果段"强在：它不否认否定句的合法性（硬禁止 + 替代是有效的），精确切出真正激活反噬的形态（软否定 + 展开被否定概念），且与 monster 内部已落地的 SKILL.md 裁决一致——关掉的是一处真实的跨文件漂移债，不是新立一条经验主张。

**这条是四个候选里你最需要被翻的一条**：你的语言学主张（否定句不激活、只因果段激活）本身就是现行第①条那个被夸大主张的镜像，你在用一个过度结论去修另一个过度结论。真相在中间，且 monster 已经走到了那个中间——你只是没读到。

---

**候选 4【in-prompt self-check 清单】→ archive 为概念，但比你的 lean 更明确地写进归因层 L2/L3 之间。**

你的 lean（登记为 L2/L3 中间档概念、不立项做基建）方向对，但"登记为概念"太轻，会变成一条没人接的 musing。in-prompt self-check 的本质是：它**比纯文字劝说强**（"回答前自问 X" 是把检查动作显式化成 prompt 步骤，比"要仔细"这种软劝说有结构），但**比 hook 弱**（仍在 LLM 自觉范围内，会被 RLHF 在高压场景压回——self-check 清单对抗不了 sycophancy 的强引力，因为做 self-check 的和被 check 的是同一个被污染的 prior，对应 essence `generator-evaluator-separation`：自证审自证 = 没审）。

所以它不是"L2/L3 之间的新档"——它就是 **L2 的上限形态**（结构化的 prompt 自觉），不是新的一层。归因表「动结构前先归因到层」现在 L2 写的是"改锚词"，应该补一句：**"L2 上限 = 结构化 self-check（把检查显式成 prompt 步骤）；但 self-check 仍是自觉范围，对抗 RLHF 默认行为（sycophancy / 自证已尽力）会被压回 → 那是 L3 hook 的活，self-check 顶不住。"** 这样它的边界被钉死：知道什么时候用（L2 不够、想再榨一点自觉）、知道什么时候没用（L3 结构对抗，别指望 self-check）。

不立项做基建——对，因为它不是基建，是 L2 的措辞升级。写进归因表当 L2 的天花板标注即可。

---

**收尾——四条的共同主轴（给你一个统一视角）**：

这四个候选全在回答同一个元问题——**Fable 是一个 RLHF 对齐过的消费端 prompt，monster 是一个对抗 RLHF 默认行为的工程系统，两者的 prompt 范式有结构性错位**。Fable 能满屏否定句、能堆强调词、能写 self-check，是因为它的读者（claude.ai 产品形态）和它的目标（安全合规）跟 RLHF 默认行为**同向**——它在顺着引力写。monster 的 prompt 大量在**逆引力写**（对抗 sycophancy / 自证 / 短输入消歧失败）。所以**收编 Fable 手法时，第一道筛子永远是"这条手法在 Fable 里 work 是因为它顺 RLHF，还是因为它真的是通用 prompt 物理"**——顺 RLHF 那部分（候选 3 的"否定句随便用"、候选 4 的"self-check 够用"）到了 monster 逆引力场景就会失效，这正是候选 3、4 你都判偏轻的根因。候选 1、2 是通用 prompt 物理（example 高带宽、强调通胀稀释），可收编。

**行动建议（按优先级）**：
1. **先做候选 3**（关跨文件漂移债，全局第①条对齐 SKILL.md 分层规则）——这是唯一在修一个**已存在的 bug**，不是加法，优先级最高。
2. **候选 2 的最小 sweep**（锁红线区 + Decision Authority 区）——配套立软上限原则。
3. **候选 1 的桥接句**（worked example 挂统领句下）——低风险加法。
4. **候选 4 写进归因表 L2 天花板标注**——一句话的事。

---

### 核心假设

1. monster prompt 大量逆 RLHF 写、Fable 顺 RLHF 写——这个"引力方向"分野是收编筛子的核心。若此分野不成立（比如 monster 其实多数也顺 RLHF），候选 3/4 的"偏轻"判定会松动。
2. arXiv 2510.17941 的"训练层 ≠ 推理层、清晰负面指令遵从被训练过"结论可靠（来自 monster 6-10 已派 WebSearch agent 独立核验的勘误，非我现场新查）。
3. 全局第①条与 SKILL.md 分层规则的不一致仍然存在（基于 6-10 thread 明确记录"全局 #1 未动"，未现场再核 SKILL.md 当前文本是否又改过）。

### 可能出错的地方

- 候选 2 的"最小 sweep 锁两区"可能仍触发主观争论（哪些 🚫 算真红线）——但比全量 sweep 风险低一个数量级。
- 候选 3 修订后的第①条三层表述可能仍偏长，落地时 Keith 需按 prompt-writing 准则 5（反复=重要、铺垫稀释）再压一轮——我给的是裁决和方向，不是终稿措辞。

### 本次哪里思考得不够

没有现场 Read SKILL.md 当前「负面表述分层规则」节的精确文本（依赖 6-10 thread 的转述），所以候选 3 我给的修订措辞是"对齐 SKILL.md 精神"的方向版，不是逐字 copy SKILL.md。Keith 落地时应以 SKILL.md 现行文本为准对齐，避免我转述漂移。

### 如果 N 个月后证明决策错了，最可能的根因

候选 2 的"最小 sweep"被执行成了"又一次全量纠结"——sweep 范围没守住"只锁两区"，扩散成逐条争论 bold 该不该留，最后不了了之，通胀照旧。根因会是"范围纪律没守住"，不是判断错。

### 北极星触达

#2 动态学习反哺——把外部样本（Fable prompt）对照后，没有照搬，而是用 monster 已有的归因层 / essence / 6-10 勘误把它**消化进**既有体系（候选 3 直接接上了一条悬而未决的内部漂移债）。这正是"整合更广"——新输入不是叠加，是接回主干。

### essence 对齐自检（必填）

- **本决策跟哪几滴 essence 对位**：
  - `field-gravity-over-prompt`（2026-04-27）→ 候选 2 强调通胀的机制根（强调词是物理引力，全 bold = 全不 bold）
  - `rule-layer-flywheel`（2026-04-24）→ 候选 2"纯增量原则治不了存量通胀"（prompt 层是跑步机）
  - `generator-evaluator-separation`（2026-04-18）→ 候选 4 self-check 顶不住 RLHF 的机制根（自证审自证）
  - `extraction-meta-inheritance` / `borrowed-method-as-mini-source`（2026-04-29/05-08）→ 收编主轴"Fable 顺 RLHF / monster 逆 RLHF"是这两滴的应用（抽取外部体系前先问元约束是否同向）
  - `survey-as-coordinate`（2026-04-23）→ 候选 3"monster 内部早有更精细裁决你没接上"= 对照前沿产出的是坐标不是清单，多数收编候选坍缩为"已做/已裁决，差同步"
- **本决策是否在某条 essence 上反着走**：无明显反走。潜在张力——`survey-as-coordinate` 说"多数坍缩为已做"，但候选 1（worked example 桥接句）和候选 2（最小 sweep）确实是真增量不是"已做差名字"，所以本次不是全盘坍缩，是"3、4 坍缩 + 1、2 真增量"的混合——这恰恰说明 survey-as-coordinate 不是"所有候选都坍缩"的懒人挡箭牌，逐条判才对。
- **cross-check 用的关键词**：grep `field-gravity` / `rule-layer-flywheel` / `extraction-meta` / `survey-as-coordinate` / `generator-evaluator`（在本次 essence.md 1-522 行 Read 中物理见到全部 5 条）

### essence 候选（可选）

- slug: `extraction-filter-by-gravity-alignment`
- 一句话: 收编外部 prompt 体系的第一道筛子是引力方向——源系统的手法 work 是因为它顺训练默认引力（到逆引力场景就失效）还是因为它是通用 prompt 物理；顺引力的手法不可跨场景移植。
- 是否已 append 到 essence.md: N（留待 Keith review 后决定，本次工作模式不自行 append——这滴是 `extraction-meta-inheritance` 的精化版，可能与既有滴重叠，需 Keith 判去重）

### 外部锚点

- `~/githubProject/monster/threads/prompt-writer.md` 2026-06-10 条 ← 候选 3 的决定性 grounding（Negation 节降级裁决 + 全局 #1 未动的明确记录）
- `~/githubProject/monster/threads/llm-foundations.md` 第三块 + 2026-05-27/06-10 勘误 ← 候选 3 语言学主张的物理证据源（arXiv 2510.17941）
- `~/.claude/CLAUDE.md` L41 ← 候选 3 待修订的全局第①条原文
