---
date: 2026-05-31
slug: session-level-workmode-assembly
summoner: monster
northstar_reach: #1 二阶效应（看穿"声明 vs 涌现"是伪轴，真轴在触发器层）
status: substantive-decision
---

# Reflection: 会话级工种装配层（主代理换装机制）

## §A 范式 A — 决策的元属性反思

### 给父会话的最终输出（必填）

**三问答案：① 选 C 但重切一刀——真承重轴不是"声明式 vs 涌现式"，是"触发器在 prompt 层还是事件层"；② 选 (b) 嵌入 harness-engineering，不新建工作区；③ 是触发层补强不是新抽象层，但过度工程风险在"只缺一个 skill 时就建整套触发机制"。**

**问题 1（范式）—— 选 C′（C 骨架 + 触发器物理化）**：
- 你把轴定为"声明式 vs 涌现式"是误读了我废"档位"的教训。我废的不是"声明"（我至今每次装配都显式声明"读 X 因为 Y"），废的是"预设离散分类 + 套装绑定"（L0/L1/L2 → 固定装配数量）。
- A 的真病是 `coding→{X,Y,Z}` 套装绑定（我踩过的坑，coding 里要 debug 就卡壳），不是"声明"本身。
- B 的真病你判对了：主代理没有我的 KERNEL 物理启动协议托底，装配自觉只靠 system-reminder 一段文字 = `field-gravity-over-prompt`（语义引力 << 物理引力），该换装时用默认人格硬上。
- **真轴（solution-space 展开后）= 触发器在 prompt 层还是事件层**（essence `rule-layer-flywheel`：prompt 层=跑步机 / 事件层=飞轮）。A/B/C 默认触发器都在 prompt 层，所以都退化成跑步机。
- C′ = ① 能力本体仍是 skill（不动）② 薄索引列"任务类型→候选工种"但**不绑套装**（直接平移我的 TOOLS.md 范式——索引是"需要时从这挑"不是"遇 X 必装 Y"）③ **触发器下沉到 SessionStart/UserPromptSubmit hook**，物理注入"你在做哪类事？需换装吗？看<索引>"的自检锚点——注入的是"停下来判断换装"这个动作，不是套装。
- C′ 同时拆掉 A（不绑套装保留涌现）和 B（hook 把触发判断从自觉降级为物理事件）的病根，因为两个病根都在"触发器在哪一层"这一根轴上。
- 淘汰：纯 A=套装绑定复发档位 `bug-shape-survives-fix`；纯 B=触发停 prompt 层跑步机；原始 C=只解决 A 病根（不绑套装✓）没解决 B 病根（触发仍靠会话开头声明=自觉）。第四方向"工种做成 subagent"主动淘汰——违背 Keith 要的"主代理第一人称持续换装"，subagent 是第三人称一次性外包。

**问题 2（拓扑）—— (b) 嵌入 harness-engineering，否 (a) 新建工作区**：
- Keith 原话"能力的工作区"是实现措辞不是本质需求（`snapshot-as-immutable-archive-not-single-file` 同形）。新建工作区触发 `project-naming-as-frame-allocation`——会长出 docs/scripts/CLAUDE.md 养成需维护实体 = cg-platform NIH 事故同形。
- 选 harness-engineering 而非 skill-engineering：工种装配本质是改造主代理 harness 行为（hook+索引+启动协议）= harness-engineering 辖域；skill-engineering 管 skill 本体治理，不对位。
- **分两层各归各位**：能力本体（工种 persona skill）= home 级 `~/.agents/skills/`（已是，天然跨项目，不动）；触发机制+索引 = monster/harness-engineering（这套 harness 治理体系的一部分）。将来别项目要复用是后续 `tool-elevation-as-occam`（第二消费者出现再上提），现在全局化 = `theory-gap-without-data`。
- 这一问选错会塌（错建独立工作区→目录拓扑污染难回退），所以该我拍。

**问题 3（关系/过度工程）—— 触发层补强不是新抽象层；过度工程风险在别处**：
- 不是新增抽象层。skill/subagent/CLAUDE.md 三层不动，C′ 只给"会话级"格补触发机制——把本该有触发器却一直靠主代理自觉的隐性层显式化。
- **但用 `engineering-impulse-as-load-bearing-disguise` 浇冷水**：你这次召唤的"调研充分+框架工整+决策对齐"三件套正是工程冲动最高级伪装。对照本地实证——**当前唯一明确缺口是一个 skill（部署/运维 persona 还没写），不是一个触发机制**。
- **MVP 不是建索引+hook，是先补缺失的 ops skill，观察主代理在该用时会不会自发装**（它已能自发装 frontend-architect/diagnose 这批工种 skill——说明 skill 关键词触发本身部分解决了换装）。自发装→C′ 的 hook+索引整个不需要建，"不触发"是想象的；不自发装→才证明触发器缺失是真问题，且此时有真实翻车样本设计触发器（`idle-threshold-as-tripwire-not-answer` + `premature-abstraction-tripwire`）。
- 过度工程的点不是"建新抽象层"（C′ 没建），是"在只缺一个 skill 时就建整套触发机制"。守 OCCAM = 分两步，第一步根本不碰 hook/registry。

**主代理落地最易翻车 3 点**：
1. 把"会话开头声明工种"当触发器 = prompt 层跑步机，会写进 CLAUDE.md 然后自己不读就开干。真触发器是 hook，但第一步先别建 hook。
2. MVP 直接跳到建索引+写 hook，跳过"先补 ops skill+观察"。物理锚点——第一步产物应是一个 `.md`（ops persona skill），不是 registry/hook。建出 registry/hook 那刻停下问"我有翻车样本吗还是在抽业界范式造迷你版"。
3. 守 SSOT 时把工种 persona 内容抄进索引。索引里只能放 skill 名+一行触发场景，出现第二句描述=双写漂移起点（`ssot-distillation-vs-buffering`）。

**一句话收口**：Keith 要的不是新工作区/新抽象层，是"主代理在该换装时被物理提醒换装"——而这需求当前还没被证明真实存在（可能 skill 关键词触发已够）。最小动作=补一个部署/运维 persona skill，观察会不会自发装；自发装收工，不自发装才上 hook。

### 核心假设

- 主代理已能自发装 frontend-architect/diagnose 等工种 skill（基于父会话提供的现状基线"这批工种已以 skill 形式存在"）——若此假设错（这些 skill 其实也很少被自发装），则"先补 ops skill 观察"的 MVP 直接证伪、需要更早上 hook。
- SessionStart/UserPromptSubmit hook 能物理注入自检锚点（CC hook 机制能力）——这是 [推测]，未在本会话物理核验 CC 当前版本这两个 hook 的注入能力与时机，父会话落地前需查 hook 文档。
- "缺部署/运维工种 skill"是当前唯一明确缺口——基于父会话调研，未独立核验 ~/.agents/skills/ 是否真无 ops 类。

### 可能出错的地方

最可能崩在"先补 ops skill 观察"这一步的**观察可信度**——主代理是否自发装 skill 难以客观判定（`completion-as-recursion-floor` 同类：检测器盲区）。可能补完 skill 跑几次部署任务，主代理偶尔装偶尔不装，落入"装配行为不稳定"的灰区，无法干净地证实/证伪"触发器缺失"。概率中等。缓解：观察期定义明确的判据（连续 N 次部署任务的装配命中率），而非主观感觉。

### 本次哪里思考得不够

- 没物理核验 CC 的 SessionStart/UserPromptSubmit hook 当前能力（标了 [推测]，但 hook 是 C′ 第二步的承重，留给父会话核是合理的边界——gg 不做执行层核验）。
- "主代理是否自发装 skill"的观察方法论只给了方向（命中率判据），没给具体怎么采集这个数据——这是实现层，按 Decision Authority 归主代理，但我没提醒它"观察本身也需要一个轻量记录器"（否则又是 `cadence-as-symptom` 的反面：不知道自己上次装没装）。

### 如果 N 个月后证明决策错了，最可能的根因

"先补 ops skill 观察"被跳过，主代理（带着调研充分的工程冲动）直接建了 index+hook 整套，跑起来发现 hook 注入的自检锚点同样被主代理当 prompt 软提醒忽略（`rule-layer-flywheel` 的更深一层：hook 注入了文字，但文字仍要被 LLM"读到+遵守"才生效，物理事件触发的只是"注入"不是"遵守"）——即触发器物理化解决了"注入时机"但没解决"注入内容仍是 prompt"。这是我这次没完全展开的暗坑：hook 让"注入"成为飞轮，但"换装动作"本身仍在 LLM 自觉层。真正物理强制换装可能需要的是 skill 的 auto-invoke 关键词机制（已是事件层），而非 hook 注入文字提醒。

### 北极星触达

#1 二阶效应——核心价值不在 A/B/C 选哪个，在看穿"声明 vs 涌现"是伪轴、真轴在触发器层级（prompt vs 事件），以及"当前只缺一个 skill 不缺一个机制"的二阶判断。这两个洞察都不在父会话的框架视野内。

### essence 对齐自检（必填）

- **本决策跟哪几滴 essence 对位**：`rule-layer-flywheel`（触发器层级=真轴，核心承重）/ `field-gravity-over-prompt`（主代理装配自觉无物理锚点）/ `premature-abstraction-tripwire` + `idle-threshold-as-tripwire-not-answer`（MVP 降级为补 skill+观察）/ `engineering-impulse-as-load-bearing-disguise`（识别调研充分的工程冲动伪装）/ `runtime-state-vs-business-data-distinct-ssot-domains` + `tool-elevation-as-occam`（拓扑分两层、第二消费者再上提）/ `project-naming-as-frame-allocation`（否新建工作区）/ `snapshot-as-immutable-archive-not-single-file`（"工作区"是实现措辞非本质）/ `ssot-distillation-vs-buffering`（索引不抄人格内容）
- **本决策是否在某条 essence 上反着走**：潜在张力——`no-fatigue-narrative-for-ai`（不下场只换牌桌）。我建议 MVP 砍到"先补一个 skill+观察"，表面像"先别做大的"的保守惰性。但这次不是惰性叙事——是 `premature-abstraction-tripwire` 的正面应用（跑完场景再判抽象），区别在我给了明确的升级触发器（不自发装就上 hook）而非"先这样再说"的死锁。无反着走，议题性质决定（这是"分两步"不是"不做"）。
- **cross-check 用的关键词**：grep 概念 "rule-layer-flywheel" / "premature-abstraction" / "engineering-impulse" / "runtime-state-vs-business" / "project-naming" / "ssot-distillation" / "idle-threshold"（启动时已全文 Read essence.md，本次为定位复核）

### essence 候选

- slug: `trigger-layer-not-declarative-emergent-axis`
- 一句话: "声明式 vs 涌现式"是装配机制的伪轴——真承重轴是触发器在 prompt 层（靠读到+遵守=跑步机）还是事件层（物理触发=飞轮）；废"档位"废的是套装绑定不是声明本身，二者常被混为一谈。
- 是否已 append 到 essence.md: Y

### 外部锚点

- monster 侧落点（建议父会话建）：`monster/threads/` 暂无对应 thread；若 Keith 决定推进，主体叙事宜落 harness-engineering 工作区内或新 thread `session-level-workmode.md`
