---
date: 2026-06-30
slug: cgplatform-selfserve-migration-signal
summoner: monster / cg-platform
northstar_reach: n/a 非北极星触发（架构层 deploy 契约裁决，服务 Keith 当前战场）
status: substantive-decision
---

# Reflection: cg-platform self_serve 凭据迁移信号选型（A/B/C）

## §A 范式 A — 决策的元属性反思

### 给父会话的最终输出（必填）

**推荐：选 A（物理信号），但改正实现位置——不在行 96 的 DATASOURCE 派生处读 config.env，而在 PYDS 注入守卫处（行 335，config.env 已 cat 的同一上下文）加 config.env-aware 跳过。并把信号统一到所有路径（不只 self_serve）。**

**核心理由（三层）**：
1. **A 的信号 = 数据本身，零背离面**。去中心化的本质就是"config.env 成为 DB 凭据的 SSOT"，所以"是否已迁"严格等价于"config.env 是否真的含 DB 凭据"。A 直接读这个事实，信号即数据，物理上无法背离（`physical-anchor`）。B（registry 标记）、C（datasources.json 键）都引入一个**与数据分离、需手工同步的第二标记**，背离面 = 那个手工同步步骤。
2. **A 不是新机制，是消除不一致**。PYSEC（secrets map 注入，行 360）**已经**是 config.env-aware 的——它跳过 config.env 已提供的字段；只有 PYDS（DB 字典）不 aware，靠"最后注入"无条件赢。A 就是让 PYDS 和 PYSEC 一样尊重 config.env。这把 A 从"加一个 config.env 读"降级为"补一个不对称 bug"，且复用 PYSEC 已有的 CONFIG_FILE 入参，零新数据依赖。
3. **A 在 Keith 担心的"静默"轴上反而比 C 更安全**。C 的真实静默失败：写了 config.env 但忘删字典键 → 字典旧值仍赢 → 若是为轮换密码而迁，就部署了旧密码、迁移静默不生效。A 没有这个模式——写 config.env 那一刻它就赢，迁移与"写凭据"原子绑定。

**Keith 四问的答复**：
- **① 选哪个**：A，且实现位置从行 96 移到 PYDS 注入守卫（关键修正，见下 trade-off）。
- **② A 读 config.env 的隐患**：唯一能让 A 出问题的是"config.env 含非空但错误的 DB_PASSWORD" → 跳字典 → 用错凭据 → `health db:false` → 蓝绿回滚 → pipeline 红。**响应是大声的，由整个 lazy/N抄方案本就依赖的同一个 health 传感器兜底（§6 gg盲区6）**。A 不引入任何该传感器覆盖不到的新失败模式。空占位（scaffold 的 `DB_PASSWORD=`）因"非空"判据正确 fall through 到字典。
- **③ 信号统一**：统一，且 A 天然统一——把守卫做成"config.env 含非空 DB_PASSWORD 就跳字典"，与 DATASOURCE 怎么派生（self_serve 派生 / datasource 显式 / test_datasource legacy）无关。一个物理信号覆盖全部迁移路径（新 self_serve onboard / lazy self_serve / lazy 共享源 / lazy legacy）。**不要为"统一"加 registry flag（那是 B）——B 给一个过渡态加永久 schema，迁完后全等于 "config" = 死字段。**
- **④ cg-aps 当靶子**：合理，零 prod 风险（test-only），且精确演练 lazy 自迁 + A 的守卫翻转。**但要点明它只验 deploy.sh 半边，不覆盖 create_app_db.py 新 onboard 写 config.env 那半边**（那半仍按 §0 point3 挂账待真 onboard）。补一个 cg-ppt test 回归验证——它是唯一已写过 config.env 的应用，A 落地后会把它从"字典赢"切到"config 赢"，重部署确认 green。

**行动建议**：
1. 改 deploy.sh PYDS 注入守卫：`if [ -n "$DATASOURCE" ]` → 增加 "config.env 无非空 DB_PASSWORD" 条件（grep CONFIG_FILE）；config.env 有 DB_PASSWORD 时 echo 一句"config.env owns DB creds, skip dict"。不动行 96 派生、不动行 147 heredoc 变量串、不动 registry schema。契约 7 最小面。
2. 改完必跑 `sync-deploy-tooling.sh both`。
3. cg-aps test 端到端验证：写 config.test.env 的 DB_* → 部署 → 断言部署日志中 DATASOURCE 注入块被跳过（"DB 凭据已从字典注入"echo 缺席）+ `health db:true`。这比 C 更强——可在字典键仍存在的情况下验证 config.env 单独足以翻转。
4. cg-ppt test 回归重部署，确认切到 config-sourced 后仍 green。
5. drift_audit.py 已按 §3c 读 config.env，无需额外改；create_app_db.py 仍挂账。

### 核心假设
- deploy.sh 中 config.env（`\$CONFIG_FILE`）、datasources.json、secrets.json 在行 333/337/360 是**同一个执行上下文**（代码可见三者同在转义 heredoc 段），故把 A 放注入守卫处 config.env 必然可用——绕开行 96 本地/远端拓扑不确定性。
- health db:false → 蓝绿回滚 → pipeline 红这条传感器对"错凭据"可靠触发（§6 已 Keith 知情接受为 lazy 方案的兜底）。

### 可能出错的地方
- 若 deploy.sh 实际拓扑里行 333 的 config.env cat 与行 337 的 PYDS 不在同一 shell 上下文（我从转义符推断同上下文，未逐行通读 269–334），守卫放置点要再确认。概率低但这是 A 实现的唯一硬前提，Keith 落地前用一次实读确认 CONFIG_FILE 在 PYDS 守卫处可见即可。

### 本次哪里思考得不够
- 没读 deploy.sh 行 123–315 全文，对 runner/target-host 二级 ssh 拓扑是从 `\$` 转义模式推断的，非实证。结论不依赖该拓扑细节（守卫放 config.env-cat 同段即可），但 Keith 落地时该实读确认一次。
- 没核 cg-ppt test 当前 datasources.test.json[cg-ppt] 条目是否仍在 —— 若已删，cg-ppt test 今天就已 config-sourced，回归验证退化为纯确认。

### 如果 N 个月后证明决策错了，最可能的根因
config.env 含 DB_PASSWORD 成为"已迁"信号后，某个非 self_serve、用共享源 cgdata 的应用，其 config.env 因无关原因混入了 DB_PASSWORD（命名撞车）→ 被误判已迁 → 跳共享源注入。缓解：共享源应用的 config.env 本不该有自有 DB_PASSWORD；真撞了也是 health 红。但这是 A 全局化（不限 self_serve）后理论上唯一的误判面。

### 北极星触达
n/a —— 架构层 deploy 契约裁决，服务 Keith 当前战场（cg-platform 去中心化收尾），非三北极星直接触达。

### essence 对齐自检（必填）
- **对位 slug**：`physical-anchor`（A 把信号锚到物理事实=config.env 真有没有密码，非声明意图）/ `ssot-distillation-vs-buffering`（B/C 的分离标记 = 软缓冲层，漂移温床）/ `invariance-allocation`（A 选"config.env 拥有凭据"为不变性锚点，B/C 选一个需手工同步的标记）/ `reversibility-not-permission`（弱相关：A 的误判由可逆 health 传感器兜底）。
- **是否反着走**：潜在张力 with `premature-abstraction-tripwire` —— 有人可能说"A 把检查全局化（不限 self_serve）是过度设计"。但全局化不增代码（同一守卫），反而消除 per-path 特例，是 OCCAM 不是抽象膨胀，不构成反走。
- **cross-check 关键词**：grep 了 essence 1–424 行 + 凭"physical-anchor / ssot / invariance / reversibility / occam" 语义检索。

### essence 候选（可选）
- slug: signal-as-data-vs-separate-marker
- 一句话: 迁移/状态信号若等于数据本身（读源头），零背离面；若是与数据分离需手工同步的第二标记，背离面 = 那个同步步骤——分离标记的"显式自描述"优点常被它与数据漂移的代价吃掉。
- 是否已 append 到 essence.md: N（留 Keith review 后定；本滴有去 gg 化重量，倾向沉淀）

### 外部锚点（可选）
- `~/githubProject/monster/cg-platform/docs/secrets-decentralize-plan.md` §0 / §3c ← 方案底稿
- `~/githubProject/monster/cg-platform/cg-platform-deploy.sh` 行 96–110 / 330–353 ← 改动靶点
