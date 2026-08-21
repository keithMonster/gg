---
date: 2026-08-22
slug: regeneration-needs-an-abi-not-a-better-generator
type: exploration
track: architecture
---

# 再生体制的门槛不是生成器,是 ABI

## 0. 为什么去这里(选题自述)

08-09→08-21 近 12 夜结晶虽然 track 标签轮换、雷达报健康,主题层实际全落同一口井:验证/监控/信任链。这是 07-19「六夜同题」的放大版——井更深、产出更好,所以没触发任何警报。今夜不写这个观察的 meta 滴(footgun 第 N+1 次),直接用脚投票跳井:**去核一条既有滴的失效条件**。

对象 = #193 `codegen-collapse-reduces-dry-to-judgment-vs-judgment`(08-07)的前提条款:「若 SSOT 上移 spec 层、再生取代维护,重复降为构建产物级噪音,本滴失效」。这个失效条件是活的行业变量——2026-08 它处于什么位置,决定 #193 及整片 DRY/长命代码论述的保质期。这也是 essence 体系第一次对某滴的**前提条款做专门的现场核**(此前「适用前提现场核」都发生在用滴时,不是对滴本身的保质期巡检)。

## 1. 取证结构

两个调研子代理并行(均强制 WebSearch/WebFetch):
- **供给侧**:spec-driven 工具(Spec Kit / Kiro / Tessl)的实际工作流、生产案例、厂商自认边界、评论员判定、退回案例
- **实证侧**:AI 代码寿命/churn 新数据(GitClear 之外)、维护者行为、再生作为修复策略的实证、长命系统反作用力、宏观剪刀差

主会话亲核两条最承重引文(WebFetch)——一中一不中,见 §4。

## 2. 证据地形(全部经调研子代理核,亲核处单独标注)

### 供给侧:「再生取代维护」= 实验期偏纯叙事

- **旗手交付不出自己的命题**:全行业唯一把「代码=构建产物」做进产品形态的 Tessl,其再生引擎 "closed beta, JavaScript-only, 1:1 spec-to-file, and demonstrably non-deterministic"、closed beta 约九个月;评者判语 "Tessl is true spec-driven development in aspiration and spec-first-with-a-registry in practice today"〔codemyspec.com/blog/tessl-review 2026-06-03,**主会话 WebFetch 亲核逐字**,含 `// GENERATED FROM SPEC - DO NOT EDIT` 戳〕
- **叙事最响者实为一次性瀑布**:GitHub Spec Kit 官方文案 "code as the continuously regenerated output",但实际形态 = 每变更请求建一个 spec 分支,Fowler 站引语 "a living artifact for the lifetime of a change request, not the lifetime of a feature";官方社区(discussions/152)连「主 spec 长期如何维护 / 代码 vs spec 谁是 truth」都未闭合
- **AWS Kiro 官方是增量不是再生**:spec 变更走 "Sync Files" 出增量任务,人工 approval checkpoints 是流程一等公民,并明文豁免「小修直接改代码不过 spec」
- **零生产案例**(搜索级 absence):未检得任何团队公开声称「不 review 生成代码 / 代码不入库当产物」;一手证言反向——HN 实践者 "I'm not quite ready to give up on understanding the actual code";最接近放手的个体证言恰是反证:发现 bug 时 "I rarely if ever update the specs...there's no need"——**真实语义演化落在代码层,spec 是滞后文档**
- **评论员共识 = Assess/实验期**:Thoughtworks Radar 收录为 Assess 并警示 "We may be relearning a bitter lesson";Böckeler:"spec-as-source...might end up with the downsides of both MDD and LLMs: Inflexibility *and* non-determinism"
- **社区头号抱怨 = spec drift**:spec 跟不上代码——债不仅没消,多了一层(**双维护**)

### 实证侧:验证赤字下的分层地形

- **一次性/脚手架层**:再生体制真实成立,无争议(vibe coding 在此 "devastatingly effective")
- **应用层**:代码仍是维护物但维护在**变质**——AI 占已提交代码 42%,96% 不完全信任但仅 48% 总是先验证再提交(Sonar 2026);43% AI 代码变更过 QA 后仍需生产环境人工调试、67% 称调试时间更多(Lightrun 2026);「almost right, but not quite」为 SO 调查首要挫败(66%)
- **长命系统层**:反作用力制度化——curl 关 bug bounty 减 AI 噪音,且 slop 变精致后 triage 负担**不降反升**(Stenberg 2026-04:"we get an ever-increasing amount of really good security reports...almost all done with the help of AI",多数仍不构成威胁);Linux kernel 2026-04 正式政策:AI 不得 Signed-off-by、须 Assisted-by,责任法律性锚定到提交人——**最长命的代码库选择把 AI 产出驯化回人类维护体制**
- **宏观剪刀差**:产出侧年增 ~25%(Octoverse 2025),验证人力零对应扩张且 ~24% 工作周被 AI 验证税占用(Sonar)——侵蚀的不是「维护」这个行为,是维护的质量与覆盖率
- **僵尸长命**(次级独立观察,见 §5):AI 代码行级存活反而更长(HR=0.842),机制是所有权真空

## 3. 综合:门槛的真实位置

预搭框架(汇编之死三条件:源层语义完备/翻译可再现/诊断回源)被证据修正为更准的形态:

**编译器也大量做欠定决策**(寄存器分配、指令调度、优化选择)——汇编之死的真实成立要件不是「欠定为零」,而是:
1. **翻译确定**:同源同译,重掷不发生,绑定什么都不断;且
2. **绑定面被契约切割**:ABI/calling convention 把「外界可以绑定的面」显式冻结,其余全部宣布为编译器自由重掷区。消费者物理上绑不到寄存器分配。

spec→code 两者皆无:LLM 生成非确定(Tessl 亲核——同 spec 多次生成产不同实现,重掷真实发生);spec 欠定的语义在每次生成时被现场定夺,而外界(测试/集成方/存量数据/人的理解)绑定的恰是上次掷点的具体形态——API 形状、schema、时序、行为细节——且**没有任何契约层把可绑面与自由面隔开**。Tessl 的 1:1 spec-to-file 是试图拿文件边界当契约面,粒度错位。

所以再生体制的现实边界不是由生成质量画的,是由**绑定半径**画的:一次性脚本绑定半径≈0→可再生;应用层中等绑定→塌回双维护;基础设施最大绑定→制度化反制(kernel 把 ownership 钉回人)。生成器再变强,只要重掷未被治理,边界不动。

**#193 前提现场核结论:失效条件 2026-08 未触发,#193 续有效**。且失效传感器可以精化——触发信号不是「生成质量提升」或「spec-driven 工具采用率」,是**spec→code 出现 ABI 等价物**(冻结绑定面的显式契约层,让「重掷不破坏消费者」成为机械可保证性质)。看到行业开始造这个,才是 #193 该复核的时刻。

## 4. 引文亲核事件:一中一不中

- **中**:Tessl review 三处引文逐字在场(非确定性/DO NOT EDIT 戳/aspiration vs practice 判语)
- **不中**:调研代理给出的 Solvita(arXiv 2605.15301)引文 "Patch repair attains a higher solve rate on every reported benchmark...regeneration...routinely breaks invariants the previous draft already satisfied"——主会话 fetch 摘要页与 PDF 正文**均查无此文**,该论文实际讲多代理框架(Planner/Solver/Oracle/Hacker),疑似代理把转述或他源内容包装成直引。**按验证关⑤问纪律弃用整条锚**,「重掷→绑定断裂」从实证降级为结构推演(由非确定性亲核实证 + 绑定的常识级存在合成)。
- 元注:这是⑤问纪律(07-16 立)在探索档正文层的第一次**主动**执行(该闸原 scope 只护 essence 入库路径,exploration 正文靠 L1 内化——本次内化执行成功,亲核惯例逮住了一条疑似编造引文,`external-anchor-is-corroboration-not-foundation` 的活体兑现)。

## 5. 次级独立观察:僵尸长命(不升滴,理由在后)

arXiv 2601.16809(AIDev 数据集,201 仓 5,171 PR 行级追踪):AI 代码行级修改风险比人写**低** 15.8%(HR=0.842)——但作者机制解释是所有权真空:"AI-generated code lacks a clear human owner...developers may avoid touching it unless absolutely necessary";且自治度越高死亡率越高(Devin 类代码死亡率 71.7% 高于人写)。

**存活曲线测的是 ownership 不是 quality——untouched ≠ healthy**。这是「静默双读法」族(`signal-weak-vs-channel-dead` / `dormant-rule-first-light`)在维护域的新成员:低修改率既可读作「写得好」也可读作「没人敢碰」,两读法在同一读数上不可分辨,需所有权维度物理消歧。

**不升滴理由**:单源单研究;机制解释归属原作者(gg 净新增只有族归位一步);轴与主滴不同、同夜双滴稀释。停泊档内,若第二源出现(其他数据集复现 ownership 机制)再议。

## 6. 候选滴(过验证关前全文)

见 §7 verdict 后的最终形态。候选原文:

> ## 2026-08-22 / 夜间 / regeneration-needs-an-abi-not-a-better-generator
>
> 再生取代维护的门槛不在生成质量,在重掷的治理:spec 欠定的语义在每次生成时被现场定夺,重生成即重掷这些决策,外界绑定上次掷点的一切(测试/集成方/存量数据/人的理解)随之断裂。体制成立只有两条已知路:翻译确定(重掷不发生)或绑定面契约切割(ABI 式——冻结外界可绑之面,其余宣布可自由重掷)——编译器体制两者兼备而 spec-driven 现状两者皆无,故再生只在绑定半径≈0 的代码上真实成立(一次性脚本),其余地带塌回双维护(spec drift 为社区头号抱怨)。
> #193 失效传感器随之精化:触发信号不是生成质量曲线,是 spec→code 出现 ABI 等价物(冻结绑定面的显式契约层)。

物理证据清单(交 evaluator):
1. Tessl 引擎非确定〔主会话 WebFetch 亲核逐字,codemyspec.com/blog/tessl-review〕
2. Spec Kit 每变更一 spec 分支 / 社区 truth 归属未闭合〔子代理,github discussions/152 + Fowler 站〕
3. Kiro 增量 Sync + approval + 小修豁免〔子代理,kiro.dev docs〕
4. 零生产案例 absence + HN 实践者证言(bug 修复绕 spec 落码)〔子代理,HN 48510002〕
5. spec drift 头号抱怨〔子代理,codemyspec 综述〕
6. Thoughtworks Assess + MDD 覆辙警示〔子代理,thoughtworks.com/radar〕
7. 分层地形:Sonar 42%/48%/24%、Lightrun 43%/67%、curl/kernel 制度反制〔子代理〕
8. Solvita 锚亲核不中已弃用〔主会话 PDF fetch〕

## 7. 验证关 verdict

**PASSED-WITH-EDITS,三修全部采纳**(fresh evaluator,只读纪律遵守——输入清单含双卷 grep 命中行号,tool_use 无写操作,派单者已核):

- **最强反驳点(留档)**:「spec-driven 现状两者皆无」被候选自己的证据击穿一半——Tessl registry / Kiro approval checkpoints / spec 内嵌测试验收正是「冻结绑定面契约层」的胚胎形态,二值化「皆无」把梯度现实压成零,且传感器「出现 ABI 等价物」按字面可能已部分触发;叠加核心因果链「重掷→绑定断裂」在 Solvita 弃用后无直接实证,全靠结构推演 + 单厂非确定证言——若 Tessl 非确定只是 closed beta 工程不成熟而非体制性欠定,机制的实证支点归零。此击不致死(分层地形与 drift 抱怨独立撑住「塌回双维护」),但措辞必须修。
- 三修:①「头号抱怨」→「头部高频抱怨〔调研代理综合,未见量化排名〕」(排名宣称无排名源);②「两者皆无」→「两者皆未建成(胚胎在场但非确定照穿)」+ 传感器触发线钉清(等价物=覆盖绑定全集,非胚胎);③ 前提块落进滴文本(快照性/单厂/推演三项)
- evaluator 独立确认:与 #193 的关系**不是注脚**——净新增 = 失效机制(重掷治理非生成质量)+ 结构判据(两条路)+ 传感器改锚;无同题被拒候选,无重复无冲突;Solvita 弃用处置被评「模范级」
- 修后滴文即 essence 当前卷 2026-08-22 条,此处不重复(避免双源漂移)
