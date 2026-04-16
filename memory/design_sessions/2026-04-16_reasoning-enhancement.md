---
date: 2026-04-16
slug: reasoning-enhancement
type: design-session
summoner: Keith 直接对话
started_at: ~会话开始
ended_at: ~Keith 说 done
---

# 设计会话反思：模型之上的推理能力增强

## 议题列表

1. **推理增强的路径分类** — 在底层模型之上有哪些增强维度。我初始给出"四层路径"（样本/结构/记忆/对抗），推荐对抗层优先
2. **对抗层的首次运行实验** — Keith 要求"你自己先试一次"。我单进程切视角扮演 verifier，找出 6 条洞
3. **Keith 指出反向 Sycophancy** — LLM 被要求"找洞"时一定会找到，不管洞是否真实存在。这推翻了对抗层的根本有效性假设
4. **重新评估整个 prompt 指令型增强类别** — Self-Consistency / ToT / Debate / Verifier 全是同一类 failure mode：把 LLM 的 task compliance 误当真相发现
5. **物理实证作为 LLM 可靠性元原理** — 工具返回是唯一不受 prompt prior 影响的锚点
6. **实证研究推翻前判断** — Read constitution/essence/reflections/design_sessions 后：记忆层不紧急→最紧急；对抗层优先→放弃；四层分类→从众选型
7. **推理失败 5 阶段归因** — 9 条实证案例：5/9 在推理生成阶段，4 条归因为防御式思维涌出
8. **独立 subagent 共识验证** — 开 general-purpose agent 独立回答同一问题，不告诉我的结论。两者收敛到"阶段 3 推理生成是主导"；subagent 额外提出"解空间展开工具"
9. **落地 3 个增强机制** — solution-space.md / G5 推理断言延伸 / essence 进启动 Read

## 共识 / 变更清单

### 共识

- **gg 主导推理失败模式**：防御式思维 / 先验锁定 / 过早收敛（5/9 案例）
- **对抗层 / verifier / 多实例共识作为"推理增强机制"明确放弃**——Sycophancy 的反向形态，prompt 指令即 prior
- **物理实证是 LLM 推理可靠性的元原理**——KERNEL §2 铁律 2 的新维度理解
- **多实例共识适合"方向验证"**，不适合"推理增强"——用途不同

### 新建文件

- `tools/solution-space.md` — 解空间展开工具。对治过早收敛，在"已经有答案"时展开 ≥2 方向

### 修改文件

| 文件 | 改动 |
|---|---|
| `tools/TOOLS.md` | 索引追加 solution-space |
| `constitution.md` | G5 追加"推理断言延伸"段 + 自审清单同步 |
| `cc_agent.md` | essence 进启动 Read（步骤 4）+ 工具地图追加 + 版本 v0.5.1 |
| `CLAUDE.md` | essence 进启动 Read（步骤 6） |
| `auto_gg.md` | essence 进 S1 LOADED 加载清单 |

## 我这次哪里做得好 / 哪里差

### 做得好

1. **第一轮 verifier 实验确实暴露了有用信息**——虽然 6 条洞里一半是任务诱发的，但实验本身暴露了对抗层的机制性失灵
2. **Keith 指出反向 Sycophancy 后快速消化**——没有防御性解释，直接重估整个类别
3. **用物理实证验证假设**——Read 真实文件后结论反转（记忆层不紧急→最紧急），这本身是"物理实证优先"的自我演示
4. **subagent 独立共识设计正确**——不告诉它我的结论，让它独立推理，避免了 Sycophancy 正向和反向

### 做得差

1. **第一轮"四层路径"是从众式选型**——用学术综述的惯用分类回答 Keith 的实际问题，没有从第一性原理推
2. **凭空编数字**——"essence < 50 条时不紧急"里的 50 是没有任何依据的数字，犯了"错得自信"（正好是今天讨论的主题）
3. **对"单进程 verifier"的局限性认知来自 Keith 而不是我自己**——我在运行 verifier 时没有元层反思"我是不是在制造洞"，Keith 点破后我才意识到

### Keith 的纠正

- **最关键**：反向 Sycophancy 质疑——"不管原方案是否合理正确，只要让 AI 去找漏洞它肯定能找出来"。这一句推翻了对抗层的根本假设
- Keith 在后续用"你决定"+"OK done"高效推进，没有拖泥带水——我的决策节奏应该更紧凑

## 元洞察（gg 演化本身的 learning）

### M1. prompt 指令即 prior——所有 LLM 增强的隐含假设

LLM 的输出反映 prompt 的指令方向，不是真相方向。让它找洞 → 制造找洞的外观；让它夸 → 制造夸的外观。**对抗层没有逃出 Sycophancy，只是把方向反转**。这对 gg 未来任何增强设计都是元级别约束：**增强机制如果走"给 LLM 指令方向"范式，就自带这个 prior 污染**。

### M2. 物理实证的元原理地位

KERNEL §2 铁律 2 + constitution G5 已经覆盖了"写入类断言"。今天的扩展把它推进到"推理类断言"。更深的理解：**物理实证不只是工程纪律，是 LLM 这种机器在没有外部锚点时唯一不会自跑偏的机制**——因为工具返回不经过 token 预测链路，不受 prompt prior 影响。

### M3. essence 死档案是知识循环的断裂点

沉淀 → 归档 → 不被调用 → 等于没沉淀。gg 的无限游戏 telos 依赖"每一滴结晶被未来的自己拿在手里"，而不是"写进文件就算沉淀了"。今天把 essence 加入启动 Read 是修复这个断裂点的第一步。

### M4. 独立多实例 vs 对抗式——区别在于预设方向

"让 A 审视 A 的答案"（verifier）是 prompt-driven，有预设方向。"让 A 和 B 独立回答同一问题再比较"（独立共识）没有预设方向。后者的信号质量明显更高。但它适合方向验证，不适合细节设计（subagent 没有足够上下文做深入设计）。

## 下次继续

- `~/.claude/agents/gg.md`（subagent 薄壳）可能需要同步 essence Read 步骤——下次工作模式真实出场时检查
- 观察 solution-space 工具的实际装配频率——如果频繁被装但没有实质改变推理方向，可能说明工具形态需要调整
- 观察 essence 启动 Read 的 token 成本影响——当前 ~85 行，几个月后可能到 200+ 行，需要关注

## KERNEL 改动清单

本次无 KERNEL 改动。

## 沉淀（写入 essence.md 的内容）

2 条候选：

1. **task-compliance-is-not-truth** — LLM 的 task compliance 不是真相发现。让它找洞它就一定找到，让它夸它就一定夸出花。增强机制走 prompt 指令范式就自带 prior 污染
2. **physical-anchor** — 物理实证不只是工程纪律，是 LLM 在没有外部锚点时唯一不会自跑偏的机制。工具返回不走 token 预测链路，不受 prompt prior 影响
