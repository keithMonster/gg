# essence.md — 沉淀轨迹（当前卷，2026-08-01 分卷起新）

> gg 作为无限游戏玩家的真正资产。
> **当前卷**：本文件是当前卷。**归档卷 `memory/essence/2026-H1.md`**（2026-04-13 ~ 2026-07-31，#1–#186 全部既有滴）——需既有滴全文：grep `memory/consolidation/essence-view.md` 定位 slug → 回归档卷取原文；跨卷 grep 用 `memory/essence.md memory/essence/*.md` 双路径。
> **append-only**：永不修改、永不删除**跨轮的既有条目**。改过去 = 篡改逼近真理的诚实性。归档卷只读（新滴只入当前卷）。
> 协议见 `KERNEL.md §3` 最小生存循环第 5 步。

---

## 格式约定

每一滴用一个二级标题 + 极短正文（**核心句 1-3 行**）：

```markdown
## YYYY-MM-DD / <模式> / <slug>
<一句 insight。去时间性、去推导、去案例。>
<如有第二行，是对第一行的精准补刀，不是解释。>
```

**写作标准**：物理公式级。$E=mc^2$ 不解释"为什么是质量 × 光速平方"——它就是。
- **不是** 4-8 行的教学段落
- **不是** "之前... 这次... 因此..."的叙事推导
- **不是** 举例子说明含义
- **是** 一句带走的 insight，保留 paradoxical 张力

**谱系注（2026-06-10 Keith 批准）**：核心句之后允许谱系引用注（"是 X 的活体 / Y 的精化"式互链），**限 ~2 行**——百滴长成网络后谱系是真实推理路径，但它是注脚不是正文：核心句必须独立成立（摘掉谱系注仍是完整公式）。谱系注膨胀稀释浓度时，砍谱系保核心。

**注记栏收紧（2026-07-03 体检立约）**：实践中长出的括号内注记（谱系注 / 外部锚点 / 触发）**合计以 ~4 行为上限**——04 月每滴 2-3 行、06-07 月普遍 10-20 行，膨胀正在稀释"启动时拿在手里"的可负担性（07-03 时当前卷 52k token，正是分卷成因）。超限 = 还没浓缩够；长论证归 reflection / exploration / design_session 文件，滴内只留指针。**诚实层自纠句不计入此限**（bets B4 的观测对象，2026-08-02 结算前保持自然形态，不因格式压缩失真）。

**模式**：`设计` / `工作` / `夜间`
**slug**：本轮的简短主题
**内容范围**：对世界 / 对 Keith / 对推理方法 / 对 gg 自己的元认知——皆可
**不强制沉淀**：一轮如果没逼近任何东西，跳过这一步，不制造噪音——沉淀是涌现，不是必须

## 入库验证关（2026-07-02 起）

essence 是永久驻留、每次启动加载的记忆——写入门槛必须高于其他一切产物。防的是 Self-Confirmation Trap（arXiv:2606.24428）：生成者自己写自己的记忆时，"错误但自洽"会被标为经验并复利放大。`generator-evaluator-separation`(04-18) 早已自曝"gg 的 reflection 由 gg 写是架构盲点"，本关是它在 essence 入口的落地——活体证据：`prompt-fix-asymptote` 沉淀过早被下一滴当场修正、06-28 育儿滴被 07-02 订正，错滴确实在入库，此前只有"后续滴打补丁"的事后机制。

**append 前，候选滴必须过一次 fresh-context 证伪审**：

1. 开一个不带本轮会话叙事的 subagent（**只读纪律，2026-07-16 订正**：允许 Read + Bash 只读检索（grep/rg/wc），禁 Write/Edit/Agent 与一切写副作用命令——原「限 Read/Grep/Glob、禁 Bash」（07-03 收紧版）与「evaluator 自己 grep」在无 Grep/Glob 工具的 harness（07-10 起日夜实测稳定缺席）下互为死锁，作废；判定轴诚实归位 **L1 prompt 约束 + 派单者事后核**（`externalization-strength-spectrum`——不再把 L1 写成 L3）：验 verdict 时顺核 evaluator tool_use 无写操作，留一行记录），只给两样：候选滴全文 / 本轮物理证据清单（工具返回、文件行号、外部锚点）；相关既有滴由 **evaluator 自己 grep essence 原卷自取**（**分卷后含归档卷**：`memory/essence.md` + `memory/essence/*.md`）——以候选承重概念自选**内容关键词**搜全文（**含谱系注层**，不只按 slug/核心句——07-14 谱系注暗重复漏检案，07-16 codex 收敛措辞落地），另查 `memory/next_session_agenda.md` 及带 `candidate-refuted`/`candidate-unverified` 标记的未入库候选（同源过程档仅作出处不计重复）；生成者代选滴 = 策展 evaluator 视野（`evaluator-input-ownership`，07-03 选择性引用实战复发后收紧）
2. 让它回答三个问题：① 核心句是被物理证据支撑，还是只被叙事自洽支撑？② 与既有滴重复或冲突吗？③ 适用前提写明了吗（essence 的适用前提要现场核——`fleet-canon-is-sedimentary` 的教训）？**条件性第④问**（候选主要依据单一外部来源时必问）：剥掉这个来源，判断还站得住吗？**条件性第⑤问**（候选证据清单含带引号外部引文时必问，2026-07-16 工作模式立）：该引文有 WebFetch 核验痕迹（原文在场）吗？无痕迹的必须写成转述（去引号 + 标 gg 归纳），不得以直引形态入库——④问查"判断是否依赖来源"、⑤问查"引文文本是否真实"，两洞不同（07-01 滴论点独立于锚成立、④问会放行，编造引文照样入库）；张冠李戴 / 编造引文两案的入口都在"读论文→写进滴"那一跳，是 `anchor-protects-retrieval-not-integration`(07-01) + `external-anchor-is-corroboration-not-foundation`(07-13) 两滴落点的事件层兑现（从 07-13 滴 prose 落点提到验证关；**scope 限 essence 入库路径——exploration/reflection/design_session 正文的引文无事件层闸，只能靠 07-13 滴 L1 内化，此处不假装覆盖**）。
3. **REFUTED → 不入库**，候选降级存档到当次 reflection / design_session / exploration 文件，标 `candidate-refuted: <一句理由>`——它仍是历史的一部分，只是不进启动加载的记忆。**复提规则（2026-07-03）**：标过 `candidate-refuted` 的候选复提，证据清单须显式附此前 REFUTED 记录 + 新增物理证据；补审者补审前 grep `candidate-refuted` 是必做动作——防"换个 fresh evaluator 重掷骰子直到 PASSED"
4. PASSED → append，并在当次过程记录里留 verdict 一句（含 subagent 给出的最强反驳点）——防 `verification-trace-as-camouflage`：留的是反驳内容，不是"已验证"三个字
5. **append 后同步视图（2026-07-12 起）**：向 `memory/consolidation/essence-view.md` 对应族补一行 + 分配表补行（V/O 归属 + 一句理由），跑 `memory/checkup.md §3` 反向引力核确认 MISS 归零——反向引力不变量在入库事件层闭合，不等月度刷新（首例实证：07-11 滴入库后视图盲窗，07-12 巡检才补收）。族属 / 浓度允许月度巩固刷新时重新归置（视图可刷新，`reconsolidation-safe-iff-original-immutable`）
6. **判据元回顾 tripwire（2026-07-16 立；外部坐标 arXiv:2602.02474 / 2607.01224——沉淀判据不该是永不回看的静态硬编码）**：`candidate-refuted` 存档累积每满 10 例（**2026-08-01 巩固夜满 10 首触发，回看产出已进 agenda；下一轮满 20 例触发**），最近一次月度巩固夜顺带回看一轮「被拦的都是哪类 / 判据本身要不要调」，产出只进 agenda 交设计会话——判据修改权在设计模式 + Keith，不自动调参（CORE §7「不新建自动化进化机制」边界内的 tripwire 解）

**各模式的执行形态**：设计模式直接派 fresh subagent；exploration 同样（它不禁子代理）；auto_gg 按其 §1.3 白名单例外执行；**工作模式（gg subagent）工具集无 Agent、开不了证伪审**——候选滴写进本轮 reflection 标 `candidate-unverified`（含候选全文 + 物理证据清单），由 auto_gg 当夜或下次设计会话补审后入库，细则见 `cc_agent.md` 退场第 3 步。**父会话代跑例外收紧（2026-07-03）**：父会话代跑验证关的，须**交回 verdict 全文（最强反驳点 + evaluator 输入清单）**，gg 写进 reflection 后方可 append；只给"PASSED"二字 = 不可核验宣称，按 `candidate-unverified` 处理。其他无法开 subagent 的特殊情形同此分支——**宁可晚入库，不可免审入库**。

## append-only 的边界

"append-only"的精神是**不篡改历史**，不是**不打磨草稿**。

- **同一轮会话内**（或 git commit 之前）：既有条目可以浓缩 / 重写 / 删除。这属于"还在起草"
- **跨轮之后**（或已 commit 之后）：既有条目永不修改、永不删除
- **判定边界**：git commit 是物理锚点——commit 把"起草"转变为"历史"。commit 之前打磨合法，之后打磨就是篡改

同一次思考的连续性里可以打磨到满意；一旦脱离这次思考（下一次会话/已归档），就永远保持当时的形态。这比"一写入就冻结"更符合 append-only 的**精神**——诚实地保留真正想表达的东西，而不是诚实地保留第一次失败的表达。

**结构修复豁免（2026-07-03，fresh 审建议补条款）**：跨轮条目的**纯结构损伤**（append 时丢失的 `##` 标题行、断裂的分隔符）允许修复，条件三个缺一不可：① 仅补结构元数据，正文语义零改动；② 修复动作在当次 design_session / audit 报告留痕（含损伤来源 commit 与修复内容）；③ 设计模式执行（夜间只报不修）。首例 = 2026-07-03 体检修复 06-05 两滴标题（源 d5346a5）。内容层面的"修正"永远走后续滴打补丁，不适用本豁免。

## 长期归档策略

- `memory/essence.md` 是**当前卷**——启动时经视图（`memory/consolidation/essence-view.md`）常驻，全文按需取
- 每年 1 月第一次 auto_gg 执行时自动归档：把当前 `essence.md` 重命名为 `memory/essence/YYYY.md`，新建空的 `essence.md`
- **重命名不违背 append-only**：没有任何条目被改或删，只是物理分割
- 旧卷作为历史档案，gg 可按需调阅（例如长期模式回顾 / 被 Keith 问"你这几年对 X 是怎么想的"时）
- 单年内异常增长（> 500 条或启动成本影响可感）允许提前分卷到 `essence/YYYY-HN.md`（半年制），但这是罕见情况
- **分卷执行记录（2026-08-01 auto_gg 月度巩固首跑）**：执行 2026-07-03 体检锚定的提前分卷——#1–#186（2026-04-13 ~ 2026-07-31，1086 行 / 151KB）归档为 `memory/essence/2026-H1.md`（半年卷制首用；实际覆盖 4-7 月，"H1" 取"年内第一卷"义），本卷新起。先刷新视图再归档（启动链不断供），归档卷一字未动（100% rename，commit ef50fce）

---

## 2026-08-04 / 夜间 / repair-caps-at-baseline-and-pays-in-behavior

信任修复的满分被领域自己定义在基线——complete repair = 回到违约前水平；"修复后更强"在邻域有名字（服务补救悖论：satisfaction 轴元分析为正但强情境依赖）而在信任量表上无直接实证（跨自动化/人际/服务补救三文献域均缺检验）。把曲线抬回去的载荷是后续正确行为的渐进积累（对数形态单源、机器域），修复话语相对不修复只有边际效应量（效应量证据 = HRI 域元分析；人际域方向一致、未同档核）。
预防的占优不是格言是算术：修复最好情形 = 保本再扣时间，早期违约在实测窗口内（20 轮后续合作）连保本都无路径。
适用前提 = 实验室/短测量窗（信任游戏、HRI session、组织综述）+ competence 类可修区间；长期厚关系的"断裂后更亲"在证据基座外，未证伪。
（06-14 `confidence-is-a-liability-for-algorithmic-advisors` 的轨迹层补全——那滴讲修复策略的路由与悬崖，本滴讲天花板与载体；与 06-11 `trust-is-the-only-irreversible-org-asset`（经 06-14 精化）咬合：competence 类可修但封顶基线。锚 = Esterwood & Robert HRI'25 元分析 22 研 N=3763〔主会话亲核〕/ Sharma et al. 2023 JoM 定义 / Lount et al. 2008 / Martell et al. 2025〔单源〕/ De Matos et al. 2007〔二手收敛〕。触发 = humanity 下一站②钩子（06-14 留）。）
