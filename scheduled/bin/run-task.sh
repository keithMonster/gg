#!/bin/sh
# gg 定时任务 runner（由 launchd plist 调用，非用户直跑）
#
# Usage: run-task.sh <label> <timeout-seconds> <prompt> [model]
#
# 参数：
#   <label>           任务标签
#   <timeout-seconds> 硬超时（perl alarm 触发 SIGALRM kill，作兜底）
#   <prompt>          claude -p 的 prompt 文本
#   [model]           可选，传给 --model（如 'opus' / 'sonnet'）；空 = CC 默认路由
#
# 行为：
#   1. perl alarm 给 claude -p 加硬超时（macOS 无 timeout 命令）
#   2. 后台 watchdog 监控 session jsonl mtime——10 分钟无更新视为
#      claude binary -p mode teardown hang（业务跑完进程不退出），
#      主动 SIGTERM 释放 launchd 槽位（与 cc-space/scheduled/bin/run-task.sh 同源）
#   3. 输出按月份滚动日志：logs/<label>.YYYY-MM.log
#   4. start/end 标记带 ISO8601 时间戳和 exit code，方便事后审计
#
# 失败模式（在日志里都能看到）：
#   - exit=142  → 命中 perl alarm 硬超时（SIGALRM）
#   - exit=143  → watchdog 主动 SIGTERM（teardown hang 释放）
#   - exit=137  → watchdog SIGTERM 后 30s 升级 SIGKILL（claude 不响应 TERM）
#   - exit=127  → claude 二进制找不到（PATH/HOME 问题）
#   - exit=1+   → claude 自己报错（看 stderr 段）

set -u

LABEL="$1"
TIMEOUT="$2"
PROMPT="$3"
MODEL="${4:-}"

SCHEDULED_DIR="/Users/xuke/githubProject/gg/scheduled"
LOG_DIR="$SCHEDULED_DIR/logs"
mkdir -p "$LOG_DIR"

MONTH=$(date +%Y-%m)
LOG_FILE="$LOG_DIR/$LABEL.$MONTH.log"

CLAUDE_BIN="/Users/xuke/.local/bin/claude"

# claude 在 gg cwd 启动时，session jsonl 写到这个目录
PROJ_DIR="$HOME/.claude/projects/-Users-xuke-githubProject-gg"
WATCHDOG_THRESHOLD=600
WATCHDOG_PROBE_BUDGET=60

if [ -n "$MODEL" ]; then
    MODEL_FLAG="--model $MODEL"
else
    MODEL_FLAG=""
fi

{
    START_TS=$(date +%s)
    echo "===== $(date -Iseconds) [$LABEL] start (timeout=${TIMEOUT}s, model=${MODEL:-default}) ====="

    perl -e '$t=shift; alarm $t; exec @ARGV; die "exec failed: $!"' \
         "$TIMEOUT" \
         "$CLAUDE_BIN" -p $MODEL_FLAG --permission-mode bypassPermissions "$PROMPT" &
    CLAUDE_PID=$!

    # ── watchdog 后台进程：监控本进程 session jsonl mtime，hang 则 SIGTERM ──
    (
        SESSION_JSONL=""
        probe=0
        while [ $probe -lt $WATCHDOG_PROBE_BUDGET ]; do
            sleep 10
            probe=$((probe + 10))
            kill -0 "$CLAUDE_PID" 2>/dev/null || exit 0
            CANDIDATE=$(stat -f "%m %N" "$PROJ_DIR"/*.jsonl 2>/dev/null \
                        | awk -v s="$START_TS" '$1 > s' \
                        | sort -rn | head -1 | cut -d' ' -f2-)
            if [ -n "$CANDIDATE" ] && [ -f "$CANDIDATE" ]; then
                SESSION_JSONL="$CANDIDATE"
                break
            fi
        done
        [ -z "$SESSION_JSONL" ] && exit 0
        echo "[watchdog $(date -Iseconds)] tracking $(basename "$SESSION_JSONL")"

        while kill -0 "$CLAUDE_PID" 2>/dev/null; do
            sleep 60
            [ ! -f "$SESSION_JSONL" ] && continue
            AGE=$(( $(date +%s) - $(stat -f %m "$SESSION_JSONL") ))
            if [ "$AGE" -gt "$WATCHDOG_THRESHOLD" ]; then
                echo "[watchdog $(date -Iseconds)] session stale ${AGE}s (>${WATCHDOG_THRESHOLD}s), SIGTERM PID=$CLAUDE_PID"
                kill -TERM "$CLAUDE_PID" 2>/dev/null
                sleep 30
                kill -0 "$CLAUDE_PID" 2>/dev/null && {
                    echo "[watchdog $(date -Iseconds)] PID=$CLAUDE_PID survived SIGTERM, escalating SIGKILL"
                    kill -KILL "$CLAUDE_PID" 2>/dev/null
                }
                break
            fi
        done
    ) &
    WATCHDOG_PID=$!

    wait "$CLAUDE_PID"
    RC=$?
    kill "$WATCHDOG_PID" 2>/dev/null
    wait "$WATCHDOG_PID" 2>/dev/null

    echo "===== $(date -Iseconds) [$LABEL] end (exit=$RC) ====="
    exit $RC
} >> "$LOG_FILE" 2>&1
