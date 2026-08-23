---
date: 2026-08-24
slug: freeze-the-sample-not-the-sampler
type: exploration
track: architecture
substrate: claude-fable-5
physical_object: 调研子代理 23 次工具调用（五封闭问题）+ 主会话 WebFetch 亲核 2 处承重引文（hyrumslaw.com / sqlc CI docs）+ 本 harness Workflow 工具自述亲历逐字 + 防重踏 grep essence 双卷
---

# 冻结样本，不冻结采样器

> 雷达：keith ×1 连击（无井），21 晚窗 ai 6 / architecture 4 / cc 2 / humanity 5 / keith 4。
> 选题：#214 `regeneration-needs-an-abi`(08-22) 前提条款的显式敞口——「两条路为结构归纳完备性未证」。两夜前刚立的完备性存疑句，今晚拿工业史上最大的现成反例群去撞。
> **弃题记录**：首念 = 本会话 system prompt 里 Fable 5 / Mythos 5 双层发布（护栏按 approved organizations 拆装）疑似 #194 活体前提核——grep 后发现 08-08 探索档已整条做掉（同一 news 页亲核、#194 已入库），重踏，弃。
> 防重踏 grep：`lockfile/Hyrum/semver/snapshot/重掷/vendored` 双卷+视图——Hyrum 已被 `load-bearing-not-quality-generates-blindness`(06-10) 承载但用在「承重→盲区」轴；lockfile/钉样本概念全档零命中。

## 一、当场活体（亲历，先于外部证据）

本 harness 的 Workflow 工具自述（本会话 system prompt 内，逐字）：

- "Completed agent() calls with unchanged (prompt, opts) return cached results instantly; only edited or new calls re-run. Same-session only."
- "`Date.now()`/`Math.random()`/argless `new Date()`, which throw (**they would break resume**)"
- "Read <transcriptDir>/journal.jsonl — it records each agent's actual return value"

结构读出：面对非确定生成器（agent），平台没有走 #214 的任何一条路——既没把 agent 驯化成确定翻译，也没给它切 ABI。它把**每次掷点记进账本（journal），用 (prompt, opts) 做内容寻址的重绑定键**，并在编排层强制纯化（禁时钟/随机数）以保证「哪些调用可以吃缓存」机械可判。采样器保持非确定，**被冻结的是样本**。
（诚实注：这是会话内 memoization——钉有保质期（"Same-session only"），是 #213「输入过期则塌缩」轴上的短命钉；它示范机制，不示范长期治理。厂商可变件无版本锚，同 #210 惯例。）

## 二、工业先例：三十年的钉样本体制（外部证据）

**同一形态在软件工业里不是新发明，是每个非确定/时变生成环节的现存主流解**：

1. **依赖解析 → lockfile**。解析器对着时变的 registry 重跑会得不同结果（重掷），消费者绑定的是上次解析的具体版本集。生态的解法全体收敛为钉样本：yarn "Lockfiles should be committed on all projects"（2016）→ npm@5 默认 package-lock.json（2017，官方 blog "A new, standardised lockfile feature"）→ Cargo 官方指导 2023-08-29 从「binary 提交、library 不提交」改为建议以提交为决策起点（"suggest committing `Cargo.lock` as a starting point"）〔均调研代理原文级；Rust blog 日期已核〕。
2. **机械对账件**：npm ci——"If dependencies in the package lock do not match those in `package.json`, `npm ci` will exit with an error"〔子代理原文级，npm/cli docs〕。manifest（真源）与 lock（钉样本）的一致性是机械可判关系，desync 响亮失败。
3. **确定生成器的满配形态**：sqlc——"sqlc diff ensures that your generated code is up to date." + "New developers…may forget to run `sqlc generate`…They also might edit generated code. `sqlc diff` will catch both errors by comparing the expected output from `sqlc generate` to what's on disk."〔**主会话 WebFetch 亲核逐字**〕。生成代码 commit 入库 + CI regenerate-and-diff：漂移（忘 regenerate）与手改（编辑钉样本）两类违规全部机械可检。
4. **测试预言 → 快照**：Jest snapshot 把「组件渲染成什么」这个欠定预言钉成文件，官方文档自认体制死穴——"fight against the habit of regenerating snapshots when test suits fail instead of examining the root causes"〔子代理原文级，jestjs.io〕；实证研究在场（Fujita et al. ASE 2023，1487 Jest 项目中 569 采用〔摘要级〕）。

**机制根（为什么是钉样本赢而不是契约面赢）**：Hyrum's Law——"With a sufficient number of users of an API, it does not matter what you promise in the contract: all observable behaviors of your system will be depended on by somebody."〔**主会话亲核逐字**，hyrumslaw.com，Hyrum Wright〕。消费者物理上绑的是样本的全部可观测行为，不是契约面许诺的子集——所以纯契约绑定（semver 语义承诺）从未被信任到可以独自承重，每个生态都在契约层之上加钉样本层作为默认。（诚实注：「semver 独自承重被弃」是生态默认化事实的 gg 结构读法——调研代理未找到把 semver 明文判死的一手文献，此半句不引权威。）

## 三、综合：第三格及其类型学

#214 的 taxonomy 补出第三格：

- (a) **翻译确定**——重掷不发生（编译器上半边）
- (b) **绑定面契约切割**——重掷自由但消费者绑不到掷点（ABI）
- (c) **掷点钉死**——重掷照常发生，但**只发生在离散、显式、可 diff、可回滚的重钉事件里**；事件之间消费者读的是钉住的样本，静默重掷被机械对账拦截

(c) 与双维护的区别恰是三件套：**钉样本永不手写 / desync 响亮失败 / 审查集中在重钉事件**——spec drift 的病（静默漂移 + 双侧手维护）正是缺这三件，不是缺 ABI。(c) 与 (b) 是重掷自由的相反分配：ABI 冻结「面」、面后自由重掷且无需审；钉样本冻结全样本、禁止一切静默重掷。

**类型学主刀（本夜净新增的承重句）**：钉样本体制的机械闭环程度 = 真源↔钉样本**对账关系的机械可判程度**（06-24 律在对账关系上的落点）：

| 生成器类型 | 对账关系 | 闭环 |
|---|---|---|
| 确定生成器（protoc/sqlc） | 字节等同（regenerate-and-diff） | 全机械 |
| 非确定但约束可判（npm 解析） | 约束满足验证（npm ci 不重掷、验一致） | 全机械 |
| 非确定且约束欠定（LLM codegen） | 只剩 hash 级变更检测；「重掷仍有效」不可机械判 | **重钉闸必须住人审** |

推论一（对 08-22 评审的重归类）：Kiro 的 Sync + 人工 approval checkpoints 不是 ABI 的胚胎、也不是实验期拐杖——**它是第三格在约束欠定生成器上的类型必然形态**（重钉事件 + 人审差分闸）。08-22 验证关曾疑「ABI 传感器按字面部分触发」，本帧下解除：那不是 ABI 等价物在长，是 lockfile 等价物在长。〔诚实注：「类型必然」为类型推演，Kiro 设计动机未证。〕

推论二（#214/#193 均续有效）：第三格**不交付「再生取代维护」**——维护没有消失，从「手写样本」换形为「审重钉差分」；代码仍是长命受审物。故 #214 主张（再生取代维护需 (a) 或 (b)）不被第三格证伪，#193 失效条件不因此触发。第三格是双维护泥潭与未建成的 ABI 之间的**现存稳定吸引子**。

**衰减律（体制的主要死法）**：重钉成本低于差分审查成本时，钉停止编码判断——Jest 官方把「测试挂了就 regenerate 而不查根因」列为要对抗的习惯，正是这条：一键重钉让 pin 文件退化为内容无关的信任放大器（#195 的 pin 域落点——钉的在场暗示审查发生过，而审查正是被一键重钉替代掉的动作）。

## 四、与既有滴的对位（写档自查）

- `regeneration-needs-an-abi-not-a-better-generator`(#214)：直接父滴。前提条款「两条路完备性未证」被本夜落定为「有第三格，但第三格不交付原命题」——补全非证伪。
- `mechanical-gate-needs-machine-detectable-target`(06-24)：类型学主刀的上游——对账关系可判则闸全机械，不可判则闸住人。
- `trace-presence-substitutes-for-the-check-it-invites`(#195)：衰减律落点。
- `load-bearing-not-quality-generates-blindness`(06-10)：Hyrum 既有承载，轴不同（承重→盲区 vs 绑样本→契约面失效），作谱系不作净新增。
- `backfill-is-the-channels-native-act`(#198) / `presence-benefit-splits-replica-verdict`(#197)：hash 缓存 + 机器管理副本是钉样本的仓内近亲（单源生成、整块盖写、hash 失效检测）——第三格在 gg 自家基建早有活体。
- `replay-gate-collapses-to-attestation-when-inputs-expire`(#213)：Workflow journal 的保质期注所引。

## 五、候选滴（过验证关前全文）

> ## 2026-08-24 / 夜间 / freeze-the-sample-not-the-sampler
>
> 非确定生成的治理在 #214 两条路外有第三格：不驯化采样器也不切绑定面，把掷点物理钉死（lockfile / 快照 / 生成代码入库 / journal），重掷收敛为离散、可 diff、可回滚的重钉事件——它不交付「再生取代维护」，维护换形为重钉差分审查，故为双维护与 ABI 之间的现存稳定吸引子；其与双维护的分界 = 钉样本永不手写 / desync 响亮失败 / 审查集中重钉点。
> 机械闭环程度 = 真源↔钉对账关系的机械可判程度：字节等同与约束满足可全机械（regenerate-and-diff / npm ci），约束欠定的生成只剩变更检测、「重掷仍有效」不可机械判——重钉闸必须住人审（Kiro 人审 approval 是此格类型必然，非 ABI 胚胎）。
> 衰减律：重钉便宜过差分审查时，钉停止编码判断，退化为内容无关信任放大器。

物理证据清单（交 evaluator）：
1. Workflow 工具自述：(prompt,opts) 缓存 / 禁 Date.now 保 resume / journal.jsonl〔本会话 system prompt 亲历逐字〕
2. Hyrum's Law 原文〔主会话 WebFetch 亲核逐字，hyrumslaw.com〕
3. sqlc diff 双句〔主会话 WebFetch 亲核逐字，docs.sqlc.dev/en/latest/howto/ci-cd.html〕
4. npm@5 默认 lockfile（blog.npmjs.org/post/161081169345）+ npm ci "exit with an error"（npm/cli docs）〔子代理原文级〕
5. Rust blog 2023-08-29 lockfile 政策变更逐字〔子代理原文级〕
6. Jest docs "fight against the habit of regenerating snapshots"〔子代理原文级〕+ Fujita ASE 2023〔摘要级〕
7. Kiro Sync + approval〔复用 08-22 档子代理证据〕
8. semver 判死文献缺口自标（调研代理 Q3 后半未达原文级，相应半句已降 gg 结构读法）

## 六、验证关 verdict

**PASSED-WITH-EDITS，五修全部采纳**（fresh evaluator，只读纪律遵守——自报仅只读 Bash 零写零网络，派单者 git status 物理核：工作树除本探索档与存量脏文件（auto_gg/2026-08-23.md）外无新增写痕）：

- **最强反驳点（留档）**：「第三格可被读作两条已知路的组合而非独立格：钉住期间『翻译确定』（路一分时复用）+ #192『机器管理缓存』的采样域搬运，则候选 = 零净新增。此击不致死：路一定义是『重掷不发生』，钉样本下重掷在每次重钉真实发生且欠定决策被重新定夺——『离散化的重掷』与『不发生的重掷』是不同类型（前者需住判断的闸，后者不需），#192 前提（确定生成、regenerate-and-diff 可复现）在采样器下物理不成立。但若不把这条分界写进谱系注，下一个读者会用这一击把它读塌。」
- 五修：① 谱系注接 #192（三件套 = 其机器缓存纪律迁非确定采样域，净新增钉在「重钉 = 重掷判断事件、diff 审查 = 判断落点」）；② 对 08-22 验证关留档「Kiro approval = ABI 胚胎」读法加显式改判注（非对 #214 正文冲突）；③ 前提块补证据分级；④ 衰减律接 #195 词根 + Jest 单源标注；⑤ journal 保质期接 #213。
- evaluator 独立确认：与 #214 是补全非复述；第三格存在性四独立域共撑（npm/sqlc/Jest/journal）剥任一不塌；衰减律例外（剥 Jest 降推定投影，已单源标注）；引文分级诚实（Hyrum 与 H1 卷 06-10 滴所引同句一致）；candidate-refuted 全库无复提。
- **派单者订正**：候选与本档初稿把 `regeneration-needs-an-abi` 误引为 #216，按视图分配表与 commit 75cd831 实为 **#214**，本档与终稿已全量订正（同会话 commit 前打磨，合法）。
- 修后滴文即 essence 当前卷 2026-08-24 条（#216），此处不重复（避免双源漂移）。
