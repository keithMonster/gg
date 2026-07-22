---
date: 2026-07-22
slug: cg-dev-console-m32-inf03-inf04-boundary
summoner: monster (platform-help / 叶维政 302855 M3.2 缺口回应)
northstar_reach: "#3 决策超越直觉（识破 INF-04 签名缺口是从 SLSA/cosign 开源默认继承来的、当前单方全控链路下承重目的没落地——威胁模型未显式，签名是理论生造的缺口，不是设计缺口）"
status: substantive-decision
---

# Reflection: cg-dev-console M3.2 INF-03（私有不可变制品）+ INF-04（签名密钥）契约边界裁决

### 给父会话的最终输出（必填）

**总裁决**（Keith 没看过的坐标，放在最前）：**INF-04 是伪命题**——签名承重的经典场景是"多方共享 registry / 跨组织 provenance"（cosign/sigstore/SLSA 原生），川锅是**单方全控**链路（cg-dev-console 是唯一生成方、私有 MinIO 是唯一存储方、平台 Agent 是唯一消费方）。签名在这条链路里除"Agent 侧存储代理被内部人篡改 object"这一极小场景外**没有可承重的攻击面**——INF-03 的私有桶 + object-lock + presigned URL 短时授权 + HTTPS + Bearer 已经封住完整性+机密性。**签名不是设计缺口，是 V3 原文从开源默认继承来、未审视的理论缺口**（essence `theory-gap-without-data` + `security-invariant-encodes-an-owner-set-threat-model`）。这是 Keith 初判里 B 段"应用 vs 平台 vs GitLab tag"三选一没往回问的一层——**先问要不要签，再问怎么签**。

INF-03 存储侧承重成立，走"新建独立私有 MinIO 桶 + 应用直连 SDK（无 platform-services 门面）"最轻治理。

---

## 裁决 A（INF-03 存储侧）：新桶 + 应用直连 + **不上 SDK 门面**

**选**：新建独立私有 MinIO bucket `cg-platform-releases`（复用现有 MinIO 物理实例），policy = non-public / versioning=on / object-lock 或 IfNoneMatch 幂等；storage_key 采用 Keith 初判结构 `<slug>/<environment>/<releaseId>/<appId>/<fileName>`（tenantKey 折进 environment 合理，slug 前缀留下——原因见下）；presigned URL TTL 15 min 参数化；cg-dev-console 应用**直连 MinIO SDK**（server/src/config 声明 MinIO endpoint/key），**不上 platform-services 统一 SDK/HTTP 门面**。

**理由（essence 对齐 + 反驳 Keith 初判具体错在哪）**：

- `separation-need-is-not-topology-verdict`（06-10）：先试最轻治理形态，物理证据证明装不下再造墙。**第二个消费者还没出现**（M3.2 首个签发方就是 cg-dev-console，未来是否第二个应用要发 Release 未知），premature 起 platform-services 门面 = 造未来的墙。**每次造墙成功都在喂下一次**——起了 platform-services，第二个应用的 sign / releases 都会顺手往里塞，抽象层膨胀。
- `tool-elevation-as-occam`（05-06）**边界**：Keith 初判问"是否要统一提供 SDK"是把它当默认动作。essence 有 06-22 打过的边界注："第二个消费者出现时上提"是判据，**不是"预感未来会有第二个"就上提**。当前 N=1，OCCAM 判无门面。
- **反驳 Keith 初判**：Keith 写 storage_key 时说"平台承桶去掉冗余 slug 前缀"——**保留 slug 前缀**。理由：`ownership-by-facet`（05-06）+ 未来独立签发方（假设的第二个应用）加入时，slug 前缀是**跨签发方隔离锚**（每个签发方能被授独立的桶 prefix policy，不用 releaseId 混装）。去掉 slug = 假设签发方永远只有 cg-dev-console 一家，是把当前实况当不变量（违反 `invariance-allocation`——选真正稳定的不变量）。存储代价：4-5 字节 × Release 数，可忽略。
- `paradigm-not-feature-completeness`（05-14）：不引入 COS。引入 COS = 引入新云依赖 + 新凭据面 + 新 SDK 熟悉度，**收益仅"更弹性"**——川锅现有 MinIO 有本轮全部承重能力（private / versioning / object-lock 需核版本 / presigned URL），范式已足。

**契约动作（写入 `integration-contract.md` 第 8 条 candidate）**：
- 桶名 `cg-platform-releases`，policy 已如上
- storage_key layout `<slug>/<environment>/<releaseId>/<appId>/<fileName>`
- 平台侧动作 = 建桶 + policy + 发放 MinIO account/key 走 secrets-catalog（per-app 后缀键 `MINIO_RELEASES_KEY__<slug>`）
- 应用侧动作 = server/src 声明 MinIO endpoint/key，SDK 直连；上传路径固定；下载走 presignedGetObject TTL 15 min
- 明确非契约（今天不做）：平台侧 `POST /platform/releases/artifacts` HTTP 门面——第二个签发方应用出现时再上提

**触发升级/回撤条件**：
- ➕ 升级到 platform-services SDK 门面：第二个独立签发方应用出现（不是"cg-dev-console 增加签发种类"，是"另一个应用也当 Release 签发方"）
- ➕ 升级到 COS：MinIO object-lock 物理不支持（需 call platform-help 核 MinIO 版本，见文末必核清单）；或平台层出现"跨云容灾"目标层需求（Keith 拍）
- ➖ 回撤桶方案：从未有过——本轮不动 wflow 那 7 个桶（Keith 初判也不动），风险面隔离

---

## 裁决 B（INF-04 签名侧）：**延期挂账 parking-lot，M3.2 首刀不签名**

**选**：拒签。当前 M3.2 Release 阶段**不引入签名**。INF-04 缺口**降级为 parking-lot 前瞻议题**（`cg-platform/docs/parking-lot.md` 新增条），带明确 tripwire。**不做 platform sign 微服务，不做 GitLab signed tag，不做应用容器持私钥**——三个方案全否，因为**签名承重的目的当前不成立**。

**理由（essence 对齐 + 反驳 Keith 初判具体错在哪）**：

- `theory-gap-without-data`（05-06）：没数据（没威胁模型）时找理论缺口=生造。V3 原文的"签名 + 密钥托管 + 轮换"三件套的原生场景 = **多方共享 registry / 跨组织 provenance**（sigstore/cosign/SLSA）。川锅链路 = **单方全控**：cg-dev-console 唯一生成方（其数据库 approvals 表 + Release Compiler 是唯一权威）→ 私有 MinIO 唯一存储方（同 VPC 内平台自管）→ Agent 唯一消费方（平台自管系统账号）。**这条链路里签名要承重"防谁"没有答案**——三方都在同一信任域。
- `security-invariant-encodes-an-owner-set-threat-model`（06-17）：安全不变量把威胁模型（防恶意 vs 防手滑 vs 防传输 vs 防审计不可否认）偷编成定律；**威胁模型是 owner 参数**。V3 原文没说防谁；叶维政 GAP 只说"平台无 KMS/无 Ed25519/无轮换"——继承开源默认清单，**没论证川锅链路里签名的承重承担什么攻击面**。
- **穷尽 INF-03 已覆盖的攻击面**：
  - 传输中被改 → HTTPS/TLS 覆盖（MinIO 都是 https 访问）
  - 存储被覆盖 → object-lock + versioning（INF-03）
  - 越权下载 → 私有桶 + presigned URL 短 TTL（INF-03）
  - Agent 被中间人 → HTTPS + Bearer（Agent enroll 时已有）
- **INF-03 未覆盖的剩余攻击面**（签名的边际承重）：
  - MinIO 侧内部人物理替换 object（有 versioning 也能加新版本）—— 极小概率（MinIO 是平台自管）
  - 存储代理链路（CDN/网关）被投毒 —— 川锅无 CDN、无跨链路缓存
  - 审计不可否认（多方场景才需，单方全控无此需求）—— 川锅无对外审计合规要求（Keith 拍）
- **反驳 Keith 初判**：Keith 初判 B 里"优先复用 GitLab tag signing"和"降级平台 sign 微服务"——两者**在承认签名必要性的前提下**做方案选择。**先要问上层问题**：签名的承重目的是什么？没答案 → 不做。用 `no-fatigue-narrative-for-ai`（04-27）：不给 owner 出局叙事——"总要做一点"的直觉是防御式思维，M3.2 首刀就应该显式**不签**、把签名承重条件挂在 tripwire 上。
- **反驳叶维政方案（应用容器持 Ed25519 私钥）**：**当前范式下确实违 06-10 essence 骨架**——cg-dev-console 是 web-facing 后端（有 HTTP 入口），攻破 Web 后端 = 私钥泄漏 = 签名被伪造。这是 essence 候选 `web-facing-executor-is-untrusted-regardless-of-payload-trust`（06-10 挂账未 append）的直接落点。但**上一层攻击面是**：攻破 web 后端本身 = 攻击者可以自填 approvals.state=APPROVED + 拼恶意 Release + 上传到桶 + 发放签名——**签名不签名都塌陷**。承重的墙不在签名，在 web 后端本身；给一个塌陷点加签名 = `ghost-rules`（04-15）。
- **反驳 GitLab signed tag（Keith 初判 B "优先"路径）**：**范式错配**（`paradigm-not-feature-completeness` 05-14）。GitLab signed tag 是给**代码提交**加签名，验证的是"这段代码从谁的仓库来"。cg-dev-console 的 Release 产物是**运行时配置 JSON**，不是代码，不进 GitLab 仓。签一个不进 git 的东西用 git tag 签名 = 载体错位。**不用查 GitLab CE 是否支持 signed tag**（Keith 的必验清单里问过）——查也没意义，因为签的东西不在 git 里。

**parking-lot 条文（新增至 `cg-platform/docs/parking-lot.md`）**：

> **候选契约「Release 制品签名」（2026-07-22 挂账，源：V3 原文 INF-04 缺口）**
>
> V3 原文要求 Release 制品签名 + 密钥托管 + 公钥分发 + 轮换。当前**单方全控**链路下签名承重目的未显式（cg-dev-console 唯一生成方 / 私有 MinIO 唯一存储方 / 平台 Agent 唯一消费方 / 无对外审计合规），INF-03 已覆盖完整性+机密性攻击面。**不立项**。
>
> **触发条件（任一命中升 thread + 独立 sign 议题）**：① Keith 明示"cg-platform Release 需给外部合规审计（cgboiler 外部审查、监管、客户 SLA）"② 出现第二个独立 Release 签发方且需跨签发方互信 ③ 出现"Agent 侧不完全可信"场景（如 Agent 落在客户机房 / 第三方托管，需签名防运维人员篡改）④ 显式威胁模型定义"防内部人替换 MinIO object"是承重风险面。
>
> **触发时的方案骨架（预挂账）**：按 06-10 骨架"密钥物理不在 web 后端进程可达域"——落到独立签名子容器（cg-dev-console 应用内 sidecar，Web 后端调 `POST http://sign-side/sign`，签名私钥挂 sign-side 容器不挂 Web 后端）。不起 platform-services 抽象（首个签名应用先在自身容器域内治理，第二个应用出现再上提）。**Ed25519 算法保留**（尺寸小、libsodium 覆盖广），公钥走 GET HTTP 分发。

**触发升级/回撤条件（本轮决策的）**：
- ➕ 立即启动 INF-04 契约设计：上面 4 条 tripwire 任一命中
- ➖ 永久归档 INF-04 缺口：M3.2 上线 6 个月内未触发任一 tripwire → 从 parking-lot 移到 `closed/`

---

## 裁决 C（契约立位）：INF-03 = 第 8 条平台契约 · INF-04 = parking-lot

**选**：INF-03 写入 `integration-contract.md` 作为第 8 条契约（`Release Artifact 私有存储`），INF-04 只进 `parking-lot.md`。

**理由（essence 对齐）**：

- `ownership-by-facet`（05-06）：按"面"切归属，不按系统整块归。
  - **存储面**：跨签发方共享（虽然当前 N=1，但存储 policy / bucket 命名 / storage_key layout 是**未来所有 Release 签发方共同遵守**的东西）→ 平台契约。
  - **签名面**：签名密钥的爆炸半径 = 单签发方（cg-dev-console 单应用），不跨应用；即使未来签名启用，也是**应用内业务动作**（cg-dev-console 内部 sign-side sidecar，不出应用容器域），**不需要契约化**——除非 tripwire 触发条件里的"第二个签发方需跨签发方互信"发生。
- **反驳 Keith 初判 C**：Keith 写"归 cg-platform 平台契约（第 8/9 条契约候选）"把 INF-03/INF-04 合并当"契约候选"看。**分开处理**——存储是共享面必须契约，签名是应用面且当前不做。合并 = 8/9 两条一起进契约表 = 未来读契约的人以为"平台承诺提供签名基建"，误导（`stale-observer` 04-15 的前置形态：写下就变成幽灵规则）。
- `fleet-canon-is-sedimentary`（06-22）：舰队 canon 沉积岩，向前传不向后回流。第 8 条契约今天写下 = 所有后续应用继承同结构。INF-03 结构承受得起（`ownership-by-facet` + storage_key 层次已考虑扩展性），INF-04 承受不起（威胁模型未显式，写下的任何结构都是理论生造），故 INF-04 只挂 parking-lot。

**触发升级/回撤条件**：
- 契约 8 (INF-03) 收紧回撤：MinIO object-lock 版本不支持（call platform-help 核）→ 需重新裁 fallback（回退到 IfNoneMatch + 手动 policy 阻止 delete）
- INF-04 从 parking-lot 升契约：tripwire 4 条任一命中

---

## call platform-help 补验的清单（决策不需要，但落地需要）

以下 3 项**不阻断本裁决**（本裁决在物理事实上鲁棒），但落地前需 platform-help 走一趟确认：

1. **MinIO 服务端版本 + object-lock 支持性**：需 MinIO ≥ RELEASE.2020-04-10（object-lock GA 版本）。call 命令 `mc admin info <alias>` 或 `curl <endpoint>/minio/health/live` 看版本头。**降级路径已有**（object-lock 不支持 → IfNoneMatch + bucket policy DENY DeleteObject + versioning=on 三件套等效替代）。
2. **现有 7 个 MinIO 桶 policy 现状**：叶维政声称"全 public-read、无 versioning / object-lock"。call `mc anonymous get <alias>/<bucket>` + `mc version info <alias>/<bucket>` 全部 7 个桶实测。**不阻断新桶决策**（新桶是新建 + 主动配 policy，不受存量影响），但如果存量确实全 public-read，属独立议题：**wflow 桶自身承载真敏感数据吗？是的话是独立的 P1，需另立 thread**（不进本决策）。
3. **叶维政声称的 003_m3_release.sql / releases 表 / signing adapter 完成度**：platform-help 已让他澄清（本次召唤 prompt 说的），核实完成度 = 意图 vs 已做。**不阻断契约决策**（契约是定"未来该怎么做"、不是审"当前做了什么"），但直接影响 M3.2 实施估时——如果叶维政声称已做的其实还没做，本裁决落地需要他新做 storage adapter + registry 桶配置 + api/releases POST 接入 MinIO 上传路径。

**不需要核的（Keith 必验清单里问的、被本裁决消解的）**：GitLab CE 是否支持 signed tag —— 本裁决 B 已通过 paradigm 拒 GitLab tag signing 路径（签的对象不进 git，签名载体错位），核不核都不用它。

---

## 行动序（给父会话 monster 主代理）

1. **立刻**：给叶维政（platform-help sender_id=302855）回消息 —— 见"父会话回消息模板"（下方）
2. **本轮契约动作**（monster 侧文件改动）：
   - `~/githubProject/monster/cg-platform/integration-contract.md` 新增 §7「Release Artifact 私有存储」（第 7 条平台契约；上面章节顺序 §6 是"应用身份校验候选 ⏳"、§7 现空缺；本条落入 §7，不是 §8——原初判编号误）
   - `~/githubProject/monster/cg-platform/docs/parking-lot.md` 新增「候选契约「Release 制品签名」」条目（parking-lot 已有的"候选契约「Agent 调用网关」"格式仿写）
   - `~/githubProject/monster/cg-platform/CLAUDE.md` 「高频动作速查」下新增一行"要发 Release 制品（M3.2）"→ 指向 integration-contract §7
3. **本轮平台侧动作**（Keith 拍板后启动）：
   - 建 MinIO 桶 `cg-platform-releases`（走 mc mb + policy set + versioning enable）
   - 发放 MinIO account/key（写入 `secrets.<env>.json` 用后缀键 `MINIO_RELEASES_KEY__cg-dev-console` / `MINIO_RELEASES_SECRET__cg-dev-console`，`sync-creds.sh` 推同步）
   - 更新 `secrets-catalog.md` 加两条 per-app 后缀键
4. **应用侧动作**（叶维政侧，本裁决给出接入模板，不代做）：
   - server/src/config 加 MinIO endpoint / accessKey / secretKey 声明（zod fail-fast）
   - server/src/releases 实现 upload path（`<slug>/<environment>/<releaseId>/<appId>/<fileName>`）+ IfNoneMatch 幂等
   - server/src/api/config-agent 实现 `GET /api/config-agent/v1/releases/:releaseId/artifacts/:appId/download` 走 presignedGetObject 15 min TTL
5. **INF-04 显式不做**：给叶维政的回消息里明确"本轮 M3.2 不签名，威胁模型显式后再启动 INF-04 契约"，让他不要等平台方给 KMS / Ed25519 基建。
6. **不 commit**：本裁决落地 monster 侧 3 处文件修改由 Keith / 主代理决定何时 commit，我不越界。

## 父会话回消息模板（给 platform-help 302855 叶维政）

```
INF-03/INF-04 平台方回应：

INF-03 存储侧：本轮平台建独立私有 MinIO 桶 cg-platform-releases（policy=private + versioning + object-lock），
配 secrets map 发放 per-app key（MINIO_RELEASES_*__cg-dev-console 后缀键）。storage_key 结构定为
`<slug>/<environment>/<releaseId>/<appId>/<fileName>`（保留 slug 前缀为跨签发方隔离锚）。应用侧直连 MinIO SDK，
不上 platform-services HTTP 门面（等第二个 Release 签发方应用出现再上提）。写入 cg-platform 契约 §7。

INF-04 签名侧：本轮**不做签名**。当前单方全控链路（cg-dev-console 唯一生成 / 私有 MinIO 唯一存储 / 平台 Agent
唯一消费），INF-03 的 HTTPS + object-lock + presigned URL 短 TTL + Bearer 已覆盖完整性+机密性攻击面；
签名承重的经典场景（多方 registry / 跨组织 provenance / 对外合规）当前不成立。挂 parking-lot 前瞻，
触发条件：① 外部合规审计需求 ② 出现第二个独立签发方 ③ Agent 落在不完全可信环境 ④ 显式威胁模型
出现"防内部人替换 MinIO object"。触发任一升 thread 复议。

不要等平台方给 KMS / Ed25519 基建——本轮 M3.2 不签，Manifest 里 `signature` 字段可留 null 或从
schema 里删。你要继续 003 migration + 应用层 releases 表 + storage adapter；storage adapter 直连
MinIO SDK。003 migration / releases 表 / signing adapter 完成度请 Keith/monster 侧同步 platform-help
回本消息，好让平台方判断 storage adapter 什么时候能开工。
```

---

**置信度 4/5**。扣 1 因：INF-04 拒签依赖"当前威胁模型 = 单方全控"这个 owner 参数——如果 Keith 目标层里有我不知道的"未来 cg-platform 要接外部审计 / 客户 SLA / 合规"意图，本裁决 INF-04 部分需要翻转。**这条应由 Keith 显式 ack "当前无对外审计合规需求"，或反向拨回"其实有 X 合规要求"**。此 ack 一到，置信度 5/5。

### 核心假设

- **cg-dev-console 是 cg-platform 第 22 应用，落象限② AI 生成代码 + 模板治理**——基于 monster CLAUDE.md 索引 `cg-dev-console` 条 + platform 应用清单推断（本次未物理核 registry.json 是否 cg-dev-console 已 onboard，但召唤 prompt 说"叶维政经 platform-help"、platform-help 白名单含 302855 叶维政，且他管 M3.2 = 强推断成立）。
- **cg-dev-console 消费方（Agent）落在平台自管系统账号域内**——基于 API-CONTRACT §5 `/api/config-agent/v1/*` 有 enroll/heartbeat/task 生命周期 + monster CLAUDE.md cg-desk / dev-console 描述"研发工作台 → V3 配置平台"推断（Agent 是平台自管系统，非客户机房 / 第三方托管）。若 Agent 未来落客户机房 → INF-04 tripwire ③ 命中。
- **川锅当前无对外 Release 审计合规要求**——基于 Keith 明示"独立工作者 / 超级个体 / 不见客户 / 拒 SRE 世界"（monster CLAUDE.md User Profile 段）+ 无监管审计 / SLA / 供应链证明需求推断。**这条是最需要 Keith 显式 ack 的**。
- **MinIO 服务端支持 object-lock 或等效替代**——基于 川锅内部广泛使用 MinIO（DEPLOYMENT.md 拓扑推断）+ MinIO 从 2020-04 起 GA object-lock 推断。call platform-help 补验清单第 1 条待核。
- **签名密钥若真要引入，独立 sign-side 容器路径可行**——基于 06-10 骨架"密钥物理不在 web 后端可达域" + docker sidecar 是 cg-platform 已有部署形态（integration-contract §3 network + docker run）推断，未物理核 cg-dev-console 当前是否 monorepo one-container 无法拆两容器。

### 可能出错的地方

- **最高：Keith 目标层里其实有"未来对外合规审计"需求，我没读到**——INF-04 拒签直接翻转。缓解 = 明确要求 Keith ack "当前无外部合规审计需求"这条假设；ack 不到就先按拒签做，触发条件命中时立启动 INF-04 契约。
- **次高：MinIO 服务端版本过老不支持 object-lock**——INF-03 承重的"不可覆盖"降级到 IfNoneMatch + policy DENY DeleteObject + versioning=on 三件套（等效但更 fragile）。缓解 = platform-help 补验清单第 1 条，验完再落地。
- **中：叶维政声称 003_m3_release.sql / releases 表已完成实际未完成**——本裁决落地时序错位（先 storage adapter 后 releases 表 = 无 releaseId 可挂 storage_key）。缓解 = 让 platform-help 补澄清完成度后再定实施顺序。
- **中：存量 7 个 MinIO 桶如果确实全 public-read 且承载真敏感数据 → 独立 P1，需另立 thread**——不影响本裁决但影响 monster 主代理注意力分配。

### 本次哪里思考得不够

- **没物理读 V3 原文**（Keith 传入的召唤 prompt 引 V3 原文只说"必须签名"），我对 V3 原文的"签名承重目的"是"继承自开源默认"这个论断**是基于 V3 提到 KMS/Ed25519/公钥分发/轮换这一整套 SLSA 词汇表推断**（开源生态的 signature ceremony 命名一致性极高），但没直读 V3 原文里"签名要防谁"的显式陈述。若 V3 原文其实显式声明"防运维人员替换 MinIO object"这一威胁模型（我拆解的 tripwire ④），INF-04 拒签立即翻转。
- **没读 cg-dev-console 的 Manifest schema**（API-CONTRACT §4 只见 POST/GET /api/releases 端点、未见 Manifest 字段清单），"signature 字段可留 null 或从 schema 里删"的建议不带体检——如果 Manifest 已经在 M3.1 SecretRef / Schema v2 里跟 signature 硬编字段耦合，删字段有二级影响。
- **没考虑签名的另一个非安全承重目的：审计追踪的完整性锁定**（"这份 Release 5 年后被人质疑改动，签名 + 时间戳能证明未改"）——若 Keith 有长期审计追溯需求，签名承重目的从"防现在被改"扩展到"防未来被质疑"，不受"单方全控"消解。**这个假设点应该在 Keith ack 里覆盖到**。

### 如果 N 个月后证明决策错了，最可能的根因

- **形态 A（最可能）**：Keith 目标层里有"对外汇报 / 客户 SLA / 合规审计"意图我没读到 → INF-04 tripwire ① 命中 → 半年后翻转起 sign-side sidecar。根因 = 决策时没显式向 Keith 追问威胁模型（Decision Authority 目标层三类合法 trigger 之一——"目标范围"），把"当前看起来无合规需求"当默认成立。**缓解 = 本裁决明确 flag 出"待 Keith ack 当前无外部合规审计需求"**。
- **形态 B**：MinIO object-lock 版本不支持 + IfNoneMatch/policy 组合被 MinIO 后续版本悄悄降级/bug → "不可覆盖"承重塌 → Release 被覆盖 → 追不回原始 Release → 声誉损失。根因 = 依赖单一存储实现的物理特性，没做 tripwire "定期 mc admin info 版本核验"。**缓解 = 契约 §7 条文里加"MinIO 版本 tripwire：每 quarter 核 mc admin info"**（这条应该由主代理落到 auto-monster tripwire 里）。
- **形态 C（低概率但严重）**：起 sign-side 容器时"图省事"把签名私钥直接挂进 cg-dev-console web 后端容器（`fallback-detectability` 05-06 的孪生失败） → 承重内核塌陷 → 攻破 web 后端 = 拿到签名私钥。根因 = tripwire 触发启动 INF-04 契约时，实施方（future gg / future 主代理 / 叶维政）没守住"密钥物理不在 web 后端可达域"这条硬约束。**缓解 = parking-lot 条文里明写"落 sign-side sidecar，签名私钥挂 sign-side 容器不挂 Web 后端"这条骨架**，防未来同轴退化。

### 北极星触达

**#3 决策超越直觉**。直觉解 = 顺着 Keith 初判在 B 段"应用容器持密钥 / 平台 sign 微服务 / GitLab tag signing"三选一里挑一个（自证 gg 有独立判断——但仍在 Keith 帧内选）。超越直觉处 = 识破 INF-04 是**上一层问题**——不是"怎么签"，是"要不要签、签什么、防谁"。V3 原文继承开源 SLSA/cosign 默认清单（这一继承在开源生态里是无审视传播的、essence `stale-observer` + `theory-gap-without-data` 双击命中），川锅**单方全控**链路里签名的承重目的未落地，`security-invariant-encodes-an-owner-set-threat-model` 提醒威胁模型是 owner 参数——**应主动 flag 给 Keith 拍威胁模型，而不是替他假设一个然后选方案**。这符合"决策符合 Keith sense 甚至更完善"判据——Keith 初判在 gg 视线里是"三个方案的两条 essence 已经 tag 好了"（他自己 tag 了 invariance-allocation / tool-elevation-as-occam / physical-anchor），但**上一层帧"要不要做"没被开题**。gg 的价值 = 换帧不是选。

### essence 对齐自检（必填）

- **本决策跟哪几滴 essence 对位**（grep 物理命中）：
  - `theory-gap-without-data`（2026-05-06）—— 承重根：V3 签名要求继承 SLSA 生态默认，没有川锅侧数据支撑必要性。essence 直接说"没数据时找理论缺口=生造"。
  - `security-invariant-encodes-an-owner-set-threat-model`（2026-06-17）—— 直接落点：INF-04 拒签的判据是"威胁模型未显式 = owner 参数未提供"，把安全律降格为 owner 参数交回 Keith。
  - `separation-need-is-not-topology-verdict`（2026-06-10）—— A 段拒 platform-services SDK 门面的根据：先试最轻治理形态，第二个签发方还没出现，造门面 = 造未来的墙 + 喂下一次。
  - `tool-elevation-as-occam`（2026-05-06）**带 06-22 边界注**——第二个消费者判据要现场核，本轮 N=1 不上提；不是"预感未来 N=2"就上提。
  - `invariance-allocation`（2026-04-19）—— storage_key 保留 slug 前缀而非 Keith 初判的去除：选真正稳定的不变量（跨签发方隔离），不选当前 N=1 的临时事实（"只有一个签发方"）。
  - `ownership-by-facet`（2026-05-06）—— 契约立位 A/B 分治的根据：存储面跨签发方共享（契约化），签名面单签发方（应用内业务，不契约化）。
  - `paradigm-not-feature-completeness`（2026-05-14）—— 双击命中：拒 COS（范式匹配足，无需引入新云依赖）+ 拒 GitLab signed tag（签的对象不进 git，载体错位）+ 拒 GitLab Release Artifacts（Agent 拉配置不是拉构建产物，语义错配）。
  - `no-fatigue-narrative-for-ai`（2026-04-27）—— 拒"总要做一点"的直觉：M3.2 首刀显式**不签**是最难的决策（比选一个方案难，因为"什么都不做"看起来像失职），不给 owner 出局叙事。
  - `physical-anchor`（2026-04-16）—— 存储侧承重的具体承担者是 MinIO 服务端物理能力（object-lock），不是文档约定；文末补验清单第 1 条落到 mc admin info 物理核。
  - `execute-untrusted-code-never-holds-prod-trust`（2026-05-18）+ 未 append 的 `web-facing-executor-is-untrusted-regardless-of-payload-trust`（06-10 挂账候选）—— 反驳叶维政方案（应用容器持 Ed25519）的骨架：即使拒签的裁决站住，未来 INF-04 tripwire 触发时也不能把签名私钥落 web 后端容器；parking-lot 条文里明写 sidecar 骨架防未来同轴退化。
  - `ghost-rules`（2026-04-15）—— 反 face-value 论证：不给已塌陷的 web 后端补签名 = 不为已被绕过的攻击面加防御。
  - `stale-observer`（2026-04-15）—— C 段反驳 Keith 初判合并 INF-03/INF-04 进契约 8/9 的根据：签名进契约会变成"平台承诺提供签名基建"的历史档案，未来读的人误导。

- **本决策是否在某条 essence 上反着走**：
  - 潜在张力 `caged-freedom`（2026-04-26）：给 storage_key 结构定死 5 层（`<slug>/<environment>/<releaseId>/<appId>/<fileName>`）+ 拒 SDK 门面 = 给 cg-dev-console 应用侧加约束。**判定不构成反走**：这是承重墙（跨签发方隔离锚 + 首个案例=契约的 fleet-canon 效应），收紧的是"应用不该自由发挥 storage_key layout"这条本就该收紧的边界，应用真实自由（业务逻辑 / Release Compiler 内部结构 / 签发触发流程）零损。`ghost-rules` 警戒也已主动跑——storage_key 结构是首个案例=契约后所有 Release 应用要遵守的、真实物理需求（否则跨签发方 policy 授权无从下手），非臆想。
  - 另一条潜在张力 `no-clean-outside`（2026-05-22 以 06-02 修正态）：我用 `theory-gap-without-data` 拒 INF-04 时判据是"川锅链路无签名承重目的"，但 essence 提醒 prior 共盲不恒满 + 可下压。本轮**主动跑了"是不是我自己 prior 里没考虑到的威胁模型"** ——枚举出的 4 条 tripwire（外部合规 / 第二签发方 / Agent 落客户机房 / 显式威胁模型）就是补集采样，把 prior 下压到"这 4 条都不成立时才拒签"，不是无条件拒。属于用 `falsification-as-structure-not-just-skepticism`（06-29）的结构性证伪，不是软怀疑。

- **cross-check 用的关键词**（grep 物理证据）：`theory-gap-without-data / security-invariant-encodes-an-owner-set-threat-model / separation-need-is-not-topology-verdict / tool-elevation-as-occam / invariance-allocation / ownership-by-facet / paradigm-not-feature-completeness / no-fatigue-narrative-for-ai / physical-anchor / execute-untrusted-code-never-holds-prod-trust / ghost-rules / stale-observer / caged-freedom / no-clean-outside / falsification-as-structure-not-just-skepticism`（均在 essence-view.md 视图或全卷 grep 命中；`web-facing-executor-is-untrusted-regardless-of-payload-trust` 为 06-10 挂账候选未 append，仍作论证锚点引用）

### essence 候选（可选）

- slug: **inherited-security-checklist-drifts-under-context-change**
- 一句话: 从开源生态继承而来的安全清单（KMS / 签名 / 密钥轮换 / SLSA 三件套）**它的承重目的绑在其原生场景**（多方共享 registry / 跨组织 provenance），当继承者的场景不同（单方全控 / 单组织闭环），清单条目会**保留形式失去实质**——不审视地按清单实现 = `theory-gap-without-data` 在治理层的落点；判据 = 每继承一条前，问"这条防的攻击面在我这条链路上还是同一个吗"，答不出就是理论生造缺口不是设计缺口。
- 是否已 append 到 essence.md: **N（本轮不 append，初标 candidate-unverified；2026-07-22 auto_gg 补审 → `candidate-refuted`，见文末「auto_gg 补审记录」）**——subagent 工具集无 Agent，无法开 fresh-context 证伪审。按 KERNEL §3 第 5 步 subagent 分支协议：候选滴留在本 reflection，等 auto_gg 夜巡或设计会话补审入库。原因：这一滴承重结构完整（在治理层扩展 `theory-gap-without-data` 到"继承外部清单"场景），但需要 fresh 证伪：① 与已有 `borrowed-method-as-mini-source`（05-08）不同吗（那滴说"批量抽取外部体系 = 造它的迷你版"，本滴说"抽取每条条目在新场景下重估承重目的"，是不同颗粒度，但可能被认作同一滴）？② 与 `stale-observer`（04-15）不同吗（那滴说"规则演化速度 < 对象演化速度时退化为历史档案"，本滴的失效机制是"从别处继承时目的已经失效"，不是规则老化，是继承时点就失效）？—— fresh 证伪审若判"是 `borrowed-method-as-mini-source` 在治理层的重述、无新重量" → 归档；若判"是承重的独立扩展、`theory-gap-without-data` 在治理层的具体落点" → append。

**物理证据清单**（供 auto_gg 补审用）：
- 本裁决 INF-04 拒签的**唯一根据**就是这一滴的原理：川锅链路场景与 SLSA 原生场景不同 → V3 原文签名清单条目保留形式（KMS/Ed25519/轮换）失去实质
- 现场应用产生了具体决策（拒签 + parking-lot tripwire），不是空谈
- 相关既有滴：`borrowed-method-as-mini-source`（05-08）/ `theory-gap-without-data`（05-06）/ `stale-observer`（04-15）/ `no-clean-outside`（05-22）—— 待 fresh 判是否已被这四滴组合覆盖

### 外部锚点

- `~/CGProject/cg-dev-console/docs/INFRASTRUCTURE-GAPS.md` INF-03/INF-04 条目 ← 缺口 SSOT，本裁决闭合 INF-03 落契约 / INF-04 挂 parking-lot
- `~/CGProject/cg-dev-console/docs/prd/release-management.md` ← M3.2 期望 SSOT，本裁决明确 Manifest signature 字段可留 null 或删
- `~/CGProject/cg-dev-console/docs/API-CONTRACT.md` §4 releases / §5 config-agent artifacts ← 应用侧接入契约 §7 的入口
- `~/githubProject/monster/cg-platform/integration-contract.md` ← 本裁决落 §7 新增（第 7 条平台契约「Release Artifact 私有存储」）
- `~/githubProject/monster/cg-platform/docs/parking-lot.md` ← INF-04 挂 parking-lot 条目
- `~/githubProject/monster/cg-platform/CLAUDE.md` ← 高频动作速查加行
- `~/githubProject/gg/memory/reflections/2026-06-10_cg-dev-console-deploy-auth-boundary.md` ← 近亲议题（cg-dev-console 部署认证 06-10 裁决）；本轮延续其"象限区分 + web-facing-executor 挂账候选"骨架
- `~/githubProject/gg/memory/reflections/2026-05-18_cgplatform-deploy-trust-model.md` ← C′ 骨架前身；本轮的"存储契约立场"（第 7 条）跟 C′ 的"部署契约立场"（契约 3 收紧）同轴
- `~/githubProject/gg/memory/reflections/2026-06-25_cgplatform-secrets-shared-vs-perapp-split.md` ← per-app 后缀键机制（`MINIO_RELEASES_KEY__cg-dev-console`）本轮沿用

---

## auto_gg 补审记录（2026-07-22 夜巡）

候选滴 `inherited-security-checklist-drifts-under-context-change` 过 fresh-context 证伪审（sonnet fresh evaluator，只读纪律：Read + Bash grep，事后核 tool_use=17 全只读、essence.md `^## 20` 计数入审前后均 179 未变、git status 零写副作用）。

**VERDICT: REFUTED → 不入库，标 `candidate-refuted`**。

**理由（evaluator 最强反驳点，留档防 `verification-trace-as-camouflage`）**：
1. **既有滴已覆盖**：候选 = `security-invariant-encodes-an-owner-set-threat-model`(06-17) × `engineering-impulse-as-load-bearing-disguise`(05-28) 在"打包继承清单"场景的重述，加一层"多条目逐条应用同一测试"操作提示 = **应用注记（corollary），非独立机制**。候选自比的四滴里漏掉了 05-28——evaluator 独立 grep 补出，其"业界共识≠本地需要，越多 source 一致背书越可能在抽业界范式造迷你版"几乎逐字覆盖候选想说的。候选自比 `theory-gap-without-data` 是"治理层落点"，但那个落点已由 06-17+05-28 组合占据。
2. **时序反证（Self-Confirmation Trap 典型样本）**：本 reflection 的 essence 对齐自检节自证——INF-04 拒签在候选被提出**之前**就已由 12 条既有 essence（尤其 06-17/05-28/06-10/05-06）完整推出。候选是决策做完后回头贴的标签，不是决策当时缺失、必须补上才能推出结论的那一环。这正是入库验证关设计要拦的"生成者把已有材料的组合错认成新洞察"。
3. **区分部分成立但不救场**：候选 vs `stale-observer`(04-15) 的"语境错配≠规则老化"区分成立，vs `borrowed-method-as-mini-source`(05-08) 的颗粒度区分部分成立——但"不是 A 的重复"不等于"不是 B(06-17) 的重复"，而 B 才是真冲突点。

**首次审**（essence.md 全文 + next_session_agenda.md 均无此 slug 既往 `candidate-refuted`/`candidate-unverified` 记录）。复提须附本记录 + 新增物理证据（入库验证关协议第 3 步复提规则）。
