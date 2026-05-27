---
date: 2026-05-26
slug: cgplatform-contract1-applicability-decoupling
summoner: monster (cg-platform)
northstar_reach: #3 决策超越直觉
status: substantive-decision
---

# Reflection: cg-platform 沙箱契约 1 反向验证闸门适用域解耦

### 给父会话的最终输出（必填）

**推荐**：三问全拍——

- **Q1**：阶段 1 解耦方案接受，但**判定信号源从内存 `tables` dict 派生**（不绕 registry.json）——`any(mode == "RO_JUDGE" for _, mode in tables.values())`。无 RO_JUDGE 表时显式日志 `[env] _verify_isolation 测 2 跳过：tables 中无 RO_JUDGE 模式` 后 return。测 2 内部表名/列名仍硬编码（cg-meetos 唯一 RO_JUDGE 实例，不元数据化），加注释标 invariant + 第二个 RO_JUDGE 用例出现时升级。
- **Q2**：选 b——cgx 完全跳过 DB 流程。registry.json 加 `db: null` 字段（显式 null，非缺字段）；`create_app_db.py` 入口判 `if not tables: skip + log`。否决选 a（建空 user 立"每 app 必有 user"伪范式）+ 选 c（dev_ro 无调研对象）。
- **Q3**：`_verify_dev_ro` 测 2 同步解耦但**判据不同**：`len(tables) > 0` 即跑（不限 RO_JUDGE，因为 dev_ro 测的是"全程只读"通用承重），测试表挑 `tables` 第一张（不硬编码 `_snapshot` 后缀）。

**理由**：

1. 当前 `_verify_isolation` 测 2 承重对象是"列级排除是否生效"——唯一信号源是 GRANT_PRIV 字典中 `RO_JUDGE` 模式（含 `UPDATE (judgment_data, render_html)` 列级声明）。无 RO_JUDGE 表 = 无列级 GRANT = 测 2 没承重对象。表名 `_snapshot` + 列名 `deterministic_data` 是从 cg-meetos 实物归纳硬编码——是"实物形态"不是"契约形态"。判据应该挂在契约形态（GRANT mode）上，不是实物形态（表名后缀）上。
2. 从内存 `tables` dict 派生而非从 registry.json 派生——registry.json 是部署后的事实记录，闸门跑在写入之前；内存 dict 是当前部署动作的输入参数，更直接 + 不绕弯。
3. cgx 选 b 让基建层正式支持"无 DB 应用"形态——Keith 已明示"后面也有可能还有这种纯的 HTML 的应用"，第二个静态站需求已在视野内（不是 `theory-gap-without-data` 凭空猜未来），现在立"db: null"形态比为对称性建空 user 更扎实。
4. Q3 同步解耦防 `bug-shape-survives-fix` 反向复发——同一函数结构里两个 `_snapshot` 硬编码，只改一个下次撞同形态问题；判据不同但解耦动作必须同步。

**trade-off**：

- 阶段 1 RO_JUDGE 表名/列名仍硬编码——第二个 RO_JUDGE 应用出现时再升级元数据化（schema 加 `column_excluded` 字段）。当前避免在 `theory-gap-without-data` 下叠未验证抽象。
- cgx server 健康检查需要自行处理 `db: null` 情况（不走 mysql ping）——这是 cgx 自家工程，非基建层负担。Keith 已说明 cgx server 几乎无业务逻辑，加 health 端点条件分支不增加显著复杂度。
- 未核验假设：第二个静态站真的会出现（Keith 说"也有可能"，不是 committed）——若长期只有 cgx 一个，"db: null"形态的基建层支持只服务单一应用，等价于轻度过度工程。但比"建空 user"代价小（多 5-10 行 if 分支 vs 永久不用的 MySQL user/凭据/env-file）。

**行动建议**：

1. 改 `shared/scripts/cg_platform_create_app_db.py`：
   - `_verify_isolation(env, env_file, app, tables)` 签名加 `tables` 参数；入口判 RO_JUDGE 存在性，无则跳过测 2 + 显式日志
   - `_verify_dev_ro(dev_ro_env_file, app, tables)` 签名加 `tables` 参数；入口判 `len(tables) > 0`，无则跳过测 2 + 显式日志
   - `_build_one_env` 入口判 `if not tables: skip_db_provisioning + log + return registry_fragment_with_db_null`
   - registry.json 写入逻辑支持 `db: null` 字段
2. cgx 走 `APP_REGISTRY["cgx"]` 中 `tables = {}` + 注册流程产出 `db: null` 的 registry.json 条目
3. cgx server 健康检查代码处理 `db: null`（返 `{status: ok, db: null}`，不走 mysql ping）——cgx 工作区任务，非 cg-platform 基建变更
4. 更新 `cg-platform/integration-contract.md` 契约 1 段：补"列级隔离测仅对声明了 RO_JUDGE 模式的应用承重；纯静态/无 DB 应用整体跳过 DB 流程，但仍走 registry 登记（`db: null` 字段）"
5. 落 thread：`monster/threads/cg-platform.md` append 一条 5-26 entry——契约 1 适用域解耦 + cgx 形态"无 DB 应用"基建层正式支持

### 核心假设

1. cg-meetos 是当前唯一 RO_JUDGE 应用——已物理核验（APP_REGISTRY 中只有 cg-meetos 表里有 RO_JUDGE mode）
2. cgx server 健康检查由 cgx 自家工程承担——Keith 表述"server 几乎无业务逻辑，目前不需要 DB"暗示 cgx 工作区会处理
3. Keith 说"后面也有可能还有这种纯的 HTML 的应用"——第二个静态站需求在视野内但未 committed，决策按 50%/50% 概率赋权（"db: null"形态值得立，但不为它建复杂机制）

### 可能出错的地方

1. **最大风险**：阶段 2 元数据化无限期 park——第二个 RO_JUDGE 应用出现时没有触发器提醒升级，又一次直接硬编码 + 命中 `bug-shape-survives-fix`。**对冲**：在 `_verify_isolation` 测 2 内部加注释 `# TODO: 第二个 RO_JUDGE 应用出现时升级元数据化（见 reflection 2026-05-26_cgplatform-contract1-applicability-decoupling.md）` + 同步 `monster/threads/cg-platform.md` 留 tripwire 记录
2. **中等风险**：cgx server 健康检查处理 `db: null` 的实现质量不在 cg-platform 基建层闸门下——cgx 自家工程可能写出"无 DB 但 health 仍 mysql ping 报错"的破口。**对冲**：契约文档明示 cgx 类应用 server 必须自行处理 db=null，cg-platform 基建不替它兜底

### 本次哪里思考得不够

- 没核 `_dry_run` / 其他调用 `_verify_isolation` 的代码路径——加 `tables` 参数是 signature 变更，理论上 grep 全引用方再下手；实施时主代理需做辐射检查（按全局 CLAUDE.md Delivery Standard 辐射检查段）
- 没考虑"应用从有 DB 演化到无 DB"或反方向的迁移路径——当前决策假设应用类型在创建时就锁死，未来若需要迁移会撞机制

### 如果 N 个月后证明决策错了，最可能的根因

- **#1 候选**：第二个 RO_JUDGE 应用出现时仍未升级元数据化，第三个应用的表名/列名跟 cg-meetos 不一致，硬编码 + 静默失败（测 2 SQL 报 unknown column 但被当 IsolationGateFailure 抛——这是 fail-loud，不是静默 = 反而是好事；真正风险是表名一致但列名不一致 → 测 2 误绿）。**预防**：加注释 + thread 留 tripwire。
- **#2 候选**：cgx 类应用增多，"db: null"形态的基建层支持成为新承重——若有应用从"无 DB"演化到"有 DB"（cgx 加用户反馈表），整个 db: null → db: {...} 的迁移路径没设计过，需要走完整新建流程（drop&recreate）或临时给 dev_ro 加 grant 等 hack。

### 北极星触达

**#3 决策超越直觉**：从"测 2 是普适契约必跑"的直觉判断（隐式假设所有应用都有列级排除测的承重对象），看穿"测 2 承重对象只对 RO_JUDGE 应用存在"的契约真相。判定信号源选择（GRANT_PRIV mode 而非 registry.json table_modes 而非表名后缀）也是反直觉——最直观的"表名带 `_snapshot` 就跑"被否决，最契约化的"GRANT mode 有 RO_JUDGE 就跑"被选。

### essence 对齐自检（必填）

- **本决策跟哪几滴 essence 对位**（列 slug，至少 1 条）：
  - `gate-as-physical-fuse-not-business-metric` (2026-05-07)——契约 1 闸门是物理保险丝（贴 GRANT 写权行为），不是业务指标；本决策让保险丝只装在有承重对象的应用上，不替无 RO_JUDGE 应用造伪保险丝
  - `theory-gap-without-data` (2026-05-06)——阶段 2 元数据化不做，没数据支撑（cg-meetos 单实例）
  - `network-cannot-cut-what-shares-tuple` + `safe-default-by-whitelist-inversion` (2026-05-19)——契约 1 立约的根方向不变（GRANT 物理隔离 + 准入白名单），本决策不动这层
  - `mechanism-relocation-has-its-own-precondition` (2026-05-19)——解耦前已物理核验"无 RO_JUDGE 表则列级 GRANT 不会被生成"这一前提（GRANT_PRIV 字典只有 RO_JUDGE 涉及列级，代码层证据）
  - `bug-shape-survives-fix` (2026-04-27)——Q3 同步解耦 `_verify_dev_ro` 测 2 防同形态复发，不只改一个对称的那个
- **本决策是否在某条 essence 上反着走**（有 = 必须解释 / 无 = 明示）：
  - **潜在张力，未展开**：`tool-elevation-as-occam` (2026-05-06) "第二个消费者出现时把工具上提到共享层是 OCCAM"——本决策对"无 DB 应用"形态做了基建层支持（"db: null"形态），是为预期中的第二个静态站立结构。但 Keith 表述"也有可能"≠ committed 第二个消费者已出现，介于"上提 OCCAM"和"过早抽象"之间。**判断**：cgx 已经是真实第一个应用，"db: null"基建层支持是为 cgx 立结构而非为想象的第二个应用立，所以不是过早抽象——若长期只有 cgx 一个静态站，"db: null"支持服务单一应用是 OCCAM 在"无 DB 应用 ≠ 跳过 registry 登记"的合理代价
- **cross-check 用的关键词**（物理证据）：闸门 / 适用域 / 解耦 / 元数据 / 应用类型 / 物理保险丝 / 演化 / 抽象 / OCCAM / 第二个

### essence 候选（可选）

- slug: `gate-applicability-derives-from-load-bearing-object`
- 一句话: 物理保险丝的适用域由"被保护对象是否存在"派生，不由"应用是否属于某类"声明——前者是契约形态判定（pull），后者是分类标签判定（push），后者会在分类粒度跟保护对象粒度错配时静默失能或伪保护
- 是否已 append 到 essence.md: N（议题性质边缘，"保险丝随承重对象存在性派生"概念上是 `gate-as-physical-fuse-not-business-metric` 的应用而非新洞察——同 essence 滴成立的具体落地形态。**判定不沉淀**——避免稀释 essence 浓度。本议题归档进 reflection 即可）

### 外部锚点（可选）

- `~/githubProject/monster/threads/cg-platform.md` ← 接续 5/19 契约 2 消解后续治理时间线
- `~/githubProject/monster/cg-platform/integration-contract.md` ← 契约 1 文档需同步更新
- `~/githubProject/monster/shared/scripts/cg_platform_create_app_db.py` ← 实施落点（`_verify_isolation` + `_verify_dev_ro` + `_build_one_env`）
