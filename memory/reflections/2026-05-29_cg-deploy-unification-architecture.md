---
date: 2026-05-29
slug: cg-deploy-unification-architecture
summoner: monster
northstar_reach: "#3 决策超越直觉（统一 ≠ 一套打天下；切分维度从「依赖拓扑」纠到「信任 + 演化速度」双轴）"
status: substantive-decision
---

# Reflection: 川锅 CG 系统部署方式统一架构裁决

### 给父会话的最终输出（必填）

**总裁决：召唤者的「分层 + 收敛 + 清债」骨架方向对，但切分维度选错了——换轴后 4 个决策点的答案有 3 个变。**

**核心纠正：分层维度从「基础服务层 vs 业务应用层（论据=循环依赖）」纠正为「信任边界 ×  演化速度」双轴。**循环依赖不是真问题（见下），它是个被误判为承重墙的隔断。

---

**决策点 1（分层框架）——推翻召唤者切法，换双轴：**

召唤者的「基础服务层 vs 业务应用层」二分，主论据「PM 应用调 cg-proxy 做认证 → 塞进 C 有循环依赖味」**站不住**：
- C（cg-platform-deploy.sh）是**部署执行器**，cg-proxy 是**运行时被调服务**——两者在不同层。cg-meetos 已经既"被 C 部署"又"运行时调 cg-proxy 认证"，**没有任何循环**。把 cg-proxy 用 C 部署，只是"C 这个部署工具去部署 cg-proxy 这个服务"，跟 cg-proxy 运行时被谁调用完全正交（`metric-vs-pattern`：召唤者把"运行时调用拓扑"和"部署工具选型"两个不同抽象层黏在一起了）。
- 真正决定一个项目走哪个部署范式的，是**两条正交轴**：
  - **轴 A 信任边界**：代码由谁写、谁运行。`AI 生成 + AI 运行`（PM 应用）vs `Keith/团队写 + 受控运行`（cg-proxy/cc-gateway 等基座）。这条轴决定**部署器要不要 C 的"不信任传参 + GitLab 反查 sha"信任模型**（我 2026-05-18/19 裁决 C′ 的承重内核，essence `execute-untrusted-code-never-holds-prod-trust` + `deploy-decision-must-not-read-untrusted-controllable-inputs`）。
  - **轴 B 演化速度 / 拥有者**：Keith 高频自改、需快速迭代的（基座）vs 模板化、PM 自助产出、需强约束的（PM 应用）。这条轴决定**要不要 registry 白名单 + 派生物强约束 + PM 二次确认那套"模板化治理"**。
- **双轴交叉出 4 象限，真实项目落 3 个**：
  - 象限①「可信代码 + 高频自改」= cg-proxy/cg-api/cc-gateway/wflow-api（**基座**）→ 不需要 C 的信任模型（代码可信，不必反查 sha 防注入），但**值得统一 deploy 内核**（消除手敲 + 参数顺序混乱）。
  - 象限②「AI 代码 + 模板治理」= PM 应用（cg-meetos 等）→ 必须 C 全套（信任模型 + registry + 派生物约束）。
  - 象限③「可信代码 + 低频/静态」= 纯静态前端（cg-manage 等 B）→ 既不需要信任模型也不需要模板治理，**保持 B 不动是对的**（强行套 C 是过度工程，cgx 走 C 是因为它本就是 PM 自助产出的无 DB 应用，不构成"静态站都该走 C"）。
- **结论**：召唤者把"基座 vs 应用"切对了边界线的**位置**（哪些项目归一组），但切错了**维度的名字和论据**——真维度是信任 + 演化速度，不是依赖方向。换轴后边界线落点几乎一致（基座一组、PM 应用一组、静态一组），但**决策点 2/3 的答案因此改变**。

**决策点 2（是否统一 deploy 底座）——部分采纳，但按轴 A 切两个内核，不是一个：**

召唤者问"把 C 信任模型下沉成所有 Docker 后端（A+C）共享内核"。**否决"一个内核"，定"两个内核 + 一个共享脚手架库"**：
- C 的信任模型内核（GitLab 反查 sha 不信任传参 + 私钥物理隔离 + deploy stage 平台锁定）是**为"不可信代码"设计的**。把它强加给基座（cg-proxy 等可信代码）= 用 essence `ghost-rules` 警戒的"为不存在的风险加防御"——基座代码 Keith 自己写，没有 prompt injection 攻击面，反查 sha 防的是 PM 改 ci.yml，基座没有 PM。**强行统一信任模型 = 给基座套 PM 应用的笼子，是错的统一**（`paradigm-not-feature-completeness`：范式错配下功能覆盖 100% 也是错的）。
- 但召唤者点出的**真痛点是对的**：A 手敲 deploy.sh + 参数顺序不统一（cg-proxy `env branch` vs cg-api 反着 `branch env`）是真摩擦，值得消除。**这个痛点的解不是"统一信任模型"，是"统一脚手架库 + 统一参数契约"**——把蓝绿/健康检查/flock/失败日志/TZ/nexus 代理这些**与信任模型正交的机械动作**抽成共享库（`tool-elevation-as-occam`：第二个消费者出现时上提到共享层），A 和 C 都引用同一个机械库，但**信任层各保各的**（A 不要 sha 反查，C 要）。
- **落地形态**：`shared/deploy-lib/`（机械层：蓝绿函数 + 健康检查 + flock + 失败 dump + 统一 `deploy.sh <env> [branch]` 参数序）→ A 类项目逐步收敛参数序到这个契约（cg-api 那个反着的参数序是纯 bug，该修）；C 在机械库之上叠自己的信任层（sha 反查 + 白名单）。**净效果**：消除手敲摩擦（采纳召唤者诉求）+ 不把信任模型错配给基座（纠正召唤者方案）。

**决策点 3（registry.json 是否升格全川锅资产账本）——否决升格，定"两本账分治"：**

这是我 essence `runtime-state-vs-business-data-distinct-ssot-domains` 的直接落点（虽然那滴讲 runtime vs business data，同构在这里是"治理账本 vs 资产清单"）：
- cg-platform 的 `registry.json` 是**强约束治理账本**——它的字段（白名单 / 派生物规则 / table_modes / pm_user_id / 二次确认占位）全部服务于"AI 生成应用的强约束治理"。把 A/B/D 项目塞进来 = 这些项目根本不需要 table_modes / pm 二次确认 / 派生物约束，**塞进来会反向稀释 registry.json 的语义判别力**（那滴 essence 的原话：runtime state 塞进 business data SSOT 反向稀释判别力）。
- A/B/D 需要的是**资产清单**（哪个项目、哪台机、什么域名、什么部署脚本）——这正是 DEPLOYMENT.md §3 项目矩阵在做的事，它是手维护的轻量清单，**职能正确**。
- **结论**：保持 registry.json = cg-platform 专属治理账本；DEPLOYMENT.md §3 = 全川锅资产清单。**两本账，不同辖域，不合并**。升格的合法触发不存在（`tool-elevation-as-occam` 反向：升格的不合法触发 = 形式同构"看起来都是部署资产"，但治理需求量级完全不同）。
- 唯一可加的轻量改进：A 类项目若也想要"部署事实物理证据层"（C 的 CI exit code 审计价值），可以在引入共享 deploy-lib 时顺带产 deploy log，但**不进 registry.json**，进各项目自己的 `/tmp/<svc>-deploy-<ts>.log`（DEPLOYMENT.md §4.4 已有此机制）。

**决策点 4（优先级 + 触发条件）——这是 ROI 题，定"钉范式 + 改 cg-api bug + 不做深度统一"：**

这是本次最容易被工程冲动带跑的决策点。我用 essence `engineering-impulse-as-load-bearing-disguise`（工程冲动的高级伪装 = 调研一致 + 方案工整 + 对齐表全 ack）+ `premature-abstraction-tripwire`（留 tripwire 不抽象）+ `cadence-as-symptom`（先问真痛点频率）来卡：
- **现在值得做的（低成本 + 真痛点）**：
  1. **钉死新项目默认范式**（零成本，纯文档）：新 PM 应用 → C；新基座后端 → A 进化版；新静态站 → B；**不再产生 E/F 新实例**。这是把"范式选择"从每次决策提前到一次性钉死，`project-naming-as-frame-allocation` 同源——定了默认，下游不再每次纠结。
  2. **修 cg-api deploy.sh 参数顺序 bug**（半小时）：这是真 bug 不是范式分歧，`env branch` 统一掉，避免下次踩。
- **现在不值得做的（高成本 + 痛点未达频率）**：
  3. **抽 `shared/deploy-lib/` 共享机械库**：方向对，但**当前 A 类项目稳定运行、手敲摩擦低频**（Keith 超个体，部署基座是偶发动作不是高频）。按 `premature-abstraction-tripwire` 留 tripwire：**触发条件 = 出现第 3 个新基座后端需要从零写 deploy.sh 时**（前两个=已有的抄，第三个=证明这是重复劳动）→ 那时再抽库。现在抽 = 给 5 个稳定项目做重构，ROI 为负。
  4. **存量 A/B 强迁统一**：不做。稳定的不动（`reversibility-not-permission`：它们没有"选错会塌"的承重风险，是隔断不是承重墙）。
- **存量清债（按 cost-benefit 各自判，不打包）**：
  - **E（pm2 非容器化）**：召唤者说"真债该淘汰"——**我降级为"不主动淘汰，触发式迁移"**。pm2 的 cg-monitor 等在 ft@10.13.1.29 跑着没出事 = 它的"无版本管理"债没真咬人。`theory-gap-without-data`：没有"它出过事"的数据就主动淘汰 = 凭理论判债。触发 = 它下次需要改动/出故障时，顺手迁 Docker。
  - **D（哈轴）**：召唤者说"补凭据管理"——**采纳但定为独立优先级**。哈轴"凭据进 git + GIT_BRANCH 漏设静默写错租户"是**真安全风险**（不是理论债，是 essence `security-claim-as-physical-fact` 域的真问题），这条**优先级高于 deploy-lib 抽象**，因为它是"选错真会塌"（写错租户=生产事故）。但它独立于本次统一框架（哈轴是平行租户，不进 A/B/C 任何一类），单独走一轮 fix。
  - **F（一次性脚本 dataease 等）**：不动。一次性产物，本就不该进范式体系（monster `output/` vs 入库的边界同理）。

---

**一句话行动序**（给父会话）：
1. 立刻（零成本）：钉死新项目默认范式表（C/A/B 三选一 + 禁 E/F 新实例），写进 DEPLOYMENT.md §6 开头。
2. 立刻（半小时）：修 cg-api deploy.sh 参数顺序 bug 对齐 `<env> [branch]`。
3. 排期（独立高优）：哈轴 D 凭据管理 fix（真安全风险，单独一轮，不并入本框架）。
4. 留 tripwire（不现在做）：`shared/deploy-lib/` 共享机械库——触发=第 3 个新基座后端从零写 deploy.sh。
5. 不做：存量 A/B 强迁 / E 主动淘汰 / registry.json 升格 / 统一信任模型内核。

### 核心假设

- cg-meetos 当前确实"既被 C 部署、又运行时调 cg-proxy 认证"且无循环——基于 integration-contract §6（契约 9 候选，应用调 cg-api check-token）+ cg-meetos 已上线推断，未逐行核 cg-meetos runtime 是否真调 cg-proxy（contract §6 是候选 ⏳，cg-meetos 实际可能尚未接认证）。但循环依赖论据的证伪不依赖这一点——即便它调，部署工具选型与运行时调用拓扑仍正交。
- A 类项目（cg-proxy 等）代码是"Keith/团队可信编写"——基于 DEPLOYMENT.md §3.1 + 这些是川锅核心服务推断。若将来某基座后端也开始让 AI 自由生成代码，轴 A 会把它推向 C 信任模型，框架仍成立（轴本身吸收这种迁移）。
- cg-api deploy.sh 参数顺序"反着"是 bug 而非有意设计——基于 DEPLOYMENT.md §3.1 明确标注"⚠️ 参数顺序与 cg-proxy 反着"推断，未读 cg-api deploy.sh 源码确认是否有不可改的历史原因。

### 可能出错的地方

- 最高风险：把"双轴框架"本身做成了一个比召唤者方案更复杂的抽象，违反 OCCAM——若 Keith 读完觉得"我就想要一句话该怎么部署"，那双轴是过度分析。缓解=最终行动序压到 5 条可执行项，框架只是论证骨架不是交付物。
- 次高：cg-api 参数序"反着"可能有我没读到的历史原因（某个调用方依赖旧序），改它可能辐射破坏——必须 grep 调用方再改，不能直接动（monster Engineering Rules #7）。
- 中：deploy-lib tripwire 设的触发"第 3 个新基座后端"可能永远不来（Keith 超个体，新基座低频），等于这个抽象永久 park——这正是 tripwire 的正确行为（不来就不抽），不是 bug。

### 本次哪里思考得不够

- 没物理核验 E（pm2）当前到底跑了哪些服务、是否真有"无版本管理咬人"的历史事故——降级"不主动淘汰"是基于 theory-gap-without-data 的保守判断，但若 Keith 知道 pm2 实际出过事，该判断要翻（交父会话/Keith 补这个事实）。
- 哈轴 D 的"凭据进 git + GIT_BRANCH 漏设"风险，我标为"真安全风险高优"，但没展开 fix 形态（凭据移出 git 走 env-file？GIT_BRANCH 加 fail-loud 校验？）——只给了优先级判断，具体方案需另一轮（HZ_DEPLOYMENT.md 是独立 SSOT）。
- 没核 `shared/deploy-lib/` 抽象的真实工作量——判"现在 ROI 为负"基于"5 个稳定项目重构成本 > 收益"的直觉，未量化。但 tripwire 范式的好处恰是不需要现在量化（触发了再算）。

### 如果 N 个月后证明决策错了，最可能的根因

- 形态 A（最可能）：deploy-lib tripwire 设太高，A 类项目手敲摩擦其实比我估的高频，Keith 反复踩参数序/蓝绿细节的坑累积成本 > 早抽库成本——根因=我把"超个体=低频部署"的画像当成了"基座部署低频"，但 cg-platform 长大后基座迭代可能变频繁。
- 形态 B：双轴框架虽然论证更正确，但 Keith 落地时发现"信息上还是按基座/应用两组在想"，双轴的"信任×演化速度"在脑子里坍缩回召唤者的二分——说明我纠正的是论据不是结论，框架的增量价值没兑现（`survey-as-coordinate`：差名字≠差能力的反向，我可能在给一个已对的结论换更贵的名字）。
- 形态 C：哈轴 D 凭据风险被"独立排期"事实上无限推迟（独立=没人管），某天真写错租户出生产事故——根因=我把它从框架里摘出来标"独立高优"，但"独立"在 Keith 单人系统里等于"没有 owner 的 backlog"。

### 北极星触达

#3 决策超越直觉。直觉解 = 顺着召唤者的"基础服务层 vs 业务应用层"确认框架（它听起来很对、循环依赖论据很专业、对齐表能全 ack）。超越直觉处 = 识破"循环依赖"是 metric-vs-pattern 层混淆（部署工具选型 ⊥ 运行时调用拓扑），换出"信任边界 × 演化速度"双轴——边界线落点几乎一致，但**决策点 2 因此从"统一一个内核"翻成"两内核+共享机械库"、决策点 3 从可能升格翻成明确否决**。这正是 essence `engineering-impulse-as-load-bearing-disguise` 的活体应用：召唤者方案的"内部一致性"（分层+收敛+清债三段工整）恰是工程冲动的伪装，识别只能靠对照本地已验证 essence（runtime-state-vs-business-data / execute-untrusted-code / ghost-rules），不能靠方案内部一致性。

### essence 对齐自检（必填）

- **本决策跟哪几滴 essence 对位**（grep 物理命中）：
  - `runtime-state-vs-business-data-distinct-ssot-domains` (2026-05-20) — 决策点 3 直接落点：registry.json 治理账本 vs DEPLOYMENT 资产清单是不同辖域，塞一起反向稀释判别力。同构迁移（runtime/business → 治理/资产），已在"可能出错"承认非原域。
  - `execute-untrusted-code-never-holds-prod-trust` (2026-05-18) — 轴 A 信任边界的承重根：决定 PM 应用必须 C 信任模型、基座不必。本决策是我自己那滴的反向应用（不只"AI 代码要 C"，更是"可信代码不该被 C 笼子套"）。
  - `deploy-decision-must-not-read-untrusted-controllable-inputs` (2026-05-19) — C 信任模型内核的精确定义，决策点 2 区分"哪些项目需要 sha 反查"的判据。
  - `paradigm-not-feature-completeness` (2026-05-14) — 决策点 2 否决"一个内核"的承重：把 C 信任模型加给基座 = 范式错配，覆盖率 100% 也错。
  - `tool-elevation-as-occam` (2026-05-06) — 双面用：正面支持抽 deploy-lib（第二消费者上提机械层）；反面卡 registry 升格（形式同构非合法上提触发）。
  - `metric-vs-pattern` (2026-04-19) — 识破召唤者"循环依赖"论据是抽象层混淆（运行时拓扑 metric ⊥ 部署工具 pattern）。
  - `engineering-impulse-as-load-bearing-disguise` (2026-05-28) — 决策点 4 防工程冲动的核心判据：方案内部一致性是伪装本身，靠本地 essence 对照识别。
  - `premature-abstraction-tripwire` (2026-04-21) — 决策点 4 deploy-lib 留 tripwire 不现在抽。
  - `cadence-as-symptom` (2026-05-06) — 决策点 4 先问"基座部署真高频吗"再判要不要抽库。
  - `theory-gap-without-data` (2026-05-06) — E（pm2）降级"不主动淘汰"：没"出过事"数据就淘汰=凭理论判债。
  - `ghost-rules` (2026-04-15) — 决策点 2 否决给基座套信任模型=为不存在的风险（基座无 PM 注入面）加防御。
  - `reversibility-not-permission` (2026-05-06) — 存量 A/B 不强迁：它们是隔断（改得起）不是承重墙（选错塌）。
- **本决策是否在某条 essence 上反着走**：潜在张力 `ontology-expansion-velocity-needs-cap`（扩展节奏封顶）——我引入"双轴框架"是不是新增一层认知结构？判定不构成违反：双轴不是新本体论层，是把召唤者已有的"分层"维度**纠正命名**（依赖方向→信任×演化），元素数量不增反降（召唤者 6 范式归 3 类，我归 3 象限+明确不做项，没加新桶）。`survey-as-coordinate` 警戒已跑：双轴是坐标不是清单，且边界落点与召唤者一致，差的是论据正确性不是结论。
- **cross-check 用的关键词**：`runtime-state-vs-business-data / execute-untrusted-code / deploy-decision-must-not-read-untrusted / paradigm-not-feature-completeness / tool-elevation-as-occam / metric-vs-pattern / engineering-impulse-as-load-bearing-disguise / premature-abstraction-tripwire / cadence-as-symptom / theory-gap-without-data / ghost-rules / reversibility-not-permission / ontology-expansion-velocity / survey-as-coordinate`（均在 essence.md 全文 grep 命中）

### essence 候选（可选）

- slug: deploy-paradigm-axis-is-trust-not-dependency
- 一句话: 部署范式分层的正确轴是"代码信任边界 × 演化速度/拥有者"，不是"运行时依赖拓扑"——"A 调 B 所以 A 不能用 B 的部署工具"是把运行时调用拓扑（metric）和部署工具选型（pattern）黏在一起的 level confusion；部署工具部署谁，与被部署者运行时被谁调，正交。
- 是否已 append 到 essence.md: N（本次不沉淀——这是 `metric-vs-pattern` + `execute-untrusted-code` 在"部署分层"场景的合并应用，"循环依赖论据站不住因为抽象层混淆"是 metric-vs-pattern 的直接推论，未越过 essence-degg-test 的"去 gg 化仍有独立重量"门槛。强行沉淀违反 essence-application-needs-precondition-recheck 自己刚学的教训）

### 外部锚点

- `~/githubProject/monster/shared/docs/DEPLOYMENT.md` ← §3 项目矩阵（资产清单 SSOT，决策点 3 保持）/ §6 新增项目 Playbook（决策点 4 新项目默认范式表落点）/ §6.0 两层 nginx 实证
- `~/githubProject/monster/cg-platform/integration-contract.md` ← §5 双环境 CICD（C 路线 SSOT，本决策不改 C，只定 C 的辖域边界）
- `~/githubProject/monster/shared/docs/HZ_DEPLOYMENT.md` ← 哈轴 D 凭据 fix 的独立 SSOT
- `~/githubProject/gg/memory/reflections/2026-05-18_cgplatform-deploy-trust-model.md` ← C′ 信任模型内核（轴 A 承重根）
- `~/githubProject/gg/memory/reflections/2026-05-19_cgplatform-cicd-form-decision.md` ← C 形态 + 契约 7（部署器不变锚点）
- `~/githubProject/CGProject/cg-api/deploy.sh` ← 决策点 4 行动 2 待修参数序 bug（改前 grep 调用方）
