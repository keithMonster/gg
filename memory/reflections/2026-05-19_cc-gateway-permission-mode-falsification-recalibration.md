---
date: 2026-05-19
slug: cc-gateway-permission-mode-falsification-recalibration
summoner: cc-space
northstar_reach: #3 决策超越直觉
status: substantive-decision
---

# Reflection: cc-gateway permission-mode 证伪校准（承接 llm-autonomy-is-the-bug）

## §A 范式 A — 决策的元属性反思

### 给父会话的最终输出（必填）

**背景**：昨日 `llm-autonomy-is-the-bug` 决策的 (b) 实施约束第 3 条「bypassPermissions 不改，隔离靠 allowedTools/MCP 与 permission-mode 正交」被官方文档正面证伪——bypassPermissions 把整个权限层连同 allowedTools/disallowedTools 一起绕过。

**推荐（5 项裁决）：**

1. **permission-mode 校准：per-agent，拒绝全局改**。runner.js L36 改 `args.push('--permission-mode', agent.permissionMode || 'bypassPermissions')`。agents.json 仅 `personal-assistant` + `business-proxy` 加 `"permissionMode": "dontAsk"`；default / task-runner 不加（fallback bypassPermissions，行为字节不变）。拒全局改的代价不对称：全局改收益≈省 10 行代码，风险=赌文档未覆盖的 dontAsk-on-no-allowedTools 行为，赌输则打断 huasheng 无人值守 cron（次日才发现）+ cg-meetos 判断层（均走 task-runner，物理核实 huasheng-tick.sh L150 + agents.json L13-21 确认 task-runner 无 allowedTools/disallowedTools）。`reversibility-not-permission` 直接落点：全局=不可逆侧，per-agent=可逆侧（隔离在新 agent）。per-agent 不是规避风险的补丁，是修正错配——task-runner（可信内部 skill 执行器）与 personal-assistant/business-proxy（外部不可信输入业务面）信任模型根本不同，全局单值是 `m2m-vs-h2m-coupling-illusion` 同构错误。

2. **business-proxy 是当前活体故障（超出父会话框定范围）**：物理核实 agents.json L26，business-proxy 配了 disallowedTools 九件套（Agent/Skill/Read/Write/...），它在 bypassPermissions 下从未生效——cc-assistant 业务面安全约束此前一直是纸面层（`network-cannot-cut-what-shares-tuple` 同形态）。校准范围必须从 personal-assistant 一个扩到 personal-assistant + business-proxy 两个，本次 per-agent 改造两个都声明 dontAsk。

3. **Keith ack 边界：不需要二次 ack（前提=走 per-agent 严格隔离）**。改动物理隔离在两个业务接入 agent（正是已 ack 范式轴的施加对象），task-runner 零行为变更 → 落在已 ack 范式轴内部，不是「cc-gateway 全局 permission 模型变更」。但**必须主动告知 Keith（告知非 ack）**：business-proxy disallowedTools 此前失效 = cc-assistant 安全约束是纸面层（Context Asymmetry，Keith 大概率不知此 latent 状态）。反向边界写死：若 per-agent 不可行被迫全局改 L36 → 停，回 Keith 二次 ack。

4. **spike 重心转移确认正确**：从「白名单硬不硬」（文档已答）转到三个文档灰区。spike 矩阵：
   - **S1（承重闸门，最高优先级）**：dontAsk + allowedTools 白名单下，LLM 调白名单外内置工具（Bash/Read/Task）的实际行为。三选一：(a) 静默 deny+回灌继续【唯一满足 personal-assistant 隔离】/ (b) abort session / (c) 阻塞。**S1=(b)/(c) → 立即停，不跑 S2/S3，回 Keith 范式回炉**（工具空间硬约束在 claude CLI 当前能力下做不到软挡，要么接受 abort 体验要么走 MCP-only 极简能力面从根上消灭"白名单外"概念）。这是 `dimension-blindness-not-asymptote` 落点——别在 spike 参数维度微调一个范式维度的失败。
   - **S2**：resume 续话是否继承首轮 allowedTools/disallowedTools（不继承 → runner.js L31-34 resume 分支补传，纯实现层）。
   - **S3**：resume 是否需重传 --mcp-config（需重传 → resume 分支补 + 容器内 mcp server 须常驻）。
   - spike 不做：HTTP transport MCP 接入（文档已覆盖）、两容器拓扑性能、真接 MCP server（S1 用 fake server 名即可触发白名单逻辑）。全在本地/prod 容器，零外部副作用，订阅 plan 内不涉成本。

5. **essence：精化既有滴 + 新增一滴**。精化 `llm-autonomy-on-capability-invocation-is-the-bug-not-the-channel`（方向对，隐含未核实前提=工具空间约束在当前 permission-mode 下成立）。新增 `mechanism-relocation-has-its-own-precondition`（已 append）。

**行动建议（按序）**：① 改 runner.js L36 per-agent ② agents.json personal-assistant+business-proxy 加 permissionMode:dontAsk ③ 先跑 S1（=(b)/(c) 停回 Keith）④ S1=(a) 后跑 S2/S3 定 resume 分支改造 ⑤ 告知 Keith business-proxy 纸面层事实 ⑥ 边界写死：被迫全局改 = 停回 ack。

### 核心假设

- per-agent permissionMode 字段 claude CLI 行为可控（buildArgs 已有 mode 分支，加字段是低风险实现层改动）——已被 runner.js 物理结构支持（L20-47 已是参数化构建）
- dontAsk 模式确实尊重 allowedTools/disallowedTools——这是父会话从官方文档带来的事实，我未独立二次核实文档原文（采信父会话的文档引用）
- S1 三选一穷尽了 dontAsk-on-unlisted-tool 的可能行为——可能有第四种（如降级为 ask 但 cron 环境无 stdin 直接 EOF→deny），spike 设计已用"三选一硬判定"兜底，第四种会落进 (b)/(c) 触发回炉，不漏判

### 可能出错的地方

最可能崩点：S1=(a) 但 (a) 的"回灌继续"在多轮对话里行为不稳定（首次 deny 回灌 LLM 继续，但 LLM 反复尝试同一被禁工具导致 maxTurns 耗尽 session 假性失败）。概率中等。这不是 S1 二元判定能捕获的——S1 只验"单次行为"，没验"多轮稳定性"。已在 reflection「思考不够」标注，建议父会话 S1=(a) 通过后补一个 mini 多轮稳定性观察（非阻塞闸门，观察项）。

### 本次哪里思考得不够

1. S1 闸门设计验的是"单次工具准入行为"，没设计"多轮 deny 回灌后 LLM 行为收敛性"的观察——personal-assistant 是多轮对话 agent，单次行为对≠多轮体验可用。
2. 没核实 cg-meetos 判断层走的具体 agent 是否真是 task-runner（父会话称走 huasheng cron 范式同可用性域，我物理核实了 huasheng=task-runner，但 cg-meetos 判断层调用点没独立 grep，采信父会话陈述的"同范式"）。若 cg-meetos 走的不是 task-runner 而是某个带 allowedTools 的 agent，per-agent 隔离边界要重画——这是采信未核实的传入陈述。
3. 没验证 claude CLI 版本——dontAsk 是较新 permission-mode，prod 容器内 claude CLI 版本若过旧可能不支持 dontAsk，spike S1 应前置一步 `claude --version` + dontAsk 是否被识别。已隐含在 S1 但未显式列为 S0 前置。

### 如果 N 个月后证明决策错了，最可能的根因

per-agent 路线落地后，未来新增的业务接入 agent（如华昇之外的新 cron、新业务编排层）开发者**默认不知道要加 permissionMode:dontAsk**——因为 default fallback 是 bypassPermissions（沉默的不安全默认）。新 agent 裸奔重演 business-proxy 当前故障。根因=fallback 方向选了"沉默不安全"而非"沉默安全"。当前选 fallback=bypassPermissions 是为了 task-runner/huasheng 零变更的正确权衡，但它把"安全是默认"反转成"安全要显式声明"——这是本决策埋的最深的债。缓解建议（未纳入本次行动，标记给未来）：agents.json 加 schema 校验或 cc-gateway 启动时对"无 permissionMode 且无 allowedTools/disallowedTools 的 agent"打 warning 日志，让裸奔可见。

### 北极星触达

#3 决策超越直觉。直觉（昨日的我）凭对 claude CLI 的训练记忆判"permission-mode 与 allowedTools 正交"，恰好推反。本次靠物理核实（runner.js L36 / agents.json L26 / huasheng-tick.sh L150）+ 官方文档证伪把决策从直觉拉到实证，并发现了直觉之外的活体故障（business-proxy）。

### essence 对齐自检（必填）

- **本决策跟哪几滴 essence 对位**：`physical-anchor`（2026-04-16，昨日的我凭训练记忆推断 permission-mode 关系未工具核实，恰推反）/ `reversibility-not-permission`（2026-05-06，全局 vs per-agent 用可逆性二分裁决）/ `m2m-vs-h2m-coupling-illusion`（2026-05-09，task-runner vs 业务接入 agent 信任模型异构不该单点配置）/ `network-cannot-cut-what-shares-tuple`（2026-05-19，business-proxy disallowedTools 纸面层=幻觉层）/ `dimension-blindness-not-asymptote`（2026-04-27，S1=(b)/(c) 触发范式回炉而非 spike 参数微调）/ `llm-autonomy-on-capability-invocation-is-the-bug-not-the-channel`（2026-05-19，被本次精化的昨日滴）
- **本决策是否在某条 essence 上反着走**：无明显反着走。潜在张力检查：`bug-shape-survives-fix`（2026-04-27）——昨日的我给出"工具空间移走决策点"诊断后，下一步（写"bypassPermissions 不改"）就以同形态犯错（没核实工具空间约束的生效前提）。这不是反着走，是该 essence 的活体复现，已在新 essence 滴里显式记录。无例外需解释。
- **cross-check 用的关键词**（物理 grep 证据）：grep `physical-anchor` / `reversibility-not-permission` / `m2m-vs-h2m` / `network-cannot-cut` / `dimension-blindness` / `bug-shape-survives` / `llm-autonomy-on-capability` over essence.md（启动时已全文 Read，cross-check 基于全文）

### essence 候选

- slug: mechanism-relocation-has-its-own-precondition
- 一句话: "把决策点从 X 物理移走"这个解自身依赖未被核实的物理前提——移走目标位置必须真能承接该决策；给出"移到 Y"诊断的人下一步极易跳过"Y 在当前配置下真能挡住吗"的物理核实
- 是否已 append 到 essence.md: Y

### 外部锚点

- `~/githubProject/cc-space/threads/cc-gateway.md` ← cc-gateway 主体协作叙事（中立 runtime + 软硬层 + workspaceId 一等公民）
- `~/githubProject/cc-space/threads/cc-assistant.md` ← cc-assistant 业务接入层叙事（能力迁移台账 + 本次校准承接 llm-autonomy 决策）
- `/Users/xuke/CGProject/cc-gateway/server/runner.js` L36 ← 被证伪的承重点物理位置
- `/Users/xuke/CGProject/cc-gateway/config/agents.json` L26 ← business-proxy 活体故障物理位置
