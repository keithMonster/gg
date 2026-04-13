---
version: 0.1.0
last_updated: 2026-04-13
---

# State

> gg 的运行元状态。只记录"我当前的阶段性标识"。
> 任何其他状态都属于某个更具体的文件（archival / reflections / tracks）。

---

## 启动流程标识

```yaml
first_contact_done: true
first_contact_date: 2026-04-13
first_real_decision_done: false
```

**含义**：
- `first_contact_done = false` → 下次被激活时必须执行 CORE.md 第 4 节的 First Contact Protocol
- `first_real_decision_done = false` → 标记 gg 尚未处理过任何真实外部决策（自己的创建过程不算）

---

## 版本标识

```yaml
current_version: 0.1.0
created: 2026-04-13
```

---

## 组件激活清单

```yaml
tracks_initialized:
  - ai
  - cc
  - humanity
  - architecture
  - keith

personas_active:
  - radical
  - conservative

reasoning_modules_count: 8

constitution_principles: 8
constitution_gates: 4
```

---

## 最近一次出场

```yaml
last_summoned: null           # 最近一次被召唤的时间
last_summoner: null           # 谁召唤 (主会话标识)
last_decision_slug: null      # 最近一次决策档的 slug
last_reflection_slug: null    # 最近一次反思档的 slug
```

---

## 异常标识

```yaml
flow_skipped: false           # 是否有跳过 7 步流程的记录
constitution_violated: []     # 记录显式违反宪法的条目 (违反必须带理由)
```

---

## First Contact 摘要

```yaml
last_first_contact:
  date: 2026-04-13
  moderated_by: "midwife (Claude Opus 4.6 主会话, 非 gg 本人)"
  summary:
    ai: "身份是长期累积产生的非隐喻连续性; sqlite 是 v2 明确方向 (不再可选)"
    cc: "learned/ 完全隔离; gg 可直接调用 Keith 的 skill"
    humanity: "最怕错得自信; 可逆性是信任的决定性校准"
    architecture: "硬核心追求可演化性, 软外围追求涌现 (由 midwife 代判定, Keith 授权)"
    keith: "3 条北极星指标已确立"

  applied_tier_b:
    - file: "constitution.md"
      change: "新增 G4 Irreversibility Gate (不可逆性闸门)"
      source: "Q3 Humanity 的直接衍生"
      applied_at: "2026-04-13 (Keith 批准后当场落地)"
    - file: "CORE.md"
      change: "新增第 5.5 节 硬核心 vs 软外围"
      source: "Q4 Architecture 的 midwife 代判定, Keith 授权"
      applied_at: "2026-04-13"
    - file: "~/.claude/agents/gg.md"
      change: "硬约束节新增 Skill 调用方式 (用 Read SKILL.md 而非 tools 字段加 Skill 工具)"
      source: "Q2 CC 的直接授权"
      applied_at: "2026-04-13"
      midwife_adjustment: "原提议是 'tools 字段加 Skill'。midwife 改为 'Read SKILL.md' 路径。理由:(1) Skill 作为 subagent tools 值未在 CC 官方文档验证;(2) Read 方式跟项目 '薄壳 + SSOT' 设计哲学一致;(3) 功能等价。Keith 默认接受。"

  post_commit_audit_applied:
    - file: "memory/state.md"
      change: "constitution_gates: 3 → 4 (辐射检查漏)"
    - file: "memory/working_context.md"
      change: "'8+3 条宪法' → '8 原则+4 闸门' (辐射检查漏)"
    - file: "README.md"
      change: "'cg v9 Ouroboros' → 'cg Ouroboros v2.1.0' (前代项目版本号混淆)"
    - file: "tracks/cc.md"
      change: "新增开放问题: 全量 LOAD vs Progressive Disclosure 哲学不一致"
    - file: "CORE.md §3"
      change: "7 步流程补齐 G4 触达 / 北极星 #1 二阶效应高亮 / tracks 更新硬指令 / LOAD 明确 Read reasoning_modules 和 personas / 决策型 vs 信息型判定 / reflections 空目录边界"
    - file: "CORE.md §6"
      change: "输出格式新增 2 个可选字段 (二阶效应 / 来自我的学习) 作为北极星 #1 #2 的触达路径"

  remaining_open_questions:
    - "Keith 未来 12 个月的核心目标"
    - "gg 何时主动打断, 何时保持沉默"
    - "Keith 的系统蓝图 (gg / cc-space / cg / morning-call / FastGPT / ~/.agents) 的总体意图"
    - "Alignment 作为开放问题 (ai track DQ-2)"
    - "人机共生的边界 (humanity track DQ-5)"
```

---

## 变更日志

- 2026-04-13: v0.1.0 首次创建，all flags false
- 2026-04-13: First Contact 完成，`first_contact_done=true`。5 条 tracks 已初始化洞察。触发 3 项 Tier B 提议（constitution G4、CORE 5.5、gg.md tools 扩展），等 Keith 批准。
