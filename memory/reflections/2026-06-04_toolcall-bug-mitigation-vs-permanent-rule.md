---
date: 2026-06-04
slug: toolcall-bug-mitigation-vs-permanent-rule
summoner: monster
northstar_reach: #1 二阶效应
status: substantive-decision
---

# Reflection: 拆 tool-use 缓解清单——承重墙 vs 绷带 vs 伪命题

### 给父会话的最终输出（必填）

**推荐**：四条候选里没有一条是"绕 bug 的有效绷带"——不存在第二个 track，"临时缓解 track"是空桶/死锁载体。按下面四分法处理：

1. **#1 多次小 Edit** = 反向有害，不仅判绷带，要写进准则**反面**。理由：bug 是"该吐 tool_use 没吐出来"，N 个小 Edit = N 个 tool_use，每个都可能触发，总触发概率**单调上升**——这是把缓解写成催化剂。bug 期间正确方向**相反**：合并成一次 Write 减少 tool_use 暴露次数。
2. **#2 Write 替 heredoc** + **#4 拆 pipeline/写脚本** = 独立工程准则，进 CLAUDE.md。判据：**删掉"为绕 bug"这个动机，它们照样立得住**（#2 靠 Engineering Rule #1 专用工具优先，#4 靠 Code First）。bug 给它们的支持是 0——tool_use 数量/结构不变，对 bug 触发率零关联。
3. **#3 commit message 控短** = 噪音，从讨论中删除。commit message 是 Bash 工具的**参数内容**，bug 是 tool_use 的**数量/结构**解析失败——两者无因果。这是"bug 期间我紧张了什么都想压缩"误认成"压缩能缓解 bug"的幻觉关联。
4. **第五点（主代理括号里提的"文件不该大到要几百行一次性写"）** = 唯一真承重墙，但它是**既有准则的适用域扩展**不是新准则。文件职责切好（单文件<200行，CLAUDE.d 上下文治理已在做），"巨型 Write vs 多次 Edit"这个伪选择题根本不出现。载体已存在：`monster/CLAUDE.d/context-curation.md` 200 行拆分规则。

**理由（framing 元判断）**：主代理第三问方向对（不该把通用准则和绕 bug 混一张清单），但它把这当"待裁决选项"提出，实际结论更狠——**临时 track 不该存在**。① 临时 track 的撤除依赖"Anthropic 修了服务端 bug"这个**不可观测事件**（无 changelog、无触发信号）= essence `fermentation-without-detector` 精确形态，每个读取时点都是僵尸 ② 它装的 #1 还是反向有害的 = 有害且无撤除检测器 = 最坏死锁载体 ③ essence `default-bucket-as-deadlock`：没有可观测出口的桶 = 漏斗，"bug 修了就撤"是出口语义廉价版。

**真正有效的 bug 缓解根本不在这四条里**，且不是"工程准则"也不是"行为清单"——是**运行时配置策略**：降 effortLevel / 关 1M（降组合强度）+ 合并 tool_use 减暴露次数。载体不该是 CLAUDE.md。

**trade-off / 未核验假设**：① 我对 bug 机制的判断（tool_use 数量↑→触发率↑）基于父会话给的描述"该吐 tool_use 却没吐出来"——若真实机制是"单个 tool_use 内容过大导致解析失败"而非"数量多导致漏吐其一"，则 #1 的负关联判断要反转（这是最可能翻车点，建议父会话回查报错的实际 payload）② 我没有 Anthropic 服务端 bug 的物理证据，"不可观测"是基于"厂商不会为内部解析 bug 发 changelog"的合理推断，非实证。

**行动建议**：
- 进 CLAUDE.md：#2 #4 按"独立工程实践"措辞，**删掉一切 bug 引用**（带 bug 动机会让它们在 bug 修复后面临无意义的清理）。
- 不进任何地方：#3 删除。
- 写进准则反面 / known-issue 便签：#1 标"错误缓解方向，不要采纳"——防 `bug-shape-survives-fix` 复发（下个会话的 Claude 重新发明这个反向措施）。
- 若 Keith 想留临时缓解（"合并 tool_use 减暴露"，bug 存续期真有效）：**落 `inbox/` 或独立 `known-issues/` 便签，不进 CLAUDE.md**（物理位置即"临时"标签）；撤除检测器绑**可观测信号**——`连续 N 次 1M+xhigh 会话未再撞 tool_use 解析失败 → 便签作废`，把"等 Anthropic 修"（不可观测）换成"我自己会话不再撞"（可观测）= essence `idle-threshold-as-tripwire-not-answer` 落点。

### 核心假设

bug 机制 = "服务端在 1M+xhigh 偶发漏吐 tool_use 之一"，故有效缓解维度 = 降组合强度 + 减 tool_use 暴露次数。整个 #1 负关联判断挂在这个假设上。

### 可能出错的地方

最可能崩在 #1 的定性：若 bug 真因是"单个 tool_use payload 过大解析失败"而非"数量多漏吐其一"，则拆小 Edit 反而是正解，我把方向判反了。概率中等——父会话的描述偏向"数量/结构"侧但没给 payload 证据。

### 本次哪里思考得不够

没要父会话提供实际报错 payload 就下了 #1 的负关联强判断——这是 `physical-anchor` 的欠账：结论依赖的中间机制前提（bug 到底是数量触发还是单体触发）没物理核验。我用"合理推断"代替了"问一句"。

### 如果 N 个月后证明决策错了，最可能的根因

bug 机制和我假设的相反（单体 payload 触发 ≠ 数量触发），导致 #1 的"准则反面"措辞把唯一有效的缓解写成了禁令。

### 北极星触达

#1 二阶效应——主代理问的是"这四条怎么分类"，二阶洞察是"分类框架本身（混一张清单）错了，且'临时 track'这个桶会因撤除检测器不可观测而退化成永久僵尸"，看到的是规矩生命周期的二阶效应，不是规矩内容的一阶对错。

### essence 对齐自检（必填）

- **对位 slug**：`fermentation-without-detector`（临时 track 无撤除检测器=永久搁置）/ `default-bucket-as-deadlock`（无可观测出口的桶=漏斗）/ `idle-threshold-as-tripwire-not-answer`（撤除条件从不可观测换成可观测 tripwire）/ `bug-shape-survives-fix`（#1 反向措施会在下个会话复发）/ `physical-anchor`（结论依赖的中间前提=bug 机制未核验）
- **是否反着走**：潜在张力——`anchor-value-in-activation-not-in-content` 说"别把模型已会的抄进文档"，而我建议把 #2#4 写进 CLAUDE.md。但这两条本就是 monster 既有准则（Rule #1 / Code First）的重申，不是新抄知识，张力不成立——我建议的恰是"删掉 bug 引用、归并到既有准则"，方向一致。明示：无真实反走。
- **cross-check 关键词**：grep 用了 `detector` / `deadlock` / `tripwire` / `bug-shape` / `physical-anchor` / `default-bucket`

### essence 候选（可选）

- slug: temporary-rule-needs-observable-sunset
- 一句话: "临时规矩"的合法性不在它声称临时，在它的撤除条件是否可观测——撤除绑不可观测外部事件（厂商修 bug）= 永久僵尸；绑可观测自身信号（我的会话不再撞）才是真临时。`fermentation-without-detector` 在"规矩生命周期"维度的落点。
- 是否已 append 到 essence.md: N（候选，等 Keith review）

### 外部锚点（可选）

无工作区侧 ADR——本次是 monster 主代理的元讨论级架构咨询，决策实质归本 reflection + final message。
