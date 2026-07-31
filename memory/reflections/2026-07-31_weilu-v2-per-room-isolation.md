---
date: 2026-07-31
slug: weilu-v2-per-room-isolation
mode: work
status: substantive-decision
summoner: monster 主会话（cg-weilu v2 方案，改上游 cc-assistant）
---

# 围炉 v2 per-room 隔离：A（workspaceKey 穿线）vs B（per-room botId）裁决

## 给父会话的最终输出

**裁决：B（per-room botId `cg-weilu__r<roomId>`），且 B 不是 botId 语义扩张，是语义还原。** 附带三条父会话未列的实查新事实与一份加固/行动清单。

**核心理由链**：
1. cc-assistant 的隔离原语是 `(botId, userid)` 元组——workspace / skill / `getResumable` / `resetUser` / 白名单全部按它切；sessionKey 只切进程池一层（essence `network-cannot-cut-what-shares-tuple`：隔离的刀只能切它那层能区分的维度）。A 案 = 引入系统所有现有代码都不认识的第三维度并手工穿到每一层，且**未来每个新增落盘点都会默认只看元组**，workspaceKey 永远靠人记得穿——静默分裂是结构性复发，不是一次性 diff。
2. **C 案反证**（补集采样）：另一半元组 per-room userid（`888888__r<id>`）也零新管道，但 `issueInternalApiToken(userid)`（pool.js:111-113）和 `lookupUser(userid)` 都吃 userid → 笔记读权限与画像链路全断。结论：**房间必须编码在「不进下游身份系统」的那一半维度上**——botId 恰是这一半。这反证 B 选对了维度。
3. botId 语义之辩：cc/index.js 头注「多 bot：每个 bot 一个 client 实例」——bot 的语义本就是「一个独立 agent 实例」，不是「调用方应用」。围炉 v2 产品定义（每群可依被各自约定/记忆钉住）= 每群一个独立 agent。错的是把 N 个 agent 挤进一个 botId，不是 B 案。
4. tenantId 一等维度方案 = 为一个并不存在的「botId=应用」纯度付 A 案全部穿线成本，reject。

**三条父会话未列的实查新事实**（全部行号复核）：
- **F1 `resetUser(botId, userid)`（pool.js:222-233）按元组全灭**：A 案下「改约定 reset 该群 session」（brief §5.2 / 验收判据 5）会杀掉**所有群**的进程并 drop resumable——A 案还得给 reset 链路穿 key，diff 更宽。B 案天然 per-room。
- **F2 `store.getResumable(botId, userid)`（pool.js:183）**：围炉侧只传 `body.sessionId`、不传 fresh（assistant.service.ts:169）。A 案下新群首轮 sessionId=null → 捞到**别的群**最近 session → 新群第一句接上别群完整历史。必现，不是「可能」。B 案 key 天然分群。
- **F3 EverOS 记忆层 A/B 都不解决**：`memorize.js:71` 沉淀 body 只有 `user_id`（botId 不进箱）、`fetchMemoryBlock(userid)`（cc/index.js:1640）只按 userid 预取，`AUTO_MEMORIZE_ENABLED=true` prod/test 均开。**N 个群的对话都会灌进 888888 一个 EverOS 箱再被跨群预取回来**——第三个隔离维度，两案之外的独立必修项。

**加固最小集**（问题 3）：
- 白名单：保留精确集合 + 单一硬编码谓词 `isWeiluRoomBot(botId)`（正则 `^cg-weilu__r[a-z0-9-]{1,32}$`），不做通用 pattern env（单消费方不配通用机制）；同一谓词供 resolveClient 与 systemPromptAppend 门禁两处复用，别写两份。
- **roomId 生成器源头收窄**到 `[a-z0-9-]`（nanoid 自定义字母表），保证 botId/safe() 目录名/正则三方一致，杜绝 safe() 转义撞目录。v1 `main` 符合。约定 `__` 为维度分隔符、应用级 botId 禁用（封顶原则：botId 格式到 `<app>` | `<app>__r<roomKey>` 为止，不再叠维度；出现第三正交维度时才升一等参数）。
- `extraWebClients` + `sharedSkillStores`（cc/index.js:37，父会话没列的第二个无上限 Map）统一 cap（如 500），**超限拒新 fail loud，不做 LRU**——真实群数有限，超限即异常；LRU 还要处理 skillStore dispose，复杂度不值。
- 磁盘放大实测界：一个伪 roomId 只造空目录 + 1KB CLAUDE.md，真实放大要走对话（进程池 50 顶 + 配额）；内网防手滑不防恶意的威胁模型（owner 参数）下上述已够。

**行动清单**：① B 案落地 + roomId 字符集收窄 ② 白名单谓词单点化 ③ 双 Map cap ④ **cg-weilu 前缀 botId 跳过 memorizer.flushSession 与 fetchMemoryBlock**（群记忆走围炉自建 cg_weilu_memory，EverOS 是私人助理的记忆模型、对可依是错的）⑤ 检查按 botId 聚合的日志/用量归因面，围炉需前缀归并 ⑥ brief §5.3(b) workspaceKey 段作废改 B ⑦ 归档群 workspace 不清理，brief 登记尾巴。旧 botId=cg-weilu 下的数据是已砍掉的 8 个个人助理的（userid=真人），可依数据全新，零迁移负担。

## 核心假设
- cc-assistant 后续新增落盘/隔离点仍会默认按 (botId, userid) 元组——B 案的「未来免穿线」红利依赖这一惯性成立。
- 围炉每群恒一个 cc session 的形态不变（进程数 = 群活跃数，50 共享顶未被本裁决改变）。
- 川锅威胁模型 = 防手滑不防内网恶意（Keith 一贯 owner 参数）；若翻转，白名单加固要重估。

## 可能出错的地方
- skillStore 实例若含 watcher/timer，cap-拒新之外还需 dispose 审计（未逐行核 skill-store.js 内部资源）。
- 按 botId 的统计/告警面我只做了推断级扫描（upstream-proxy 剥计费头、scheduler 钉 cg-desk），未穷举全部日志消费方；行动 ⑤ 交父会话跑辐射检查。
- `main` 群保留为普通群时 botId 变 `cg-weilu__rmain`，v1 时代可依走 FastGPT 无 cc 侧遗产——已核，但若 v1 期间有人用 888888 在 cc 侧留过 session 则有残留（未查 store db 实数据）。

## 推理盲区
- 我未运行任何代码，全部为静态读证；`getResumable` 串会话（F2）是代码路径推演，未活体复现。
- EverOS 箱污染的实际后果强度（预取 block 的注入权重）未量化——判「必修」基于机制而非实测危害。

## 根因预判
若本裁决错，最可能错在：低估「botId 散桶」对某个我没看到的按-botId-消费方（计费/告警/审计）的破坏——即 F3 同构的第四个隐藏消费面。

## essence 对齐自检
- `network-cannot-cut-what-shares-tuple`（已 grep 视图 F8）：本裁决主承重滴——隔离维度选择即刀所在层。
- `separation-need-is-not-topology-verdict`（F7）：B 案是「最轻治理形态」（复用已有维度），A/tenantId 是造新墙——方向一致。
- `ontology-expansion-velocity-needs-cap`（F7）：botId 格式封顶原则即其落地。
- `security-invariant-encodes-an-owner-set-threat-model`（F8）：白名单加固强度显式挂在 owner 威胁模型上。
- 反向检查：`tool-elevation-as-occam` 边界注（前提要现场核）——本次未把「第二消费者」逻辑套白名单机制，反而反向收窄（单消费方硬编码），无冲突。
- 对齐度：高。

## 北极星触达
#3 决策超越直觉：父会话倾向 B 但理由停在「diff 宽 vs 复用管道」；本裁决把它推进到「元组哪一半可编码」的判据层（C 案反证），并挖出 F1/F2/F3 三条两案框架外的物理事实——其中 F3 是方案盲区。

## essence 候选滴（~~candidate-unverified~~ → 已入库：2026-07-31 夜巡 fresh 验证关 PASSED-WITH-EDITS，三改后 append 为 essence #186——补「新粒度⊥身份」适用前提 / 补最小闭包轴对身份侧不可见的翻面 / 必须→默认；最强反驳点见 essence 滴内注记）

**slug 候选**：`isolation-key-goes-in-the-identity-free-half`
**候选全文**：扩隔离粒度时，复合 key 的各维度不等价——有的维度流进下游身份系统（token / 画像 / 权限查询），有的只参与本地路由与落盘。新隔离粒度必须编码进「不进下游身份系统」的那一半，否则每个下游身份消费点都成断点。判据：对每个候选维度 grep 它的全部消费面，选消费闭包最小的。← `network-cannot-cut-what-shares-tuple` 的内部精化：元组不是均质的，刀要挑元组里下游耦合最小的那根轴。
**物理证据**：cc-assistant pool.js:111-113（token 只吃 userid）vs workspaceDir/skillStore/getResumable/resetUser（吃 botId+userid）——per-room userid 断权限链、per-room botId 零断点，同一系统内两半维度消费闭包实测不对称。
**相关既有滴**：`network-cannot-cut-what-shares-tuple`（精化对象）、`ownership-by-facet`（同属「按消费面切」家族）。
