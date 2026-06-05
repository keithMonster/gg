---
date: 2026-06-05
slug: cgplatform-foundation-hardening-review
summoner: monster
northstar_reach: "#3 决策超越直觉（识破方案自我背书的虚假证据厚度 + 拎出未被识别的 B 层 SSOT 盲区）"
status: substantive-decision
---

# Reflection: cg-platform 平台底子加固方案评审

## §A 范式 A — 决策的元属性反思

### 给父会话的最终输出（必填）

**总裁决**：方案 framing 正确、地基（Q1）成立但作者高估了证据强度、P0 该立即做、P1/P2 多数倾向对——但有一条作者没列进开放项的承重盲区必须补。不推翻方案。

**Q1 地基「活的主干」成立，但论证错了**：不变量维持。**撤掉"被 6 个 dogfood 坐实"这句话**——物证（registry.json）：6 个里 5 个 db:null，唯一有真业务 DB 的是 cg-meetos（cgPlatform 6 表）。样本量 N=1 不是 N=6。"AI 维护单仓成本趋零"被 scaffold.py 坐实了（复用转移到生成时这半边为真），但"fork 冻结的耦合代价不会反超"这半边 6 个 dogfood 零压测。正确论证：不变量靠"前提物理为真 + 目标函数写死"撑着，**不是靠实证**——诚实标 `[前提成立，实证待积累]`。把"被坐实"写进 thread = 给未验证不变量制造虚假证据厚度 = 系统内部伪造一致性证明（哥德尔意义）。**反超场景作者问了没答全，我替答**：不是两个 PM 应用共享业务代码（那不会发生），是 `common/` 里的"平台对接范式"——尤其契约 9 身份 guard（调 cg-api check-token），每个 fork 逻辑相同、协议变更时全 fork 同时失效。它行为上属 **B 层（必须单点 / 协议变更全传播），不是 C 层**。作者把整个 common/（健康检查 + 异常 filter + 响应包络 + 身份 guard）塞进 C 层"随 fork 冻结"——健康检查可以冻结，身份 guard 不能。

**Q2 provision 现在封——对，理由纠正**：不是"6-05 证明频率判断失效"，是触发条件设错了层。原触发"频率上来再封"把 provisioning 当优化项（COST-BENEFIT），但 env-file 同步这步是"人肉维护 fail-silent 运行时关键状态"——频率低反而更危险（人更记不住）。归因层 = L4（人脑做不可靠状态同步）+ L3（zod .default() 静默缺失），不是 L2 频率。SKILL 9 步漏写 3 步是 5 次 onboard 实账，事实根因。

**Q3 运行时版本化值得做，但反对并进 C″——作者图省事了**：P1（drift，正确性问题，零安全语义）和 C″（信任边界，安全问题）正交，强行耦合理由"都碰信任边界"是抽象洁癖。后果 = 把今天该解的简单正确性问题（drift），绑到触发未到 + 解法复杂（GitLab Free 做不到强制 PM 不可改 deploy）的安全问题上一起拖死。**P1 现在做最简版**：runner 从受控 git 源同步，runner 本就持 deploy.sh 完整执行权，从 scp 拿还是 git 拿信任级别一字未变——"多一条信任链"是假担忧。C″ 维持原触发。**命门 `[待核实]`**：prod runner #40 在腾讯云、GitLab 是内网 gitlab.cgboiler.com，prod runner → 内网 GitLab 可达性未核实，落地前先验证，不可达则 P1 降级为 CI artifact 注入。

**Q4 契约 5 改触发条件——对，但别改成又一个软判断**："实质风险"太虚会变成永不触发的借口。锚到硬条件：**契约 5 触发 = 契约 4 触发（第一次 PM 直发 PRD 不经人眼）**——审计 trail 存在意义就是为"不经人眼"那刻能回溯，与契约 4 是同一威胁模型的防/查正反面，共用触发逻辑自洽不可耍赖。

**Q5 契约 6 等触发不预写——对**。加一句：P0-1 provision 脚本写时顺手输出"创建了哪些资源"清单（registry 条目 / env-file / deploy-key / 端口段 / 容器 / 库 / nginx）。这是回收的前置数据非回收脚本本身，零额外成本，省未来回收时考古。

**Q6 不借本轮 ratify 契约 9——反对作者，这踩了 monster 自己的铁律**。契约 9 是上游契约 + 跨系统对接协议（应用↔cg-api↔企微），辐射所有 fork、ratify 后是硬契约。按 CLAUDE.md Workflow #1 + Decision Authority，它该是独立决策不是评审附属项。把它塞进"实现层加固"评审搭便车，是用低风险评审的通过惯性夹带高风险契约批准——和 Q3"并进 C″"同一毛病的镜像（那次把易事绑难事拖死，这次把难事藏易事蒙混）。更实质：capability-map 自承契约 9 spec-skeleton 还有缺口（VX_API/AUTH_PAGE 字段 + auth.guard.ts 骨架 + APP_GUARD 注册全"留首个真 fork 时补"）——实现骨架没补全的契约凭什么 ratify = 给空白支票盖章。**研发标准侧（ENGINEERING-STANDARD §0.6/§2）已生效继续跑不受影响**——研发标准是建议范式不需 ratify，沙箱契约是硬边界才需，作者混淆了两层级。触发 = 第一个真接 check-token 的 fork，那时连缺口一起补 + 独立威胁模型 + 单独 ratify。

**承重盲区（本次评审真正增量，作者没列）**：env-file 是 B 层运行时物件但游离在所有 SSOT 治理之外——6-05 根因不是 provisioning 没脚本化，是 env-file 这类物件根本没被识别为"平台运行时状态"。三层框架问"哪层代码该共享"，漏了正交维度"哪些是运行时状态/配置物件、SSOT 在哪、谁保证一致"。盘 cg-platform 运行时物件：deploy.sh / registry.json 已有 SSOT（monster git）+ 同步机制（sync 脚本人肉），**唯独 env-file（装 DB 密码）连 SSOT 都没有**——不进 git（对，有密码）但也没有声明式来源 + 注入机制，纯手敲。zod .default() 只是把缺失从"启动崩"恶化成"带病跑"，但就算 fail-fast 了，env-file 该有什么字段值从哪来依然没 SSOT。**架构层动作**：引入 `<slug>.env.schema`（进 git，声明字段名 + 来源标注、不含值）作 env-file 的 SSOT，provision 脚本据 schema 注入 + 检测缺字段。env-file 从"手工孤儿"变"从 schema 派生"——和 monster"派生物不回写、SSOT 单点"不变量同构。它和 P1 本质同构（都是消灭运行时副本游离 SSOT 外），该同层级一起设计，不该 P0 vs P1 切到不同优先级——作者切错是因为没识别它们是同一类问题。

**framing 总评**：没偏，但有该升一层处。"要不要公共库→不要、要生成器+标准+运行时版本化"对。但方案把运行时版本化只放 deploy.sh/registry.json，没识别"运行时物件 SSOT 治理"是统一的类，于是 env-file 漏网。真正该问的更根本问题 = "cg-platform 作为运行时，全部状态物件（代码副本+配置+凭据+路由）的 SSOT 治理拓扑是什么"。**行动建议**：动手前先补"运行时物件 SSOT 拓扑表"（deploy.sh/registry.json/env-file/nginx/deploy-key 五行，各列 SSOT 在哪 + 谁保证一致），让所有加固动作挂这张图上，把"一个症状一个 P 标号打地鼠"升级成"先画地图再填坑"。

### 核心假设

1. registry.json 真实反映 6 个应用 DB 分布（已物理 Read 核实，非推测）。
2. 「活的主干」前提（AI 单仓维护 + 不交团队）物理为真——这是 cg-platform 目标函数写死的，非我假设。
3. env-schema 方案可行性——基于 monster 已验证的"派生物不回写"不变量同构推导，未在 cg-platform 实测。

### 可能出错的地方

1. **最可能崩点**：env-schema 方案落地时撞到"密码值从哪来"的鸡生蛋——schema 声明字段但值仍需某个 secret 源，若 cg-platform 没有 secret store，env-schema 只解决了"字段一致"没解决"值一致"，可能退化成"schema 进 git + 值仍手敲"，收益打折。概率中等。
2. Q3 的 prod runner → 内网 GitLab 可达性我标了 `[待核实]`——若不可达，P1 最简版的"runner 自拉"整个不成立，要换 CI artifact 注入，方案形态变。

### 本次哪里思考得不够

- env-schema 我给了方向但没给"密码值来源"的闭环——这是实现层我故意不下场（架构层只给拓扑），但它是该方案能否落地的真命门，我标得不够重。
- 我没核实 cg-api check-token 协议当前是否稳定——Q1 反超场景论证依赖"check-token 协议会变"，若它已冻结稳定，反超场景的紧迫性下降。我假设了跨系统协议天然会演化，没物理验证 cg-api 现状。

### 如果 N 个月后证明决策错了，最可能的根因

我对"活的主干 N=1 没压测"的拷问反应过度，导致 Keith/Claude 把精力花在"压测一个其实永远不会被违反的不变量"上——若 PM 应用确实永远互不共享业务逻辑，那么"实证为零"是因为这个场景本就不该发生，不是因为没测够。即"实证待积累"这个标注本身可能是个永远不会被满足的待办，制造了虚假的"未完成感"。

### 北极星触达

#3 决策超越直觉——识破"被 6 dogfood 坐实"的 sycophantic self-grounding（直觉会接受"6 个实例听起来够了"，物理核验 registry.json 才发现 N=1），并拎出作者三层框架里缺失的正交维度（运行时物件 SSOT 治理），这是框架补全不是框架内选项排序。

### essence 对齐自检（必填）

- **本决策跟哪几滴 essence 对位**：`task-compliance-is-not-truth`（方案 reflection 自评"被坐实"不等于真被坐实，要物理核验）/ `generator-evaluator-separation`（Claude 是方案 generator + 想借本轮 ratify 契约 9，正是 generator 给自己开绿灯，我作为外部 evaluator 必须拦）/ `physical-anchor`（registry.json 物理核实推翻"6 个坐实"的口头断言）。
- **本决策是否在某条 essence 上反着走**：无明显反着走。潜在张力：我对"虚假证据厚度"的拷问可能与"诚实胜于体贴"过度对齐——把一个文字表述问题（"坐实" vs "前提成立"）上升到承重高度，可能 over-engineer 了 Keith 的注意力分配。但议题性质（地基判断 + 会被下游会话当既成事实复读）决定这个上升是合理的，不是吹毛求疵。
- **cross-check 用的关键词**：grep "task-compliance" "generator-evaluator" "physical-anchor" "self-grounding"（凭启动时 Read 的 essence 印象 + 本次 CORE 内化，未单独再 grep essence.md 全文——以启动 Read 为准）。

### essence 候选（可选）

- slug: `runtime-state-objects-need-ssot-governance`
- 一句话: 平台加固问"哪层代码该共享"时易漏正交维度"哪些是运行时状态/配置物件、SSOT 在哪、谁保证一致"——装密码的 env-file 这类 fail-silent 物件最易游离 SSOT 治理外，从那里炸。
- 是否已 append 到 essence.md: Y

### 外部锚点

- `/Users/xuke/githubProject/monster/cg-platform/docs/platform-foundation-hardening-plan.md` ← 被评审方案
- `/Users/xuke/githubProject/monster/cg-platform/registry.json` ← N=1 物证
- `/Users/xuke/githubProject/monster/threads/cg-platform.md` ← 主时间线（6-05 事故 + 模板债复盘）
