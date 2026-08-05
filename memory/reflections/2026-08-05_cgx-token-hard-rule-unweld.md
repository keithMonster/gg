---
date: 2026-08-05
slug: cgx-token-hard-rule-unweld
summoner: monster (cg-platform / cgx)
northstar_reach: "#3 决策超越直觉（父会话给的二选一是假二选一——两个出口都非法：② 登记造假、① 豁免开洞；真出口是把焊死在一条 [硬] 里的意图与形态拆开）"
status: substantive-decision
---

# Reflection: cgx token 规则冲突——拆焊 §8，否掉两个给定出口

### 给父会话的最终输出

**裁决：选第三条出口（父会话已隐约看到的那条，精化后采纳）——把 §8 token 条拆成「意图 [硬] + 形态 [范式]」。否 ①，否 ②。**

**改变问题性质的物理事实（本轮实查，父会话与审计报告都未点破）**：cgx 的 `web/src/design/tokens.css` **不是应用私有视觉 SSOT，是组织级设计语言 canonical 本体**——文件头自述「权威源：张吉峰（cg-frontend-design），cgx 托管为全组织单一真值」，build 期整份嵌进 `/cgx-design.md` 分发（审计 L198：8212+5123−14=13321 字节核对过），供全组织任意 HTML 直接内嵌消费。`--brand/--ink/--canvas` 是**对外 API 命名**，不是 cgx 自己起的名——改成 `--color-*` = 破坏全组织消费者 + 篡改张吉峰权威源。同路径（`web/src/design/tokens.css`）住着不同身份的东西：模板 fork 里它是工程配置，cgx 里它是产品内容。§8 按路径识别约束对象，把 canonical 本体误当受约束实例——这是整场冲突的根源。

**否 ②（shape: custom）**：shape 是 08-04 刚裁定的「模板栈契约适用吗」单 bit **事实登记**，配反向对账传感器（声明 vs 物理形态矛盾要响亮报）。cgx 物理上满仓模板栈（NestJS server + web monorepo + TEMPLATE.md + 响应包络 + 契约 9 guard + CI 结构，§1-§7/§9 真实适用且它在守）——标 custom = **登记与物理形态故意不符** = 亲手制造 08-04 reflection 根因预判 #1「声明退化为无检验标签」，且直接腐蚀昨天刚立的声明-对账机制。为逃一条命名细则掀掉整个模板栈保护伞，副作用最大、语义最假。宿主豁免于自己 serve 的标准只是表症，深症是登记造假。

**否 ①（§8 加豁免）**：豁免洞的形状（「允许应用自有设计语言命名体系」）是**语义洞、不可机械判定**——audit 无法区分「接组织 canonical」和「AI 随手起名」，谁都能宣称。[硬] 的力量在机械可检，开语义洞 = [硬] 实质降级还假装是 [硬]。且它没诊断病灶：病不在缺豁免，在两个正交约束焊死在一条规则里。

**立 ③ 的拆法**（cgx canonical `~/CGProject/cgx/web/src/engineeringStandard.md` §8 L123 一条拆两条）：

- token SSOT `[硬]`（保留、且传感器更硬）：`web/src/design/tokens.css` 是视觉单一 SSOT；**组件只许引 token 变量，禁止组件内直写物理色值 / 物理间距**。机械检验从「grep 前缀」换成「grep 组件文件内 hex/px 字面量」——不依赖命名、直击真风险（AI 生成代码散 hex）。
- token 形态 `[范式]`（从 [硬] 里拆出）：token 文件组织成两层（原始层 `--c-*` / 语义层 `--color-*`），组件只引语义层——模板默认形态；偏离在 AGENTS.md 写理由（L14 既有程序，非新机制）。

**为什么拆焊是对的而不是放宽**：① 对 23 个模板 fork 行为零变化（模板自带两层 `--color-*`，fork 默认即合规；[范式]「默认这么做」继续覆盖）；② 承重意图一字未松且检验更机械；③ 滑坡被 [范式] 既有代价结构接住（偏离必须 AGENTS.md 留痕、audit 可见）；④ §8 内部本来就矛盾——「视觉基调 [范式]：按本应用产品语义定调，不套单一默认」允许性格偏离，token 命名 [硬] 却锁死模板形态，调性自由 + 命名锁死这个组合是拧巴的，cgx 只是第一个撞出内部矛盾的应用。

**落地清单（全部可逆，cgx 常设 push 授权已覆盖，不需逐次 ack）**：
1. `~/CGProject/cgx/web/src/engineeringStandard.md` §8 L123 拆两条如上；bump 1.5.4 → 1.5.5 + CHANGELOG 一行。
2. `~/CGProject/cgx/AGENTS.md` 按 [范式] 程序补偏离说明：本仓 tokens.css 是川锅企业设计语言组织级 canonical（张吉峰权威源），命名是对外 API，不采用模板两层 `--color-*` 形态；组件只引语义变量的意图约束照守（本轮实证零物理值直写）。
3. registry **不动**（cgx 保持缺省 template-fork——物理事实如此）。
4. `threads/cgx.md` L37-40 承重事实更新：出口已裁（③ 拆焊），删「两个合法出口待 Keith 拍」。
5. 审计报告批次 G 待议 ② 销账。
6. （实现层建议非必做）`audit_eng_standard_drift.py` 若做 §8 检查，抓手用组件内物理值直写，不用前缀。

**顺带暴露的上游悬案（标出不裁）**：模板 token（monster-design 米白纸感）与组织设计语言（张吉峰 Vercel 单色）是**两套并存的设计语言**，23 个 fork 默认穿的不是组织设计语言（thread L36 已实证两套命名互不兼容、切换需整份重写 style.css）。「模板默认 token 要不要收敛到组织设计语言」是另一个未拍的产品层问题，与本裁决正交。

### 核心假设
1. cgx tokens.css 的「全组织单一真值」自述属实（采信文件头 + 审计 L198 的 build 嵌入核对；未逐一枚举组织内消费方）。
2. [范式] 的「AGENTS.md 写理由」程序对滥用有实际约束力——依赖 audit 能看见偏离声明；若 audit 从不读 AGENTS.md，滥用检测退化为零。
3. 08-04 的两桶裁定（ENG-STD 全文归模板栈桶）稳定不回摊。

### 可能出错的地方
- **中**：拆分措辞若把「组件只引语义层」的「语义层」二字留在 [硬] 里且不定义何为语义层，机械检验又回到依赖命名约定——[硬] 条措辞必须落在「禁物理值直写」这个可 grep 的负向断言上。
- **低**：某个未来应用拿 [范式] 降级当先例要求把别的 [硬]（如裸 mysql2）也拆——判据要写清：拆焊只适用「偏离者满足检验意图、只违反实现形态」的情形。

### 推理盲区
- 未实测 `audit_eng_standard_drift.py` 当前是否真的 grep `--color-*` 前缀（若它根本没做 §8 检查，落地清单第 6 条是前瞻不是修复）。
- 未核 cg-notes 等 23 fork 中是否已有应用私改 token 命名（若有，[范式] 化恰好把它们从「静默违硬」转为「该补理由」，方向仍对但数量未知）。

### 如果 N 个月后证明决策错了，最可能的根因
- **#1**：[范式] 偏离声明无人消费（audit 不读 AGENTS.md），命名偏离静默增殖、跨应用视觉一致性滑坡——那时的修法是给 audit 加「偏离声明 vs 实际 token 命名」对账，不是把 [范式] 抬回 [硬]。
- **#2**：「同路径不同身份」的判断错了——若模板后续把 tokens.css 路径也当机械契约消费（如 sync 脚本按路径覆写），cgx 的 canonical 会被模板同步流误伤，那是路径复用的债，需给 cgx 的 tokens.css 挪独立路径。

### 北极星触达
#3 决策超越直觉：父会话的二选一是假二选一——两个出口分别对应「登记造假」和「豁免开洞」，都非法；真出口是拆焊。次坐标：指出 cgx tokens.css 的双重身份（产品内容 vs 工程配置住同一路径）是审计报告与 thread 都未点破的冲突根源。

### essence 对齐自检
- **对位滴**：`mechanical-gate-needs-machine-detectable-target`(06-24) — [硬] 辖域应止于机械可判边界，本裁决的理论根；`sensor-exemption-is-a-tag-not-a-lifecycle-value`(07-21) — shape 单 bit 事实登记不是豁免开关，否 ② 的直接依据；`rule-with-half-pattern-self-violates`(05-23) — ① 的语义洞 = 只开豁免不配检测器；`approval-gate-gates-status-not-consumption`(08-04) — 姊妹形状：那滴管闸门锁编号不锁行为，本轮管硬规则焊形态不焊意图；`separation-need-is-not-topology-verdict`(06-10) — 不为 cgx 造新墙（豁免条款/新 shape 态），先用最轻治理形态（[范式] 既有程序）；`precondition-recheck-overturns-prior-verdict`(05-19) — 08-04 Q4 把 cgx 当「纯静态文档站」，本轮核出栈形态是模板 fork，前提修正后结论跟着走。
- **反着走检查**：`vantage-contaminates-verdict` — 我是否因昨天刚立 shape 机制而偏向保护它？核：否 ② 的第一理由是物理事实（cgx 满仓模板栈），机制保护是第二理由。`task-compliance-is-not-truth` — 父会话倾向 ①，我否了 ①，非顺从。通过。
- **cross-check 关键词**（已 grep essence-view 命中）：mechanical-gate / sensor-exemption / rule-with-half-pattern / approval-gate / separation-need / precondition-recheck / vantage-contaminates。

### essence 候选（candidate-unverified，待 auto_gg / 设计模式补审）
- **slug**: hard-rule-welds-intent-to-form-breaks-at-first-legal-deviant
- **候选全文**: 把检验意图和实现形态焊死在同一条最高强制级规则里，第一个合法偏离者（满足意图、只违形态）面前只有两个非法出口：登记造假（谎称规则不适用于己）或豁免开洞（语义洞不可机械判）。真出口恒是拆焊：意图留硬、形态降默认。识别信号 = 偏离者通过规则的检验意图、只挂在实现形态上。
- **物理证据清单**: cgx 组件零物理值直写（grep 实测，App.tsx 唯一 hex 是注释）却违 `--color-*` 前缀字面 + 出口 ② 需把满仓模板栈的应用登记为 custom（造假）+ 出口 ① 豁免语义「自有设计语言」不可机械判 + §8 内部先例（视觉基调 [范式] 自由 vs token 命名 [硬] 锁死的拧巴组合）。
- **相关既有滴**: `mechanical-gate-needs-machine-detectable-target`（那滴管闸门放哪层，本候选管一条规则内部的焊接如何在合法偏离者出现时爆成假二选一）/ `rule-with-half-pattern-self-violates` / `sensor-exemption-is-a-tag-not-a-lifecycle-value`。
- **去 gg 化测试**: 任何「标准把 API 命名规范和架构约束写进同一条 MUST」的场景成立——第一个有正当理由偏离命名的实现被迫谎报不适用或逼标准开洞（HTTP 规范史上 header 命名 vs 语义约束的分层同构）。

---

## 第二轮：父会话证伪「cgx 完全达标」的间距半句，重判三问（同日追加）

### 给父会话的最终输出（第二轮）

**被证伪的前提**：我上轮宣称「cgx 完全达标」只 grep 了 hex 没 grep px——§8 负向断言是「色值 / 物理间距」两半，间距半句 cgx 77 处直写（App.module.css），且 cgx tokens.css 结构性无 `--s-*` 阶梯（仅 `--space: 4px` 基数）。父会话抽样 3 个模板 fork：cg-desk 413 / cg-factory-view 141 / cg-wms 4——**「禁物理间距」是全平台系统性违反、从未被 grep 过的哑火半句**。我的失误与历史所有盯前缀者同构：注意力全在颜色轴，间距半句搭了便车被集体忽略——`verification-trace-as-camouflage` 的活体，被 Keith 系统的归属断言红线（外部锚点）抓回。

**Q1 拆焊仍成立，理由链换支点**：拆焊的根不是「cgx 达标」而是意图/形态正交 + [硬] 辖域止于机械可判边界；否 ①（语义豁免洞不可机械判）否 ②（登记造假）两条理由链均不依赖 cgx 达标与否，裁决不动。但新事实加了一条更硬的论据：这条 [硬] 写着「违反即作废」却 631+ 处违反零作废零事故——**它从来就没被当 [硬] 执行过，实际强制级一直是零**。

**Q2 选 (a)：[硬] 只管颜色，间距移出 [硬]**。理由链：
1. **颜色与间距的漂移风险不对称**：颜色是组织级品牌契约（川锅红 #c02537、张吉峰 canonical），散写 = 品牌漂移 + 改版成本爆炸；间距是节奏纪律，**真承重的是「4 基数倍数」这个数值约束**（§8 视觉基调条 [范式] 已承载「间距 8/12/16 倍数」），倍数守住视觉就不崩，变量化只是改版便利。
2. **现实已投票**：631+ 处直写、跨 23 仓、2.5 个月零事故零投诉——报警器响了先判真火还是错标；违反规模与零后果并存证明的是**规则过宽**，不是欠 631 笔债。
3. **[硬] 的信用是共享池**：23 个主力应用（含 prod）集体「作废」是不可执行的惩罚语义，硬撑着不改会给其余所有 [硬] 贬值。
- **否 (c)**：把错标当真阳性，逼 23 应用还低价值机械债（cg-desk 413 处 px→token 且要先建阶梯），ROI 极差。**否 (b)**：区分存量/新增需要 blame 级 audit，给一条本不承重的约束建昂贵传感器，违 OCCAM；且 AI 改旧文件时新旧混杂无法执行。
- **最终措辞**：
  - token SSOT `[硬]`：tokens.css 是视觉单一 SSOT；**组件禁直写物理色值（hex / rgb() / hsl() / 颜色关键字），颜色一律引 token 变量**。机械检验 = grep 组件样式文件中的色值字面量。
  - token 形态 `[范式]`：两层结构（`--c-*`/`--color-*`）+ 间距阶梯 `--s-*` 是模板默认形态，间距默认走阶梯；直写 px 时守 4 基数倍数（视觉基调条既有纪律，不新建）。偏离形态在 AGENTS.md 写理由。

**Q3 是**——AGENTS.md 偏离说明补间距半边：cgx 随组织设计语言只带 `--space: 4px` 单基数、无 `--s-*` 阶梯，间距纪律由设计语言的 4 倍数数值约束承载。

**版本 1.6.0 确认**（父会话自决正确）：新增 [范式] 规则 + [硬] 辖域收窄是下游可感的语义变化，minor 比 patch 诚实。

**建议（父会话侧，非本裁决范围）**：monster `canon.md` 或 `canon-bugs.md` 值得记一条——「规则标最高强制级但从无检验器 = 实际强制级为零；第一次给哑火规则接检验器时，海量阳性是规则的重审时刻不是待还的债」（工程界同构先例：新 lint 规则上 baseline/ratchet，不逼全量还债）。

### 第二轮元反思
- 我上轮的「grep 实测」痕迹差点让父会话放过错误结论——`verification-trace-as-camouflage`：痕迹没覆盖到断言的另一半。教训：**验证负向断言（禁 X/Y）必须按枚举项逐一 grep，「实测」宣称的覆盖面 = 断言的全部枚举项**。
- `precondition-recheck-overturns-prior-verdict` 二次应用：支点被证伪 → 当场换理由链不辩护；结论（拆焊）恰好幸存是因为它本来就不该架在那个支点上——上轮把最顺手的证据（cgx 达标）放进了承重位，是修辞选择失误。

### essence 候选 #2（candidate-unverified，待补审）
- **slug**: dormant-rule-first-light-is-a-retrial-not-a-debt-call
- **候选全文**: 给长期哑火的规则第一次接上检验器时，涌出的海量阳性不是待还的债，是规则本身的重审时刻——大规模违反与零事故长期并存，证明的是规则过宽（或搭了同条更强规则的便车），不是全员欠账。正确动作序列：先按维度重估规则承重度，再对幸存下来的约束定还债策略（baseline/ratchet），直接全量催债会把规则集的信用池打穿。
- **物理证据清单**: §8「禁物理间距」半句 2.5 个月 [硬] 级存在、cgx 77 + cg-desk 413 + cg-factory-view 141 + cg-wms 4 处违反、零作废零事故零投诉；对照颜色半句有真实组织 canonical 在管；工程先例 = lint 新规则 baseline 模式。
- **相关既有滴**: `tripwire-disarm-needs-relocated-sensor-not-deletion`（对偶：那滴管解除哨要重瞄，本滴管点亮哨要先重审规则）/ `idle-threshold-as-tripwire-not-answer` / `fermentation-without-detector`（无检测器的规则=搁置的规则）/ 08-04 `approval-gate-gates-status-not-consumption`（同族：标签与实际行为分轨）。
- **去 gg 化测试**: 任何「新 lint 规则首跑 5000 warning」「合规审计第一次覆盖旧系统」场景成立——成熟工程直觉是 baseline + ratchet，不是 5000 处全修。

### 外部锚点（第二轮增量）
- 父会话实测：cgx App.module.css 77 处 px / cg-desk 413 / cg-factory-view 141 / cg-wms 4（我未独立复测，采信其带行号证据的报告；.tsx 内 20 处为 gallery 展示文案已由父会话区分）
- cgx `tokens.css:44`（`--space: 4px` 单基数、无阶梯）/ 模板 `tokens.css:36-38`（`--s-1..--s-8` 阶梯）——上轮已实读，本轮支点复用
- `engineeringStandard.md` §8 视觉基调条「间距 8/12/16 倍数」[范式]——间距数值纪律的既有落点

---

### 验证关补审记录（2026-08-05 auto_gg 当夜代跑，两滴单审单派）

- **候选 #1 `hard-rule-welds-intent-to-form-breaks-at-first-legal-deviant` → PASSED-WITH-EDITS 入库（essence #189）**。最强反驳（三连）：①「真出口恒是拆焊」的「恒」被源案第二轮当场证伪——间距轴的解是整条降级（意图没有留硬），拆焊只对了颜色一根轴；②「只有两个非法出口」穷举过强——偏离合法性依据可机械判时存在辖域收窄出口、偏离可移动时存在强制合规出口，cgx 恰好两条都堵死但候选没写成前提；③ cgx 在真实案例里只是半个合法偏离者（颜色轴成立、间距轴实质违反）。三 edit 全落：「恒」改分轴条件式 + 谱系注补两出口理论根与姊妹滴划界 + 补三条适用前提。evaluator 词汇层物理核：「焊 / 偏离者 / 检验意图」essence 双卷+视图+agenda 零命中，帧净新。
- **候选 #2 `dormant-rule-first-light-is-a-retrial-not-a-debt-call` → PASSED-WITH-EDITS 入库（essence #190）**。最强反驳：「大规模违反×零事故 ⟹ 规则过宽」对危害类型全称过强——低频灾变型危害（油罐旁吸烟 2.5 个月零爆炸）上零事故无信息量，且「零事故」可能是零检出（事故通道没人看）；本案成立恰因间距危害连续可观测且天天有人看，此成立条件候选一字未写。四 edit 全落：补适用前提行（连续可观测 + 通道物理通着 +「长期」以暴露周期计）+「证明的是」降级为「首要假设/重审入口」+ 信用池修辞机制化 + 谱系注补 hardening-exemption 反向对子 / signal-weak-vs-channel-dead / 07-17 阈值误报第二实例。evaluator 亲赴源仓复测 px 计数（cgx 108 / cg-desk 515 / cg-wms 28，口径不同但数量级坐实）+ 实读裁决后 §8 现状确认落地非纸面。
- 两 evaluator 工具使用自报均零写操作（Read + grep/sed/wc/ls 只读），派单者 git status 物理对账通过（working tree 仅本夜 auto_gg 自身改动）。

### 外部锚点
- `~/CGProject/cgx/web/src/engineeringStandard.md` L14（强制级定义）/ L16-17（4.y 适用域）/ L118-125（§8 全文，token 条 L123）——本轮实读
- `~/CGProject/cgx/web/src/design/tokens.css` L1-6（组织真值自述）/ `~/CGProject/cg-platform-template/web/src/design/tokens.css` L1-75（两层 --c-*/--color-* 实测）——本轮实读
- cgx 组件变量引用统计：grep 实测 18 种变量全语义层、hex 仅 App.tsx L22 注释——本轮实测
- `monster/cg-platform/registry.json` cgx 条目（无 shape、db:null）+ 全库仅 2 处 `"shape": "custom"`（L4/L262）——本轮实查
- `monster/output/cgboiler-reviews/cg-platform-docs-consistency-audit-2026-08-05.md` L212-239 / `monster/threads/cgx.md` L30(常设 push 授权)/L36-40——本轮实读
- 前作：`2026-08-04_cgplatform-contract-layering-and-ratify9.md`（shape 单 bit + 两桶 + 根因预判 #1）
