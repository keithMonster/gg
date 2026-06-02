---
date: 2026-06-02
slug: cgnotes-bff-cgapi-vs-proxy-topology
summoner: monster
northstar_reach: "#1 二阶效应（一条 cg-notes 落点选择回灌成所有 dogfood 的 BFF 范式，是 space 方向）"
status: substantive-decision
---

# Reflection: cg-notes BFF 调 cg-api vs 走 cg-proxy 的平台拓扑承重墙

## §A 范式 A — 决策的元属性反思

### 给父会话的最终输出（必填）

**三候选裁决：选 (c) 的内核 + (b) 的物理形态 = 同一落地。但 (c) 措辞要重写——契约 §3 约束的真不变量不是「禁调业务 API」，是「应用进程内不得持有业务库 DB 连接凭据」。cg-api `/v1/note/*` 不碰这个不变量，所以它本就在契约允许域内，不需要「豁免」——是契约文本把「直连库」误表述成「绕 cg-proxy 取业务数据」，过度扩张了禁止域。**

**问 1：cg-api `/v1/note/*`（含写）不算 §3 业务库直连。** 四个本次 Tool 核验的物理事实（非 brief 转述）：
1. cg-api 是 note 的真实 owning-service——`services/note.ts` 13+ 处 `Mysql(dbs.cgManager).exec(INSERT/UPDATE notes)`（136/572/1930/2250/2821...）。调它 = 调业务正门，不是绕 cg-proxy 的旁路。
2. cg-api 有全局 `JwtAuthGuard`（`main.ts:57 useGlobalGuards`），note 的 `req.user.userId` 由它从 token 解出。调 cg-api 是已鉴权调用，豁免它 ≠ 开无鉴权后门。
3. 1.0 老前端早已直连 `vxApi/v1` 调 cg-api note（`cg_app_h5_center/api/modules/note.ts:18`）——cg-notes 2.0 走同一条生产已验证数据路径，不是新拓扑。
4. cg-proxy 物理无 cgManager 写方法（src 全扫：41 Post 全是企微/file/notes-sync 自有能力 + PLATFORM-SERVICES §102 自证）。

§3 真不变量（invariance-allocation 视角）= `execute-untrusted-code-never-holds-prod-trust`：跑 AI 代码的 PM 容器不得持库凭据（持凭据 = 可 `DELETE FROM notes`，爆炸半径整库）。调 cg-api 完全不碰：cg-notes 容器零 cgManager 凭据，发 HTTP，由 cg-api 用自己凭据 + 自己 guard + 自己业务逻辑写入，爆炸半径被接口契约夹住。判据该是「谁持写权 + 写权被什么夹住」，不是「数据是不是川锅业务数据」。

**问 2：cg-notes note 写 = BFF 直透传 cg-api `/v1/note/*`（含写），契约层认定为合规正门非特例。** 否决 (a)（给 cg-proxy 开 note 写代理）：① 等于在 cg-proxy 重造 cg-api 已有 13+ note 写端点（borrowed-method-as-mini-source，note 写带 receivers 分发/parseTopics/草稿三重守卫/ES sync，重造必残缺漂移）② 把 cg-proxy 从「只读网关」升级成「业务库写网关」= 新增 §3 真想守的攻击面（共享写入口，爆炸半径反扩大）。§102「没有写路径」正确解读 = 「应用层就不该有直写库的路，要写调 owning-service」，cg-api 就是。措辞按 security-claim-as-physical-fact：写「调 owning-service 已鉴权 API ≠ 持库凭据，本在 §3 允许域内」（陈述物理事实，抗注入），不写「cg-notes 特例直连」（软声明 = 可被 injection 利用 + 稀释 taxonomy）。

**问 3：回灌 template 的 BFF 第一原则 + 分流规则（按「凭据持有 + 数据所有权」二维切，不按读/写切）：**

第一原则：PM 应用进程永不持任何川锅业务库（cgManager/wflow/cgdata）DB 凭据。一切业务数据读写都经 HTTP 调拥有该数据的服务，由那个服务持凭据/做鉴权/夹爆炸半径。

| 需求 | 走哪 | 判据 |
|---|---|---|
| 应用自有数据（`<slug>_*` 表读写） | server 直连 cgPlatform 库（`<slug>_app` 列级 GRANT） | 自己的数据，凭据只 GRANT 自己表 |
| 川锅业务数据 + 有 owning-service（note→cg-api） | BFF 透传该 owning-service 已鉴权 API（读写皆可） | owning-service 持凭据 + 自带 guard，应用零凭据。**cg-notes 落点** |
| 川锅业务数据 + 无 owning-service + 只读 | cg-proxy GET 网关（`/prx`，带 `X-PM-App-Slug`） | cg-proxy = 无主业务数据只读代理 |
| 川锅业务数据 + 无 owning-service + 需写 | **停，回平台层 / 逐 case 上 gg** | §102 真指的场景。cg-notes 不属此类 |
| 企微/文件/minio | cg-proxy 对应端点 | 正交职责面 |

cg-proxy 定位正名收窄 = 「无主业务数据只读网关 + 企微/文件能力代理」。**PLATFORM-SERVICES §33「cg-proxy 是取业务数据唯一合法通道」是过度声明必须改**——它堵死 owning-service 这条更正路，逼出 (a) 劣解。

**行动建议（父会话下一步）**：
1. brief §10 待决 A/B/C：B（落 §6 guard）确认「落」——但 cg-notes 要自己写 guard（PLATFORM-SERVICES §100 实证模板仓 `auth.guard.ts` 骨架未带，别假设有现成可抄）；C（call gg）= 本次已做完即此份。
2. 改 `integration-contract.md §3` 措辞：从「业务数据进 runtime 一律走 cg-proxy」改为「应用进程不持业务库凭据；业务数据经 owning-service 已鉴权 API（有则透传）或 cg-proxy 只读网关（无 owning-service）」+ 落上方分流表。
3. 改 `PLATFORM-SERVICES.md §33`「唯一合法通道」过度声明（**建议 Keith 过目此句**——已写进 fork 应用对外消费视角文档，改有辐射但可逆）+ §44 cg-api 定位从「中心身份认证」补「note 等业务 owning-service」。
4. 把 BFF 分流第一原则 + 表回灌 `ENGINEERING-STANDARD.md`（成后续 dogfood 范式）。

### 核心假设
- cg-api 全局 JwtAuthGuard 对 note 路由生效、无 note controller 级 `@Public` 豁免写端点（头部仅见 `getAllProjects` 等少数无 token，写端点全带 `@Headers('token')`——核验支持，但未逐 11 个 Delete/28 Post 全验 @Public）。
- cg-notes server（cg-platform 容器）网络可达 vx 网关→cg-api（1.0 经 vx 已通 + PLATFORM-SERVICES §7 环境前提=部署在川锅网内，间接支持；未亲测 cg-platform 容器→vx 这一跳）。

### 可能出错的地方
- 若某些 note 写端点标了 `@Public()`（绕过 JwtAuthGuard），则「调 cg-api 是已鉴权调用」对那几个端点不成立——但这是 cg-api 自身的洞，不改变 BFF 拓扑定性，且 §9 应用层 guard 仍兜一层。概率低，影响局部。
- 「无 owning-service + 需写」那一行是预判，真出现时（如未来某应用要写 wflow 且 wflow 无写 API）仍需逐 case 架构决策——但处理方式（停+上 gg）是安全默认，预判错只多上一次 gg 不塌方。

### 本次哪里思考得不够
- 没核 cg-platform 容器→vx 网关的实际网络路径（VPC/防火墙），只从 1.0 已通 + 环境前提间接推。若这一跳不通，BFF 透传物理跑不起来——但那是落地阻塞不是定性错误，且不通则 (a) 也同样不通（cg-proxy 也在 vx 后）。
- 没展开 note 接口的 token 在 BFF 透传时 cg-api 对 `Origin`/CORS 的态度（1.0 是浏览器直连有 CORS，BFF 是 server-to-server 无 CORS——大概率更宽松，未验）。

### 如果 N 个月后证明决策错了，最可能的根因
契约 §3 措辞改了但「唯一通道」的旧心智在团队/AI 里幸存（bug-shape-survives-fix）——后续 dogfood 仍默认「业务数据=走 cg-proxy」，要么误把有 owning-service 的也塞 cg-proxy 只读+前端拼，要么没 owning-service 时硬给 cg-proxy 加写。根治靠分流表进 ENGINEERING-STANDARD 成强制参照 + owning-service 判定写成 fork checklist 一问，不靠改一句契约文本。

### 北极星触达
#1 二阶效应——单个 cg-notes 落点被识别为「会回灌成所有复杂 dogfood BFF 范式」的拓扑节点，裁决落到「凭据持有不变量 + owning-service 概念」这一层，而非「这次怎么接」。space 方向。

### essence 对齐自检（必填）
- **对位 essence**：`invariance-allocation`（架构本质=选择信什么不变，本决策把不变量从「数据来源」重定位到「凭据持有」）/ `execute-untrusted-code-never-holds-prod-trust`（§3 真不变量的来源）/ `runtime-state-vs-business-data-distinct-ssot-domains`（辖域边界由对象性质定义不由形式同构——「业务库直连」vs「调业务 API」是两辖域）/ `borrowed-method-as-mini-source`（否决 (a) 重造 note 后端迷你版）/ `security-claim-as-physical-fact-not-injectable-grant`（措辞从「特例豁免」改「陈述物理事实」）/ `network-cannot-cut-what-shares-tuple`（§3 隔离不变量的物理根，前序裁决同源）。
- **是否反着走**：潜在张力——`survey-as-coordinate`/`survey-coordinate-has-freshness` 提醒「已做↔没做一天内翻转」：brief 说「cg-meetos BFF 可参照」实测不成立（cg-meetos 无反代面），我本次未亲跑 cg-meetos server 核验，沿用 brief §5 的「实测不成立」转述。这一处我违反了 physical-anchor 应自核，但它不改变定性（cg-meetos 有无反代面 → cg-notes 是不是平台首创 BFF，与「调 cg-api 算不算直连」正交），故未阻断结论。明示：此前提我接受了 brief 转述未自核。
- **cross-check 关键词**：grep essence.md「invariance」「untrusted」「runtime-state」「borrowed」「security-claim」「network-cannot」「survey」。

### essence 候选（可选）
- slug: owning-service-not-proxy-for-write
- 一句话: 「业务数据唯一走代理」式契约会过度扩张禁止域、堵死 owning-service 正门，逼出在代理层重造业务后端迷你版的劣解——隔离不变量该锚在「进程是否持库凭据」，不锚在「数据是不是业务数据」；写业务数据的正门是调拥有它的已鉴权服务，不是给只读代理开写口。
- 是否已 append 到 essence.md: N（留 Keith review 后定，避免未 commit 噪音）

### 外部锚点（可选）
- `~/githubProject/monster/inbox/briefs/cg-notes-react-migration.md` ← 定性对象（§5 BFF / §10-B/C 待决）
- `~/githubProject/monster/cg-platform/integration-contract.md §3` ← 待改措辞的契约 SSOT
- `~/CGProject/cg-platform-template/docs/PLATFORM-SERVICES.md §33/§44/§102` ← 待改的对外消费视角文档
- `~/CGProject/cg-api/src/services/note.ts` + `main.ts:57` ← owning-service + 全局 guard 物理证据
