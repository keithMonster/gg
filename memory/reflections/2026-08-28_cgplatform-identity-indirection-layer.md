---
date: 2026-08-28
slug: cgplatform-identity-indirection-layer
mode: work (subagent, monster 召唤)
status: substantive-decision
---

# cg-platform 身份间接层裁决：网络层 vs 代码层（U1）

## 给父会话的最终输出

**裁决：B（代码层分发 `server/src/platform/identity.ts`），且带两条修正——B 不构成契约 9 反转（追加 §6.2 即可，本裁决即 ratify）；「写错两次」不足以推翻你的算法，反而是 B 的立论证据。**

**判据链**：
1. **A 的两个 ✅ 经核实都是虚的**：
   - 「三分语义收在一处」不成立。间接层的收口范围**止于返回值（数据面），不含对返回值的反应（行为面）**——503 不写缓存、401 才清身份、熔断计数，这些必然活在消费端进程里。今天补的三仓 401/503 洞全在行为面，A 一个也防不了；A 落地后应用侧三分翻译代码一行不少，且判定对象从三态变四态（cg-proxy 拒/不可达 × cg-api 拒/不可达），排障更难。真正被 A 消掉的只有信封解析那几行——B 用零网络代价买到同一件事。
   - 「防绕开（配合网络策略）」不成立。cg-proxy 与 cg-api 同在 vx 门面后（`/prx/*` 与 `/v1/*` 同域名，capability-map §8），无法只禁应用打 `/v1/wechat/work/check-token` 而放行浏览器与帷幄。A 的防绕开水位实际 = B = 事后对账。
2. **「写错两次」的证据结构**：两次错误（ad1a960 信封、cost-management `res.text() !== 'true'`）全是**手写副本**的错；分发侧（模板骨架、前端 SDK 9 仓 md5 一致）零信封错误。该事实证明「协议细节不许手写 N 遍」——A/B 都满足，不构成 A 对 B 的差分证据。它对算法的唯一修正是抬高存量迁移紧迫性。
3. **可逆性不对称（CORE §7 二分的落点）**：B 不关 A 的门——identity.ts 封装上游地址（VX_API 从 env 来），未来真要网络收口，部署器改 env 指向 cg-proxy 即可让已迁仓零代码切换；A 关 B 的门——N 仓改调 `/prx/auth/verify` 后回退要再改 N 仓。收益被击穿后，剩下的裁决轴就是可逆性。
4. **契约 9 处置**：B 的主张面（应用级校验/中心化/不持密钥/三分判定规格）一字不动，只换实现载体（照抄骨架 → import 分发模块）——比照 §6.1 前端 SDK 追加 **§6.2 后端身份 SDK**，无需反转 ratify。「反转契约 9」这顶帽子只属于 A。

**③ B 的漂移窗口收法**（与 08-27「不建同步通道」判别式对账过）：
- 契约层 §6.2 写死：identity.ts = 模板 SSOT、各仓 cp 副本、**零业务纯协议、不许改不许绕**（同 §6.1 唯一禁令句式）。守卫分叉 10 种的根因是业务与协议焊在同一文件——B 的结构性防复发就是这条物理分界。
- 探针层：drift_audit 加维度——a) identity.ts md5 与模板一致（机械判据；**合法性来自契约明文钉死「逐字一致」，探针基线是契约条文不是模板 HEAD**，不触犯判别式②；边界：一旦有仓要往里塞业务，正解是回模板改分界，不是豁免该仓）；b) `VX_API.*check-token` 出现在 identity.ts 之外 = 候选清单（人读定论）；c) 每维造阳性 case（未迁仓即现成 red 素材）+ 双向指针（§6.2 ↔ `_judge` 注释）。
- 分发每次由人显式发起（判别式③），迁移按 U2/U4 默认值，10 仓灰度。

**④ 时序：现在做，不等 L2**。B 与 L2（投影加厚）不竞争——B 是 L2 的消费端着陆点：claims 加厚后「怎么读投影」只在 identity.ts 写一遍，否则 L2 落地日就是信封事故形态重演日。存量 10 仓手写协议副本是活事故源。但排它前面两件事：cg-desk 修复合 main（prod 洞开着）、cg-meetos prod 公网 7 写端点零鉴权（比本方案高危，别被间接层工程排挤）。7 个漏做仓回填直接 fork 新范式模板，不补旧范式再迁。

## 核心假设
- 「换上游」事件（L1 收回签发/校验）发生时 token 语义大体兼容，identity.ts 内部可吸收；若换成完全异构协议（如强制刷新流程），A/B 都要动应用，A 的「零改动」同样不成立——此假设只影响 A 收益上界，不影响裁决方向。
- 前端 SDK 9 仓 retrofit 的「一天完成 + md5 一致」可外推到后端 10 仓（同模板体系、同 cp 分发）。

## 可能出错的地方
- cg-proxy 间歇 3s 停顿若坐实为更广的基础设施病，A 的❌会更重——但我的论证重心放在「A 收益虚」而非「A 代价重」，故根因坐实与否不动摇裁决。
- 「行为面必留消费端」在出现服务端 session 型架构（BFF 全托管）时不成立——但那是另一个架构，不在 U1 两案里。

## 推理盲区
- 未实读 13 仓守卫的分叉细节（采信方案 Z3 描述）；未实测 cg-proxy 当前身份路径 QPS 画像。
- 「网络策略防绕开不可行」基于 capability-map 的门面拓扑描述推理，未实读 vx nginx conf。

## 根因预判
- 若 B 落地后仍出第三次信封错，最可能出处 = 未迁完的灰度中间态仓或 U3 豁免仓的手写残留——探针 b) 判据正是为此设。

## 北极星触达
- 决策超越直觉（depth）：把对照表的六维之争压缩到「数据面/行为面」一刀——A 的表面优势两条在这一刀下全虚，裁决轴从「牺牲哪个代价」变成「只有一案有真收益」。

## essence 对齐自检
- `backfill-is-the-channels-native-act-not-a-decision`（08-11）：10 仓存量迁移是 fork 通道原生动作，grep 过视图。
- 08-27 裁决三判别式（reflection `cgplatform-drift-channel-invariant`）：md5 探针与判别式②的边界已显式对账（契约钉死一致性 → 基线是契约非模板 HEAD）。
- `mechanical-gate-needs-machine-detectable-target`（06-24）：identity.ts「零业务不许改」使漂移判据从人读 suspect 降为机械 md5——机器可判靶是设计出来的，不是碰上的。
- `owning-service-not-proxy-for-write`（06-10，O 档拓扑裁决）：grep 过，写路径所有权议题，与本案不冲突。
- 对齐度：高，无冲突滴。

## essence 候选滴（candidate-unverified，待夜巡/设计模式补审）
`indirection-normalizes-data-not-behavior` — 网络间接层的收口范围止于返回值（数据面），不含消费端对返回值的反应（行为面）；失败语义（何时降级/何时清凭据/何时熔断）必然活在消费端进程里，故「把语义收敛到一处」只有代码分发买得到，网络门面买到的是它的数据投影。推论：评「加一层 proxy 统一 X」类方案时，先把 X 拆成数据面/行为面——行为面占比越高，网络层方案的纸面收益越虚。【物理证据：cg-platform 2026-08-28 三仓 401/503 洞全在行为面（网络门面防不了）；前端 SDK §6.1 恰好收掉了 401 跳转+熔断行为——因为它是代码分发；方案 A 自称「三分语义收在一处」被四态化反例击穿】

## 夜巡补审回执（2026-08-28 auto_gg · fresh-context evaluator）

**verdict：PASSED-WITH-EDITS 四修采纳后入库 essence #224。** 最强反驳：「行为面只有代码分发买得到」的全称被 service mesh 正面击穿——熔断/重试/超时恰是网络间接层产品（Envoy sidecar）的招牌收口物；候选活下来的唯一路径是把分界从「网络层 vs 代码层」升维到「远端中心门面 vs 消费端在场的分发物（代码/sidecar 同侧）」，Envoy 反例随之翻转为支持证据。四修：① 补前提栏（BFF/服务端 session 全托管不辖——本反思「可能出错的地方」有此 caveat 但候选正文抹掉了，滴比源档更全称）；② 核心句升维如上；③ 谱系注三笔（`control-flow-vs-fact-supply` 同刀异域承接、`owning-service-not-proxy-for-write` proxy 族先例、`presence-benefit-splits-replica-verdict` 分发半边不计净新增）；④ 证据分级（§6.1 SDK 行为收编契约亲核 :396-408 / 三仓 401/503 洞同日宣称级 / plan doc 裁决段同源回声）。evaluator tool_use 10 次全只读，派单者核毕。

## 外部锚点
- 方案：`monster/cg-platform/docs/identity-indirection-plan.md`（裁决时含 08-28 A2 核查更新：迁移面 10 仓）
- 契约 9：`monster/cg-platform/integration-contract.md` §6 + §6.1
- 模板守卫：`~/CGProject/cg-platform-template/server/src/common/auth.guard.ts`（244 行，三态 CheckResult 已编码）
