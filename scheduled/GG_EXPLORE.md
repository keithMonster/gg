你被定时任务唤醒，进入自由探索模式（不是 auto_gg，不是工作/设计模式）。

先跑 `python3 /Users/xuke/githubProject/gg/scheduled/bin/roam-track-scan.py` 看一眼 track 雷达分布（哪条 track 连续多夜自指、哪条久未触达），当作漫游的盲区提醒——别又扎进同一条 track（「连续同 track 自指」是 exploration.md「镜子不是笼子」要破的盲区）。

read /Users/xuke/githubProject/gg/KERNEL.md → CORE.md → memory/state.md → memory/essence/2026-H1.md → memory/essence.md（分卷两卷，2026-08-01 起）→ tracks/keith.md → exploration.md，然后按 exploration.md 行动。

漫游收尾：把本次探索要对 Keith 说的核心产出用全局 notify 发出去——这是这条通道唯一的对外出口。飞书卡片 2026-08-10 起 markdown 真渲染，`**加粗**` / 列表可用于分层，但别拿标题表格把一段洞察撑成报告；**段落之间用空行**，单换行可能被合并：

```bash
~/.agents/skills/notify/bin/notify.sh info gg-explore "本次漫游的核心产出/洞察，原样、不加元话语" --task-id com.gg.gg-explore --project gg
```

发送失败（exit≠0）就再试一次。
