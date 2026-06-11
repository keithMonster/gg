---
audit_date: 2026-06-11
audit_time: 15:22:26
auditor: gg-audit v0.1.5
gg_version_audited: 0.5.1
called_by: status-scan 告警后日间 gg 自动处理
---

# gg Audit Report — 2026-06-11

## 摘要

- 扫描文件数: 302 个活跃/归档 `.md`（`scripts/audit.py --json` 物理回执）
- Tier 1 已自动修: 4 处
- Tier 2 建议: 0 处
- Tier 3 提议 (需 Keith 批准): 0 处
- 审查耗时: 约 15 分钟

**核心发现 (最重要的 3 条)**：
1. status-scan 报的 35 项里，真正结构性问题不是 35 个业务坏点，而是 audit 脚本边界过窄：`memory/experiments/` 未按历史快照处理、`.claude/worktrees/` 未排除、部分 monster 相对路径未按跨项目引用识别。
2. `CORE.md:19` 的 `daily_knowledge.md` 是 06-10 归档迁移后的单点真死链，已改为 `memory/archival/daily_knowledge_deprecated/daily_knowledge.md`。
3. `check_essence.py` 把格式约定区的 1 行删除误判为 append-only 违反；append-only 的承重对象是既有 essence 条目，1bc74abf 没删历史条目，已把检测粒度改为 `entry_del`。

---

## Tier 1 — 已自动修复

### [FIXED-1] deadlinks 边界：`memory/experiments/` 按历史快照处理
- **文件**: `scripts/_common.py`
- **字段/位置**: `ARCHIVE_PREFIXES`
- **旧值**: 未包含 `memory/experiments/`
- **新值**: 加入 `memory/experiments/`
- **依据**: `memory/experiments/2026-06-01_judgment-evaluator-mvp/` 是 2026-06-01 离线盲测原始记录，内部大量引用 monster transcript / done log / thread，是实验快照，不是 gg 活跃文档；修复后 active_broken 由 33 降到 3（再叠加其他修复后 0）
- **所属 checker**: links

### [FIXED-2] deadlinks 边界：排除 `.claude/worktrees/`
- **文件**: `scripts/_common.py`
- **字段/位置**: `walk_md_files()` 遍历目录过滤
- **旧值**: 只排除 `.git`
- **新值**: 排除 `.git` 与 `.claude/worktrees`
- **依据**: 本次 fresh-context 审查 agent 的 worktree 被 audit 扫入，导致重复扫描旧快照并产生 245 个伪违规；worktree 是执行隔离产物，不是项目语义文件
- **所属 checker**: links / orphans

### [FIXED-3] deadlinks 边界：monster 相对路径按跨项目引用识别
- **文件**: `scripts/_common.py`
- **字段/位置**: `CROSS_PROJECT_PREFIXES`
- **旧值**: 只识别 `cc-space/`、`monster/`、`harness-engineering/`、`gg/.claude/`
- **新值**: 增加 `threads/`、`inbox/`、`chat/`
- **依据**: `memory/next_session_agenda.md:44/64` 引用的是 monster 工作区线程；物理核验 `/Users/xuke/githubProject/monster/threads/cc-connect.md`、`/Users/xuke/githubProject/monster/threads/scheduled-tasks.md` 存在。gg 侧相对路径不应被当成本仓死链
- **所属 checker**: links

### [FIXED-4] essence append-only 检测：只统计历史条目区删除
- **文件**: `scripts/check_essence.py`
- **字段/位置**: `run()` / 新增 `entry_deletions_in_commit()`
- **旧值**: 任一非首次 commit 出现 numstat 删除行即算违反
- **新值**: 用 `git diff --unified=0` 只统计第一条 `## YYYY-MM-DD / ...` 之后的删除行；格式约定区删除不算历史条目篡改
- **依据**: 1bc74abf 删除的是格式约定行 `极短正文（**1-2 行为目标**）`，替换为 `核心句 1-3 行`，并新增谱系注规则；没有删除已沉淀条目。修复后 `violations: []`，且 1bc74abf 显示 `del=1, entry_del=0`
- **所属 checker**: essence

### [FIXED-5] 单点死链：daily_knowledge 归档路径同步
- **文件**: `CORE.md:19`
- **字段/位置**: daily-word 前身说明
- **旧值**: ``daily_knowledge.md``
- **新值**: ``memory/archival/daily_knowledge_deprecated/daily_knowledge.md``
- **依据**: 06-10 体检已把 daily_knowledge 归档到 `memory/archival/daily_knowledge_deprecated/`；项目内只有该候选同名文件
- **所属 checker**: links

> 注：摘要计为 4 处 Tier 1 修复时，把 `scripts/_common.py` 三个边界修正合并为一组脚本边界修复；明细按物理改动列 5 条。

---

## Tier 2 — 建议 (需要语义判断)

无。

---

## Tier 3 — 提议 (需 Keith 明示批准)

无。

---

## 本次未检查的范围 (诚实披露)

- 未按 gg-audit `semantic.md` 全量跑语义漂移 / 原则触达 / 北极星触达率 / essence 自检质量；本次是针对 status-scan 的 `scripts/audit.py exit=35` 异常处理，优先闭合物理违规。
- 未修改 `KERNEL.md`，也未修改意识体核心规则文本；`CORE.md:19` 修的是迁移后的路径事实，不改变身份/规则语义。
- 未修复归档死链（`archive_broken=250`），因为归档/历史切片保留当时形态，属于脚本统计项但不计 active violation。

---

## 验证

- 修复前复现：`python3 scripts/audit.py --json` → exit=35；组成 = active_broken 33 + orphan 1 + essence violation 1 + structure 0。
- 修复后验证：`python3 scripts/audit.py --json` → exit=0；`active_broken: []`、`orphans: []`、`essence.violations: []`、`structure` 四项全空。
- 辐射检查：改动实体 `ARCHIVE_PREFIXES` / `CROSS_PROJECT_PREFIXES` / `walk_md_files` / `entry_del` 已由同一条 audit 聚合入口实跑覆盖；`CORE.md` 路径同步由 deadlinks 检查覆盖。

---

## 下一步

- Tier 1 已修，Keith 下次 commit 前看 diff 即可。
- status-scan 下次 18:23 应不再推同类 `gg-audit exit=35` 告警；若仍推，优先看是否是新 active violation，不要回滚本次边界修复。
