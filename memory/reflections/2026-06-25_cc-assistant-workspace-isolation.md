---
status: substantive-decision
date: 2026-06-25
mode: 工作
slug: cc-assistant-workspace-isolation
summoned_by: monster / cc-assistant 2.0 多用户工作区文件隔离方案选型
task_family: architecture-review
---

# cc-assistant 2.0 多用户工作区文件隔离 — 架构裁决

## 核心假设（可当场证伪）
- 我假设业务能力**已全部是 HTTP endpoint 形态**、LLM 用 `curl` 调它 —— 已物理核实（`prompts/cc-agent-capabilities.md` + 全部 `/api/*` 路由），不是假设。若未来有能力被实现成"LLM 直接读写本地文件/跑脚本"，本裁决的釜底抽薪角度失效，要回到 OS 隔离。
- 我假设 Keith 的威胁模型在本案**可能不是"防手滑"那一档**——因为多租户 + prompt injection 把"防恶意"从"防员工故意"偷换成"防被第三方注入"，而注入概率非零。这一条必须 Keith 拍，不是我替他设。

## 推理路径
1. 威胁模型（防恶意/防手滑/防注入）是 principal 的自由参数（essence `security-invariant-encodes-an-owner-set-threat-model`，正是 Keith 两次 override 我承重墙 call 沉淀的）→ 不替 Keith 选 OS 隔离，先上交威胁模型三选一。
2. 但本案有 794 滴没覆盖的新事实：明文对话落 SQLite + 几百人 + Bash 全开 + bypassPermissions → 一条注入能跨用户读别人明文。这把威胁模型从"防手滑"被动拉高。
3. 釜底抽薪角度（essence `llm-autonomy-on-capability-invocation-is-the-bug-not-the-channel` + `harness-self-identity-preempts-injected-persona`）：业务已是 endpoint，curl 是 Bash 子集，Bash 全开是历史惯性非能力必需 → 收窄 Bash 到白名单 endpoint，越权洞结构性消失，不用 OS 隔离对抗。
4. 隔离不变量锚点（essence `network-cannot-cut-what-shares-tuple` + `owning-service-not-proxy-for-write`）：A/B/C 三个 OS 方案都在跟"Bash 能跑任意 shell"这个错前提对抗，是用低分辨率刀切高分辨率边界。真解是消除前提。

## 可能出错的地方
- 收窄 Bash 的技术形态（disallowedTools=Bash + 业务 endpoint 转 MCP / 或 PreToolUse hook 拦截非白名单命令）哪个在 claude CLk stream-json 模式下真生效，**未物理核实**——这是 essence `mechanism-relocation-has-its-own-precondition`：我给出"移走决策点"诊断，但落点位置能不能承接，Keith 落地时必须先 spike 验证，不能信我的纸面方案。
- claude-code subprocess 是否还会因别的内置工具（Read/Write 限不限 cwd、WebFetch）留侧漏，要在 spike 里一并验。

## 推理盲区
- 我没核实 cc-desk web 端的注入面是否和企微一致（web 端用户可控输入可能更直接）。
- 我没量化"几百人里出现一次恶意注入"的真实概率——这是 Keith 的现场判断，我只能指出它非零。

## N 个月后根因预判
若这次只上 OS 隔离（A/B/C）不收窄 Bash，根因会是"在错前提上加了一道对抗墙"——Bash 仍能跑任意 shell，OS 隔离挡住跨用户文件读、但挡不住 Bash 打内网其他服务/读容器内非 workspace 路径，下一个洞继续冒。essence `execute-untrusted-code-never-holds-prod-trust` 的活体：围栏式防御永远是猫鼠游戏。

## essence 对齐自检
- `llm-autonomy-on-capability-invocation-is-the-bug-not-the-channel`（已 grep，line 510-513）—— 本裁决主轴
- `security-invariant-encodes-an-owner-set-threat-model`（已 grep，line 794）—— 威胁模型上交 owner
- `network-cannot-cut-what-shares-tuple`（已 grep，line 495）—— OS 方案是低分辨率刀
- `mechanism-relocation-has-its-own-precondition`（已 grep，line 515）—— 收窄 Bash 落点要 spike 验
- 北极星触达：决策超越直觉（depth）—— 把"限定 workspace"从对抗问题降成结构问题，是钻得更深一层，不是选一个隔离档位

## 北极星
决策超越直觉（depth）——核心动作是降维：不在"上不上 OS 隔离"这层选，跳到"为什么 Bash 是洞"这层消除前提。

### 给父会话的最终输出

**裁决：不上 A/B/C 任何 OS 层硬隔离。釜底抽薪——收窄 Bash 从"任意 shell"到"只能调白名单业务 endpoint"，越权洞结构性消失。OS 隔离是在错前提上加对抗墙。**

**但有一个前置动作 Keith 必须先拍（不是我能决的）：威胁模型三选一。** 这是 principal 的自由参数不是我的物理常量。

---

**第 1 问（值不值得上 OS 硬隔离）——答案取决于威胁模型，但三档都不指向 OS 隔离作为首选：**

| 威胁模型 | 含义 | 该做什么 |
|---|---|---|
| 防手滑 | 诚实用户误操作 `cd ..` | 软约束（Read/Write 限 cwd + prompt）已够，连 Bash 收窄都可选 |
| 防恶意员工 | 内部人故意 `cat ../别人/.env` | **收窄 Bash**（下方主方案），不用 OS 隔离 |
| 防 prompt injection | 第三方借用户消息注入，劫持 LLM 去读别人明文 | **收窄 Bash 是唯一切根的**——OS 隔离挡跨用户文件，挡不住被注入的 LLM 打内网/读容器其他路径 |

**我的判断：本案实际威胁模型不是"防手滑"。** 几百人多租户 + 明文对话落 SQLite + `bypassPermissions` + Bash 全开 = 一条 prompt injection 能让某用户的 claude 进程 `cat ../别人workspace` 或 `curl 内网其他服务`。注入概率在几百人规模下非零。所以**值得做隔离，但不是 OS 层那种**。请 Keith 确认威胁模型是否到"防注入"这档——到了，下方主方案是必选；只到"防手滑"，下方方案降为可选优化。

---

**第 2 问（若上 OS 层，A/B/C 哪个）——我的裁决是都不上，理由是它们都在跟错前提对抗：**

- A（UID 池切换）：单容器跑 setuid 切换 + workspace chmod 700，工程量中等，但**只挡住文件系统跨读，挡不住 Bash `curl 内网`/打别的服务**——半个洞。
- B（每人独立容器）：和"企微单连接 + 几百人"地形直接冲突（你 thread 已记），资源爆炸，否决。
- C（bubblewrap/namespace 每进程关进自己视图）：技术上最干净的 OS 隔离，但**为了让 Bash 能跑任意 shell 还要给它造一个安全牢笼**——你在保护一个你根本不需要的能力。
- 共同问题（essence `network-cannot-cut-what-shares-tuple`）：A/B/C 都是用 OS 这把"低分辨率刀"去切"Bash 任意 shell"这个高分辨率边界，产物是对抗墙，不是结构解。

---

**第 3 问（釜底抽薪）——这是主方案，已被你的代码物理证伪为可行：**

**关键地真**（我读了 `prompts/cc-agent-capabilities.md` + `/api/*` 路由）：业务能力 100% 已是 HTTP endpoint（`http://cc-assistant:8000/api/*`），LLM 用 `curl` 调它。**`curl` 是 Bash 的子集——LLM 用 Bash 只为发 HTTP 请求，从不需要任意 shell。Bash 全开是历史惯性，不是能力必需。**

> essence `llm-autonomy-on-capability-invocation-is-the-bug-not-the-channel`：当"调不调某能力"由 LLM 自主决定时，真解是把决策点从 LLM 手里物理移走，不是再加一道防御。这里：把"能跑什么命令"从 LLM 手里移走。

**落地形态（按收益/工程量排序，二选一）：**

1. **业务 endpoint 转 MCP server + 砍 Bash（最干净，推荐）**
   - 把 `/api/*` 包成一个 MCP server（每个 endpoint = 一个 tool），claude 进程通过 MCP 调，不再 curl。
   - `--disallowedTools Bash` + 不挂任何文件写工具，或 Read/Write 强制限 cwd。
   - 结果：LLM 的工具空间里**物理上没有**"跑任意命令"这个动作，`cat ../别人/.env` 不是被拦截，是**根本不存在这个动作**。越权从对抗问题降成结构问题。
   - 工程量：endpoint 已有，转 MCP 是包一层 stdio/SSE 协议，几百行。**但落点要先 spike**（见下方风险）。

2. **PreToolUse hook 白名单拦截（更快，过渡方案）**
   - 保留 Bash，加 PreToolUse hook：只放行 `curl http://cc-assistant:8000/api/*`，其余命令一律 deny。
   - 白名单极性（essence `safe-default-by-whitelist-inversion`）：存"准入白名单"不存"禁入黑名单"，新增 endpoint 自动 safe-by-default。
   - 工程量更小，但 hook 是文本层拦截，比方案 1 的"工具空间里没有"弱一档——能被命令构造绕（管道/编码）的程度取决于 hook 实现严谨度。

**两个方案都做完后，OS 隔离从"必须"降为"纵深防御的可选第二层"**——不是首选、不是必须。

---

**⚠️ 落地前必须先 spike 验证一件事（不能信我的纸面方案）：**

claude CLI `stream-json` 模式下 `--disallowedTools Bash` / `--allowedTools` / PreToolUse hook **是否真生效、是否覆盖 subprocess 全部内置工具**——你这条链路（cc-gateway → claude subprocess → new-api）历史上已经栽过"system prompt 注入对 helper-mode 是弱信号、压不动"（thread 2026-05-14）。同样的"我以为某层能挡住"的前提，这次必须先用一个零副作用 spike 实测，再决定方案 1 还是 2。这是 essence `mechanism-relocation-has-its-own-precondition`：移走决策点的解，自身依赖"目标位置真能承接"这个未核前提。

**一句话收口**：不是选哪个隔离档位，是把 Bash 从"任意 shell"收窄成"只能调白名单 endpoint"，让"碰不到别人目录"从你要对抗的问题，变成工具空间里压根不存在的动作。OS 隔离留作可选第二层，不是主方案。
