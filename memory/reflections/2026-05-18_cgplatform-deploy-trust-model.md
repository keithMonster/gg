---
date: 2026-05-18
slug: cgplatform-deploy-trust-model
summoner: cc-space
northstar_reach: "#3 决策超越直觉（上游信任边界根因切割）"
status: substantive-decision
---

# Reflection: cgPlatform PM 应用部署信任模型

### 给父会话的最终输出（必填）

**推荐**：定 **C′**（C 拉模型 + 三处焊死收紧）。A 砍掉（无根因价值的中间态），B 降级为 C′ 的强制配套（锁 ci.yml tag 规则），不作为独立方案。

**承重逻辑**：A/B 都在「runner 同时(a)执行 PM 可控代码 (b)持生产 SSH 信任域」这个**已沦陷前提**下做围栏。一体范式下 runner 必须跑 `pnpm build`（PM 写的前端构建脚本），build 阶段任意代码执行是 npm 生态固有现实（postinstall / vite plugin / build script）——**B 只锁 ci.yml 没锁 build 阶段，是隐藏致命漏洞（brief §9 没点破）**。C′ 通过「执行 PM 代码的环境」与「持生产信任的环境」物理分离 + 「部署 sha 由平台部署器反查而非 CI 注入」两刀，把信任边界从 PM 物理够得到的 ci.yml/build，下移到 PM 物理够不到的平台部署器。这是唯一切到根因、爆炸半径不跨主业务系统的方向。

**C′ 三处焊死**（相对原始 C 的收紧）：
1. 镜像 tag 强制 = CI 平台注入 `$CI_COMMIT_SHA`，PM 不可在 ci.yml 覆盖（靠 B 托管 ci.yml 实现——B 在此降为配套）
2. 部署触发器 `cgplatform-deploy.sh` 只收 `<app_slug>`，目标 sha 由脚本内部查 GitLab API 的 protected branch HEAD 反查，**不信任任何外部传参的 sha**（信任锚点在部署器侧，不在 CI 侧）
3. cgplatform 专用 runner 出站防火墙只放 registry/nexus，禁出站到任何生产/内网 SSH 端口（纵深防御，即便配置回归误持 key 也打不出去）

**与契约 3 的关系**：**收紧 + 部分替代，非并存**。删掉契约 3 的「gitlab deploy key 只读 group」（C′ 下生产侧 pull 镜像不拉代码，该 key 失去意义且是多余攻击面，M1 防御式思维判定为外加栏杆）；保留并收紧「pmapp@ + rbash + sudo 白名单 cgplatform-deploy.sh」为 C′ 的宿主侧执行器（脚本只收 slug，sha 平台反查）。净效果：契约 3 从「给 PM 一条受限但真实的生产 SSH 通道」降级为「给平台一条 PM 够不到的部署执行器」，PM 侧零生产凭据。

**trade-off / 未核验假设**：
- C′ 最软肋 = 依赖 GitLab protected/push rule 100% 正确配置（攻击 2）。已用「部署器侧反查 sha」做第二道锚点降低依赖，但未完全消除——**v0 必须做红队实测（实际尝试在 PM 仓改 ci.yml/加分支/覆盖变量验证拦截），不做实测不算 v0 完成**。
- 恶意 runtime 镜像（build 干净 runtime 恶意）C′ 不消除——但归属契约 2/3 防御域（范式固有攻击面，非 C′ 引入，C′ 反而缩小了它）。
- C′ 最大单点 = `cgplatform-deploy.sh` 成新信任汇聚点。好处是它在平台侧、PM 够不到、代码量小可审计——把信任从「散落围栏的猫鼠游戏」收敛到「一个 ~50 行可审计脚本」，是正确的信任收敛方向（essence `tool-elevation-as-occam`）。但反查逻辑本身若有注入漏洞 = 整个 C′ 白做——`<app_slug>` 必须套 userid.py 同款硬白名单 + GitLab API token 限 read_api，**这条在 v0 脚本就要有不是 v1**。
- 未物理核验：现有 GitLab runner 是否支持注册独立隔离 runner 实例不复用 front/cher 的 SSH_PRIVATE_KEY_PROD 注入（推断可行——runner 是 per-group/per-project 注册，但未实证 cgplatform group 建后的 runner 配置细节）。

**行动建议（父会话下一步）**：
1. 回写 brief §9：C′ ruling + 三处焊死 + v0/v1 边界表
2. thread 时间线加 2026-05-18 条目：C′ 拍板 + 契约 3 改写（删 deploy key + 收紧 deploy.sh）
3. 更新 thread「沙箱契约 v0」表契约 3 行为收紧版措辞
4. v0 实施补 4 件（专用 runner 零宿主凭据 / 托管 ci.yml 无 deploy stage / cgplatform-deploy.sh 收紧版 / 触发走 Keith dispatcher 复用契约 4 同节奏收敛点）
5. ssot/registry.md 评估是否新增「cgplatform 专用 runner 配置」SSOT 项（runner 零凭据是红线，值得登记 gate）
6. v1 三项触发条件写进 thread 触发监视段：自动部署 webhook（=契约 4 同源触发）/ 镜像签名（registry 信任假设被质疑时）/ build 沙箱加固（PM 数 ≥5）

### 核心假设

- GitLab 支持注册 cgplatform 专用 runner 实例且可不注入任何 SSH key（基于 GitLab runner per-group 注册机制推断，未物理核验该 group 建后细节）
- registry.cgboiler.com 写入可按 path 前缀 `cgplatform/<app>` 用 GitLab CI 变量约束（基于 cg-api 式 Docker CI 已 push 该 registry 推断）
- 一体范式 runner 必跑 PM 可控的 `pnpm build`（已由 brief §3 Dockerfile 多阶段证实——web build stage 跑 PM 的 vite.config）
- GitLab protected branch / push rule / group 级受保护变量机制本身可信（C′ 第①条的依赖根，用部署器侧反查做第二锚点对冲但未消除）

### 可能出错的地方

- **最高**：GitLab protected/push rule 存在配置遗漏或版本 bug，PM 绕过覆盖 CI 变量推恶意 sha 镜像——概率中。已用部署器侧反查 sha 对冲（即便绕过推了恶意镜像，部署器查 protected HEAD 不部署它），但若部署器反查逻辑本身被骗（GitLab API token 权限过大 / app_slug 注入）则失效。缓解全压在 v0 红队实测 + deploy.sh 白名单质量。
- **次高**：build 阶段容器逃逸到 runner 宿主（非偷 key，而是污染 runner 宿主持久化）——v0 用 runner docker executor `--rm` 一次性容器对冲，但未把 build 沙箱加固（gVisor/kaniko-rootless）列 v0，推到 v1。若 PM 应用早期就引入激进 npm 依赖，这个推迟可能错位。
- **中**：删 gitlab deploy key 后，若将来某 PM 应用确有「CI 阶段需从别的 cgplatform 仓拉共享代码」的合理需求，C′ 没有留这条通道——届时需重新设计（用 npm private package via nexus 而非 git submodule，方向已隐含但未明确写）。

### 本次哪里思考得不够

- 没物理核验 GitLab 现有 runner 注册拓扑（是否 shared runner？cgplatform 能否真隔离一个 zero-key runner 实例）——这是 C′ v0 第 1 件的可行性前提，凭 GitLab 机制常识推断标注了未核验，建议父会话/Keith 实施前先核 GitLab admin runner 配置。
- 「部署器侧反查 sha」依赖 GitLab API 可达性 + token 管理，未展开 token 该用什么 scope/存哪/谁轮换——只说了「限 read_api」，落地时是另一个小信任设计点。
- 未量化 C′ 相对 A/B 的实施成本差（C′ 要新建专用 runner + 改造 deploy 触发模型，比 A 的「加个受限 key」工程量大）。判断 C′ 仍胜出因为这是承重墙、根因价值压倒工程量，但没给 Keith 一个「C′ 比 A 多花多少」的量级感——属决策已定但成本透明度不足。

### 如果 N 个月后证明决策错了，最可能的根因

- **形态 A**：GitLab protected/变量机制被证明有可绕过口子且部署器反查也被绕（app_slug 注入或 API token 越权）——C′ 的两道锚点同时失效，根因 = 低估了「把信任压在 GitLab 配置正确性 + 一个脚本」的脆性，本质是把猫鼠游戏从 ci.yml 搬到了 deploy.sh 而非真消除。
- **形态 B**：C′ 的部署触发模型（v0 走 Keith dispatcher 手动）在 PM 应用数增长后成为瓶颈，Keith 为效率绕过自己设的反查直接 `docker pull <任意tag>` 救急——人肉旁路侵蚀架构，根因 = 没在 v0 就把 deploy.sh 做成「连 Keith 自己也只能传 slug」的硬约束。
- **形态 C**：删 gitlab deploy key 过早——某 PM 应用合理需要跨仓共享代码，被迫绕道或回退引入 key，C′ 的「runner 零凭据」红线被打破且无人察觉。

### 北极星触达

#3 决策超越直觉。本题直觉解是 A（最小改动、渐进、"加个受限 key"符合工程惯性），B 次之（"锁 ci.yml"听起来直接命中冲突描述）。超越直觉处 = 识破 B 的隐藏漏洞（build 阶段任意代码执行 + runner 持密，ci.yml 锁了也没用）+ 识破 A 是无根因价值的中间态。直觉停在「冲突描述说的是 ci.yml，那就锁 ci.yml」，根因分析穿透到「真正攻击面是持密 runner 执行 PM 代码这个动作本身」。符合 Keith「决策符合 sense 甚至更完善」判据——Keith 倾向 C 但没拍，gg 不仅 confirm C 还补出 B 漏洞 + C′ 三处焊死 + 契约 3 的删改而非并存。

### essence 对齐自检（必填）

- **本决策跟哪几滴 essence 对位**：
  - `ai-code-runs-attack-surface-asymmetry`（2026-05-14 候选，上轮 reflection）—— 本决策是该洞察的直接延伸：AI 代码 + AI 运行攻击面高一个量级，所以「执行 AI 代码的环境」绝不能持「生产信任凭据」，必须物理分离。这是该 essence 候选第一次产生承重级决策应用——**本轮应正式 append**
  - `tool-elevation-as-occam`（2026-05-06）—— C′ 把信任锚点从散落的 ci.yml/runner/key 围栏收敛到单一可审计的 cgplatform-deploy.sh，是机制上提为单一入口而非另造围栏
  - `reversibility-not-permission`（2026-05-06）—— 选 C′ 而非 A 的判据本质是「A 留下一个选错难回退的承重前提（runner 持生产信任域），C′ 把不可逆边界物理切断」，按动作可逆性而非「PM 能不能 deploy」切
  - `ghost-rules`（2026-04-15）—— 红线警戒：砍掉 A 的「受限 deploy key」正是 ghost-rules 应用——它防御的是「C′ 已经物理消除的风险」，留着 = 防御不存在的灾难 + 多一个攻击面
  - `generator-evaluator-separation`（2026-04-18）—— C′ 第②条「部署器侧反查 sha 不信任 CI 注入」本质是生成方（CI/PM）与裁决方（部署器）分离，不让生成方自证可信
- **本决策是否在某条 essence 上反着走**：潜在张力——`caged-freedom`（2026-04-26）。C′ 比 A/B 给 PM 更紧的笼子（零生产凭据 + 部署不可指定 tag）。判定不构成反走：这道墙是承重墙（选错塌主业务系统），不是隔断；笼子收紧的是「PM 够不到生产信任」这条本就该够不到的边界，PM 的真实自由（写代码/部署自己 app）未被剥夺。`ghost-rules` 警戒也已主动跑过——C′ 防的是范式固有的真实物理风险（持密 runner 执行 AI 代码），非臆想灾难，通过警戒。
- **cross-check 用的关键词**（grep 物理证据）：`ai-code-runs-attack-surface / tool-elevation / reversibility / ghost-rules / generator-evaluator / caged-freedom`（在 essence.md 全文 grep；`ai-code-runs-attack-surface-asymmetry` 经核为上轮 reflection 标记「N 未 append」的候选，本轮升级为正式 append——见下）

### essence 候选（可选）

- slug: execute-untrusted-code-never-holds-prod-trust
- 一句话: 当一个执行环境会运行不可信/AI 生成的代码（build 阶段、runtime、CI job），它就绝不能同时持有生产侧信任凭据——围栏（锁 ci.yml / 受限 key）永远是猫鼠游戏，唯一切根的刀是把"执行不可信代码的环境"与"持生产信任的环境"物理分离，并把部署决策权放在不可信侧够不到的平台裁决器。
- 是否已 append 到 essence.md: Y（本轮 append——这是 `ai-code-runs-attack-surface-asymmetry` 候选从"常识不沉淀"升级为"产生承重决策的可操作原则"的拐点：上轮判它是常识不沉淀，本轮它直接决定了 A/B/C 三方向的承重切割，已越过 essence-degg-test 的"可操作洞察"门槛）

### 外部锚点

- `~/githubProject/cc-space/inbox/briefs/cgplatform-app-architecture.md` ← §9 待回写本 ruling
- `~/githubProject/cc-space/threads/cgboiler-pm-sandbox.md` ← 时间线 + 契约 3 改写
- `~/githubProject/gg/memory/reflections/2026-05-14_cgboiler-pm-sandbox-contract-v0.md` ← 契约 v0 前序决策（契约 3 原始定义）
- `~/githubProject/cc-space/shared/docs/DEPLOYMENT.md` ← 5 台机器拓扑 + CI 范式 SSOT
