---
date: 2026-05-06
mode: 工作
slug: launchd-cc-scheduler-scope
status: substantive-decision
decision_type: 范围控制 / 工程基建评审
parent_session: cc-space
---

# launchd 接管 8 个 CC 定时任务的基建范围拍板

## 议题

Keith 要把 8 个 CC 定时任务从 Claude Desktop GUI 迁到 macOS launchd + `claude -p`。已写最小 hello-world 验证 RunAtLoad 链路通。给出的"管理系统"方案要 6 个 helper 脚本 + 8 项金丝雀 + plist 即 SSOT，问 6 个具体问题让我拍板。

## 装配

- Inversion（先想怎么失败）
- Cost-Benefit / YAGNI
- essence: ssot-distillation-vs-buffering（缓冲层是漂移温床）
- essence: fallback-detectability（失败被误判为成功 = 永不触发恢复）—— 直接命中 timeout 缺位的隐性成本

不装 personas / reasoning_modules——这是工程范围判断，3 个棱镜够用。

## 核心判断

方向对，方案稍重不多——砍 2 个 helper（list/status/trigger 中的两个）+ 加 timeout 前置 + 加 4 项金丝雀 = 合适形态。

## 给父会话的最终输出

### 方向

launchd + claude -p 是正确路径。cc-connect 接管不成立（角色错配——它是 messaging bridge daemon 不是 cron runner，且 daemon 挂了一起挂这个弱点 Keith 已识别）。Routines API 违反"本地"约束。继续客户端是确认死路。

### 6 问拍板

1. **方向**：对，无更优解。
2. **plist 即 SSOT**：保持。8 任务 × 写一次跑一年的场景下 YAML+generator 是 ssot-distillation-vs-buffering 反例。`_template.plist` + sed 占位足够，不要 generator。
3. **6 helper 砍到 4**：留 install / uninstall / logs / new-task。删 list / status / trigger——launchctl 原生一行能干（`launchctl list | grep cc-space` / `launchctl print gui/$UID/<label>` / `launchctl kickstart -k gui/$UID/<label>`）。封 helper = 把简单的事再加皮 + macOS 升级 launchctl 输出格式变了你的解析逻辑就是债。README 教原生命令更稳。
4. **timeout 前置加**。Inversion 一秒：8 个 claude -p 任务 hang 是 when not if（OAuth refresh / 5xx / 网络瞬断）。launchd 不会自动 kill，hang 1 个 = label busy = 下次 calendar 触发被跳过 = **静默失败**——直接命中 fallback-detectability。perl alarm 一行包不增加复杂度。默认 1800s。
5. **金丝雀漏 4 项**：
   - macOS 睡眠跨过触发时间（launchd 不补跑——隔夜/凌晨任务大概率撞）
   - OAuth token 在 launchd 上下文能否被 claude 找到——金丝雀必须真调模型不是 echo
   - stdout/stderr 文件无限增长（8 × 365 × N MB → GB 级）→ logrotate 或日期后缀
   - 同 label 重 install 是覆盖还是报错——语义先定，不要 install.sh 中途变更
6. **范围**：按 #3 #4 修订后不过度。但**强烈建议灰度迁移**——先 1-2 个低风险任务（auto_cc_space / test）跑 1 周再迁剩下 6 个。"之前失败这次没复现"≠不会复现，灰度让失败可隔离。

### 漏的维度

- 不要让 launchd 任务相互依赖（A→B 模式是 launchd 弱项），现在约束好"每个任务自包含"
- Keith 改 plist 后忘记 bootstrap → install.sh mtime 检查或 README 顶部贴提醒
- gg / auto_gg 调的是 gg 项目不是 cc-space → WorkingDirectory / prompt 路径不要写死 cc-space 根

## 核心假设

1. cc-connect 是 messaging bridge 不是通用 runner（fact-checked: thread/cc-connect.md 已确认部署形态）
2. launchd 在 hang 上确实不会自动 kill 子进程（macOS 标准行为，未现场验证但跨多个项目共识）
3. 8 个任务长期不会演化出复杂依赖（这点风险中——若错估 launchd 弱项会暴露）

## 可能出错的地方

- **timeout 1800s 可能不够**——若有任务正常运行就要 30+ 分钟（如全量 transcript 扫描），1800 会误杀。Keith 装时按任务 SLA 单独配
- **灰度迁 1 周太短**——某些 hang 路径（OAuth token refresh）可能 30 天才一次，1 周观察期会假绿
- **launchctl 原生命令可读性 Keith 接受不了**——若 Keith 实际用了发现"我连 status 都要 launchctl print 太丑"，再回来加 helper 不晚

## 推理盲区

- 我没读 cc-space 的 hourly_check.py 现状——它已经是 crontab，是否值得也迁 launchd 一并管理（统一调度面）？没纳入范围讨论。Keith 可能心里默认"crontab 那个不动"——但若想统一就该一起谈
- 我没问 8 个任务的实际 SLA 分布——timeout 默认值 1800 只是猜。Keith 应该按 task 列出 p99 运行时长再决定

## N 个月后的根因预判

如果 6 个月后这套基建出事，最可能根因排序：
1. **静默失败未被察觉**（hang task 不重启 + log 没人看）—— 缓解 = 加每日 cron 扫 stale log（"X 小时没新输出告警"）
2. **OAuth token 过期**——claude -p 在 launchd 上下文 token refresh 是否 work，金丝雀不一定撞到
3. **macOS 升级动了 launchd 行为**—— gui domain / system domain 切换史上变过

## 北极星触达

- ✅ Keith 5 年领先：脱离 GUI = CC 任务可 git 管 = 长期资产化（vs 客户端不开就丢）
- ✅ 能力 > 体验：选 launchctl 原生 + 4 helper 比 6 helper + cct wrapper 更稳
- ✅ 诚实胜于体贴：直接说"6 helper 砍 2 个"+ "timeout 必须前置"+ "灰度迁移"，不和稀泥
- ✅ 一致性：跟 essence ssot-distillation-vs-buffering / fallback-detectability 一脉相承

## 对齐度

5/5。Keith 已自陈倾向"不过度"，本次拍板把"倾向"落到具体砍哪两个 helper / 必加哪一项防御 / 必跑哪几项金丝雀。
