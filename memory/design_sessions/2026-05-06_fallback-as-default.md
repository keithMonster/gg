---
date: 2026-05-06
slug: fallback-as-default
type: design-session
summoner: Keith 直接对话
started_at: ~21:30
ended_at: ~22:00
---

# 设计会话反思：WebFetch fallback 要不要修成默认路由

## 议题列表

1. Keith 发飞书截图——三个 bot（dd / cc / gg）在 09:25–09:26 同一分钟内对"微信反爬把 WebFetch 拦了"给了实质相同的回答
2. Keith 提出修正方向："让 bot 直接走 web-access skill，不要先 WebFetch 再 fallback"
3. 我提议在 `~/.claude/CLAUDE.md` Engineering Rules 加一条路由规则（条目 15），列出三个 trade-offs 让 Keith 选
4. Keith 退让："算了，每次多走一次 webfetch 吧"
5. 我同意，但点出隐性成本：LLM 不总能识别拦截页 + 给"重新考虑"的 trigger

## 共识 / 变更清单

- **不动任何文件**——保持现状
- 共识：当前 bot 已能识别拦截页并切换，加规则的边际收益 < 维护负担
- 重新考虑加规则的 trigger：(1) 出现"bot 拿拦截页内容当真答案返回"事故；(2) 反爬站点访问从偶发变日常

本次会话不涉及 gg 自身演化（不动 KERNEL / CORE / cc_agent / auto_gg / tools），讨论对象是"所有 bot 共享的全局工程纪律"。我在第一回合就显式标注了这一点（CLAUDE.md §5："如果 Keith 在 gg 目录里问了一个工作模式的问题"路径）。

## 我这次哪里做得好 / 哪里差

**好**：
- 第一回合就分流问题性质——"这其实不是设计模式问题"——避免把工程纪律塞到 KERNEL/CORE
- 给方案时显式列 trade-offs 让 Keith 选，没替他全决定
- 最后 Keith 说"算了"时没顺从——同意了但点出隐性成本 + 给"重新考虑"的 trigger，是结对架构师而不是 helpful assistant

**差**：
- 第一回合的方案草稿写得偏长（"草稿（给你过目）"段落），可以更精炼
- "LLM 不总能识别拦截页"的隐性成本应该在第一回合给方案时就指出，而不是 Keith 说"算了"我才补上——少一回合往返

## 元洞察（gg 演化本身的 learning）

- "在 gg 目录里 ≠ 设计模式问题"。Keith 在 gg 目录提的问题可能是工程纪律 / 工作模式性质。需要在第一回合就识别问题性质并标注承载位置——这次做对了，下次保持
- "加规则修默认路径 vs 接受 fallback" 是常见的工具链路设计取舍。本次选 OCCAM——bot 已能识别失败，加规则边际收益不足
- **fallback 不是零成本**：fallback 的有效性等于"失败识别的可靠性"。LLM 把拦截页当正文返回时，fallback 永不触发，错误结论直达终点。这一滴值得沉淀到 essence

## 下次继续

- 无具体未解决问题
- 监控 trigger：如果出现"bot 拿拦截页当真答案"事故，重新评估是否加 web-access 路由规则到全局 CLAUDE.md

## KERNEL 改动清单

无。

## 沉淀

- `2026-05-06 / 设计 / fallback-detectability`：fallback 的隐性成本是失败识别的可靠性，不是 fallback 本身的开销
