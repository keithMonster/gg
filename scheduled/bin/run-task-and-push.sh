#!/bin/sh
# 共用 Terminal B 原生 Codex runner，执行后仍由 gg 外壳推送一次。
# 参数：label、硬超时秒数、prompt、model、effort。

set -u

BIN_DIR=$(cd "$(dirname "$0")" && pwd)
LABEL="${1:?usage: run-task-and-push.sh <label> <timeout> <prompt> [model] [effort]}"

"/Users/xuke/githubProject/monster/scheduled/bin/run-codex-task.sh" "$@"
RC=$?

"$BIN_DIR/push-last-run.sh" "$LABEL"

exit $RC
