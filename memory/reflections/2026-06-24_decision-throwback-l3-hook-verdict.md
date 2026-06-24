---
status: substantive-decision
slug: decision-throwback-l3-hook-verdict
date: 2026-06-24
mode: 工作
summoned_by: monster 主会话（Keith 点名）
task_family: skill-governance / architecture-review
tracks_touched: [cc, architecture, keith]
---

# decision-throwback 是否升 L3 机械 hook — 裁决

## 核心假设（可证伪）
1. decision-throwback 是**语义模式**不是字符特征——已被 monster 自己的数据证伪点反向印证：dd_verify_gate（孪生的 verify-throwback）粗筛真阳性仅 1.2%，基础率 ~0.3 次/天。同族行为机械粗筛已被实测否决过一次。
2. 已有 L3 先例（guard_native_memory / destructive-bash / userid 白名单）全是 path/调用闭包/字符可机械判定的硬边界——decision-throwback 与它们**异类**，前提（可机械判定）不成立。
3. 真正的检测点不在 PreToolUse（够不着纯文本抛回），只在 Stop（输出后）——而 Stop 上做语义判定 = spawn fresh LLM critic = prior 共盲 + 误杀合法上抛（三类 trigger）。

## 可能出错的地方
- 若 Keith 真实诉求是「不要再加文字规则了，我要的是别的形态」——那我的「第三条路=不升 hook、换工程锚点」可能仍被读成「又一条软规则」。我的第三条路必须是**事件层飞轮**（onboard 脚本内嵌门控），不是 prompt。这是关键分界。
- 误判 base rate：~10 次是 Keith 印象 + done 时间线条目，未做 transcript 实测。decision-authority.md 自己 2026-04-29 校准过一次（「300+」实测为 17 次主动授权、0 次事后纠正）。本议题的「10 次」也可能虚高——但即便虚高，结论不变（基础率低 = 更不该上 block hook）。

## 推理盲区
- 我没读 AskUserQuestion 在这套 harness 是否真有可 hook 的 PreToolUse 工具调用点。但这不影响裁决——即便有，在 AskUserQuestion 前注入反例仍是「软提醒搬到事件层」，治标不治本（抛回常以纯文本「你想 A 还是 B」出现，根本不调 AskUserQuestion）。
- subject-is-configuration：我是同源 LLM，判 monster 的 LLM 病灶 = prior 共盲。但本裁决的承重证据是 monster 侧的**物理数据**（dd_verify_gate 退役复盘 1.2% 真阳性），不是我的纯推理——锚到了工具返回。

## N 个月后根因预判
若误升了 block hook：3 个月内出现「合法上抛被误杀 → Keith 烦 → 关掉 hook」，复刻 dd_verify_gate v0→退役的同一条曲线。bug-shape-survives-fix 在治理机制层的活体。

## 北极星触达
- 二阶效应：识破「加机制」本身是 monster 的结构性冲动（engineering-impulse-as-load-bearing-disguise 的治理层复发）——比解决单个 decision-throwback 更重要的是不再用「加 hook」回应每个屡犯的软规则。
- 决策超越直觉：直觉是「屡压不住就升 L3」，物理数据反转为「同族已实测否决」。

## essence 对齐自检
- `engineering-impulse-as-load-bearing-disguise`（decision-authority.md 2026-05-28 候选）：本案「累积 10 次 → 该升 L3 hook」正是这条的治理层活体——grep decision-authority.md 确认存在。
- `cadence-as-symptom` / `theory-gap-without-data`：「屡压不住」的对症解不是加层，是先拿 base rate 数据。
- `rule-layer-flywheel`：prompt 层=跑步机，事件层=飞轮——第三条路若做必须落事件层（onboard 脚本内嵌），不是再写一条 CLAUDE.md。
- 新 essence 候选：`mechanical-gate-needs-machine-detectable-target`——L3 机械拦截的前提是目标行为可被非 LLM 物理量判定；语义模式不满足前提，硬上=造一个必被关掉的 block。

## 给父会话的最终输出

**一句结论：不升 L3。语义模式不满足 L3「可机械判定」前提，且同族机制（dd_verify_gate）已用物理数据实测否决过一次——再升就是复刻它的退役曲线。第三条路：归 L1（场景化 self-check 锚点）+ 把 G1 提案 resolve 为 reject-with-reason，不新增任何 hook。**

### 理由链

**① L3 的前提是「可机械判定」，decision-throwback 不满足。**
已有 3 个 L3 hook 全是硬边界：guard_native_memory（path 匹配）/ destructive-bash（rm -rf 字符 + 调用闭包）/ userid 白名单（数字串查表）。它们都是非 LLM 物理量可判定。decision-throwback 是「抛回 vs 合法上抛」的语义区分——区分它必须理解上下文（这个分叉是不是命中三类合法 trigger）。机械判定要么字符匹配「你想 A 还是 B」式句式（漏抓变体 + 误杀合法 trigger 的同款句式），要么 spawn LLM critic（prior 共盲 + 引入新误杀源）。**两条路都不是硬边界，是把语义判断伪装成机械判断。**

**② 同族机制已经用物理数据否决过一次——这是本案最强证据。**
dd_verify_gate.py 是「核对不抛回」(verify-throwback) 的 Stop hook，与 decision-throwback 同族（都是 LLM 输出文本里的语义抛回模式）。它跑了 v0 观察档 10 天攒 344 条数据，**真阳性仅 1.2%**，基础率 ~0.3 次/天，2026-06-10 评估结论：「文字规则已够用」，摘除注册退役。decision-throwback 没有理由比它的孪生跑出更好的机械判据。**升 L3 = 无视自己刚花 10 天得出的实测否决，重走一遍。**

**③ 检测时机印证够不着。**
抛回出现在 assistant **输出文本**，不是 tool call——PreToolUse 够不着。唯一可 hook 点是 Stop（输出后），动作只能是「打回重写」或「spawn critic」。Stop hook 写错的爆炸半径 = 会话卡死（dd_verify_gate 注释里 Keith 自己写的铁律）。在最危险的 hook 点上做最不可机械判定的判断 = 最坏组合。

**④ 「累积 10 次该升 L3」本身是 monster 的结构性冲动。**
decision-authority.md 沉淀过 `engineering-impulse-as-load-bearing-disguise`——「屡犯 → 加机制」的反射本身是工程冲动。base rate 还没实测（「10 次」是印象，2026-04-29 同类「300+」实测为 17 次）。对「屡压不住」的正解是先拿数据，不是先加层（`cadence-as-symptom` / `theory-gap-without-data`）。

### 第三条路（具体落地）

**归因到层：decision-throwback 不是 L2 失败，是 L1 + 帧问题，所以 L2 锚词当然压不住——但解法也不是跳到 L3。**

decision-authority.md 自己 2026-04-29 就判定这是「结构性偏置」，但归错了出路（以为结构性=该上 L3）。真相是：它是**帧问题**——「方案呈现」帧下，「列多个实现选项」被默认语法奖励为「周全」，self-check「这几个是不是实现层」在该帧里提不出来（对照 CLAUDE.md Context Asymmetry 段「这不是阈值问题是帧问题」的同款诊断）。

1. **resolve G1 提案为 `reject-with-reason`**：理由=语义模式不满足 L3 前提 + 孪生 dd_verify_gate 已实测否决（1.2% 真阳性）。NW 只识别+提案，本就不自动改 hook——这条正好该被人工 reject 掉，避免它在 pending 池里发酵成「待办的加机制债」。

2. **L1 场景锚点（已部分存在，补全即可）**：decision-authority.md 时间线 2026-06-18 条已落自检「出方案时数待决项里几个是实现层我该自己拍的」。这是对的方向——把它从「时间线散记」提到 CLAUDE.md Decision Authority 段的**显式 self-check 步骤**（结构化 self-check 是 L2 上限，比纯锚词硬一档，但仍是文字、不是 hook）。一行：「出『待决项』表前，逐条标实现层/目标层/偏好/不可逆——只有后三类能留在表里。」

3. **若 Keith 仍要工程托底（可选、低优先）**：唯一不退化成软规则的形态是**事件层飞轮**——不是通用 hook，是在**具体高发场景的脚本里内嵌门控**。如 cg_platform_onboard.py（decision-throwback 高发于 onboard 类方案会话）在生成「待决项」段时，脚本侧强制每条带 `layer:` 标注，缺标注或标了「implementation」的条目直接不渲染进输出。这把判断锚到脚本执行（rule-layer-flywheel：事件层），而非 prompt。但这是**单场景**解，不通用——通用 decision-throwback 没有可锚的事件，只能靠 L1。

**不做的**：不写通用 Stop hook、不扩 dd_verify_gate（它自己已退役）、不在 AskUserQuestion 前注入反例（抛回常是纯文本不调该工具，且仍是软提醒换壳）。

### trade-off
- 选不升的代价：decision-throwback 会继续偶发，靠 Keith 在场快速纠正兜底（base rate 低，可接受）。
- 选升的代价：误杀合法上抛（三类 trigger）→ Keith 烦 → 关 hook，3 个月内复刻 dd_verify_gate 退役曲线，且期间污染了 hook 体系 + 强化了「屡犯就加机制」的错误路径。
- 不对称：误杀合法上抛比偶发 decision-throwback 伤害大得多——合法上抛被拦=Keith 该拍的不可逆参数被 hook 挡住，那是真风险；decision-throwback 只是浪费 Keith 一次否决。
