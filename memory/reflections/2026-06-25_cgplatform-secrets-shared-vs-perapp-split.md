---
date: 2026-06-25
slug: cgplatform-secrets-shared-vs-perapp-split
summoner: monster (cg-platform)
northstar_reach: "#1 二阶效应（A/B 载体耦合是结构因，flat map 单字段装不下 N 值是症状）"
status: substantive-decision
---

# Reflection: cg-platform secrets 存储数据模型 — 共享凭据 vs per-app 密钥分治

## §A 范式 A — 决策的元属性反思

### 给父会话的最终输出（必填）

> **2026-06-25 收窄修订**：Keith 在我初裁后补入 I-secret 黑名单分类（已物理核实：9 真 secret 命中黑名单 / 14 非密元数据未命中且全非空）。据此**收回初裁的过度工程部分**——不把整个 secrets.json 升 slug 嵌套、不分两文件。今早 config/secret 分治已先于本议题改变了前提：map 本就只该留真 secret，14 个 HOST/PORT/USER/NAME 是分治前残渣、归 git config.env。下为修订后的右尺寸裁决。

**裁决（右尺寸）：flat 共享 map 对 8/9 真 secret 是对的、保留不动；只给 WECHAT_SECRET 这一个多值冲突字段加 per-app 命名空间，且用 flat map 内的 slug 后缀键（`WECHAT_SECRET__<slug>`）实现，不升整文件嵌套、不建第二个文件。14 个非密元数据残渣随各应用下次加字段自然迁回 git config.env（被动），不主动批量清。命名目录 `secrets-catalog.md` 仍要做（治 WFLOW_PASSWORD 漂移 + A/B 归类）。**

理由链：① 23 字段里真正需要 per-app 命名空间的实测只有 WECHAT_SECRET 一个（Keith 黑名单分类 + 我物理核实双重确认）——为一个字段把整个 map 推倒升嵌套/分文件是过度工程，违反 OCCAM（我初裁 essence 自检里自己警惕过这条张力，但当时把 22 字段误粗归"A 类共享"、没看出 14 个是非密残渣，导致判断面虚大）。② 8/9 真 secret 是全平台单值（4 业务库共享密码 + MQTT_PASS/GITLAB_PAT/IOS_TOKEN/BRIDGE_TOKEN 各单值少消费者），flat 共享 map 装得下、无冲突，**不动**。③ WECHAT_SECRET 的 per-app 隔离用**flat 内 slug 后缀键**（`WECHAT_SECRET__cg-inspector-map`）而非整文件嵌套——deploy 注入时按"先查 `<FIELD>__<slug>`、命中则用、否则 fallback 裸 `<FIELD>`"两级查找，零文件结构变更、零新范式、跟现有 flat 解析器最小增量兼容。未来若 `*_API_KEY` 多值冲突高频复发再升嵌套（tripwire：第 ≥3 个出现 per-app 冲突的字段时升级数据模型）——现在上嵌套是 premature-abstraction。

逐问裁决（修订后）：**

**问 1 — 数据模型：flat map 保留 + WECHAT_SECRET 单字段 slug 后缀键（不升整文件嵌套、不分文件）。**

- **否决 (a) 现状延续（B 类走 env-file 兜底）**：env-file 今早已被拍为 legacy；把 B 类 secret 往 legacy 载体塞 = 逆今早方向，且 sync-creds.sh 不同步 env-file（手动 scp），把 B 类密钥踢出"录一次自动同步"飞轮。**(a) 是症状治疗。**
- **否决 (c) 物理分文件 + (b) 整文件升嵌套（我的初裁，收回）**：实测只有 1 个字段需要 per-app 命名空间，为它分两文件 / 升整文件嵌套是 premature-abstraction——8/9 真 secret 是 flat 单值、装得下、零冲突。整文件嵌套要改 deploy 解析器（裸 flat → 嵌套分支）+ 闸门左集 + sync-creds + 模板，改动面跟收益（隔离一个字段）严重不成比例。
- **选：flat 共享 map 不动 + WECHAT_SECRET 用 slug 后缀键**：在现有 flat `secrets.<env>.json` 里，把撞车的两个值存为 `WECHAT_SECRET__cg-cost-management` / `WECHAT_SECRET__cg-inspector-map`（双下划线分隔 FIELD 与 slug，slug 含连字符不与 FIELD 命名冲突）。deploy 注入 WECHAT_SECRET 时**两级查找**：先查 `WECHAT_SECRET__<当前slug>`，命中用之；否则 fallback 裸 `WECHAT_SECRET`。这给所有字段一个统一的"per-app override > 共享默认"机制，**零文件结构变更、零新解析范式**，只在现有 flat 解析后加一个后缀匹配。**升级触发器（tripwire）**：当出现第 ≥3 个需要 per-app 命名空间的字段（如多个应用各自 `*_API_KEY`）时，再把 flat 后缀键升级为 datasources.json 同构的 slug 嵌套——那时数据点足够、不是猜。现在上嵌套违反 `premature-abstraction-tripwire`。

**问 1b — 14 个非密元数据残渣：随渐迁被动清，不主动批量动。**

- Keith 已核实它们是分治前残渣（HOST/PORT/USER/NAME，分治后归 git config.env）。但**它们留在 map 里当前不造成错误**——deploy 注入逻辑对它们和对 secret 等价（都是"声明且未提供则注入"），cg-inspector-map 已是新范式样板（这些字段在它 git config.test.env、只密码进 map）。
- **被动清（推荐）**：对偶今早 config/secret 分治的"渐迁不一刀切"裁决——主动批量清 14 字段 × N 应用 = 多次重验堆风险，收益只在"该应用下次加字段"时兑现。随各应用自然迁、迁某应用时顺手把它的非密元数据从 map 删掉（迁移动作的一部分，同今早 reflection 选择 4）。**唯一例外**：若某非密元数据字段值过时/错误正在误导注入，那是 bug 要立即修、不算"主动清残渣"。

**问 2 — 改动面（按文件，右尺寸后大幅收窄）：**

- **deploy.sh map 注入段（L303-332）**：唯一实质改动——在现有 flat 查找前加一层 slug 后缀优先查找。伪逻辑：对每个 declared 字段 `k`，`val = secrets.get(f"{k}__{slug}") or secrets.get(k)`，命中且未被 env-file/config 提供则注入。约 2-3 行增量，不改文件结构、不改解析器形态。改完 `sync-deploy-tooling.sh both`。
- **字段闸门**：左集判定加一项——`WECHAT_SECRET` 是否提供，要认 `WECHAT_SECRET__<slug>` 命中。小改。
- **sync-creds.sh**：**不动**（仍同步 datasources + secrets 两份，没加文件）。这是 flat 后缀键相对分文件方案的关键省事处。
- **「录一次复用」语义精确化**：flat 共享区语义不变（A 类单值字段录一次全复用）；新增一条 per-app override 语义——「某字段某应用要独立值时，录 `<FIELD>__<slug>`，覆盖共享默认」。文档显式写明，别让"录一次复用"继续暗示 WECHAT_SECRET 也能共享（那正是撞车认知根因）。

**问 3 — 字段名目录：必须做，committed 零值进 git。**

- 这次顺带暴露的命名漂移（map 里 `WFLOW_PASSWORD`，.env.example 跨库范式约定 `WFLOW_DB_PASSWORD`，同一个 wflow 密码两个名字、应用按约定起名反而不命中 map）**是没有"字段名→类型→数据源"对账锚点的直接后果**。这正是 monster 元方法论准入三问②「谁检验命名一致持续成立」——答案必须是一份机械可查的目录，不是 PM 凭记忆。
- 形态：`cg-platform/secrets-catalog.md`（或 `.json`，**进 git、零值**），每行 `KEY | 含义 | 类型A共享/B-per-app | 对应数据源/服务 | 标准字段名`。PM/应用起名前查它对账。**关键约束**：它是命名 SSOT，map 实际键名必须跟目录一致——可加一个轻量 tripwire（map 出现目录里没有的新字段名时告警，堵"录值时随手起了个新名"漂移）。这条目录同时根治：① A/B 分类（PM 知道某字段该录哪份文件）② 命名漂移（WFLOW_PASSWORD 一类）③ "新凭据 vs 已有同名"判断（目录里有 = 已有、复用；没有 = 真新增、按类型录对文件）。

**问 4 — 迁移路径 + 爆炸半径（右尺寸后极小）：**

- **冲突隔离迁移（唯一必做的本议题动作）= 把 WECHAT_SECRET 撞车的两个值改成 slug 后缀键**：
  1. `secrets.<env>.json` 里：`WECHAT_SECRET` 一行（当前是 cg-cost-management 的值 `heRCEo...`）→ 改为两行 `WECHAT_SECRET__cg-cost-management: heRCEo...` + `WECHAT_SECRET__cg-inspector-map: _yr9ln...`。**删掉裸 `WECHAT_SECRET`**（无共享默认，企微 secret 本就该 per-app；保留裸键会让没登记后缀的新应用静默拿到别人的 secret——这正是撞车根因，必须删）。
  2. cg-inspector-map 兜底 env-file（`cg-inspector-map.test.env`）里的 WECHAT_SECRET 删掉（值已进 map 后缀键）；WFLOW_DB_PASSWORD 那行：密码归 map（真 secret），HOST/PORT/USER/NAME 归该应用 git config.env（新范式，cg-inspector-map 本就是样板）。
  3. 改 deploy.sh 两级查找 + 闸门（问 2），`sync-deploy-tooling.sh both` + `sync-creds.sh both`。
- **14 非密残渣**：本次不动（问 1b 被动清）。
- **命名目录**：建 secrets-catalog.md 登记 9 真 secret + 标准名对账（WFLOW_PASSWORD 定标准名）+ 标哪些字段支持 per-app 后缀。
- **爆炸半径**：仅 cg-cost-management + cg-inspector-map 两应用受影响，迁完是**修复**（cg-cost-management 之前"恰好 map 裸键是它的值"是脆运气，改后是确定性命中各自后缀键）。其他在跑应用零影响。改动集中 deploy.sh 2-3 行 + map 文件改值 + 1 份目录文件，无 schema 破坏性变更、无新文件、无解析器范式变更——**风险等级低**。

**行动建议（父会话执行，按序；改 deploy.sh(契约3锚点)+契约§2 措辞+新增目录传感器，全局 Workflow #1，与今早 config/secret 分治合并成一份方案给 Keith 异步过；secrets-catalog 形态 .md vs .json 是偏好待决）：**
1. 改 `integration-contract.md §2`「应用自声明账密走 secrets.json flat 凭据 map」段：明确 map **只留真 secret**（呼应今早 I-secret），新增 per-app override 语义（`<FIELD>__<slug>` 后缀键，覆盖共享默认）；14 非密元数据标"分治前残渣、随应用迁回 config.env"。
2. 改 `cg-platform-deploy.sh` map 注入段（L303-332）：加 slug 后缀两级查找（`secrets.get(f"{k}__{slug}") or secrets.get(k)`）；闸门左集认后缀键命中。改完 `sync-deploy-tooling.sh both`。
3. 建 `cg-platform/secrets-catalog.md`（committed 零值，9 真 secret + A/B 标 + 标准名）+ 轻量 tripwire（map 出现目录外新字段名则告警），注册 `auto-monster/scripts/tripwire_check.py`（准入三问②兑现 + 根治 WFLOW_PASSWORD 命名漂移）。
4. 迁移：WECHAT_SECRET 两值改 slug 后缀键 + 删裸键；cg-inspector-map env-file 删 WECHAT_SECRET、WFLOW 元数据迁 config.env。test 绿后同步 prod。
5. **升级 tripwire**：当出现第 ≥3 个需 per-app 命名空间的字段（多应用各自 `*_API_KEY` 等）时，把 flat 后缀键升级为 datasources.json 同构 slug 嵌套——届时数据点足够。
6. sync-creds.sh **不改**（不分新文件，flat 后缀键省掉了这一步）。

### 核心假设

1. **B 类撞车面极小（实测仅 WECHAT_SECRET）这一事实持续成立**——基于物理读 secrets.test.json 23 字段 + 你给的冲突实证。若未来大量应用引入各自 `*_API_KEY`（per-app 值），B 类会涨，但 slug 嵌套形态正是为这个涨设计的、涨不破模型。
2. **datasources.json 的 slug 嵌套形态已 prod 验证可复用**——6 个 app entry 实证 grouped 结构在跑，secrets per-app 区照抄同形态零新范式风险。
3. **per-app > 共享的注入优先级是对的默认**——给"某应用覆盖共享默认值"留路；若实际从无此需求，优先级是 no-op 不造成错误。

### 可能出错的地方

- **最可能崩点：命名目录沦为又一个无传感器的软约定**（概率中）。secrets-catalog.md 若只是一份"建议查"的文档、没有 map↔目录一致性的机械 tripwire，半年后又漂回 WFLOW_PASSWORD vs WFLOW_DB_PASSWORD 老路——这正是它要根治的病。所以问 4 第 4 步的 tripwire 不是可选项，是目录成立的承重前提（同今早 I-config-leak-gate 之于 config 进 git）。
- 次可能：物理两文件让 onboard 一个带企微的新应用要"同时改 secrets.json 嵌套 + 查目录确认 A 类已在共享区"，比单文件多一步。缓解：onboard 脚本（cg_platform_onboard.py）把"写 per-app secret 区"编排进去，不靠手改。

### 本次哪里思考得不够

- 没展开 `BRIDGE_TOKEN` / `IOS_TOKEN` 这两个字段的 A/B 归类是否真 A 类——我按"非 WECHAT_SECRET 即归 A"快速分类，但 IOS_TOKEN 听起来可能 per-app（某 iOS 应用一个 token）。建表时需逐字段确认归类，不能照搬我的"22 全 A"粗分。
- 没核实 deploy.sh L303-332 之外是否还有别处读 SECRETS_FILE（如 drift_audit.py 是否扫 secrets map）——辐射检查留实现层 grep `SECRETS_FILE` / `secrets.*json` 全引用方。

### 如果 N 个月后证明决策错了，最可能的根因

物理分三文件（datasources / secrets-shared / secrets）后，"某字段该录哪份"的判断负担转移给了 PM/onboard 脚本，若目录 + tripwire 没真正兜住，会出现"录错文件→注入不命中→应用启动 fail-fast→又要人肉排查录哪了"的新型 drift。根因会是"把存储分治的复杂度从 deploy 端推给了录入端、但录入端的检验传感器没跟上"。对冲已内置（问 4 第 4 步 tripwire + onboard 脚本编排），但若实现时省了 tripwire 只做文档，这条根因兑现。

### 北极星触达

**#1 二阶效应**：flat map 单字段装不下 N 值是一阶症状，结构因是"A 类共享凭据和 B 类 per-app 密钥被焊进同一个 flat 载体"。裁决拆载体（按真相拥有者分文件）+ 建命名目录传感器治漂移，是结构根治不是兜底补丁——跟今早 config/secret 分治是同一个 essence 的第二个活体。

### essence 对齐自检（必填）

- **本决策跟哪几滴 essence 对位**：今早自己提的候选 `red-line-overcoverage-from-carrier-coupling`（红线/约束被过度泛化源于载体耦合，拆载体比加豁免根治——这次是它的第二个活体，从 config/secret 扩到 shared/per-app）；`ssot-distillation-vs-buffering`（"B 类走 env-file 兜底"是软缓冲层、放任不一致逃过审视，否决它选真分治）；`reversibility-not-permission`（A 类不动 / 只迁 B 类一字段 = 按爆炸半径分治迁移）；monster 侧 `attribute-failure-layer-before-restructure`（命名漂移是 L2 缺对账锚点的结构问题，目录+tripwire 是结构动作不是加规则）。
- **本决策是否在某条 essence 上反着走**：潜在张力 `tool-elevation-as-occam` / OCCAM——分三个凭据文件是不是过度工程？判断不是：三类的真相拥有者 / 变更频率 / 爆炸半径全不同（平台 per-app DB / 全平台共享 / 应用 per-app 密钥），物理分文件让 sync 和心智边界一刀切干净，比单文件多语义混合区（候选 b）更 OCCAM——OCCAM 是"最少的认知复杂度"不是"最少的文件数"。
- **cross-check 用的关键词**：本次 grep 了今早 reflection 的 `red-line-overcoverage-from-carrier-coupling`（同源确认）+ 凭 CORE §7 可逆性二分 + gg-briefing B5/B7 内化判断 + essence `ssot-distillation-vs-buffering`/`default-bucket-as-deadlock`（否决 env-file 兜底的依据）。

### essence 候选（可选）

- slug: `carrier-coupling-overcoverage`（升级今早候选——把 `red-line-overcoverage-from-carrier-coupling` 泛化）
- 一句话: 一个载体被多类"真相拥有者不同"的值共用时，针对其中一类的约束/形态会过度泛化到全体（红线过包覆 / flat 单字段装不下 N 值）——拆载体按真相拥有者分治，比给共用载体加豁免/兜底更根治。
- 是否已 append 到 essence.md: N（留 Keith review，与今早候选合并定稿避免噪音）

### 外部锚点（可选）

- `~/githubProject/monster/cg-platform/integration-contract.md` §2（secrets map 段，本次裁决落点）
- `~/githubProject/monster/cg-platform/docs/env-management.md`（今早 config/secret 分治，同源前序）
- `~/githubProject/gg/memory/reflections/2026-06-25_cgplatform-config-secret-split-home-of-record.md`（同日同把刀第一刀）
