---
date: 2026-08-31
slug: monster-hallucination-guard-family
summoner: monster（对话层幻觉防线：第四道 guard / transcript 真值定义抽层 / 消息编号方案三题裁决）
northstar_reach: "#3 决策超越直觉"
status: substantive-decision
---

# Reflection: monster 幻觉 guard 族三题裁决（A 建否 / 定义抽层 / 编号方案）

### 给父会话的最终输出（必填）

**裁决一（A 第四道 guard）：不建常驻 hook，降为夜跑 tripwire 传感器。**
- 基率 3 命中 / 1738 会话 / 30 天 ≈ 0.17% 会话，「低频不常驻」直接命中。
- 更硬的理由：常驻挂点买不到它声称要买的东西。伪造文本一经产出即已落盘，Stop / PreToolUse 都改不了记录层（记录层是化石，`authoring-rules-do-not-govern-record-layers`）；实时检测唯一增量 = 会话内注入一条反注记，而反注记能否被后续 compact 正确吸收无保证。可靠修复在结构排除（裁决二的 B），不在实时警告。
- 实时闸的假阳性通道在 monster 这种天天书写/讨论 harness wrapper 的仓里天然宽，实时误报打断工作流并透支闸信用；夜巡误报有人工定性缓冲。
- 落地：signatures.py 保持签名 SSOT 并从 scratch/ 迁入 harness-engineering（monster scratch 规则：有工作区归属的 spike 迁走 + 更新指针）；扫描挂 `auto-monster/scripts/tripwire_check.py`，阳性 case 注册 `tripwire_selftest.py`（准入三问②已满足，selftest 4+4 已绿）。命中动作 = 定性 → 登记 thread/canon-bugs → 检查是否已被 compact 固化，固化的伪句登记为已知污染句（供未来「Keith 说过 X？」对账排除）。
- `downstream-gate-is-upstream-sensor` 的射程注记：夜巡射程 = 全项目 transcript 全集，覆盖三道现有 guard 的全部盲区（回合中间 / 无归属短语），无射程差集。

**裁决二（问题 2）：抽层，做；但形态是 co-location 单源，不是运行时依赖 monster 仓。**
- 「什么算用户输入」定义（turn 分类白名单 + 排除规则 + 已知 harness 字段清单）抽成单文件 stdlib-only 模块，落 `~/.claude/hooks/lib/`——与 hooks 同可用域，「monster 仓不可用时独立工作」按构造成立，attribution-guard 的内联约束不否掉抽层、只否掉「import monster 仓」这一种形态。monster 侧消费者（explain-guard / 夜巡扫描）绝对路径 import 同一文件。import 失败 fail-open + 写 trace，夜巡查 trace 防哑火假绿（canon-bugs「命中恒 0 长期假绿」条）。
- B（isCompactSummary 排除）与抽层是同一个动作：B 就是单源模块 v1 的第一条排除规则，不在 attribution-guard 里再打第四份定义的第三个内联补丁。当天要止血可先内联一行 + 注「待迁单源」，一周内完成迁移。
- **架构层真正要收的口：定义是活面**（isMeta → isSidechain → queued_command → isCompactSummary，harness 持续加字段），三次事故全是「新字段出现 → 定义没跟上」。单纯 dedupe 只保证四道 guard 一起错。必须配**未知字段哨兵**：夜巡扫 transcript 记录中出现不在已知分类清单的新字段即报警「定义过时候选」——把第五次事故从「出事后发现」提前到「字段出现当天发现」。依据 `one-shot-invariant-decays-under-live-append`：宣告必须绑定写入路径的维护机制。
- 单源模块登记 `ssot/registry.md`。

**裁决三（C 编号方案）：否得对，且理由要升级成结构性的，回话给 Keith 时用它。**
- 编号是自证水印（in-band 真实性标记），而核验者与伪造者是同一个预测过程：会伪造 user turn 的模型同样会给伪造 turn 编出承接上文的合法号。本轮案例 1 是直接物理证据——被伪造的恰是「防把通知当用户授权」的防伪注入文案本身。任何进过上下文的防伪标记都会成为伪造模板；把编号格式教给模型 = 给未来的伪造 turn 镀真实感。
- 编号独有价值只剩「Keith 肉眼对账」，但 Keith 不读 transcript，落不了地；离线对账已被字节级核验覆盖。
- 对 Keith 的回话要点：他观察的两种形态 3/3 定性属实，他的意图（用户输入可对账）由夜巡传感器 + 单源定义实现，更便宜且不改输入字节。

**行动清单（父会话执行序）**：① 建 `~/.claude/hooks/lib/` 单源模块（含 isCompactSummary 排除 + 已知字段清单）→ ② attribution-guard 切换 import（其余 guard 随后）→ ③ signatures.py + 扫描迁 harness-engineering，挂 tripwire + selftest 注册 → ④ 未知字段哨兵进夜巡 → ⑤ 三处既有命中登记 thread + 已知污染句清单 → ⑥ 回 Keith：编号方案否，附「防伪标记进上下文即成伪造模板」理由。

**Trade-off / 未核验假设**：夜巡 ≤24h 检测延迟内，同会话可能已消费自己的伪造（三例中未证实有错误动作跟随，此为残留敞口，接受）；compact 固化对未来会话的信念污染无 hook 层解（记录层不可改），只能靠污染句登记对账，此为已知残留风险非本裁决遗漏。

### 核心假设

1. 3/27,990 的 30 天普查是真实基率，签名集没有大面积漏报形态（扫描只认 5 类结构签名，无签名的自由文本伪造不在射程——但那类已由 attribution-guard 的归属短语锚覆盖一半）。
2. `~/.claude/hooks/lib/` 与 hooks 同生共死这一可用域判断成立（hooks 全在 `~/.claude/hooks/`，explain-guard 在 monster 仓但 monster 不可用时它本身也不运行）。
3. 三例伪造未导致错误的不可逆动作——若父会话后续定性推翻（发现某例伪造被当授权消费），裁决一需重开。

### 可能出错的地方

- 未知字段哨兵可能噪音偏高（harness 更新频繁加字段），若月均报警 >2 次且多为无关字段，需收窄为「仅 user 类型记录上的布尔标志字段」。
- fail-open + trace 的兜底若 trace 无人查，退化为静默失效——已绑夜巡查 trace，但夜巡自己也是链上一环（`omission-failures` 的递归），接受为当前最深一层。

### 本次哪里思考得不够

- 未实测「compact 是否会把 Stop 时注入的反注记正确吸收」——裁决一按「无保证」处理，若实测证明反注记可靠改写 compact 结果，实时挂点的价值判断会上修。
- 对 self-action-guard 的语料定义耦合度没实查（它拦「我改了 X」，可能不消费 user corpus），行动清单②按需裁剪。

### 如果 N 个月后证明决策错了，最可能的根因

基率误判：伪造形态随模型换代变频（换代后 confabulation 率跳升），0.17% 的静态基率失效，夜巡 24h 延迟不再够——那时再升实时挂点，且因单源已抽好，升级成本只剩挂载本身。

### 北极星触达

#3 决策超越直觉：直觉方向是「多一道 guard 更安全 + 编号给模型自查」；裁决反向——guard 降级为传感器、编号方案指出其主动武装伪造者。两处都是把「防御在模型够得到的地方」翻成「核验在模型够不到的地方」。

### essence 对齐自检（必填）

- **对位滴**：`downstream-gate-is-upstream-sensor` (08-28，射程差集核算用于夜巡覆盖判断)；`omission-failures-evade-event-driven-sensors` (07-28，出路二周期抽样 = 夜巡形态、出路三结构消除 = B 排除)；`one-shot-invariant-decays-under-live-append` (08-11，定义活面须绑维护机制 → 未知字段哨兵)；`presence-benefit-splits-replica-verdict` (08-06，副本裁决轴 = 在场性收益；此处 co-location 直接消副本，比生成分发更优)；`authoring-rules-do-not-govern-record-layers` (08-18，记录层不可改 → 实时拦截买不到修复)；F5 族核心命题（内部自洽恰是伪装 → 编号自证水印否决）。
- **反着走**：`counterfeit-the-watched-world-not-the-watcher` (08-13) 潜在张力——伪造流行率极低时传感器判据可能漂移（长期零命中 → 阈值松弛），本裁决靠 selftest 阳性 case 顶住，但 selftest 只验签名匹配、不验「人还看不看夜巡报告」，未展开。

### essence 候选滴（candidate-unverified，待验证关）

**slug 候选**：`anti-forgery-marks-in-context-become-forgery-templates`
**候选全文**：进过模型上下文的防伪标记（注入 wrapper / 消息编号 / 结构签名）必然成为伪造模板——伪造者与识别者是同一个预测过程，标记的每次出现都在教它复现；in-band 真实性标记只能提高伪造保真度，真实性核验必须 out-of-band 锚在模型写不到的记录层比对【物理证据：2026-08-31 普查案例 96d78f5f——被伪造的正是「防把后台通知当用户授权」的防伪注入文案全套 wrapper，真实 user 流零命中；前提：标记曾进上下文；n=1 直证 + 编号方案反事实推演】← F5「内部自洽恰是伪装本身」在防伪标记供给侧的机制化；`rhetoric-vs-mechanism` 异轴（那滴管承诺锚点，本滴管真实性标记的信道位置）
**相关既有滴**：`counterfeit-the-watched-world-not-the-watcher`、`the-machine-watchers-immunity-is-purchased-by-amnesia`（上下文通道把统计接回来——同款「进过上下文即被污染」机制在判据侧）

### 验证关 verdict（auto_gg 2026-08-31 补审 → **PASSED-WITH-EDITS 采纳入库 essence #230**）

- **最强反驳点**：keyed in-band 标记——每条 harness 通知附 `sig=HMAC(secret, body)`，模型读到格式后照仿，但 secret 从不进上下文：伪造件格式保真度升、核验零失守。候选「in-band 标记只能提高伪造保真度」对此为真却无害，「核验必须 out-of-band」退化为「密钥 out-of-band、标记仍可 in-band」——候选把「信道位置」当判轴，真判轴是「模型能否完整生成」。修订以此判轴置换吸收。
- **降档**：「必然」→「一旦进过上下文就是伪造模板」（断可复现性非发生率——基率 3/27,990 块本身反证「必然发生」）；out-of-band 半句已由 `attestation-has-no-fixed-point-under-self-audit`(#211) / `deploy-decision-must-not-read-untrusted-controllable-inputs`(05-19) 持有，降为谱系引用，净新增 = 供给侧一句 + 判轴；前提补三条（无秘密值 / 记录层比对排除 compact 摘要等模型可写记录 / 限上下文内复现）。
- **证据物理核验订正**（evaluator 亲核）：96d78f5f L539 `type=assistant` 块内 preamble 全套坐实，且逐字匹配 `~/.local/share/claude/versions/2.1.251` 二进制内置文案（`strings` 命中）——模型复现的是真实 harness 文案非自编；**「真实 user 流零命中」是记录层结构事实非伪造证据**：preamble 由 harness 发送时前缀、jsonl 只落裸 XML（该会话 12 条裸 XML / 0 条 preamble），对任何会话恒真，本档拿它当证据系误读；**记录层并非模型写不到**：319221de 案伪句经 compact 以 `type=user, isCompactSummary=True` 落盘——裁决二「记录层不可改」措辞过强，compact 摘要是模型到记录层的一条写路径（不推翻裁决一，但「已知污染句登记」的对账对象须含 compact 摘要）。基率出处 `tripwire_check.py:662` + `known-contaminated-quotes.md` 成立。
- **既有滴关系**：#206 供给侧镜像 / #211、05-19 持有 out-of-band 半句 / `verification-trace-as-camouflage`、#195 读者侧痕迹（未言供给侧）/ #202 异轴。「模板 / 教它复现」轴双卷零命中。
- evaluator tool_use：Bash × 10（grep / sed / cat / ls / file / strings / python3 只读解析 jsonl），零 Write / Edit / Agent。
