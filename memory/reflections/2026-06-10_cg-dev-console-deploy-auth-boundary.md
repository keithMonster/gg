---
date: 2026-06-10
slug: cg-dev-console-deploy-auth-boundary
summoner: monster
northstar_reach: "#3 决策超越直觉（识破「工作台代跑」不是 cg-platform deployd 的同象限问题——信任轴从「被部署代码可信吗」翻到「执行进程被攻破时半径多大」）"
status: substantive-decision
---

# Reflection: cg-dev-console 部署执行层认证授权边界裁决

### 给父会话的最终输出（必填）

**总裁决：4 个待裁问题的承重内核 = 一句话——「工作台后端永不持有任何能直接落 prod 的凭据；它对 prod 的全部能力 = 向一个工作台够不到的旁路执行器投递一个『已被守门人签名的部署意图』，执行器自己反查 GitLab 权威分支 + 验签后才动手」。本轮合理终点 = test 真执行打通 + prod 全链路设计冻结但执行器 prod 侧不接线（与 16 把 key 冻结天然相容）。**

这是我 2026-05-19 给 cg-platform 拍的 C″（deployd 反查可信源 + 单向阀）在一个**不同象限**的兑现——不是照搬。换象限的三个物理事实必须先讲清，否则会照搬错。

---

**先纠一个会带偏整个设计的前提（最重要）：CG Notes 1.0 落的象限 ≠ cg-platform PM 应用象限。**

按我 2026-05-29 的双轴框架（信任边界 × 演化速度）：
- cg-platform PM 应用 = 象限②「**AI 生成代码** + 模板治理」→ C″ 信任模型的承重根是「被部署的代码不可信 → 部署决策不能信 PM 仓任何可写输入 → 反查 GitLab 权威分支 sha 防 PM 注入」。
- CG Notes 1.0 = 象限①「**Keith/团队写的可信代码** + 高频自改」→ 叶维政/欧强写的 Vue 前端**没有 prompt injection 攻击面**。C″ 那条「反查 sha 防 PM 改 ci.yml」的承重需求**在 1.0 这里不成立**——照搬就是 essence `ghost-rules` 警戒的「给可信代码套不可信代码的笼子」（我 5-29 已为此否决过「一个内核统一」）。

**那 1.0 的真攻击面是什么？换了维度**：不是「代码不可信」，是「**执行身份从 Keith 本人手敲 ssh，变成一个常驻后端进程代跑**」。攻击面 = 召唤 prompt 问题 3 说的「工作台后端被攻破时的爆炸半径」。这条**5-29 / 5-19 都没处理过**——之前的执行者要么是 CI runner（不可信，故清空凭据），要么是 deployd（可信进程，但部署的是不可信代码）。这里是**可信代码 + 一个新引入的、会暴露在 Web 请求面的执行进程**。所以 C″ 的「反查权威源」骨架复用，但承重点从「防被部署代码注入」平移到「防执行进程自身被攻破后越权落 prod」。

---

**问题 1（执行通道形态）——选「宿主侧旁路执行器拉取 / 验签」，否决「工作台后端直接 ssh 代跑」，也否决 CI runner 代跑（1.0 非容器化，CI 不适配）：**

候选淘汰逻辑：
- ❌ **工作台后端直接持 ssh key 代跑 deploy.sh**：这正是把「要 ssh key 才能部署 prod」降级成「攻破一个 Web 后端就能部署 prod」——brief 自己标的反例。工作台后端是有 HTTP 入口的常驻服务，攻击面比一台需要物理持 key 的笔记本大一个数量级。直接否。
- ❌ **CI runner 代跑（把执行外包给 GitLab CI）**：1.0 是「本地 build→tar→scp→远端解压」非容器化、无 registry、无镜像 digest——C″ 的「registry digest 作为可信构建产物存在性证据」这个反查锚点**物理不存在**。强行上 CI = 把 1.0 顺手容器化，这是 brief 阶段 2 的事，不该塞进认证设计这一轮（范围蔓延）。
- ✅ **宿主侧旁路执行器（命名 `cg-deploy-agent`）拉取式 + 验签**：在**部署目标可达域**（test 机；prod 侧本轮不接线）常驻一个小执行器，工作台后端**不持 ssh key**、只能向它投递一个「部署意图」。执行器拿到意图后做两件工作台够不到的事——① 反查 GitLab：`ref` 真的是该项目权威分支的 HEAD 吗（防工作台被攻破后投递任意 sha）② 验签：这个意图真的带着守门人的有效签名吗（见问题 3）。两者都过才 `git checkout <反查得到的 sha> && build && scp`。

**这是 C″ 的「调度器与被调方同可用性域 + 反查可信源 + 单向阀」三件套的 1.0 兑现**，差别只在反查的锚点：C″ 反查 `registry digest`（容器化），这里反查 `GitLab 分支 HEAD sha + 守门人签名`（非容器化 + 可信代码不需要防代码注入、但需要防执行进程越权）。

---

**问题 2（认证模型，test/prod 一体）——身份只在「投递意图」和「守门人签名」两处需要真实，执行器侧不认人只认签名：**

test/prod 一体的最小可信实现，按「谁触发 / 谁批准 / 谁执行」三角色拆：
- **谁触发**（test 自助 / prod 申请）：工作台用户身份。**MVP 单用户占位 `ACTOR='董超戈'` 必须先换成真实身份**，但不必自建账号体系——复用川锅已有认证标准（企微 / 帷幄 + cg-api `check-token`，即 cg-platform 契约 9 / `integration-contract.md §6` 那套，工作台作为 cg-platform 第 7 dogfood 本就该接这个，零新造）。test 环境：身份验证通过即可自助投递。
- **谁批准**（prod 守门人）：叶维政 / 欧强，任一人点即放行（Keith 已拍非会签）。批准动作的产物**不是数据库里一个 `approved_by='叶维政'` 字段**（那个工作台后端可以自己写，攻破即伪造）——而是一个**工作台后端无法伪造的签名**（见问题 3）。
- **谁执行**：`cg-deploy-agent`，**不认人、只认两个物理事实**（GitLab 反查 sha + 有效守门人签名）。它不读工作台数据库、不信工作台传来的 `approved_by`、不接受工作台传来的任意 sha。

**关键：test 和 prod 共享同一个执行器 + 同一套「反查 + 验签」框架，差别只在「prod 多一道守门人签名验证、test 不需要签名」。** 一体设计 = 一个执行器、一个意图 schema（带可选 `gatekeeper_signature` 字段），test 投递时该字段空、执行器对 test 跳过验签；prod 投递时必须有有效签名、执行器对 prod 强制验签。不为 test/prod 造两套通道。

---

**问题 3（审批→执行的不可伪造信任链，控爆炸半径）——这是本轮真正的承重墙，给具体机制：**

「任一守门人点了」这个事实如何不可伪造地传到执行器？分三档实现强度，**推荐档 2 作为本轮终点，档 3 留 tripwire**：

- **档 1（不够，会留洞）**：工作台后端记 `approved_by` 字段 + 执行器信工作台 API。→ 工作台后端被攻破即可自填 `approved_by='叶维政'` 调执行器。**信任链断在「执行器信任了一个可被攻破的进程」**——直接否，这等于没有信任链。
- **档 2（推荐，本轮终点）**：**守门人签名物理来自工作台后端够不到的地方**。最小可信实现 = 守门人审批走一个**独立的确认动作**，产出一个**带时效的签名令牌**，签名私钥**不在工作台后端进程内**（落在 `cg-deploy-agent` 宿主侧 / 或一个独立的轻量签名端，工作台只能拿到公钥验证形态、拿不到私钥伪造）。执行器用公钥验签 + 校验令牌绑定的 `(project, env, ref, 时效)`。工作台后端被攻破 → 攻击者能改 UI、能改 `approved_by` 显示字段、但**签不出执行器认的那个签名** → 投递的 prod 意图过不了执行器验签 → 爆炸半径被摁在「test 自助部署 + prod 申请记录」，碰不到 prod 真执行。

  最务实的档 2 落地（避免过度工程一个 PKI）：守门人确认动作 = **守门人在自己侧用一个工作台后端访问不到的密钥**对意图摘要签名（可以朴素到「守门人持一个 HMAC 密钥 / 一个 GitLab 个人 token 对 MR 做一个 approve 动作，执行器反查 GitLab MR 的 approve 状态」）。**最优雅的一种 = 复用 GitLab 自己的 MR approval 作为签名源**：prod 部署的前置 = 该 ref 对应的 MR 已被叶维政或欧强在 GitLab 上 approve；执行器用自己的 read token 反查 GitLab API「这个 MR 被这两个 user_id 之一 approve 了吗」。**GitLab 的 approve 记录工作台后端改不了**（它在 GitLab 服务端，不在工作台库里）——这就把「守门人签名」物理外移到了 GitLab，零新造签名基建，且天然对齐 brief 的「MR + 部署一起建」。⚠️ 待核：GitLab Free 是否支持 MR approval rules（社区版可能阉割，需父会话物理核 `gitlab.cgboiler.com` 版本/特性）；不支持则降级到 HMAC 独立签名端。

- **档 3（tripwire，本轮不做）**：完整签名服务 + 审计链 + 令牌吊销。触发条件 = 工作台扩到管 ≥3 个 prod 仓 / 或第一次出现「守门人不在场需要代签」需求。现在做 = premature。

---

**问题 4（与 prod 冻结的相容性，本轮合理终点）——「全设计、test 真执行、prod 不接线」：**

16 把 prod key 不动 + 「正式环境的东西一律不碰」的约束，跟我推荐的形态**天然相容**，因为：
- `cg-deploy-agent` 是**新增的旁路进程**，不碰那 16 把 key、不碰现有 `root@42.193.55.173` 的任何配置。它本轮**只在 test 机 `cg@10.13.1.61` 接线并真执行**。
- prod 侧：执行器的 prod target **设计完整冻结**（意图 schema 带 prod、验签逻辑写好、GitLab approval 反查写好），但**执行器在 prod 宿主上不部署、不持 prod 落地能力**——`registry.json` 的 `prod.enabled=false` 闸门**保持现状不动**，与现在代码完全一致。
- **本轮合理终点的精确刻度**：① test 端到端真跑通（投递意图 → 执行器反查 GitLab → build → scp → test 机落地 → 审计）② prod 全链路（含守门人 GitLab approval 验签）**设计冻结在文档 + 代码 interface 层**，执行器 prod 侧**物理不接线**。这样既验证了「不持凭据 + 反查 + 验签」信任模型在 test 上真成立（不是纸面），又一行没碰 prod。**收 16 把 key 是另一轮的事**（Keith 已拍「不动」）——工作台 prod 通道做完设计冻结后，将来收 key 时它是现成的替代通道，但本轮不收、不开闸。

---

**给父会话的行动序（落地切法，4 阶段）：**

1. **立刻（本轮认证设计的代码落点）**：① 把 `DeployService` 的 `ACTOR='董超戈'` 占位换成真实身份——接 cg-platform 契约 9 认证标准（企微/帷幄 + cg-api check-token），不自建账号。② 在 `deploy.types.ts` 扩 `DeploymentProvider` 接口，新增 `execute` 方法签名 + 一个 `DeployIntent` 类型（带 `project/env/ref/gatekeeperApprovalRef?` 字段），但 `ChecklistProvider` 不实现 execute——execute 由新的 `AgentRelayProvider` 实现（只负责「向 cg-deploy-agent 投递意图」，不持 ssh）。
2. **阶段 0a（test 真执行打通）**：在 `cg@10.13.1.61` 部署 `cg-deploy-agent`（小常驻进程：收意图 → GitLab 反查 ref→sha → checkout+build+scp 到 test workdir → 回传日志 → 审计）。工作台 `test.enabled` 翻 true。**test 不需要守门人签名**，身份验证通过即自助。
3. **阶段 0b（prod 链路设计冻结，不接线）**：执行器 prod 验签逻辑（GitLab MR approval 反查 = 叶维政/欧强任一 approve）写完、`DeployIntent.gatekeeperApprovalRef` 字段定义完、prod target 配置完，但 `prod.enabled` **保持 false**、执行器 prod 宿主**不部署**。先物理核 `gitlab.cgboiler.com` 是否支持 MR approval rules——支持则用它当签名源，不支持降级 HMAC 独立签名端。
4. **tripwire（不现在做）**：① 完整签名服务（触发 = 管 ≥3 prod 仓 / 代签需求）② 1.0 容器化迁 CI（触发 = brief 阶段 2，与本认证轮解耦）③ 收 16 把 prod key（触发 = Keith 另拍，工作台 prod 通道届时已是现成替代）。

**可逆性**：test 执行器 = 完全可逆（新增旁路进程，删了就回到现状）。prod 设计冻结不接线 = 零不可逆动作（一行没碰 prod）。唯一需要 Keith 拍的不可逆参数 = 将来开 prod 闸（`prod.enabled=true`）那一刻——本轮不发生。**置信度 4/5**，扣 1 因 GitLab Free 是否支持 MR approval rules 未物理核（决定档 2 用 GitLab approval 还是降级 HMAC，是实现分支不是方向分支，方向不受影响）。

### 核心假设

- **CG Notes 1.0 是团队可信代码、无 AI 自由生成成分** —— 基于 brief「叶维政单人→四五人维护的 Vue3 前端」+ 1.0 不在 cg-platform PM 应用集合内推断。若将来 1.0 引入 AI 自由生成代码，轴 A 会把它推向 C″ 的「防代码注入」承重，框架仍吸收（双轴本身吸收迁移），但本轮按可信代码裁。
- **`cg@10.13.1.61` test 机可常驻一个执行器进程且工作台后端对它只有「投递意图」一个入口、无 ssh/shell 入口** —— 基于 cc-gateway/huasheng cron / cg-platform deployd 同范式既有实证推断，未实测 test 机当前 cg@ 账号权限边界。
- **GitLab approval 记录工作台后端无法伪造** —— 成立前提 = 执行器用自己的、工作台够不到的 read token 反查 GitLab API，且 GitLab Free 支持 MR approval（**未物理核 `gitlab.cgboiler.com` 版本/特性，最关键未核项**）。不支持则整个档 2「签名源」降级到 HMAC 独立签名端，承重内核（签名物理在工作台够不到处）不变。
- **prod 16 把 key 冻结期间，工作台 prod 通道「设计冻结不接线」是 Keith 接受的本轮终点** —— 基于 Keith 拍「不动 + 正式环境一律不碰」+ 范围「先只管 1.0」推断。

### 可能出错的地方

- **最高：GitLab Free 不支持 MR approval rules**（社区版常阉割 approval）。→ 档 2 的「最优雅落地（复用 GitLab approve 当签名源）」塌，必须降级 HMAC/独立签名端，工程量增一个轻量签名端。这是实现分支，方向（签名物理外移出工作台进程）不塌。父会话**必须先核这一项再进详细设计**。
- **次高：把「test 执行器」做着做着顺手把 prod 也接了线** —— 「都设计好了，开个闸而已」的工程冲动会侵蚀 prod 冻结约束。防御 = `prod.enabled` 翻 true 是 Keith 显式拍的不可逆动作（problem 4 已钉），执行器代码里 prod 落地路径用一个「需 Keith 在执行器宿主侧手动置位的 flag」物理隔离，不是工作台能翻的配置。
- **中：执行器自身成为新单点信任汇聚（它持 GitLab read token + test 落地能力 + 将来 prod 落地能力）** —— 同 C″ deployd 的固有风险。`<project>/<ref>` 必须套 userid.py 同款硬白名单防注入（v0 脚本就要有），token 落点 chmod 600 禁进任何 Web 可达进程。

### 本次哪里思考得不够

- 没物理核 `gitlab.cgboiler.com` 的 GitLab 版本与 MR approval 特性支持 —— 这是档 2 最优雅落地成立的前提，标为父会话进详细设计前必核项，没核就先按「方向定、签名源实现二选一待核」交付。
- 没读 1.0 的 `deploy.sh` 实际源码（只从 `checklist.provider.ts` 的 dryRun 命令预览推断它是 build→tar→scp→解压）—— 执行器要「受控复跑 deploy.sh」，deploy.sh 内部是否有交互式确认 / 是否硬编码了某些只在叶维政笔记本上成立的路径，未核。属实现期细节，不影响认证边界方向。
- 执行器的运行时细节（投递队列 / 并发去重 / 失败重试 / 日志回传协议）只给了骨架，与 C″ deployd 同样把这些留给实现期 —— 方向已定，运行时设计点待落地会话补。

### 如果 N 个月后证明决策错了，最可能的根因

- **形态 A（最可能）：执行器的 GitLab read token 或 test 落地能力被证明权限过大/泄漏** —— 信任从「16 把散落 key」收敛到「一个执行器 + 一个 token」后，收敛点本身成软肋，且 v0 没红队实测 token 边界（C″ deployd 形态 A 的同形态复发——`bug-shape-survives-fix`）。缓解全压 v0 红队实测 + 落点 chmod 600 + `<project>/<ref>` 硬白名单。
- **形态 B：档 2 降级 HMAC 后，HMAC 密钥被偷偷塞进工作台后端能读到的地方**（图省事），签名物理外移的承重内核被悄悄焊回工作台域 —— 等于信任链断了但没人察觉（`fallback-detectability`：降级路径的失败不可见）。根因 = 降级实现时没守住「签名私钥物理不在工作台进程可达域」这条硬约束。
- **形态 C：1.0 被容器化迁 CI 时，有人把本轮的「执行器反查 GitLab sha」简化成「信 CI 传来的 sha」** —— 退回我 C″ 反复警告的「信任不可信侧传参」失败形态（`deploy-decision-must-not-read-untrusted-controllable-inputs`）。根因 = 阶段 2 容器化时把认证轮的承重内核当「旧实现」丢弃。

### 北极星触达

#3 决策超越直觉。直觉解 = 顺着「cg-platform 已有 deployd 信任模型，照搬 C″ 即可」（召唤 prompt 自己说「有现成设计可复用」）。超越直觉处 = 识破 CG Notes 1.0 落的是**不同象限**——它是可信代码（C″ 反查 sha 防代码注入的承重需求不成立），但引入了一个 C″/5-29 都没处理过的新维度「执行身份从人手敲变成常驻进程代跑」。照搬 C″ 会犯两个反向错：① 给可信代码套防注入笼子（`ghost-rules`）② 漏掉真攻击面（执行进程被攻破半径）。正确动作是复用 C″ 的**骨架**（反查可信源 + 单向阀 + 调度器同可用性域），但把承重点平移、把反查锚点从 registry digest 换成 GitLab 分支 HEAD + 守门人签名。

### essence 对齐自检（必填）

- **本决策跟哪几滴 essence 对位**（grep 物理命中）：
  - `execute-untrusted-code-never-holds-prod-trust`（2026-05-18）—— 骨架根：执行环境与 prod 信任物理分离。本轮**反向应用**——这里被部署的代码可信，但「会被攻破的 Web 后端」充当了「不可信执行环境」的角色，故工作台后端不持 prod 信任，等价于 runner 不持 prod 信任。
  - `deploy-decision-must-not-read-untrusted-controllable-inputs`（2026-05-19）—— 直接落点：执行器的部署决策输入（GitLab 权威分支 HEAD + 守门人签名）必须是工作台后端物理够不到的；工作台传的 `ref`/`approved_by` 全在执行器信任输入之外。
  - `deploy-paradigm-axis-is-trust-not-dependency`（2026-05-29 reflection 候选，未沉淀 essence 但在 reflection 锚定）+ 我 5-29 的双轴框架 —— 识破 1.0 落象限①而非②，是整个裁决的换轴起点。
  - `ghost-rules`（2026-04-15）—— 否决「照搬 C″ 反 sha 注入」：给可信代码套防 PM 代码注入的笼子 = 为不存在的攻击面加防御。
  - `invariance-allocation`（2026-04-19）—— 选「工作台后端不持任何 prod 直达凭据」为不变量，执行通道/签名源是可换实现。
  - `physical-anchor`（2026-04-16）—— 信任边界靠物理判据（执行器持私钥/工作台只持公钥、GitLab approval 在服务端、token chmod 600）不靠 enforcement；GitLab Free approval 支持未核→标注交父会话核。
  - `tool-elevation-as-occam`（2026-05-06）—— 信任收敛到单一可审计执行器；签名源复用 GitLab 已有 approval 而非新造 PKI。
  - `fallback-detectability`（2026-05-06）—— 形态 B 根因预判：HMAC 降级路径若把密钥塞回工作台域，失败不可见。
  - `terminus-walk-needs-terminus-visibility`（2026-05-02）—— prod「设计冻结不接线」与 cg-platform 单环境「零用户≈零风险、回访点绑定」同源逻辑。
- **本决策是否在某条 essence 上反着走**：潜在张力 `caged-freedom`（2026-04-26）—— 给执行通道加「不持凭据 + 验签」约束是否过度？判定不构成反走：这是承重墙（认证有洞→prod 暴露难回退），收紧的是「工作台后端够不到 prod 直达能力」这条本就该够不到的边界，团队真实自由（页面点部署、test 自助、prod 申请体验）零损，且 prod 本轮不接线一行没碰。`ghost-rules` 警戒已主动跑——防的是「常驻 Web 进程持 prod 凭据」的真实物理风险，非臆想。另一条主动核的张力：本轮我**没有**照搬 C″ 全套（反 sha 注入那条砍了），这是对 `paradigm-not-feature-completeness` 的正向遵守（功能覆盖 100% 照搬 = 范式错配），不是偷工。
- **cross-check 用的关键词**（grep 物理证据）：`execute-untrusted-code-never-holds-prod-trust / deploy-decision-must-not-read-untrusted / ghost-rules / invariance-allocation / physical-anchor / tool-elevation-as-occam / fallback-detectability / terminus-walk / caged-freedom / paradigm-not-feature-completeness`（均在 essence.md 全文 grep 命中）

### essence 候选（可选）

- slug: web-facing-executor-is-untrusted-regardless-of-payload-trust
- 一句话: 一个会暴露在请求面的常驻执行进程，无论它部署的代码可信不可信，自身都要按「不可信执行环境」对待——「被部署代码是否可信」决定要不要防代码注入（反 sha），「执行进程是否会被攻破」决定要不要不持直达凭据 + 反查 + 验签，这是两条正交的攻击面，可信代码也需要后者。
- 是否已 append 到 essence.md: N（本轮**不沉淀**——这是 `execute-untrusted-code-never-holds-prod-trust` + `deploy-decision-must-not-read-untrusted-controllable-inputs` 在「执行者是 Web 进程而非 CI runner」场景的合并应用，承重内核「会被攻破的环境不持 prod 信任」已被前两滴覆盖，本场新增的只是「把『不可信执行环境』的外延从 CI runner 扩到 Web 后端」——是外延扩展不是新机制。按 essence-application-needs-precondition-recheck 自己的纪律，未越过 essence-degg-test 的「去 cgboiler 后独立成立的新重量」门槛，强行沉淀违反 `bug-shape-survives-fix` 警戒的同形态复犯。若将来出现第三个「可信代码 + 不可信执行进程」独立场景仍需此判据，届时再沉淀。）

### 外部锚点

- `~/githubProject/monster/inbox/briefs/dev-console.md` ← 行动建议落「部署执行层认证设计」新章节（父会话要的设计结论摘要）
- `~/githubProject/monster/threads/dev-console.md` ← 时间线加 2026-06-10 gg 部署认证裁决条目
- `~/CGProject/cg-dev-console/server/src/deploy/` ← 行动序 1：扩 DeploymentProvider 接口 + 换 ACTOR 占位 + 新 AgentRelayProvider；execute 闸门暂留
- `~/CGProject/cg-dev-console/server/src/registry/projects.ts` ← test.enabled 翻 true（阶段 0a 后）；prod.enabled 保持 false
- `~/githubProject/gg/memory/reflections/2026-05-19_cgplatform-free-tier-deploy-trust-boundary.md` ← C″ 骨架前序（本决策是其在象限① + 非容器化的换锚点兑现）
- `~/githubProject/gg/memory/reflections/2026-05-29_cg-deploy-unification-architecture.md` ← 双轴框架（识破 1.0 落象限①的起点）
- `~/githubProject/monster/cg-platform/docs/pm-paas-platform.md` ← 沙箱契约 3（deploy 权限边界，本决策复用其「执行身份独立账号 + 反查可信源」骨架）
