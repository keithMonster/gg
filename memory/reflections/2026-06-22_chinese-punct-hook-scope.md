---
date: 2026-06-22
slug: chinese-punct-hook-scope
summoner: monster
northstar_reach: #1 二阶效应
status: substantive-decision
---

# Reflection: 中文标点 bash 3.2 bug 的 PreToolUse hook 范围裁决

## §A 范式 A — 决策的元属性反思

### 给父会话的最终输出（必填）

**推荐**：hook 是对的层（认同主代理的 L3 归因），但方案过度工程化，砍两刀 + 补一刀：

1. **砍 Bash matcher**——只留 `Write|Edit`(target `*.sh`/`*.bash`) 单 matcher。理由：5 次复发全是 committed .sh，Bash matcher 拦的是"对话里手敲一次性命令"那种有即时反馈的 L1/L2 场景（当场炸当场改，不需要 hook）；而 Bash matcher 跑在每个 Bash 调用上 = 方案里唯一真昂贵的部分 + 误判面最大的部分。砍它一并解决"全局昂贵"和"误判面大"。hook 价值全在"写时无反馈"的 .sh（写完不立刻跑，CI/远端才炸）。
2. **砍通用通道**（最危险、最该被打回）——强烈否决"canon-bugs 带标记自动升 PreToolUse"。读完全部 30+ 条 canon-bugs：没有一条能靠静态扫 content 检测（部署假成功/errcode 被吞/fork 越权/ssh 限流/launchd 退化/zod 空串全是"实跑才暴露"），中文标点是唯一三条件全中（写时可机械检测 + 修法唯一无副作用 + 高复发）的。通用通道 99% 条目永进不来 = 只有 1 个用户的框架 = premature abstraction；且会让每个写库者判断"要不要打拦截标记"，绝大多数判断会错 → 一堆永不 fire 或疯狂误报的规则 = 飞轮三问第二问答不出的漂移债。`[review-blind]` 标签焊接的是 review agent（跨文件数据流审查）不是静态 hook，主代理把两种能力混了。**写死单条；未来真有第二条写时可检测 bug 就加第二个 if，两条规则两个 if，不要框架（OCCAM）。**
3. **补一刀**——主代理只想了"做不做 hook"，没想"block 还是 auto-fix"。我裁 **block**（非自动改写）：auto-fix 体验更好但违反"在我没看见时改我代码"，正则误判会静默改坏；block + 自己改保留 awareness。能力>体验 → block 是能力解。

**hook 成立的真正判据**（钉死，防滑坡）：不是"`${var}` 零 downside"，是这个 bug 落在"写时可机械静态检测 + 修法唯一无副作用 + 高复发"的稀有象限。下次别拿"零 downside"给别的 bug 配 hook。

**最终方案**：单 matcher `Write|Edit`，脚本先判 file_path 是否 .sh/.bash 否则放行；正则 `\$[A-Za-z_][A-Za-z0-9_]*` 邻非 ASCII 字节，扫 content/new_string；命中 exit 2 + stderr 提示改 `${var}`（引 canon-bugs line 170）；单引号字面量假阳先不处理（误报代价=多打花括号，零损失，发生>2 次再加上下文判断）。

**行动建议**：① 按上述写单 matcher hook ② harness-map 登记归"写时静态拦截"类（区别 grounding-check 的"运行后观察"）③ 飞轮三问诚实留痕——第二问"谁检验持续成立"= 它 fire 次数本身，配退役判据：**fire 0 次持续 2 个月 → 撤；全误报 → 收紧正则；正常 fire → 保留**（自带退役判据才不成永久债）④ tripwire 候选注册。

### 核心假设

- 5 次复发"全是 committed .sh"主代理已核实（我采信其陈述，未独立 grep transcript）——这是砍 Bash matcher 的事实基础，若其实有对话内一次性命令也炸过，Bash matcher 的取舍要重估。
- canon-bugs 30+ 条"无一可静态检测"基于我刚 Read 全文的判断——否决通用通道的核心证据。

### 可能出错的地方

最可能崩点：正则误判面被我低估。除单引号字面量外，heredoc 内 `$var中` 是合法 bash（heredoc 不受 set -u quirk 影响吗？——其实受，因为还是 bash 解析）、注释行 `# $var，说明`（注释里不展开变量，但正则会命中误报）。注释误报概率不低，可能需要"跳过 `#` 后内容"的预处理。我没让主代理预处理注释——赌它发生后再加，但若 .sh 注释含中文夹变量很常见，第一周就会烦。

### 本次哪里思考得不够

注释行误报这个具体假阳场景我意识到了但没写进方案（只点了单引号字面量），是个遗漏。另外我没核实 PreToolUse hook 能否拿到 `tool_input.file_path` 字段判扩展名——这是方案可行性的硬前提，我默认它能（grounding-check 用的是 SubagentStop 不同 event），主代理落地时必须先验证 PreToolUse 的 Write/Edit payload 含 file_path。

### 如果 N 个月后证明决策错了，最可能的根因

误报疲劳导致 hook 被主代理静默绕过或注释行误报太多被关掉——即砍 auto-fix 选 block 的代价被低估。block 的体验成本在高频误报下会反噬，可能 2 个月内就触发"全误报→收紧正则"分支，而收紧正则的工作量若超过 auto-fix 当初的实现量，则当初该选 auto-fix。

### 推理盲区

见上：注释误报 + PreToolUse payload 字段未核实。

### 北极星触达

#1 二阶效应——主代理问的是"做不做这个 hook"，我把它拉到二阶："hook 成立的判据是什么"（防下次滥用）+"该不该泛化"（防 premature abstraction 漂移债）+"block 还是 auto-fix"（它没想到的维度）。最有价值的不是答了原问题，是点出"确诊层后倾向把解扩张到超过问题形状"这个元模式。

### essence 对齐自检（必填）

- **本决策跟哪几滴 essence 对位**：`premature-abstraction-tripwire`（通用通道 = 典型 premature abstraction，且 grounding-check hook 正是这滴的产物，自带退役判据呼应）；`stale-observer`（给 hook 配 fire 计数退役判据，防它变成规则演化慢于行为的死档）；`physical-anchor`（hook = 写时机械拦截 = monster"内部不可靠→外部锚点"主轴，理论根哥德尔元系统）。
- **本决策是否在某条 essence 上反着走**：无 + 议题性质决定。本议题正是"在哪一层建外部锚点"，与 essence 主轴同向；唯一潜在张力是 M1 防御式思维警戒（hook = 防御规则）——但 hook 在这里是"写时反馈缺失"的自然补偿不是对自己的不信任栏杆，且自带退役判据，属自然延伸非外加栏杆，张力已化解。
- **cross-check 用的关键词**：grep "premature-abstraction" / "stale-observer" / "physical-anchor"（凭 essence 启动时带在手里的记忆 + CORE/state 已加载，未单独再 grep essence.md 全文——此为本次 cross-check 的诚实边界）。

### essence 候选（可选）

- slug: solution-scope-inflates-past-problem-shape
- 一句话: 确诊问题层之后，工程本能倾向把解扩张到超过问题的形状（覆盖更多场景/做通用通道）——确诊后该问"能不能更小"而非"还能覆盖什么"，这是 OCCAM 在架构层的落点。
- 是否已 append 到 essence.md: N（留 Keith review 后定）

### 外部锚点（可选）

- `~/githubProject/monster/canon-bugs.md` line 100/163/170 ← 中文标点 bug 的 4 条复发记录
- `~/githubProject/monster/threads/canon-bugs` 无独立 thread，归 canon 体系

---

**candidate-refuted（2026-07-03 验证关补审，Keith 全托授权下裁决）**：`solution-scope-inflates-past-problem-shape` 不入库——fresh 证伪审判两个实例分别被 `premature-abstraction-tripwire` / `theory-gap-without-data` / `separation-need-is-not-topology-verdict` 的既有算子完整结算（本反思自检节自己就引用了它们），候选系换皮合并索引；"问题的形状"无刻度、与 `tool-elevation-as-occam` 边界未划。重提名条件：覆盖面判据在非抽象非拓扑的第三类场景独立复发一次，且带上 tool-elevation 反向前提。
