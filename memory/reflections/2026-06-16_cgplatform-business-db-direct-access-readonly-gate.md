---
date: 2026-06-16
slug: cgplatform-business-db-direct-access-readonly-gate
summoner: monster
northstar_reach: "#3 决策超越直觉（在 Keith 的目标层「放开直连」与我自己 2026-06-02 立的真不变量正面冲突处，给出比「服从字面」和「辩护旧裁决」都更完善的精确化解）"
status: substantive-decision
---

# Reflection: cg-platform 应用直连业务库的安全放开形态（受限只读 + 表级白名单 + GRANT 反向闸门）

## §A 范式 A — 决策的元属性反思

### 给父会话的最终输出（必填）

**裁决：把「应用直连业务库」严格收窄为「库级/表级只读 SELECT + 敏感表显式排除（默认表级白名单）+ 经现成 datasource 机制下发 + datasource 注入路径补一道 GRANT 反向验证闸门」。绝不下发可写账号、绝不下发未经 GRANT 收窄的账号、绝不复用 root/库级全表账号。**

我正面拒绝「让应用拿 cgManager/wflow 库凭据」的字面最宽解——撤掉它会塌掉 2026-06-02 真不变量 `execute-untrusted-code-never-holds-prod-trust` 的内核（AI 生成代码 + 持可写库凭据 = 可 DELETE/UPDATE，爆炸半径整库 465 表）。但我把不变量**精确化而非辩护**：旧不变量真正拦的是「可写 + 碰敏感表」，不是「一个 DB 连接都不许持」。Keith 的目标层决定落在「只读直连」这个被旧契约一并误禁的中间档——合法且可安全兑现，我兑现它。

**五问逐条裁：**

**① 权限粒度（不可逆关键参数）**：只读 SELECT，无任何写/DDL（写仍走 owning-service BFF，2026-06-02 范式不变）。每应用**独立账号**（`<ident>_ro_ds`）不复用现成 `pm` 账号。**敏感表必须从白名单挖掉**——`users`/薪酬财务表/`form_data_*`(CRM 名录)：只读不等于零风险，prompt injection 能诱导 `SELECT * FROM cgManager.users` 并外泄，「只读」只把风险从「改坏数据」降到「看光数据」。默认形态 = 表级白名单（GRANT 到具体表，新表默认不可见 = `safe-default-by-whitelist-inversion`），不是库级 SELECT。**这条与现成 `pm` 账号的「库级只读含 users」冲突 → 不能直接拿 pm 账号当 datasource 下发**。

**② 替代隔离（契约 1 闸门失效拿什么补）**：契约 1 的 1142/1143 反向验证对 datasource 账号**根本不生效**——datasource 走 deploy.sh L219-236 那条**无任何 GRANT 闸门**的裸注入路径（data-asset-console 的 cgdata 直连**当前正在裸奔**）。补位 = 给 datasource 注入路径补一道对偶闸门 `_verify_datasource_ro`（同构 `_verify_isolation`）：部署期实测 ① SELECT 白名单表通过 ② 写必被拒 1142（只读确认）③ SELECT 敏感表必被拒 1142（表级排除确认）。任一不符 = 中止部署。**这是放开的硬前提不是可选加固**——没它 = 把 465 表只读权交给没人验证过边界的账号 = 回到 1142/1143 之前的裸奔。

**③ 载体**：走现成 datasource 机制扩展（datasources.json 补条目 + registry 声明 `datasource`）——deploy.sh 已实现、已验证、OCCAM 不另造，对。**但 cgManager ≠ cgdata 同构**：cgdata 是 FMO 派生库（敏感面较低，data-asset-console 已用库级只读可接受）；cgManager 是核心主业务库（users/form_data_*/notes 全在，**必须表级白名单，不允许库级 SELECT**）。datasources.json 条目设计为 per-(应用×业务库) 受限账号，不是万能账号。

**④ 契约源怎么改**（不执行，仅指令）：`integration-contract.md §2 L74`「不允许应用拿任何账号直连业务库」是真不变量的过宽表述（同 2026-06-02 §3 的病）。改法 = 精确化 + 分档，措辞走 `security-claim-as-physical-fact-not-injectable-grant`（陈述物理约束不写「授予例外」）：
> 应用进程**不得持有任何业务库可写凭据 / 未经表级白名单收窄的凭据**。业务数据读写三档：① 写 + 有 owning-service → BFF 透传已鉴权 API（2026-06-02 范式）② 只读 + 经表级白名单受限账号 → datasource 机制直连（GRANT 限只读 + 排敏感表 + 部署期 GRANT 反向闸门物理核验）③ 写 + 无 owning-service → 停，上 gg。dev_ro 物种边界不变。

配套指针（父会话转方案落）：§2 dev_ro 段同步（dev_ro 与 datasource-ro 两并存物种）/ `cg_platform_create_app_db.py` 加建账+GRANT+新闸门 `_verify_datasource_ro`（承重代码，写完派 codex-rescue）/ `database/CLAUDE.md cgPlatform 段`凭据分层表加第 5 类 / `capability-map.md L127` 挂账翻状态 / `PLATFORM-SERVICES.md §33`（fork 辐射，建议 Keith 过目）。

**⑤ dev_ro 去留 + 下发清单**：dev_ro **保留**（人在 CC 查业务库写 PRD ≠ 容器 runtime 直连，两条路）。物种从二分变三分：dev_ro(人/不进容器) / datasource-ro(应用容器只读直连/新增) / `_app`(应用容器读写自己表)。

要 Keith 下发的不可逆动作（全需 ack）：
| 动作 | 落点 | 状态 |
|---|---|---|
| 建 per-应用表级白名单只读账号 + GRANT 具体表 | prod 实例（root 操作）扩 create_app_db.py 后脚本建 | 待 Keith 定每应用读哪些表 |
| datasources.json 补条目 | prod 宿主 `42.193.55.173:$APP_BASE/datasources.json` + test 宿主 `10.13.1.61` 对应文件，chmod 600 | 待账号建好 |
| registry 加 `datasource` 字段 | `cg-platform/registry.json` | 待对齐 |

**绝不放可写/库级全表/root 账号进 datasources.json。** 复核 data-asset-console 的 cgdata 条目当前用的什么账号——若是 wflow/pm 库级账号，本身是待收窄隐患。

**风险姿态（Keith 必须知情接受）**：爆炸半径从「零」变「一个 AI 应用/一次 injection 能 SELECT 白名单内业务表并外泄」。三道闸门夹住：只读(改不了) + 表级白名单(碰不到 users/财务/CRM) + GRANT 反向闸门(部署期核验前两条真生效)。知情项：① 只读拖库仍可能（白名单内表，唯一控制 = 白名单尽量窄）② **GRANT 闸门没写就放开 = 裸奔，cgdata 已在裸奔，放 cgManager 前必须先补闸门并回头给 cgdata 套上** ③ 白名单维护是持续债，GRANT 修改权必须物理留 Keith 侧 root、不进 AI 可控代码路径（`deploy-decision-must-not-read-untrusted-controllable-inputs` 同构）。

**整体判断**：可安全兑现，但前置依赖一道当前不存在的 GRANT 反向闸门。没它我不建议放开任何业务库直连（含已跑的 cgdata）。本质不是「放不放开」（Keith 已定），是「把契约 1 让渡给 GRANT 的那套物理核验机制对 datasource 路径也补齐」——契约 1 精神（隔离靠 GRANT + GRANT 必被物理验证）原样平移，一行不放松。

### 核心假设
- deploy.sh L219-236 datasource 注入路径确实无 GRANT 反向闸门（已物理读源码确认：原样从 datasources.json 注入 5 字段，无 verify 调用）。
- data-asset-console 的 cgdata 直连当前就走这条裸路径（registry `datasource:"cgdata"` + deploy.sh 实现，已读两处互证）。
- MySQL 5.7 表级 GRANT 可行（create_app_db.py 已实证逐表 GRANT，表级白名单技术可行）。
- 现成 `pm` 账号是库级全表只读含 users（database/CLAUDE.md L48-66 表实证 cgManager「只读(查)」无表级排除）。

### 可能出错的地方
- datasources.json 当前 cgdata 条目用的账号若已是表级受限（而非 wflow/pm 库级），则「cgdata 已裸奔」表述对权限粒度过严——但「无 GRANT 反向闸门」这条仍成立（裸奔指的是注入路径无物理核验，不是账号一定配错）。概率中，不改变裁决方向只改措辞强度。
- 「敏感表」边界（哪些算敏感）是业务判断，我列的 users/财务/CRM 是高置信子集，完整清单需 Keith/PM 按应用定。我给的是默认排除原则不是穷举清单。

### 本次哪里思考得不够
- 没核 datasources.json 实际内容（该文件在宿主、不在 monster 仓，我物理够不到）——「cgdata 条目用什么账号」是推断（基于 data-asset-console 是只读消费 + database 有 pm/wflow 库级账号），未亲验。已在行动清单标「复核」。
- `_verify_datasource_ro` 闸门的「敏感表拒 1143/1142」具体错误码我按表级 REVOKE 推 1142（跨表无权），但若用「GRANT 白名单表」而非「REVOKE 敏感表」实现，敏感表是「未 GRANT」也是 1142——两种实现都落 1142，结论稳，但实现细节留给落地脚本。

### 如果 N 个月后证明决策错了，最可能的根因
「GRANT 闸门补了，但白名单配太宽」——表级白名单退化成「图省事 GRANT 整库」，敏感表混进去，闸门测的敏感表清单又没跟上，于是闸门绿着放行了一个能读 users 的应用。根治靠：① 闸门的敏感表黑名单是平台级常量（不是 per-应用可调，AI 改不动）② 白名单 GRANT 必须 Keith 逐表 ack（不让 onboard 脚本自动 GRANT 业务库表）。bug-shape-survives-fix：我这次把「闸门」立为硬前提，但闸门自己的「敏感表清单完整性」无人验证 = 下一层裸奔点，已在风险姿态点出但未给机制。

### 北极星触达
#3 决策超越直觉——Keith 的目标层「两者都放开」字面读是「应用拿业务库凭据直连」，直觉服从会撤掉真不变量酿灾；但辩护旧裁决（「不变量不可动」）又违背 Keith 已定的目标层。第三条路 = 把不变量从「禁一切直连」精确到「禁可写/禁未收窄」，让 Keith 要的「只读直连」合法落地同时保住灾难防线。这是「比 Keith 当场 sense 更完善」的操作判据：他要放开，我给的是「安全放开的唯一形态 + 一道他没意识到当前已缺的闸门」。

### essence 对齐自检（必填）
- **本决策跟哪几滴 essence 对位**：`owning-service-not-proxy-for-write`(2026-06-10，隔离不变量锚「进程是否持库凭据」不锚「数据是不是业务数据」——本次把「凭据」再细分「可写凭据/未收窄凭据」) / `execute-untrusted-code-never-holds-prod-trust`(2026-05-18，AI 代码不持生产可写信任——本次确认只读放开不破此条) / `network-cannot-cut-what-shares-tuple`(2026-05-19，隔离全压 GRANT 时 GRANT 必被物理验证——补 datasource 闸门的直接依据) / `safe-default-by-whitelist-inversion`(2026-05-19，存准入白名单非禁入黑名单——表级白名单默认新表不可见) / `precondition-recheck-overturns-prior-verdict`(2026-05-19，旧裁决前提被推翻时主动覆盖自己不辩护——本次正面反转自己 2026-06-02 真不变量) / `deploy-decision-must-not-read-untrusted-controllable-inputs`(2026-05-19，GRANT 修改权物理留 Keith 侧不进 AI 代码路径) / `security-claim-as-physical-fact-not-injectable-grant`(2026-05-19，契约措辞陈述物理约束不写授予例外)。
- **本决策是否在某条 essence 上反着走**：表面在 `execute-untrusted-code-never-holds-prod-trust` 上反着走（那滴说「绝不能同时持生产信任凭据」，本次放开持业务库凭据）——但实为**精确化非违背**：那滴的承重是「生产**信任**凭据」=可写=可破坏，只读 SELECT 不构成「生产信任」（改不了状态、不可逆动作半径为零，只剩可逆的「被读」）。`vantage-contaminates-verdict` 提醒我审自己 2026-06-02 裁决会偏向辩护「一个连接都不许」——我顶住了，承认旧措辞过宽，但顶的方式不是全撤而是分档，分档的合法性靠「可写 vs 只读」是物理可验证的硬边界（GRANT 闸门测得出），不是修辞。潜在张力已展开。
- **cross-check 用的关键词**：grep essence.md「owning-service」「untrusted」「network-cannot」「whitelist-inversion」「precondition-recheck」「deploy-decision」「security-claim」「vantage」。

### essence 候选（可选）
- slug: readonly-direct-access-splits-the-write-invariant
- 一句话: 「应用不持业务库凭据」式隔离不变量被目标层要求放开时，可解形态不是全撤也不是辩护，是沿「可写/只读」这条物理可验证的硬边界分档——只读直连是被旧不变量误禁的合法中间档，因为它的爆炸半径塌到「可逆的被读」、不含「不可逆的被写」；放开它的硬前提是给新凭据通路补一道与旧通路（契约 1 的 1142/1143）对偶的 GRANT 反向闸门，否则「隔离让渡给 GRANT」在新通路上退化为「隔离让渡给对配置的信任」。是 `owning-service-not-proxy-for-write` 的下一层（前者把不变量从「数据来源」移到「凭据持有」，本滴把「凭据持有」再沿「可写/只读」劈开）+ `network-cannot-cut-what-shares-tuple` 在「新增凭据通路」维度的复用（GRANT 必被物理验证，每条注入通路各补各的闸门）。
- 是否已 append 到 essence.md: N（留 Keith review 后定，避免未 commit 噪音）

### 外部锚点（可选）
- `~/githubProject/monster/cg-platform/integration-contract.md §2 L74` ← 待改措辞的真不变量表述
- `~/githubProject/monster/cg-platform/cg-platform-deploy.sh L219-236` ← datasource 裸注入路径（无 GRANT 闸门，承重证据）
- `~/githubProject/monster/shared/scripts/cg_platform_create_app_db.py _verify_isolation/_verify_dev_ro` ← 待对偶补 `_verify_datasource_ro` 的闸门范式
- `~/githubProject/monster/cg-platform/docs/capability-map.md L127` ← 挂账原文（待翻状态）
- `~/githubProject/monster/database/CLAUDE.md L48-66 pm 账号 + L76-91 凭据分层` ← 现成只读账号 + 待加第 5 类
- `~/githubProject/gg/memory/reflections/2026-06-02_cgnotes-bff-cgapi-vs-proxy-topology.md` ← 被本次精确化的前序真不变量裁决
