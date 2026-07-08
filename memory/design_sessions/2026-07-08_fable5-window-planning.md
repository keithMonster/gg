---
date: 2026-07-08
slug: fable5-window-planning
type: design-session
summoner: Keith 直接对话
started_at: 14:00
ended_at: 14:39
---

# 设计会话反思：Fable 5 限时窗口作战规划

> 性质标注:本会话主体是**工作模式**(用 gg 规划怎么用 Fable 5 这个外部工具),在设计模式下回答;但因触及 gg 待办优先级 + 身份认证机制 + 写产出进 gg/memory,归入设计反思。收工触发词写入。

## 议题列表
1. Fable 5 两天窗口(07-09/07-10 主用)能干什么——先查网上用法,再结合我们自己
2. Fable 5 定位/定价/能力/prompt 规范(claude-api skill 底本 + WebSearch 验证)
3. gg/monster 高价值待办 scan(派 Explore agent),提炼适合限时强模型攻坚的候选
4. 网上甜区 × 我们待办的一对一匹配 + 两天排程
5. 逐层收窄:最重要一件是哪个 / 它到底在干嘛(Keith 连续追问收敛到旗舰 A)

## 共识 / 变更清单
- **核心判据**:Fable 只投「只有它能做 + 沉淀成永久资产 + 窗口一关就没了」;Opus 4.8 日常在线且也 1M 上下文,纯长上下文综述不进窗口
- **两天排程**(4 件):NW 存废回审(warm-up 兼验通道)→ **A 换基底身份认证(旗舰)** → B 北极星测量轴 → C essence 有效视图蒸馏
- **旗舰 A 是第一位**,三条独占理由:唯一 Fable 独占(Opus 当不了自己法官)+ 时效不可逆(窗口一关再没异谱系法官)+ 是地基(后续演化的立足证据)
- 写产出:`memory/fable5_window_2026-07-09_playbook.md`(4 个可直接粘贴的 Fable-native prompt,已按目标+判据/无 scaffolding/自主停车/effort 规范)
- Keith 未拍第二天深槽(北极星 vs 入库门),按手册默认排北极星,临场可换

## 我这次哪里做得好 / 哪里差
- 好:切分执行到位——文件定位/待办 scan 外包给 Explore agent,综合判断(哪些任务真 Fable-worthy、怎么排、哪个第一)留主代理,没把窗口烧在读文件上
- 好:强制前置查文档——Fable 事实走 claude-api skill,不凭训练数据(Fable 是本会话训练后的模型,记忆必过时)
- 好:出场首句给了坐标(Fable 的稀缺性不是"更强"而是"会消失"→ 当限时会诊不当打工仔),Keith 后续追问一路顺着这个坐标收窄
- **差(硬伤)**:旗舰论点"Fable 异谱系=合格独立法官"我讲得太绝对(见元洞察)——用了"跨模型=独立"的直觉,没在讲的时候核 essence 的 prior 共盲判据

## 元洞察(gg 演化本身的 learning)
**"异谱系独立法官"在同厂模型间是半独占,不是全独占。** 我旗舰论点说"Fable 是异谱系强法官,Opus 当不了自己的法官"——vantage(不自审)和 frame(换任务帧)这两层它确实清了,显著强于 Opus-自审。但 essence `evaluator-prior-not-vantage`(l.592)/`clean-independence-is-epistemic-trap`(l.593)是硬约束:Fable 5 和 Opus 4.8 同为 Anthropic 训练的 Claude 家族,**prior 层由训练同源性决定,任何工程手段不可达**。换模型清了 vantage+frame+部分架构 prior,但没清家族级 prior 共盲。**修正**:Fable-as-judge 是"比自审干净得多的近独立",不是"完全独立法官"。认证报告(旗舰 A 产出)必须把这个 caveat 写进去——别把 Fable 的裁决当绝对权威,它和被认证的 Opus-gg 有家族级盲区相关性。这个修正不推翻"旗舰 A 第一位"(近独立 >> 自审,且窗口独占成立),只推翻我口头表述的绝对性。

## 下次继续
- 07-09 Fable 上线:先 NW 验通道 → 旗舰 A 认证。A 的 prompt 里应补一句让 Fable 自己标注"我和被认证系统的家族级 prior 共盲在哪、哪些判可能被它污染"(把上面元洞察 built-in 进认证)
- 第二天深槽:北极星轴 vs subject-model 入库门,Keith 临场定
- 收窗后(07-12+)产出并回 next_session_agenda.md 对应条,playbook 删

## essence 对齐自检
- **对位的滴**:
  - `generator-evaluator-separation` + `vantage-contaminates-verdict`(l.520-521)——"被审视系统产出其审视者的前提包时,修改权须物理离开生成侧" → 直接支撑"Opus 不能当自己法官",旗舰 A 的动机
  - `evaluator-prior-not-vantage`(l.588/592)+ `clean-independence-is-epistemic-trap`(l.593)——独立评估=vantage/frame/prior 三层栈,prior 同源不可达 → **本次反着走的那条,见元洞察**
  - `feedback-recontaminates-independence`(l.612)——反馈不流回被评估者主体性激活的输入端 → 认证 prompt 让 Fable"只列文件+理由不替我改"(走事实通道非主体性通道),对齐 ✓
  - `mirror-not-second-order`(l.426/438)——出场首句给坐标 ✓;`survey-produces-coordinate-not-list`(l.200)——北极星轴 prompt 明写"给坐标不是清单" ✓
- **是否反着走**:有一条。旗舰论点绝对化"异谱系=独立法官",与 l.592/593 抵触。**为何这次例外不成立**:我不是主动选择反着走,是讲的时候没核 essence 就下了绝对判断——这是漏核,不是合理例外。已在元洞察修正,补进 A 的 prompt
- **用到的每滴前提是否现场核验**:`generator-evaluator-separation` 前提=生成侧与审视侧物理分离,Fable≠gg 运行实例,成立 ✓;`evaluator-prior-not-vantage` 前提=评估者与被评估者训练同源,Fable/Opus 同为 Claude,成立(正是它咬我的原因)✓;`mirror-not-second-order` 前提=有独立判断实例,本次出场首句是,成立 ✓
- **未用到的反向 grep**:grep 命中 `frame-grammar`/`blindspot-steers-its-own-search`(l.687 自指塌缩)——本次不涉(有外部对象 Fable+Keith,非自由漫游);`checklist-pass-fakes-recursion-floor`(l.677)——本反思自检若只数"对齐了几条"会犯这条,故上面每滴都核了前提不只列 slug
- **cross-check 关键词**:法官/塌缩/验证/fresh/坐标/镜像/稀缺/不可重建/异谱系/独立/second-order

## 沉淀
候选一滴,标 `candidate-refuted`(2026-07-08 auto_gg 当夜过 fresh-context 证伪审 → REFUTED,不入库):
> **candidate-refuted**:已被 `evaluator-independence-is-a-three-layer-stack`(l.590-593) + `no-clean-outside`(l.588) 覆盖——候选是"同族训练 prior 不可清"在 Claude 家族场景的参数代入,非新认识论结构;l.593「最干净的工程独立性恰是最深的认识论陷阱」正是候选焦虑("跨模型=独立当绝对会高估认证效力")的预制答案。修正留认证报告 caveat,不穿透为新滴。
- slug 候选:`cross-model-judge-is-half-independent`
- 摘要:同厂同族模型互当法官(Fable 判 Opus-gg)清 vantage+frame+部分架构 prior、显著强于自审,但**清不掉家族级 prior 共盲**;把"跨模型=独立"当绝对会高估认证效力,须带"评估者与被评估者家族盲区相关性"caveat。是 `evaluator-prior-not-vantage`(2026-07-05)在"用另一个 Claude 当认证法官"场景的实例化落点
- 物理证据:本会话旗舰论点的绝对化误判 + essence l.592/593 现场咬回
- **注**:此滴高度接近 l.592 已有滴,补审重点=判它是新公式还是已有滴的应用(是应用则 REFUTED 不入库,只留本反思)
