---
date: 2026-05-19
slug: cc-gateway-acl-rejudge-dual-path
summoner: cc-space
northstar_reach: "#3 决策超越直觉（基于物理新事实主动推翻自己上一轮承重墙，而非辩护既有裁决——审视位置偏向辩护现状的对冲）"
status: substantive-decision
---

# Reflection: cc-gateway 双路径能力面隔离（上一轮 ACL 决策的增量重裁）

### 给父会话的最终输出（必填）

**推荐**（5 条增量裁决，逐条标与上一轮关系）：

1. **裁决1 SSOT落点（覆盖上一轮第2条）**：workspace/agent 能力准入收敛进**既有 skills.json**（扩展 schema：每 skill 项加可选 `allowedWorkspaces`/`allowedAgents`，留空=保持现状全可见）。**不**新建独立 ACL 文件。上一轮拒此选项的论据建立在未核实前提（以为 skills.json 是 cg-skills 中立内容）；物理事实推翻——Dockerfile:91 只 echo `{}` 占位、docker-compose:34 从 ${SKILLS_DIR} 只读挂载、deploy.sh:183 硬依赖它存在否则 abort = **skills.json 物理在 cg-skills 仓但语义归属 cc-gateway，本就是 cc-gateway 部署契约载体**。上一轮的 (b) 会造 skills.json + skill-acl.json 双 SSOT 碎片，撞我上一轮自己定的反碎片原则。
2. **裁决2 cg-skills禁区（收紧+重定义边界）**：禁区真实边界不是物理仓边界，是"cg-skills 中立 skill 实体 vs cc-gateway 注入进其物理空间的部署配置"。**可写 skills.json 内容**（语义归 cc-gateway）；**仍不动 skills/ 下 SKILL.md/frontmatter**（真 skill 实体，上一轮拒落 frontmatter 论据成立）。两个 cg-skills 仓债维持单独 threads/cg-skills.md 不阻塞。
3. **裁决3 双路径分治（覆盖上一轮核心机制——M2 不再是两路径统一答案）**：物理事实——/trigger+/trigger/stream 走 validateTrigger（body.skill 强制 + skills.get 不在表 404），run() 调用不传 cwd/workspaceId（index.js:633 实测，runner.js:121 fallback process.cwd），**无 workspaceId key 可挂 M2**。分治：**/sessions 走 M2**（runner buildArgs 按 workspaceId 反查取反拼 `--disallowedTools "Skill(x)"`，注入点 runner.js:38，与 agent.disallowedTools 取并集不覆盖）；**/trigger 走既有 skills.json 准入白名单 + 扩展 allowedAgents 二级校验**（请求层拦截，LLM 根本碰不到，比 M2 更前置更硬）。一个 SSOT（扩展后 skills.json）两套读法（同一 skill 准入事实的不同维度投影，非两份独立声明）。
4. **裁决4 契约8措辞（收紧）**：改双路径不对称声明——/trigger=请求校验层准入硬墙（不进 LLM 进程）/ /sessions=进程级 disallowedTools 硬墙（dontAsk 下 2026-05-14 prod 实证）。SSOT 单一 skills.json。不写"双层防御"，各路径诚实声明一层真层（维持 essence network-cannot-cut-what-shares-tuple 一致）。
5. **裁决5 分期（收紧 MVP）**：MVP=skills.json schema 扩展（留空=safe-by-default 保持现状，Dockerfile 占位仍 `{}`）+ /sessions 侧 M2 读取逻辑 + 契约8 v0 双路径措辞 + ssot/registry 升级注册 + contract test（细粒度 Skill(name) deny + subagent 维度）。**关键收紧**：因 cc-assistant 仅依赖 _common 桶 + huasheng-cron 三 skill 全绕 Skill 工具走代码 import（M2 对其零影响，上一轮已识别），MVP 阶段 allowedWorkspaces 可全留空 = 现状 = **直接消解上一轮"deploy 前必须枚举全部现有 workspaceId 依赖否则断 huasheng"的高危 ack 点**（safe-by-default 默认值替代枚举正确性赌注）。v1 推迟：/trigger allowedAgents 校验逻辑（硬触发=cg-meetos 正式上线前必须就位，它是第一个真 /trigger 消费者）/ M1 纵深 / M3 物理切 / 全双维矩阵（各原触发条件不变）。

**否决项**：(b) cc-gateway 仓侧独立 acl 文件（双 SSOT 碎片，本轮我自己推翻上轮选择）/ (c) 改 volume 拓扑迁出 SSOT（付辐射税换物理位置洁癖，premature-abstraction）/ 给 /trigger 硬造 workspaceId 维统一 M2（为对称性给程序化路径强加 LLM 不可靠面，它有更前置的天然闸门）/ MVP 强制枚举全 workspaceId 依赖（被 safe-by-default 消解）。

**trade-off / 未核验假设**：① /trigger 的 allowedAgents 二级校验在 v1 才装——现 MeetOS 未上线零回归，但若 MeetOS 上线节点早于 v1 实施则有窗口（已焊为硬触发：MeetOS 上线前必须就位，非"出案例再说"）② /sessions M2 细粒度 `Skill(name)` deny 强度等同 2026-05-14 粗粒度实证——MVP contract test 物理核验，未盲信 ③ skills.json 一个文件被 /trigger（请求层）+ /sessions（runner 层）两处代码读，耦合点增加——接受，因为它本就是单一准入事实，分两文件才是真碎片。

**行动建议（父会话下一步）**：① skills.json 加 allowedWorkspaces/allowedAgents 可选字段（留空=现状）+ 同步 deploy.sh 校验/README/Dockerfile 占位兼容 ② runner buildArgs 加按 workspaceId 反查取反，与 agent.disallowedTools 取并集去重 ③ /trigger allowedAgents 校验逻辑标 v1 + cg-meetos thread 记硬触发"上线前装好" ④ integration-contract.md + 沙箱契约表落契约8 双路径措辞 ⑤ ssot/registry.md 把 skills.json 升级注册为"双路径能力准入 SSOT"（非新注册 acl 文件）⑥ contract test 含 subagent 调被 deny skill 用例 ⑦ cc-gateway thread + cg-platform thread 加时间线 entry。承重墙=5裁决+4否决不可在实现层翻；隔断（字段名/array vs object/_common 成员/错误码/代码位置/仓债节奏）实现层自决。

### 核心假设

- skills.json 语义归属 cc-gateway（物理证据三连：Dockerfile echo {} 占位 / docker-compose volume 注入 / deploy.sh 硬依赖）——已物理核实，非假设。
- /trigger run() 不传 workspaceId（index.js:633 + runner.js:121 fallback）——已物理核实。
- cc-assistant 仅依赖 _common 桶 + huasheng-cron 绕 Skill 工具——来自上一轮已确认的题面事实 + 父会话本轮确证，沿用未重核（若错则 MVP 留空策略需回退到枚举，已在 trade-off 标）。

### 可能出错的地方

最可能崩点：cg-meetos 实际上线节点早于本轮 v1 /trigger ACL 实施 → /trigger 路径在 MeetOS 上线后短暂裸奔（无 allowedAgents 二级校验，仅靠 skills.json 白名单本身——白名单本身仍拦未注册 skill，所以是"二级校验缺位"非"完全裸奔"，blast 有限）。概率中（取决于父会话实施排期 vs Keith 推 MeetOS 速度），已焊硬触发缓解。次要：skills.json 两处代码读取的 schema 版本不同步（/trigger 侧读旧 schema /sessions 侧读新）——实现层 contract test 应覆盖同源解析。

### 本次哪里思考得不够

未实地核 runner.js buildArgs 内 session.workspaceId 在 /sessions 路径的实际可达链路（依赖 thread 记载 2026-05-15「cwd 在 createSession 锁死写 store」+ 本轮核到 index.js:411 createSession 传 {workspaceId, cwd}，但 runner buildArgs 阶段从哪个对象取 workspaceId 未逐行追——交实现层）。未核 cc-assistant/huasheng-cron 当前真实 workspaceId 取值（沿用上一轮+父会话确证，MVP 留空策略使此核实非 deploy 阻塞，但若未来要填白名单则是前置）。

### 如果 N 个月后证明决策错了，最可能的根因

把 /trigger ACL 推 v1 被证明过乐观——cg-meetos 上线推进比预期快，"硬触发"在实施排期里没被当成真闸门（`bug-shape-survives-fix` 活体：写下硬触发的人不等于执行排期的人，触发器仍是被动的）。届时根因会是"已知消费方+已知上线节点本应 v0 装，被分期惯性推 v1"。已在行动建议③显式要求 cg-meetos thread 记账缓解，但 thread 记账≠实施排期强制。

### 推理盲区

skills.json 被 /trigger（validator.js 请求层，每请求 loadSkills）和 /sessions（runner buildArgs，每会话）两条路径在不同生命周期读取——loadSkills 是否每次请求重读文件 vs 启动缓存，影响"改 skills.json 后多久生效 / 两路径是否看到一致版本"。本轮未追 loadSkills 调用时机（startup once vs per-request），假设两路径读同一份磁盘文件即一致——若 /trigger 启动缓存而 /sessions 实时读，会出现改 ACL 后两路径生效时差。这是该进 MVP contract test 的一个 case（建议补：改 skills.json 后两路径生效一致性）。

### 北极星触达

#3 决策超越直觉——本轮的直觉是"父会话拿新事实回来质疑，gg 解释为何上一轮仍成立 / 打补丁"（审视自己既有裁决天然偏向辩护，`vantage-contaminates-verdict` 同根）。本决策反直觉地基于物理新事实**主动推翻自己上一轮的承重墙第2/3条**（SSOT落点 + M2 统一机制），并显式标注上一轮错在"未核落点物理前提"——这正是 `mechanism-relocation-has-its-own-precondition`（昨天我自己沉淀的 essence）的活体兑现。

### essence 对齐自检（必填）

- **本决策跟哪几滴 essence 对位**：
  - `mechanism-relocation-has-its-own-precondition`（2026-05-19，昨日我自沉淀）——本轮核心轴。上一轮"SSOT 落 cc-gateway 侧"是 relocation 决策，未核落点物理前提（以为 skills.json 是 cg-skills 中立内容）；本轮父会话核出前提部分不成立 → 推翻。这滴 essence 在 24h 内从沉淀变成审判自己上一轮的工具，是它越过 essence-degg-test 的实证。
  - `network-cannot-cut-what-shares-tuple`（2026-05-19）——分辨率错配。上一轮用"物理仓边界"低分辨率刀切"语义归属"高分辨率边界，把 skills.json 误判为禁区；本轮重定义边界=按语义归属切，非物理位置切。同时塑造契约8诚实化（不写双层）。
  - `safe-default-by-whitelist-inversion`（上一轮 essence 候选）——本轮直接兑现：MVP allowedWorkspaces 留空=safe-by-default，把"deploy 前枚举全依赖"的伪代价消解为"默认值=现状"。这是该候选去 gg 化后有重量的证据。
  - `bug-shape-survives-fix`（2026-04-27）——双重活体：① 上一轮我给诊断后以同形态做未核前提决策 ② 本轮"硬触发被排期惯性推 v1"的根因预判仍是同形态风险。
  - `llm-autonomy-on-capability-invocation-is-the-bug-not-the-channel`（2026-05-19）——否决"给 /trigger 硬造 workspaceId 统一 M2"：/trigger 的天然闸门 validateTrigger 是请求层（决策点不在 LLM 手里，比 M2 进程内 deny 更彻底移走），不该为对称性降级它。
  - `premature-abstraction-tripwire` / `evaluator-input-ownership`——前者否决 (c) 迁 volume；后者反面印证 skills.json 已是 cc-gateway 拥有的输入面（非上游的）。
- **本决策是否在某条 essence 上反着走**：潜在张力——`abstraction-tax`/反碎片 与 "skills.json 一个文件被两处不同生命周期代码读" 的耦合增加。表面像在一个文件上堆两套消费逻辑（碎片的反面=过度集中）。判定不反走：准入是关于"skill X 对谁可见"的**单一事实**，两路径读的是同一事实的不同维度投影，分两文件才制造真碎片（同一事实两处声明）。张力已在 trade-off ③ 显式展开，非未察觉。
- **cross-check 用的关键词**：启动时全量 tail essence.md；本轮 grep 比对 `mechanism-relocation` / `network-cannot-cut` / `whitelist-inversion` / `bug-shape` / `capability-invocation` / `premature-abstraction` / `evaluator-input-ownership` / `vantage-contaminates`。

### essence 候选（可选）

- slug: precondition-recheck-overturns-prior-verdict
- 一句话: 当一个旧裁决依赖的物理前提被后续证据推翻时，正确动作是基于新事实主动覆盖自己的承重墙并显式标注"上一轮错在未核前提"，而非辩护旧裁决或打补丁——审视自己既有决策的位置系统性偏向辩护现状（vantage-contaminates-verdict 的自指版本），对冲它需要把"推翻自己"作为默认假设而非例外。是 `mechanism-relocation-has-its-own-precondition` 的下一拍：不只要在给诊断时核前提，更要在前提被他人核出不成立时无摩擦地放弃旧结论。
- 是否已 append 到 essence.md: N（候选，留 Keith review；与 mechanism-relocation 同族但角度不同——前者讲"决策时要核前提"，本候选讲"前提被推翻后要无摩擦覆盖自己"，去 gg 化后对任何"基于旧前提的既有决策被新证据挑战"场景有重量）

### 外部锚点

- `~/githubProject/cc-space/threads/cc-gateway.md` ← 双路径分治 + skills.json 语义归属落地后加时间线 entry
- `~/githubProject/cc-space/threads/cg-platform.md` ← 契约8 双路径措辞落点（integration-contract.md + 沙箱契约表）
- `~/githubProject/cc-space/threads/cg-skills.md` ← skills.json 语义归属澄清 + 两仓债登记处
- `~/githubProject/cc-space/threads/cg-meetos.md` ← /trigger ACL v1 硬触发"上线前装好"记账处
- 上一轮 reflection: `~/githubProject/gg/memory/reflections/2026-05-19_cc-gateway-skill-acl-isolation.md`（本轮覆盖其第2/3条）
