---
date: 2026-05-08
slug: cc-space-design-asset-integration
summoner: cc-space
northstar_reach: #1 二阶效应
status: substantive-decision
---

# Reflection: cc-space 设计资产整合方案（借鉴 open-design）架构层判断

### 给父会话的最终输出

**总体判断**：方案 v2 整体可落，但 12 scenarios + reference-systems/ 两块要砍；落点 shared/design/ 不对，scenarios 该上提到 product-design-prelude/scenarios/；critique-checklist 不要做。

**推荐（按优先级）**：

1. **第一步（半天 / 真痛点）**：在 `cc-space/shared/design/` 只做两个文件——
   - `cc-space-design.md`（9-section SSOT，cc-space 自己的视觉契约浓缩）
   - `examples.md`（已落地锚点链接清单）
   - `cc-space/CLAUDE.md` UI 默认段改 1 行指针指向 cc-space-design.md
2. **第二步（按需 / 触发驱动）**：scenarios + critique 等 product-design-prelude / frontend-design 真实使用反馈，该上提到 skill 层的就上提，**不在 cc-space 项目里建第三处载体**。reference-systems/ 不做。
3. **directions.md（cc-space 已落地视觉学派盘点）可做可不做**——它跟 examples.md 重叠度高，建议合并进 examples.md 的 frontmatter 标签或直接砍。

**理由（按"想让你拍的 6 点"对应回答）**：

1. **落点 shared/design/ 不合理**：是第三个设计资产载体（与 product-design-prelude/scenarios/ 和 cc-space CLAUDE.md UI 段并列），SSOT 必然漂移。scenarios（dashboard/docs/kanban）是**全局复用资产不是 cc-space 资产**——挂在哪个项目都通用，应归 product-design-prelude/scenarios/。reference-systems（anthropic/apple/xhs）是 frontend-design/references/ 该承载的视觉语言库。只有 cc-space-design.md（项目特定视觉契约）+ examples.md（已落地实例锚点）真属于 cc-space。
2. **三件套必要性**：critique 不做（review-routing 已是流程审 SSOT，再加同位 checklist 是切碎触发；5 维 critique 是 LLM 自审 prompt 检查表，对应 essence `task-compliance-is-not-truth` 高发区）；reference-systems 砍掉（Keith 视觉主调已清晰，二手摘要不如临时 WebFetch 原站；对应 essence `caged-freedom`——给灵感空间建笼子）；scenarios 减半（cc-space 真做过的 5 个，其余凭想象编内容是 `premature-abstraction-tripwire` 反例）。
3. **reference-systems 在 cc-space 里没意义**：Keith 真要参考时不会 Read 二手摘要，会临时翻 cosmos.so / mobbin / apple HIG 原站。常被消费的是 examples.md（已落地实例对比），不是抽象 design system 摘要。
4. **scenarios.md 慢慢长 vs 一次写满**：慢慢长。但要立闸门——「新 scenario 入场条件：cc-space 至少 1 个真实落地实例 + 第二次同类需求出现」，否则 Keith 兴致来时一次扩到 8 个仍是同失败模式。
5. **CLAUDE.md 注入 context skill 自然能看见**：一半 work 一半不 work。work 部分：CC 进 cc-space 时 CLAUDE.md 进 system prompt，skill LLM 能看见。**不 work 部分**：skill 自己的 SKILL.md / references/* 不会自动应用 CLAUDE.md 设计契约——product-design-prelude 的"范式映射"段不会自动把"米白/中文/工业"作 prior 注入候选生成。除非在 SKILL.md 里写明"触发时如果在 cc-space 项目内先 Read cc-space-design.md"——但这条指针会成为 skill 跨项目通用的污染。**正确解耦**：cc-space-design.md 留 cc-space（项目特定），scenarios 上提到 skill（跨项目通用），靠 system prompt 里的 cc-space-design.md 自动 prior 校准，不靠 skill 显式 Read。
6. **未看见的架构问题**（盲区 3 条）：
   - **盲区 1**：本动作的方法论本身在 essence 里有红旗——`extraction-meta-inheritance`：批量抽取 open-design 方法论 = 在造单人版 mini open-design，事实上抵消抽取目的。识别信号"源作者看这份方案会说'对，按你工作量做轻量版'"反而是危险信号。
   - **盲区 2**：Keith 工作模式（独立工作者 / 单线工作）跟 open-design 假设（团队 / 多项目 / 设计系统化）不符——重型设计资产基础设施的固定成本几乎收不回。
   - **盲区 3**：动机检视——这是真痛点还是借鉴诱发的方案？方案缺"为什么要做"段。诚实自检：summon-deck brief 写得很顺、cc-space CLAUDE.md UI 默认段实际覆盖了主要需求、真正触发更可能是"读 open-design 觉得很好"。**这是探索类工作不是工程必要项**——按"允许慢、允许反复、产出小可接受"走，不要套"完整 v2 方案 8-10h 单天落地"的工程节奏。对应 essence `wish-as-pain-laundering`。

**Trade-off**：
- 砍掉 reference-systems / critique / 大半 scenarios = 损失"完整体系感"，可能 Keith 觉得"做得不够 systematic"——但 systematic 不是终点，**SSOT 不裂 + 真实使用反馈驱动扩展**才是。
- 上提 scenarios 到 product-design-prelude/scenarios/ = product-design-prelude skill 会变重——但这是"内容回到该在的层"不是工具膨胀，对应 essence `tool-elevation-as-occam`。
- 第一步只做 2 文件 = 看起来"投入产出小"——但探索节奏的产出本来就允许小，强行把它当工程节奏跑会触发 `means-end-inversion`（工具维护吞噬目的）。

**未核验假设**：
- 假设 1：Keith 之前"做新 UI 时缺设计资产整合"不是真痛点——基于 summon-deck/Voca/cookie-arcade 等近期项目都顺利完成的观察推断，未直接问 Keith"哪次卡住了"。如果 Keith 反馈"X 项目实际卡了但你没看见"，第一步会扩展到 3-4 文件。
- 假设 2：scenarios 上提到 skill 不会引入 cc-space 特定污染——基于"dashboard/docs/kanban 是通用场景"判断，但 cc-space 的 dashboard 确实带 Keith 个人偏好（米白/思源/工业），上提时需要有意识地**把通用部分留 skill / cc-space 特化部分留 cc-space-design.md**。

**行动建议（父会话下一步具体动作）**：
1. 把这份判断回给 Keith，请他 ack 第一步收敛方案（2 文件 + 1 行指针）
2. Keith ack 后直接做第一步——不需要再 call gg 拍细节
3. 第二步留作"按需触发"——下次做新 UI 项目时如果 product-design-prelude / frontend-design 真不够用，再单独决策上提 scenarios / 加 critique
4. **如果 Keith 不 ack 收敛方案、坚持完整 v2** → 可以做，但请他显式标记"这是探索类工作"，按探索节奏走（允许慢、允许半成品、不套 cost-benefit），并显式 ack 接受三个盲区的风险

### 核心假设

1. cc-space-design.md（项目特定视觉契约）+ examples.md（已落地锚点）已覆盖 80% 真实使用场景
2. scenarios（dashboard/docs/kanban）属于跨项目复用资产，正确归宿是 product-design-prelude/scenarios/
3. Keith 这次的触发更可能是"读 open-design 觉得很好"而非真实痛点——基于近期项目（summon-deck / Voca / cookie-arcade）完成顺利的观察
4. CLAUDE.md system prompt 注入对 skill 内部判断逻辑的影响是**间接 prior**（被 LLM 注意力吸收）而非**显式 Read**（skill 主动调用文件）

### 可能出错的地方

最可能崩在假设 3——如果 Keith 反馈"我确实有过 N 次缺整合卡住"，第一步收敛方案就不够，得回到 v2 接近完整版。概率 30%：cc-space 近期项目顺利不代表"没痛点"，可能是 Keith 通过其他方式补偿了（每次手动翻历史工作区 / 凭脑子记）。

第二可能：scenarios 上提到 product-design-prelude 后**实际触发率仍很低**——product-design-prelude 起手 3 scenarios 用了 7 天才被首例消费，如果再扩 5 个，每个真触发可能要月级。这意味着上提"在层级上正确但消费驱动不足"——但仍然比留在 cc-space 项目里建第三载体好。

### 本次哪里思考得不够

1. **没物理验证 Keith 历史项目卡顿点**：判断"summon-deck/Voca 完成顺利"基于 thread 和 essence 的快照，没去 grep 这些项目的协作过程是否有"找不到锚点 / 重新发明"片段。如果有，盲区 3 的诚实自检需要修订。
2. **没核 directions.md 的实质必要性**：方案里 directions.md 是"cc-space 已落地视觉学派盘点（descriptive）"，跟 examples.md 重叠到什么程度没量化判断。建议合并是 OCCAM 直觉，没数据底。
3. **没考虑 frontend-design vs product-design-prelude 边界对 cc-space-design.md 的影响**：cc-space-design.md 9-section（color/typography/spacing/layout/components/motion/voice/brand/anti-patterns）是**视觉系统级**资产，按现有 skill 分工应归 frontend-design 而非 product-design-prelude。但落到 cc-space 项目内时，由 cc-space CLAUDE.md 注入即可，不需要细分——这层我没在判断里说清楚。

### 如果 N 个月后证明决策错了，最可能的根因

**根因 A（概率 40%）**：第一步 2 文件方案太"轻"，Keith 在做下一个新 UI 项目时仍然每次重新整理一遍设计契约，发现"没有 systematic 加成"。这种情况下回头看，应该一次到位做"3-5 scenarios + cc-space-design.md + examples.md"中等版本，而不是只做 2 文件。

**根因 B（概率 30%）**：scenarios 上提到 product-design-prelude 后跟 skill 自身的 instant-utility / focused-dashboard / ceremonial-display 三类范式碰撞——dashboard / docs 两个新 scenario 跟 focused-dashboard 边界不清，导致 skill 内部 scenario 体系裂化。这种情况下回头看，应该把新 scenarios 收编进 focused-dashboard（作为子类）而非平级新增。

**根因 C（概率 20%）**：本判断对"借鉴 open-design 是否真痛点"的诚实自检过度——其实 Keith 在做 cgboiler 自我表征 / mirror / summon-deck 多种产物时确实需要统一视觉契约 SSOT，我把"近期项目顺利"误读为"没痛点"。

**根因 D（概率 10%）**：CLAUDE.md 注入 context 对 skill 判断的影响其实**比我估计的小**——skill 触发时父会话的 system prompt 不一定完整传递给 skill subagent（subagent 有自己的 system prompt），cc-space-design.md 实际上没被 skill 看见，需要 skill 显式 Read。

### 北极星触达

#1 二阶效应。本次判断的核心价值不是"做不做这个方案"，而是**识别"借鉴诱发的方案"这个反复出现的失败模式**——把外部范式 catalog 当抽取对象 → 在自己项目里造迷你版 → fixed cost 收不回 → 维护吞噬目的。这条二阶规律对未来"读了 X 想做 X 的轻量版"类决策都适用，不限本次。

### essence 候选

- slug: `borrowed-method-as-mini-source`
- 一句话: 批量抽取外部体系的方法论 = 在自己项目里造它的迷你版——抽取动作反向继承被抽取对象的元约束，事实上抵消抽取目的；判别试金石"源作者看这份方案是否会说'对，按你工作量做个轻量版'"——会说就是危险信号，不是赞许。
- 是否已 append 到 essence.md: N（在退场动作里 append）
- 跟既有关系：是 `extraction-meta-inheritance`（2026-04-29）的具体落地——前者是抽象规律，本条是判别试金石的精化（"源作者赞许"反而是危险信号这一反直觉点）。

### 外部锚点

- `~/githubProject/cc-space/CLAUDE.md` UI 默认段（现有视觉契约 SSOT）
- `~/githubProject/cc-space/threads/product-design-prelude.md`（skill 演化历史 + summon-deck/cc-copilot 暴露的 brief 模板局限）
- `~/.agents/skills/product-design-prelude/SKILL.md`（scenarios 上提的目标载体）
- `~/.agents/skills/frontend-design/SKILL.md`（reference-systems 如要做的正确归宿）
