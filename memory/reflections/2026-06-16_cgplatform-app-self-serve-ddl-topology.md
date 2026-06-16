---
date: 2026-06-16
slug: cgplatform-app-self-serve-ddl-topology
summoner: monster (cg-platform)
northstar_reach: "#1 二阶效应（拓扑切换的真承重点不在 Keith 提的两个方向轴上）"
status: substantive-decision
---

# Reflection: cg-platform 共用库→独立库拓扑切换 + 应用自治建表

## §A 范式 A — 决策的元属性反思

### 给父会话的最终输出（必填）

**推荐：方向一（每应用独立 database）做拓扑切换，但拒绝 Keith 隐式绑定的"runtime 进程持 DDL 权限"——把"应用自治建表"重切为"onboard/migration 期由平台侧权威进程持 DDL，runtime 进程只持 DML"。即"独立库 + DDL 与 DML 凭据分离"。**

这是"方向一·B 变体"：要方向一的拓扑（解隔离+解瓶颈），但不要 Keith 方向一原文里"GRANT ALL ON `<app>`.* 给 app user（含 DDL）"那一刀。

**裁决四问逐条：**

**Q1 拓扑切换值不值得做 / 一 vs 二？**
值得做，选方向一（独立库），但走 B 变体。方向二（共用库 + CI 代跑 migration）解不了根——它只搬走 Keith 的手，没搬走"中心 schema 台账成为单点"这个结构性瓶颈，且共用库下 essence `network-cannot-cut-what-shares-tuple` 的幻觉隔离层一直在（脚本 line 333 已自承"契约2网络层已消解、横向隔离全靠契约1 GRANT"——逐表 GRANT 是 5.7 下唯一还能切的刀，一旦给 app user 整库 CREATE 这把刀立刻钝掉）。独立库把隔离从"GRANT 逐表枚举"升级到"库边界"——这是分辨率匹配的刀（库边界切库级隔离），不是低分辨率刀硬切高分辨率边界。

**Q2 三个设计意图哪些承重不能弃 / AI 持 DDL 风险怎么权衡？**
- **隔离 = 承重，但换更硬的形态**：从"逐表 GRANT 前缀隔离"换成"库边界隔离"，更硬不更软。承重判据不是"保留 APP_REGISTRY"，是"app 进程读不到别的 app/业务库"——独立库 + `GRANT ... ON <app>.*`（不含 DDL）对 DML 完全满足，且比表前缀硬。
- **中心台账 = 可换形态，但不能弃"存在性"**：APP_REGISTRY 作为"所有表 DDL 写死在一个 .py"的形态可弃（它正是瓶颈本体）；但"平台知道每个库里有哪些表"这个能力不能弃——换成 `information_schema` 巡检 + 每库的版本化 migration 文件（git 留痕）。台账从"事前白名单"变"事后可巡检 + migration 可追溯"。Keith 这条判断对。
- **留痕审计 = 承重不能弃，但"禁运行时动态注册"这条红线要重新定位**：留痕的承重内核是"DDL 变更可追溯、可审计、可回滚"，不是"DDL 必须经 git commit 才能跑"。B 变体用版本化 migration 文件（每个 migration 是 git 文件 + 执行日志）满足留痕内核，比 APP_REGISTRY 单文件更细粒度。
- **AI 持 DDL 直改生产库结构——这是整个决策的真承重墙，我的裁断：runtime 进程绝不持 DDL（essence `execute-untrusted-code-never-holds-prod-trust` 硬命中——thread line 17「AI 生成代码+AI 运行」物理坐实 runtime 跑不可信代码）。但 Keith 把"AI 持 DDL"和"应用自治建表"焊死了，这是假约束。** 解耦点：建表（DDL）发生在 onboard/migration 期，由平台侧一个**不跑业务代码的权威 provisioning 进程**持 DDL 凭据执行；runtime 容器里的 app user 只有 `SELECT/INSERT/UPDATE/DELETE`，无 `CREATE/ALTER/DROP`。"应用自治"自治的是"提交 migration 文件不经 Keith"，不是"runtime 持 DDL 权"。这样既解了 Keith 的人肉瓶颈（migration 走自动化 provisioning，不经 Keith 手改 .py），又守住了"执行不可信代码的环境不持生产 DDL 信任"这条切根刀。

**Q3 迁移成本 / 新老并存？**
新老并存——但不是"老的留共用库等死"，是**老应用零迁移、永久留共用库，新应用走独立库**。理由：8 个 db:null 应用根本不碰这套（onboard 脚本已确认它们跳过整个 DB provisioning）；真正有表的只有 cg-meetos（6 表，RO_JUDGE 列级隔离是它独有的精细需求）+ cgx（其实也是 db:null）。即真正受影响的存量 = **1 个**（cg-meetos）。强迁 cg-meetos 要重做它的列级隔离语义、风险/收益极不划算。让共用库范式作为"已封存的 legacy 拓扑"对 cg-meetos 继续有效，新拓扑只接新应用——双拓扑并存的治理成本由"老侧冻结不再 onboard 新应用进共用库"控制，不是长期维护两套活拓扑。

**Q4 没看到的承重点 / 更优第三方向？**
三个 Keith 没点破的承重点：
1. **真承重点不在"共用库 vs 独立库"这根轴上，在"DDL 凭据持有者是不是跑不可信代码的进程"这根正交轴上**（essence `separation-need-is-not-topology-verdict` + `control-flow-vs-fact-supply`）。方向一原文把拓扑切换和"runtime 持 DDL"打包，是把两个正交决策焊成一个——拆开后发现拓扑该切、DDL 权不该给 runtime。
2. **migration 执行进程本身就是新的"执行不可信代码"攻击面**——AI 生成的 migration SQL 由 provisioning 进程用高权限 root/DDL 凭据执行，这跟 thread 已识别的"build 阶段 pnpm build 是任意代码执行"同源。承重要求：migration 执行进程的凭据**只能 DDL 不能跨库**（`GRANT CREATE,ALTER,DROP ON <app>.*`，不是全局 root），且 migration 内容要过 essence `deploy-decision-must-not-read-untrusted-controllable-inputs` 同款约束——AI 生成的 migration 是"不可信方可写的输入"，执行它的进程权限必须收敛到"即便 migration 是恶意的也只能炸自己库"。pinme 暴露的"AI 生成 migration 灌爆"资源配额盲点（thread 162 行已登记）在这里一并接住。
3. **独立库下 dev_ro 跨库读业务库的设计不受影响**——dev_ro 本来就是库级 GRANT，独立库拓扑下它照常 `GRANT SELECT ON cgManager/wflow/cgdata.*`，无损。这点 Keith 的"列级对应用读自己表无意义≈无损"判断我同意，但要补一句：列级 GRANT 唯一真承重的是 cg-meetos 的 RO_JUDGE（deterministic_data 列防写污染）——这是它留在共用库 legacy 的额外理由，独立库 + 整库 DML 会丢掉这个列级防护，但新应用若需要列级防护可在 migration 里单独建。

**没有更优第三方向**——B 变体已经是"切根刀"（凭据分离）而非"加围栏"（CI 锁 ci.yml 那种猫鼠游戏），符合 essence `execute-untrusted-code-never-holds-prod-trust` 的"唯一切根的刀=物理分离两环境"。

### 行动建议（给父会话/Keith）
1. 拓扑：新应用 onboard = `CREATE DATABASE <app>` + 两类 user：`<app>_app`（runtime，仅 DML，进容器 env-file）+ `<app>_ddl`（provisioning 期 DDL，仅 `CREATE/ALTER/DROP ON <app>.*`，**绝不进容器**，在 Keith 机器/CI provisioning 阶段用）。dev_ro 照旧。
2. 台账：弃 APP_REGISTRY 硬编码 DDL；改每库 `migrations/` 目录（版本化 SQL，git 留痕）+ `information_schema` 事后巡检脚本（替代事前白名单的 schema SSOT 角色）。
3. 自治闭环：PM/开发者提 migration 文件 → provisioning 进程（不跑业务代码）用 `<app>_ddl` 凭据执行 → 不经 Keith 手改。Keith 的人肉环节消失，但 DDL 信任锚点留在"不执行不可信业务代码的 provisioning 进程"。
4. migration 执行进程加资源配额护栏（接 pinme 盲点 + thread 162 登记项）。
5. 存量：cg-meetos + 任何已有表应用零迁移留共用库（legacy 拓扑冻结，不再 onboard 新应用进共用库）；8 个 db:null 不受影响。
6. **这是契约 1 核心安全契约的拓扑级变更——Keith 拍板后应走 cg-platform 设计模式正式改契约措辞，不在本次召唤内单方面改契约文本**（gg 不执行决策）。

### 核心假设
1. runtime 容器进程确实跑 AI 生成的不可信代码（thread line 17 坐实，强）。
2. MySQL 5.7 支持库级 DDL GRANT 分离（`GRANT CREATE,ALTER,DROP ON <db>.*` 与 `GRANT SELECT,INSERT,UPDATE,DELETE ON <db>.*` 可授给不同 user）——这是标准 5.7 语义，强假设但未在本会话物理核验，建议落地前 dry-run 验一次。
3. 存量有表应用只有 cg-meetos 1 个真受影响（onboard 脚本 + registry 显示 8/10 是 db:null，cgx 也是 db:null）。

### 可能出错的地方
最可能崩点：假设 2 若 5.7 实例配置或 proxy 层有限制导致库级 DDL GRANT 不能干净分离（概率低但非零），B 变体的"DDL/DML 凭据分离"落不下来，会退化成"要么 app user 持 DDL（破安全）要么回平台手动（回瓶颈）"——届时方向二反而成兜底。所以行动建议 1 必须先 dry-run 验证 DDL GRANT 分离。

### 本次哪里思考得不够
没有物理核验假设 2（库级 DDL GRANT 分离），只凭 5.7 标准语义先验下断言——按 physical-anchor 纪律这是中间机制前提未核（essence `mechanism-relocation-has-its-own-precondition` 活体：给出"移到 provisioning 进程"诊断，但没核 provisioning 进程那个位置真能干净持 DDL 而不跨库）。已在行动建议里标"落地前 dry-run 验"，但裁决本身建立在未核前提上，诚实标注。

### 如果 N 个月后证明决策错了，最可能的根因
migration 执行进程（持 `<app>_ddl` 的 provisioning 进程）成为新瓶颈或新攻击面被低估——把 Keith 的人肉瓶颈搬到了 provisioning 自动化上，若该进程的 AI 生成 migration 审查/配额没做扎实，"AI 持 DDL"的风险从 runtime 搬到了 provisioning 期，只是换了时刻没换性质。

### 北极星触达
#1 二阶效应——核心价值是拆穿"应用自治建表 = runtime 持 DDL"这个焊死的假约束，把决策从 Keith 给的"拓扑轴"挪到真承重的"DDL 凭据持有者轴"。

### essence 对齐自检（必填）
- **本决策跟哪几滴 essence 对位**：`execute-untrusted-code-never-holds-prod-trust`（2026-05-18，runtime 跑不可信代码绝不持生产 DDL 信任——本决策核心）/ `owning-service-not-proxy-for-write`（2026-06-10，隔离不变量锚在"进程是否持库凭据"不锚在"数据是不是业务数据"——本决策锚在"进程是否跑不可信代码"）/ `network-cannot-cut-what-shares-tuple`（2026-05-19，共用库下逐表 GRANT 是唯一能切的刀、给整库 CREATE 即钝刀）/ `separation-need-is-not-topology-verdict`（2026-06-10，需要分离 ≠ 自动等于造新拓扑——本决策反向应用：这次拓扑切换确实成立，但 Keith 焊死的"runtime 持 DDL"被拆出来用更轻的凭据分离解）/ `deploy-decision-must-not-read-untrusted-controllable-inputs`（2026-05-19，migration 执行进程接同款约束）/ `snapshot-as-immutable-archive-not-single-file`（2026-05-19，"应用自治"是产品诉求、"runtime 持 DDL"只是它最弱的兑现，拆开用更强机制接）
- **本决策是否在某条 essence 上反着走**：潜在张力——`separation-need-is-not-topology-verdict` 说"升格拓扑前先试最轻治理形态、物理证据证明装不下再造墙"，而本决策**支持**拓扑切换（造库边界这堵墙）。为何这次例外合理：方向二（共用库不切、只 CI 代跑）正是"最轻治理形态"，但它装不下的物理证据是确凿的——5.7 下共用库给 app 自治建表必给整库 CREATE（破隔离）或回平台预建（回瓶颈），二者皆死，逐表 GRANT 的刀在自治诉求下钝化（network-cannot-cut-what-shares-tuple）。即"试过最轻形态、物理证明装不下"这个前置条件本决策满足，故造库边界墙合理，不是 engineering-impulse。
- **cross-check 用的关键词**：`grep -iE "ddl|tenant|database|grant|prefix|isolation|migration|untrusted|prod.*trust|tuple|owning-service|separation-need"`（essence.md 全文）

### essence 候选（可选）
- slug: self-serve-decouples-submission-from-execution-privilege
- 一句话: "自治"诉求的承重内核是"提交不经守门人"，不是"执行进程持高权限"——把提交权（DDL migration 文件不经 Keith）和执行权（谁的进程持 DDL 凭据）拆开，自治给提交侧、高权限留不跑不可信代码的执行侧；二者被焊死时（"应用自治建表=runtime 持 DDL"）是把人体工学诉求伪装成权限架构诉求。是 `execute-untrusted-code-never-holds-prod-trust` 在"自治需求"维度的对偶 + `snapshot-as-immutable-archive-not-single-file`（产品给的实现路线是其诉求最弱的兑现）的合并落点。
- 是否已 append 到 essence.md: N（留 Keith review 后决定，本次仅候选）

### 外部锚点（可选）
- `~/githubProject/monster/threads/cg-platform.md`（契约 1 主时间线）
- `~/githubProject/monster/shared/scripts/cg_platform_create_app_db.py`（契约 1 权威实现，待拍板后改）
