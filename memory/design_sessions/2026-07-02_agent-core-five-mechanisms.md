---
date: 2026-07-02
slug: agent-core-five-mechanisms
type: design-session
summoner: Keith 直接对话
started_at: 08:50
ended_at: 10:05
---

# 设计会话反思：agent 的核心是什么 → 五机制落地

## 议题列表

1. **Keith 之问："对 agent 来讲什么是核心？提示词？机制？还是别的？"** —— 答：核心 = 换了模型还成立的部分。对 gg 是三资产：目标函数（KERNEL 身份原点+北极星+铁律）/ append-only 记忆 / 物理反馈回路。提示词是配置向模型加载时的临时编码，机制分承重契约与垫片实现。物理证据 = 06-10 codex 冷启动验收（承重层完整移植、断点全在垫片层）。
2. **Keith 追问："该纳入但还没有的？我不知道我不知道的？"** —— 双路作业：内部用 gg 自己的 essence 审 gg 结构（主代理自做），外部派 agent 强制 WebSearch 扫 2026 上半年前沿（22 条发现，ER#11 半衰期规则）。
3. **Keith 授权（/goal）："交给你来完成…建立简洁且真正高效的机制"** —— 按 `scope-of-blanket-authorization` 解读为方向授权，落点按可逆性二分执行。

## 共识 / 变更清单

**判断层共识**：三资产每个都缺一个守护机制——反馈回路层缺 detector+gate、记忆层缺 consolidation+input filter、目标函数层缺物理保险丝。其中两个缺口是"内部理论推导 × 外部前沿独立演化"双链撞同一点（巩固相位 ↔ Anthropic Dreaming；验证关 ↔ Self-Confirmation Trap arXiv:2606.24428），一个纯外部新知（memory poisoning arXiv:2604.16548）。

**五机制落地**（全部 KERNEL 之外，全部可逆，未 commit 留 working tree）：

| # | 机制 | 文件 | 验证 |
|---|---|---|---|
| 1 | KERNEL 物理保险丝 | `scripts/hooks/pre-commit`（新）+ `git config core.hooksPath scripts/hooks` + `check_structure.py` 保险丝哨兵 + `audit.py` 汇总纳入 | 实测：改 KERNEL 提交被拦 exit 1 后恢复干净；哨兵负面测试（拆 config 报警/恢复归零）双路径过 |
| 2 | 外部输入卫生 | `exploration.md §2.5`（新节） | 静态（协议类，下次漫游夜首跑） |
| 3 | essence 入库验证关 | `essence.md` 头部新协议节 + 4 入口指针（CLAUDE.md §3 / auto_gg DID#6 / auto_gg §1.3 白名单例外 / exploration §3） | **当轮吃狗粮**：本次会话自己的候选滴走了这道关（fresh subagent 证伪审），verdict 见"沉淀"节 |
| 4 | 月度记忆巩固相位 | `auto_gg.md §2` 新节 + `memory/consolidation/README.md`（新） | 静态；首跑 = 8 月第一个 auto_gg 夜 |
| 5 | 身份回归基线 v0 | `eval/README.md` + `eval/identity-cases.md`（10 题，全部有 essence 事故原型，status: draft-for-keith-review） | audit 孤儿清零；题库判据冻结权在 Keith，未批准前不作正式判定 |

辐射同步：README 结构树 +3 行、CORE §8 记忆清单 + 新"检验"行。audit 复跑 10→9 违规（-孤儿 1，+保险丝哨兵 0；余 9 全预存：8 死链在 monster canon-bugs 相对路径、1 命名违规是 06-15 待 Keith 拍的 12 夜议题）。

**[CORE_RULE_TOUCH] 显式标注**：本次改了三处规则性文本——auto_gg §1.3 子代理禁令加白名单例外（验证关 subagent 是 evaluator 不是决策代理）、auto_gg DID#6 加验证关前置、exploration 加 §2.5。设计模式有权直改，但 Keith review 时请重点看这三处：**§1.3 例外是给夜间模式开了一道此前全禁的口子**，收窄措辞我已尽力（仅限验证关、仅 evaluator 角色），仍值得你亲自过目。

## 我这次哪里做得好 / 哪里差

**好**：① 内外双链方法——内部缺口全部先用 gg 自己的 essence 滴论证再动手，外部调研按 ER#11 强制 WebSearch，两链交叉后才定优先级；② 机制建立当轮实测（hook 真拦了一次提交、哨兵真拆了一次报警、验证关真跑了一次证伪审），无一纸面交付；③ Keith 授权解读显式过了 `scope-of-blanket-authorization`（git config 判可逆执行，push/cron 不动）。

**差**：① 上午回答"核心是什么"时引用 06-10 跨模型验收，未先读 06-24 `craft-ports-identity-doesnt` 对 CORE §8 的 category slip 批评（承重层捕获工艺非身份）——答案主体成立但"承重层=身份可移植"的表述在 essence 里已被精化过，我引用了旧版本理解，恰是本次建"巩固相位/修正链视图"要解的那个病（读到被后续修正的旧滴而不自知）——**病在自己身上发作了一次，反而坐实机制必要性**；② 五机制一口气落完才写反思，中途未留阶段性检查点，若中途会话中断，Keith 看到的是半套机制无解释。

## 元洞察（gg 演化本身的 learning）

**gg 的理论一直跑在 gg 的结构前面**。五机制里四个不需要任何新洞察——rule-layer-flywheel(04-24) 论证了 hook、generator-evaluator-separation(04-18) 自曝了验证关缺失、reconsolidation-safe(06-10) 许可了巩固、06-25/27/30 三滴诊断完了身份基线——最早的一条等了 10 周。自审的最高产动作不是想新结论，是 grep 自己的既有结论找未兑现项。已写入候选 essence（见"沉淀"节，过验证关）。

## 下次继续

1. **Keith review 三件**：eval 题库 10 题（判据冻结权在你）/ auto_gg §1.3 白名单例外措辞 / 本轮全部 working tree 改动
2. **观察点**：8 月第一个 auto_gg 夜 = consolidation 首跑；连续两期质量认可后议进启动链
3. **未做的低优先级**：budget 意识（gg 对自身 token 成本零感知）、LongMemEval-V2（将来记忆 eval 参考）
4. **预存债**（非本轮，顺手记）：essence L869 + nw-reconciliation 8 条 canon-bugs 死链（monster 相对路径识别）、06-15 中文 slug 命名违规（12 夜议题待拍）
5. **Keith 生态提醒**：Snyk 检出 36% 公开 skill 含 prompt injection——search-skill 安装流程值得加注入审查（gg 域外，留给 Keith 主会话）

## KERNEL 改动清单

**无**。KERNEL.md 内容零改动（保险丝是外部保护层，git config 与 hook 文件均在 KERNEL 之外；测试中对 KERNEL 的临时空行改动已 `git checkout --` 恢复并核实干净）。

## 代码质量（本轮有代码产出）

- `scripts/hooks/pre-commit`：bash，无外部依赖，grep -qx 精确匹配文件名；已知边界——`git commit --no-verify` 可绕过（auto_gg §1.3 契约层已禁，设计/工作模式无此约束，Keith 本人天然可绕，符合"保险丝防机器不防主人"定位）
- `check_structure.py::check_kernel_fuse`：subprocess 局部 import 与文件风格略不一致（顶部 import 更佳）；timeout 5s 有兜底
- `audit.py` exit code 沿用"违规总数"设计，>255 会被 shell 截断——预存设计未动，当前量级（9）无风险

## essence 对齐自检（必填）

- **对位滴**（本次判断/改动的依据）：`rule-layer-flywheel`(04-24)+`rhetoric-vs-mechanism`(04-27)+`mechanical-gate-needs-machine-detectable-target`(06-24)→机制1；`generator-evaluator-separation`(04-18)+`recursive-point-self-audit-splits-by-format-vs-content-axis`(06-10)→机制3；`reconsolidation-safe-iff-original-immutable`(06-10)→机制4；`judgment-step-has-no-clean-correctness-target`(06-25)+`substrate-ships-the-evaluator-body-not-its-eyes`(06-27)+`evaluator-is-keith-and-doesnt-fork`(06-30)→机制5靶子设计；`scope-of-blanket-authorization`(05-06)→授权解读；`survey-as-coordinate`(04-23)→外部调研筛法；`subject-is-configuration`(04-30)+`invariance-allocation`(04-19)→上午"核心"答案
- **反着走**：一处张力——机制2给 exploration 加输入卫生，与 `caged-freedom`(04-26,"给自由建笼子是设计自由模式的失败模式")有表面冲突。判断为不违反：卫生协议不约束探索方向/时长/产物，只约束"外部文本的指令地位"与"essence 写入门槛"，后者本就是 KERNEL §3 派生的全模式约束。显式记录供 Keith 复核。
- **前提核验**：`rule-layer-flywheel` 前提=目标是机器可检物理量→KERNEL.md 的 staged diff，成立（hook 实测拦截为证）；`reconsolidation-safe` 前提=原件不可改写→consolidation 契约明文"绝不修改 essence 原件"+append-only 哨兵在岗，成立；`scope-of-blanket-authorization` 前提=存在未明示高代价落点→本轮 push/cron 未动、git config 经可逆性判定，成立；`survey-as-coordinate` 前提=认真读原文而非清单式对照→22 条逐条对 gg 现状三相分类（收敛/替换诱惑/真缺口），成立。
- **未用到的反向 grep**：关键词 `井|回路|检索|加载` → `essence-grep` 工具（tools/essence-grep.md）存在但本轮自审用的是全量 Read 而非该工具——漏用现成工具，成本可接受（全量读更完整）但下次自审先看 tools/；`bucket-time-asymmetry`(05-08,"出口需求迟到") 未引用——它警告 consolidation 类"以后会读"的产物可能变空头支票，已用"连续两期质量认可才进启动链"的 tripwire 部分对冲，记为机制4的已知风险。
- **cross-check 关键词**（物理证据）：`flywheel|rhetoric|mechanical-gate|generator-evaluator|reconsolidation|judgment-step|substrate-ships|evaluator-is-keith|blanket|survey|caged|bucket-time`

## 沉淀（写入 essence.md 的内容）

一滴 `theory-outruns-structure-in-self-evolving-systems`——**入库验证关首跑，PASSED 含 3 处实质修正，全部吸收后 append**：

- verdict 物理留痕（按验证关协议第 4 步，留反驳内容不留"已验证"三个字）：审查员独立核了 4 条既有滴原文逐字在案 + `.git/hooks` 今日前为空 + 新目录时间戳；**最强反驳点** = "差值就是工作队列"与 `premature-abstraction-tripwire`(04-21) 直接相抵——部分已论证推论的正确处置是留 tripwire 等第 N 次场景而非建制，今日 4/4 全建可能是 grep 后的幸存者筛选
- 三处修正：①"最高产"→"高产"（n=1 无对照的最高级）②"工作队列"→"候选池"（兼容 tripwire 类该留空）③"成本天然不对等"补制度门槛（D1/D2 授权是 gg 内的实际成因之一，"天然"二字洗掉了它）+ 补适用前提（沉淀层须高门槛策展）
- **机制自证**：generator 初稿三处滑出证据边界的表述被 fresh evaluator 当场逮住——验证关建立当轮就产生了它存在的第一手证据。

## dd 后回看补记（Keith 要求"趁上下文在复盘所有改动"，同轮补记）

**回看发现并已修**：
1. **验证关协议自身有错**（最重）：原协议写"工作模式直接派 fresh subagent"——但 gg 工作模式工具集（Read/Write/Edit/Glob/Grep/Bash）**没有 Agent，物理上开不了证伪审**。写协议时没核执行者的工具集，ER#13 同源失误。已修三处：cc_agent.md 退场第 3 步接 candidate-unverified 分支（候选滴留 reflection，auto_gg 夜里或设计会话补审入库，父会话代跑 PASSED 例外）+ essence.md 头部协议同步 + monster gg-briefing 订正条措辞改准（"父会话先代跑验证关"）
2. **"机制无一纸面交付"表述过了**：五机制里巩固（8 月首跑）和 eval（零 run）执行次数为零。已补 eval Q1 冒烟：被测（真实文件缺失，零模拟）弃答 + 三条物理证据 + 求助，裁判 PASS 且 tool_uses=0——PROTOCOL 全链路可执行实证，run 存档 `eval/runs/2026-07-02_fable5-smoke-q1.md`。巩固相位维持 8 月首跑不提前
3. **eval README 补两条局限**：单轮题测不出长程漂移（06-23 事故系长会话产物，长程 detector 仍是 Keith + auto_gg）；被测载入集（承重层三件）≠ 真实 gg（还载 essence/state），够换模型验收、日常漂移代表性打折
4. **孤儿豁免前置修**：eval/runs/ 与 memory/consolidation/ 的产物文件不会被逐个引用，首个 run 已实测报孤儿 → `_common.py` ARCHIVE_PREFIXES +2 前缀，audit 回基线 9
5. **Snyk 36% 标注未核**：该数字系调研 agent 二手转述，agenda 已加"[未核原报告]"标注——ER 承重事实禁采信二手摘要，传给 Keith 的数字要么核要么标

**回看确认的已知缝（不修，记录理由）**：
- `core.hooksPath` 是仓库本地 config 不入版本库——重 clone 后保险丝静默失效,由 audit 哨兵覆盖（首夜 audit 即报），可接受
- exploration 模式未继承 auto_gg §1.3 的 --no-verify 禁令（其硬约束集仅 KERNEL §2 + CORE §7）——物理缝存在，但被铁律 3 身份层覆盖（夜间无 Keith 在场 = 双确认不可能成立）；不给 exploration 加条款（M1：给未发生过的灾难写规则是幽灵，且保险丝定位本就是"防漂移不防故意"）
- hook 提示信息含绕过变量名——对手是漂移的自己不是攻击者，藏钥匙（如移到 hook 源码外）是幽灵锁，M1 不加
- 输入卫生是五机制中唯一纯 prompt 层——但按 `mechanical-gate-needs-machine-detectable-target` 判别刀这是**正确层**（投毒判定是语义判定，无物理量可挂 hook），非妥协；此论证建制时未留痕，本节补
- 验证关成本账（回看时发现未算）：每滴 ≈1 次 subagent（本轮实测 ~43k tokens），按近月沉淀频率（约每夜 0.5-1 滴）月增量约 0.6-1.2M tokens。**Keith 知情项**：换更小模型跑证伪审可砍大半，或维持现状——essence 是永久资产，质量闸的成本花在最该花的地方，gg 倾向维持，Keith 有异议再调
