---
date: 2026-05-19
slug: cgplatform-cicd-form-decision
summoner: cc-space
northstar_reach: "#3 决策超越直觉（CI/CD 承重墙不可逆边界设计）"
status: substantive-decision
---

# Reflection: cgPlatform PM PaaS CI/CD 形态决策

### 给父会话的最终输出（必填）

**推荐：形态 C 变体「CI 触发器 + cgplatform-deploy.sh 执行器 + runner 降权 deploy-bot 身份 + per-app deploy key + 双环境分级触发」。否决 A（拆掉契约 3 唯一锚点），否决纯 B/纯 D（无部署事实物理证据层），C 变体收编 D 作为 test-only 降级兜底。**

**理由链**：
1. 不变性锚点 = `cgplatform-deploy.sh` 是契约 3 rbash sudo 白名单唯一放行物。只要最终落到"调这个脚本"这一跳，契约 3 横向移动防御就成立——触发层（CC会话/CI/人手）是可替换实现细节（essence invariance-allocation）。A 死在它绕过脚本做 tar+scp 覆盖式发布 = 物理拆掉 v0 已拍承重墙。
2. B/D 满足契约 3 但失败形态 = 部署成败可观测性绑定在"CC 会话是否如实回报"上（task-compliance-is-not-truth）。PM 应用是 AI 生成+AI 运行，部署这一跳必须有不经 LLM 的物理证据层。**召唤者漏看的关键价值：C 不只是 B 的自动化升级，C 是契约 5（审计 trail，v0 推迟）的廉价前置实现**——pipeline exit code + stage log 就是部署事实的物理记录。
3. C 变体 = D 的契约3合规 + B 的会话可不在场 + CI 的物理审计层三合一。

**硬点 1 裁决（CI runner 身份 vs 契约 3）**：召唤者的二分（root → 架空 / pmapp@ key → 泄露面）错在把"身份"和"凭据存放位置"两个正交维度黏一起。拆开：
- 维度 A（身份）：新建 `cgplatform-deploy-bot@` 独立账号，共享 pmapp@ 的 rbash+sudoers 模板但**更窄（无 docker logs）**。不复用 pmapp@ 账号——触发面(CI)和交互面(CC会话)是不同的面，按面隔离(ownership-by-facet)，成本近零。
- 维度 B（凭据）：deploy 私钥**禁止进任何 gitlab CI variable**，落 runner 宿主本地文件 chmod 600。理由：PM 的 .gitlab-ci.yml 是 AI 生成的 = prompt injection 可达 = CI variable 可被诱导 echo 外泄。把私钥从 AI 可触达面物理移到不可触达面（physical-anchor）。
- 配套硬约束：deploy stage 由新建 `cgplatform/ci_template` 强制 include，PM 仓 AI 只能生成 build/test stage，**不可覆盖 deploy job**。

**硬点 2 裁决（自动化节奏 vs 契约 4）**：召唤者两个选项其实是同一答案两种说法。正解 = 按终态可见性分流（terminus-walk-needs-terminus-visibility）：
- test 环境（终态清晰、可逆）→ v0 期就上全自动，别给 PM 试错建笼子（caged-freedom）
- prod 环境（终态模糊、不可逆侧）→ v0 期 `when: manual`（gitlab CE 也有），点击人=Keith。**这个 manual gate 就是契约 4 触发条件"PM 直发 PRD 不经人眼"没发生的物理证据**。去掉 prod when:manual ⟺ 契约 4 必须同时落地——把节奏咬合从靠记忆升级成 pipeline 配置里的物理 gate（rule-layer-flywheel）。

**Trade-off / 未核验假设（关键，红队未完全击败 2 条）**：
- 红队未击败 1：gitlab `include:` 的 job 可被本仓同名覆盖（真实 gitlab 行为）。契约 7.4 锁定需要 gitlab Premium 的 "Required pipeline configuration"；**若川锅 gitlab 是 CE → 降级方案：deploy 不放 CI，runner 只 curl 一个 PM 不可达的内部 deploy-trigger 服务**。川锅 gitlab 版本我无物理证据。
- 红队未击败 2：runner 若注册在生产 docker 宿主或挂 docker.sock，整个身份降权是纸糊的。川锅 runner 宿主拓扑 DEPLOYMENT.md 没记，我无物理证据。
- 按 redteam.md 规则：含未击败红队的不可逆决策不能 gg 单方拍死 → 拆层：形态+硬点2+契约7框架 5/5 直接拍（不依赖未核事实）；硬点 1 架构方向 5/5 拍，但 **2 个实施前置物理核查项交父会话 ssh 补证据后才能落地**。

**行动建议**：
1. 父会话实施契约 7 前必须 ssh 核验 2 项：① 川锅 gitlab 是 CE 还是 Premium ② gitlab runner 注册在哪台机、是否挂 docker.sock。5min 能核完。
2. 新增契约 7「部署触发链隔离」（v0 装，契约 3 的 CI 侧延伸，同等承重）——7.1 触发分级 / 7.2 执行层只调脚本 / 7.3 身份隔离+私钥禁进 variable / 7.4 配置锁定 / 7.5 节奏闸门绑契约 4。规则表见父会话 final message。
3. v0 实施顺序：1→3（建 pmapp@ 同时建 cgplatform-deploy-bot@）→新增 3.5 契约7（前置核查→建 cgplatform/ci_template→test auto/prod manual）→2→6→dogfood。
4. paas-deploy skill 改设计：产物从"我 ssh 跑 deploy.sh"改为"我 git push 到 cgplatform/<app> test 分支，pipeline 接管；prod 由 Keith 点 manual"。skill 不持有 deploy-bot 私钥（私钥在 runner 宿主）。保留 D 作 test-only 降级兜底（一次性 spike 不进 gitlab 时走 pmapp@ ssh，prod 永不走会话直发）。
5. ssot/registry.md 新增 `cgplatform/ci_template`（与 front/ci_template 并列且隔离不复用）+ `cgplatform-deploy-bot@ 凭据落点`（runner 宿主本地，禁 CI variable）。
6. 失败形态监视：契约 7.5 触发监视段监视的是"prod manual job 点击人是否仍 Keith/授权 dispatcher"，不是"manual gate 是否还在"（gate-as-physical-fuse 反面：gate 存在 ≠ 人眼有效）。

完整决策（含契约 7 规则表 / v0 顺序图 / 红队 3 条 / 3 个失败形态）见 final message。

### 核心假设

- `cgplatform-deploy.sh` 真的只 reload `/etc/nginx/conf.d/cgplatform/` 子目录、不 reload 全局 nginx（红队 3 的咬合前提，实施时验）
- 川锅 gitlab runner 存在且可新建独立 CI executor 机器（未核——红队 2）
- gitlab `when: manual` 在川锅 gitlab 版本可用（CE 也有，置信度高）
- DEPLOYMENT.md 记的腾讯云新拓扑（1.14.13.140 → 172.27.0.5）是当前真值，老 CI 的 10.13.1.29 PROD_SERVER 确已过时（已用 grep 物理核验 §1.1/§1.3）

### 可能出错的地方

- 最高风险：川锅 gitlab CE，CE 降级 deploy-trigger 服务方案被当"v1 再做"推迟，PM 的 AI 同名覆盖 deploy job 自定义 scp 到生产宿主——契约 7.4 架空（fermentation-without-detector 形态）。概率中。缓解=契约 7.4 实现必须和 test 自动化同时上线，不允许先上自动化后补锁定。
- 次高：runner 在生产宿主，deploy-bot 降权纸糊。概率取决于川锅图省事程度，未知。
- 中：prod manual 点击人从 Keith 漂移成 PM（Keith 嫌烦放权），gate 在但语义死。概率中。

### 本次哪里思考得不够

- gitlab CE/Premium 和 runner 宿主是承重墙实现路径的分叉点，我没有物理证据只能交还父会话核——这不是盲区是 physical-anchor 纪律的正确应用，但意味着这个决策的"完整可落地"依赖父会话补两步，gg 单方未闭环
- CE 降级方案（runner curl 内部 deploy-trigger 服务）只给了方向，没展开该服务本身的鉴权/部署形态——如果走这条路需要再起一轮设计
- 没核 `cgplatform/ci_template` 与川锅 `front/ci_template` 是否真能完全隔离（gitlab group 级 runner 共享可能引入交叉），列为实施验证项

### 如果 N 个月后证明决策错了，最可能的根因

- 形态 D-fail（最高，承接 v0 reflection 形态 A）：gitlab CE 降级方案没认真做，AI 生成 ci.yml 覆盖 deploy job 绕过隔离。触发因=前置核查没在实施前做或 CE 降级被推迟
- 形态 E-fail：runner 在生产宿主，身份降权全程纸糊
- 形态 F-fail：prod manual 点击人漂移，gate-as-physical-fuse 反面——gate 存在给虚假安全感
- 共同根因：承重墙实现细节依赖 2 个无物理证据的前置事实 + 1 个会漂移的人因。这正是拆"架构方向拍 / 物理核验交父会话"的原因

### 北极星触达

#3 决策超越直觉——CI runner 身份是不可逆错误的物理放大器（攻破后横向到生产）。决策没停在召唤者的二分框架内，而是拆出"身份 vs 凭据位置"正交维度 + 把节奏咬合从记忆升级成 pipeline 物理 gate。符合 essence ghost-rules 警戒域审视：契约 7 防的是 AI 生成 pipeline 配置的真实物理风险（prompt injection 入口与部署权零距离），不是幽灵规则。

### essence 对齐自检（必填）

- **本决策跟哪几滴 essence 对位**（grep 物理命中）：
  - `invariance-allocation` (2026-04-19) — 形态决策本质=选「脚本即契约锚点」为不变量，触发层可换。直接推理依据
  - `physical-anchor` (2026-04-16) — 私钥从 CI variable（AI 可触达）物理移到 runner 宿主（不可触达）；承重墙实现细节不能建二手转述上 → 交父会话 ssh 核
  - `terminus-walk-needs-terminus-visibility` (2026-05-02) — 硬点 2 正解=按终态可见性分流（test 清晰按终态走 / prod 模糊按 emergent 走 + 物理 gate）
  - `task-compliance-is-not-truth` (2026-04-16) — B/D 拒因=部署成败绑定 LLM 如实回报
  - `ownership-by-facet` (2026-05-06) — runner 身份不复用 pmapp@：触发面 vs 交互面按面隔离
  - `rule-layer-flywheel` (2026-04-24) — when:manual 物理 gate > 靠记忆的节奏咬合（事件层 vs prompt 层）
  - `fallback-detectability` (2026-05-06) — B/D 失败形态=部署失败被误判为成功，CI exit code 是检测器
  - `gate-as-physical-fuse-not-business-metric` (2026-05-07) — 失败形态 F：gate 存在 ≠ 人眼有效，监视点击人不是监视 gate
  - `caged-freedom` (2026-04-26) — test 全自动别给 PM 试错建笼子
- **本决策是否在某条 essence 上反着走**：潜在张力，已展开——契约 7 是第 7 条契约，触碰 essence `ontology-expansion-velocity-needs-cap`（扩展节奏封顶）。但契约 7 不是新本体论层/新视角桶，是契约 3 在 CI 侧的同维度延伸（同一"deploy 权限边界"主体），归得入已有契约 3 的语义域，不构成扩展节奏失控。明示通过封顶自检。
- **cross-check 用的关键词**：`invariance-allocation / physical-anchor / terminus-walk / task-compliance / ownership-by-facet / rule-layer-flywheel / fallback-detectability / gate-as-physical-fuse / caged-freedom / ontology-expansion-velocity`（均在 essence.md 全文 grep 命中）

### essence 候选（可选）

- slug: ai-authored-pipeline-config-is-injection-surface
- 一句话: AI 生成的 CI/CD 配置文件本身是 prompt injection 攻击面——部署凭据放"masked CI variable"是软保证，AI 能 echo 出来；唯一硬边界是把凭据物理移到 AI 不可触达的位置（runner 宿主本地）+ deploy stage 平台锁定不可被生成配置覆盖。
- 是否已 append 到 essence.md: N（本次不沉淀——这是 `physical-anchor` + v0 reflection 已记的 `ai-code-runs-attack-surface-asymmetry` 在 CI 配置层的应用，"AI 生成的配置也是攻击面"是前者的直接推论不是新洞察。强行沉淀违反 essence-degg-test）

### 外部锚点

- `~/githubProject/cc-space/threads/cgboiler-pm-sandbox.md` ← 契约 7 应追加进此 thread 时间线 + 触发监视段
- `~/githubProject/cc-space/inbox/briefs/pm-paas-platform.md` ← v0 决策快照（契约表应加第 7 行）
- `~/githubProject/gg/memory/reflections/2026-05-14_cgboiler-pm-sandbox-contract-v0.md` ← v0 6 契约决策，本决策是其延伸
- `~/githubProject/cc-space/shared/docs/DEPLOYMENT.md` ← 物理事实锚点（§1.1/§1.3 腾讯云拓扑 + §4.3 deploy.sh 蓝绿）
- `~/githubProject/cc-space/ssot/registry.md` ← 待新增 `cgplatform/ci_template` + `cgplatform-deploy-bot@ 凭据落点`
