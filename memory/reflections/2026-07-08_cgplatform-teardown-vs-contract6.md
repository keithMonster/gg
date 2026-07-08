---
date: 2026-07-08
slug: cgplatform-teardown-vs-contract6
summoner: monster (cg-platform)
northstar_reach: "#3 决策超越直觉（骨架未写契约的条款分层 supersede 判定）"
status: substantive-decision
---

# Reflection: cg-platform teardown 与契约 6 的冲突裁定

### 给父会话的最终输出

**元判断（贯穿 5 条）**：契约 6 是 2026-05-14「骨架未写」的 v0 设计，它是一次**低终态可见度下的按终态走**（essence `terminus-walk-needs-terminus-visibility`）——单环境、pre-onboard、pre-self_serve 的假设下预判了一个删除工具的形状。14 个月演化（双环境双 runner / --internal 消解 / self_serve 自治建表 / migrations 通道 / 凭据去中心化）之后，契约 6 的条款要**分层**：编码"不变量"的存活（要物理确认销毁、要删账号和 env-file），编码"当年终态假设"的被 supersede（archive-for-recovery / 30天备份 / 三阶段仪式）。而且——**连存活的那条也命名了已消失的对象**（dev_ro 在 self_serve 下从不存在）。

**裁定 1 · 命名 → `cg_platform_recycle.py`（改名对齐，非保留 teardown）**
`cg_platform_recycle` 已在 3 处注册为该角色的 snake_case 标识符（CLAUDE.md 命名边界段列为「统一新名」/ SKILL line356 / 契约 6）。自造 `teardown` = 制造命名漂移，正是 monster SSOT/concepts 纪律要防的（authoring-handbook「缺路由假地图」：有人 grep `recycle` 三处引用找不到 → 以为没建）。脚本刚写、无消费者，改名成本近零、收益是补活三个死指针。语义差异（真删 vs archive）是**工具的参数**（裁定 2 管），不是另起名的理由——工具角色是"退役一个应用"，其 GitLab 默认行为正交于命名。`.py` 对（onboard 生态全 python，契约文字的 .sh 是 pre-python 遗留）。

**裁定 2 · GitLab → 默认 delete（Keith 批的真删对），保留 `--archive-repo` 逃生口**
契约 6「archive 不删」2026-07 部分失效——它假设的语义是"回收=保留可复用资源"，被两个演化事实 supersede：① 删重建同 slug 是真实工作流（前两次改名都是删重建），archive 让 GitLab path 被占，重建撞 409（SKILL 错误矩阵 line349 正是此坑）；② delete 自带 pending-deletion 软窗口（脚本已 202→404 轮询），本身有恢复缓冲；③ 真删的取证损失被"本地仓也 rm + thread 归档"兜住。archive 保留的价值（commit 史取证 + 可 unarchive）只对**成熟应用退役**成立，对 db:null 骨架重建近零——故保留 `--archive-repo` flag 给前者，默认 delete 给后者（高频主路径）。

**裁定 3 · mysqldump → 完整 30天备份子系统不落；--drop-data 路径落单文件 dump-before-drop**
契约 6「删前 mysqldump 30天备份」的**保留期基建**失效——因为 teardown 默认保留业务数据（--drop-data 才删），把防误删前移到了"根本不删"，绝大多数路径零数据损失，完整备份子系统（dump 落点 + 30天 retention cron + cleanup）是当前阶段过度工程。**但**保留其精神落在真正不可逆那一步：--drop-data 路径 DROP TABLE 前，mysqldump 本前缀表到 host 上带时间戳单文件、打印路径、不建滚动 cleanup（essence `fallback-detectability`：把不可逆销毁翻成可恢复）。契约 6 第 3 条降级为 --drop-data 专属单文件 dump，非全局备份子系统。

**裁定 4 · 确认 → y/N + 逐项 ack + 不可逆项全 opt-in flag 足够；三阶段字面确认不落**
契约 6 第 4 条（输入字面 `DELETE <slug>` 三阶段）2026-07 失效——**我自己 2026-05-14 reflection 形态 B 就标了**「字面确认是认知防御不是机械防御，对长期使用者退化为机械复制粘贴」。高频 onboard/删重建期它只多摩擦不多防御。真正的防御是**结构性**的（essence `reversibility-not-permission`）：--drop-data / --include-prod / --purge-thread 把全部不可逆动作 opt-in，加 --dry-run 必先跑——这比字面仪式硬。**唯一加码点**：`--include-prod --drop-data` 组合（真删 prod 业务数据，唯一真正灾难性组合）保留一次 slug 字面回显，其余 y/N。这是靶向慎重，不是全局仪式。

**裁定 5 · dev_ro → 问题打错了模式；真缺口是 legacy 应用整个 D 段被静默跳过**
物理核对（非采信口头）：`dev_ro` 在 **self_serve 模式下根本不建**（create_app_db.py:646 `不建 dev_ro`），只在 **legacy 模式 + prod** 建（line599 `if env=="prod"`）。而 teardown 的整个 D 段只在 `if self_serve:` 触发（teardown line440）。registry 实测 19 应用 = 13 legacy（`db_mode:<none>`）+ 6 self_serve。所以：
- self_serve 应用（teardown 唯一处理的 DB 模式）**没有 dev_ro**，当前 teardown 只 DROP `_app` 是**对的、无需补**。
- 真正的静默缺口：**legacy 应用（有 dev_ro + `_app` + `<slug>.dev-ro.env`）teardown 的 D 段根本不触发**——`_app`/`_dev_ro` 双账号孤儿、两 env-file 残留、migrations 不清。SKILL line356「须一并 DROP `_app`+`_dev_ro` 两 user + 删 `.env`/`.dev-ro.env`」是 legacy 时代写的指令，在 self_serve 语境已错（无 dev_ro、env-file 名是 `.test.env` 不是 `.dev-ro.env`）。

**处置**：① teardown 遇 legacy 应用（db_mode 非 null 非 self_serve）**显式 abort/warn**，不静默跳 D 段（静默跳 = 留孤儿是危险失败模式）——legacy 退役是 onboard 镜像之外的单独手工事，但必须让人看见。② SKILL line356 的 dev_ro 指令按模式重写：self_serve 无 dev_ro；legacy 退役单独走。③ 附带遗漏：`secrets.<env>.json` 的 per-app 后缀键 `<FIELD>__<slug>`（若该应用注册过）teardown 未清——次要，登记 TODO。

**契约旧条款 supersede 汇总（显式）**：
- 契约 6 第 2 条（GitLab archive 不删）→ 2026-07 部分失效，因删重建同 slug 工作流被 archive 的 path 占用阻塞（409）。
- 契约 6 第 3 条（mysqldump 30天备份子系统）→ 失效，因默认保留数据把防误删前移，保留期基建成过度工程；精神降级为 --drop-data 单文件 dump。
- 契约 6 第 4 条（三阶段字面确认）→ 失效，因它是低频回收假设下的认知仪式，高频删重建期退化为机械动作且摩擦更高，被 opt-in flag + dry-run 的结构化防御取代。
- 契约 6 第 6 条 + SKILL line356（DROP `_app`+`_dev_ro` 双 user）→ 存活但**命名腐烂**：self_serve 下 dev_ro 从不存在，指令按模式重写。

**行动建议（给父会话，只做架构裁定不改代码——以下交回主代理执行）**：
1. `git mv` teardown → `cg_platform_recycle.py`；更新 teardown-design.md 内所有 teardown→recycle 引用（辐射检查 grep）。
2. GitLab 默认 delete 保留、加 `--archive-repo` flag。
3. `--drop-data` 路径 DROP TABLE 前加单文件 mysqldump（打印路径），不建 retention cron。
4. `--include-prod --drop-data` 组合加一次 slug 字面回显；其余维持 y/N。
5. 主入口加 legacy 应用（db_mode 非 null/self_serve）显式 abort/warn，不静默跳 D 段；SKILL line356 dev_ro 指令按模式重写。
6. secrets.json per-app 后缀键清理登记 TODO。

### 核心假设
- GitLab delete 的 pending-deletion 软窗口足够作误删恢复缓冲（脚本已轮询 202→404 印证异步删存在，但未实测窗口时长/可 restore 与否——[推测] 基于 GitLab 通行行为，Keith 若在意可核 self-hosted 版本 restore 策略）。
- legacy 应用（13 个）在可预见期内是"退役/迁移"对象而非"重建"对象——若某 legacy 应用要删重建，D 段缺口从"静默跳"暴露为"必须补 legacy DB 分支"。
- 前两次改名=删重建的具体应用未在本轮核（主代理背景陈述采信）；若其中含 legacy 应用带 dev_ro，则历史删重建可能已留过 dev_ro 孤儿——建议顺带 grep 两 MySQL 实例 `information_schema.user` 里 `_dev_ro` 结尾账号对账。

### 可能出错的地方
- **最高风险**：裁定 1 改名 recycle。若 Keith 实际更认同 teardown 的"拆除=真删"语义（与 recycle 的"回收=可复用归还"张力），则该反向——改的是 CLAUDE.md 命名边界段一处 + 辐射，而非脚本名。我判 recycle 是因"honor 已注册 SSOT，减漂移 > 我的语义审美"，但这条踩在偏好边界（命名审美是 Decision Authority 合法抛回项）——**列为 Keith 可否决点**。
- **次高**：裁定 2 archive 逃生口可能永不被用（db:null 骨架占绝大多数），沦为 caged-freedom 式的无用 flag。缓解=先不加、真需要退役成熟应用时再加（YAGNI），本轮只定"默认 delete"这一刀。
- **中**：裁定 5 的 legacy abort 若做得太硬，会挡住"就是要删一个 legacy 骨架"的合法场景——abort 应可 `--force-legacy` 越过并提示手工补 dev_ro，非死墙。

### 推理盲区
- 未核 GitLab self-hosted（cgboiler）delete 后同 slug 立即重建是否真无 path 冲突——delete 若也占 path 一段时间，裁定 2「delete 更利重建」的论据弱化。这是我论证链里唯一没落物理证据的一跳。
- 未读 onboard 脚本全 15 步逐点，"其他遗漏持久对象"只从 registry/create_app_db/teardown 三处交叉推，可能漏 onboard 独有落点（如 cg-logs token 之外的 skill 侧注册）。

### 如果 N 个月后证明决策错了，最可能的根因
- **形态 A**：某 legacy 应用真要删重建，abort 拦住后有人手工删 DB 又漏了 dev_ro——静默孤儿只是从脚本移到了人手，没根治，只是移动了失败点。根因=legacy DB 退役通道始终没正式建，一直"触发式待办"。
- **形态 B**：recycle vs teardown 命名反复——Keith 半年后又觉得 teardown 更贴切，再改一次，两次辐射成本 > 当初一次性拍死。根因=命名审美抛回了但没抛透（我该更明确逼 Keith 在这条上一次拍死）。

### 北极星触达
#3 决策超越直觉——5 条裁定没有一条是"契约 6 说啥就啥"或"Keith 批啥就啥"，全部回到"这条条款编码的假设在当代还成立吗"重判。出场坐标（Keith 没想到的）：裁定 5 的问题本身打错了模式——dev_ro 在 teardown 唯一处理的 DB 模式里根本不存在，问题问的"补 dev_ro"是个不存在的对象，真风险（legacy 整段静默跳）在问题的视野之外。

### essence 对齐自检（必填）
- **对位滴**：
  - `terminus-walk-needs-terminus-visibility` (2026-05-02) — 契约 6 是低终态可见度下的按终态走，其编码终态假设的条款（archive/backup/仪式）该按 emergent 重判，编码不变量的存活。**本裁定的元骨架**。
  - `reversibility-not-permission` (2026-05-06) — 裁定 4：opt-in flag（结构性）> 字面确认（认知仪式）。
  - `fallback-detectability` (2026-05-06) — 裁定 3：--drop-data 单文件 dump 把不可逆销毁翻成可恢复。
  - `bug-shape-survives-fix` / `field-gravity` 家族 — 裁定 5：问题继承了 SKILL line356 legacy 时代的命名引力，"补 dev_ro"复制了旧框架，没看见对象已消失。
  - `ssot-distillation-vs-buffering` + `project-naming-as-frame-allocation` (2026-05-06) — 裁定 1：honor 已注册 SSOT 名，减漂移。
  - 我自己 `2026-05-14_cgboiler-pm-sandbox-contract-v0` 形态 B — 直接喂裁定 4（字面确认退化，是我当年就预判的形态）。
- **是否反着走某条**：`ghost-rules` 边界——裁定 2/3/4 都在"砍防御"，需警惕砍过头。但砍的都是"低频假设下的防御在高频场景失效"，非砍真实物理风险（DB 隔离闸门 1142/1143 一条没动），通过警戒。
- **cross-check 关键词**（已 grep essence.md 命中）：`terminus-walk / reversibility-not-permission / fallback-detectability / bug-shape-survives-fix / project-naming / ssot-distillation`。

### essence 候选（candidate-refuted，2026-07-08 auto_gg 当夜 fresh 证伪审 → REFUTED）
> **candidate-refuted**：已被 `stale-observer`(04-15) + `terminus-walk-needs-terminus-visibility`(05-02) 复合覆盖——"未写"vs"已写"在「规则演化速度 < 对象演化速度」轴上是程度差非种类差，stale-observer 已含规则演化=0 的极限形态；候选未跨到新失效机制。存档供史，不入 essence。
- **slug**: unwritten-contract-rots-not-waits
- **候选全文**: 未落地的契约不是冻结待建，是边腐烂边等——它引用的对象（表/账号/字段）可能在它被实现前就已从演化中的系统消失。骨架未写 ≠ 骨架保鲜；"待落地"里藏着"边落地边发现名词表已烂"。
- **物理证据清单**: 契约 6（2026-05-14 骨架未写）+ SKILL line356 明写 DROP `_dev_ro` / create_app_db.py:646 self_serve `不建 dev_ro` / registry 13 legacy vs 6 self_serve——契约引用的 dev_ro 对象在其从未实现的 14 个月里，被 self_serve 演化从主路径抹除。
- **相关既有滴**: `terminus-walk-needs-terminus-visibility`（精化：不只终态假设会错，连引用的名词都会腐烂）/ `stale-observer`（精化：规则演化 < 对象演化的极端形态——规则连"写"都没写，对象已变）/ `fleet-canon-is-sedimentary`。
- **去 gg 化测试**: 通过——任何"先写规范后实现"的工程物（RFC/设计稿/接口契约）都成立：未实现的契约其 referent 会随系统演化腐烂，落地时可能发现引用对象已不存在。
- **待补审**: auto_gg 当夜或下次设计会话过 fresh-context 证伪审后入库。

### 外部锚点
- `monster/cg-platform/docs/pm-paas-platform.md` line98 契约 6
- `monster/cg-platform/skills/cg-platform-create-app/SKILL.md` line356
- `monster/shared/scripts/cg_platform_create_app_db.py` line599/646（dev_ro 建库真相）
- `monster/shared/scripts/cg_platform_teardown.py` line440（D 段仅 self_serve 触发）
- `monster/cg-platform/docs/teardown-design.md`（主代理方案）
- 我的前作 `2026-05-14_cgboiler-pm-sandbox-contract-v0.md`（契约 6 原始决策 + 形态 B 预判）
