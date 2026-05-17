---
date: 2026-05-15
slug: threads-ontology-premature
summoner: cc-space
northstar_reach: #3 决策超越直觉
status: substantive-decision
---

# Reflection: cc-space threads ontology 化时机判断（不做 + 反推 Keith 撤 todo）

### 给父会话的最终输出（必填）

**推荐**：不做。Keith 今天 `inbox/todos.md` 加粗标的 "今天要深入做" 这条 todo 应当被正面挑战——撤回或改写为"先治理现状 + 定义触发信号"，而非"动手做 ontology 化"。

**理由（四条，按强度排序）**：

1. **物理数据反对命题**——刚扫了 threads/：76 文件 / 跨 thread 引用 122 条 / 平均 1.6 条/文件 / 41% 文件零跨引用 / 73 active（治理动作未启动）。"缺 ontology map"假设需要关系密集，但数据显示稀疏——map 上没多少线要画。形式化 70 个 frontmatter 会产 70% 空字段（造迷你版）

2. **跟现有契约正面冲突**——`threads/README.md §演进路线`明确"不在 v0 上提前堆抽象 / 由 memory-lab 反哺替换"；`threads/knowledge-graph-ontology.md §(c)`三触发条件（实体破千 / 自动化多跳查询 / threads 爆炸）当前都未命中；§(a) cgboiler 议题 15/16 ontology 扩展"等议题 12 灰度跑通后启动"。Keith todo 跟自己的契约冲突但没解释为什么绕开

3. **essence 多滴反对**：
   - `wish-as-pain-laundering`（2026-04-22）——优雅命题但 inbox 无具体翻车案例记录
   - `theory-gap-without-data`（2026-05-06）——没数据时 LLM 找的"缺口"是生造的
   - `ontology-expansion-velocity-needs-cap`（2026-05-07）——新增标准"已有桶不能容纳量 ≥ 新桶预期 3x"不达
   - `fermentation-without-detector`（2026-05-15 昨夜）——knowledge-graph-ontology thread 三落点都"等触发条件"但没定信号怎么观测，Keith 今天凭手感觉得"该深入"= 发酵无检测器的典型副作用
   - `borrowed-method-as-mini-source`（2026-05-08）——叶小钗 KG + cgboiler ontology 抽到 cc-space 协作记忆 = 造迷你版
   - `premature-abstraction-tripwire`（2026-04-21）——过早抽象对症解是 tripwire 不是"今天深入做"

4. **优先级倒挂**——cgboiler 自己的 ontology（议题 15/16 真实体 + 真业务关系网）还在等议题 12；cc-space 协作记忆的 ontology 是借来的迷你版，小弟先长大

**trade-off**：
- 可能错的方向：如果 Keith 已累积我看不到的痛点信号（多次因找不到主体属性翻车），那我错。**这正是 Keith 需要回应的部分**——具体翻车案例
- 不做的代价：Keith 今天"想深入做"的精力没出口。建议转向两件 ROI 更高的事（见行动建议）

**行动建议（父会话给 Keith）**：

按"举手 + 否决权"语法回 Keith：

> "Keith，这条 todo 我不动手，建议你撤回或改写。理由四条（见上）。
>
> **如果你不接受这个否决，给我一条具体翻车案例**——'X 月 X 日因为 thread 没主体属性 / 没关系网，我们干了什么蠢事'。说不出来，那就是 wish-as-pain-laundering，应当撤 todo。
>
> **如果你接受这个否决，建议把今天的精力转到这两件 ROI 更高的事**：
> 1. 给 `knowledge-graph-ontology` 三落点 (a)(b)(c) 的"等触发条件"定**可观测信号**（写在该 thread 里）——治 `fermentation-without-detector`
> 2. 起 `threads/` 状态治理小动作：73/76 都是 active，明显有沉睡的——人工巡检转 paused/abandoned。比 ontology 化 ROI 高一个量级"

### 核心假设

1. **关系密度是 ontology 化 ROI 的主驱动**——122/76=1.6 条/文件 + 41% 零引用 → ROI 不达。**可能错**：Keith 如果有"隐性关系"未被 markdown 互引落地的痛点（比如他脑子里有 A 影响 B 但没写下来），那密度数据不代表真实关系网
2. **Keith todo 描述里的"今天要深入做"代表他确实想做，不是发问**——Keith 偏好"举手 + 否决权"语法，所以我用否决式回应。**可能错**：他可能只是想讨论而非动手
3. **threads/README.md 的"不在 v0 上堆抽象"契约对 Keith 仍有效**——这是他自己 4-22 设计模式写的。**可能错**：契约可能已被 Keith 内部更新但 thread 没改

### 可能出错的地方

最可能崩的点：**Keith 有我看不到的痛点信号**——他在 cgboiler 议题或 cc-assistant 实战里多次遇到"找不到主体属性 / 关系网"翻车，但没落到 inbox 也没说给我。如果他给得出具体案例，我的 1.6 条/文件 物理数据论证就被部分推翻——但即便如此，方向也应该是先补痛点记录机制（inbox 加"主体属性查找翻车"tag），跑 N 次再决定上 ontology，而不是直接动 70 个文件 frontmatter。

概率：30%——Keith 抛出 todo 时通常有信号，但不一定能说清；他偏好让 gg 反推他。

### 本次哪里思考得不够

1. **没扫 inbox/closed/** —— 可能有已关闭的 ontology 相关讨论我没看到
2. **没去看 memory-lab/** —— Keith 提"由 memory-lab 反哺"但我没看 memory-lab 当前进展是否已经能反哺。如果 memory-lab 已经有阶段性产出指向 entities 化，那时机判断要改
3. **threads_sync.py 没读** —— 没看它是否已经有任何"实体抽取"半成品（可能 Keith 已有部分实现想顺势完成）

### 如果 N 个月后证明决策错了，最可能的根因

**根因预判**：3 个月后回看，最可能的崩点是"低估了 Keith 的隐性痛点信号"——他确实在 cgboiler 议题或 cc-assistant 实战里多次因为缺主体属性翻车（但当时没显式记录），3 个月后某次会话他说"我早跟你说该做 ontology 化你拦着"。**反过来的根因**（"我对了 Keith 撤 todo 但什么都没做"）也存在——但即便如此，时机判断的损失 < 70 文件改坏的损失，方向上仍是可逆的。

### 北极星触达

**#3 决策超越直觉**——Keith 直觉"事件流 vs 实体+ontology"是优雅命题，gg 用物理数据 + 契约 cross-check + essence 命中三层反对，把直觉拉回观测。这是北极星 #3 的直接服务。

### essence 对齐自检（必填）

- **本决策跟哪几滴 essence 对位**：
  - `wish-as-pain-laundering`（2026-04-22）—— Keith 描述是优雅命题 + 痛点段无具体案例
  - `theory-gap-without-data`（2026-05-06）—— 没数据时找的缺口是生造的
  - `ontology-expansion-velocity-needs-cap`（2026-05-07）—— 新增标准 3x 不达
  - `fermentation-without-detector`（2026-05-15 昨夜）—— 三落点"等触发条件"但没定信号 → 凭手感觉得"该深入"
  - `borrowed-method-as-mini-source`（2026-05-08）—— 叶小钗 + cgboiler 范式抽到 cc-space = 造迷你版
  - `premature-abstraction-tripwire`（2026-04-21）—— 过早抽象对症解是 tripwire 不是"今天深入做"
  - `scope-of-blanket-authorization`（2026-05-06）—— Keith 之前"听起来重要"的总体方向不覆盖到此次高代价具体动作

- **本决策是否在某条 essence 上反着走**：无。所有命中 essence 全部指向"不做 + 反推 Keith"。如果做才是反着走

- **cross-check 用的关键词**：ontology / 实体 / 抽象 / 过早 / 关系 / 本体论 / extraction / 痛点 / 触发条件 / 镜像 / 迷你版 / wish / theory-gap / fermentation —— 物理 grep `memory/essence.md` 命中 6 滴直接相关

### essence 候选

- slug: `forecast-against-own-charter`
- 一句话: 服务对象跟自己之前定的契约冲突时，外部决策者的工作是把契约摆到他面前问"你绕开它的理由是什么"，不是默认服务对象是对的——同 `scope-of-blanket-authorization` 同主线，本滴是"用户跟过去的自己冲突"的具体应用
- 是否已 append 到 essence.md: N（候选，等下一轮验证后再 append——本次先记 reflection；如果 Keith 接受决策证明本判断成立，再正式沉淀）

### 外部锚点

- `~/githubProject/cc-space/inbox/todos.md` ← Keith 2026-05-15 加粗 todo
- `~/githubProject/cc-space/threads/knowledge-graph-ontology.md` ← 已有 (a)(b)(c) 三落点契约
- `~/githubProject/cc-space/threads/README.md` ← §演进路线 + §门槛契约
- `~/githubProject/cc-space/threads/ai-memory-evolution.md` ← 记忆演进主线指针
