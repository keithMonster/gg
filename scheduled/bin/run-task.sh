#!/bin/sh
# gg 定时任务 runner（由 launchd plist 调用，非用户直跑）
#
# Usage: run-task.sh <label> <timeout-seconds> <prompt> [model]
#
# 参数：
#   <label>           任务标签
#   <timeout-seconds> 硬超时（perl alarm 触发 SIGALRM kill）
#   <prompt>          claude -p 的 prompt 文本
#   [model]           可选，传给 --model（如 'opus' / 'sonnet'）；空 = CC 默认路由
#
# 行为：
#   1. 用 perl alarm 给 claude -p 加硬超时（macOS 无 timeout 命令）
#   2. 输出按月份滚动日志：logs/<label>.YYYY-MM.log
#   3. start/end 标记带 ISO8601 时间戳和 exit code，方便事后审计
#
# 失败模式（在日志里都能看到）：
#   - exit=142  → 命中 timeout（perl alarm 触发 SIGALRM）
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

if [ -n "$MODEL" ]; then
    MODEL_FLAG="--model $MODEL"
else
    MODEL_FLAG=""
fi

{
    echo "===== $(date -Iseconds) [$LABEL] start (timeout=${TIMEOUT}s, model=${MODEL:-default}) ====="
    perl -e '$t=shift; alarm $t; exec @ARGV; die "exec failed: $!"' \
         "$TIMEOUT" \
         "$CLAUDE_BIN" -p $MODEL_FLAG --permission-mode bypassPermissions "$PROMPT"
    RC=$?
    echo "===== $(date -Iseconds) [$LABEL] end (exit=$RC) ====="
    exit $RC
} >> "$LOG_FILE" 2>&1
