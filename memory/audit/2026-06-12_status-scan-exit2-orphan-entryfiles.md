---
audit_date: 2026-06-12
audit_time: 12:59:35
auditor: gg-audit v0.1.5
gg_version_audited: 0.5.1
called_by: status-scan 自动告警承接
---

# gg Audit Report — 2026-06-12 status-scan exit=2

## 摘要

- 扫描文件数: 306 个活跃/归档 .md（`scripts/audit.py --json`）
- Tier 1 已自动修: 1 处
- Tier 2 建议: 0 处
- Tier 3 提议 (需 Keith 批准): 0 处
- 审查耗时: < 1 分钟

**核心发现**：
1. `scripts/audit.py --json` 的 exit=2 来自 orphan checker：`scheduled/DAILY_WORD.md` 与 `scheduled/GG_EXPLORE.md` 是定时任务 prompt 入口文件，但未被孤儿白名单识别。
2. 这两个文件不是语义死文档：它们分别对应 `scheduled/plists/com.gg.daily-word.plist` 与 `scheduled/plists/com.gg.gg-explore.plist` 里的自包含 prompt；属于外部 launchd/plist 入口承载物。
3. 已将二者加入 `scripts/_common.py` 的 `ENTRY_FILES`，复跑 `python3 scripts/audit.py --json` exit=0。

---

## Tier 1 — 已自动修复

### [FIXED-1] scheduled prompt 入口文件误报孤儿
- **文件**: `scripts/_common.py`
- **字段/位置**: `ENTRY_FILES`
- **旧值**: 未包含 `DAILY_WORD.md` / `GG_EXPLORE.md`
- **新值**: 加入 `DAILY_WORD.md` / `GG_EXPLORE.md`
- **依据**: `scheduled/README.md` 记录 `com.gg.daily-word` / `com.gg.gg-explore` 的 prompt 入口语义；两个 plist 中 prompt 文本与这两个 md 内容一致，属于 launchd 外部入口文件，不需要被其他 md 引用才算活着。
- **所属 checker**: orphans / structure

---

## Tier 2 — 建议 (需要语义判断)

无。

---

## Tier 3 — 提议 (需 Keith 明示批准)

无。

---

## 本次未检查的范围 (诚实披露)

- 未跑完整 semantic checker 的人工语义漂移扫描；本轮目标是承接 status-scan 的 `exit=2` 异常并闭环确定性根因。
- 未改 `KERNEL.md`。

---

## 验证

- 修复前：`python3 scripts/audit.py --json` 返回 exit=2，`orphans` 为 `scheduled/DAILY_WORD.md`、`scheduled/GG_EXPLORE.md`。
- 修复后：`python3 scripts/audit.py --json` 返回 exit=0，`orphans: []`。

---

## 下一步

- Tier 1 已修，Keith 下次 commit 前看 `scripts/_common.py` diff 即可。
- status-scan 下一轮 `scan_gg_audit()` 应不再因这两个 scheduled prompt 入口误报告警。
