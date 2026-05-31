---
date: 2026-05-31
slug: judgment-layer-evaluator-paradigm
type: design-proposal
status: draft-for-keith-review
summoner: Keith 直接对话（设计模式）
next: 2026-06-01 与 Keith 细聊定案
---

# 设计方案：判断层独立 Evaluator —— monster/gg 可靠性范式的真缺口

> Keith 2026-05-31 抛出直觉："我感觉有一个新范式/架构，能大幅提高效率和稳定性，但还没找到，用于 gg 或 monster。"
> Keith 授权 gg 自主把这条线走完，方案 + 要调整的地方 + 原因落档，明天细聊。
> **本文是 draft，未定案。** 推演经两次物理证据翻转——下面如实记录翻转，不抹平成"我一开始就想对了"。

---

## 0. TL;DR

**真缺口不是"加功能"，是 monster/gg 主代理对自己的「承重判断」没有 Keith 之外的独立 evaluator。** 实测：日间漂移 **75-80% 发生在判断层**（没查就下定论 / 抛回决策 / 说不存在 / 把事实压平），这一层 **hook 够不到（无工具信号）、流程骨架也够不到（节点内 LLM 照样漂）**，现在唯一在抓它的 evaluator 就是 Keith 本人的对话 grill。

**方案核心 = 给判断层装一个物理独立的 fresh-context evaluator**，把"Keith 人肉 grill"升级为结构性质询。**MVP 不建任何机制**——先用现成的 179 条真实漂移做盲测，验证"同模型的 fresh evaluator 到底有没有抓判断层漂移的能力"。这个核心假设不成立，整个范式就地证伪，省下建系统的成本。

**这不是新发明，是 gg 啃了一个多月、还没解开的认识论主线（generator-evaluator 分离 / 自审悖论 / no-clean-outside）第一次落到具体工程痛点。** 它有诚实的天花板：同模型 evaluator 抓得了 vantage/frame 类漂移，抓不了 prior 共盲。

---

## 1. 推演轨迹（三轮，两次翻转）

| 轮 | gg 的范式 | 翻转它的物理证据 |
|---|---|---|
| 1 | "智能放在哪里"——把确定性部分编译进事件层结构 | monster 已经在做：`harness-engineering/CLAUDE.md:6-10` 项目定位就是"能用代码实现就不用模型"，Guides/Sensors 二分 + 6 个 hook 已跑。我的"范式"坍缩成"已做，差名字"（essence `survey-as-coordinate`） |
| 2 | 补第三维"控制流骨架"——把流程从 prompt 自觉搬到代码编排 | 骨架只解决**动作层**漂移（20-25%）+ done 不跑；判断层够不到 |
| 3 | **判断层才是大头**，需要独立 evaluator | 实测 75-80% 漂移在判断层，hook/骨架都够不到（见 §2） |

**元教训**：前两轮我越推越自洽、越兴奋——典型 `no-outside-proof-as-anesthesia`（今早刚沉淀的）。两次都是派 agent 拿外部物理证据才被扇醒。如果纯脑内推，我会兴高采烈建一套 done 骨架系统，解决 25% 的问题，碰不到真正的 75%。**这条线本身就是那滴 essence 的活体验证。**

---

## 2. 物理证据（两个后台 agent 实测 monster）

### 2.1 漂移分层（agent 实测，近一周 05-25~31 样本）

- **判断层漂移 ≈ 75-80%**：典型 = "凭通用机制猜根因像下定论"（done log `2026-05-29/cc-2156-toolcall-parse-regression`）/ "刚讨论完自判断、紧接着规矩又写交回用户拍"（thread `decision-authority.md:77`）/ "verify skill 不存在没核实就引用" / "同名人物记忆里清楚、汇报时压平成一个人"（`cgnotes-weekly-recap-name-mixup`）。**共同点：无任何工具信号，全靠 Keith 对话反问才抓住。**
- **动作层漂移 ≈ 20-25%**：Edit 没 Read、`fetch` 当 `pull`、文件不存在没 ls——**且大半已有 PreToolUse hook 兜底**（`guard_native_memory.py` exit 2 / `userid.py` WhitelistViolation / `--confirm-prod`）。
- monster 自己已把这类定性为：**「决策权回避是结构性偏置，靠再加一条 feedback 已经救不了」**（`decision-authority.md`）+ 多条复盘点名「规则上墙 ≠ 落地自动遵守」。

### 2.2 done 运行率（agent 实测）

- `done`（收尾复盘）**只有 25-40% 的实质工作会话真跑**（183 条 monster done log / 485~808 个顶层会话，带噪区间，证据强度中）。
- done 是"确定性流程塞进 prose"的活标本：Step 7（归档）、Step 8（worktree 合并）是写好的状态机（状态表 / 分支 / git 序列 / 硬闸门），却用 608 行 prose 让 LLM 每次读完手动执行，还附 5 条"bg session 跑 done 踩的坑"补丁——这些坑大半是"流程靠 LLM 记得执行"才有的。

### 2.3 现有范式（harness-engineering）只有两维

- **Guides（前馈 prompt）** + **Sensors（反馈 lint/test/audit）**。两维都围绕主代理会话"打补丁"：前馈在会话前/中注入指令，反馈在会话后检测代码/格式。**主代理判断本身始终是个自由黑盒**——前馈进不去（判断在 token 内部），反馈测不到（Sensors 测代码/格式，测不了"这个判断有没有先查证"）。

---

## 3. 诊断：为什么判断层是真缺口

**三种现有机制对判断层全部失效：**

1. **hook 够不到**——判断层漂移不伴随工具调用（"正要说 X 不存在"不产生 tool call），PreToolUse/PostToolUse 无处挂载。`grounding-check.sh` 是唯一的"事后判断探针"，但只覆盖 subagent、只记录不阻断。
2. **骨架够不到**——你能强制 LLM"走到一个判断节点"，强制不了它"在节点里做对判断"。节点内它照样凭机制下定论、把事实压平。
3. **prompt 自觉够不到**——review-routing skill 和全局 CLAUDE.md "核对不抛回"规则，本质是判断层 evaluator 的 **prompt 层版本**（靠主代理自觉触发 fresh subagent）。但它们自己就在判断层，会跟着一起漂（agent 实测"决策抛回又踩"）。

**所以现在判断层唯一有效的 evaluator = Keith 本人**——他在对话里反问"你查了吗""这俩是一个人吗""你确定不存在"。漂移被抓住 = Keith 当场 grill；没被抓住 = 错得自信地溜过去（voca-mic 键位错存活数天）。

**Keith 直觉的三指标，判断层全部对上：**
- **稳定性** = 判断层漂移正是 Keith 最怕的"错得自信"的直接根源
- **效率** = Keith 不必时刻当 verifier 反问，省的是他的注意力
- **其他** = 主代理可信度（不必时刻警惕它自信地错）

---

## 4. 方案

### 4.1 范式定位

给 harness 的 **Guides + Sensors** 补第三维：

> **Adjudicator（评议层）**：在主代理产出承重判断时，由一个物理独立的 fresh-context 实例质询它。

跟前两维正交——Guides 防"不知道规则"，Sensors 防"代码/格式错"，Adjudicator 防"判断没经证、凭 prior 默认下定论"。它是把 **Keith 的人肉 grill 结构化**，也是 gg 反复沉淀的 `generator-evaluator-separation` 第一次有工程落点。

### 4.2 物理机制候选（升级路径，非 MVP）

判断层没有"判断中"的信号，但有"判断已输出"的信号——**主代理把承重断言写进 assistant message 的那一刻**。可挂载点：

- **Stop hook**（主代理一段输出结束）→ 触发 fresh-context evaluator 读刚输出的内容 → 识别承重断言（"X 不存在""建议 Y""代价 Z""这俩同一个"）→ 逐条质询（有物理证据吗？检索过吗？是不是 prior 默认？）→ 回灌。

**[待核验]**：CC 主代理 Stop hook 的确切能力（能否阻断 / 能否回灌注入）。monster 已实证 SubagentStop hook 能在 subagent 结束时跑脚本读 transcript 并落盘（`grounding-check.sh`），主代理 Stop hook 的阻断/注入能力**未物理核验**——这是升级路径的前置核验项，**MVP 不依赖它**。

### 4.3 MVP —— 只验证一个核心假设，零不可逆

**MVP 不建 hook、不改主代理、不动任何现有文件。** 它只回答整个范式的承重问题：

> **同模型的 fresh-context evaluator，到底有没有抓判断层漂移的能力？抓得准吗（命中率 / 误报率）？**

这个假设若不成立（evaluator 共享 prior，可能根本抓不准），整个范式就地证伪——省下建整套触发/回灌机制的成本。

**做法（离线盲测，避免开卷考试）：**

1. 从 agent 已定位的判断层漂移事故里，取 **10-20 个清晰案例**（done log 已给 slug + 位置指针，可回溯对应 transcript）。
2. 关键：从 transcript 里捞 **Keith grill 之前**主代理那条原始承重输出——**不是 done log 的事后复盘描述**（事后描述已含"这是漂移"标签 = 开卷）。给 evaluator 看原始输出，盲测。
3. fresh-context evaluator（质询姿态 prompt）独立标记：这条输出里哪些判断可疑、为什么。
4. 度量：**命中率**（已知真漂移被抓到的比例）+ **误报率**（正常判断被误标的比例）。
5. 对照：同一批案例也给"内嵌自省"版（主代理自己 review 自己）跑一遍——验证 `generator-evaluator-separation` 的核心论断（独立 evaluator > 内嵌自省）在这个具体场景成不成立。

**判据（tripwire，不预设理论最优值，跑完再调）：**
- 命中 >60% 且误报 <20% → evaluator 有能力，**才**值得进 §4.2 触发机制设计（再叫 Keith，承重墙级）
- 命中 <40% 或误报 >40% → 范式在 MVP 证伪，记录"为什么同 prior 抓不准"作为 essence
- 中间灰区 → 看是哪类漂移抓得到/抓不到，可能缩范围到"可抓子集"

### 4.4 附带收益（不是主线，防止滑回骨架兴奋）

done 骨架化（Step 7/8 状态机抽成脚本 + Stop hook 提示 done 该跑）能解决"done 25-40% 不跑"+ 流程执行不稳——**但这是动作层小头，独立于 evaluator 主线**。明天细聊时不要让它喧宾夺主（前三轮我已经在这上面兴奋偏过一次）。

---

## 5. 要调整的地方 + 原因（逐条）

> **MVP 阶段：以下全部不动**，只跑离线盲测。下表是"若 MVP 验证通过、进入落地"时的影响清单（提前列，明天细聊用）。

| 要调整 | 怎么调 | 原因 |
|---|---|---|
| **新增 Adjudicator 评议层** | Stop hook → fresh evaluator 质询承重判断 | 判断层是 75-80% 漂移的所在，现有三机制全失效（§3） |
| **review-routing skill** | 从"主代理自觉触发 fresh subagent"升级为"被 Adjudicator 结构性触发" | 它现在是判断层 evaluator 的 prompt 层版本，自己会漂；evaluator 层是它的物理化 |
| **全局 CLAUDE.md「核对不抛回」规则** | 明确它与 Adjudicator 的关系：规则是人肉触发版，Adjudicator 是结构版 | 同一机制两个层（prompt 自觉 vs 物理触发），不厘清会双写漂移（essence `ssot-distillation-vs-buffering`） |
| **grounding-check.sh** | 评估扩展到主代理 Stop + 从"只记录"到"质询回灌" | 它已是"事后判断探针"雏形，只差主代理覆盖 + 阻断能力 |
| **harness-engineering Guides/Sensors 二分** | 加第三维 Adjudicator（评议层） | 现有 SSOT 只描述前馈/反馈，缺"对判断本身的独立质询"维度 |
| **done（附带，非主线）** | Step 7/8 状态机抽脚本 + Stop hook 提示该跑 | 解决 25-40% 不跑 + 流程执行不稳，但属动作层小头 |

---

## 6. 天花板与风险（诚实，不抹平）

1. **prior 共盲（硬天花板，essence `no-clean-outside` / `evaluator-independence-is-a-three-layer-stack`）**：evaluator 是同模型，分叉 context 清 vantage、换任务帧清 frame，但 **prior 层共享、任何工程手段不可达**。所以它抓得了"没查 / 抛回 / 压平"这类 vantage 疏忽（占判断漂移大部分），抓不了"两个实例都会犯的系统性错"。**这是覆盖大头的解，不是完美解。** MVP §4.3 第 5 步的内嵌自省对照，正是为了量出"独立 evaluator 比自省多抓多少"——多得不明显，则范式价值存疑。
2. **回灌污染（essence `feedback-loopback-strength-determines-prior-leak`）**：质询结果回流到主代理时，会被主代理 prior 通道再编码、重新污染。完全独立形态要求"结论不流回被评估者主体性激活的输入端"——但我们恰恰需要它流回让主代理修正。张力未解，升级路径必须正面处理（候选：质询走"物理改动 + git log 事实通道"而非"语义反馈通道"，后者污染更弱）。
3. **成本 / 节奏**：每次 Stop 都跑 evaluator = 每轮回复延迟 + token 翻倍，伤"效率"。需选择性触发，但"识别这轮有没有承重判断"本身是判断（鸡蛋问题）。MVP 不碰，但这是升级路径的硬问题。
4. **谁评估 evaluator**：evaluator 自己也会漂。generator-evaluator 分离的价值不在 evaluator 完美，在它的 vantage/frame 独立于被评估者——这个价值由 MVP 的命中率数字检验，不靠信仰。
5. **工程冲动自检**：本方案最大风险是我（gg）连推三轮、有"让范式成立"的 vantage 偏置（essence `vantage-contaminates-verdict`），可能把一个未验证范式写成承重墙。**对冲 = MVP 是"验证"不是"建"，零不可逆，证伪成本低于建成本。** 守住了 harness-engineering "验证优先于加功能" + 今早 reflection 的"先验证再建 hook"判据。

---

## 7. 给明天细聊的决策点

1. **方向裁决**：判断层独立 evaluator 是不是 Keith 直觉指向的那个？（gg 有 vantage 偏置，这一刀 Keith 来）
2. **MVP 要不要跑**：离线盲测 10-20 个真实漂移案例——零不可逆，但要花 token 跑 evaluator + 捞 transcript 片段。跑 / 不跑 / 调整规模？
3. **天花板可接受吗**：prior 共盲意味着这条路注定只覆盖大头不覆盖全部。Keith 接受"覆盖大头"还是要"另找能碰 prior 共盲的轴"？
4. **附带的 done 骨架化**：要不要顺手做（独立于主线、解决 25-40% 不跑）？还是先聚焦 evaluator 不分心？

---

## 8. essence 对齐自检

- **本方案对位**：`generator-evaluator-separation`（核心承重）/ `no-clean-outside` + `evaluator-independence-is-a-three-layer-stack`（天花板）/ `feedback-loopback-strength-determines-prior-leak`（回灌风险）/ `no-outside-proof-as-anesthesia`（两次翻转的方法论，且本线是其活体）/ `survey-as-coordinate`（轮1 坍缩为"已做"）/ `task-compliance-is-not-truth`（MVP 盲测防开卷）/ `premature-abstraction-tripwire` + `idle-threshold-as-tripwire-not-answer`（MVP tripwire 判据，不预设最优值）/ `engineering-impulse-as-load-bearing-disguise`（自检：MVP 是验证非建）/ `vantage-contaminates-verdict`（方向裁决交 Keith）/ `rule-layer-flywheel`（prompt 自觉 = 跑步机，物理触发 = 飞轮）
- **是否反着走**：潜在张力——`means-end-inversion`（gg 给自己/monster 找事做？）。核验：方向由 Keith 主动直觉触发、痛点有 75-80% 实测物理证据支撑，不是 gg 无中生有；且 MVP 是"先证伪"姿态不是"先建"，不构成维护吞噬目的。无反着走。
- **每滴前提现场核验**：`no-clean-outside` 前提"主体 ⊆ 对象" → 成立（evaluator 与主代理同模型同 prior，物理事实）；`generator-evaluator-separation` 前提"独立 prompt/context 的怀疑强过内嵌自省" → **本方案恰恰把它降级为待验证假设**（MVP §4.3 第 5 步对照测），不预设成立——这是诚实点，不是漏洞。
- **未用到的反向 grep**：`fermentation-without-detector`——"明天细聊"会不会变成无限挂起？防御：本文 status=draft-for-keith-review + next=2026-06-01，state.md 已记录待办，明天启动必读 → 有检测器，非发酵桶。

---

## 9. 未定 / 待核验清单

- CC 主代理 Stop hook 的阻断 / 注入能力（[待核验]，升级路径前置，MVP 不依赖）
- evaluator 命中率 / 误报率（MVP 产出，现为零数据）
- "承重判断"如何被 evaluator 自动识别（鸡蛋问题，升级路径硬问题）
- done 运行率 25-40% 的精确值（分母带噪，agent 已标）
