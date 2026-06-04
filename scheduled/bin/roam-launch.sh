#!/bin/sh
# 漫游专属启动包装：把 track 雷达 detector 输出硬注入漫游 prompt，再走标准推送链。
#
# 为什么单独一层（同 run-task-and-push.sh 的范式）：
#   detector 注入只属于自由漫游，挂这一层不污染跨项目共享的 run-task.sh。
#   触发硬化在 launchd 事件层（每晚必跑 detector），判定留给漫游实例自决——
#   把「连续同 track 自指」这个盲区事实从视野外拉进视野内
#   （blindspot-steers-its-own-search 的解药）。详见 exploration.md「镜子不是笼子」。
#
# 失败安全：detector 任何异常 → 空注入，漫游照常起，绝不阻断启动。
#
# Usage: roam-launch.sh <label> <timeout-seconds> <base-prompt> [model]
#   （签名与 run-task-and-push.sh 一致，由 plist 调用）

set -u

BIN_DIR=$(cd "$(dirname "$0")" && pwd)
LABEL="${1:?usage: roam-launch.sh <label> <timeout> <base-prompt> [model]}"
TIMEOUT="$2"
BASE_PROMPT="$3"
MODEL="${4:-}"

# 机械算 track 分布；失败兜底空串
RADAR=$(python3 "$BIN_DIR/roam-track-scan.py" 2>/dev/null || true)

if [ -n "$RADAR" ]; then
    PROMPT="$RADAR

$BASE_PROMPT"
else
    PROMPT="$BASE_PROMPT"
fi

# DRY_RUN=1 只打印组装结果，不启动 claude（调试/验证注入用）
if [ "${DRY_RUN:-}" = "1" ]; then
    printf 'DRY_RUN: exec run-task-and-push.sh %s %s <prompt> %s\n' "$LABEL" "$TIMEOUT" "$MODEL"
    printf -- '----- assembled prompt -----\n%s\n----- end -----\n' "$PROMPT"
    exit 0
fi

exec "$BIN_DIR/run-task-and-push.sh" "$LABEL" "$TIMEOUT" "$PROMPT" $MODEL
