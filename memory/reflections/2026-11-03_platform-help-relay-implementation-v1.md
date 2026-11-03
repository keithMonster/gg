---
date: 2026-11-03
slug: platform-help-relay-implementation-v1
summoner: monster 主会话 /root
northstar_reach: "#3 决策超越直觉"
status: substantive-decision
---

# Reflection: 长任务修复 v1 独立实现复核

### 给父会话的最终输出

**Verdict：REQUEST_CHANGES。** 最危险的空隙在成功/报错终态：超时分支已经防住 Close 失败，普通终态却仍绕过同一保护。本次核对 candidate-v1.json 的 19 个实际源码 SHA，全部一致；结论限该冻结版本，不含后续修改。审读实际源码、测试与日志，未改业务文件、未访问生产、未运行真实会话。

开题四问：① 问题改写为“新生命周期的不变式有没有覆盖所有出口，而不只覆盖故障样例那个出口”。② 错答案会在终态后的第二次 Start、迟到 pending 恢复 running、迁移话题原请求计数归零上现形。③ 对照仅重跑成功测试、扩大为新任务框架、按出口和数据形态构造反例；选择第三项，前两项分别漏控制流分支和扩大修改面。④ 最便宜接触已做：全 19 文件 hash 对账，两个内存反例分别复现原件遗漏和状态降级。

**P1：tracked 正常终态绕过有界关闭和保锁。** `/Users/xuke/githubProject/_other/cc-connect/core/engine.go:13284-13285` 在 EventResult/EventError 后仍直接调用 `agentSession.Close()`，无 10 秒上界且忽略错误；deadline 同时有 ready final 时经 `finishReadyRelayTerminal` 进入 `finishDrainedRelay:13469-13481`，仍如此，后者还只记录持久化错误并返回 true。明确失败形状：EventError/Result 后 Close 返回错误，defer 解锁使第二个 request 能启动；Close 挂住则 goroutine/锁没有界限。最小修复是 tracked 共用终态 finalizer，保留已知业务 done/failed，同时独立表达回收未知、失败保锁；ready-final 路径传回真实持久化/关闭错误，legacy 可继续旧语义。补 EventError+Close失败、EventResult+Close挂住、deadline+ready-final+持久化失败测试。

**P2：迁移路由的前置说明导致原请求恢复全漏。** `/Users/xuke/githubProject/monster/platform-help/runtime/task_evidence.py:23` 要求文本从 `[keith-mcp]` 起始，而真实 `relay.mjs::send` 对已迁移 source 前置 `retiredConversationNotice()`，即 `[keith-mcp-history-reset]`。本轮只读加载模块，以同一信封调用 request：plain 返回原消息，加真实形状前缀返回 null。这直接影响本次已迁移话题，现 fixture 都是裸信封。最小修复为识别/剥离唯一受信前缀，再锚定首个真实信封；不能改成全篇任意搜索，避免把嵌套引用当原请求。零原请求应显式提示恢复缺口。补 actual buildRelayMessage+retiredConversationNotice 形状及伪造/重复信封反例。

**P2：旧 pending 可以把执行器复活。** `/Users/xuke/githubProject/monster/studio/spikes/cc-connect/keith-mcp/src/jobs.mjs:104-123` 先合并 execution，再判断旧状态是否 stopped；同 count/time 的旧 running 会先覆盖 stopped，从而绕过后面的拒绝条件。无文件 JobStore 实际重放得到 `outcome_unknown stopped → pending running`。最小修复在合并前按旧执行状态拒绝生命周期降级；stopped 与 unknown+已知终止原因（含 close_failed/daemon_restart）都不可被旧 pending 复活，真实迟到 done/failed 仍可提升业务结果。补相同 count/time 的迟到快照，不要只测计数变小。

**P2：历史活动被措辞升格为当前存活。** `src/execution.mjs::executionDetail` 将保存的 running 渲染为“执行器仍在运行”；getResult 失败时 JobStore 保留历史 execution，failureMessage 仍拼这句话。最小改成“最近一次记录：运行中/正在启动”，保留时间与查询未知，不需要新状态层。snapshot 是最后观察，不是当前存活证明。

**验收实况：** go-full-packages.log 已结束，core FAIL 六项，agent/codex PASS；六项分别涉及 footer 路径四项、delete confirm card 一项、/var 与 /private/var 规范化一项，不能在未回放旧基线前擅自归为无关。node-full.log 已结束，281 项中 279 通过、2 失败：idesk-shutdown fixture 的 employee 缺导出；jobs 跨 caller 用例在等待结果时仍 pending。旧实现 go-before-fix-replay.log 在虚拟第 40 分钟按预期失败，支持修复靶点真实。相关新测试通过不消除上述具体反例。父会话应补必要反例，并给全量失败的基线/修复证据。

**未覆盖与范围：** startup 新测试只证明 StartSession 服从 ctx 时可截止，未证明任意不服从 ctx 的后端有界；应把通用保证限于支持取消的实现，或补迟到 session 的回收测试。confirmed pending 后 job.promise 已 resolve，check_keith 的 Promise.race 会即时返回，原 45 秒等待不再实际长轮询；可先诚实说明短查询，不因此建调度器。native-compaction fixture 直接安装 task-evidence hook，证明原生 compact 事件能注入，不等于真实 codex_hook_bridge 和专属服务的最终接线已验。shared Go/Node 未安装，不宣称生产已修；hook 源为加载入口，需分别核实际生效范围。`monster.patch` 只含小部分增量，整批来源以 manifest 当前源码为准，最终 diff 应注明准确基线以免漏掉已被其他提交带走的改动。

### 核心假设

本批仍保持同 request 不重放、unknown 不放开原 conversation、legacy 兼容；对强状态保留没有业务恢复新授权。

### 可能出错的地方

把已观察终态与执行器回收绑为一个结果导致真实成功丢失，或为保成功而漏掉 Close 失败；修复应保留两个事实。另一个失败方向是宽松搜索信封导致引用文本被冒认原始请求。

### 本次哪里思考得不够

Go 终态关闭缺陷由原始分支直接核实，没有在业务仓写新测试复现；遵循本轮只读限制，由父会话添加反例。未核任何运行中用户会话或生产结果。

### 如果 N 个月后证明决策错了，最可能的根因

把“能解释原事故”的测试当作“覆盖新不变式”的证明，导致正常出口与同时就绪分支继续沿旧语义运行；或把同一状态的时间戳比较当作状态转换合法性的替代。

### 北极星触达

#3：从原超时出口转向正常终态出口，并用真实迁移前缀和相同事件计数构造测试原先未覆盖的输入形态。

### essence 对齐自检

- 对位：anchor-protects-retrieval-not-integration（状态投影不能升级事实）、reconsolidation-safe-iff-original-immutable（原件恢复）、tripwire-disarm-needs-relocated-sensor-not-deletion（回收保护需覆盖全部出口）。沿同批次已读原卷。
- 反向张力：separation-need-is-not-topology-verdict 仍约束方案，四项均可在现结构内修，不因审查发现推出新框架。
- cross-check 关键词与原卷物理读取沿本批上一份 reflection；本轮新增证据是 19 文件摘要对账、两个无文件反例与实际测试日志。

无 essence 候选。实际产物仅此 reflection；未提交、推送、安装、重启或业务修改。
