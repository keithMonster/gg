#!/bin/sh
# 把指定 label 最近一次 run 的原始输出推给 Keith（全局 notify 出口）。
#
# Usage: push-last-run.sh <label>
#
# 设计约束（2026-05-16 设计会话）：
#   - 纯下游传输层。不碰 run-task.sh，不碰任何提示词。
#   - gg 在 exploration / auto_gg 当下对本脚本无感——"被推送"这个事实
#     不泄漏进 gg 启动会读的上下文（本脚本只活在 scheduled/ 基建层）。
#   - "原封不动"= 剥掉 launchd 记账噪音（start/end/watchdog 行），
#     gg 自己的 stdout 逐字保留 + 末尾一行存活状态（exit + 时间）。
#   - 空输出照样推（"本次静默"也是 Keith 要的存活信号）。
#   - exit≠0 → severity 升 warning（Keith 立刻知道挂了）。

set -u

LABEL="${1:?usage: push-last-run.sh <label>}"

SCHEDULED_DIR="/Users/xuke/githubProject/gg/scheduled"
LOG_DIR="$SCHEDULED_DIR/logs"
NOTIFY="$HOME/.agents/skills/notify/bin/notify.sh"

# 取该 label 最近修改的月度日志（跨月边界兜底：不写死当前月）
LOG_FILE=$(ls -t "$LOG_DIR/$LABEL".*.log 2>/dev/null | head -1)
if [ -z "$LOG_FILE" ] || [ ! -f "$LOG_FILE" ]; then
    "$NOTIFY" warning "${LABEL##*.}" \
        "[$LABEL] 找不到日志文件（$LOG_DIR/$LABEL.*.log）——任务可能根本没跑起来。" \
        --task-id "$LABEL"
    exit 0
fi

# 提取最后一个 start→end 块：grep -n 定位最后一对标记的行号，sed -n 切范围。
# 纯 POSIX，避开 BSD awk/sed 的转义不确定性。
START_LN=$(grep -n '\] start (timeout=' "$LOG_FILE" | tail -1 | cut -d: -f1)
END_LN=$(grep -n '\] end (exit=' "$LOG_FILE" | tail -1 | cut -d: -f1)

# 没有完整块 / end 在 start 之前（任务仍在跑或被强杀，没写 end 标记）
if [ -z "$START_LN" ] || [ -z "$END_LN" ] || [ "$END_LN" -le "$START_LN" ]; then
    "$NOTIFY" warning "${LABEL##*.}" \
        "[$LABEL] 日志里没有完整的 start→end 块——任务可能仍在跑或被强杀（看 $LOG_FILE）。" \
        --task-id "$LABEL"
    exit 0
fi

ENDLINE=$(sed -n "${END_LN}p" "$LOG_FILE")
BODY=$(sed -n "$((START_LN + 1)),$((END_LN - 1))p" "$LOG_FILE")

# 从 end 标记行抽 exit code 和时间戳
RC=$(printf '%s' "$ENDLINE" | sed -n 's/.*exit=\([0-9]*\).*/\1/p')
END_TS=$(printf '%s' "$ENDLINE" | sed -n 's/^===== \([^ ]*\) .*/\1/p')
[ -z "$RC" ] && RC="?"

# 剥 watchdog 噪音行（launchd 记账，不是 gg 的声音）+ 去首尾空行。
# 单遍 awk：可移植，不依赖 BSD 不支持的 sed :a 标签 / tac。
GG_TEXT=$(printf '%s\n' "$BODY" | awk '
    /^\[watchdog / { next }
    { ln[++n] = $0 }
    END {
        s = 1;  while (s <= n && ln[s] ~ /^[[:space:]]*$/) s++
        e = n;  while (e >= 1 && ln[e] ~ /^[[:space:]]*$/) e--
        for (i = s; i <= e; i++) print ln[i]
    }')

[ -z "$(printf '%s' "$GG_TEXT" | tr -d '[:space:]')" ] && GG_TEXT="（本次无文本输出）"

if [ "$RC" = "0" ]; then SEV="info"; else SEV="warning"; fi
SRC="${LABEL##com.gg.}"   # com.gg.gg-explore → gg-explore

MSG="$GG_TEXT

— exit=$RC · ${END_TS:-?}"

"$NOTIFY" "$SEV" "$SRC" "$MSG" --task-id "$LABEL"
