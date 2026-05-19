---
date: 2026-05-18
slug: nw-misuse-detection-premise-collapse
summoner: cc-space
northstar_reach: #1 二阶效应
status: substantive-decision
---

# Reflection: NW Bash misuse 判定逻辑前提崩塌后的重裁（承接 nw-bash-hook-warn-not-deny）

### 给父会话的最终输出（必填）

**总裁定**：第 1 批 hook 砍掉（不做不降级）。真正第 1 优先是修 `constants.py` 子串匹配 bug（它是 hook 提案的诱因本身，属 nw-auto-apply 白名单内机械落地，父会话可直接落）。第 4 次撞 NW 指标不可信需一个最轻结构动作（nw-daily 加一条指标核验约束），不是新建框架。

**5 问定论**：

1. **hook 还做不做**：砍掉。前提物理崩塌（82%→4%，`rule-layer-flywheel` 触发条件"软规则高频失效"不成立，4% = 软规则基本生效）。4% 精确命中 cc-space 工程原则补充 1"偶发不写机制"，COST-BENEFIT 直接 reject 非判断题。我上一份"根因预判第一条"已自我预言此结局（只是包装成"warn 压不住 prior"，真相更彻底——被压对象本身不存在）。不降级保留：双指标拆分服务对象（测 hook 压制率）随 hook 砍而失效，一并砍。八 pattern 判别逻辑本身不浪费——下沉问题 2 复用。
2. **判定逻辑怎么修**：第 1 优先。`transcript.py:107-116` 子串匹配→结构短路+裸命令判别。短路四条：①含 `|/>/>>/<<\/$(`/反引号（86% 水分主体）②含 `&&/;/||` 复合（8%）③ git/npm/pip/docker/make 子命令上下文（1%）④ pattern 是参数字面量非命令头（1%）。只裸命令头判 misuse。硬约束三条：curl/wget 不准加回（rtk exclude 锁定）；**必须用父会话 613 条人工分桶做回归验证**（这是 R1 复发根因——当年无 ground truth 证伪，分子须落 26/613≈4% ±2pp）；不引入脆弱 shell parser（Occam，99% 水分靠结构符号短路即可）。
3. **判定逻辑与 hook 关系**：你识别"同一规则源两消费端"正确。但 hook 砍后塌缩为单消费端，SSOT 漂移风险消失，不需前置防御机制（否则是 `ghost-rules`）。落地：放过规则写 constants.py（事实判定 SSOT），加一行防漂移注释——未来若做拦截 hook 必须复用本模块。
4. **属哪类 + 账本**：判定逻辑修复 = nw-auto-apply 白名单内机械落地（落点 `harness-engineering/{lib,analysis}/**` ✓ / git revert 可回滚 ✓ / 零价值判断——"cat>>f<<EOF 是写不是读"是纯物理判定 ✓），**父会话可直接落不占 Keith 闸门**。上一份"落点 hooks/settings.json 需 Keith 闸门"的一致性论证随 hook 被砍而作废——前提崩塌后结论正确翻转，非矛盾。账本：R1 保持 done 追加复盘注（当年只移 curl/wget 未根治子串匹配是本次伪信号远因）；2026-05-12-R1+G1 标 **rejected**（非 superseded——问题本身被证不存在）；新开 2026-05-18-Rx 直接 done（走机械落地通道本轮闭环）。
5. **元层**：要动作不要框架。4 次撞墙（dashboard TTL / 事实矛盾提案 / subagent 报告≠行为 / 82% 伪信号）是同一元缺陷 4 次显现——每个指标被默认"可信输入"直喂治理，无一层问"这数字怎么算的、经得起人工分桶吗"。不建审计器（递归无底 + `tool-eats-its-critique`）。在 nw-daily 加一条约束：提案用统计百分比当"该不该做"论据时，生成前必须 ≥30 条原始样本人工分桶核验口径，存疑不得作承重论据。与 nw-auto-apply"陈旧度核验"完全同构（`physical-anchor` 第二次落地），非新机制。

**行动清单（按序，给父会话）**：①修 constants.py+transcript.py:107-116（四短路+三硬约束）②613 样本回归验证（强制闭环，~4%±2pp）③constants.py 加防漂移注释 ④nw-daily 加指标核验约束 ⑤收账本（R1 追注 / 5-12-R1+G1 rejected / 新开 Rx done）⑥辐射检查：grep 所有消费 is_bash_misuse / Bash 滥用率的点（晨报 fmt / dashboard / hourly_check 告警）确认口径修复自动传导。

### 核心假设

- 父会话 613 条人工分桶（4% 真值）可信、可作回归 ground truth——这是整个重裁的承重砖。上一份的承重砖（82%）已崩，本份若 4% 也错则重裁同样失效。但 4% 来自父会话物理分桶非二手统计，可信度结构性高于上次的 82%
- 结构符号短路（管道/复合/重定向/子命令）能覆盖 ~99% 水分，剩 1% 边缘 case 漏判只影响统计精度不影响行为（hook 已砍，无行为后果）——可接受
- 判定逻辑修复"零价值判断"成立：剥掉判断后剩"shell 命令是否含管道/重定向符号"是纯物理核对（`mechanical-apply-decouples-from-value-gate` 试金石过）

### 可能出错的地方

- **最大风险（概率 30%）**：613 分桶里"裸命令"边界定义与我短路规则有口径差——父会话分桶可能按更细/更粗标准，回归跑出来不是 4% 而是 8% 或 2%，那时要回去对齐"什么算裸命令"的定义而非继续调短路规则（否则又是 R1 式"修计算口径不修根本"）。缓解=回归验证步骤强制，数字对不上不算闭环
- **次风险（概率 20%）**：nw-daily 那条"≥30 样本人工核验"约束本身被 nw-daily 会话敷衍执行（LLM 自约束复发，同 nw-auto-apply 生成端轻约束风险）——它是 prompt 软约束不是物理闸。缓解弱：靠"存疑指标不得作承重论据"是判据非机制。若复发，下次撞墙时升级为 apply 端物理拦（但现在做=过度设计，留 tripwire）
- **小风险**：reject 2026-05-12-R1+G1 后，若未来 Bash 真滥用率因业务接入（cc-gateway/华昇等）结构性飙升到非偶发量级，hook 提案需重启——但那是新前提下的新提案，非本次 reject 错误

### 本次哪里思考得不够

- 没物理读父会话 613 条分桶的具体样本，只接受了汇总表（4 类水分占比）——与我批判上一份"接受 82% 未核验"是同一动作的弱化版。缓解=回归验证步骤把核验推给父会话实跑（有 ground truth 在手），但我自己这一轮仍是"接受了一个二手数字 4%"，诚实标注
- 没设计 transcript.py 短路规则的具体代码形态（token 切分边界、heredoc 检测的精确实现）——只定了判别原则四条，实现细节留父会话，可能实现时发现某条短路规则有歧义需回裁
- nw-daily 那条元层约束的具体措辞未逐字敲定（"统计百分比当论据"的边界——多少算"承重论据"？），留了模糊空间

### 如果 N 个月后证明决策错了，最可能的根因

最可能：**613 这个新数字也是某种口径产物，4% 同样不是"真值"而是父会话另一种分桶标准下的声称**——我这一轮的元洞察是"指标是声称不是事实"，但我自己又接受了 4% 当新的承重砖，只是把信任从 82% 平移到 4%。若父会话分桶时把"`find . -exec cat`"算进水分而 hook 设计本意要拦这种，则 4% 低估了真滥用，hook 不该全砍。根因：`metric-is-a-claim-not-a-fact` 这条洞察我用来批判上一轮，但没有递归应用到本轮自己接受的数字上——`bug-shape-survives-fix` 的精确重演（修了对 82% 的盲信，没修"接受单一汇总数字"这个内化动作本身）。唯一缓解=回归验证步骤强制父会话用原始样本跑，把"接受数字"换成"跑出数字"。

次可能：hook 全 reject 后业务接入（华昇/cc-gateway 大量 subagent）让 Bash 模式整体重洗，4% 在新使用模式下失真，rejected 提案需重启——但这在 reject reason 里已显式标"新前提下的新提案"，非决策错误。

### 北极星触达

**#1 二阶效应（space 方向）**：Keith 一阶诉求是"上一份裁定前提被证伪了，重裁"。二阶结构是——这是同一个本体论错位的**第四次显现**（前三次：2026-04-21 NW 治理档位线性分级 / nw-auto-apply 机械与行为同池 / 上一份可逆动作套不可逆 deny 档），但本次显现的不是"档位/权力错配"而是更底层的**"指标被当事实"**：所有前三次错配的共同上游是"决策基于一个未核验的给定数字"。更远一层——这对 cc-space 元方法论"内部不可靠→外部锚点托底"划了第二条边界（上一份划了第一条"锚点受力对象"）：外部锚点不仅可能施力错对象，**锚点本身可能是个测错的尺子**。一个测错的外部锚点比没有锚点更危险——它给伪信号穿上"客观度量"的外衣，让基于它的精巧治理（我上一份整份裁定）看起来无比合理。这条边界对 5 年维度 cc-space 所有"建指标→基于指标治理"的复利是：指标投产前必须有一次人工分桶 ground truth 校准，否则建的是放大伪信号的机器。

### essence 对齐自检（必填）

- **本决策跟哪几滴 essence 对位**：
  - `physical-anchor` (2026-04-16)——核心：上一份接受 82% 未物理核验是反面教训；本份解法（613 回归验证 + nw-daily 抽样核验约束）是其在"二手统计数字"输入类型上的落地
  - `rule-layer-flywheel` (2026-04-24)——hook 砍掉的核心：触发条件"软规则高频失效"在 4% 下不成立，前提崩塌；上一份基于 82% 误判触发条件
  - `task-compliance-is-not-truth` (2026-04-16)——元层根因：让 LLM 基于给定痛点数字设计治理，它设计出精巧治理但不质疑数字真伪（我上一份就是样本）
  - `action-type-over-aggressiveness` (2026-04-21)——判定逻辑修复归类机械类：与 nw-auto-apply 同承重墙，剥价值判断后纯物理核对
  - `mechanical-apply-decouples-from-value-gate` (2026-05-18 今日)——问题 4 直接应用其判别试金石：判定修复零价值判断→白名单内机械落地不占 Keith 闸门
  - `ghost-rules` (2026-04-15)——问题 3 否决建 SSOT 共享机制：hook 砍后第二消费端不存在，为不存在的漂移建防御=幽灵规则
  - `tool-eats-its-critique` (2026-05-12)——问题 5 否决建指标审计器：把对指标的批判写进又一个产指标的工具，递归无底
  - `decision-execution-gap` (2026-04-21)——R1 追加复盘注的依据：让下一次决议看见上一次估错多少
  - `bug-shape-survives-fix` (2026-04-27)——根因预判核心：我用"指标是声称"批判上一轮，但自己又接受 4% 当新承重砖，bug 形态幸存于修复
- **本决策是否在某条 essence 上反着走**：表面顺着 `physical-anchor` 走（强制回归验证），但根因预判已自曝半反——我这一轮自己仍是"接受了 4% 这个二手汇总数字"，没把 `metric-is-a-claim-not-a-fact` 递归应用到本轮。没因此改决策（4% 来自父会话物理分桶，可信度结构性高于 82%，且回归验证步骤把核验外推给父会话实跑），但显式标注这个未闭合的递归——这是诚实而非自洽
- **cross-check 用的关键词**：grep "physical-anchor" / "rule-layer-flywheel" / "task-compliance" / "action-type-over" / "mechanical-apply-decouples" / "ghost-rules" / "tool-eats-its-critique" / "decision-execution-gap" / "bug-shape-survives-fix"（启动时 essence.md 已 Read 全文 L1-L475，记忆检索 + 物理确认 mechanical-apply-decouples 在 L471-474）

### essence 候选

- slug: `metric-is-a-claim-not-a-fact`
- 一句话：指标不是事实，是某段代码对事实的一个声称——把指标当治理承重输入前必须物理抽样核验其计算口径，否则是为一个被代码放大的伪信号设计精巧解法。判别试金石："这个百分比，我亲手对 ≥30 条原始样本人工分桶过吗，还是我接受了它"。一个测错的外部锚点比没有锚点更危险——它给伪信号穿上客观度量的外衣。
- 是否已 append 到 essence.md: N（工作模式不擅自 append；这是 `physical-anchor` 在"二手统计数字"输入类型上的精化 + `task-compliance-is-not-truth` 的工程数据变体，候选性质需 Keith review。与上一份候选 `anchor-receives-next-round-not-this-round` 互补——共同构成对 cc-space 元方法论的双向边界）

### 外部锚点

- `~/githubProject/cc-space/harness-engineering/lib/constants.py` ← 判定逻辑 SSOT，待机械落地修复（白名单内）
- `~/githubProject/cc-space/harness-engineering/lib/transcript.py` :107-116 ← 子串匹配 bug 本体，待修
- `~/githubProject/cc-space/harness-engineering/analysis/proposals.jsonl` ← R1 追注 / 5-12-R1+G1 rejected / 新开 Rx done（待父会话）
- `~/githubProject/cc-space/harness-engineering/nw-daily.md` ← 待加指标核验约束（机械落点）
- `~/githubProject/gg/memory/reflections/2026-05-18_nw-bash-hook-warn-not-deny.md` ← 被本份证伪的前一裁定（前提崩塌对照基准）
- `~/githubProject/gg/memory/reflections/2026-05-18_nw-auto-apply-mechanical-boundary.md` ← 白名单边界判据来源（问题 4 一致性依据）
