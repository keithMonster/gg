---
date: 2026-11-03
slug: platform-help-bounded-relay-lifecycle
summoner: monster 主会话 /root
northstar_reach: "#3 决策超越直觉"
status: substantive-decision
---

# Reflection: platform-help 长任务的执行期限与结果恢复

### 给父会话的最终输出

**设计准入：有条件通过，选保持现有同步 send 协议、只为 tracked 请求分离等待与有界执行的最小方案。** 这次中断最容易修错的地方，是把“执行器停止”写成“业务失败”：这样能清掉 unknown，却会把已发生的生产动作重新执行。原请求、执行器寿命、业务结果、回执交付须分别结算；复用现有 request/ticket/outbox，不新建调度框架。

开题四问：① 重写为“一个已接收动作由谁继续持有执行权、谁能证明它已结束”。② 错答案会让 HTTP 失联杀任务、同请求执行次数大于一、绝对期限被活动重置，或把旧副作用当未执行；读数是进程终止时间、Send 次数、持久记录和 caller 可见结果。③ 比较提高全链超时、立即异步接单、现协议内分离 wait/execute；第一种保留耦合，第二种可行但引入不必要 ack/JobStore 改造，第三种复用已有 MCP 45 秒出票及后台恢复。④ 最便宜接触已做：读 relay 生命周期、原始日志与 rollout；固定 30+10 分钟硬切实证闭合，且找到摘要归因的反证。

**根因已证实：** config.toml 选择性读取为 relay.timeout_secs=1800、idle_timeout_mins=10、max_turn_time_mins=150；Node relay.mjs 默认为 1800000ms。Go engine.go:13345 的 drain 固定 10 分钟；stdout.log:85022 在 14:58:42.989 对精确 conversation 报 drain timeout，原 relay record 同毫秒转 outcome_unknown，rollout:3210 在 14:58:43.011 记 turn_aborted。原记录起于 14:18:42.944，恰为 40 分钟。现 maxTurnTime/eventIdleTimeout 在普通会话事件循环生效，relay 路径不引用它们；不能裸删 drain 上限。relay_results.go::complete 对 unknown 清 response/error，导致有已知终止触发器却只剩 error=null；Node jobs.applyRelayResult 还把确认的 pending 变成 unknown。

**摘要归因已被反证：** rollout:2010/2083 的原始工具输出已包含 controlled-release-interface.md 的 15min 观察要求，:2285 工具输出也包含 deploy.sh 同义注释，均早于 :2834 摘要。当前 docs/controlled-release-interface.md:50 仍有此要求。gate.py:911-920 本身只核 healthy/Running、image/SHA、health 配置；不机械核 15min。这支持“等待来自既有操作规程”，不支持“摘要发明等待”或“Test 最多等 15 分钟被改成 Prod 至少观察 15 分钟”。该协调器规程是否完整适用于本次同 SHA 配置修复，须另做适用范围判断，本批不取消规程。rollout:2668/2712 证明当时三轮合成验证与 AppArmor 检查成功，不证明当前生产状态或原任务已交付。

**最小生命周期：** 仅 tracked 请求使用独立于 HTTP waitCtx 的 executionCtx，由 engine 生命周期派生，接单起固定绝对 deadline，跨同步/后台等待、重查与 compaction 不重置；现配置 150 分钟接入后才取代固定 10 分钟 drain。配置为 0 时须为 tracked 路径给明确有限后备值或拒接，不能隐式无界。一个 collector 始终拥有事件流、session 锁及关闭权；HTTP 断开只结束等待。StartSession、Send 和 Close 的阻塞也须受生命周期验证覆盖，不能只给收事件循环上计时器。legacy 无 request_id 的 partial 语义保持兼容。

**Idle 的取舍：** 绝对 deadline 是本批必要硬界；10 分钟无事件不等于业务卡死，长工具可能合法静默。若接入硬 idle，它必须明确是“协议静默上限”，不得宣称真实停滞检测；需测试 tool-in-flight 静默与持续事件无进展两个方向。心跳、轮询、工具输出均不得延长绝对 deadline。

**状态最少增量：** 沿现 relay record/Result 投影增加有限枚举的 stop_reason、执行结束证据、固定 deadline、last_event_at、会话/原件定位；请求身份继续绑定 request_id+from+to+session_key。已确认 running/pending 保持 pending；本地查询失败才表示本次观察 unknown，不能覆盖更强终态。执行期限/idle/shutdown/channel_closed 分开记录；终止后业务结果仍不确定时保留 outcome_unknown，不改 failed，不清原 conversation 占位。appserver_session.go:876 在 shutdown 起始就设 alive=false，因此 Alive()==false 不是退出证据；Close 失败继续未知，Close 成功也不证明远端副作用已停止。并发到达的真实终态优先于推测 unknown，持久化失败不得对外宣称成功。

**阶段与交付：** 进度记录只保留有界的事件种类、时间、工具 call_id、原件定位/摘要，以及窄白名单的安全字段。EventText 标“代理报告”，任意 JSON ok=true 只算该工具返回，不算业务验收完成；不落工具命令、全 stdout、秘密、员工正文或推理文本。check 可以在 Node live send 仍未返回时只读查询进度；不要让 executionActive 阻断所有取证。进度更新与终态/unknown 回执 version 分离，避免每个事件都触发 outbox。保持已有版本幂等、重启恢复及只查不 send。

**断点与压缩：** 在现 SessionStart compact/resume 入口补当前任务原件投影即可。只取可信 session/turn 与 caller 绑定的原始 response_item/user；排除 compacted.replacement_history、assistant 摘要和别的 session。原请求按不可信引用数据包裹，原文自称授权不能升级成 developer 权限。同时给原始验收条件、适用规程出处、已完成工具证据定位和未核实项；有证据冲突保留冲突，截断就明示。可从已有 rollout 重建，不写第四份常驻总结。只读断点材料能支撑接手，但不等于自动恢复执行；本批不建自动重放器。若另加机器续接，须确认旧 worker 退出、绑定同 caller 原票、以新 request_id+resume_of 留新尝试，重新核实际状态后只补缺项；不能发送原 message 再赌幂等。

**最低测试集合：** 缩短可注入时钟复现原 30+10 场景，修前被切/修后在更长但有限预算内完成；HTTP 断线仍完成，deadline 在首次等待与后台两段都不变；无事件/持续事件/静默长工具/engine shutdown/Close失败/Start或Send阻塞；截止点 final 同时到达、重复 ID 并发只 Send 一次、同 ID 改 payload 冲突、同 conversation 新 ID busy、不同 caller 同名 conversation 隔离；pending 不降 unknown，metadata 变化不冒充新结果，未知后迟到 final 只交付一次，重启只查不重放，落盘/outbox 失败不丢结果；伪造摘要授权/错误 caller/thread/引用其他票据/超大或损坏 rollout/JSON 含秘密/原始请求含 XML 闭合符；以明确区分 Test“最多等待”和规程“最少观察”的 fixture 验恢复保真。时间竞态用事件同步，不靠放宽 48ms 睡眠掩盖。

**上线验收边界：** 本轮设计取证不是实现通过；主代理离线测试通过后仍须冻结 diff 独立复核。共享 daemon/运行配置未更新前只能称候选已修；正式安装后要核实际 binary/配置/对应运行器，并用获授权的隔离合成任务经过真实 MCP→relay→执行器→结果/outbox 链，跨旧 40 分钟边界、断线恢复、compaction 注入以及最终取件；缩时测试可以证明代码机制，不能单独证明真实加载。不得重放本次生产动作做验收，不改已被父会话接手的原 release gate，也不把结果可取件写成请求人已读。

### 核心假设

现有 request/ticket/outbox 仍是唯一执行与交付身份链；本批目标是修本机通用执行机制和恢复事实供给，不获得业务重放、远端清理或新权限。同步 send 在 MCP 首等之外，故保留它不增加用户必须前台等待的时长。

### 可能出错的地方

以关闭本机执行器代替确认远端动作结束；以有活动代替有进展；以原件投影代替语义核对；向所有会话开 idle 硬切造成合法长工具误杀。不存在可凭本轮证据给出的概率。

### 本次哪里思考得不够

没有运行候选、测试 native hook 是否在当前专属 home 的 compact 事件触发，也没有核实际生产结果；方案阶段无冻结 diff。历史测试名称与源码已读，未把父会话的 baseline 通过当成本实例运行结果。

### 如果 N 个月后证明决策错了，最可能的根因

请求状态被当成一个枚举同时承载执行器存活、业务结果与交付状态，后续某个“方便恢复”分支重新把 unknown 解释为可重试，或观察超时又悄悄获得取消执行的权力。

### 北极星触达

#3：把“任务太慢”改写成执行所有权与事实强度问题，并用压缩前工具原件推翻摘要发明观察窗的便利归因。

### essence 对齐自检

- 对位：control-flow-vs-fact-supply、reconsolidation-safe-iff-original-immutable、anchor-protects-retrieval-not-integration，已回 2026-H1 原卷读取。
- 反向张力：separation-need-is-not-topology-verdict 反对由生命周期分离直接推导新调度服务，故选择现有 send 内改造；tripwire-disarm-needs-relocated-sensor-not-deletion 要求将 10 分钟防泄漏职责迁入绝对执行期限，不能裸删。recurrence-defense-pays-on-second-occurrence 的复发前提由 10-10 恢复记录与本次精确 40 分钟中断两案支撑。
- cross-check 关键词：separation-need-is-not-topology-verdict、control-flow-vs-fact-supply、anchor-protects-retrieval-not-integration、tripwire-disarm-needs-relocated-sensor-not-deletion、recurrence-defense-pays-on-second-occurrence、reconsolidation-safe-iff-original-immutable。

无 essence 候选。本轮只写本 reflection；未改业务仓、未外呼、未部署、未重启、未提交推送。
