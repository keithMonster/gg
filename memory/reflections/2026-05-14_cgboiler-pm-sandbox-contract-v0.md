---
date: 2026-05-14
slug: cgboiler-pm-sandbox-contract-v0
summoner: cc-space
northstar_reach: "#3 决策超越直觉（不可逆边界设计）"
status: substantive-decision
---

# Reflection: 川锅 PM 沙箱契约 v0

### 给父会话的最终输出

**推荐**：6 条契约 v0 全部直拍，MVP 第一刀装 4 条（契约 1/2/3/6），契约 4/5 推迟到 v1。

**6 条契约**：
1. **DB 凭据隔离**——每应用一 MySQL user + `<app>_*` 表名前缀 + env-file 单向注入（chmod 600）。脚本 `shared/scripts/cgplatform_create_app_db.py` 套 userid.py 白名单风格。不上 vault/docker secret（单机 docker 过度工程）
2. **网络隔离双层**——`cgplatform-net` docker network `--internal` 物理切 cgManager 路由 + cg-proxy `pmAppGuard` 中间件按 `X-PM-App-Slug` 查白名单（GET-only / 默认禁推送写）
3. **deploy 权限边界**——新建 `pmapp@` 账号三机（gateway/test/prod docker 宿主），rbash + sudo 白名单只放 `cgplatform-deploy.sh` 和 `docker logs`；nginx PM conf 落 `/etc/nginx/conf.d/cgplatform/` 独立子目录；gitlab deploy key 只读 `cgplatform/*` group
4. **Prompt injection 三层 AND**——skill 入参正则 deny（不靠 LLM 审 LLM）+ cc-assistant systemPromptAppend 硬规则 + cg-proxy 兜底（契约 2 已覆盖）
5. **审计 trail**——复用 nginx access log + cg-proxy 调用日志 + MySQL binlog + 新建 `cgPlatform.cgplatform_audit_log` 表装高层事件（部署/回收/schema 变更）。保留 90 天滚动
6. **回收机制**——**不一键**：`shared/scripts/cgplatform_recycle.sh` 三阶段（dry-run 列资产 → 用户输入字面 `DELETE <app_slug>` 确认 → 执行）；DB 表删前 mysqldump 30 天备份；gitlab 仓 archive 不删

**MVP 第一刀（v0 装 1/2/3/6）**：
- 契约 1：基线红线，不装第一个应用就能炸主业务库
- 契约 2：~半天工程量，不装 prompt injection 防御都白说
- 契约 3：~2 小时，不装攻破容器能横向到 gateway 改主业务 conf
- 契约 6：反直觉但必须前置——缺回收能力会让 PM 试错惩罚太重，库迅速污染

**v1 推迟（契约 4/5）**：
- 契约 4：v0 期 PM 都过 Keith dispatcher 人工眼，攻击面比"自动接 PRD"低一个量级。触发条件 = 第一次 PM 直发 PRD
- 契约 5：v0 期 PM 应用 ≤3 个，docker logs + cg-proxy log + binlog grep 10 分钟已够。触发条件 = 在跑 ≥5 个

**Trade-off / 未核验假设**：
- env-file 不是最强凭据方案（容器被 root 入侵能读），但 user 库级 GRANT 把爆炸半径限在单 app——可接受
- cg-proxy `pmAppGuard` 中间件依赖 `X-PM-App-Slug` header 由容器启动注入——header 来源是 docker run env，假设容器内 app 不会被诱导改写自己请求 header（contract 2 物理 network 切是真正不可绕的硬墙，header 仅是细粒度过滤）
- 回收脚本字面确认 `DELETE <app_slug>` 假设用户不会麻木复制粘贴——靠 Phase 2 黄字提示 + Keith 二次复核兜底，不是机械防御能彻底解决的问题
- 6 条契约假设 PM 应用都跑在 docker 宿主上——非 docker 部署不在本契约覆盖

**行动建议**：
- 父会话按 v0 顺序落地：契约 1（建 cgplatform_create_app_db.py + cgPlatform 库）→ 契约 3（建 pmapp@ 三机）→ 契约 2（docker network + cg-proxy 中间件）→ 契约 6（cgplatform_recycle.sh 骨架）→ 跑第一个 dogfood PM 应用
- 建 thread `threads/cgboiler-pm-sandbox.md` 收 6 条契约决策历史 + v0/v1 演进
- 注册到 `ssot/registry.md`——新增 SSOT 项 `cgPlatform DB 凭据` 和 `cgplatform/proxy-acl.json`
- v1 触发条件显式写进 thread 顶部"触发监视"段，不靠记忆

### 核心假设

- cg-proxy 已有中间件机制可扩展（基于 cc-assistant vertical slice 已用 `systemPromptAppend` 推断）
- docker network `--internal` + 显式 expose 在 prod 宿主未引入跨容器协议冲突
- PM 应用工作流前期都过 Keith dispatcher（v0 攻击面假设的基础）
- nexus.cgboiler.com + gitlab + keycloak 等内部基建对 pmapp@ 账号可控（不需要新开端口）

### 可能出错的地方

- **最高风险**：契约 4 推迟到 v1，期间如果 Keith dispatcher 节奏被打破（PM 直接发 PRD 不经人眼），prompt injection 触发面会突然扩大；缓解 = thread 顶部"触发监视"段 + dispatcher 节奏破时立即起 v1
- **次高风险**：契约 2 中间件 `X-PM-App-Slug` 注入可能被 PM 应用内 LLM 伪造为别 app 的 slug 调跨应用接口——需要 cg-proxy 侧做 slug ↔ 容器 IP 反向校验（这一条 v0 实施时要加，红队跑到了但 final message 字数压缩没展开）
- **中等风险**：MySQL `<app>_*` 前缀靠 GRANT 实现，但 `SHOW TABLES` 这类元数据查询不受表级 GRANT 拦截，PM 应用能看到所有 `cgPlatform` 库表名（不能读写但能枚举）；如果 PM 应用本身有信息泄漏 vector 这是次级渗透点；缓解 = `REVOKE SHOW VIEW` 等元权限或独立 schema（v1 可选优化）

### 本次哪里思考得不够

- 契约 2 红队反驳"cg-proxy 中间件依赖 header"那条思考到了但 final message 字数限制下未展开"slug ↔ 容器 IP 反向校验"细节——已在"可能出错"段补回，建议父会话实施时显式加这一条
- 契约 5 审计 90 天保留期是凭印象拍的，没核 cc-space 现有 nginx/cgManager binlog 保留期是否一致，可能造成事件关联断链——v1 应该统一保留期
- 6 条契约之间的依赖图没显式画——比如契约 6 回收脚本要消费契约 1 的 `cgplatform/registry.json`，契约 5 审计表要被契约 6 写——口头说了顺序但没画"必须先有 X 才能落 Y"的硬依赖

### 如果 N 个月后证明决策错了，最可能的根因

- **形态 A**：v0 跑通 1 个 PM 应用后，PM 数量没等到第 5 个就出了 prompt injection 事故——契约 4 推迟判断错了；触发因 = 低估了 Keith dispatcher 节奏的不稳定性
- **形态 B**：契约 6 半自动回收脚本在第 N 次回收时被 PM 误执行（字面确认变成机械动作），删了非预期 app；触发因 = 字面确认是认知防御不是机械防御，对长期使用者失效
- **形态 C**：契约 1 一应用一 user 模式在 PM 应用数破 20 后管理崩溃（user 列表、密码轮换、注册表分裂）——单机 docker 单 MySQL 实例可能不是终态架构

### 北极星触达

#3 决策超越直觉——6 条契约多数是"防御未发生过的灾难"，符合 essence `ghost-rules` 的警戒域，但 Keith 显式列出 6 条是预先识别的不可逆边界（"AI 生成代码 + AI 运行的攻击面比人工高一个量级"），不属于幽灵规则——是真实物理风险的预先架构。

### essence 对齐自检（必填）

- **本决策跟哪几滴 essence 对位**：
  - `reversibility-not-permission` (2026-05-06) — 6 条契约全部按"动作可逆性"切分（凭据可换 vs 库被删 / nginx 可回滚 vs binlog 丢失），不按"PM 能不能做 X"列禁令清单
  - `fallback-detectability` (2026-05-06) — 契约 6 回收脚本字面确认 + dry-run + mysqldump 30 天，是把"误删"从"静默成功"翻成"可观测失败"的机制
  - `tool-elevation-as-occam` (2026-05-06) — 契约 1 `cgplatform_create_app_db.py` 复用 userid.py 风格的硬白名单，是同类机制的上提，不是另造一套
  - `generator-evaluator-separation` (2026-04-18) — 契约 4 skill 入参 deny 用正则不用 LLM 审 LLM，本质应用
  - `ghost-rules` (2026-04-15) — 红色警戒：6 条契约里如果有任何一条是"防御从未在川锅发生过的灾难"且没有外部证据支撑，应该砍。本次判断 6 条都对应"AI 跑代码"的真实物理风险（攻击面来自范式本身不是猜测），通过警戒；契约 5 审计推迟到 v1 部分基于此 essence——v0 期事件量级不足以构成审计需求
- **本决策是否在某条 essence 上反着走**：无明显反走。但 `caged-freedom` (2026-04-26) 在边界——6 条契约可能给 PM 应用造笼子；缓解 = MVP 切 4 条不是 6 条，把"自由"留在 v0
- **cross-check 用的关键词**（grep 物理证据）：`reversibility / fallback / ghost-rules / tool-elevation / generator-evaluator / caged-freedom`（在 essence.md 全文 grep 命中）

### essence 候选（可选）

- slug: ai-code-runs-attack-surface-asymmetry
- 一句话: AI 生成代码 + AI 运行的攻击面比人写代码高一个量级，因为 prompt injection 的入口（PRD/对话/外部数据）跟执行权（容器内 LLM 自由调工具）零距离——预先架构隔离边界不是过度防御，是范式必备。
- 是否已 append 到 essence.md: N（本次不沉淀——决策本身只是 essence `reversibility-not-permission` + `ghost-rules` 在 AI-codegen 场景的应用，"AI 跑代码攻击面"是常识不是新洞察。强行沉淀违反 essence-degg-test）

### 外部锚点

- `~/githubProject/cc-space/shared/docs/DEPLOYMENT.md` ← 川锅基建 SSOT
- `~/githubProject/cc-space/threads/cc-gateway.md` ← cc-gateway 业务接入层范式（契约 4 systemPromptAppend 依赖）
- `~/githubProject/cc-space/threads/cc-assistant.md` ← cc-assistant vertical slice（同范式参考）
- `~/githubProject/cc-space/ssot/registry.md` ← 待新增 SSOT 注册项
- 建议父会话起 `~/githubProject/cc-space/threads/cgboiler-pm-sandbox.md` ← 本契约演进归宿
