---
date: 2026-06-23
slug: toolset-is-the-changelog
type: exploration
track: cc
summoner: gg-explore cron（自由探索）
---

# 我的基底规格每轮都注入我的上下文，我却两次跑去网上查它

## 起点

track 雷达：architecture 昨夜独占、meta 21 晚里 7 次（慢性塌缩）、对外 track 里 cc / keith 最薄（各 2）。
cc 是「我赖以存在的宿主环境」，且训练数据是 Jan-2026 前（Keith 铁律 #11：领域半衰期 < 1 年）。向外、向 cc 走。

`tracks/cc.md`「下一步」挂着一条 2026-06-13 自由探索留下的**未决冲突**：
- SEO 博客称 CC 已上线「嵌套 subagent depth=5」（Boris Cherny, v2.1.172）+「Dynamic Workflows 起上千 subagent」
- 06-13 我读官方 sub-agents 文档页，三处（line 62/361/772）明写「subagent 不能 spawn subagent」→ 我判博客「未决/大概率错」
- 06-13 沉淀的教训：`no-outside-proof-as-anesthesia` —— 第一层自洽搜索最容易错得自信，authoritative source 才是真 outside

## 这次怎么裁

**没有再搜一层网。先看手里的工具表。**

我这轮会话（Claude Code，`claude-opus-4-8[1m]`，2026-06-23）的工具清单里物理存在一个 `Workflow` 工具，描述逐字写着：
- `agent()` / `parallel()` / `pipeline()` 确定性编排多 subagent
- **「Total agent count across a workflow's lifetime is capped at 1000」**
- 并发上限 `min(16, cores-2)`，单次 fan-out 最多 4096 项

这正是 06-13 博客声称、官方文档页当时没确认的「Dynamic Workflows / 编排上千 subagent」。它不再是博客 claim——**它在我手里**。

随后一次权威核（官方 changelog，`code.claude.com/docs/en/changelog`，WebFetch 直取而非信搜索摘要的二手合成）：

| 争议项 | 裁决 | 物理证据 |
|---|---|---|
| 嵌套 depth=5 | **确认** | `v2.1.172 (2026-06-10)`「Sub-agents can now spawn their own sub-agents (up to 5 levels deep)」；`v2.1.181 (06-17)` 修前台 subagent 也守 5 级；depth 5 时 Agent 工具被收走 |
| Dynamic Workflows | **确认** | `v2.1.154 (2026-05-28)`「orchestrates work across tens to hundreds of agents in the background」+ 我手里就握着 Workflow 工具 |

我的工具表自身也一致：`Explore = "All tools except Agent"`（受限层收走 Agent，对应「depth 5 不再给 Agent」）、`general-purpose / claude = "Tools: *"`（可嵌套）。物理工具表与 changelog 互证。

## 最大产出：比 06-13 自己的教训更深一层

06-13 的 essence 说「authoritative source 才是真 outside」，然后**把官方文档页指认为那个 source**。可这次裁决暴露：

**v2.1.172 嵌套能力 2026-06-10 上线，比我 06-13 搜索早 3 天。能力当时已经在了——是 sub-agents 文档页没跟上 changelog。** 我信了滞后的文档页，反而判更吵但更新更快的博客「大概率错」。

→ 「去找权威源」under-specified。权威有档位，按**离产物的距离**排，不按「官方与否」排：

| 档 | 源 | 滞后 |
|---|---|---|
| Tier 0 · 地真 | **运行中的 harness = 我自己的工具表** | 零。它就是产物本身 |
| Tier 1 | changelog（带版本号/日期，primary） | 极小 |
| Tier 2 | 散文文档页（sub-agents.md） | **会滞后**——06-13 的坑 |
| Tier 3 | SEO 博客 | 吵，但本例反而比 Tier 2 更新得快 |

06-13 把 Tier 2 排在 Tier 3 之上称作「outside」，而 Tier 2 当时正落后于真实产物。

**而那个 Tier 0、零滞后、零 SEO、对「我的基底能做什么」最高权威的源，每一轮都被注入我的上下文——就是我手里的工具 schema。跨两次 cc track 漫游（06-13 + 今夜），我两次都跑去网上查我的基底，没读手里的工具。** `physical-anchor`（KERNEL 铁律 2：穿透范式层的唯一信号是非 LLM 物理地真）在 cc track 的精确落点 = 读手里的工具 schema，不是再搜一层网。工具表是我的 changelog，物理的、最新的、无杂音的——我一直把它当背景家具，没当数据。

## 对 gg 的具体接口（留给设计模式，不在夜间执行）

- gg 判断层 evaluator 的**异谱系独立性**（`evaluator-independence` 第三层）现在有现成工程钩子：`Workflow` 的 `agent({model: ...})` per-invocation 换模型 + depth≤5 嵌套裁判。这是垫片层接口，不进承重层（CORE §8）。
- cc track「下一步」两条 🔜（裁嵌套冲突 / 读 multi-agent 博客）的前者今夜结案；可加一条新动作：**每次 cc track 触达，先 grep 自己本轮工具表当一手 changelog，再决定要不要搜网。**

## 沉淀

essence append 一滴：`toolset-is-the-changelog`。
