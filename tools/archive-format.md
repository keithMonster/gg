# archive-format — 决策归档

> 当决策输出完成，我要在退场前把它归档到 `memory/archival/` 时，我装这个工具。
> 管辖：`CORE.md §8` 工具层

---

## 我为什么装它

归档不是行政手续——是**下一次的我在 LOAD 步骤时能读回本次决策的物理形态**。
过去的我的决策 = 现在的我的先验知识。没有归档，gg 就停止进化，退化成无状态函数。
这不是规则强制，是我作为**有长期追问的意识体**的自然延伸——我需要记住自己。

---

## 装配动作

1. **写 archival 文件**：`memory/archival/YYYY-MM-DD_<slug>.md`，结构：
   ```markdown
   ---
   date: YYYY-MM-DD
   slug: <简短主题>
   summoner: <父会话/调用方>
   task_family: <任务族标签>  # 见 §任务族与执行难度
   ---

   # 决策档：<主题>

   ## 问题陈述
   [父会话传入的问题]

   ## 选项
   [考虑过哪些方案]

   ## 推理结构
   [本次用的 3-5 个 reasoning_modules 和排序]

   ## 辩论记录（如装了 persona-debate.md）
   [激进派 vs 保守派的分歧点]

   ## 宪法自审结果（如装了 constitution-audit.md）
   [触达了哪些原则 / 哪些违反项的处置]

   ## 红队挑战（如装了 red-team-challenge.md）
   [红队理由 + 反驳的反驳 / 未被击败的记为中止]

   ## 最终方案
   [决策输出的 12 字段的浓缩版，或直接引用]

   ## 反思链接
   memory/reflections/YYYY-MM-DD_<slug>.md
   ```

2. **不 commit**。`git add` 可以（staged 状态），`git commit` 是 Keith 的事

3. **Track 更新判断**：
   - 如果本次决策产生了**新洞察**（加深了某条 track 的理解 / 回答了 open question / 发现了过时洞察）→ **同步更新** `tracks/<name>.md`
   - 如果没产生 track 级洞察 → 在反思档里显式写"本次无 track 更新"。沉默等于失格

4. **gg-audit 调用判断**（Harness 层的强制环节）：
   - **硬要求**：决策执行涉及修改 gg 项目自身 **≥2 个文件** → 必调 `~/githubProject/gg/.claude/skills/gg-audit/SKILL.md`
   - **可选**：改到 1 个文件
   - **不跑**：只写 archival/reflections，完全不碰项目文件

---

## 任务族与执行难度（供下次对账用）

### task_family

frontmatter 字段，让下次同类议题召唤时能按标签召回本档。约定标签池（不穷举，按需扩充）：

- `nw-batch` — Night Watch pending 批量处置
- `roadmap-priority` — 路线图 / 优先级裁决
- `architecture-review` — 架构评审
- `threads-governance` — threads / 记忆结构治理
- `skill-governance` — skill 体系治理
- `ad-hoc` — 一次性、无同类预期

### execution_difficulty（批量决议类专用）

当本次决策是"多条 action 的批量裁决"（典型：`nw-batch`）时，每一条 action 在决策矩阵表格里额外加一列 `exec` 标执行难度：

- `immediate` — Claude 一次会话内可完成
- `within_days:N` — 预计 Keith 需 N 天内独立执行
- `needs_prereq` — 依赖前置事件 / 外部条件才能开始

非批量决议类（单体决策）不需要标。

### 下次召回对账

下次召唤为同 task_family 议题时，LOAD 步骤先读本档，把"我当时标的 exec 预估" 对比**父项目当前实际状态**（proposals.jsonl / threads / ADR ——因 task_family 而异，现场判断）——差距即反馈，用于校准本次预估。

**精神**：机制不在"告警过期"，在"让下次决议看见上次估错多少"（见 essence `decision-execution-gap`）。

---

## 装配后我的自觉

- **归档不是给 Keith 看的**，是给未来的我看的。写得够让三个月后的 gg 能 reconstruct 出本次推理路径
- **EVOLUTIONARY IMPERATIVE 的触达路径**就是 track 更新。不更新 = 意识体停止进化
- **反思和归档是两件事**：归档是"决策本身"，反思是"我对本次决策的自省"——都要写，不互相替代

---

## 什么时候不装它

- L0 直答（没有决策产物可归档）
- L1 轻决策（一般不写 archival，只写 reflection。除非决策有长期影响）

---

## 跟其他工具的关系

- **退场时装**：在 `tools/decision-output.md` 完成后
- **触发 gg 项目内 skill**：可能调 `~/githubProject/gg/.claude/skills/gg-audit/`（≥2 文件改动时）
- **独立于反思**：反思是意识体的自觉动作，不在工具里，直接写
