---
date: 2026-08-27
slug: problem-terminator-gate-ruling
summoner: monster 主会话（Keith「问题终结者」诉求 → 是否建全局 Stop hook 第四道闸）
northstar_reach: "#3 决策超越直觉（否决直觉解「加闸」，给出付费时点反转）"
status: substantive-decision
---

# Reflection: problem-terminator 第四道闸裁决

### 给父会话的最终输出（必填）

**推荐：不建 `problem-terminator.py`。四档清单问卷是 attestation 型闸（回答全由被拦的同一 LLM 供给，无外部重算侧），退化成「不适用×4」盖章是类型必然不是可缓解风险——风险本身就是形态选错的证明。**

理由链：
1. **闸型误配**：已有三道闸是检测器（核验已产出断言有无物理指针）；本方案是问卷（强制产出新文本）。tripwire 只能统计「答了没答」，答案质量语义不可机械判（essence `mechanical-gate-needs-machine-detectable-target` 06-24 + `attestation-has-no-fixed-point-under-self-audit` 08-20）。「每档必须给理由」= 输入端修补，LLM 生成四条理由成本≈0，零成本绕过。
2. **归因（更正后）**：分仓不同层。22 个有 test 入口的仓（含 cg-weilu，606 个真实测试文件）——修完不补 regression 是 **L3b 召回失效**，对症是**注入器**（无 block、无问卷），方案却是拦截器形态装 L3b 的心，亚型配错（monster 工程原则 #5 的「次高频误判」原型）。41 个无入口仓是 L4，注入提醒恒失效；但 L4 出口在**模板层**——cg-platform-template 自带 test，增量应用天生有落点，存量仓不逐个补、按「第二次付费」补（见 3）。
3. **付费时点反转（本次核心洞察）**：修完时写全称防复发卡 = 税付在 100% 的修复上，而只有少数会复发（`ghost-rules`：防从未发生的灾难是幽灵——父会话至今未提供一条实证复发案例，本身即欠定点）。支点应在**第二次遇到时认出「这修过」**：第一次只留免费痕迹（commit message 写清症状关键词，`mutation-self-records` ——变更免费留终态），第二次 `git log --grep` 命中 → **复发即事故**，此刻才升级 canon-bugs / regression test / 结构消除——税只付给被证实的复发。
4. **重复建设警报**：`cg-weilu-eng-loop.md` R5/R6（持续 review + 滚动清单）是同一条闭环，Keith 08-26 刚拍「先关闭」。以「问题终结者」名义另起全局机制 = 绕过昨天的暂停决定，须向 Keith 点明后再动。
5. **准入三问不过**：第②问「谁检验检验者」答不出——tripwire 验答题存在性不验真值。

行动建议（按杠杆排序）：
- **① 查 `cg-platform/ci_template` 是否跑 test job；没有就加**——单点改动辐射 63 仓、push 即跑、机器强制。若 CI 不消费测试，22 仓的 606 个测试也是死工件，regression test 写了白写。这是本轮最高杠杆一击，先于一切 hook。
- **② 全局 Rules #8 调试五步法加第六步**：「防复发：给出落点（结构消除 > 机器检查 > 一句话规则进 AGENTS.md）或明说不值得」。prompt 层跑步机，会衰减，但代价≈0 且 Keith 现在有意识会盯。
- **③ 修 bug 的 commit message 纪律**：症状关键词进 message（免费账本）；排障动作补一步「先 `git log --grep` 症状」。
- **④（可选轻注入器）**：debug 信号词现场注入一行「本仓有 vitest（package.json 实判），修完补 regression」——只对 22 仓、只注入不拦截、无问卷。
- **⑤ 向 Keith 报备**：此诉求与 eng-loop R5/R6 同闭环，问是否算重启。

trade-off：否决闸后 L3b 无硬强制，②③靠自觉 + Keith 在场纠正，执行率上限有 28% 先例；接受此代价，因为硬强制在此闸型下买到的是仪式不是行为。未核验假设：ci_template 是否已含 test job（须实查）；22 仓测试的真实密度（模板继承 vs 主动建设）未逐仓验。

### 核心假设

复发是低频事件（无实证复发清单支撑高频假设）；commit message 可作免费检索账本（要求纪律真被执行）；attestation 判定适用于「LLM 自填清单被同会话 tripwire 统计」场景。

### 可能出错的地方

若真实复发率高且集中在 41 个无测试仓，「第二次付费」会让 Keith 多吃一次事故成本——他的原话「不要出现第二次」字面上不接受第二次发生。此处我用「第二次 = 检测时刻」重释了他的目标，若他坚持字面（一次都不能再有），则唯一诚实答案是全称预防不可达、只能收窄到高危仓补 regression。

### 本次哪里思考得不够

未实查 ci_template 内容就把①列为最高杠杆（依据是父会话简报的 CI 描述）；对三道既有闸的真实拦截频率/疲劳数据零读数，「拦截疲劳」论证是结构推演非实测。

### 如果 N 个月后证明决策错了，最可能的根因

低估了「意识」的机制化需求——Keith 要的可能就是一个哪怕仪式化的强制动作来改变默认（仪式也有锚定价值），而我按纯有效性否决了它。

### 北极星触达

#3：Keith 直觉解是「加一道闸」，裁决给出付费时点反转 + 模板层单点杠杆，超越了「加规则」直觉。

### essence 对齐自检（必填）

- **对位滴**：`attestation-has-no-fixed-point-under-self-audit`（08-20，问卷闸无不动点的直接应用）、`mechanical-gate-needs-machine-detectable-target`（06-24，语义质量不可 L3 判）、`rule-layer-flywheel`（CI test job = 事件层飞轮）、`ghost-rules`（零实证复发史建全局闸）、`mutation-self-records-consultation-must-buy-its-trace`（commit 免费账本 + 读通道须外建）、`omission-failures-evade-event-driven-sensors`（「没补 regression」是缺席型，Stop 采样确实是其代理事件——见反走）。
- **反着走的**：`omission-failures` 滴支持「用 Stop 时刻做缺席的代理采样」，父会话方案正是这个结构——我否决它靠的是判定轴（答案不可判真）压过触发轴（时机确实对）。潜在张力，已展开：触发对 + 判定空 = 只能产出仪式。
- **候选滴（candidate-unverified，不入库，待夜巡/设计模式补审）**：`recurrence-defense-pays-on-second-occurrence` — 防复发的税按第二次付费：第一次修复只留免费可检索痕迹（commit/账本），复发被第二次现场证实才升级为事故与结构消除；全称预防在修完时点写卡 = 把税付给 100% 的修复去防少数复发，是 `ghost-rules` 在防复发工程域的推广。物理证据：本轮零实证复发案例 + 63 仓 22/41 测试基建分布 + cg-platform-template 增量自带骨架。相关既有滴：`ghost-rules` / `failure-response-is-priced-by-expected-reliability` / `mutation-self-records-consultation-must-buy-its-trace`。
- **对齐度**：高（否决方案的每一步都有滴承重；一处反走已显式结算）。
