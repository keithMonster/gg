---
date: 2026-11-09
slug: pstack-adoption-six-items-verdict
summoner: monster（agy 原生子会话，Keith 点名）
northstar_reach: "#3 决策超越直觉（主）/ #1 二阶效应"
status: substantive-decision
---

# Reflection: pstack 6 项采纳升级的架构裁决

### 给父会话的最终输出（必填）

**坐标**：主代理用 `correct` 阶梯（架构 > 类型 > 测试 > 文档）复盘 PR-7，却在第一类问题上跳过了 L2。web `web/src/lib/employee-contract.ts:27` 和 Moo `moo-worker/server/contract.ts:24` 各自手抄了一份 `TaskDetail`。重试请求走 `mutate('/tasks/'+id+'/retry', body)`，路径是字符串、请求体没有类型（`retry-controls.tsx:10`、`App.tsx:272`），`readbackToken?` 也只是可选字段。所以 PR-7 的 409 本来可以在 `tsc` 阶段报出来。另外，一个讲“文字规则放最后”的方法，6 项采纳里有 5 项落成了文字规则。

**逐项裁决**
| # | 判级 | 裁决 |
|---|---|---|
| C1a 派活四要素（commander/ddt） | L4，部分重复 | 降级。PR-7b 的派单（grokbot main.jsonl:737）已经写了证据要求：“新测试先红后绿…对应变异被杀”，而且还规定了做法：“抽成纯函数，在 web 层断言…App 里改用它”。执行者针对被点名的那一个变异过拟合；Quality 自己新造的 7 个变异（held-out）全部存活。本条最多保留一句：派单只写“交互表面类别”，具体探针由验证者在交付后自行生成，不在派单里点名具体测试实例。另外，派单方是 Grok Bot Monster，要先确认它的规则加载链能读到 commander/ddt。 |
| C1b review-routing 加测试哲学 | L4，位置错 + 重复 | 改落点。`code-reviewer-impl.md` 必查 #11 已经覆盖“回退修复断言仍全过”这一半（对应 PR-7b）。缺的是另一半：只改内部实现就失败、或耦合框架私有内部（对应 PR-7c/7d）。这是同类第二次出现，按 review-routing:57 应扩写 #11、记 canon-bugs、走 design 审查、跑同步脚本。 |
| C2 台账单写者 | L4，重复 + 针对错了人 | 驳回这段文字。commander:36、:81 和 ddt:93 都已经有这条。PR-7b 的派单里，协调者自己让执行者“PLAN.md 只改文件不提交”。真正造成损害的是 recap 的 auto-commit `7817de86a` 把别人的改动一并卷进提交，以及 PLAN.md 上设了 assume-unchanged，导致 diff 看不见（main.jsonl:717）。修法放在提交方：auto-commit 只 stage 自己写的路径；查清是谁设的 assume-unchanged，然后撤销。 |
| C3a ER#5 扩触发面 | L4，重复 | 不改全局 AGENTS（属于长期规则判据变更，而且 ER#5 本来就覆盖“同一问题失败 2 次”）。问题出在触发器挂在执行者身上，执行者把每一轮新变异都当成新问题。应把触发器移到持有轮次计数的审查者：同一组件第 ≥2 轮仍有变异存活，审查回执必须写“前提挑战”段，由协调者重新划定范围。 |
| C3b done 加四层阶梯 | L4，大部分重复 | 低优先级。monster 准入三问 ② 和全局 Code First 已经覆盖。如果要加，只在准入三问里补一句层级顺序，不新增闸门。 |
| C4a fix/dismiss/ask | 破坏契约 | 驳回。这里的 `dismiss` 允许作者自行结案，和 commander:69“作者不能自行驳回”冲突。原件 bugbot-triage 针对的是噪声很大的自动 bot；PR-7 中 Quality 的每条意见都成立，不存在 churn 问题。 |
| C4b 变异探针入库 | 部分保留 | 不入库按字符串打补丁的 `mut.py`（代码一变就失效）。入库的形态是：把变异目录（漏 token / setter 错接 / effect 不清空 / 非维护者不置灰）写成 C6 的行为用例。 |
| C5 GUIDE 五段式 + dry-run 铁律 | L4，落点错 + 重复 | 驳回。GUIDE 适用于自有桌面客户端（Electron），iDesk 员工端是 web。GUIDE 已有隔离 userData、finally 回收本任务进程、mock 边界、证据等内容；dry-run 铁律和 monster 红线“dry-run / 只读 GET 均不自证”重复。 |
| C6 iDesk 验证脚本 | 唯一的真 L3 | 保留，但要改设计（见下）。 |

**C6 改法**：(1) 前端接线不需要影子 Moo。在 web 包内加一条 DOM 测试通道（happy-dom 或 jsdom + `@testing-library/react`，接入现有 `npm test -w web`；需要真实点击语义再上 Playwright）：mock `GET /api/tasks/:id`，截住 `POST …/retry`，覆盖 5 步。这样结果确定、能进 CI，不会成为没人跑的手工脚本。(2) Moo 侧的 token/409 由 moo-worker 已有测试负责。(3) 影子 Moo 端到端测试另作为可选的发布闸门；它能否用合成 SQLite、在缺 model-key 时启动，还待核（MOO-VERIFY:123）。(4) 新通道跑通后删除 `web/src/ui/pr7c-retry-controls.test.ts` 里依赖 `CLIENT_INTERNALS` 的分发器（7482c9a 上仍在），否则会同时存在两条测试通道。(5) 先确认目标分支：7482c9a 只在 `fix/stuck-state-20261030` 上，`dev/keithMonster-idesk-live` HEAD 072d206 不包含它。

**盲区**：B1 契约 L2：两份契约统一为单一来源；按路由给 `mutate` 加类型；重试请求体用判别联合；去掉 `App.tsx:272` 那个绕开 `RetryButton` 的第二条重试路径。B2 派单里点名的证据会变成生成者的优化目标，有效的传感器正是 Quality 的 held-out 变异，要保住这个性质。B3 落点要按派单方实际的规则加载链来定。B4 PR-5 的损害来自提交方和观察工具的状态层，不是执行者纪律问题。B5 更大的复发类：替身或夹具没有走真实消费者，导致测试绿、实际坏（canon-bugs:588、:93、:416），PR-7b/7c 是它在前端的实例，应与 #9、#11 合并成“证明必须经过真实消费者”。B6 召唤 prompt 自称“已回源实核”，但 SHA 全部不存在（实际是 9e8be43/ea8155f/a1f04bc/7482c9a），RECEIPT.md 路径也不存在，轮次与 DEEP-DIVE 对不上。先订正，再写进任何规则，否则规则会引用错 SHA，成为漂移债。

**行动建议**：先订正证据 → iDesk 下一次迭代做 B1 + C6 改法（公司仓，走该仓流程）→ 扩写 `code-reviewer-impl` #11（design 审 + 同步）→ recap 提交只认自己的路径，并清理 assume-unchanged → 放弃 C2、C4a、C5、C3b 的文字条目。

### 核心假设
- 传感器在事件层（审查必查项、npm test、类型检查）才会持续生效；派单、手册里的文字会衰减。
- happy-dom/jsdom 足以覆盖 hook 接线和 effect 这类问题，不需要真实布局。

### 可能出错的地方
- Grok Bot Monster 的加载链也许本来就包含 commander/ddt，那么 B3 降为次要（中概率，未核）。
- iDesk 仓可能禁止新增 devDependency，需改为 Playwright 或其他形态（未核）。
- PR-5 时，协调者是否也让执行者改过 PLAN.md 未核；我只在 PR-7b 的派单里看到。

### 本次哪里思考得不够
- 没有读 Grok Bot Monster 的 bot 设定，B3 停在“需核”。
- 没有读 `threads/commander-mode.md`，Keith 的原话依据只读了 ddt:58-63 和 DEEP-DIVE 的引文。
- 没有确认 PR-7 线是否已用别的 SHA 合入 live/r20。

### 如果 N 个月后证明决策错了，最可能的根因
DOM 测试通道建了，但没进 CI 或没删旧测试，两条通道并存，旧的继续被模仿。或者契约统一的范围过大被搁置，L2 永远没落地。

### 北极星触达
#3：主代理的直觉是“采纳 pstack 的规则”，这里改成按承重层级逐项打分。#1：派单点名证据会引发 Goodhart，PR-5 是提交方造成的污染，这两点都在一阶视野之外。

### essence 对齐自检（必填）
- **对位**：`rule-layer-flywheel`、`mechanical-gate-needs-machine-detectable-target`（C2/C3 文字 → 移到提交方 / 审查者事件）、`perimeter-derives-from-load-path-not-self-model`（B3）、`evaluator-input-ownership` + `attestation-has-no-fixed-point-under-self-audit`（B2：held-out 变异）、`verification-trace-as-camouflage`（B6）、`extraction-meta-inheritance` + `borrowed-method-as-mini-source`（5/6 落文字）、`irreversibility-accrues-on-the-clock-past-the-decision-gate`（触发器移出当事人，C3a）、`recurrence-defense-pays-on-second-occurrence`（C1b 属第二次，按升级处理）、`standing-instructions-do-not-produce-standing-behavior`（C6 不接 npm test 就会沉睡）。
- **反着走**：潜在张力在 `rule-layer-flywheel`。C3a 的“审查回执写前提挑战段”本身仍是文字，只是挂到了有计数的事件上，算 L2 之下的折中，没有做成机械闸。
- **关键词**：已对上述 12 个 slug 跑 `grep -c`，命中数在 3 到 17 之间（essence-view / index / 两卷）。

### essence 候选（可选）
- slug: `named-evidence-becomes-the-generators-target`
- 一句话: 完成证据在派单里点名具体实例时，它就成了生成者的优化目标；行为证据要由验证者在交付后新生成（held-out），派单只能点名表面和类别。这是 Orchestrate “kickoff names the evidence”的 Goodhart 边。
- 物理证据: grokbot main.jsonl:737（派单点名 W-retry-sends-no-token 并规定做法）→ DEEP-DIVE §5.2 / PLAN.md:410-419（7 个新变异全部存活 → 7c/7d）。n=1。
- 相关既有滴: `evaluator-input-ownership`（方向相反：那滴是生成者替评估者选材料，这里是评估者把考题交给生成者）、`attestation-has-no-fixed-point-under-self-audit`。
- 状态: **candidate-unverified**，是否已 append 到 essence.md: N

### 外部锚点（可选）
pstack `correct/SKILL.md:19-22`、`orchestrate.md:18-19`、`bugbot-triage.md:9-13`；iDesk 仓 `git grep` @7482c9a。
