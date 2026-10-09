---
date: 2026-10-09
slug: monster-readme-routing-verdict
summoner: monster / Codex 原生子代理
northstar_reach: "#1 二阶效应；#3 决策超越直觉"
status: substantive-decision
---

# Reflection: README 改名不等于规则到场

### 给父会话的最终输出
最危险的迁移失败不是漏读新 AGENTS，而是把 README 里已退休的流程重新激活成现行规则。cgboiler 旧写链和 behavior-eval 重跑契约都存在这个实证形状。
开题：重写为“让操作发生时只收到一套适用规则，并让任务列表保持可扫读”；错误判据是规则副本仍能给出相反动作、文档被当 thread 数据扫描、历史/夜跑权限扩大到普通维护；最便宜一击已完成：核原件、脚本 glob/排除逻辑、真实路由。补集一是只整理 todos 并保留所有 README，能修可读性但漏掉已发生的流程分叉；补集二是所有命令型 README 整体 AGENTS 化，会重启旧流程并扩大角色约束。选定按职责分拆、按动作接线的局部迁移。
三层分别验收：内容职责决定规则真源；显式路由决定动作前可达；文件名消费者决定扫描、lint、注入和指标是否正确。AGENTS 名称本身不证明从根目录跨区任务已加载，更不证明行为收益。
1. inbox：新增 AGENTS 承载局部写入/分档/生命周期/格式规则，README 留用途、理由链与历史。todos 保留标题、单一规则入口、待办区；移走列表中部六行文件级说明，条目正文与其缩进子行完整保留。根入口明确“写入/移动/关闭 inbox 条目前读 inbox/AGENTS”。抽取规则时保留“Keith 明确说先留 todo 就留”的例外：源 README:28 的全称句不能覆盖 :60 的后来条件。
2. inbox 的全仓欠定点槽单独保留一个全局可达真源；推荐放现有 CLAUDE.d 规则拓扑内的独立契约，由根 Context Asymmetry 与 inbox AGENTS 引用，理由/裁决仍留可查证来源。不可把它只塞进 inbox 局部规则后宣称仍覆盖全仓，也不可复制成两份。迁移不修改原判据或观察窗。
3. threads：规则主体迁到 AGENTS，README 可留很薄的目录导航，但不留第二套 schema/生命周期指令。正文开头限定 live 顶层主体、redirect 和归档/evidence 的各自适用范围；避免子目录继承被误读成重写历史。改动必须包含所有活跃消费者与规则路由，且新旧规则文件都不参加主体枚举。根 AGENTS 与线程读取示例里的 rg 排除也要加 AGENTS；只改三个 Python 不足。
4. chat：保留用户手册，删除 README 内独立的召唤/收尾/升级操作序列与旧 JSON schema 示范，改指 AGENTS 的相应入口；改掉 AGENTS 文件树的“README 自包含、读它就够”承诺。实际流程唯一源继续包含 raise-topic.py 占用/去重和默认文字；不顺带重写聊天口吻或边界。
5. cgboiler：保留资料地图，将仍有效的不收项、写前读哪些契约等边界收敛到 AGENTS。README 的 legacy 更新表不可直接升为当前写入授权：现行 AGENTS 已明确 stage3 写侧冻结；将旧表明确标为 legacy read model 说明，当前操作路由指向 WORLD_MODEL_SCHEMA/DATA_RUNBOOK，且机制维护不隐含跑业务数据。无需改变业务授权。
6. scheduled：保留 README 与已登记的按任务读范式入口，不整体改名。auto-monster：保留机制手册，夜跑角色权力/动作规则收敛到 PROMPT；README 仅概述并指到 PROMPT，不把这些限制施加给普通维护 Agent。顺带修 PROMPT 首段“lint 失败跳过 sync”旧全仓门，按 §2.2 和 threads_sync.py 实际违规文件隔离执行；不扩夜跑权限。README/PROMPT 的旧 Desktop 调度身份换成现行入口指针，实值回 plist/CLI-INVENTORY，不在本批修改调度。
7. scratch：保留 README，无需新建薄 AGENTS；其独有“被引用/第二次使用则迁走”规则未被根完整承接，根 scratch 入口补写操作前的精确读取路由即可。无需搬任何 scratch 实物。
观察项裁定：developer-inbox 已有父 AGENTS 显式路由，README 还承担公共投影源，保留；idesk-duty 的授权由 run.py 读取 AUTHORIZATION，保留授权单源，可在 hermes 父入口补维护时读取 README+AUTHORIZATION 的路由，不能让维护者继承值班免 ACK；behavior-eval README 头明确 07-24 封存、09-21 继续冻结，撤回“给维护纪律补活跃路由”的旧建议；studio/new_impl 恢复开发另有目标条件，本轮保持历史材料。
具体验收：保存迁移前正文和任务块；对 todos 原任务块逐块保真；对拆分规则做原条款→新落点映射；本地测试覆盖 README/AGENTS 均被排除、正常线程仍被 lint、MEMORY 不生成规则页、hook 不把 AGENTS 当 thread。更新共享 done 技能、persistence、SSOT/seam 登记、框架测量路径和读取率正则等活消费者；历史快照原路径保留。读取率旧哨只看 Claude transcript 且不验先读后写，修改正则不能当 Codex 到场证明。
实施边界：本地内容迁移、同源冲突清理与必要代码消费者修改；不批量改 269 份 README、不改外部系统、不重启封存评测、不迁移定时任务、不改任务状态。已有审计只表示枚举与抽样，不升级为全仓逐篇语义审完。本次未执行业务改动；父会话完成实现与验收。

### 核心假设
父会话传来的用户“根据结论完成所有调整”授权涵盖上述本地迁移及消费者接线；保留所有既有外部动作与角色边界。
### 可能出错的地方
仓外消费者、动态构造路径和大小写排除漏扫；保留 README 的兼容导航被误当第二套生效规则；修改旧监测正则后错误宣称跨 harness 验证通过。
### 本次哪里思考得不够
核了指定原件与代表性补集，没有逐篇阅读 inventory 的 269 份；未运行迁移候选、harness 加载实验或全部代码测试。未对全部长文件作当前性治理。
### 如果三个月后证明决策错了，最可能的根因
交付被“文件已改名”定义，未对“从根目录进入动作”的实际路由做检查；或者将迁移中的语义纠偏扩成了未经原证据支持的规则改写。
### 北极星触达
将命名讨论转成“内容/激活/文件名消费者”三个独立闭环；识别冻结流程可能因搬家复活，并具体撤回 behavior-eval 路由建议。
### essence 对齐自检
- 对位：anchor-value-in-activation-not-in-content；mechanism-relocation-has-its-own-precondition；authoring-rules-do-not-govern-record-layers。已 grep 原卷标题并读取对应原文。
- 反向张力：separation-need-is-not-topology-verdict，故不为所有 README 新建 AGENTS，也不为 scratch 增薄壳；threads/inbox 迁移限已有规则和实际分叉，不新建扫描机制。
- cross-check 关键词：上述四个完整 slug，检索当前卷 memory/essence.md 与归档卷 memory/essence/2026-H1.md。
- 本轮不产 essence 候选，不修改 gg 其他文件，不 commit/push。
