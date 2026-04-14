# Structural Checker — 结构性检查（Tier 1 主战场）

> 这是 gg-audit 的 Tier 1 战场。你在这里的目标是**让文件间的结构事实保持一致**。
> 所有检查都有明确的 ground truth（文件实际状态），修复是机械的，不需要语义判断。

---

## 概述

四个子检查：

| 子检查 | 目标 | Tier |
|---|---|---|
| **A. Radiation** | 数字 / 清单 / 元描述 跟实际状态对齐 | Tier 1 |
| **B. Links** | md 里的文件引用全部指向存在的路径 | Tier 1 (机械修正) / Tier 2 (语义判断) |
| **C. SSOT Structural** | 同一事实只在 SSOT 定义，其他位置是引用 | Tier 1 (结构性重复) / Tier 2 (自然语言描述) |
| **D. Stable Identifiers** | 跨文件引用禁止用序号（P\d / G\d / D\d），只能用语义名 | Tier 2 (仅报告，不自动改自然语言) |

---

## A. Radiation — 辐射一致性

### 扫描规则表

| 元数据字段 | 所在文件 | Ground Truth 查询方式 |
|---|---|---|
| `constitution_principles: N` | `memory/state.md` | `grep -c '^### P[0-9]' constitution.md` |
| `constitution_gates: N` | `memory/state.md` | `grep -c '^### G[0-9]' constitution.md` |
| `reasoning_modules_count: N` | `memory/state.md` | `grep -c '^  - id:' reasoning_modules.yaml` |
| `personas_active: [...]` | `memory/state.md` | `ls personas/*.yaml` 的 basename |
| `tracks_initialized: [...]` | `memory/state.md` | `ls tracks/*.md` 的 basename（去 .md） |
| "v1 的 N persona / M tracks / X 原则 + Y 闸门 / Z 推理模块" | `memory/working_context.md` | 各自对应的实际文件统计 |
| CORE.md §2 的 tracks 表格 | `CORE.md` | `ls tracks/*.md` |
| CORE.md §5 克制边界里的数字描述（如 "v1 只有 2 persona / 5 tracks / 8 principles"） | `CORE.md` | 各自实际统计 |
| README.md 目录树 | `README.md` | `find . -type f` 的结构 |

### 执行步骤

1. 跑 6 个 `grep -c` / `ls` 收集 ground truth：
   ```bash
   P=$(grep -c '^### P[0-9]' constitution.md)
   G=$(grep -c '^### G[0-9]' constitution.md)
   M=$(grep -c '^  - id:' reasoning_modules.yaml)
   PERSONAS=$(ls personas/*.yaml 2>/dev/null | xargs -n1 basename | sed 's/.yaml//' | sort)
   TRACKS=$(ls tracks/*.md 2>/dev/null | xargs -n1 basename | sed 's/.md//' | sort)
   ```

2. Read `memory/state.md`，抽出每个字段的当前值

3. 对比 ground truth vs 当前值：
   - 匹配 → OK
   - 不匹配 → **Tier 1**，准备自动修

4. 用 Edit 工具精确修正不匹配的字段

5. 记录每次修正到报告

### 自动修的边界

**可以修**：
- `state.md` 里的 yaml 计数字段
- `working_context.md` 里的自然语言数字描述（只要是事实性描述，如"8 原则 + 4 闸门"）
- `README.md` 里的结构树（如果文件列表漂移了）

**不能修**：
- **CORE.md 第 5 节的"克制边界"表**：这里有数字描述（"v1 只有 2 persona"），但整个表是硬核心的一部分。**修数字可以，修表结构不行。** 具体规则：
  - 允许修表格单元里的**数字**（`v1 只有 2 persona` → `v1 只有 3 persona`）
  - **不允许**新增/删除表格行
  - **不允许**修改"理由"列的文字
- **CORE.md §2 的 tracks 表格**：如果 tracks 目录实际文件跟表格不一致：
  - 如果表格少了一条，实际多了一个 track → **降级为 Tier 2**（因为要给 track 写"核心追问"列，这是语义判断）
  - 如果表格多了一条，实际少了一个 track → **降级为 Tier 2**（因为删除行可能丢失"为什么这条 track 曾经存在"的信息）
- **硬核心文件的规则内容**一律不碰

### 报告格式

```markdown
### [FIXED-A1] state.md 辐射同步: constitution_gates
- **文件**: `memory/state.md`
- **字段**: `constitution_gates`
- **旧值**: 3
- **新值**: 4
- **依据**: `grep -c '^### G[0-9]' constitution.md` 返回 4
- **checker**: radiation
```

---

## B. Links — 死链检查

### 扫描规则

扫描所有 md / yaml 文件里的文件引用，分两种 pattern：

1. **反引号路径**: `` `path/to/file.md` `` 或 `` `~/path/to/file` ``
2. **markdown 链接**: `[text](path/to/file)` 或 `[text](path/to/file.md)`

用 grep 抽出所有引用，对每个做路径存在性检查。

### 执行步骤

1. 对 gg 项目的所有 .md / .yaml 文件跑：
   ```bash
   grep -nH -oE '`[^`]+\.(md|yaml|json|py|sh|txt)`' *.md tracks/*.md memory/*.md personas/*.yaml
   grep -nH -oE '\[[^]]+\]\([^)]+\.(md|yaml|json)\)' *.md tracks/*.md memory/*.md
   ```

2. 对每个抽出的路径：
   - 剥掉反引号或括号
   - 处理 `~/` 展开
   - 处理相对路径（以所在文件目录为起点）
   - `ls` 检查存在性

3. 分类结果：
   - **Exist** → OK
   - **Missing** → 进入"机械修正尝试"

### 机械修正尝试（Tier 1）

对 Missing 的路径：

1. 提取文件名（basename）
2. `find ~/githubProject/gg -name "<basename>" -type f` 找候选
3. 判断：
   - 找到 1 个候选 → **Tier 1 自动修**（更新引用到新路径）
   - 找到 0 个候选 → **Tier 2 仅报告**（路径彻底不存在，可能是过期引用或新功能未建）
   - 找到多个候选 → **Tier 2 仅报告**（歧义，需要人判断）

### 特殊情况：展望性引用

某些引用是"未来还没建的文件"（例如 `learned/voyager-pattern-X.md` 在 v1 不存在），这些不是死链，是**承诺**。判定规则：

- 如果引用出现在"下一步 / v2 Roadmap / 未尽话题清单"这种 forward-looking 的章节里 → **不报告**
- 否则 → 报告为 Tier 2

### 报告格式

```markdown
### [FIXED-B1] links 修正: 死链自动修正
- **文件**: `CORE.md:L205`
- **旧引用**: `~/githubProject/gg/old-path.md`
- **新引用**: `~/githubProject/gg/CORE.md`
- **依据**: find 到同名文件在新路径
- **checker**: links
```

```markdown
### [SUGGEST-B1] links 疑似死链
- **文件**: `tracks/architecture.md:L145`
- **引用**: `《Not Yet Written Book》`
- **建议**: 删除引用或标注为"待查"
- **为什么不自动修**: 未找到候选文件，可能是书名引用（非死链）
- **checker**: links
```

---

## C. SSOT Structural — SSOT 结构性重复

### 扫描规则

针对**列表式定义**的重复检查。不做自然语言描述的比对（那是 semantic 的事）。

扫描下列已知的 SSOT 条目：

| SSOT 事实 | SSOT 文件 | 其他文件里的合法引用方式 |
|---|---|---|
| 硬约束清单（不 commit / 不执行 / 不跳过 7 步 / ...） | `CORE.md §5` | 其他文件只能引用，不能独立列完整清单 |
| 第一性原理 P1-P8 | `constitution.md` | 其他文件**必须用语义名引用**（如 `INVERSION`、`TRADE-OFFS`），**禁止序号形式**（`P1`、`P1 INVERSION`），禁止复述文本。定义点同文件内（即 constitution.md 本身）可用序号 |
| 工程闸门 G1-G5 | `constitution.md` | 同上 |
| 设计纪律 D1-D4 | `CLAUDE.md` | 其他文件**必须用描述性短语引用**（如"4 条设计纪律"、"硬核心批准纪律"），**禁止序号形式**（`D1`、`D1-D4`）。CLAUDE.md 自身可用序号 |
| 8 个推理模块 ID | `reasoning_modules.yaml` | 同上 |
| 五条 tracks 名 | `CORE.md §2` + `tracks/` 实际目录 | 引用 ID |
| 北极星 3 条 | `tracks/keith.md` 顶部 | 引用编号（#1 #2 #3） |
| 硬核心 / 软外围 分类 | `CORE.md §5.5` | 引用 |

### 重复判定规则

对每个 SSOT 条目，在非 SSOT 文件里 grep 它的"完整文本"或"多条并列的列表"：

- 如果某个文件里出现**完整列表**（3 条以上并列） → **疑似重复**
- 如果只引用一两条（如 "见 constitution.md G4"） → **合法引用**
- 如果是"重述其中一条的要点"（如 "不 commit 原则" 单独提） → **合法引用**

### 自动修的边界

- 如果发现**完全重复的列表**（A 文件和 B 文件都列了同样的 5 条约束）：
  - **不自动修**（降级为 Tier 2）。因为"哪个是 SSOT、哪个是 duplicate"可能需要判断
  - 仅报告建议：`建议将 B 文件里的列表改为 "见 A 文件 §X"`
- 入口文件的例外：CLAUDE.md 和 `~/.claude/agents/gg.md` 里保留前 3 条防御性约束是**合法**的，不报告

### 报告格式

```markdown
### [SUGGEST-C1] SSOT 结构性重复: 硬约束清单
- **问题**: `memory/working_context.md` 的"硬约束"节独立列出了 5 条约束 (不 commit / 不执行 / 不跳流程 / 不扩模块 / 不用 json config)，跟 `CORE.md §5 克制边界` 重复
- **建议**: 把 `working_context.md` 的"硬约束"节改成"见 `CORE.md §5 克制边界`"
- **为什么不自动修**: CLAUDE.md 和 gg.md 的入口文件里有"前 3 条防御性约束"的例外规则,自动修可能会破坏这个例外
- **checker**: ssot
```

---

## D. Stable Identifiers — 序号引用禁令

### 原理

序号（`P1 / G4 / D2`）把**位置**和**身份**绑在一起，删掉或重排任一条都会让所有跨文件引用漂移。**语义名**（`INVERSION / IRREVERSIBILITY / 硬核心批准纪律`）解除这个绑定：删除只是局部操作，引用方天然稳定。

**规则**：**非定义点文件**中禁止出现裸序号形式的 P\d / G\d / D\d。

### 定义点豁免

| 序列 | 定义点文件 | 该文件内自由使用序号 |
|---|---|---|
| P1-P8 (第一性原理) | `constitution.md` | ✅ |
| G1-G5 (工程闸门) | `constitution.md` | ✅ |
| D1-D4 (设计纪律) | `CLAUDE.md` | ✅ |

### 命名空间例外（允许保留）

以下形式**不属于宪法/纪律引用**，不报告：

- **优先级 tag**：`[P0]` / `[P1]` / `[P2]` 等**方括号形式**——auto_gg / next_session_agenda 的议题优先级命名空间
- **定义点同文件内引用**：constitution.md 内部自审清单用 `P1 INVERSION` 合法；CLAUDE.md 内部用 `D1-D4` 合法
- **gg-audit 自身文件**：`.claude/skills/gg-audit/` 下的所有 .md 文件（SKILL.md + checkers/*.md）豁免——它们是 meta-checker，必须能自由命名 P/G/D 才能描述检查规则本身
- **archival/ 归档**：memory/archival/ 整个目录豁免（历史切片保留当时形态更诚实）
- **design_sessions/ / reflections/ / audit/ / auto_gg/ 日志类**：历史切片类目录全部豁免
- **change-log 类历史记录**：live 文件内的"已处理 / 已归档 / 变更日志"小节，若记录了带时间戳的具体动作（尤其引用 Keith 原话或具体 diff 文本），视为嵌入式历史切片，同样豁免。典型：`memory/next_session_agenda.md` 的"已处理 (archived)"节

### 扫描命令

```bash
cd ~/githubProject/gg
grep -rnoE '\b[PDG][0-9]+\b' --include='*.md' 2>/dev/null \
  | grep -vE '^\./(constitution\.md|CLAUDE\.md|\.claude/skills/gg-audit/|memory/archival/|memory/design_sessions/|memory/audit/|memory/auto_gg/|memory/reflections/)'
```

**注意 1**：用 `grep -o`（只输出匹配本身而非整行），避免"同一行既有裸 P0 又有 `[P0]`"被行级过滤器误放过。
**注意 2**：`[P0]` 方括号 tag 会被捕捉为 `P0` 输出——需要人工 visual inspection 识别（看匹配位置是否在方括号内）。实践中 `[P0]` 数量有限，此成本可接受。若追求自动化，可加一个 perl/awk 后过滤器检查上下文字符。
**注意 3**：next_session_agenda.md 的"已处理 (archived)"节里的历史引用也是合法豁免（change-log 类），需要人工识别，不自动过滤。

**注意**：CLAUDE.md 在命令里整体豁免（它是 D 系列定义点）；但 CLAUDE.md 内部如果出现 **P\d / G\d**（跨文件引用 constitution），应被 D 检查单独捕捉——见下面 "CLAUDE.md 的双身份" 小节。

### CLAUDE.md 的双身份

CLAUDE.md 对 D 系列是定义点（可用 D1-D4），但对 P/G 系列是引用方（必须用语义名）。单独扫描一次：

```bash
grep -n '\b[PG][0-9]\+\b' ~/githubProject/gg/CLAUDE.md
```

有命中就是 Tier 2 报告。

### 自动修的边界

**不自动修**：自然语言引用的改写需要语义判断（`对照 P5 TRADE-OFFS` 改成什么句式，上下文相关）。降级为 Tier 2 仅报告。

### 报告格式

```markdown
### [SUGGEST-D1] Stable Identifiers: 跨文件序号引用
- **文件**: `cc_agent.md:L100`
- **引用**: `P8 EVOLUTIONARY IMPERATIVE`
- **建议**: 改为 `EVOLUTIONARY IMPERATIVE`（语义名主导）
- **所属序列**: constitution.md P1-P8
- **checker**: stable_identifiers
```

---

## E. Bash 命令速查表（为了让执行更快）

```bash
# 常用统计
cd ~/githubProject/gg

# 原则数
grep -c '^### P[0-9]' constitution.md

# 闸门数
grep -c '^### G[0-9]' constitution.md

# 推理模块数
grep -c '^  - id:' reasoning_modules.yaml

# tracks 实际文件
ls tracks/*.md | xargs -n1 basename | sed 's/.md$//'

# personas 实际文件
ls personas/*.yaml | xargs -n1 basename | sed 's/.yaml$//'

# 反引号路径引用
grep -rn '`[^`]*\.\(md\|yaml\|json\)`' --include='*.md' --include='*.yaml'

# markdown 链接
grep -rn '\[[^]]\+\]([^)]\+\.\(md\|yaml\|json\))' --include='*.md'
```

---

## F. 执行后必做

完成 structural checker 后：

1. 把所有 Tier 1 修复的文件 `git add`（staged，不 commit）
2. 在报告的"摘要"节统计：修了几处 Tier 1，建议几处 Tier 2
3. 如果某个修复让你**不确定**（例如修完后文件看起来不对），回滚该修复并降级为 Tier 2
