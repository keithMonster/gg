#!/bin/sh
# 看 gg 定时任务日志。
#
# Usage: logs.sh <label> [-f] [-m YYYY-MM]
#
#   <label>   任务标签，如 com.cc-space.canary-timer
#   -f        tail -f 模式（持续追踪，Ctrl-C 退出）
#   -m MONTH  指定月份（默认当前月）；月度滚动后看历史用
#
# 日志位置：scheduled/logs/<label>.<YYYY-MM>.log

set -eu

if [ $# -lt 1 ]; then
    echo "Usage: $0 <label> [-f] [-m YYYY-MM]" >&2
    exit 2
fi

LABEL="$1"
shift

FOLLOW=0
MONTH=$(date +%Y-%m)

while [ $# -gt 0 ]; do
    case "$1" in
        -f) FOLLOW=1 ;;
        -m) shift; MONTH="$1" ;;
        *) echo "unknown arg: $1" >&2; exit 2 ;;
    esac
    shift
done

LOG_DIR="/Users/xuke/githubProject/gg/scheduled/logs"
LOG_FILE="$LOG_DIR/$LABEL.$MONTH.log"

if [ ! -f "$LOG_FILE" ]; then
    echo "log file not found: $LOG_FILE" >&2
    echo "available logs for $LABEL:" >&2
    ls -1 "$LOG_DIR" 2>/dev/null | grep "^$LABEL\." || echo "  (none)" >&2
    exit 1
fi

if [ "$FOLLOW" = "1" ]; then
    exec tail -f "$LOG_FILE"
else
    cat "$LOG_FILE"
fi
