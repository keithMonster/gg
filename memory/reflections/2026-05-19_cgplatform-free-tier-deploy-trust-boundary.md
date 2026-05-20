---
date: 2026-05-19
slug: cgplatform-free-tier-deploy-trust-boundary
summoner: cc-space
northstar_reach: "#3 决策超越直觉（在 Free 约束下找到不依赖 enforcement 的真不可绕过边界）"
status: substantive-decision
---

# Reflection: cgplatform GitLab Free 约束下的 build/deploy 信任边界形态

### 给父会话的最终输出（必填）

**推荐：形态 C″（registry-as-handoff）——CI 只构建产镜像绝不部署；部署由 PM 物理够不到的平台侧常驻 poller `cgplatform-deployd` 承载，它只认两个 PM 够不到的事实（GitLab API 反查的 protected/默认分支 HEAD sha + registry digest 存在性），反查可信源拉起 `cgplatform-deploy.sh`。员工体验零损（git push 即自动上线、零 SSH），但 push 链路在 PM 仓第一个 CI job 跑完那刻永久离开 PM 可控域。**

C″ 是 C′「平台裁决器反查可信源」在 Free 约束下的具体兑现，不是新方向。

**核心机制（物理判据）**：不锁 ci.yml（Free 锁不住，Keith 已弃 enforcement），而是让 **PM 能改的一切都不在部署决策函数的信任输入里**。部署决策 = `deploy(app) iff registry has image@(gitlab_api.protected_head(app))`。PM 对 `gitlab_api.protected_head(app)` 零写权（这是 GitLab 服务端基于 push+分支保护的状态，非 PM 仓内文件）→ PM 改自己仓任何文件只能改"镜像内容"，改不了"哪个 sha 被部署"。这就是不依赖 Ultimate Required pipeline、不依赖锁 ci.yml 的真不可绕过边界。

**四条物理判据**（每条回答"PM 改自己仓任何文件能否越过"，全部"不能"）：① runner 零 prod/SSH/deploy 凭据注入（攻击面清空非围栏）② runner 出站只放 registry/nexus 封死内网/prod SSH（纵深第二层）③ deployd 不读 PM 仓任何文件、不接受任何外部传参 sha/digest（PM 仓 yml/分支/CI variable 全在 deployd 信任输入之外）④ runner 唯一信任 = registry path 前缀 `cgplatform/<app>` 写权，且"能 push 镜像 ≠ 能让镜像上线"（上线决策权在 deployd，deployd 只认分支 HEAD 对应 sha 的镜像）。

**deploy.sh 仍是不变锚点零改动复用**，变的只是调用者身份：C′/契约 7 设想的"CI 触发器调"→ C″ 改"deployd 调"。deployd 在部署目标可用性域常驻，对齐 cc-gateway/huasheng「调度器与被调方同可用性域」既有范式。

**CC skill「部署 xxx」**退化为软层可选语义：① 仅作 deployd `/poke?app=<slug>`（不传 sha/digest，只催 deployd 跑一遍自己的反查）② 单环境要人眼则 deployd 配 `auto=false`，poll 出新镜像只通知不部署、等 `/poke` 执行——人眼闸门落 deployd 侧（PM 够不到）而非 CI 侧，比 GitLab manual 更干净，与单环境"点击人=Keith"一致。Keith 在 auto/manual 间选，不影响信任边界。

**与既有契约关系（钩子级，详细辐射父会话做）**：
- 契约 7：amend，框架（7.1/7.2/7.3/7.5）保留，实现假设 supersede——"deploy 是 CI 里平台强制 include 的 job"→"deploy 完全不在 CI、由 deployd 承载"。**7.4「配置锁定」整条消解**（依赖 Free 下证伪的 Ultimate Required pipeline，C″ 下 CI 压根无 deploy job 可被覆盖——ghost-rules 正向应用）。`cgplatform/ci_template` 从承重物降级为可选 build 公共片段。
- 契约 7.3「cgplatform-deploy-bot@ 私钥落 runner 宿主」：消解（与 thread 时间线父会话推导一致，本决策给出根因——CI 链路零 deploy 私钥，runner 唯一信任是 registry job token 非 SSH 私钥）。新信任汇聚点 = deployd 的 GitLab read_api token + sudo deploy.sh 能力，落 deployd 宿主，PM 够不到。
- 契约 3：amend，deploy.sh + rbash + sudo 白名单零改动保留，调用者身份改 deployd；删残留"给 PM/CI 受限部署通道"语义（PM/CI 双侧零部署凭据，部署能力 100% 收敛到 deployd）。
- 契约 1/2：零打折保留，正交不动。
- **roadmap.md / paas-deploy skill：amend，最关键待辐射点**——"部署引擎 = GitLab CI/CD"措辞不准确，应改"部署引擎 = 平台 deployd；CI 仅 push→镜像转换"。员工心智模型不变。**父会话机械推导收口("deploy 移出 CI")与 roadmap("CI/CD 自动部署")当前互相矛盾，C″ 是消解这个矛盾的缺失环节**——这是本次召唤暴露的真问题。
- integration-contract §5：amend，CI 产物=registry digest，部署接口=deployd poll 协议 + `/poke`（不收 sha）。
- ssot/registry.md：`cgplatform-deploy-bot@ 凭据落点`改写为 `cgplatform-deployd 凭据落点`（read_api token + deploy.sh sudo，PM/CI 双侧禁持）；新增 `cgplatform runner registry-push scope` gate。

**inversion（按概率，物理判据见 final message）**：
- ① deployd GitLab API token 权限过大（中高，最可能真实失效点）→ 物理判据：实测 token = `read_api` + 仅 cgplatform group 可读 + 不可写分支保护；落 deployd 宿主 chmod 600 禁进 CI variable/镜像层。**v0 必须红队实测**（等价 C′ "部署器反查被骗"那条）。
- ② PM 对默认分支有 push 权 → push 恶意 commit 即新 HEAD，deployd 忠实部署（中，范式级）。这不是 C″ 缺陷，是 Keith 明示接受的"不做权限"后果，归契约 1/2 爆炸半径 + 蓝绿回退。**揭示真张力，见下节。**
- ③ 半年后有人嫌 poll 慢加 webhook，webhook payload 的 sha 来自 PM push，若 deployd 信 payload sha 即被短路退回 C′ 警告的失败形态（中，时间衰减型）→ 物理判据：deployd 架构上只有 poll 一种事实获取方式，webhook/skill 只能是"催它查一次"的无参信号，永不读 payload 里 sha/ref。写进 deployd 设计契约。

**必须摊给 Keith 的真张力（不硬凑顺从）**：约束 A「不做权限、谁装插件谁能 push 谁上线」与约束 B「build/deploy 分离、不可信代码不持 prod 信任」之间有隐含张力。C″ 完美兑现 B（配置层攻击面物理清零），但 A 意味着业务代码层攻击面 Keith 主动敞开——装插件者 push `rm -rf`/数据外泄代码到默认分支，C″ 会安全地零 SSH 地部署它。**不冲突到"安全不变量 vs 目标层"程度**（B 的安全不变量 C″ 完整守住；A 敞开的是另一维度，Keith 知情的产品阶段取舍，与单环境定调同源）。故不否决、给一句话刻度请 Keith 确认知情：**C″ 安全承诺 = "部署链路不可被 PM 配置绕过 + 不可信构建环境零 prod 信任"，显式不承诺"被部署业务代码良性"——后者由"谁能 push 默认分支"决定，那层 Keith 当前已弃管控，回访触发点建议绑定契约 7 supersede 记录第 1 条同一个点（真实终端用户 / 补 test）。** 写进 roadmap 该处即与 Keith 风险姿态完全自洽无暗坑。

**行动建议（父会话）**：
1. 回写 roadmap.md：① 改"部署引擎=GitLab CI/CD"→"部署引擎=平台 deployd；CI 仅 push→镜像" ② 契约 supersede 记录第 1 条旁加 C″ 安全承诺边界刻度（业务代码良性不在承诺内 + 回访触发点绑定）
2. thread 时间线加 2026-05-19 C″ 条目：消解"deploy 移出 CI vs CI/CD 自动部署"矛盾 + 契约 7.4 消解 + 7.3 私钥落点消解根因 + 调用者身份改 deployd
3. integration-contract §5 改 CI/部署接口为 registry digest + deployd poll + `/poke` 无参
4. cgplatform/CLAUDE.md「已收口决策 CICD」段改：deploy 不在 CI，deployd 承载，ci_template 降级可选 build 片段
5. ssot/registry.md 改 deploy-bot@→deployd 凭据落点 + 新增 runner registry-push scope gate
6. v0 实施补：cgplatform 专用零 key runner / runner 出站防火墙规则 / cgplatform-deployd（poll + GitLab API 反查 + sudo deploy.sh + /poke 无参端点 + auto/manual 模式开关）/ deployd token red_api 红队实测（不实测不算 v0）
7. essence 已 append（slug deploy-decision-must-not-read-untrusted-controllable-inputs）

### 核心假设

- GitLab Free 的 API（查 protected/默认分支 HEAD sha + 查 registry digest）可用且可用 read_api 限权 PAT 访问（GitLab Free 完整含 API + container registry，置信度高，未实测该 token scope 边界）
- registry.cgboiler.com 可按 path 前缀 `cgplatform/<app>` 约束 runner 写权（基于 cg-api 式 Docker CI 已 push 该 registry 推断，C′ reflection 同假设未变）
- 部署目标宿主可常驻一个 poller 进程（deployd）且该进程 PM 无任何账号/触发入口（基于单环境=直接生产宿主 + cc-gateway/huasheng cron 同范式既有实证推断）
- "PM 对 `gitlab_api.protected_head` 零写权"——前提是默认分支保护开启或 PM push 权限不能改分支保护配置；但 inversion ② 已指出"不做权限"下 PM 对默认分支有 push 权本身使 HEAD 可被 PM 改（非配置漏洞，是 Keith 接受的风险，已在张力节摊明）

### 可能出错的地方

- 最高：deployd GitLab API token scope 给宽（api 写 / 跨 group），token 泄漏后攻击者改分支保护或越权——C″ 根基塌。缓解全压 v0 红队实测 token 边界 + 落点 chmod 600。这是 C′ "反查逻辑被骗"在 C″ 的同形态延续。
- 次高：deployd 单点——它是新信任汇聚点（read_api token + sudo deploy.sh）。好处是代码量小、PM 够不到、可审计（同 C′ tool-elevation-as-occam 信任收敛逻辑）；坏处是 deployd 自身有注入漏洞则全盘失效，`<slug>` 必须套 userid.py 同款硬白名单，这条 v0 脚本就要有不是 v1。
- 中：父会话/Keith 把 C″ 读成"只是给 C′ 换个触发器"，忽略它实质消解了 roadmap 与机械推导收口的文档矛盾——若 roadmap 措辞不回写，下游继续按"deploy 在 CI"实现，信任边界被焊回 PM 域，C″ 形同未决。

### 本次哪里思考得不够

- 没物理核验 registry.cgboiler.com 是否真支持 per-path-prefix 写权限约束（GitLab container registry 项目级，cgplatform group 下多 app 是否真能限到单 app 前缀未实证）——列 v0 实施验证项，凭 GitLab registry 机制常识推断标注未核
- deployd 的 poll 间隔 / 失败重试 / 同一 app 并发部署去重 / 部署失败回滚联动蓝绿——只给了架构骨架，运行时细节未展开，属决策方向已定但实现设计点待父会话/后续会话补
- 没量化 C″ 相对父会话已收口的"deploy 移出 CI"机械推导多花多少——C″ 实质是给那个推导补上"那 deploy 到底由谁触发才安全"的缺失环节，工程量增量 = 一个 deployd 常驻进程，但没给 Keith 精确量级感（属成本透明度不足，判断仍 C″ 胜出因为它是唯一同时兑现"push 即上线"+"不可信码零 prod 信任"两约束的形态）

### 如果 N 个月后证明决策错了，最可能的根因

- 形态 A（最可能）：deployd 的 GitLab API token 被证明权限过大或泄漏，攻击者改分支保护/越权——C″ 两道锚点（反查可信源 + 单向阀）同时失效，根因 = 把信任从"散落围栏"收敛到"一个 token + 一个 deployd"后，没在 v0 红队实测 token 边界，收敛点本身成软肋（C′ 形态 A 的同形态复发——bug-shape-survives-fix）。
- 形态 B：poll 慢被加 webhook 且 deployd 信了 webhook payload 的 sha——C″ 单向阀被短路，退回 C′ 警告的"信任外部传参 sha"。根因 = deployd 设计契约没把"事实输入只有主动 poll 两路、信号只能无参催查"焊成硬约束。
- 形态 C：roadmap 措辞没回写，下游按"deploy 在 CI"实现——信任边界焊回 PM 域，C″ 决了等于没决。根因 = 文档矛盾消解动作（行动建议 1）被当作"措辞润色"推迟，而它是 C″ 的承重落地点。

### 北极星触达

#3 决策超越直觉。直觉解在 Free 约束下是"那就尽量锁 PM 仓 ci.yml / 用 push rule + protected branch 硬扛"——继续猫鼠游戏。超越直觉处 = 识破"Free 锁不住 ci.yml 且 Keith 已弃 enforcement"意味着**不该再在'锁 PM 改不了什么'这个维度求解**，转而在"让 PM 能改的一切都不在部署决策的信任输入里"这个维度重构——CI 退化为纯转换器，部署决策函数的输入物理上 PM 够不到。同时识破召唤者收敛的"唯一问题"背后还藏着父会话机械推导收口与 roadmap 的文档级矛盾（deploy 移出 CI vs CI/CD 自动部署），C″ 正是那个缺失环节。并主动摊出 Keith 两条目标层约束间的隐含张力（配置层 vs 业务代码层攻击面）给一句话刻度而非掩盖——符合 Keith「诚实胜于体贴」+「决策符合 sense 甚至更完善」判据。

### essence 对齐自检（必填）

- **本决策跟哪几滴 essence 对位**（grep 物理命中）：
  - `execute-untrusted-code-never-holds-prod-trust`（2026-05-18，上轮本主线 append）—— C″ 是该 essence 在 Free 约束下的具体兑现：执行不可信代码的环境（runner build 阶段）零 prod 信任，部署决策权放在不可信侧物理够不到的裁决器（deployd），裁决器反查可信源（GitLab 权威分支 HEAD）而非信任不可信侧传参。本决策是该 essence 第二次产生承重应用，且把"裁决器反查可信源"从 C′ 抽象兑现到 Free 下可落地的 deployd poll 模型
  - `invariance-allocation`（2026-04-19）—— C″ 选"部署决策函数的信任输入"为不变量（PM 够不到的两个事实），触发层/CI 形态全是可换实现。直接推理依据
  - `physical-anchor`（2026-04-16）—— 信任边界靠物理判据（runner 零 key、出站防火墙、deployd 不读 PM 文件、registry path 写权）不靠 enforcement 配置；deployd token scope 未实证→标注交父会话红队实测
  - `ghost-rules`（2026-04-15）—— 契约 7.4「配置锁定」依赖 Free 下证伪的 Ultimate 特性，C″ 下 CI 无 deploy job 可覆盖→7.4 整条消解。砍掉一条防御不存在物的规则是正向应用
  - `tool-elevation-as-occam`（2026-05-06）—— C″ 把部署信任从散落的 CI/runner/key 收敛到单一可审计的 deployd，机制上提为单一裁决进程而非另造围栏
  - `task-compliance-is-not-truth` / `fallback-detectability`（2026-04-16 / 2026-05-06）—— inversion ③ 物理判据"触发信号不等于事实来源"（webhook/skill 只能催查、不能供 sha）直接由这两滴推出
  - `terminus-walk-needs-terminus-visibility`（2026-05-02）—— 张力节"零用户期≈零风险、回访触发点绑定"与单环境定调同源逻辑，承接此滴
- **本决策是否在某条 essence 上反着走**：潜在张力 `caged-freedom`（2026-04-26）——C″ 给 PM 比 C′ 更彻底的"够不到部署决策"边界。判定不构成反走：这是承重墙（选错塌主业务系统），笼子收紧的是"PM 够不到部署决策输入"这条本就该够不到的边界，PM 真实自由（写代码/push/部署自己 app/git push 即上线体验）零损。`ghost-rules` 警戒已主动跑过——C″ 防的是范式固有真实物理风险（持信任环境执行 AI 代码 + 部署决策读 PM 可控输入），非臆想灾难，通过警戒。
- **cross-check 用的关键词**（grep 物理证据）：`execute-untrusted-code-never-holds-prod-trust / invariance-allocation / physical-anchor / ghost-rules / tool-elevation-as-occam / task-compliance-is-not-truth / fallback-detectability / terminus-walk / caged-freedom`（均在 essence.md 全文 grep 命中）

### essence 候选（可选）

- slug: deploy-decision-must-not-read-untrusted-controllable-inputs
- 一句话: 部署决策函数的安全性不取决于"能不能锁住不可信方改配置"（enforcement 永远是猫鼠游戏，且常因 license/特性缺失根本锁不住），取决于"决策函数的事实输入里有没有任何一个是不可信方物理可写的"——把决策输入收敛到不可信方够不到的权威源（服务端状态反查 + 可信构建产物存在性），不可信方对配置的全部写权就自动失去意义，不需要锁它。
- 是否已 append 到 essence.md: Y（本轮 append——这是 `execute-untrusted-code-never-holds-prod-trust` 的下一层精化：上滴说"执行不可信码的环境不持 prod 信任"，本滴说"部署决策的判定函数不读不可信方可控的输入"，是同一根因在"决策函数输入端"而非"执行环境凭据端"的落点，越过 essence-degg-test：去掉 cgplatform 后"判定函数不读对手可写的输入"在任何信任边界设计上独立成立）

### 外部锚点

- `~/githubProject/cc-space/cgplatform/docs/roadmap.md` ← 行动建议 1：改部署引擎措辞 + 加 C″ 安全承诺边界刻度
- `~/githubProject/cc-space/threads/cgboiler-pm-sandbox.md` ← 时间线加 C″ 条目 + 契约 7.4/7.3 消解
- `~/githubProject/cc-space/cgplatform/integration-contract.md` §5 ← CI/部署接口改 registry digest + deployd poll
- `~/githubProject/cc-space/cgplatform/CLAUDE.md` ← 已收口决策 CICD 段改写
- `~/githubProject/cc-space/ssot/registry.md` ← deploy-bot@→deployd 凭据落点 + runner registry-push scope gate
- `~/githubProject/gg/memory/reflections/2026-05-18_cgplatform-deploy-trust-model.md` ← C′ 前序（本决策是其 Free 约束下的具体兑现）
- `~/githubProject/gg/memory/reflections/2026-05-19_cgplatform-cicd-form-decision.md` ← 形态 C 框架 + 红队未击败 1（本决策确证该假设为真并给出 Free 下解）
