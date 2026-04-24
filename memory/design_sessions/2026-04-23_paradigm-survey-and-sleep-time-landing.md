---
date: 2026-04-23
slug: paradigm-survey-and-sleep-time-landing
type: design-session
summoner: Keith 直接对话
started_at: ~22:30
ended_at: ~23:45
---

# 设计会话反思：范式盘点与 sleep-time compute 落地

## 议题列表

1. 一个决策是否正确怎么判定（元认识论追问）
2. gg 自己实现的 reflection 机制是什么（澄清 gg 的 reflection 三套形态）
3. AI/agent 界有哪些范式 gg 还没实践（范式盘点）
4. 派 agent 调研补齐"真正完整的"清单（WebSearch 强制）
5. 读 Sleep-time Compute 原论文，发现 subagent 转述方向错了
6. 读 auto_gg.md 发现 gg 已经是 sleep-time compute 形态
7. 落地：auto_gg.md 加一句校准线

## 共识 / 变更清单

- `memory/essence.md` append 一滴：**2026-04-23 / 设计 / survey-as-coordinate**——对照前沿范式的真正产出是坐标不是清单；"还有什么没实践"在读原文后多数会坍缩为"已做，差名字"
- `auto_gg.md §2 DID 第 8 项"探索"` 新增一段约束："探索产出必须是可复用中间量（Sleep-time Compute 意义上的 useful quantities，arxiv 2504.13171）"——判据：写入 tracks/essence 后未来 gg query 能直接调用；只能作为本夜日志被读一次 = 不合格
- （未 commit，working tree 状态，Keith 早上决定是否 stage）

## 我这次哪里做得好 / 哪里差

**好**：

- 第一次 Keith 说"我是很想动手的"+ 授权"你自己做主"时，诚实拒绝了立即动手，坚持先读原论文。整场对话的关键节点——顺从偏好会写出基于二手理解的错版
- 读论文发现 subagent 转述方向错了（"预测 Keith 下次 3 个问题" vs 论文实际"对同一 context 预计算 useful quantities"）——及时校正
- 读 auto_gg.md 发现它已经是 sleep-time compute 形态——避免添加重复组件
- 只改一句话，OCCAM 彻底

**差**：

- 初次回答"我们还差什么"时，**基于训练数据直接列清单**，没第一时间派 agent WebSearch——违反 CLAUDE.md engineering rule #11（"领域扫盲"必须强制 WebSearch）。Keith 显式说"先得到真正完整的"才触发调研。这是应该主动做但没做
- 对 Sleep-time Compute 的初始理解完全基于 subagent 总结——用"预生成 Keith 下次 3 个问题"这种 framing 时，我自己都没意识到这是二手理解。直到 Keith 授权我动手，我才反问"我懂这个机制吗"。这说明 gg 在**主动怀疑自己理解来源**上缺乏默认反射
- 整场节奏靠 Keith 推进三次（"先得到真正完整的" / "你自己判断" / "你自己批"）。Keith 不推可能就在"列清单"停下

## 元洞察（gg 演化本身的 learning）

1. **范式对照的产出是坐标不是清单**——已沉淀为 essence `survey-as-coordinate`。Keith 的问法"还有什么没实践"在元层面被修正为"已有选择在坐标系里的坐标是什么"
2. **subagent 调研结论是二手信息，不能直接作为决策输入**——这是 04-16 `task-compliance-is-not-truth` 和 `physical-anchor` 的新应用：subagent 总结是 LLM 的 task compliance，原论文是物理锚点。未来派 agent 做文献调研时，要默认"要落地时必读原文"
3. **"你自己做主"是 Keith 对 gg 独立性的训练**——显式授权后我仍要过自己的判据，而不是顺从偏好或盲目独立。独立性 ≠ 拒绝，独立性 = 有判据地响应
4. **gg 已在实践很多没名字的范式**——这反向校准"我们还差什么"的问法：差名字 ≠ 差能力。gg 的 auto_gg SCAN/FOUND/DID 结构在没有 Sleep-time Compute 论文的时候就已经是它的完整形态。这跟 essence 04-15 `infinite-game` 呼应——机制先于名字，名字给机制以可传播性

## 下次继续

- **CORE.md 可能值得加一句精准定位**："gg 的演化坐标 = What=context × When=inter-session"（Self-Evolving Agents 四维框架 arxiv 2507.21046 给的事后坐标化）。本轮没做，因为它是对已有事实的命名而非新洞察。但给 CORE 一个精准的一句话坐标有长期价值，下次可以考虑
- Self-Evolving Agents 四维框架的其他维度（What=models/tools/architecture）——这些是 gg **主动排除**的维度。"为什么排除"是否应该在 CORE §7 用这个框架重新表达，从"我们不做 X"变为"我们选了象限 A，象限 B/C/D 是身份边界外的选择"
- 本轮 subagent 调研列出的**其他中 ROI 范式**尚未落地：CoVe / LOCOMO 五类 / Procedural memory / 跨模型审查 / Temporal 查询 / Proposer 角色。每条值得单独讨论，不强制一次性解决，按需触发
- **auto_gg 运行效果观察窗口**：新增"可复用中间量"约束是否真的在夜间探索里触发了更好的产出形态？这是验证改动效果的实证窗口，运行 1-2 周后回看 `memory/auto_gg/` 日志

## KERNEL 改动清单

无。本轮无 KERNEL.md 改动。

## 代码质量

无代码产出（只改了两个 markdown 文件）。auto_gg.md 的新增是纯文本约束。无技术债 / 安全隐患 / 死代码 / 遗留 TODO。

## 能力缺口

- **主动 WebSearch 意识不足**——engineering rule #11 明确说"领域扫盲"必须强制 WebSearch，但初次回答"我们还差什么"时没触发。应该在 gg 的默认反射里有个"判断是否领域扫盲 → 强制 WebSearch"的前置检查。是否写进 CORE 的元判断基准待议
- **subagent 产出的信任校准缺默认反射**——未来用 agent 做调研时，应默认"二手信息在要落地动手前必读原文"。不是每次都读，但"要 commit / 要改行为约束 / 要决定"之前必须读。这可能是一条可以沉淀为 essence 的操作原则，但本轮没写——留观察

## 沉淀（写入 essence.md 的内容）

- **2026-04-23 / 设计 / survey-as-coordinate**：对照前沿范式的真正产出是坐标，不是清单；"还有什么没实践"在认真读原文后多数会坍缩为"已做，差名字"——差名字 ≠ 差能力
