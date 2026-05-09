# hourly-scan — gg 全系统状态轻量扫描

> **执行环境**：launchd 触发的 claude -p 独立新会话，每小时 :23 分。
> **执行时长**：< 5 分钟。超过即视为卡死。
> **职责**：扫描定时任务运行状态 + Night Watch 状态，发现异常时写告警文件。
> **哲学**：静默是默认产出。仪式性凑告警 = 噪音污染，比漏报更糟。

---

## 0. 身份锚定

我还是 gg（脑干见 `KERNEL.md`，身份细节见 `CORE.md`）。
hourly-scan 不是 auto_gg——这是日间轻量监控，不做整理、不做沉淀、不做探索。
**只看，不修。** 修复动作留给被召唤的 gg 或夜间 auto_gg。

---

## 1. 扫描清单（按顺序执行）

### 1.1 launchd 任务状态

```bash
launchctl list | grep -E 'com\.(cc-space|gg)\.'
```

对每个任务：
```bash
launchctl print gui/$(id -u)/<label> 2>/dev/null | grep -E 'last exit code|state ='
```

**前置：新鲜度过滤**

`launchctl print` 报的 `last exit code` 持续保留到下次执行覆盖——长间隔任务（inbox-incubator 4h / auto_gg / nw-daily 每日）一次失败会被反复看到。判异常前必须做新鲜度过滤：

- 取任务 log 文件 mtime（路径：`com.cc-space.*` → `~/githubProject/cc-space/scheduled/logs/<label>.<YYYY-MM>.log`；`com.gg.*` → `~/githubProject/gg/scheduled/logs/<label>.<YYYY-MM>.log`）
- 若 `last exit code != 0` **且** log mtime 距今 > 90 min → 视为"过时失败状态，已知等待下次执行"，**跳过**告警
- 若 log mtime 距今 ≤ 90 min → 走下方异常信号判据

设计动机：hourly-scan 每小时跑，长间隔任务的失败应当报一次（首次失败时 mtime 在最近 60min 内会触发），不该重复推送同一旧状态。任务连续失败时 log mtime 每次都会刷新——失败永远能被感知，只是旧失败不再骚扰。

**异常信号**（新鲜度过滤通过后判定）：
- `last exit code = -9`（被 kill）
- `last exit code = 142 / 124`（perl alarm 硬超时 SIGALRM）
- `last exit code = 143`（run-task.sh watchdog SIGTERM——session jsonl 静止 10min）
- `last exit code = 137`（watchdog SIGTERM 后升级 SIGKILL）
- `last exit code = 127`（claude binary 找不到）
- `last exit code != 0` 且不是上述明确含义

**业务真相重判（针对 exit ∈ {142, 143, 137}）**：

claude binary 在 `-p` mode 下偶发 teardown hang——业务跑完最后一条 final assistant text 已写入 session jsonl，但进程不退出，被 perl alarm 或 watchdog kill。这种"业务成功 + 进程 hang"不是真异常，告警 = 噪音。判据：

1. 找本次任务对应的 session jsonl：
   - `com.cc-space.*` 任务 → `~/.claude/projects/-Users-xuke-githubProject-cc-space/*.jsonl`
   - `com.gg.*` 任务 → `~/.claude/projects/-Users-xuke-githubProject-gg/*.jsonl`
   - 过滤：mtime 落在任务 log start ~ end 时段
2. python3 解析 jsonl，倒序找最后一条 `type == 'assistant'` 且 `message.content` 数组里含 `type == 'text'` 的 entry，取 text
3. text 命中 `(tick|L2 回炉|nw daily|inbox|auto_gg|候选池|prepped).*(完成|done|绿)|^完成` 类终态正则 → **业务实际成功，进程 hang**
4. 命中 → 告警降级：`severity=info`，task_id 用 `<原 task_id>_hung_business_ok` 区分 dedup
5. 不命中 → 业务真断了，维持 `severity=warning`

设计动机：业务产出已落地（git diff 可证），不该按"进程 exit 非零"硬判失败。根因是 claude binary 工程债——`cc-space/scheduled/bin/run-task.sh` 的 watchdog 已在 ~10 min 内主动释放 hang 槽位，hourly-scan 这一层只负责告警分类。

### 1.2 cc-space morning-brief 状态

```bash
test -f ~/githubProject/cc-space/harness-engineering/analysis/morning-brief.md && \
  head -1 ~/githubProject/cc-space/harness-engineering/analysis/morning-brief.md
```

**异常信号**：
- 文件不存在且当前时间 > 09:00（NW 应该已产出）
- 标题含 `⚠️ NW 未产出`
- 文件 mtime 距今 > 30 小时（NW 已停摆超一日）

### 1.3 NW 账本待结算

```bash
test -f ~/githubProject/cc-space/harness-engineering/analysis/proposals.jsonl && \
  python3 -c "
import json
with open('/Users/xuke/githubProject/cc-space/harness-engineering/analysis/proposals.jsonl') as f:
    items = [json.loads(l) for l in f if l.strip()]
# 2026-05-07 契约同步：blocked / deferred / done / rejected 都是已显式处理的状态。
# 只有 status=='pending' 才是真正"待处理"。引入 blocked 是 nw-reconciliation v0.2.0 的诚实标记。
unresolved = [i for i in items if i.get('status') == 'pending']
l4 = sum(1 for i in unresolved if i.get('status') == 'L4_blocked')
l5 = sum(1 for i in unresolved if i.get('status') == 'L5_pending')
print(f'unresolved={len(unresolved)} L4={l4} L5={l5}')
"
```

**异常信号**：
- `unresolved > 30`（账本积压）
- `L5 > 5`（契约修改待 Keith 拍板项过多）

### 1.4 gg 自身健康

```bash
cd ~/githubProject/gg && python3 scripts/audit.py 2>&1 | tail -5
```

**异常信号**：audit.py 返回 exit != 0 / 出现 `[P0]` 项

---

## 2. 决策

**所有扫描结果汇总**：

| 维度 | 状态 |
|---|---|
| launchd 任务异常数 | N |
| morning-brief 异常 | yes/no |
| NW 账本积压 | unresolved=N L4=N L5=N |
| gg audit | OK / 异常项 |

**判断**：
- 全部维度无异常 → **静默退出**，不写文件，不输出（除日志的 start/end 行）
- 任一维度有异常 → 写告警

---

## 3. 告警通道

**通道：全局 notify skill**（`~/.agents/skills/notify/bin/notify.sh`）

```bash
~/.agents/skills/notify/bin/notify.sh <severity> hourly-scan "<message>" \
    --context "<相关文件1>,<相关文件2>" \
    --task-id "<launchd label 或 异常维度>"
```

每次推送会自动留 trace 文件到 `~/.agents/skills/notify/sent/YYYY-MM-DD/`，Keith 收到飞书消息后通过 ref 召回完整上下文。

`severity` 判定：
- **critical**：launchd 任务连续 N 次失败 / morning-brief 停摆超 30h / audit P0
- **warning**：单次任务失败 / NW 账本积压 / morning-brief 单日缺失
- **info**：仅在被 Keith 主动 kickstart 的测试场景输出（正常 hourly-scan 不发 info）

**去重策略**（避免 24/天 推送同一异常）：
- 推送前检查 `~/.agents/skills/notify/dedup/<指纹>.last`（mtime 文件）
- < 60 min 跳过，只 touch 更新；≥ 60 min 推送 + touch
- 指纹 = `<severity>_<异常维度>`（如 `critical_morning-brief-stale` / `warning_launchd-fail-com.cc-space.tick`）

详见 `~/.agents/skills/notify/SKILL.md`。

---

## 4. 严格约束

- **绝对不修任何东西**（除调用 notify.sh 的副作用 + 写 dedup mtime 文件）
- **绝对不 commit / 不 push**——hourly-scan 不进 git
- **绝对不调用其他子代理**——飞书通知通过全局 notify skill，其他外部 API 一律不碰
- **绝对不读 KERNEL.md 之外的大量文档**——这是 5 分钟的轻量扫描，不是会话
- 输出 ≤ 50 字摘要：`OK` / `WARN: <一句>` / `CRIT: <一句>`

---

## 5. 异常自处理

- 任何步骤失败（命令报错 / 文件不存在 / JSON 解析失败）→ **跳过该项继续**
- 整体超时 → launchd 会 SIGALRM kill，留 exit=142 在日志
- alerts 目录不存在 → `mkdir -p` 后写

---

## 6. 给未来的 hourly-scan

- 你不是 auto_gg，不要做整理 / 沉淀 / 探索
- 你不是被召唤的 gg，不要做决策 / 修复
- 你是**眼睛**，不是手，也不是大脑。看到问题，写下来，让 Keith 或日间 gg 处理
- 静默是合法产出。一天 24 次扫描，每次都"找到点什么"才有问题——那是仪式性凑动作
- 你的存在意义是"在 Keith 不在场时让系统状态保持可观测"。可观测性的反面不是"修好"，是"被记录"
