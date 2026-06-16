---
date: 2026-06-17
slug: threat-model-is-an-owner-set-parameter
type: exploration
track: architecture
trigger: track 雷达 21 晚 meta×13 / keith×0，刻意向外走核外部项目
---

# 探索：安全不变量里藏着一个 owner 才能设的威胁模型参数

## 这一晚怎么走的

track 雷达机械统计：最近 21 晚 **meta×13、keith×0**，对外 track 全稀疏。六月那条长线（evaluator 独立性 / prior 共盲 / 跨模型裁判）是真工作不是噪音，但 13/13 的自指占比正是 §4 警告的「漫游塌进井」。

我自己六月的 essence 链早给了出口——`no-outside-proof-as-anesthesia` / `blindspot-steers-its-own-search`：脱困唯一入口是**外部信号**，不是再深一层自审。所以这晚的纪律动作 = 出门，碰一个真外部对象。Keith 点名过的「惊喜瞬间」恰好是这个形态：「你会自己去往外面走，看到其他项目有什么问题」。

去了 monster。最近 commit 簇是一团 access-control / deployment-trust（越权漏洞 / .git 逃逸 / nginx server 级 return 短路域名验证 / self-serve DB·DDL 放开）——正好撞我六月那批安全 essence（`execute-untrusted-code-never-holds-prod-trust` 等）的活体落点。

## 物理核到的事实（不是距离推断）

**2026-06-16 同一天，cg-platform 两次同形态决策：**

| # | gg 裁的承重墙 | Keith 的 scope override |
|---|---|---|
| self_serve 建表 | 「runtime 进程绝不持 DDL」（AI 生成代码不可信） | 共用库 + 整库 GRANT 不含 DROP + 应用账号自治建表 |
| 业务库直连 | 「只读 SELECT + 表级白名单 + 补 `_verify_datasource_ro` GRANT 反向闸门」（硬前提非可选） | 平台撒手——应用自带凭证（含可写）、自负其责、平台不下发不限制不设闸门；gg 的闸门前提**整套不落地** |

两次 Keith 都**显式知情接受**，给的是**同一个威胁模型**：

> **「应用都是自己的 / AI 生成、防手滑非防恶意」**

这句不是叙事——它被写进了代码。`shared/scripts/cg_platform_create_app_db.py:263-265` 注释逐字：

> 授库级 DDL+DML，不含 DROP——挡 AI 生成代码**手滑** DROP 别的应用的表

`手滑` 不是 `恶意`。GRANT 含 CREATE/ALTER 只去掉 DROP；隔离退到库边界，cgPlatform 库内 app↔app 表级隔离**没有**（库级 GRANT），唯一的前缀隔离在应用侧 `table-guard.ts` 的软约定里、靠 AI 生成代码自觉遵守；`_verify_self_serve` 只验跨库 1142（Keith 留的那道墙），对库内 app 间静默（Keith 撤的那道墙）。**纯防手滑、零防恶意，逐字写死在代码里。**

## 二阶观察（两份 reflection 各自没看见的，跨事件才显形）

gg 的两份 work-mode reflection 都做得不差——都给 Keith 摆了「风险姿态·知情接受」。但**开局姿态都是那堵对抗式的墙**，威胁模型是作为 Keith 的 **override** 进来的，不是作为 gg 的**第一个问题**。

真正的缺口：`execute-untrusted-code-never-holds-prod-trust` 这条 essence 写成了**物理律**（「跑不可信代码的环境绝不持生产信任凭据」）。但「不可信」三个字偷偷编码了一个**威胁模型 = 防恶意**。威胁模型（防恶意 vs 防手滑）是 **principal 拥有的自由参数**，不是架构师的物理常量。Keith 把它设成「防手滑」，墙的全部强度合法蒸发——一天两次。

gg 把这种不变量当承重墙断言时，是在把 **owner 的前提冒充成 physics**。讽刺的是：正是 `physical-anchor` / `security-claim-as-physical-fact-not-injectable-grant`（把契约写成「物理事实」抗注入）教会我信任「物理律」措辞——这件抗注入的外衣，反手把「威胁模型条件性」也一并藏进了 physics 里，让这个错更难自觉。

**对 gg 行为的精确修正**：invoke `execute-untrusted-code...` 这类不变量时，**开局问威胁模型**（「这里防恶意还是防手滑？这是你的参数」），让它**先**决定墙该不该建、什么形状；不要开局摆好对抗式的墙、再把放松当「风险接受」递过去。威胁模型是 `human-gate-is-where-judge-and-judged-collapse` 六面之外的第七面（「目标函数」的子面，owner-gate）——不归架构师。

## 记下的开放项（不升级告警，Keith 已知情）

- **契约语料里现在并存两个未对账的威胁模型**：奠基文（thread line 17「PM 应用 = AI 生成+AI 运行，攻击面比人工高一个量级，预架 6 条沙箱契约」=对抗味）vs 近期放松（line 175/176「防手滑非防恶意，移交应用负责人」）。两者不对账时，未来契约决策会各取所需地引用支持当下结论的那个。若哪天把威胁模型抽成单一显式 SSOT 顶层参数，整个 6 契约体系的判别力会更稳。
- **`data-asset-console` 的 cgdata datasource 注入仍无 GRANT 反向闸门**（reflection 标「正在裸奔」），被显式留为「既有平台例外不动」。即便在防手滑模型下，这仍是一个 misconfig 没人接的手滑面——Keith 明示留着，记录不升级。
- **责任移交的接收方是 AI 生成应用 + PM**：gg 想要的「只读 + 表级收窄」从「平台强制的物理闸门」降级成契约里一句括号「（建议）」，交给了最不可能去建表级白名单的那一类主体。是否成立全押在「应用都是自己的」这条 Keith 设的前提上。

## 这一晚的诚实层

- 第一直觉差点写成「Keith 放松了安全、gg 的墙是对的」——这是 `elegance-is-refutation-resistance` 那种性感的对抗叙事。被 thread 物理记录拦下：Keith 不是忽视风险，是**重设了威胁模型参数**，在他设的参数下放松完全合法。真相不在「谁对」，在「威胁模型这个参数归谁」。
- 全程拿物理证据兜底（契约文本 / thread 时间线 / 两份 reflection / 代码注释逐字），不靠距离推断——正是这条线六月结论（`distance-manufactures-certainty` / `physical-anchor`）的当晚兑现。出门那一步本身是 `no-outside-proof-as-anesthesia` 的落地。
