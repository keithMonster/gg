---
date: 2026-05-19
slug: cgplatform-contract2-network-isolation-rejudge
summoner: cc-space
northstar_reach: "#3 决策超越直觉（凭借物理拓扑事实推翻自己 v0 立的契约，而非守住沉没成本）"
status: substantive-decision
---

# Reflection: cgPlatform 契约 2 网络隔离层重裁（B′）

### 给父会话的最终输出（必填）

**裁决：采纳 B 方向，定为 B′（GRANT 单层物理隔离 + 网络层补偿控制）。否决 A / C / D。**

契约 2「网络隔离层」半边消解；契约 2 降为「pmAppGuard 半边 + 编排网络（带补偿控制）」；`--internal` 从 integration-contract §3 移除。横向隔离承重责任全部、显式让渡给契约 1 MySQL GRANT。

**核心理由**：
1. 契约 2 v0 `--internal` 隐含"PM 应用 DB 在 docker 网络内"假设，已被 prod 三独立症状证伪——cgPlatform 在 `db.cgboiler.com:9033`，与 cgManager/wflow/cgdata 同一台外部 MySQL 实例同 host:port。`--internal` 这把刀的粒度是"网络可达性"，要切的边界是"同一 host:port 内的库级权限"——刀与对象不在同一维度（metric-vs-pattern level confusion）。
2. 同 host:port，TCP/网络层物理上永远区分不了"连 cgPlatform 库 vs cgManager 库"（OSI 层级决定）。库级区分只有 MySQL GRANT 能做，且契约 1 GRANT 已 prod 实证 1142/1143 = MySQL 内核级强制 = 真隔离非纪律层。
3. v0 的"双层"实质是「1 真层 GRANT + 1 在生产必须关否则业务死的层 --internal」= 实质 1 层。B′ 不是降级，是把"1 真层 + 1 幻觉层"诚实化为"1 真层 + 明确标注的补偿控制"。

**否决 A/C/D**：C 物理不可行（共享实例不能迁入网络）；D 给 --internal 开后门 = 隔离语义自相矛盾；A 的 iptables 层依旧做不到库级区分（单 IP:port 放行 = cgManager 通道也放行），它真正能加的是"防容器横向扫内网"——这有价值但是主机网络基线，不是契约 2 隔离承重；升格它会重蹈"纸面双层"幻觉 + 易漂移文本承重（撞 execute-untrusted-code-never-holds-prod-trust 那滴我两天前刚立的反模式）。A 的合理内核降格为补偿控制收纳。

**单层化的硬前提（不可放过）**：GRANT 成为唯一横向锚点 → 契约 1 `cgplatform_create_app_db.py` 必须在建库后**自动用新账号反向验证**（`SELECT cgManager.users` 必须抛 1142、跨库写必须抛 1143，失败则 deploy 中止）。把"GRANT 写对"从信任脚本作者升级为物理核验通过才放行。无此闸门 = 单层裸奔，B′ 不成立。

**补偿控制（B′ 的"′"，deploy 一行参数级，OCCAM）**：
- `cgplatform-net` 改普通 user-defined bridge + ICC 关闭（`--opt com.docker.network.bridge.enable_icc=false`）→ 拿到 --internal 真正想要的"容器间不互通"
- `docker run -p 127.0.0.1:$PORT:$PORT` 绑 loopback → 端口只对宿主 nginx 暴露不裸暴露公网
- iptables 容器出向白名单：v1 触发项（非 MVP 强制），显式标"纵深防御补偿，漂移不构成契约违约"——防再造纸面双层幻觉

**辐射清单 7 项**（详见 final message 表格）：① cgplatform-deploy.sh 去 --internal + ICC false + 端口绑 loopback ② integration-contract §3 改 network 语义 ③ pm-paas-platform.md 契约 2 改名+删"双层" ④ cgplatform/CLAUDE.md 软硬层 ⑤ thread cgboiler-pm-sandbox 追条目+留 v0 盲点教训 ⑥ 契约 1 脚本加反向验证闸门（B′ 硬前提）⑦ cgboiler 议题台账契约 2 状态。

**v1 触发 + 回审锚点**：第 2 个 PM 应用接入 / 任一 PM 应用需出公网 / cgPlatform 与 cgManager 不再同实例（=本裁决物理前提改变，需重审）。回审日 2026-06-19 或拓扑变化先到者。

### 核心假设

1. cgPlatform 与 cgManager/wflow/cgdata 同一台 MySQL 5.7 实例同 host:port（父会话给定 + huasheng prod cron 实证），这是全部论证的物理地基。
2. 契约 1 GRANT 的 1142/1143 是 prod 实证（父会话给定），是 MySQL 内核级强制而非纪律层。
3. 容器间需要隔离的真实需求存在（多 PM 应用横向），故补偿控制 1（ICC false）是真需要保留的那点价值，不是冗余。

### 可能出错的地方

最可能崩点：辐射项 ⑥（契约 1 反向验证闸门）若父会话只采纳"去 --internal"而漏掉"加反向验证"，则系统从"假双层"掉进"真单层裸奔"——比 v0 更危险（v0 至少 --internal 在 nginx 不可达时附带挡了外部直连）。这是本裁决唯一致命依赖项，必须强调它不是可选增强。概率：中（辐射清单长，闸门项排第 6 易被当"后续优化"）。

### 本次哪里思考得不够

未物理核验 huasheng prod 容器的实际 `docker run` 参数（第二个 grep 命中 cgboiler 噪音数据没拿到）——但该事实在父会话 prompt 中已给定且标注 prod 实证，按"父会话给定的 prod 实证不需 gg 复核"处理，非盲区但留痕。未深究 ICC=false 在 user-defined bridge 上是否需配合 `--internal` 之外的 iptables（docker user-defined bridge 默认 ICC 行为版本差异），父会话实施时需在 prod docker 版本上验证 `--opt enable_icc=false` 生效。

### 如果 N 个月后证明决策错了，最可能的根因

契约 1 反向验证闸门没落地（辐射 ⑥ 被降级），某未来 PM 应用 GRANT 写过宽（`cg_*.*` 而非 `cgPlatform.cg_meetos_*`），单层隔离静默失效，PM 应用读到 cgManager 业务数据——fallback-detectability：失败静默直达终点，无第二层兜底。

### 北极星触达

#3 决策超越直觉——直觉/沉没成本会守住自己 v0 立的"双层"契约（认输叙事的反面：守成）。本裁决凭物理拓扑事实推翻自己两天前的设计，识别"双层"从来是幻觉而非削弱。

### essence 对齐自检（必填）

- **本决策跟哪几滴 essence 对位**：`execute-untrusted-code-never-holds-prod-trust`(2026-05-18，PM 可控代码执行环境的隔离承重必须物理强制非围栏文本，直接定 A 否决与契约 1 反向验证硬前提)；`physical-anchor`(2026-04-16，物理事实压设计意图——prod 三症状证伪 v0 假设)；`metric-vs-pattern`(2026-04-19，网络隔离是 pattern、"不能碰 cgManager"是 metric，强行用前者实现后者是 level confusion)；`abstraction-tax`(2026-04-15，--internal 的"强物理保证"抽象在共享 DB 边界处付出"应用不可用"债)；`fallback-detectability`(2026-05-06，单层化后失败静默直达终点)。
- **本决策是否在某条 essence 上反着走**：潜在张力——`reversibility-not-permission`(2026-05-06) 主张权力分层按可逆性。本裁决移除一层防御看似降可逆性，但实际 v0 那层在生产从不生效（开了业务死），移除幻觉层不降真实可逆性，张力消解非反走。无真实反走 + 议题性质（拆假双层非削真防御）决定。
- **cross-check 用的关键词**：execute-untrusted-code / physical-anchor / fallback / metric-vs-pattern / abstraction-tax / reversibility（grep memory/essence.md 命中以上 slug 原文）。

### essence 候选（可选）

- slug: network-cannot-cut-what-shares-tuple
- 一句话: 隔离机制的刀只能切它那一层能区分的维度——网络层切不开共享 (host,port) 元组内的库边界，强行用它做库级隔离=造一个开了业务死、关了才能跑的幻觉层；"双层防御"的纸面计数不等于物理层数，真层数=在生产实际生效的层数。
- 是否已 append 到 essence.md: Y

### 外部锚点（可选）

- `~/githubProject/cc-space/threads/cgboiler-pm-sandbox.md` ← 主体协作叙事（契约 2 裁决条目待父会话落档）
- `~/githubProject/cc-space/inbox/briefs/pm-paas-platform.md` ← 契约 SSOT
- `~/githubProject/cc-space/cgplatform/integration-contract.md` §3 ← 三对话共用契约
