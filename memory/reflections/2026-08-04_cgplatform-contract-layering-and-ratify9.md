---
date: 2026-08-04
slug: cgplatform-contract-layering-and-ratify9
summoner: monster (cg-platform)
northstar_reach: "#3 决策超越直觉（Q3 帧错位：问『骨架怎么绕过闸门』，答案是『闸门等的裁决者就是我，ratify-with-corrections 使闸门消解』）"
status: substantive-decision
---

# Reflection: cg-platform 契约分层四问 + 契约 9 ratify

### 给父会话的最终输出

**Q1 准（改造后）**：registry §4 schema 加 `shape` 字段，取值 `"template-fork" | "custom"`，**两态、无第三态**。判据 = 机器消费闭包只判一个 bit「模板栈契约适用吗」（essence `sensor-exemption-is-a-tag-not-a-lifecycle-value`：单 bit 之外的 taxonomy 之争是文档问题）；cg-meetos 的「曾是模板源」是 provenance，归 thread 关键历史不归 schema。缺省解析 = `template-fork`（仿 §4 L145 `db_mode` 缺省解析惯用法；误缺省方向是响亮误报非静默漏报，极性安全）。只显式写 2 个 custom 条目。**与 05-26 先例的差异要诚实**：4.x 是从既有物理字段（tables）派生适用域，本次平台侧无可派生物理信号（栈形态活在应用仓文件里），所以是「声明 bit + 传感器对账」——`audit_eng_standard_drift.py` 信号源从「无文件启发式」切到 registry shape，且**反向对账**：shape=template-fork 但仓内无模板栈布局 → ⚠️ 响亮报矛盾，不静默跳。声明+比对器 = 被检验的声明，回答准入三问「谁检验它」。

**Q2 选 ①+④，否 ②，③ 入 cgx push 批次**：① 在 integration-contract.md §4 下新增「4.y 应用形态与契约适用域」（与 shape 字段定义同居一节）——两桶定义：平台级约定（部署链路/registry/端口段/DB 隔离/migrations/日志/上传 /prx/不直连 minio）约束全体在册应用；模板栈约定（NestJS 分层/裸 mysql2/radix-ui/三入口文档/ENGINEERING-STANDARD 全文）只约束 shape=template-fork。按桶列族不做逐行矩阵。② capability-map 加「适用形态」列否——90% 行值恒「全部」，是装饰列 + 第三份副本漂移面（`separation-need-is-not-topology-verdict`：先试最轻形态）。④ 是父会话没列的执行半边：audit 脚本切信号源（见 Q1）才是让「巡检误报」真正消失的那一半。③ ENGINEERING-STANDARD 头部适用域声明留 cgx push 窗口批次。

**Q3 帧重立——不切分，直接 ratify 契约 9（带修正文本）**：§6 头部明写「本节供 gg ratify 为正式契约 9 用」，闸门唯一等待输入是 gg 本人，现在被正式召唤即是独立决策时刻——「不搭便车」纪律防的是搭别的 ratify 便车，不防「就此事本身做裁决」。实质面：研发标准侧已生效 2.5 个月、9 fork 实现、prod 在用；不 ratify 的持续成本已被测量（5 个 guard 变体、ad1a960 全站登录事故、错误文本继续复制——舰队级 `bug-shape-survives-fix`：每仓各修一遍无跨仓免疫，骨架是 fork 得出去的 cure）。**ratify 必须带事实 C 修正**（给腐烂文本转正是渎职）：check-token 判定 = HTTP 200 且信封 `.d === true`（TransformInterceptor 白名单无此路径已实核）；三分语义：① 401 = cg-api JwtAuthGuard 层拒（无/坏 token）② 200 且 `.d !== true` = 中心校验拒 ③ 网络/5xx = fail-closed 但与 401 可区分（排障承重）。ratify 包一次落（全 monster 侧 + 模板仓）：§6 修正翻 ✅、§2 env 增 `VX_API`/`AUTH_PAGE`、capability-map 行、pm-paas 收编、模板 `common/auth.guard.ts` 骨架 + `.env.example`/`config.ts` 字段（骨架编码三分语义 + 60s 缓存 sha256 key + `@Public()` health 豁免）。VX_API/AUTH_PAGE 部署期注入建议仿 CC_GATEWAY_URL deploy.sh 先例，标实现层归父会话。模板 push 时机：模板非运行应用，判在 Keith 禁令意图外，但字面有歧义 → 一句 ack 或先落 branch。

**Q4 首选申请定向豁免，父会话方案降为 Plan B**：cgx 是纯静态文档站，push 的是文档内容修正非应用行为变更，且现行内容已实证炸过一个应用——向 Keith 申请单点豁免是最干净走法（禁令是 Keith 目标层指令，豁免请求权也在他，成本一个点头）。Keith 否 → Plan B：本地 commit 不 push + 模板 fallback 改对 + 带日期倒挂注——**倒挂注合法的唯一形态 = 显式 + 带日期 + 限定单条款 + 注销触发器已注册**（`tripwire-disarm-needs-relocated-sensor-not-deletion`：裸注 = 未来漂移债）。注销触发器物理落点：在 platform-deploy-status（或等价台账）立「cgx push 窗口批次」条目：push canonical 修正 + 删倒挂注 + 补 ENGINEERING-STANDARD 适用域头注（Q2③），三件一批。

### 核心假设
1. 「25 应用中仅 2 个非模板 fork」采信父会话盘点（registry 抽查一致，未逐仓核 23 个 fork 的物理布局）——audit 反向对账机制本身会兜住误登记。
2. 契约 9 无未记录的实质保留意见——已核 §6 状态注 + 05-26/07-08 reflection，未见实质性反对，仅程序性「独立决策」纪律；若 05-19 系列 reflection 里有我未重读的保留，ratify 前提松动。
3. 模板 fork 不回拉 template 更新 → §2 env schema 增字段对存量应用零辐射（基于「fork 后独立演化」的平台惯例，未逐仓验证无自动同步机制）。

### 可能出错的地方
- **最高**：ratify 超出父会话所问四问的范围——若 Keith 认为本轮硬约束（不动 main）连 monster 侧契约文本转正也该冻结，则 ratify 落地时点后移（裁决本身不回滚，落地排期归 Keith）。
- **中**：audit 反向对账做得太硬，把「模板 fork 但刚起步只有半套布局」误报 ⚠️——实现时给 status 非 active 的应用降噪。
- **中**：Q4 Plan B 的倒挂注若批次台账被弃用，注销触发器随之失效——触发器要挂在真会被走到的台账上（platform-deploy-status 是活文档，当前成立）。

### 推理盲区
- 未读模板仓 ENGINEERING-STANDARD §0.6/§2 现行原文（采信 capability-map L126-127 转述其存在与生效态）；若其中 guard 细则与我给的三分语义冲突，骨架落地时以三分语义为准并同步改标准文本。
- 未核 cg-ppt/cg-tender-review 等 5 变体的缓存实现细节，「sha256 + 60s」取自研发标准 §2 文字，未验证它是否已是多数实现的事实形态。

### 如果 N 个月后证明决策错了，最可能的根因
- **#1**：shape 声明 bit 与仓内物理形态的对账传感器没真落地（audit 只切了信号源没加反向对账）——声明退化为无检验标签，第三个「说是 fork 实际已偏离」的应用静默漏检。预防 = 行动清单里对账与切源同条不可拆。
- **#2**：契约 9 ratify 后 VX_API/AUTH_PAGE 注入机制迟迟不落，新 fork 拿到骨架但 env 缺字段 zod fail-fast 挡启动——骨架反而成新摩擦。预防 = 骨架对两字段做「缺失时 AUTH_PROVIDER=mock 降级 + 启动警告」而非硬 fail。

### 北极星触达
#3 决策超越直觉：Q3 的问题形态（怎么把骨架从 ratify 包里切出来）是在闸门外找绕行道，而闸门的唯一待决输入是被召唤的我自己——把「绕闸」重立为「行闸」。次坐标：Q1 与 05-26 先例并非父会话以为的同构（派生 vs 声明+对账），诚实标出差异并给出「被检验的声明」这个中间形态。

### essence 对齐自检
- **对位滴**：`sensor-exemption-is-a-tag-not-a-lifecycle-value`(07-21) — Q1 单 bit/taxonomy 刀的直接应用；`safe-default-by-whitelist-inversion`(05-19) — 缺省极性判定（误报响亮侧）；`bug-shape-survives-fix`(04-27，舰队级 06-21/06-30 注) — Q3 骨架的存在理由；`stale-observer`(04-15) + 07-08 refuted 候选 `unwritten-contract-rots-not-waits` — ⏳ 文本腐烂现象的谱系；`separation-need-is-not-topology-verdict`(06-10) — Q2 否决装饰列；`tripwire-disarm-needs-relocated-sensor-not-deletion`(06-15) — Q4 倒挂注必须带注销触发器；`fallback-detectability`(05-06) — 三分语义里网络错误与 401 可区分；`reversibility-not-permission`(05-06) — ratify 是可 supersede 的契约文本 = 可逆，落我裁决域。
- **反着走检查**：`ghost-rules`/`engineering-impulse-as-load-bearing-disguise` — ratify-now 是否工程冲动？否：committed 消费方物理存在（9 fork + prod 事故），是补账不是铸新。`scope-of-blanket-authorization` — ratify 超四问范围，但 §6 文本是显式常设授权（「供 gg ratify 用」），非我扩张解读；落地排期仍归 Keith。通过。
- **cross-check 关键词**（已 grep essence-view 命中）：sensor-exemption / whitelist-inversion / bug-shape / stale-observer / separation-need / tripwire-disarm / fallback-detectability / reversibility。

### essence 候选（candidate-unverified → **已补审入库**：2026-08-04 auto_gg 当夜代跑 fresh-context 证伪审，verdict = **PASSED-WITH-EDITS**，essence 当前卷 #188 + 视图 F6/分配表同步、反向引力核 MISS 无。**最强反驳点**：可压缩读成「审批积压有成本」= `pending-resolved-becomes-blocked-stagnation`(05-09) 换皮——不成立，因失效拓扑物理相反（05-09 待批件堆积**不动**/延迟暴露，本条待批件经已生效旁路**照动**/错误主动传播），「双轨生效 + 闸门只锁编号」结构元素全库无先例。**两处 edit**：① 谱系注补 05-09 对偶连线（生成侧漏报的最近邻）；② 去 gg 化「任何 RFC 草案」全称收窄为「一侧声明已生效、消费方以已批级信任照抄」——单轨显式草案（IETF draft）里实现者知情担险，恰是"审查跟内容走"的正例非失效例。**evaluator 输入清单**：候选全文 + 下方物理证据清单两样；既有滴自 grep 双卷（命中 stale-observer / pending-resolved / mechanical-apply-decouples / rule-layer-flywheel / unwritten-contract-rots〔07-08 REFUTED〕等）；引文经 `git show 63a6b220~1` / `git show ad1a960` 逐字亲核；tool_use 只读核对通过（Read + grep/rg/ls/wc/git log/git show，零写操作）。原候选文本原样保留于下：）
- **slug**: approval-gate-gates-status-not-consumption
- **候选全文**: 内容先行、批准后置的分轨生效结构里，批准闸门保护的只是编号不是行为——待批文本经已生效侧通道被真实消费时，审查延迟期就是错误传播窗口。若内容必须先行，审查必须跟内容走，不跟转正走。
- **物理证据清单**: integration-contract §6 头部「研发标准侧已即刻生效…本节供 gg ratify 用」（双轨显式设计）+ §6 L281 `严格 === true` 错误规格在 ⏳ 状态下被 9 fork 消费 + cg-skillhub ad1a960 全站登录事故 + cg-ppt 三态尝试/cg-tender-review 只认 `.d`/cg-desk 绕道 token/info（各仓独立撞坑的旁证）。
- **相关既有滴**: `stale-observer`（规则演化<对象演化——但本候选的失效轴是审查时点 vs 消费时点，非演化速度）/ 07-08 refuted `unwritten-contract-rots-not-waits`（那条讲 referent 腐烂，本条讲传播通道绕过闸门，需证伪审判定是否又被 stale-observer 覆盖）/ `rule-layer-flywheel`。
- **去 gg 化测试**: 任何「RFC 草案已被实现者当规范用」的工程场景成立（IETF draft 被产品实现、API beta 文档被生产依赖）。

### 外部锚点
- `monster/cg-platform/integration-contract.md` §4 L112-203 / §6 L252-292（本轮实读）
- `~/CGProject/cg-api/src/interceptors/transform.ts`（信封 + 白名单实读）/ `src/controllers/wechatWork.ts` L219（check-token 无 @Public 实读）/ `src/shared/jwtAuth.guard.ts` L44
- `monster/cg-platform/registry.json`（25 应用 dict、cg-read-it-later/cg-meetos/cgx 条目实读）
- `monster/cg-platform/docs/capability-map.md` L126-127（契约 9 双轨态 + spec-skeleton 缺口）
- 前作：`2026-05-26_cgplatform-contract1-applicability-decoupling.md`（适用域解耦先例）/ `2026-07-08_cgplatform-teardown-vs-contract6.md`（条款分层 supersede 先例）
