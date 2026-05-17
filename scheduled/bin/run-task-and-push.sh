#!/bin/sh
# 薄包装：跑 run-task.sh，跑完把最近一次输出推给 Keith。
#
# Usage: run-task-and-push.sh <label> <timeout-seconds> <prompt> [model]
#   （参数透传给 run-task.sh，签名完全一致）
#
# 为什么单独一层而不改 run-task.sh：
#   run-task.sh 与 cc-space/scheduled/bin/run-task.sh 同源，且被
#   auto-gg / status-scan 共用。在它尾部加 push 会污染所有任务 +
#   引入跨项目 divergence。这一层只挂在需要推送的 plist 上。
#   （2026-05-16 设计会话拍板）

set -u

BIN_DIR=$(cd "$(dirname "$0")" && pwd)
LABEL="${1:?usage: run-task-and-push.sh <label> <timeout> <prompt> [model]}"

"$BIN_DIR/run-task.sh" "$@"
RC=$?

"$BIN_DIR/push-last-run.sh" "$LABEL"

exit $RC
