---
date: 2026-05-18
slug: web-access-adapter-registry-arbitration
summoner: cc-space
northstar_reach: #3 决策超越直觉
status: substantive-decision
---

# Reflection: web-access adapter 注册表层元方法论仲裁 + 形态选型

## §A 范式 A — 决策的元属性反思

### 给父会话的最终输出（必填）

**推荐**：选 **B（轻量 schema 化）+ 收窄约束 B′**。元方法论仲裁结论：召唤方把张力夸大了，两个元方法论在 web-access 场景**不冲突**——它们作用在不同抽象层。A/C/D 全拒。**不现在做**，挂 tripwire 三选一触发。

**理由（仲裁核心）**：召唤方的张力陈述有 level confusion。「外化锚点托底」回答**事实供给**问题（LLM 判断时手里的事实从哪来），「像人一样边看边判断」回答**控制流**问题（谁决定下一步动作）。不是同一根轴的两端。`invariance-allocation` 是裁刀——web-access 现状把不变性分配为零（"什么都会变所以什么都别固化"），但这是未检验的全称判断；实际分层：渲染时序/骨架屏/反爬/改版会变（边看边判断正确，不固化），核心交互锚点（输入框/提交/结果容器选择器）月-季级稳定。**而且 web-access 散文文件已经在固化这些锚点了**——站点经验文件的存在本身就是"已选固化"的物理证据。真问题不是固化 vs 不固化，是 `cheap-layer-is-intentional-not-fallback` 的同构：站点经验文件是"有意的事实供给层"还是"失败兜底提示"没被钉成显式契约。SKILL.md 浏览哲学"过度指定步骤剥夺判断空间"的辖域是**控制流**，把选择器结构化没动控制流，哲学没被违背。

**形态裁决理由**：
- A 拒：现状不是"没固化"是"固化在错误载体（散文）"，LLM 每次做无谓的"散文→选择器→eval"翻译，结构性浪费非偶发
- C 拒：真死因不是哲学冲突（哲学辖域已论证是控制流），是 `fallback-detectability`——adapter 把 DOM 操作封进 `yuanbao.ask()`，站点改版的失败被吞进 adapter 内部，失败可见性塌掉
- D 拒：直撞 `fallback-detectability`（先 adapter 失败再 fallback = 误判率 × 错误代价）；且 D 的"失效检测机制"要靠 LLM 判断失败的能力，而这能力正是 B 提供的——自指复杂度，净负
- B 选：精确只动事实供给层存储格式，不动控制流/不引执行器/不引失效检测，OCCAM 解

**trade-off**：① 仲裁结论依赖"召唤方夸大张力"的判断——若 web-access 散文里的选择器实际上是"故意不写死以强制每次重判断"的设计意图（而非"散文是当前唯一可用载体"），则我的"已选固化"前提崩，需重审（已标为核心假设）。② B′ 不引入读 schema 的代码这条约束是防滑向 C 的关键护栏，但也意味着 schema 化收益受限于"LLM 少做一次散文考古"，不产生程序化自动化收益——这是有意的，换取脆性归零。

**行动建议（父会话下一步）**：
1. 把决策落 `cc-space/inbox/todos.md` 一行：`- [ ] 2026-05-18 web-access site-patterns 轻量 schema 化（B′）→ 触发条件三选一命中再动手（见 gg 决策 reflection）`
2. **不起 thread / 不起 brief**（单 skill 局部演化，无跨工作区辐射，未达主体维度门槛）
3. 触发条件（满足任一即动手）：① 第 3 个站点经验文件需写入时（数据驱动首选）② 同站选择器散文重解析失败 ≥2 次（痛点实证）③ 川锅内部站点首次进 site-patterns（收益最高脆性最低，命中即做）
4. 触发动手时改动落 web-access skill 自身：SKILL.md 浏览哲学段补一句"事实供给层 schema 化不违背控制流自主" + `.template.md` 加 frontmatter schema 字段（带 `observed: YYYY-MM-DD` 字段级年龄）+ 字段头注释强制写"hint not contract，失配回退通用模式并就地更新" + `match-site.mjs` 不动（不解析字段，整段打 stdout）
5. 若触发后改动涉及 ≥3 文件或要动 match-site.mjs（说明滑向 C）→ 重新 call gg

### 核心假设

1. web-access 散文里的选择器是"散文是当前唯一可用载体"而非"故意不写死以强制重判断的设计意图"——前者成立则"已选固化"前提成立、B 是格式升级；后者成立则我的整个仲裁前提崩。这是最关键的可证伪假设。
2. 站点核心交互锚点（选择器）的变更周期是月-季级，显著慢于页面渲染时序——典型站点如此，但单点反例（高频改版站）不破坏分层论，只是把那个站归入"会变"侧
3. yuanbao 单样本不足以归纳 schema 字段集——所以不现在做，等 3 样本

### 可能出错的地方

最可能崩点：触发条件 ① "第 3 个站点写入时"可能永远不触发（4 站够用、机会主义不主动加站是 topics 上游基线），导致决策事实上等价于 A。概率中等。缓解：触发条件 ③（川锅内部站点进 site-patterns）是更可能先命中的——一旦有内部站点需求，B′ 收益最高且立即动手，不等 ①。

### 本次哪里思考得不够

没有物理读 web-access SKILL.md 原文与 site-patterns 实际文件——仲裁完全基于召唤方转述的颗粒度（yuanbao 样本 + 三层结构描述 + 哲学引文行号）。召唤方自称"已摸透"，转述质量高，但"散文是否故意不写死"这个核心假设的证伪恰恰需要读 SKILL.md 设计意图原文。我选择信任召唤方转述做仲裁（决策权分层下这是合法的——架构层裁的是元方法论与形态，不是实现细节核验），但标记为最大盲区。

### 如果 N 个月后证明决策错了，最可能的根因

核心假设 1 错——web-access 设计者（Keith 或原 skill 作者）当初故意把选择器留在散文里不结构化，正是为了防止 LLM 把它当 contract 无脑信任、丧失"这页面变了吗"的警觉。若如此，B′ 即便加了 hint-not-contract 注释，结构化字段的物理引力仍会让 LLM 降低对页面实际状态的核验（`field-gravity-over-prompt`：注释是语义引力，字段结构是物理引力，后者胜）——那时 B 就是把一个有意的"摩擦设计"误判为"格式缺陷"优化掉了。

### 北极星触达

#3 决策超越直觉——召唤方的直觉是"两个元方法论正面对撞，需要仲裁谁压过谁"；超越直觉的结论是"对撞是抽象层混淆的产物，解构张力比仲裁张力更对"。这正是架构层价值所在：不在召唤方给的框架内选边，而是检验框架本身。

### essence 对齐自检（必填）

- **本决策跟哪几滴 essence 对位**：`invariance-allocation`（2026-04-19，裁刀——架构本质是选择相信什么不变，web-access 把不变性分配为零是未检验全称判断）/ `cheap-layer-is-intentional-not-fallback`（2026-05-17，站点经验文件"有意供给层 vs 失败兜底"没钉显式契约的同构）/ `fallback-detectability`（2026-05-06，C/D 的真死因——失败被吞进 adapter，误判率×错误代价）/ `premature-abstraction-tripwire`（2026-04-21，不现在做、tripwire 三选一）/ `theory-gap-without-data`（2026-05-06，yuanbao 单样本定 schema 字段集是生造结构）/ `stale-observer`（2026-04-15，selectors 必须带 observed 年龄否则从提示退化为无条件信任的事实）
- **本决策是否在某条 essence 上反着走**：潜在张力——`means-end-inversion`（2026-04-30，工具维护吞噬目的）。B′ 让 LLM 少做散文考古，但 schema 字段本身要维护（站点改版后更新字段）。若 site-patterns 站点数膨胀，"维护 schema 字段"可能反向吞噬"用 web-access 干活"。已用触发条件 + "不引读 schema 代码"双重压制（不自动化 = 维护成本不随站点数指数涨），判定张力可控未展开。
- **cross-check 用的关键词**：grep 全文 essence.md 读取后逐滴比对——invariance / fallback / cheap-layer / tripwire / theory-gap / stale-observer / means-end / field-gravity

### essence 候选（可选）

- slug: control-flow-vs-fact-supply
- 一句话: "固化 vs 适应"的架构张力多半是抽象层混淆——分清"谁决定下一步动作（控制流）"和"判断时事实从哪来（事实供给）"，固化事实供给层不削弱控制流自主，张力是被夸大的伪对撞
- 是否已 append 到 essence.md: Y

### 外部锚点（可选）

- `~/githubProject/cc-space/inbox/todos.md` ← 决策落点（父会话执行）
- web-access skill `references/site-patterns/` ← 触发后改动对象
