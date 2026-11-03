---
date: 2026-11-03
slug: platform-help-relay-implementation-v2
summoner: monster 主会话 /root
northstar_reach: "#3 决策超越直觉"
status: substantive-decision
---

# Reflection: 长任务修复 v2 复核

### 给父会话的最终输出

**Verdict：四项 v1 问题已修正；v2 尚需补一处 outbox 交付遗漏。** 最后交付路径必须携带同一事实：直接 check 看得到回收失败，而后台回执看不到，会让最常用的长任务路径丢掉异常说明。

candidate-v2.json 的 20 个源码摘要全部与实际文件一致。本轮复核统一终态 finalizer、启动截止/迟到返回、Node 状态合并、迁移信封恢复及测试日志；不修改业务文件，不调用生产或真实会话。

v1 四项闭合：① tracked 正常终态和 ready final 均调用 finishTrackedRelay，Close 10 秒有界，失败保锁并独立保留业务 done/failed 与 close_failed；持久化错误返回。新增 EventResult/EventError × Close 报错/挂住四格及 ready final 持久化错误测试。② 迁移说明前缀后仍锚定真实信封，测试使用实际 retiredConversationNotice；本实例重复原反例已返回正确请求，未框定引语仍拒绝。③ pending 在更新 execution 之前及串行 mutation 内核旧 stopped/finished/终止 reason；本实例原样重放 v1 反例，结果保持 outcome_unknown/stopped。④ running/starting 改为“最近一次记录”，不再凭陈旧活动宣称当前存活。

启动新增保护成立：startTrackedRelay 在 ctx 到期返回，迟到 session 只调用 Close、不 Send；启动归属未知仍保锁。测试覆盖延迟启动最终回收及第二请求 busy。一个永不返回的第三方 StartSession/Close 调用仍可能留下等待中的 Go goroutine，调用方无法强杀任意函数；本批保证请求控制流有界和不并发重放，不能宣传所有不合作后端物理零残留。

**剩余 P2：`/Users/xuke/githubProject/monster/studio/spikes/cc-connect/keith-mcp/src/server.mjs:825-828` 的 enqueueIfAbandoned 对 done 仍直接使用 job.result；只有 settleJob:1091-1092 拼接 close_failed 的 executionDetail。** 当后台长任务完成且执行器回收失败，outbox 的成功正文会丢失该说明，后续随任意 MCP 调用取件也不经过 settleJob。最小修复：成功结果格式化函数供直接交付与 outbox 共用；补 deferred done+close_failed 的真实 outbox 自动交付回归，核业务正文与回收异常都在、版本仍幂等。失败结果已走 failureMessage，不需要扩大改动。

实际日志：node-full-3 已结束，283/283 通过；go-all-except-baseline 的 core 与 agent/codex 均通过；go-review-fixes -race 通过；evidence-regression-final 8/8；native-compaction-final passed=true。go-baseline-full 重现五项路径相关失败；go-baseline-delete-replay 的 20 次运行通过，因此不能把第六项 DeleteMode 时序失败写成“已在基线复现”，只能记首次偶发、当前重跑未再现。修复后排除五项已复现基线失败的全量包测试已过，不为该未复现旧偶发继续扩大本批业务面。

仍保留交付边界：原生 compact fixture 证明钩子事件和 task-evidence 注入，不等于真实服务最后加载与真实 codex_hook_bridge 链路全部验收；共享 Go/Node 未安装。原任务业务与 gate 不在此审查的执行范围。hook 源、原生原件定位和正式运行生效分别报告，不以离线通过替代安装验收。

### 核心假设

v2 文件冻结与主代理回执一致；同 request 不自动重发，关闭未知保锁是有意选择。业务终态与执行器回收证据保持独立。

### 可能出错的地方

把“业务已完成”当作全部交付已完，导致 outbox、查询和审计三个消费者的异常投影不一致。

### 本次哪里思考得不够

没有写业务测试运行新 outbox 反例；代码两个明确分支直接证实差异，新增回归由父会话完成。未检查运行中的共享服务。

### 如果 N 个月后证明决策错了，最可能的根因

下一轮只修直接调用的路径，后台交付消费者继续沿历史格式拼正文；这是消费者遗漏，不是状态枚举数量不足。

### 北极星触达

#3：已修反例与新残余分开结算，不以全量绿灯覆盖确定的交付分支差异，也不把一次未复现的基线时序失败假记为根因闭合。

### essence 对齐自检

- 对位：anchor-protects-retrieval-not-integration、control-flow-vs-fact-supply；原卷本批已物理读取。回收失败原件正确，某条交付投影仍丢事实。
- 反向张力：separation-need-is-not-topology-verdict 约束改动为复用格式化函数，不另建状态/通知系统。
- cross-check 关键词沿本批已读取原卷；新增物理证据为 20 文件 SHA、同形反例回放和最终测试日志。

无 essence 候选。仅写本 reflection，未提交、推送、安装、重启或业务修改。
