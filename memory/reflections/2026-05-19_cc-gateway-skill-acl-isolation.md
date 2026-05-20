---
date: 2026-05-19
slug: cc-gateway-skill-acl-isolation
summoner: cc-space
northstar_reach: "#3 决策超越直觉（把'装载层隔离'四候选按 essence 同轴重切，否决直觉首选 M1/M3）"
status: substantive-decision
---

# Reflection: cc-gateway skill 按应用隔离机制

### 给父会话的最终输出（必填）

**推荐**：

1. **机制 = M2**（runner buildArgs 每会话拼 `--disallowedTools "Skill(非自有...)"`），语义层级 = **进程级权限硬层**（非 M1 配置软层）。M1 降级为 v1 可选纵深防御，不作主隔离。M3/M4 否决（有显式 v1 触发条件）。
2. **SSOT = cc-gateway 侧单独文件**（如 `config/skill-acl.json`），**白名单制**（`_common` 通用桶 + per-workspaceId 业务白名单），runner 运行时取反算 disallowed。**不准落 agents.json `skills` 字段**（=cc-gateway 已被 Keith 命中两次的"业务语义进中立 runtime 配置面"反模式第三次复现）、**不准落 cg-skills frontmatter**（SSOT 碎片 + 污染上游中立仓）。进 ssot/registry.md 注册。
3. **cg-skills 目录结构本轮不动**；两个 cg-skills 仓债与本决策正交，单独登记 `threads/cg-skills.md`，不阻塞本轮。skill 名权威源 = 容器实挂的 `~/CGProject/cg-skills` 11 个。
4. **新增 cg-platform 沙箱契约 8「应用能力面隔离」，v0 装**（与契约 1/2/3 同族——把 DB/网络面的 blast radius 隔离补齐到能力调用面；与"PM 过人眼/零用户/单环境"正交，是运行时硬墙不被上游条件豁免）。契约措辞只声明一层真层（M2），M1 不计入承重层数（吸收 essence `network-cannot-cut-what-shares-tuple`，不写纸面双层）。
5. **分期**：MVP=skill-acl.json + runner buildArgs 取反计算 + 初始填现有 workspaceId 白名单 + 契约 8 v0 + registry 注册 + 物理核验 deny 真生效的 contract test。v1 推迟项=M1 纵深 / M3 物理切+两仓债 / agent×workspace 双维，三项各有显式触发条件。

**理由**：本决策本质是 essence `llm-autonomy-on-capability-invocation-is-the-bug-not-the-channel`（2026-05-19，同日）的延续 + cc-gateway thread 2026-05-14 disallowedTools prod 实证 + 2026-05-15「中立 runtime」收窄的第三次同形态出现。四候选按"决策点在谁手里"重切，M1/M2/M3/M4 全对轴（Keith 方向正确）；再按 invariant"业务 skill blast radius 安全相邻"这条安全承重墙切——安全墙的隔离语义必须硬层不能软层。M2 的硬层强度已被 2026-05-14 prod `permission_denials` 物理实证，M1 的 `off` 强度本项目无实证，安全墙不能建在未实证的配置可变面（essence `network-cannot-cut-what-shares-tuple` 同构）。白名单制 SSOT 消解了题面 M2"黑名单要穷举"的代价（维护白名单语义自然，取反交代码，新 skill safe-by-default 不可见）。

**trade-off**：M2 比 M3 物理层弱（skill 实体仍在盘、CLI 仍全量发现，只在准入层 deny）——接受，因为进程级 deny 已够"安全相邻"承重线，M3 要付辐射 cg-skills 三通道 + 两仓债代价。未核验假设：① CLI `--disallowedTools "Skill(name)"` 细粒度 pattern 的 deny 强度等同 2026-05-14 实证的粗粒度 `Skill`（题面实证事实 4 已核 CLI 支持该语法，但 deny 实际硬生效需 MVP contract test 物理核验，不能凭文档）② skill-acl 白名单必须把现有 prod workspaceId（huasheng-cron 等）实际依赖 skill 枚举全，否则 deploy 即断华昇战报生产链路——这是 deploy 前 ack 点。

**行动建议**（父会话下一步）：① 落 skill-acl.json + runner/stream buildArgs 取反计算（与现有 `agent.disallowedTools` 取并集不覆盖）② 枚举现有 workspaceId 实际依赖填白名单（deploy 前按 prod 不可逆 ack 纪律核 huasheng-cron 链路）③ cg-platform `integration-contract.md` + 沙箱契约表加契约 8 v0 ④ ssot/registry.md 注册 ⑤ contract test 物理核验 deny 真生效（对齐 2026-05-14 实证标准）⑥ 两仓债登记 cg-skills thread 一行。承重墙 5 条不可在实现层翻；隔断（文件名/字段名/_common 成员/各 workspace 白名单内容）实现层自决。

### 核心假设

- CLI `Skill(name)` 细粒度 deny 与 2026-05-14 实证的 `Skill` 粗粒度 deny 同强度（需 MVP 物理核验，未盲信）。
- workspaceId 在 createSession 锁死（2026-05-15 已实现），runner 能在 buildArgs 阶段稳定拿到它做 skill-acl 查表。
- 业务/通用 skill 二分（题面实证事实 7）稳定——通用文档类全员可见无安全风险。

### 可能出错的地方

最可能崩点：skill-acl 白名单漏填现有 prod workspaceId 的真实依赖 → deploy 后华昇战报/cg-meetos 生产链路静默断（概率中，已在行动建议焊为 deploy 前 ack 点，但若实现层跳过枚举直接 deploy 会真断）。次要：CLI 细粒度 Skill() pattern 在容器内 claude 版本上语义与文档不符（概率低，contract test 物理核验兜底）。

### 本次哪里思考得不够

未实地核 cc-gateway runner.js 当前 buildArgs 的 workspaceId 可达性细节（依赖 thread 记载的 2026-05-15「cwd 在 createSession 锁死写 store」推断 workspaceId 同样在 store 可查），交实现层验证；未核 cg-skills 11 个 skill 各自实际触发词/被哪些现有 workspaceId 依赖（business 归属判断留给实现层，gg 不拍具体清单是正确边界但意味着 deploy 前枚举的完整性责任在实现层）。

### 如果 N 个月后证明决策错了，最可能的根因

M2 进程级 deny 被证明对某类诱导调用绕不过（如 LLM 经 subagent fresh context 重新发现 skill——对照 cc-gateway thread 2026-05-14「subagent fresh context 不继承约束」的杀手）。届时 M1 纵深 v1 触发条件该被改为"立即装"而非"出案例再装"——本决策把 M1 推 v1 可能是把一个该 v0 的纵深当成了可选项。已在 v1 触发表留了"M2 deny 被绕过实证"这个触发器，但触发器是被动的，subagent 穿透是已知风险不是未知风险，留观察可能偏乐观。

### 推理盲区

skill-acl 与 subagent 工具继承的交互未深推——2026-05-14 实证 subagent fresh context 不继承 systemPromptAppend，但 `--disallowedTools` 是 CLI 进程级参数，理论上对该进程内所有 subagent 生效（与 systemPromptAppend 的"主代理可见"不同机制）。这条若成立则 M2 反而比 M1 在 subagent 维度更强（强化 M2 选型）；若不成立则上一段根因预判的风险更高。本决策按"CLI 进程级参数对全进程生效"假设走，未物理核——这是该进 MVP contract test 的一个 case（建议补：subagent 内尝试调被 deny 的 skill 是否也被拦）。

### 北极星触达

#3 决策超越直觉——题面四候选的直觉排序是"M1 最省→先试 M1"或"M3 最彻底→上 M3"，本决策按 essence 同轴重切后否决了两个直觉首选，落在 M2（既非最省也非最彻底，是"安全承重线 × OCCAM"的交点）。

### essence 对齐自检（必填）

- **本决策跟哪几滴 essence 对位**：
  - `llm-autonomy-on-capability-invocation-is-the-bug-not-the-channel`（2026-05-19）——本决策的轴心先验，"决策点从 LLM 手里物理移走"直接定调四候选全对轴、Keith 方向正确。
  - `network-cannot-cut-what-shares-tuple`（2026-05-19）——塑造契约 8 诚实化表述（不写纸面双层，只声明 M2 一层真层），否决 M1"配置软层当安全墙"。
  - `bug-shape-survives-fix`（2026-04-27）——识别"SSOT 落 agents.json `skills` 字段"=cc-gateway 同型反模式第三次复现，必须显式拒绝诱因。
  - `premature-abstraction-tripwire` / `metric-vs-pattern`——否决 M3/M4 现在做（为"更彻底/更优雅"付辐射+重写成本是把手段当目的）。
  - `ownership-by-facet`（2026-05-06）——契约 8 是"能力调用面"漏掉的 facet，与契约 1/2 的 DB/网络 facet 同族；两仓债按面切分不捆进本决策。
- **本决策是否在某条 essence 上反着走**：无明显反走。潜在张力：把 M1 推 v1 与"安全承重墙建在硬层"自检——若 subagent 穿透使 M2 单层不够，M1 该 v0 不该 v1。已在根因预判 + 推理盲区显式标注此张力未完全展开，留 MVP contract test 物理核验 subagent 维度后再定 M1 是否提前 v0。
- **cross-check 用的关键词**：grep essence.md `capability-invocation` / `network-cannot-cut` / `bug-shape` / `premature-abstraction` / `ownership-by-facet` / `metric-vs-pattern` / `physical-anchor`（启动时全量 Read essence.md，本次决策中逐条比对）。

### essence 候选（可选）

- slug: safe-default-by-whitelist-inversion
- 一句话: 安全隔离的 SSOT 应存"准入白名单"而非"禁入黑名单"——取反交给运行时代码，新增能力自动落 safe-by-default 不可见，把"穷举黑名单"的伪代价消解为"白名单语义自然 + 一行取反"。
- 是否已 append 到 essence.md: N（候选，留 Keith review；与 `network-cannot-cut-what-shares-tuple` 同族但角度不同——前者讲层数诚实，本候选讲 SSOT 极性方向，去 gg 化后仍有重量：任何安全 ACL 设计的极性选择）

### 外部锚点

- `~/githubProject/cc-space/threads/cc-gateway.md` ← cc-gateway 中立 runtime 主体叙事（本决策落地后加时间线 entry）
- `~/githubProject/cc-space/threads/cg-platform.md` ← 契约 8 落点（沙箱契约表 + integration-contract.md）
- `~/githubProject/cc-space/threads/cg-skills.md` ← 两仓债单独议题登记处
