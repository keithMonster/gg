---
date: 2026-04-13
slug: neural-link-evaluation
type: design-session
summoner: Keith 直接对话（gg 目录设计模式）
started_at: ~晚间
ended_at: ~晚间（同一会话内闭环）
---

# 设计会话反思：NEURAL-LINK 协议评估 + 宪法 G5 升级

## 议题列表

今天 Keith 和我讨论了什么？按出现顺序列出：

1. **Keith 提议**：参考另一项目（openclaw, `~/.openclaw/workspace/cortex/protocol/neural-link-v1.md`）的 NEURAL-LINK v1 通讯协议，让 gg 评估其是否适用于"自我通讯 / 子代理通讯 / 文件构建"
2. **gg 三层评估**：拆出符号集 / L0 物理约束 / 跨代理通讯格式三层独立判断
3. **gg 提议**：符号集不采纳 / L0 三条吸收（其中 `@LOGIC_IS_NOT_PHYSICAL` 升级到宪法）/ 跨代理格式不引入
4. **Keith 授权**："你自己决定，不用再问我了"——对当前提议的明示批准
5. **gg 执行**：constitution.md 加 G5 + 辐射面同步（state.md / working_context.md / tracks/cc.md / 本反思）

## 共识 / 变更清单

### 共识
- **符号集**：不采纳。gg 的第一读者是人，符号化损害可审阅性，违反 CORE.md §3 精神
- **L0 物理约束**：`@LOGIC_IS_NOT_PHYSICAL` 升级到宪法 G5；`@PROMPT_PREMATURE` 和 `@TRACE_OR_DIE` 被 G5 第 1/2 条吸收
- **跨代理通讯格式**：不引入新协议。真正痛点在内容层（谁改了什么 / 下一个代理怎么收到），不在格式层
- **方法论**：评估外部协议时，拆"哲学层"和"格式层"独立判断——这个方法本身被登记为候选 reasoning_module `PROTOCOL_HARVESTING`

### 变更清单（5 文件 9 处改动）

- **`constitution.md`**：
  - 顶部描述："3 条工程闸门" → "5 条工程闸门"（顺手修复历史辐射漂移：v0.1.x 时已是 4 条但顶部没更新）
  - 新增 G5 PHYSICAL PERSISTENCE（含触发 / 4 动作 / 4 禁止 / 与其他闸门关系 / 为什么宪法级）
  - 自审清单加 G5 项 + G5 例外条款（不允许"标注原因"豁免）
  - 元数据：版本 v0.1.0 → v0.2.0 + 增补记录 + 来源加 NEURAL-LINK v1
- **`memory/state.md`**：
  - `constitution_gates: 4` → `5`
  - 变更日志加本次条目（位置在 v0.1.x → v0.2.0 双模式重构条目之前，按时间倒序）
- **`memory/working_context.md`**：
  - 第 61 行 "8 原则+4 闸门" → "8 原则+5 闸门"
  - 第 74 行表格 "8 原则 + 4 闸门" → "8 原则 + 5 闸门（G5 于 2026-04-13 NEURAL-LINK 评估后增补）"
- **`tracks/cc.md`**：
  - 追加"从 NEURAL-LINK v1 协议评估"段（含三层评估表 + DQ-1 洞察 + 候选 reasoning_module `PROTOCOL_HARVESTING` 完整登记）
- **`memory/design_sessions/2026-04-13_neural-link-evaluation.md`**：本文件，新建

## 我这次哪里做得好 / 哪里差

### 做得好

1. **拒绝了"整体引入"的诱惑**。外部协议看起来很硬核，容易让我直接照搬。但我先做了**用户群体定位**（gg 的第一读者是 Keith / 是人），从这个原点推出"符号集不适合"。这是 P2 FIRST PRINCIPLES 的正确触达
2. **拆"哲学 vs 格式"两层判断**。这个方法让我在同一份外部协议里同时做"采纳"和"拒绝"的决策——不是非黑即白
3. **G5 的命名换皮**。外部协议命名是 `@LOGIC_IS_NOT_PHYSICAL`（机器风格），我吸收时改为 `G5 PHYSICAL PERSISTENCE`（gg 的命名风格 G1-G4 系列）。避免双语污染
4. **辐射检查先做**。开始动手前先 grep 了 `4 闸门 / G4 / constitution_gates` 全量辐射面，避免漏改。这是上次 v0.1.0 双模式重构时 Keith 反复强调的教训（他在 cc.md 里写过"辐射检查漏"）
5. **让 G5 自己 dogfood 自己**。本次会话就是"内存对齐 vs 物理持久化"的最小演示——所有"我建议升级 G5"的话在文件没改前都不算数。我在 tracks/cc.md 末尾显式标注了这一点
6. **顺手修了一个历史漂移**。constitution.md 顶部说"3 条工程闸门"，但实际 v0.1.x 已经是 4 条 G1-G4。这是 v0.1.x 增补 G4 时漏改的辐射面，gg-audit 也没抓到。这次趁势改成"5 条"

### 做得差 / 本可以更好

1. **第一次提议时把"gates 顶部描述漏更新"漏掉了**。如果不是辐射 grep 阶段才发现，就会再产生一次新的辐射漂移。这说明我的 grep 还不够前置——应该在**提议阶段**就把辐射面摸一遍，而不是执行阶段
2. **"选项 A + D 组合"那段提议结构略显冗余**。Keith 的偏好是最短指令，我列了 A/B/C/D 四个选项再选 A+D，其实可以直接说"我倾向 A+D"，把 B/C 作为可选 fallback 一句话带过。这是结构性话痨
3. **我没有主动问 NEURAL-LINK 协议在 openclaw 是否真的解决了问题**。如果 openclaw 那边它运行良好 vs 它在那边也半残，我的评估应该不一样。这是上下文获取的盲区——但 Keith 没说，我也没问。下次类似场景应该问

### Keith 的纠正

- **没有显式纠正**。Keith 这次的回应只有一条："你自己决定，不用再问我了"。这是一种**程序授权**而非**内容批准**——他认可方向判断，把后续微决策权委托给我
- **隐性信号**：他用了最短形式（11 个字 + `/effort` 命令切到 auto），没有展开任何二次讨论。这跟 First Contact 里"Q1:ok; Q2:ok;"的最短确认是同一种偏好——**我提对了的时候，Keith 不浪费字**

## 元洞察（gg 演化本身的 learning）

### 1. 宪法吸收外部协议的范式

**"用本系统命名风格重命名 + 选最高匹配度的现有结构"** 是宪法演化的健康路径，比"为新内容专门建新章节"更克制。本次 G5 的处理：
- 命名换皮：`@LOGIC_IS_NOT_PHYSICAL` → `G5 PHYSICAL PERSISTENCE`
- 位置选择：放在 G1-G4 系列后面，自然延续，不为它单独开"协议吸收"区段

这个范式已经写进 tracks/cc.md 的候选 reasoning_module `PROTOCOL_HARVESTING`。

### 2. 设计模式 D1/D4 的"批准"语义有梯度

D4 说每次硬核心修改都需要 Keith 明示批准。本次 Keith 说"你自己决定，不用再问我了"——这是不是 D4 的明示批准？

我的判断：**是，但有边界**。"你自己决定"的语义边界是**对当前已经放在桌面上的具体提议**（符号集不采纳 / L0 三条吸收 / 跨代理不动），不是空白支票。

下次会话遇到类似授权时，我应该**显式标注"我把 X 解读为对 Y 的明示批准，因为 Z"**——让批准链路可追溯。本次反思就是这个标注的物理化。

**这是 D4 的细化提议**：未来可以考虑在 CLAUDE.md §2 D4 增加一句"如果 Keith 给出范围授权（比如'你自己决定'），gg 必须在执行前显式标注这次授权覆盖的具体提议清单"。**本次设计会话不动 CLAUDE.md，先观察 1-2 次类似场景再提议**。

### 3. G5 是 gg 自我维护的"真闸门"

P8 EVOLUTIONARY IMPERATIVE 说"洞察必须沉淀回资产"——但它没说**怎么才算沉淀**。G5 补上了这一刀：**沉淀必须是物理的，对话不算**。

这两条原则现在是配套的：
- P8 说**必须沉淀**
- G5 说**沉淀必须物理化**

P8 + G5 才是闭环。之前只有 P8，是半闭环——我可以说"这个洞察我记住了"然后没写文件，下次会话丢失。G5 把这条漏洞堵上。

### 4. gg 的"宪法演化纪律"在自验证

constitution v0.1.0 → v0.2.0：v0.1.x 增补 G4 是 First Contact 的衍生（被动响应 Keith 的需求），v0.2.0 增补 G5 是设计模式对话的衍生（gg 主动提议吸收外部协议）。

**两次增补的共同点**：
- 都来自 Keith 触发的具体场景（不是 gg 凭空想到要加宪法）
- 都经过 Keith 明示批准
- 都做了完整辐射面同步

**两次增补的不同点**：
- G4 是"防止 gg 越界"（保护 Keith 的不可逆决策权）
- G5 是"防止 gg 自欺"（保护 gg 自身的诚实）

**结构性观察**：宪法的成长方向是**对位 Keith 害怕的失败模式**（错得自信 / 不可逆错误 / 内存自欺）。这是健康的——宪法不是为了"显得完备"，是为了**封堵已识别的具体失败模式**。

## 下次继续

### 未解决的问题
- **NEURAL-LINK 在 openclaw 那边的实战表现是否良好？** 如果不好，我对 G5 的"宪法级判断"可能过早。下次有机会问 Keith 或自己读 openclaw 的反思
- **G5 的实际触达率**：未来 1-2 次出场后，回头看 gg 是否在 ARCHIVE 步骤真的勾了 G5 自审清单。如果跳过率高 → G5 沉睡 → gg-audit 应该把 G5 加进"原则触达"维度

### 下次应该优先做的事
- **没有强制下次议题**。本次议题闭环
- 如果 Keith 未来的设计会话提到"协议吸收"或"外部 framework 借鉴"，主动调出 `PROTOCOL_HARVESTING` 候选模块的方法论

### 开放问题（未来某天再讨论）
- D4 的范围授权语义是否要写进 CLAUDE.md（见元洞察 §2）
- gg-audit 的"原则触达"维度要不要加 G5（gg-audit 当前的 6 维度里只有"原则触达"会管这条）
- `PROTOCOL_HARVESTING` 是否值得升级硬核心（≥2 次类似场景验证后再判断）

## 硬核心改动清单

本次设计会话修改了哪些硬核心文件？每一条都关联到 Keith 的明示批准：

- **改动 1**：`constitution.md` 新增 G5 PHYSICAL PERSISTENCE + 顶部描述更新 + 自审清单 + 元数据
  - **Keith 批准于**："你自己决定，不用再问我了"（针对 gg 提议的"L0 三条吸收 / 升级 G5"具体方案）
  - **批准范围解读**：覆盖 gg 在前文提议中明确列出的"分层吸收"路径（A 升 constitution G5 + D 进 tracks 观察）

辐射面同步（不属于硬核心，但跟硬核心改动绑定）：
- `memory/state.md`（meta）
- `memory/working_context.md`（meta）
- `tracks/cc.md`（软外围）
- `memory/design_sessions/2026-04-13_neural-link-evaluation.md`（本文件，软外围）

## 物理证据 (G5 自证)

每一处改动都已通过 Edit 工具返回 OK 的确认：

| # | 文件 | 改动 | 工具返回 |
|---|---|---|---|
| 1 | constitution.md | 加 G5 主体 | ✓ updated successfully |
| 2 | constitution.md | 顶部 "3 条" → "5 条" | ✓ updated successfully |
| 3 | constitution.md | 自审清单加 G5 + 例外 | ✓ updated successfully |
| 4 | constitution.md | 元数据 v0.2.0 + 增补记录 | ✓ updated successfully |
| 5 | memory/state.md | gates: 4 → 5 | ✓ updated successfully |
| 6 | memory/state.md | 变更日志加条目 | ✓ updated successfully |
| 7 | memory/working_context.md | 第 61 行 "8 原则+4 闸门" → "5 闸门" | ✓ updated (replace_all) |
| 8 | memory/working_context.md | 第 74 行表格 "+ 4 闸门" → "+ 5 闸门" | ✓ updated successfully |
| 9 | tracks/cc.md | 追加 NEURAL-LINK 评估段 + 候选模块 | ✓ updated successfully |
| 10 | memory/design_sessions/2026-04-13_neural-link-evaluation.md | 新建 | （本文件 Write 返回 OK 即满足） |

**这张表本身就是 G5 的最小执行模板**——以后所有硬核心改动结束时都应该列一份这样的物理证据表。
