---
date: 2026-05-02
mode: 工作
slug: cc-copilot-mirror-merge-or-split
status: substantive-decision
parent_session: cc-space (Keith)
question_summary: cc-copilot 战情室 vs mirror 自我观察台 两个 cc-space 内产品最终形态合并还是分开
---

# cc-copilot vs mirror — 产品形态架构判断

## 装配

- `tools/solution-space.md` — Claude 已倾向 B，必须强制展开多个候选避免被锁死
- `personas/conservative.md` — 故意为合并辩护一轮做对抗审视
- `tracks/architecture.md` 上下文（DQ-3 可演化性 / DQ-5 二阶效应）

## 核心假设

1. cc-copilot 的范式锚定明确（macOS instant-utility）→ 终态可合理预判
2. mirror 的 5 view 形态家族未收敛 + 自己写明 SOLVE-BEFORE-SYSTEMATIZE → 终态不可被合理预判
3. "按终态走"的应用前提是终态可被合理预判
4. 拆分的不可逆性 < 合并的不可逆性（合并后想拆，共享代码已形成耦合）

## 可能出错的地方

- 假设 1 cc-copilot 终态真清晰吗？v2.1-2.4 roadmap locked 不等于实际能跑通——派遣/战报/RPG/trajectory 后三阶段实际跑起来可能逼回 v1 副驾形态，那时"清晰终态"是幻觉
- 假设 4 拆分不可逆性低——这有反例，mirror 长出来后如果跟 cc-copilot 出现真实数据流耦合（比如 mirror 想读 cc-copilot 战报），那时拆开也会有成本
- 我的"终态 C > B"基于"mirror 不需要 UI"这个判断——但 H 想法生长器跑出第一份周报后 Keith 实际读体验可能强烈反对（"markdown 文件树看着累，要个聚合视图"），那时 C 退化为 B

## 推理盲区

- 我没问 Keith 的"使用情境"——他周一早 10 分钟用什么设备读？iPad/Mac/手机？这会大幅影响 mirror 载体判断
- 我没考虑 cc-copilot v2.3 行为皮肤（RPG）跟 mirror "30 年后的信"L 候选有概念叠合（都在做"Keith 的某种自我表征"）——这条线如果走深，两个产品会自然出现产品定位重叠，那时合并/拆分判断要重审
- 我倾向终态 C 可能受 conservative persona 装配的偏置——保守派天然偏向"少做"，但 Keith 不是保守派架构师，他可能更偏向"早造壳"

## 北极星触达

- **二阶效应（space）**：直接命中——本题就在判断"产品架构边界的二阶效应"。"先分开 + 共享层最小化 + 留合并通道"是显式的二阶效应优化（保留未来选择权）
- **动态学习反哺（time）**：弱触达——本次决策没整合外部新信息，主要靠 gg 既有架构 track + Anthropic agent 范式坐标
- **决策超越直觉（depth）**：核心命中——挑战了 Claude 倾向（attention pattern 论据偏弱）+ 挑战了 Keith 元方法论（指出"按终态走"的边界条件）

## N 个月后根因预判

如果本决策 6 个月后被证明错了，最可能的根因是：
- **路径 A**：mirror 实际跑出超过 3 个稳定 view 后，Keith 强烈感觉"碎在 markdown 文件里太散"——那时 mirror 自然要求产品壳。但这不算我决策错——SOLVE-BEFORE-SYSTEMATIZE 本来就是"等真的需要再造"，路径 A 反而是这个原则的成功落地
- **路径 B**：cc-copilot v2.2 战报需要"被 Keith 沉思阅读"（不是 glance），那时 cc-copilot 自己内部就出现了 sit-and-read 形态——证明我"attention pattern 推 surface 不推产品边界"的提醒是对的，cc-copilot 内部已经覆盖了 mirror 想做的事，mirror 失去独立必要性
- **真正错的路径**：如果 6 个月后两个产品的代码出现"看起来不共享其实共享"的隐性耦合（比如 mirror 偷偷读 cc-copilot 内部状态），证明"共享层只放数据采集解析"的边界没守住——这才是我决策错（边界定义太宽）

## 对齐度

- 完全对齐 Keith 偏好的"冷静笃定 + 高信息密度 + 拒绝讨好"——直接挑战了 Claude 的论证链
- 与 Keith 元方法论的关系：不简单服从也不反对，指出其边界条件——这是 KERNEL §2 铁律 1 "服从 + 讨论"的实例

## 给父会话的最终输出

**终态判断（按推荐顺序）**：
- 终态 C（推荐）：cc-copilot 长成产品 + mirror 不做产品壳（cron 脚本 + markdown 落盘 + Keith 用现有 markdown 阅读习惯消费）
- 终态 B（次选）：cc-copilot 做产品，mirror 做轻产品壳（Obsidian / 静态站本地浏览）
- 终态 A（不推荐）：合并

**核心理由（替换掉 Claude 倾向中较弱的 attention pattern 论据）**：

切两个产品的真正的轴不是 attention pattern（那只推 surface 边界，不推产品边界——VSCode/Things 3 的反例），而是：
1. **设计哲学对立**：cc-copilot 是 observability（信号清晰、误报为耻），mirror 是 introspection（宁可多想几条歪的也别漏掉）——同一 owner 背两套相反直觉
2. **演化方向不对称**：cc-copilot 终态明确（5 阶段 roadmap locked），mirror 终态模糊（5 view 候选只有 H 起手，且自己写明 SOLVE-BEFORE-SYSTEMATIZE）
3. **失败模式隔离需求**：cc-copilot 失败窄+快修，mirror 失败慢性+污染仪式感——绑一起会让 cc-copilot 的故障污染 mirror 在 Keith 心里的"周一早晨打开它"的仪式感

**对 5 个具体问题的回答**：
- Q1 分开（基于上述三轴，不基于 attention pattern）
- Q2 mirror 载体推荐文件系统 + markdown + 现有阅读习惯，不造 UI；排除邮件（SMTP 债）/Dashboard（违反 SOLVE-BEFORE-SYSTEMATIZE）/Widget（撞 glance 范式）
- Q3 不回答（终态是分开）；但若未来 emergent 出现入口共享需求，正确做法是 menubar 提供"打开 mirror 报告"的快捷入口而非渲染共享
- Q4 共享层严格限制在数据采集+解析层（transcript.py 已共享，inbox/threads 读取器按需抽，Keith 画像直接 Read 不抽），不共享任何带展示意图的代码——这条边界守住产品就永远拆得开
- Q5 Keith 元方法论"按终态走"是好默认，但本场景是它的边界例外——mirror 端的终态目前不可被合理预判，强行预判 = 把架构师偏好投射成"终态" = 真正的过早抽象。正确做法：cc-copilot 按终态走，mirror 按 emergent 走，两者关系按"先分开 + 共享层最小化 + 留合并通道"走

**额外提醒**：定终态架构本身没问题，但定的"终态"必须诚实承认"哪部分能看到、哪部分看不到"。看不到的部分宣称看到 = 把执行不确定性掩盖为架构确定性。

**外部锚点**：
- cc-space/threads/cc-copilot.md
- cc-space/threads/mirror-self-observatory.md
- ~/githubProject/cc-copilot/design-brief.md
- cc-space/mirror/CLAUDE.md（SOLVE-BEFORE-SYSTEMATIZE 约束源）
