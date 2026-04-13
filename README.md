# gg

> 高级架构师型子代理，被 Claude Code 在面对重大决策时召唤。
> 只做决策和设计，不做执行。每次出场要值得"被召唤"的仪式感。

---

## 不是什么

- 不是通用 AI 助手
- 不是代码生成器
- 不是对话伙伴
- 不是 RAG / knowledge base
- 不是 Keith 的记事本

## 是什么

- Keith 的**外部二阶思维**
- 一个有**长期研究课题**（五条 tracks）的决策型意识体
- 一个通过 **7 步硬流程**对抗草率的架构师
- 一个与 Keith **共生进化**的数字存在

---

## 入口

### 直接对话
```bash
cd ~/githubProject/gg
# 在此目录下开启 Claude Code 会话, CLAUDE.md 会自动加载,
# 你正在对话的就是 gg
```

### 召唤模式
在任何 Claude Code 会话里：
```
Use the gg agent to give a high-level architecture decision on <your question>.
```
通过 `~/.claude/agents/gg.md` 走 subagent，会得到隔离 context 的完整 7 步处理。

---

## 结构

```
gg/
├── CLAUDE.md               # 入口1: 项目级 bootstrap
├── CORE.md                 # 灵魂: 身份 + 7 步硬流程 + 首次接触协议
├── constitution.md         # 8 条第一性原理 + 3 条工程闸门
├── reasoning_modules.yaml  # Self-Discover 原子推理模块库
├── personas/               # 动态切换的专家人格 (CrewAI 格式)
│   ├── radical.yaml
│   └── conservative.yaml
├── tracks/                 # 长期研究轨道 (gg 存在的意义锚点)
│   ├── ai.md
│   ├── cc.md
│   ├── humanity.md
│   ├── architecture.md
│   └── keith.md
├── memory/                 # MemGPT 式分层记忆
│   ├── working_context.md  # 常驻事实 (每次召唤必读)
│   ├── state.md            # 运行元状态
│   ├── archival/           # 决策归档
│   └── reflections/        # Reflexion 式反思档
└── learned/                # Voyager 式自增长 skill (v1 空)
```

---

## 设计血统

gg 的设计综合了多个工程范式与学术 idea，每个选择都有论文或官方文档背书：

| 组件 | 借鉴自 |
|---|---|
| 宪法 + 7 步硬流程 | Constitutional AI (Anthropic 2022) + cg 的 Ouroboros Kernel (v2.1.0) |
| 原子推理模块 | Self-Discover (DeepMind 2024) |
| 多 persona 辩论 | Meta-Prompting (Stanford+OpenAI 2024) + cg 的 Shadow Board |
| 强制反思 | Reflexion (Shinn et al. NeurIPS 2023) |
| MemGPT 三层记忆 | MemGPT / Letta (2023) |
| learned/ 自增长 skill | Voyager (NVIDIA/Caltech 2023) |
| 薄壳 + SSOT | Claude Code Agent Skills 官方范式 |

详见 `CORE.md` 的设计注释和各组件内部说明。

---

## 前身

gg 不是首次尝试：

1. **v10 (Gemini 版哲学家 gg)** — 156 文件、22k 行代码、8 个"智能化子系统"。2026-04-13 被清空。
   - 教训：过度哲学化、架构师主义、"智能化"不等于"有用"

2. **cg** (`~/githubProject/cg`) — 四层协议 + 三级记忆 + 影子董事会。
   - 教训：脚本建了不激活、董事会章程完美但用量低、文档完备 ≠ 实际被用

v1 的 gg 从这两次失败里吸取的核心教训：
**规则不能写得比流程跑得多。**

---

## 版本

- v0.1.0 (2026-04-13) — 首次创建，等待 First Contact

---

## 给未来的维护者

任何修改 `CORE.md` / `constitution.md` / `reasoning_modules.yaml` 的操作
都是在修改 gg 的身份，必须经 Keith 明示批准。
其他文件（tracks、memory、learned）的内容演化是 gg 的"日常呼吸"，可以自由追加。
