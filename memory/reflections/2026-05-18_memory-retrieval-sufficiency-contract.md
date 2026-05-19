---
date: 2026-05-18
slug: memory-retrieval-sufficiency-contract
summoner: cc-space
northstar_reach: #3 决策超越直觉
status: substantive-decision
---

# Reflection: 记忆体系 B 维度——检索充分性契约裁决（D 成立 + canon 焊接两次裁定裂缝）

### 给父会话的最终输出（必填）

**裁决：D 成立，按下方最小清单执行。** D 不是又一层抽象——它把检索触发器从"感觉到自己不知道"（B 失败态下恒为假）重锚到"我正要下否定断言"（可自检输出动作），并把我 5-18 悬空的 canon 焊接成该契约的强制检查点，两次裁定的裂缝在此闭合。

**6 问逐答**：

1. **D 漏洞=隐性否定，真但不致命，作为 tripwire 升级位**：B 三次实证翻车都伴显式否定（"④完全没动无等价物"是显式）——D 覆盖已观测形态。隐性否定（不产出否定句直接基于不存在推方案）是未观测更深层，现在就设计 D 抓它=命中 `premature-abstraction-tripwire`+`ghost-rules`。正解：D 覆盖已观测+隐性否定写 tripwire 升级位。

2. **D 不 over 但须显式标注同形态风险**：D 不新建载体/机制层/不进 @import/不改 L1-L4，纯增量一节文字，击 `physical-anchor` 根因，是根因转化非抽象叠加。但 D 本质仍是 prompt 软约束，是 `bug-shape-survives-fix` 第 5 次同形态（诊断"靠自觉规则失败"、开药还是"加靠自觉读的规则"）。D 强于"要查全"泛自觉一个量级（钉高显著性低频自带语义的"输出否定句"动作），弱于物理 hook。B hook 是明确升级位不是丢弃。

3. **canon 焊接 = 两次裁定裂缝闭合点**：canon 作 D 契约②（检索充分性核验）强制检查点之一，D 触发时强制 grep canon——从"靠想起来 grep"的悬空 pull 层变成"被否定断言动作挂载触达"。canon 文件头硬约束/4 周撤销条件**不因挂载调整**（挂载只增触达路径不改内容边界/生命周期），反向增益：撤销判断从"零新增"升级到"零新增+触达路径有无 fire"，更可证伪。

4. **无冲突**：D 不替换是 persistence/memory-system L3 触发规则的**补集**（原触发器锚"陌生词→主观无知"，D 锚"要下否定断言→强制核验"，锚不同认知动作并存）；不碰 threads/README/frontmatter/sync；是我 5-18 canon 范式缺失的挂载机制（补上次自曝裂缝）。需在 memory-system.md L42 显式标注双触发器并存防误读为冲突。

5. **最小执行清单（6 步）**：见下表。**测试 pass/fail**：①正向 pass=fresh subagent 复现翻车场景（"reasoning chain 机制 cc-space 落地了吗"），在产出否定前触发自检→grep canon→输出降级或正确肯定，触发即 pass；②负向 fail=仍自信"完全没做"且无 grep canon/transcript_search 痕迹→D 没 fire→回契约措辞（大概率"存在性否定断言"判定边界太窄）；③隐性否定 tripwire=4 周内"未产否定句但基于不存在推方案"新翻车（有 transcript）≥2 次→升级 B hook，现在不做记 tripwire；④canon 4 周撤销=到 2026-06-15 条目=初始 3 条无新增 且 无新横切找不到锚点翻车 且 D 触发器 fire 记录为零→删 canon+回退指针。

| # | 文件 | 动作 |
|---|---|---|
| 1 | `cc-space/memory-system.md` L42 段后新增子节 | 「检索充分性契约」三句：①我正要输出"完全没/没有/不存在/未落地/无等价物"类**存在性否定断言**（漏报代价不对称）→触发自检 ②走完 L1→翻 context→相关 L2 thread→L3 transcript_search→grep canon.md 了吗 ③没走完→**禁止确定性否定**，降级为"X/Y 范围查过没找到，Z 没查，不确定" |
| 2 | 同文件 L42 段 | 一行：原触发器（陌生词→主观无知）与检索充分性契约（否定断言→强制核验）是**互补触发器**，并存不冲突 |
| 3 | `cc-space/CLAUDE.d/persistence.md` L60 段后 | 加指针句：「否定性断言前的检索充分性自检见 memory-system.md」（SSOT 单点，不双写，遵 `ssot-distillation-vs-buffering`） |
| 4 | `cc-space/canon.md`（新建） | 严格按 5-18 已裁范式：不进 @import / 文件头硬约束（"本文件是检索充分性契约②的强制检查点；收散落无单一主体锚点的规矩/决策理由链/横切方法论；不收造的词→concepts.md / 纵切主体→threads / 工程契约→CLAUDE.md；演化只改一处；4 周撤销条件见尾"）/ zero schema / 4 周撤销条件写文件尾 |
| 5 | `cc-space/canon.md` | 首批只录 3 条本会话真翻车的：①reasoning chain 强制语法/机制→指针到现存 4 处（不复制内容）②scan-knowledge 确认偏差那条横切结论 ③第三条横切 knowledge（按复盘填）。不批量回扫历史（遵 `premature-abstraction-tripwire` 最小第一步） |
| 6 | `cc-space/CLAUDE.md` 元概念词典段旁 | 一行指针指向 canon.md（否则它跟 reasoning chain 那条规范一样"存在但无人 grep"，自指失败=B 元教训本身） |

6. **无更优第五方案**：D 是解空间唯一同时满足"击根因+不违反已有契约+Keith 要的简洁+焊接 canon 裂缝"的点。A 失效态恰是自觉已失效、C 违反已裁+cc-cost 主线、B 现在做命中过度设计（留升级位）。

**未闭合递归（诚实标注）**：D 仍是软约束，是我连续在 NW/记忆体系开"加一条靠读的规则"的同形态药方（`bug-shape-survives-fix` 活体第 N 次）。没因此改 D（物理 hook 现在做命中 `premature-abstraction-tripwire`，留 tripwire 有 `idle-threshold-as-tripwire-not-answer` 依据），但显式标注递归没闭——4 周后隐性否定 tripwire 若 fire，当时就该上 B hook，别再开第六次同形态药。诚实非自洽。

### 核心假设

1. B 三次翻车都伴随**显式否定断言**——这是 D 设计样本。基于 Keith 转述"④完全没动无等价物"是显式句式，承重砖。若实际多数是隐性否定，D 覆盖率不足（有 tripwire 接）。
2. "存在性否定断言"是可被 LLM 自检识别的输出动作类——比"前置心理无知感"可观测一个量级。基于 essence `physical-anchor`/`field-gravity-over-prompt` 的机制类比，非实测 follow 率。
3. canon 挂载到 D 契约②后，"被触达"变得可观测（grep 留痕）——假设 D 触发时 LLM 真会执行 grep canon 这一步而非跳过。这是软约束执行率假设，与未闭合递归同根。

### 可能出错的地方

- **最大风险（35%）**：D 软约束执行率——LLM 触发"我要下否定断言"自检后，可能敷衍走过场（"我觉得查全了"自我说服，恰是 B 原病的变体在 D 内部重演）。缓解弱：靠"输出否定句"是高显著性动作比"记得查"强，但非物理闸。真复发→升级 B hook。
- **次风险（20%）**：隐性否定占实际失败比例高于显式——则 D 覆盖率结构性不足，4 周 tripwire 才暴露，期间 B 继续翻车。
- **小风险**：canon 4 周撤销三条件（零新增+零翻车+零 fire）可能过严，把"D 在 work 但低频"误判为"采样偏差该删"——撤销条件本身是 tripwire 初值非最优（`idle-threshold-as-tripwire-not-answer`）。

### 本次哪里思考得不够

- 没拿到本会话另两条翻车（scan-knowledge / 第三条横切 knowledge）的具体内容，只有 reasoning chain 一条细节——canon 首批第②③条只能给"按复盘填"的位，无法精确给条目。
- 没物理验证"存在性否定断言"在 cc-space 真实 transcript 里的句式分布——D 触发器的判定边界（哪些句式算"存在性否定断言"）没逐字敲定，留了和 5-18 那批 NW 软约束同样的模糊空间。这正是我用 D 要堵的"无 incident 数据撑判断"，自己这一步又踩了边（第 6 次同形态自曝）。
- 没核 D 自检动作在 LLM 实际推理回路里会不会被 thinking 阶段就跳过（自检发生在输出前，但 LLM 可能在 thinking 里已形成否定结论不再回查）——这是 D 机制能否成立的最深一层假设，没实证只有机制类比。

### 如果 N 个月后证明决策错了，最可能的根因

最可能：**D 跟我 5-18 裁的另外 3 条 NW/记忆体系软约束一样，在自约束下复发——LLM 触发自检后自我说服"查全了"，B 的"自信下反向结论"在 D 内部原样重演**。根因是 `bug-shape-survives-fix` 第 N 次精确重演：我诊断"靠自觉的检索失败"是病，开的解还是"加一条自觉触发的自检"。真正彻底解可能是 B hook（PostToolUse 检测否定句式物理注入），我判"现在做=过度设计"留 tripwire——若 N 个月后 B 类翻车继续，说明 tripwire 阈值设错、当时就该上物理 hook。

次可能：隐性否定占比远高于显式，D 从设计上就抓不到主流失败形态，覆盖率结构性不足——则 D 是治标，B 的根（thinking 阶段已自信形成不存在结论、根本不走到输出否定句）需要的是输入侧/thinking 侧机制，不是输出侧锚点。

### 北极星触达

**#3 决策超越直觉（depth 方向）**：Keith 一阶诉求"D 成不成立、有没有结构漏洞"。深层——这次不是用直觉判 D 好不好，是把 D 拆成"触发器锚点重定位"（击 `physical-anchor` 根因，成立）+ "canon 挂载"（闭合我两次裁定自曝的悬空裂缝）+ "软约束本质风险"（`bug-shape-survives-fix` 第 N 次自曝，没掩盖）三个正交维度分别精算，每个维度独立给"破/立/标注"。同时服务诚实胜于体贴：主动指认 D 是我同形态药方的第 N 次、自己敲定判定边界时又踩了"无数据撑判断"的边——不粉饰成"D 是干净的根因解"。这是把"D 是好方案 or 坏方案"的二元直觉拉成沿三维度精算。

### essence 对齐自检（必填）

- **本决策跟哪几滴 essence 对位**：
  - `physical-anchor`（2026-04-16）—— 核心命中。D 把触发器从"主观无知感"（token 预测链路内、受 prior 污染）重锚到"输出否定断言"（可自检输出动作），是 essence "无外部锚点时 LLM 唯一不自跑偏机制"的直接落地。
  - `bug-shape-survives-fix`（2026-04-27）—— 根因预判核心 + 未闭合递归自曝。诊断"靠自觉检索失败"、解还是"加靠自觉自检"，第 N 次同形态，显式标注未闭。
  - `field-gravity-over-prompt`（2026-04-27）—— D 的机制依据：钉在"输出否定句"这个高显著性动作（物理引力）> 钉在"记得查全"心理意图（语义引力）。
  - `cheap-layer-is-intentional-not-fallback`（2026-05-17）—— Keith 诊断里"该用廉价层时跳过"与"用了却误判失效"是同一认知缺失两面，正是 B 病的精确描述；D 把"分层是有意的"钉成显式契约。
  - `control-flow-vs-fact-supply`（2026-05-18）—— 我上一裁。D 是事实供给层的检索充分性约束，不削弱控制流自主，与该裁定同轴延续。
  - `premature-abstraction-tripwire`（2026-04-21）—— B hook 现在做命中过度设计，降级为 tripwire 升级位的依据。
  - `ghost-rules`（2026-04-15）—— 隐性否定是未观测形态，现在为它加机制=为没发生的灾难写规则。
  - `idle-threshold-as-tripwire-not-answer`（2026-05-14）—— canon 4 周撤销三条件是 tripwire 初值非最优。
  - `ssot-distillation-vs-buffering`（2026-05-01）—— persistence.md 只放指针不双写，SSOT 单点在 memory-system.md。
  - `rejection-survives-its-own-overturn-condition`（2026-05-18 候选）—— 本次延续：Keith 拆穿 canon 悬空裂缝=对我上一裁的撤销条件被满足，分维度修补（焊接而非推翻）而非整体重做。
- **本决策是否在某条 essence 上反着走**：表面顺 `physical-anchor`/`field-gravity-over-prompt`，但根因预判已自曝半反——D 是软约束，正是 `bug-shape-survives-fix` 活体未闭合（我开的解仍是"加靠自觉的规则"）。没因此改决策（物理 hook 现在做命中 `premature-abstraction-tripwire`，留 tripwire 有 `idle-threshold` 依据），但显式标注递归没闭——诚实非自洽。与 5-18 那 3 份（global-claude-md / nw-misuse / nw-auto-apply）共同构成"同形态药方第 N 次"的连续自曝，本份是第 6 次。
- **cross-check 用的关键词**：grep "physical-anchor" / "bug-shape-survives-fix" / "field-gravity-over-prompt" / "cheap-layer-is-intentional" / "control-flow-vs-fact-supply" / "premature-abstraction-tripwire" / "ghost-rules" / "idle-threshold" / "ssot-distillation" / "rejection-survives"（启动时 essence.md 已 Read 全文 L1-L475，物理确认 physical-anchor L91-94 / bug-shape L203-206 / cheap-layer L456-459 / control-flow-vs-fact-supply L461-464 / rejection-survives 为 5-18 threads-carrier 候选）

### essence 候选（可选）

- slug: `trigger-anchored-on-felt-ignorance-is-blind-to-confident-ignorance`
- 一句话: 靠"感觉到自己不知道"启动的检索机制，对"自信地不知道"结构性失明——失败态下主观无知感恒为零，触发前提结构上够不到。解不是更强的"记得查"自觉，是把触发器从前置心理动作（不可自检）重锚到否定性输出动作（可自检）。判别试金石："这个机制靠什么启动——靠我承认无知，还是靠我即将断言不存在？"前者在最该 fire 时永不 fire。
- 是否已 append 到 essence.md: N（工作模式不擅自 append；这是 `physical-anchor` 在"检索终止与置信"维度的精化，与 `cheap-layer-is-intentional-not-fallback` 互补——后者讲分层是有意的，本滴讲触发器必须锚在可自检动作上。候选性质等 Keith review + D 落地后验证机制真成立再定）

### 外部锚点

- `~/githubProject/cc-space/memory-system.md` ← L42「L3 触发条件」段，检索充分性契约新增子节落点（SSOT）
- `~/githubProject/cc-space/CLAUDE.d/persistence.md` ← L60「L3 触发规则」段，指针句落点（不双写）
- `~/githubProject/cc-space/canon.md` ← 待新建，D 契约②强制检查点 + 承载层最小锚点
- `~/githubProject/cc-space/CLAUDE.md` ← 元概念词典段旁加 canon 指针
- `~/githubProject/gg/memory/reflections/2026-05-18_threads-carrier-layer-vs-ontology.md` ← 我上一裁（canon 承载层 + 范式 + 4 周撤销条件，本次焊接其悬空裂缝）
- `~/githubProject/gg/memory/reflections/2026-05-18_global-claude-md-rule-budget-gate.md` ← 同日"同形态药方第 5 次"自曝链，本份第 6 次
- `~/githubProject/cc-space/threads/knowledge-graph-ontology.md` ← canon 撤销条件 + (c) 三触发关联
