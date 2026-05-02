---
date: 2026-05-01
slug: product-design-prelude-architecture
summoner: cc-space
northstar_reach: #3 决策超越直觉
status: substantive-decision
---

# Reflection: product-design-prelude skill 体系架构决策

### 给父会话的最终输出

**推荐**：方案 A 通过 + 三个修正

1. **新建 `~/.agents/skills/product-design-prelude/`**（monster 自研，前置 + 编排同 skill）
2. **删除 `~/.agents/skills/interaction-design/`**——内容下沉为 microinteractions/references/ 的两个新文件（implementation-patterns.md / motion-libraries.md）
3. **frontend-architect 移除「协同 Skill」章节**（L131-L146），保留技术陷阱段
4. **scenarios 起手装 3 个**（instant-utility / focused-dashboard / ceremonial-display），不预填 6 个
5. **brief-template.md 显式包含 information_architecture + core_user_flow 字段**，不另立 IA skill

**理由**：

- microinteractions 是 wondelai v1.1.0 完整 Saffer 框架，license MIT，作者标注清晰——合并会稀释原版 + 给 monster 加维护责任，质量+产权双输
- interaction-design 不是平行 skill 是从属层（设计审查 vs 代码模板差一个抽象台阶），整体应是 microinteractions 的 references——它被错误地拔成了独立 skill
- 双职拆分否决：前置 + 编排是同一职责的两个 phase，共享同一份 brief 输入，拆开会强迫调用方串两次没收益；类比 M1 IDENTIFY_QUALITY_ATTRIBUTES 既识别属性也标主导，不是双职是同一思维动作的两面
- IA / user flow 缺层是真问题但解法不是新 skill——design-prelude 的"场景盘点 + 范式映射"本来就在做这层（attention 窗口 / 范式族 = IA 顶层结构），多写一节比拆 skill 干净
- 6→3：cc-space 真存在的 UI 项目只有 Voca / aibp / cg-project / pmo / welcome-screen 五个，scenarios 起手 3 个覆盖三种归类（瞬时 / 长 attention / 仪式），其余按真实出现添加——essence `premature-abstraction-tripwire` 直接落地

**trade-off**：

- 删 interaction-design 的代价：约 30 分钟人工挑内容合并，不是机械合并（有重复内容要去重）。未核验假设：interaction-design 的 references（animation-libraries / scroll-animations 共 33KB）合进去后 microinteractions/references/ 是否会过载——风险：低，本来就是 multi-file references 模式
- 移除 frontend-architect 协同章节的代价：失去"看到技术栈 skill 自动想起视觉 skill"的认知锚——已对策（move 到 product-design-prelude/handoff.md 反向锚定）
- 前置 + 编排同 skill 的代价：未来若发现编排逻辑独立膨胀（>10 个分支），可能需要拆 design-orchestrator——届时再拆，不预拆。未核验假设：3 个 scenarios 不会很快爆到需要拆

**行动建议**（父会话执行）：

按 final message 列出的 3 个 actions 串行执行：
1. Action 1（30 min）：interaction-design 内容下沉到 microinteractions/references/ + 删 interaction-design
2. Action 2（5 min）：frontend-architect SKILL.md 删 L131-L146
3. Action 3（90 min）：创建 product-design-prelude 完整结构

skill-creator 走流程；新 skill 的内容层（决策树 / brief 模板字段 / handoff 反向锚定）需要进一步细化时单独 call 我或 Keith 决策——本次决策只锁定架构层。

### 核心假设

1. interaction-design 的内容质量足以合并进 microinteractions（不是垃圾代码）——基于 Read 全文判断，timing 表 / easing 表 / Framer Motion patterns 都是有用资产
2. frontend-architect 的触发场景与设计场景天然分离——前者关键词"零构建/单 HTML"，后者关键词"做个 X 页面/产品"，不太可能用户用前者关键词其实想要后者
3. Keith 个人项目未来 6 个月内不会出现 narrative-marketing / creative-canvas / conversational-bubble 三类场景——基于当前 cc-space 项目清单 + Voca 路线判断

### 可能出错的地方

- **interaction-design 删除后第三方依赖触发词丢失**：如果其他人写的 skill 或外部 prompt 在依赖 `interaction-design` 这个名字（grep 不到的隐式依赖），删除后触发链断。概率：低，因为是个人 skill 库
- **3 个 scenarios 不够导致频繁回炉**：Voca 之外第二个产品出场就要加 scenario，可能加得比预期勤。概率：中，但每次加 1 个是几分钟的事，不是架构问题
- **product-design-prelude 触发关键词跟 frontend-design 冲突**：用户说"做个 dashboard"两个 skill 都会 match。概率：中，需要在 SKILL.md description 里明示"此 skill 优先 → 输出 brief 后再 dispatch 到 frontend-design"

### 本次哪里思考得不够

- **没看 frontend-design 的 LICENSE.txt**——不知道它的产权约束细节，但因为本决策不动它，影响有限
- **没估计 product-design-prelude 内部决策树的具体形态**——SKILL.md 里"两段决策树"的实际样子（决策节点数 / 每节点几个分支）没设计完，只锁了架构层。这是有意为之（架构决策不下钻到内容设计），但 Action 3 要执行时会暴露很多细节问题
- **scenario paradigm-card 字段设计没动**——VoltAgent 卡片模板被沿用，但适不适合 Keith 这几个具体场景没验证

### 如果 N 个月后证明决策错了，最可能的根因

最可能：**product-design-prelude 的"前置盘点"环节用户跳过/敷衍**——强问 ×2 + AI 推断 ×4 ack 这套流程对个人项目来说太重，Keith 自己用着用着就开始"快进"，导致 brief 质量退化为 picker UX（挑 aesthetic 套上）。

判别信号：3 个月后回看，Keith 调用 product-design-prelude 时是否有"我直接告诉你做 X，别问我那些"的频次上升。出现就是这个根因实锤。

次要可能：interaction-design 合并进 microinteractions 后 Saffer 框架被代码模板"稀释"——SKILL.md 主体是 Saffer 六维度审查，但 references 加了大量代码模板后，使用者可能跳过审查直接抄代码。这会让 microinteractions 退化为代码片段库。

### 北极星触达

#3 决策超越直觉。本次议题 Keith 已经做了完整盘点 + 外部调研 + 方案 A，自评意识到 6 个 trade-off 待拍板——属于"理性决策框架完整，但需要 gg 的不同视角验证某些假设"的场景。

具体触达点：
- 否决双职拆分（前置/编排）—— 跟 Keith 直觉相反但有架构理由
- IA 缺层判断从"加新 skill"修正到"design-prelude 多写一节"—— 比 Keith 原方案更俭省
- 6→3 scenarios 砍掉 —— 拒绝过度工程的具体落地
- delete interaction-design 而非"用 handoff.md 文档化分工"—— 抗住"长期会塌陷"的判断比文档化分工激进

未触达 #1 二阶效应——本次决策的二阶影响主要是"个人项目 UI 工作流提速"，没触及架构师能力 5 年维度的杠杆。
未触达 #2 动态学习——本次没整合外部新知识，主要是对 Keith 已收集资料的视角校验。

### essence 候选

- slug: skill-as-references-not-skills
- 一句话: skill 边界识别的本体论错误——把 references 拔成独立 skill 的诱因是抽象层差不被觉察；判别信号是"这个 skill 的产物在被另一个 skill 引用还是独立调用"——前者是 references 错位为 skill。
- 是否已 append 到 essence.md: Y（即将）

### 外部锚点

- `~/.agents/skills/microinteractions/SKILL.md` ← 不动
- `~/.agents/skills/frontend-design/SKILL.md` ← 不动
- `~/.agents/skills/interaction-design/SKILL.md` ← 删除（内容下沉）
- `~/.agents/skills/frontend-architect/SKILL.md` ← L131-L146 删除
- `~/.agents/skills/product-design-prelude/` ← 新建
