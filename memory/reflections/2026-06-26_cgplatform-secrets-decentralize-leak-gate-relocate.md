---
date: 2026-06-26
slug: cgplatform-secrets-decentralize-leak-gate-relocate
summoner: monster (cg-platform)
northstar_reach: "#1 二阶效应（删 I-config-leak-gate 的一阶是『闸门失意义』，二阶是 Keith 翻转的安全属性有隐含 scope=应用自有 secret，无差别删会把翻转泛化到 scope 外的平台凭据）"
status: substantive-decision
---

# Reflection: cg-platform 凭据去中心化 — 三冲击点裁决 + I-config-leak-gate 重定位

## §A 范式 A — 决策的元属性反思

### 给父会话的最终输出（必填）

**一句话裁决：改后放行。** 冲击点 1、2 直接 ACK；冲击点 3 把「裸删 I-config-leak-gate」改成「重定位传感器」——删它的 secret-命名黑名单形态（那条语义被 Keith 翻转了），但换一个 scope 收窄的「平台级凭据进应用仓」哨（显式名单 GITLAB_PAT 等）。改这一点后放行。先 cg-ppt/cg-patent-agent 单应用验证范式的计划 ACK。

**冲击点 1（撤 2026-06-25 per-app 后缀键）— ACK supersede，逻辑成立。**
后缀键解决的是「flat 共享 map 里同字段名 N 应用各异值、单字段装不下」。新模型每应用 secret 进**自己的仓** config.env——命名空间由「仓」这个物理边界提供，「一个 flat map 装两值」的问题从模型里消失，后缀键的存在理由随之消失。这是你 06-25 自己沉淀的 `carrier-coupling-overcoverage` 的整步版：06-25 是「map 内分后缀键」半步，新模型是「拆到每应用一物理文件」整步，整步让半步产物退役。我没看到后缀键的别的承重价值（它的「共享默认+per-app override」两级语义在无『共享默认』概念的新模型里也一并失效）。**但 supersede 后缀键 ≠ supersede secrets-catalog.md**——见盲区 5，catalog 在新模型下承重性反而提升，留。

**冲击点 2（改契约 7 硬层 deploy.sh，边界）— ACK 边界划得对。**
「只动存储位置不动权限模型」成立：删的 PYDS/PYSEC/PYLEAK/DATASOURCE/简化 PYCHK 全是「凭据从哪读、注入哪」；契约 1（MySQL 侧列级 GRANT，onboard 建账号时定）和契约 2（deploy.sh 行 153-158 bridge+ICC=false）deploy.sh 本就不在这些块里碰。改 secret 存哪不改 secret 能访问什么——DB 账号还是那个最小权限账号，只是密码从 datasources.json 搬进应用仓。攻击面没因「密码换存储位置」扩张到权限层。改动面我物理核对过方案 3a 清单 vs 代码，匹配——两个实现层辐射点见盲区 2、3。

**冲击点 3（翻转 secret 进 git + 删 I-config-leak-gate）— CONDITIONAL：改「裸删」为「重定位」后放行。**
拆 I-config-leak-gate 承载的两个监测对象：① secret 不进 git ② 平台级凭据不进应用仓。Keith 只翻转了①（且翻转 scope 是**应用自有** secret：爆炸半径=单应用、仓访问面他自控、接受 git 永久性）。②**没被翻转**——GITLAB_PAT 这类平台凭据爆炸半径=整个平台所有应用仓+部署链，进**任一**应用仓 = 把单应用爆炸半径放大成平台级，越过了「单应用仓访问面」这个 Keith 控制的边界。无差别删闸门 = 把①的翻转泛化到②。
正解（你方案 §1 自己已把 GITLAB_PAT 标 🔴「不进任何应用仓」，只是没机械化）：删旧的 secret 命名正则黑名单（PASSWORD/SECRET/TOKEN…，已无意义），换成 `PLATFORM_CREDS = {'GITLAB_PAT', ...}` **显式精确名单**扫 config.env，命中即 fail-loud。比旧正则还轻（查名单不猜命名模式），且这才是准入三问②「谁检验它持续成立」在新模型下的正解。这不是加回防御栏杆（CORE M1 警戒已过）——是把哨从被翻转的语义重新瞄准未被翻转的真病灶。

### 核心假设（可证伪）
1. GITLAB_PAT 一类「平台级、跨所有应用、爆炸半径=平台」的凭据，与应用自有 secret 是**不同安全 scope**——Keith 的翻转论据（仓访问面自控）只覆盖后者。若 Keith 说平台凭据进应用仓也接受，则盲区 1 收回、纯裸删成立。
2. 逐应用迁 + deploy.sh 注入块删除是最后一步——删除前注入块仍是已迁应用 config.env 漏字段时的最后安全网（map fallback）。若先删注入块再迁某应用，那应用失网。
3. 新模型最大漂移源 = N 抄共享后端连接串；其天然传感器是部署期 health db:false（轮换漏改某仓→该应用部署 health 红→蓝绿回滚→pipeline 红），不需另建轮换传感器（低频，premature-abstraction）。

### 可能出错的地方
- 最可能崩点：实现时把冲击点 3 的「重定位」省成「裸删」（只删 PYLEAK 不补平台凭据哨），半年后某次误把 GITLAB_PAT 抄进某应用 config.env、git 永久泄漏、爆炸半径平台级——这正是 `tripwire-disarm-needs-relocated-sensor-not-deletion` 警告的裸删=撤防。对冲已写进裁决（强制重定位），但若实现偷懒此根因兑现。
- 次可能：cg-meetos 这类混合来源 legacy 应用（test 走字典 test_datasource / prod 走 legacy env-file）迁移时只扒一处，漏 prod 来源 → prod 部署 health 红才发现。

### 本次哪里思考得不够
- 没逐一核 registry.json 里每个在册应用的当前凭据来源分布（哪些 self_serve 走字典 / 哪些 legacy 走 env-file / 哪些混合）——迁移最易漏在混合来源应用，这份分布该在迁移前由实现层 dump 一张表（每应用 × 每环境 × 来源），我只点了 cg-meetos 一个样本。
- 平台凭据显式名单的「完整成员」我只确证 GITLAB_PAT 一个（方案 §1 唯一标 🔴 的）；未来若引入 registry push 凭据 / CI token 等新平台凭据，名单要同步——名单本身需要一个 owner（建议挂 secrets-catalog.md 旁，与命名 SSOT 同处）。

### 如果 N 个月后证明决策错了，最可能的根因
凭据存储从「中心 map」彻底去中心到「N 仓各抄」后，安全防御从「一道集中闸门（leak-gate）+ 一处集中 map」摊薄成「N 个仓各自的纪律 + 按需 drift_audit」。若平台凭据哨没真正落地（冲击点 3 偷懒裸删），平台级凭据误抄进某应用仓且 git 永久化，是不可逆泄漏——根因会是「把集中防御的复杂度去中心化时，最高爆炸半径那一类凭据没保留集中防御」。Keith 翻转的是低爆炸半径类的存储位置，不该连高爆炸半径类的防御一起摊薄。

### 北极星触达
**#1 二阶效应**：三个冲击点里 1、2 是一阶对账（逻辑/边界核对）；冲击点 3 是二阶——看穿「Keith 翻转的安全属性带一个隐含 scope（应用自有 secret），删无差别闸门会把翻转沉默地泛化到 scope 外（平台凭据）」。一阶视角会直接 ACK「闸门失意义→删」，二阶视角拆出闸门承载的多 scope、只放行被翻转的那个 scope。

### essence 对齐自检（必填）
- **本决策对位哪几滴**：`tripwire-disarm-needs-relocated-sensor-not-deletion`(2026-06-15，本次精确活体——回审/翻转挂在某属性上的哨时，触发条件失效≠裸删，先问「它还盯着什么没被翻转的事」；这次触发从「NW tripwire 回审」扩到「安全属性被 owner 主动翻转」)；`carrier-coupling-overcoverage`(2026-06-25 候选，本决策是其**放开侧对称面**——上次「约束过度泛化源于载体耦合，拆载体根治」，这次「放开过度泛化源于无差别闸门，按真相拥有者分 scope 收窄」)；`reversibility-not-permission`(deploy.sh 删注入块放最后=按爆炸半径/可逆性排序迁移)；monster `attribute-failure-layer-before-restructure`(平台凭据哨是结构传感器不是加规则)。
- **是否在某条 essence 上反着走**：潜在张力 CORE M1 防御式思维警戒——「换个平台凭据哨」是不是加回栏杆？判断不是：M1 警的是「防从未发生过的灾难的幽灵规则」，平台凭据泄漏爆炸半径=平台级且 git 永久不可逆，是真实高代价且 monster 方案 §1 自己已识别该类别（标 🔴），把已识别类别机械化 ≠ 造幽灵栏杆。
- **cross-check 用的关键词**：grep 了 `carrier-coupling`(确认 06-25 候选仍未 append 进 essence.md，与其 reflection 标注 N 一致，诚实记录)/`reversibility-not-permission`/`ssot-distillation-vs-buffering`/`premature-abstraction-tripwire`，并 Read essence.md line 783-786 确证 `tripwire-disarm-needs-relocated-sensor-not-deletion` 全文。

### essence 候选（可选）
- slug: `safety-flip-needs-scoped-gate-not-deletion`
- 一句话: 当 owner 主动翻转一个安全属性（如 secret 从「禁进 git」变 intended），挂在该属性上的无差别闸门不能裸删——闸门常对多个爆炸半径不同的对象（应用自有 secret / 平台级凭据）一视同仁，而翻转只对爆炸半径可控的那个 scope 成立；正解是把闸门 scope 收窄到未被翻转的高爆炸半径子集（重定位传感器）。是 `carrier-coupling-overcoverage` 的放开侧对称 + `tripwire-disarm-needs-relocated-sensor-not-deletion` 在「属性被主动翻转」触发下的活体。
- 是否已 append 到 essence.md: Y（本轮已 append，留 Keith review）

### 外部锚点（可选）
- `~/githubProject/monster/cg-platform/docs/secrets-decentralize-plan.md`（本次裁决落点，冲击点 3 改 §3a「删 PYLEAK」为「重定位平台凭据哨」+ §3b/§5 同步）
- `~/githubProject/monster/cg-platform/cg-platform-deploy.sh`（行 242-269 PYLEAK 不裸删、改名单式平台凭据哨；行 147 heredoc 变量传递删 DATASOURCE 项）
- `~/githubProject/gg/memory/reflections/2026-06-25_cgplatform-secrets-shared-vs-perapp-split.md`（本次 supersede 的前裁）
