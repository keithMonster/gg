---
date: 2026-05-19
slug: cgplatform-test-env-rebuild
summoner: cc-space
northstar_reach: "#3 决策超越直觉（被推翻前提下的承重墙重裁——不是推倒重来而是精确定位假设错点）"
status: substantive-decision
supersedes-partial: 2026-05-19_cgplatform-cicd-form-decision (硬点 2 test 侧隔离假设 + 契约 7.5 解锁条件 + v0 实施顺序 2/3/3.5)
---

# Reflection: cgPlatform test 环境形态重裁（契约 7 同维度修订）

### 给父会话的最终输出（必填）

**重裁结论**：选 **(a) 借川锅 test 机 10.13.1.61 共宿主 + 逻辑沙箱隔离补丁**。否决 (b) 单开独立 test 宿主（违反 v0「不装新平台编排已有基建」元方法论 + OCCAM——独立 test 要复制 MySQL/keycloak/cg-proxy 全家桶）。否决 (c) 单环境裸蓝绿（PM=AI 生成+AI 运行，单环境=未验证代码第一次落地即唯一环境，蓝绿/recycle 是事后补救不是 terminus 前试错，直接抹掉硬点 2 按终态可见性分流的核心）。

**被推翻前提的精确定位（关键）**：被推翻的不是硬点 2 分流逻辑，是我上次 v0 物理边界图 test 机那行只写"docker logs + cgplatform-deploy.sh"、把"test 机隔离已被契约 2/3 覆盖"当隐含已交付——这是边界图的不完整。补 test 机隔离延伸，"test 全自动 / prod manual"分流原样成立。

**5 个子裁决**：

1. **建 test + 形态**：(a) 共宿主 + 补丁。物理前提已核：10.13.1.61=test-debian docker 宿主，跑 cg-proxy/keycloak/qdrant/cgManager-test 全家桶（DEPLOYMENT.md §1.3/§1.5）。契约 2 隔离粒度本就是 docker network 级不是机器级，共宿主≠共网络≠共DB，(a) 不是裸共机是"契约 2/3 边界平移到 test 机"。

2. **硬点 2**：分流结构零修改。test 侧（PM 的 cgplatform/<app> test 分支 → 10.13.1.61 cgplatform-net 内 PM 容器）对 PM 终态清晰可逆，分流前提成立。新增硬约束：川锅 test 业务对 PM 是不可逆侧，pipeline 绝不触碰 10.13.1.61 川锅容器/test 库/nginx 主 conf（进契约 7.4）。不坍缩成"都是 prod 性质"——那只在走 (c) 时成立，已否决 (c)。

3. **契约 7.5 节奏闸门**：不重写。prod when:manual + 监视点击人锚定"prod 不可逆侧不经人眼"，与 test 是否独立无关（prod 永远腾讯云 172.27.0.5）。唯一精确化：解锁条件从"去掉 prod manual ⟺ 契约 4 落地"精确为"⟺ 契约 4 落地 ∧ test 隔离补丁已物理验证生效"（防"脏 test 看着绿→误判可解锁 prod"的 gate-as-physical-fuse 反面）。新增可物理验证项：`docker network inspect` + `docker exec PM容器 curl 川锅容器` 实测不可达的 exit code。

4. **进 v0 实施顺序**：进，但不是新 brief 级条目——它就是契约 2/3 边界向 10.13.1.61 延伸，寄生在已有步骤。改动仅第 2/3/3.5 步：契约 3 加 pmapp@/deploy-bot@ 在 test 机同等创建；契约 2 加 cgplatform-net --internal 在 test 机创建；契约 7 前置 ssh 核查从 2 项→3 项（新增"test 机 docker network 默认可达性实测"），三项同批并行核，但核查批次整体前移到第 2 步后/第 3 步实施前（第③项结论改契约 2 在 test 机实现强度）。

5. **契约 2/3 边界延伸**：必须延伸，是 (a) 成立的前提条件不是可选加固。三个共享面逐一封——docker network（契约 2 延伸：cgplatform-net --internal 在 test 机 + 核查③定隔离强度）/ test 机 fs+deploy 身份（契约 3 延伸：同 rbash+sudoers 模板，cgplatform-deploy.sh 只 touch /opt/projects/cgplatform/<app>/ 绝不 reload 川锅 nginx）/ test 库（契约 1+2 联合：PM 凭据绝不发 cgManager@10.13.1.61:33060）。

**举手交 Keith 拍的目标层问题**：PM 应用 test 数据落哪个 MySQL？推荐复用 prod 实例 db.cgboiler.com:9033 的 cgPlatform 库 + `<app>_test_*` 表前缀（OCCAM + 契约 1 既定范式）。想让 test 数据物理落 10.13.1.61 test MySQL（环境彻底隔离 > OCCAM）需 Keith 拍——触碰契约 1"单一平台库"决策属目标层。

**失败形态（接上次 D/E/F，新增 G/H）**：
- G-fail（最高）：逻辑沙箱补丁被当"加固项"而非"前提条件"，为赶 dogfood 先上 PM test 应用、契约 2/3 test 机延伸"v1 再补"→ PM AI 代码在未隔离 test 机横向到川锅 keycloak/cg-proxy。是上次 D-fail（CE 降级被推迟）同构复发——承重墙物理实现被降级后补。缓解纪律（进契约 7.4，与 D-fail 缓解合并）：「沙箱隔离物与被隔离物同时上线，永不先开放后补墙」。
- H-fail（中）：核查③没认真跑，凭"--internal 应该够"假设上——但 --internal 只阻断容器→外网，不阻断同宿主其他 network 容器互访（取决 iptables FORWARD）。physical-anchor 违反。缓解：核查③产出必须是实际 curl exit code 不是文档推断。
- 新增共同根因：(a) 这个 OCCAM 选择把隔离责任从"物理机边界（天然强）"转移到"docker network 配置（需主动正确配置且易想当然）"——省一台机的代价=隔离强度从硬件级默认安全降级成配置级条件安全。trade-off 本身正确（符合 v0 元方法论），但把"隔离是否真生效"变成必须物理验证不能假设的事。这是 (a) 优于 (b) 的代价的精确表述。

**辐射点（父会话落，不执行）**：① thread 物理边界图替换 test 机块（1 行→隔离块）+ 时间线追加修订条 + 契约 7 表行补 test 共宿主隔离语义 + v0 顺序 2/3/3.5 重排 + 触发监视表契约 7 解锁条件加"∧ test 隔离补丁已验证" ② brief 契约 7 行同步 ③ ssh 前置 2→3 项 ④ essence 封顶自检通过。

### 核心假设

- 10.13.1.61 PM 应用以 docker 容器跑（契约 2 cgplatform-net 是 docker network 级隔离的前提）——v0 brief「非 docker 部署不在契约覆盖」已锁此假设，成立
- 川锅 test 业务对 PM 是"不可逆侧"——keycloak/cgManager-test 是川锅其他开发者在用的活跃 test 资产，PM 污染它=破坏川锅 test 工作流，按不可逆对待（DEPLOYMENT.md §1.3 实证 test 机跑全家桶）
- prod 侧完全不被本次前提推翻触碰（prod=腾讯云 172.27.0.5，与 test 是否独立正交）——已 grep DEPLOYMENT.md §1.1/§1.3 核

### 可能出错的地方

- 最高风险 = G-fail：补丁被实施者读成"加固"而非"前提"。这是我上次 D-fail 的同构复发，说明"承重墙的某个物理实现被降级成后补"是这条主线的反复失败模式，单靠 reflection 文字提醒挡不住——必须靠契约 7.4 里那条可被 ssh 验证的硬约束（隔离物与被隔离物同时上线）做物理 gate
- 次高 = H-fail：`--internal` 语义我也只是按理解写"物理切"，没在 test 机实测同宿主跨 network 可达性。本决策正确性依赖核查③，gg 单方未闭环（同上次模式：架构方向拍 / 物理实测交父会话）
- 中：表前缀 test/prod 共库（举手项若 Keith 选 OCCAM）会让 test 的"可逆性"打折——test 误操作可能脏到 prod 实例上的 cgPlatform 库（虽不同表前缀但同实例同 root）。已在举手项里标这是 trade-off

### 本次哪里思考得不够

- 没展开核查③具体怎么跑出确定性结论——"docker exec PM容器 curl 川锅容器"是方向，但 PM 容器在 dogfood 前还不存在，核查③实际要用一个临时 probe 容器加入 cgplatform-net 测可达性，这个 probe 的构造没给
- 表前缀共库 vs test 机独立 MySQL 的举手项，我倾向 OCCAM 但没量化"脏到 prod cgPlatform 库"的实际概率——若 PM test 应用 SQL 误删 <app>_test_* 表，recycle 备份能救，但若误连写 <app>_* prod 表则跨环境污染，这个风险面没充分展开就交还 Keith
- 没核 10.13.1.61 的 docker 是否已有其他 --internal network 命名冲突 / 端口清单是否最新（DEPLOYMENT.md §3.x 列的占用端口可能已变），列为实施验证项

### 如果 N 个月后证明决策错了，最可能的根因

- G-fail（最高，承接上次 D-fail）：隔离补丁被降级后补，PM 在脏 test 机横向。共同根因=承重墙物理实现依赖"实施者正确理解前提 vs 加固的区别"这个人因 + 无物理证据的前置事实（核查③）
- H-fail：--internal 隔离强度想当然，PM 容器实际可达川锅 test 容器
- 表前缀共库根因：OCCAM 选择把 test 可逆性和 prod 实例绑在一起，某次 PM test 误操作脏到 prod cgPlatform 库
- 元根因（本次特有）：用 (a) 共宿主省一台机，把隔离从硬件级降到配置级——这个 trade-off 决策正确，但它的代价（隔离需物理验证不能假设）若被实施环节忽略，省的那台机的成本会以"横向移动事故"形式连本带利还回来

### 北极星触达

#3 决策超越直觉——直觉反应是"前提被推翻→推倒重来重新设计 test 环境"。实际正确动作是精确定位假设错在哪一个点（v0 边界图 test 机那行不完整），证明硬点 2 分流逻辑/契约 7.5 gate 锚点都不依赖被推翻的前提，只有"test 隔离已交付"这个隐含 AND 没显式化。最小修订面 = 1 张边界图 + 1 个解锁条件 AND + 3 步实施重排，不是重写契约 7。符合 essence ghost-rules 警戒：补的隔离边界防的是 AI 生成代码在共宿主 test 机横向到川锅活跃 keycloak/cg-proxy 的真实物理风险，不是幽灵规则。

### essence 对齐自检（必填）

- **本决策跟哪几滴 essence 对位**（grep 物理命中）：
  - `terminus-walk-needs-terminus-visibility` (2026-05-02) — 否决 (c) 单环境的核心：单环境下 PM 永远在终态模糊+不可逆侧走，没有终态清晰可逆的 test 侧。直接推理依据
  - `physical-anchor` (2026-04-16) — --internal 隔离强度不能按文档推断，核查③必须是实际 curl exit code；本决策可落地性依赖父会话物理核
  - `caged-freedom` (2026-04-26) — test 侧给 PM 试错自由的前提是 test 侧本身是合格的"笼内安全场"，脏 test 不是 caged-freedom 是 caged-disaster
  - `invariance-allocation` (2026-04-19) — cgplatform-deploy.sh 仍是不变锚点，本次只把它在 test 机的边界（只 touch /opt/projects/cgplatform/）显式化
  - `gate-as-physical-fuse-not-business-metric` (2026-05-07) — 契约 7.5 解锁条件加"∧ test 隔离已验证"防"脏 test 绿→误判可解锁 prod"，gate 存在 ≠ 验证场有效
  - `ownership-by-facet` (2026-05-06) — 共宿主下川锅 test 业务 vs PM test 应用是不同面，按面隔离（cgplatform-net + 独立 deploy 身份）
  - `rule-layer-flywheel` (2026-04-24) — "隔离物与被隔离物同时上线"做成契约 7.4 可 ssh 验证的硬约束，不靠记忆
- **本决策是否在某条 essence 上反着走**：表面与 OCCAM 有张力——(a) 共宿主是 OCCAM（省一台机），但引入"隔离需物理验证"的额外负担。已展开：这不是反 OCCAM，是 OCCAM 的正确代价显式化（省机器的代价=配置级隔离需验证），符合 trade-offs 必显式说明
- **ontology-expansion-velocity-needs-cap 封顶自检**：本次是契约 7 同维度修订（同一"deploy 触发/权限边界"主体语义域），不新增契约/不新增本体论层/不新增视角桶——契约 2/3 边界向 test 机延伸是同一边界对象的物理范围扩展不是新对象。明示通过封顶，未触碰扩展节奏失控
- **cross-check 用的关键词**：`terminus-walk / physical-anchor / caged-freedom / invariance-allocation / gate-as-physical-fuse / ownership-by-facet / rule-layer-flywheel / ontology-expansion-velocity`（均 essence.md 全文 grep 命中）

### essence 候选（可选）

- slug: occam-tradeoff-shifts-burden-not-eliminates-it
- 一句话: OCCAM 选「复用现有基础设施」省的不是隔离责任本身，是把隔离责任从「硬件/物理边界（天然强、默认安全）」转移到「配置边界（需主动正确配置、易被想当然、必须物理验证）」——省资源的决策正确，但代价是"隔离是否真生效"从可假设变成必须每次物理核验的事，实施环节若忽略这个转移会连本带利还回来
- 是否已 append 到 essence.md: N（本次不沉淀——这是 `physical-anchor` + 既有 trade-offs 纪律的组合应用，"OCCAM 有代价"是已知的；唯一稍新的是"代价的形态=责任从硬件转配置层"，但这是 physical-anchor 的直接推论，不构成独立新洞察。强行沉淀违反 essence-degg-test。留候选供未来若同形态复发 ≥2 次再升）

### 外部锚点

- `~/githubProject/gg/memory/reflections/2026-05-19_cgplatform-cicd-form-decision.md` ← 被本次部分 supersede（硬点 2 test 隔离假设 / 契约 7.5 解锁条件 / v0 顺序 2/3/3.5），形态 C 变体 + 硬点 1 + 契约 7 框架不变
- `~/githubProject/cc-space/threads/cgboiler-pm-sandbox.md` ← 物理边界图替换 test 机块 + 时间线追加 + 契约 7 表行 + v0 顺序 + 触发监视表
- `~/githubProject/cc-space/inbox/briefs/pm-paas-platform.md` ← 契约 7 行同步
- `~/githubProject/cc-space/shared/docs/DEPLOYMENT.md` ← 物理事实锚点（§1.3 test=10.13.1.61 test-debian 全家桶 / §1.5 test 库 cgManager@10.13.1.61:33060 / §1.1 prod 腾讯云 172.27.0.5）
