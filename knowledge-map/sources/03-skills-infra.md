# skills 体系与基础设施机制清单（侦察原件 · 2026-07-10）

> subagent 通读 ~/.agents/skills/、skill-notes/、cc-connect 安装目录、scheduled/、web-access、codex plugin 后产出。

## 组 1 — skills 生命周期体系

| 机制 | 是什么 | 文件落点 | 原理 |
|---|---|---|---|
| skill-creator | 起草→写测试 prompt→跑 eval→改写的迭代闭环，含 description 触发优化 | `~/.agents/skills/skill-creator/SKILL.md` | 技能库的生成器 |
| skill-auditor | 只审自研 skill，四档评分，从不自动改文件 | `~/.agents/skills/skill-auditor/SKILL.md` | generator-evaluator 分离的静态质量门禁 |
| done（会话复盘） | Step0 未闭合盘点→叙事→沉淀写 skill-notes/essence；auto 会话强制最小归档 | `~/.agents/skills/done/SKILL.md` | 持续学习闭环 |
| search-skill | 搜索/安装外部 marketplace skill，三级信任源，装前扫注入迹象 | `~/.agents/skills/search-skill/SKILL.md` | 工具发现 + 供应链安全 |
| prompt-writer | 单体 system prompt 编写/诊断，"每行必须可执行行为改变/位置即权重" | `~/.agents/skills/prompt-writer/SKILL.md` | 元提示词工程 |
| skill-notes 反哺 | done 产出的持久化笔记按 skill 名归档，调用前先读 | `~/.agents/skill-notes/<name>.md`（16 个） | 经验回灌（experience replay） |
| 软链装配 | `~/.claude/skills/` 软链 → `~/.agents/skills/` 物理位置 | 两目录 | 物理存储与运行时装载解耦 |

## 组 2 — 通知通道

| 机制 | 是什么 | 原理 |
|---|---|---|
| notify.sh 唯一出口 | 飞书 webhook，三级 severity，无状态无 token | 副作用型工具调用的集中治理 |
| trace 账本 | 每条通知留永久 trace 文件（`sent/YYYY-MM-DD/`），支持回溯 | 可观测性/审计日志 |
| 项目归属推断 | --project > 环境变量 > cwd 推断 > 默认 gg 四级优先级 | 多租户身份推断 |

## 组 3 — cc-connect（消息桥）

| 机制 | 是什么 | 原理 |
|---|---|---|
| 桥接主体 | npm 全局包（外来，非自研），桥接本地 agent 到飞书/钉钉/Slack 等，双向对话 | 人机协作接口层 |
| voice-reply | 飞书 bot 场景语音播报开关 | 多模态输出适配 |
| cron 会话 + relay/send | 定时会话触发 / 多 bot 中继 / 附件投递 | 消息路由中继；与 notify 互补（双向桥 vs 单向出口） |

## 组 4 — 定时任务

| 机制 | 是什么 | 原理 |
|---|---|---|
| launchd plist = 任务 SSOT | 一任务一 plist，触发时间+prompt 全在文件里，失败不重试 | 调度器 + 声明式配置 |
| run-task.sh 等工具集 | 装载/卸载/查日志/立即触发 | 任务生命周期管理 |
| 桌面客户端迁移校准 | 2026-06-12 起 launchd→客户端 routine，plist 降级存档；prompt 入口不变 | 基础设施迁移中的契约不变量 |
| daily-word / gg-explore 推送管道 | roam-launch → run-task → push-last-run 剥噪音经 notify 推送；空输出照推 | **观察者隔离**——"会被 Keith 看到"只活在传输层，不进探索上下文（对应 essence `caged-freedom`） |

## 组 5 — 浏览器 CDP

| 机制 | 是什么 | 原理 |
|---|---|---|
| CDP Proxy 直连真实 Chrome | 直连日常 Chrome（9222），带真实登录态/指纹，本质不是 bot | "直接是这个人"而非"伪装成人"——岔路选择 |
| check-deps.mjs 前置检查 | 联网前检查 Node/Chrome 就绪 | 工具可用性前置校验 |
| 浏览哲学四步 | 定成功标准→选直达起点→结果当证据→按标准收口 | 工具路由决策树 |
| /click 非严格模式 + strict 开关 | 可逆操作快路径；不可逆操作 strict=1 拒点歧义 selector | 风险分级的动作确认 |

## 组 6 — 跨模型辅审（codex plugin）

| 机制 | 是什么 | 原理 |
|---|---|---|
| /codex:adversarial-review | review-only，挑战方案假设，禁止顺手修复 | 跨模型对抗性验证——规避同模型盲区重叠 |
| codex-rescue | 纯转发 wrapper，卡住时求助升级 | escalation on stuck 的标准化 |
| codex-cli-runtime / gpt-5-4-prompting | 调用 codex runtime 的底层协议 + prompt 指南 | 供应商适配层 |

## 最独特的 3 个设计（侦察者观察）

1. **观察者隔离作为一等公民架构原则**——推送管道刻意把"有观众"锁死在传输层，防"知道有人看"腐蚀探索质量（表演化）。
2. **真用户路径 vs 伪装路径的岔路选择**——CDP 直连本人 Chrome，把反爬对抗降级为不存在的问题。
3. **单点出口 + trace 账本的强制收拢**——所有异步外推物理收拢到唯一脚本，用架构强制换审计可回溯。
