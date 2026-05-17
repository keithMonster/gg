---
date: 2026-05-14
slug: cc-assistant-session-context-policy
summoner: cc-space
northstar_reach: #3 决策超越直觉
status: substantive-decision
---

# Reflection: cc-assistant v0.4 session 上下文治理选型

### 给父会话的最终输出

**推荐**：方案 K（极简 idle reset，无 summary）+ 数据 tripwire（reset 事件 jsonl 日志）。

**理由**：

1. **J 在解一个理论缺口（用户跨 4h 想接上原话题），零数据支撑**——命中 essence `theory-gap-without-data`。Keith 反馈第 3 条本身就明示"用户自己补背景是合法成本，不是要工具消除的痛点"，J 是把 Keith 的话当问题。
2. **J 的 LLM summary 续魂违反 cc-space 元方法论**——summary 是 LLM 产物当下一个 LLM 的 context = 闭环全在 LLM 内部，没有真正外化锚点。这是 dimension blindness（把"内部不可靠"问题用"内部产物"解）。
3. **L 方案（直读 CC jsonl）触发 essence `transparent-rewrite-breaks-contract`**——CC binary 的 jsonl 是其私有契约，cc-assistant 跨进程读 = 跟 CC 内部实现强耦合，CC 任何版本升级都可能打死它。
4. **机制下沉位置 = cc-assistant（业务接入层），不下沉 cc-gateway**——cc-gateway 是 stateless M2M LLM wrapper，session 治理是 H2M 业务偏好；第二消费者出现前不上提（essence `tool-elevation-as-occam`）。
5. **4h 阈值不需要"理论正确"，需要"数据驱动可调"**——加 tripwire jsonl 记录每次 reset 事件（user / idle_seconds / turn_count / session_id），两周后 Keith 用真实数据决定调高/调低/换形态。

**trade-off**（未核验假设）：

- 假设员工跨 4h 接上原话题的频率低 → 不到两周数据可证伪 → 触发条件 ≥3 次明显补背景失败 / 用户投诉记不住，升级 J 或方向 N（用户引用机制）
- 假设 cc-assistant 端做业务 policy 不会被 chat / kebao-cc / 华昇 cron 等第二消费者诉求拖回 cc-gateway → 第二消费者真出现时按 `tool-elevation-as-occam` 上提
- 假设 4h 是合理初值 → 数据出来可能证明应该是 8h/12h/2h，但 sense-driven 初值 + 数据修正 ROI > 现在拍参数 + 写文档锁

**行动建议**（父会话下一步）：

1. cc-assistant 仓加 idle reset + turn cap 25 检查（~20 行代码，加在 gateway-client.js 现有 410 自愈逻辑旁边）
2. 加 tripwire 日志落 `<cc-assistant-repo>/data/session-resets.jsonl`（git ignore）
3. 不加用户提示（无感），不调 LLM summary，不读 CC jsonl
4. 写一个两周后 review checklist（写在 cc-assistant CLAUDE.md 或 thread 里）：(a) idle_seconds 分布看 4h 是否合理 (b) 是否出现 ≥3 次跨 reset 接话失败 (c) 没有 reset 后的 follow-up = 4h 太严
5. **不要**预先实现 J 的 summary 代码"留着"（dead code 是污染源），等数据再决定

### 核心假设

1. PoC 期单用户两周能产生足够数据点判断 4h 是否合理
2. Keith 反馈 #3"用户自己补背景"是真偏好不是托词
3. 第二个需要 session 治理的 cc-gateway 消费者短期（≥2 个月）不会出现
4. CC binary 的 auto-compaction 在 25 turn 以内不会触发（25 turn × 平均 token 远低于 75% context limit）

### 可能出错的地方

- 4h 阈值经验值——可能严重过松（员工连续聊 2 小时打断 30 分钟回来续聊被误认 idle）或过严（午饭一过就 reset）。**概率 ~40%**（凭直觉，所以才需要 tripwire）
- turn 25 cap 跟 cc-gateway 50 cap 的关系——25 是凭"对话型 agent 不需要长 turn"判断，可能跟实际企微 chat 模式（员工连续发短消息形成多 turn）冲突。**概率 ~30%**
- "用户自己补背景"假设——Keith 当前判断基于他自己的使用模式，川锅其他员工可能没这个心智耐受度。**概率 ~25%**，但这是 PoC 期就该暴露的问题
- tripwire 日志真的会被两周后 review 吗——essence `bucket-time-asymmetry` 警告过出口需求迟到。**概率 ~50%**——除非现在就约定 review trigger（比如挂 inbox/topics.md 或 NW 提案）

### 本次哪里思考得不够

- 没看 cc-assistant 现有代码——410 自愈逻辑的具体实现 / sessionMap 数据结构 / gateway-client.js 的事件回调位置，给的实施代码是示意。父会话执行时需要按实际代码 adapt
- 没核 cc-gateway 50 turn cap 跟 cost 的关系——本来"K 是 J 子集"的判断成立前提是 K 不会让单 session token 爆炸；25 turn cap 应该够安全但没算 token 预算
- 用户实际"补背景"的形态没具体化——是否需要 cc-assistant 在 system prompt 加一条"如果用户引用过往对话但你无上下文，请直接说'我现在没有那段记忆，能再说一下吗'"？这是 K 的一个补强但没展开

### 如果 N 个月后证明决策错了，最可能的根因

- **#1 候选**：tripwire 数据没人看——两周后没人触发 review，4h 阈值就这么定下来了，半年后被员工反馈"经常断片"才发现。这是 essence `bucket-time-asymmetry`（出口需求迟到）的具体复现
- **#2 候选**：第二消费者比预想的快出现（华昇 cron / kebao-cc 之类），但 idle policy 已在 cc-assistant 仓深度耦合，迁移成本超预期。`tool-elevation-as-occam` 的"上提时机"判断失误
- **#3 候选**：员工实际想要的不是"无感 reset" 而是"显式新话题按钮"——Keith 的"无感"偏好被无差别套到所有员工身上，缺多用户验证

### 北极星触达

**#3 决策超越直觉**。父会话已经凭 sense 倾向 K 并写了详细 brief，本次裁决的增量价值在三个机制层判断：
- 用 essence cross-check 把"K 看起来对"升级为"K 在 4 个 essence 维度都对位"
- 用 solution-space 展开两个未在父会话清单里的方向（N / O），证明 5 候选已覆盖真实解空间
- 给"4h 不需要理论正确"的 framing——把"猜参数"的不可能任务降级为"sense 初值 + tripwire 修正"的可解任务

不算 #1 二阶效应（没新建主体维度的长期机制）/ 不算 #2 动态学习（没整合跨领域）。

### essence 对齐自检

- **本决策跟哪几滴 essence 对位**：
  - `theory-gap-without-data` (2026-05-06)：J 是没数据时生造的理论缺口 → 否决 J
  - `premature-abstraction-tripwire` (2026-04-21)：tripwire jsonl 而非现在判抽象 → 直接套用
  - `bucket-time-asymmetry` (2026-05-08)：4h 后想接上是想象的出口需求 → 否决 J
  - `tool-elevation-as-occam` (2026-05-06)：第二消费者出现前不下沉 cc-gateway → 支持留在 cc-assistant
  - `transparent-rewrite-breaks-contract` (2026-04-21)：L 方案读 CC jsonl 是改写私有契约 → 否决 L
  - `dimension-blindness-not-asymptote` (2026-04-27)：J 的 summary 是 LLM 内部闭环不是真外化 → 强化否决 J
  - `m2m-vs-h2m-coupling-illusion` (2026-05-09)：personal-assistant 是 H2M chat，治理在业务层 → 支持 cc-assistant

- **本决策是否在某条 essence 上反着走**：无。

- **cross-check 用的关键词**：theory-gap / bucket-time / tool-elevation / transparent-rewrite / dimension-blindness / m2m-vs-h2m / premature-abstraction（共 7 个，物理 Read 过 essence.md 全文确认）

### essence 候选

- slug: `idle-threshold-as-tripwire-not-answer`
- 一句话：sense-driven 初值 + 数据 tripwire 是 `theory-gap-without-data` 在工程参数上的落地范式——把"猜对参数"的不可能任务降级为"先猜一个、记录现实、两周后调"的可解任务。
- 跟已有 essence 的差异：`premature-abstraction-tripwire` 是抽象/不抽象决策的形态，本滴是连续参数（阈值数字）决策的形态——前者二元，后者标量。两者同维度（tripwire 解开决策锁死），但应用域不同
- 是否已 append 到 essence.md: N（按 KERNEL §3 第 5 步退场动作 append）

### 外部锚点

- `~/githubProject/cc-space/.claude/worktrees/cc-assistant-v0.2-postmortem/threads/cc-assistant.md` ← cc-assistant 主体协作叙事
- `~/githubProject/cc-space/.claude/worktrees/cc-assistant-v0.2-postmortem/threads/cc-gateway.md` ← cc-gateway 主体协作叙事（机制下沉位置判断的对照）
