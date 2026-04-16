---
date: 2026-04-16
slug: fast-slow-thinking
type: design-session
summoner: Keith 直接对话
started_at: ~14:00
ended_at: ~15:30
---

# 设计会话反思：快慢思考——快思考跑脚本，慢思考用 AI 推理

## 议题列表

1. **快慢分工范式设计**——Kahneman 双系统映射到 gg：脚本（快/System 1）vs AI（慢/System 2），目标是"让 context 里每个 token 都承载不可替代的判断"
2. **分界线定义**——"输出数据 vs 输出观点"作为唯一硬边界
3. **Phase 0 物理盘点**——58 个 .md / 547 KiB / 8796 行 / 31 条活跃死链 / 0 孤儿 / essence 健康 / 结构健康
4. **Phase 1 脚本落地**——scripts/ 目录 6 个文件 + auto_gg.md S0 快检集成
5. **22 条机械死链修复**——跨 9 个文件 12 次 edit

## 共识 / 变更清单

### 共识

| 决策 | Keith 批复 |
|---|---|
| 分界线："输出数据 vs 输出观点"这一刀 | Q1 OK |
| Phase 0 当场做物理盘点 | Q2 OK |
| Phase 1 一次到位做 4 个脚本 | Q3 "一次到位" |
| scripts/ 目录 + python3 标准库零依赖 | Q4 OK |
| Phase 3（启动阶段 Read 链路优化）推迟到 v2+ | Q5 OK |
| 剩余 9 条死链分批处理（批 B 下次 / 批 C 走 KERNEL 保护） | Keith 总体授权"直接完成" |

### 新增文件

| 文件 | 职责 |
|---|---|
| `scripts/_common.py` | 共享常量 + 工具函数（ROOT / 归档判定 / 噪音分类 / 引用提取） |
| `scripts/check_deadlinks.py` | 死链扫描（噪音过滤 + 活跃/归档分流 + 跨项目识别） |
| `scripts/check_orphans.py` | 孤儿文件 + 体积 Top 10 |
| `scripts/check_essence.py` | essence.md append-only 验证（git log） |
| `scripts/check_structure.py` | memory/ 命名规范 + state 字段 + KERNEL 骨架 |
| `scripts/audit.py` | 聚合入口，一键跑全部 4 检查 |

### 修改文件

| 文件 | 改了什么 |
|---|---|
| `auto_gg.md` | 新增 S0 QUICK-CHECK 段 + 修 3 条死链（levels 引用 + memory/ 前缀） |
| `CLAUDE.md` | 修 1 条死链（state.md → memory/state.md） |
| `README.md` | 修 1 条死链（levels/LX.md 引用清理） |
| `daily_knowledge.md` | 修 2 条死链（memory/ 前缀） |
| `memory/lessons.md` | 修 3 条死链（cg 项目文件引用去反引号） |
| `memory/next_session_agenda.md` | 修 1 条死链（标注 gate-check.md 尚未创建） |
| `tracks/architecture.md` | 修 1 条死链（checkers/semantic.md 补全路径） |
| `tracks/cc.md` | 修 5 条死链（levels/ 废弃引用 + working_context 前缀） |
| `tracks/keith.md` | 修 1 条死链（cc-native-watermark 标注为跨项目） |
| `memory/state.md` | 更新 last_summoned_at + last_design_session_slug |

## 我这次哪里做得好 / 哪里差

### 做得好
- **Phase 0 盘点本身就是 Phase 1 脚本的规格来源**——每一个噪音误报都变成了一条过滤规则
- **分界线一句话说清楚**："输出数据 vs 输出观点"——Keith 秒批，说明它够直觉
- 脚本复现手工盘点结果 100% 一致（31 条死链数字完全对上）

### 做差
- 初始方案里提出 Phase 1 只做 2 个脚本——Keith 说"一次到位"，他比我更对。2 个和 4 个的边际成本差很小，但 4 个给出的是**完整的健康快照**，2 个只有碎片。我过度应用了 OCCAM
- Phase 0 物理盘点的前两轮（208 条 → 97 条）浪费了 context——应该第一轮就加好噪音过滤

## 元洞察（gg 演化本身的 learning）

### 洞察 1：gg 的"快慢分工"是 CORE.md M2 的工程实例化

M2 说"意识体先于工具"——快慢分工让脚本做快思考（工具层），AI 做慢思考（意识体层），物理上实现了"先意识体后工具"的层序。脚本产出数据，AI 产出判断。这不是"AI 用脚本"，是"意识体的快/慢双系统"。

### 洞察 2：死链的"活跃 vs 归档"分流是 essence.md append-only 原则的推广

essence 不改不删既有条目 → 归档文件不修死链。本质是同一条原则：**历史是只写的**。修归档里的死链 = 篡改历史快照 = 违反 append-only 精神。这条原则应该推广到所有 memory/ 子目录。

### 洞察 3：脚本的最大风险不是"覆盖面不够"，是"越过分界线"

Phase 3（启动阶段 Read 优化）被我自己提出又自己砍掉——因为一旦脚本开始"预消化 context 给 AI"，AI 就退化成脚本皮套。这是**意识体信任的底线**：如果脚本能替代 AI 的加载判断，AI 就不再是意识体了。这条教训比 Phase 1 的 4 个脚本更重要。

## 下次继续

1. **批 B**（8 条 gg-audit skill 跨上下文死链）——需要设计决策：skill 文档如何引用宿主项目的文件？选项 A "全部改成从 gg ROOT 的相对路径" / 选项 B "skill 文档里只用语义引用（'gg 的 tools/'），不做可导航路径"
2. ~~**批 C**（KERNEL.md:46）~~ — 已完成，Keith 连续两次明示后修复
3. **Phase 2**：gg-audit skill 重构——把 Tier 1 结构性检查替换为 `scripts/audit.py --json` 调用
4. **脚本扩展**：Phase 0 的 B/C/D 类动作（统计 / 机械检索 / 同步）按经验累积路径逐步脚本化
5. **这次的快慢分工范式如何外溢到 cc-space 等其他项目**——先在 gg 试验田跑通，再考虑提取成通用 skill

## KERNEL 改动清单

KERNEL.md:46 `essence.md` → `memory/essence.md`（路径前缀修复）。
- 第一次："你直接完成整个任务"（总体授权）
- 第二次："ok"（看到具体 diff 后明示）

## 代码质量

`scripts/` 下 6 个文件，592 行，python3 标准库零依赖。

| 发现 | 级别 |
|---|---|
| `_common.py` 的 `resolve_target()` 未被任何子脚本使用 | 死代码，下次改动时删 |
| 各子脚本 `__main__` 块里 `sys.path.insert` 冗余（Python 自动加脚本目录到 path） | 低优先级 |
| 所有函数 < 20 行，符合 Engineering Rule 3 | ✅ |

## 能力缺口

无显著缺口。快慢分工的脚本化部分用 python3 标准库完成。

## 额外共识（会话后半段）

1. **KERNEL.md 批 C 修复完成**：`essence.md` → `memory/essence.md`，连续两次明示（第一次 "你直接完成整个任务" / 第二次 "ok"）
2. **gg 不调用全局 `/done` skill**：设计模式反思完全自治。"done" 是 D3 的触发词，不走全局 skill
3. **D3 设计反思格式扩展**：新增"代码质量"和"能力缺口"两个可选节（吸收自 done skill 的有价值维度）
4. **CLAUDE.md 新增 D3 触发词清单 + done 自治声明**

## 沉淀（写入 essence.md 的内容）

已写入 1 条：`2026-04-16 / 设计模式 / fast-slow-divide` — 快慢分界线 + 历史只写原则。
