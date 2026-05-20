#!/usr/bin/env bash
# cc-space → monster 改名脚本 v2（gg-side 改造版）
#
# v2 修改清单（落点见 audit.md §3 M1-M12）：
#   M1  链接保护：HISTORICAL_TOKENS + awk 逐行跳过含 historical token 的整行
#   M2  LAUNCHD_LABELS_OLD/NEW 显式拆分：auto-cc-space → auto-monster
#   M3  plist rename 用 ${var//find/replace} 全量替换 + 末段映射
#   M4  phase_0 备份扩充（.claude.json / .cc-connect / .gk / agents/gg.md / scheduled-tasks /
#       cc-cli-cache + 跨仓 baseline tag）
#   M5  phase_2_5 bootout com.cc-connect / phase_6_5 bootstrap + PID 验证
#   M6  GG_ACTIVE_FILES 13 个硬编码 + essence.md NOT IN + 跑完验证 monster 字面 = 0
#   M7  phase_7.0a-d 处理 ~/.claude.json / ~/.gk/repoMapping.json / agents/gg.md /
#       cc-connect/config.toml；7.2-7.4 全量 ~/.agents/skills/ + skill-notes/done.md
#   M8  phase_7.8 mv ~/.claude/scheduled-tasks/auto_cc_space → auto_monster + 内部 sed
#   M9  phase_10 增补 ~/Library/Caches/claude-cli-nodejs/ 8 目录前缀 mv
#   M10 phase_7.7 跨仓 sed 前打印命中清单 + ack
#   M11 DRY_RUN 模式：bash monster-rename.sh dry-run = DRY_RUN=1 + target=all
#   M12 MONSTER_RENAME_DIR 环境变量（rollback.sh 据此定位备份）
#
# 用法:
#   bash monster-rename.sh all           # 跑 Phase 0-9（Phase 8 ack 暂停）
#   bash monster-rename.sh 10            # 单独跑 Phase 10
#   bash monster-rename.sh <N>           # 单 phase（断点续）
#   bash monster-rename.sh dry-run       # 全量 dry-run（不实际 mv/sed/launchctl）
#   DRY_RUN=1 bash monster-rename.sh 7   # 指定 phase 的 dry-run

set -euo pipefail

# === 配置 ===
OLD_NAME="cc-space"
NEW_NAME="monster"
HOME_DIR="${HOME}"
OLD_REPO="${HOME_DIR}/githubProject/${OLD_NAME}"
NEW_REPO="${HOME_DIR}/githubProject/${NEW_NAME}"
OLD_LABEL_PREFIX="com.${OLD_NAME}"
NEW_LABEL_PREFIX="com.${NEW_NAME}"
UID_NUM="$(id -u)"
BASELINE_TAG="rename-baseline-20260520"
BAK_SUFFIX="bak-20260520"

# 自身所在目录（M12：rollback.sh 据此定位备份）
SELF_DIR="$(cd "$(dirname "$0")" && pwd)"
export MONSTER_RENAME_DIR="$SELF_DIR"

# DRY_RUN 默认空（M11）
DRY_RUN="${DRY_RUN:-0}"

# === M2: launchd 13 个旧 label（末段） ===
LAUNCHD_LABELS_OLD=(
  usage-monitor nw-weekly cgboiler-sync mirror-n kebao-cc-sync
  cgboiler-tick chat-prep mirror-h mirror-o cgboiler-inquiry-fetch
  cgboiler-inquiry-extract auto-cc-space nw-daily
)

# 派生新 label 末段：auto-cc-space → auto-monster，其他保留
LAUNCHD_LABELS_NEW=()
for _lbl in "${LAUNCHD_LABELS_OLD[@]}"; do
  if [ "$_lbl" = "auto-cc-space" ]; then
    LAUNCHD_LABELS_NEW+=("auto-monster")
  else
    LAUNCHD_LABELS_NEW+=("$_lbl")
  fi
done

# === M1: 历史叙事 token（含此 token 的整行内文本保留 cc-space 字面） ===
# 任何活文件中含这些 slug 的行，sed_in_repo 都跳过——保护 cross-ref 不断
HISTORICAL_TOKENS=(
  "cc-space-as-living-trunk"
  "cc-space-memory-decommission"
  "cc-space-design-system"
  "cc-space-to-monster-rename"
  # gg 自身 reflections / design_sessions 历史档 slug（活文件 cross-ref 保护）
  "2026-04-21_cc-space-gg-usage-sweep"
  "2026-05-01_cc-space-memory-decommission"
  "2026-05-08_cc-space-claude-md-split"
  "2026-05-08_cc-space-context-curation-meta"
  "2026-05-08_cc-space-design-asset-integration"
  "2026-05-14_cc-space-inbox-architecture"
  "2026-05-17_cc-space-memory-retrieval-discipline-and-life-domain-boundary"
  "2026-05-19_cc-space-briefing-evaluator-gate"
)

# 文件级 carve-out（这些文件整文件不动）
HISTORICAL_PATHS=(
  "threads/cc-space-as-living-trunk.md"
  "threads/cc-space-memory-decommission.md"
  "threads/cc-space-design-system.md"
  "inbox/briefs/cc-space-to-monster-rename.md"
  "inbox/closed"
  "auto-maintenance/memory-decommissioned-snapshot"
  "chat/log.jsonl"
  "chat/history"
)

# sed 排除目录
EXCLUDE_DIRS=(
  ".git" "__pycache__" "node_modules" ".venv" ".build"
  "build" ".next" "dist" ".DS_Store"
)

# === M6: gg 自身 13 个活文件（硬编码清单，audit.md §1.2） ===
GG_ACTIVE_FILES=(
  "auto_gg.md"
  "cc_agent.md"
  "CLAUDE.md"
  "memory/next_session_agenda.md"
  "memory/state.md"
  "scheduled/README.md"
  "scheduled/STATUS_SCAN.md"
  "tools/nw-reconciliation.md"
  "tools/TOOLS.md"
  "tracks/architecture.md"
  "tracks/cc.md"
  "tracks/humanity.md"
  "tracks/keith.md"
)

# 改完仓后的 repo 路径（Phase 5+ 用）
CUR_REPO() {
  if [ -d "$NEW_REPO" ]; then echo "$NEW_REPO"; else echo "$OLD_REPO"; fi
}

# === Helpers ===
log_phase() { echo -e "\n=== Phase $1: $2 ==="; }
log_step()  { echo "  → $*"; }
log_ok()    { echo "[OK] $*"; }
log_fail()  { echo "[FAIL] $*" >&2; exit 1; }
log_dry()   { echo "  [DRY-RUN] $*"; }

is_dry() { [ "$DRY_RUN" = "1" ]; }

ack() {
  if is_dry; then
    log_dry "ack: $1 (dry-run 自动通过)"
    return 0
  fi
  echo ""
  echo "════════════════════════════════════════════════"
  echo "[ACK NEEDED] $1"
  echo "════════════════════════════════════════════════"
  read -r -p "输入 yes 继续，其他中止: " ans
  [ "$ans" = "yes" ] || { echo "已中止"; exit 1; }
}

# 构造 historical paths 的 grep -Ev pattern
build_historical_grep_v() {
  local pattern=""
  for p in "${HISTORICAL_PATHS[@]}"; do
    [ -n "$pattern" ] && pattern+="|"
    pattern+="$p"
  done
  echo "$pattern"
}

# 构造 historical tokens 的 grep -E pattern（用于 awk）
build_historical_tokens_pattern() {
  local pattern=""
  for t in "${HISTORICAL_TOKENS[@]}"; do
    [ -n "$pattern" ] && pattern+="|"
    pattern+="$t"
  done
  echo "$pattern"
}

# ─────────────────────────────────────────────────────────
# M1 核心：行级 sed（awk 逐行判断，含 HISTORICAL_TOKENS 的整行保留）
# 参数:
#   $1 = pattern (literal，用作 awk index 判断 + gsub 转义)
#   $2 = replacement
#   $3 = file path
# ─────────────────────────────────────────────────────────
sed_file_line_safe() {
  local pattern="$1" replacement="$2" file="$3"
  local tokens_pat
  tokens_pat="$(build_historical_tokens_pattern)"

  if is_dry; then
    if grep -q -F "$pattern" "$file" 2>/dev/null; then
      # 预估改动行数（剔除含 historical token 的行）
      local hit
      hit=$(grep -F "$pattern" "$file" | grep -Ev "$tokens_pat" | wc -l | tr -d ' ')
      log_dry "would sed ($hit lines): ${file}"
    fi
    return 0
  fi

  # 真实执行：awk 跳过含 historical token 的行
  local tmp
  tmp="$(mktemp)"
  awk -v pat="$pattern" -v rep="$replacement" -v tokens="$tokens_pat" '
    BEGIN { split(tokens, toks, "|") }
    {
      skip = 0
      for (i in toks) {
        if (toks[i] != "" && index($0, toks[i]) > 0) { skip = 1; break }
      }
      if (skip == 1) { print; next }
      # gsub 做字面替换（pat 是 literal，转义正则元字符）
      tmp_pat = pat
      gsub(/[][\\.^$*+?(){}|]/, "\\\\&", tmp_pat)
      gsub(tmp_pat, rep)
      print
    }
  ' "$file" > "$tmp"
  if ! cmp -s "$file" "$tmp"; then
    cat "$tmp" > "$file"
  fi
  rm -f "$tmp"
}

# ─────────────────────────────────────────────────────────
# 在仓内做批量 sed（排除 EXCLUDE_DIRS + HISTORICAL_PATHS + 二进制）
# 内部对每个命中文件调 sed_file_line_safe
# 参数:
#   $1 = old pattern
#   $2 = new pattern
#   $3 = repo root
# ─────────────────────────────────────────────────────────
sed_in_repo() {
  local old_pat="$1" new_pat="$2" repo="$3"
  local hist_v
  hist_v="$(build_historical_grep_v)"

  find "$repo" \
    \( -name "__pycache__" -o -name ".git" -o -name "node_modules" \
       -o -name ".venv" -o -name ".build" -o -name "build" -o -name "dist" \
       -o -name ".next" \) -prune \
    -o -type f \( -name "*.md" -o -name "*.py" -o -name "*.sh" \
       -o -name "*.json" -o -name "*.plist" -o -name "*.swift" \
       -o -name "*.yml" -o -name "*.yaml" -o -name "*.toml" \
       -o -name "*.txt" -o -name ".env*" -o -name "*.local.json" \) -print \
    | grep -Ev "$hist_v" \
    | while read -r f; do
        # 跳过二进制
        if perl -e 'exit (-B $ARGV[0] ? 0 : 1)' "$f" 2>/dev/null; then continue; fi
        if grep -q -F "$old_pat" "$f" 2>/dev/null; then
          sed_file_line_safe "$old_pat" "$new_pat" "$f"
          is_dry || echo "    修改: ${f#$repo/}"
        fi
      done
}

# 单文件 sed（M7 各小项用，full-file 替换无 token 保护）
sed_file_simple() {
  local old_pat="$1" new_pat="$2" file="$3"
  [ -f "$file" ] || { log_step "    跳过（不存在）: $file"; return 0; }
  if is_dry; then
    if grep -q -F "$old_pat" "$file" 2>/dev/null; then
      local hit
      hit=$(grep -c -F "$old_pat" "$file" || true)
      log_dry "would sed ($hit hits) in: $file"
    fi
    return 0
  fi
  if grep -q -F "$old_pat" "$file" 2>/dev/null; then
    # macOS BSD sed，escape | 用作分隔
    local esc_old esc_new
    esc_old="$(printf '%s' "$old_pat" | sed 's/[][\\.^$*/|]/\\&/g')"
    esc_new="$(printf '%s' "$new_pat" | sed 's/[\\&|]/\\&/g')"
    sed -i '' "s|${esc_old}|${esc_new}|g" "$file"
    log_step "    sed 应用: $file"
  fi
}

# === Phase 0: 前置备份 + 清理 ===
phase_0() {
  log_phase 0 "前置备份 + 清理（M4 扩充）"

  # 0.0a cc-space 仓
  log_step "0.0a 备份 cc-space 仓（含 .git，排 worktrees）"
  local backup1="${HOME_DIR}/Downloads/cc-space-backup-20260520.tar.gz"
  if [ -f "$backup1" ]; then
    echo "    已存在跳过: $(ls -lh "$backup1" | awk '{print $5, $9}')"
  elif is_dry; then
    log_dry "tar czf $backup1 -C ~/githubProject ${OLD_NAME}"
  else
    tar czf "$backup1" --exclude='.claude/worktrees' -C "${HOME_DIR}/githubProject" "${OLD_NAME}"
    echo "    [OK] $(ls -lh "$backup1" | awk '{print $5, $9}')"
  fi

  # 0.0b CC projects
  log_step "0.0b 备份 CC projects 内 cc-space 相关目录"
  local backup2="${HOME_DIR}/Downloads/cc-projects-backup-20260520.tar.gz"
  if [ -f "$backup2" ]; then
    echo "    已存在跳过: $(ls -lh "$backup2" | awk '{print $5, $9}')"
  elif is_dry; then
    log_dry "tar czf $backup2 -C ~/.claude/projects *cc-space*"
  else
    local cc_dirs
    # 用 find + tar -T -：BSD tar 对 `-` 开头文件名当 option 解析，find 输出 `./` 前缀绕开
    local cc_count
    cc_count="$(cd "${HOME_DIR}/.claude/projects" && find . -maxdepth 1 -type d -name "*cc-space*" 2>/dev/null | wc -l | tr -d ' ')"
    [ "$cc_count" -gt 0 ] || log_fail "CC projects 内未找到 cc-space 相关目录"
    (cd "${HOME_DIR}/.claude/projects" && find . -maxdepth 1 -type d -name "*cc-space*") \
      | tar czf "$backup2" -C "${HOME_DIR}/.claude/projects" -T -
    echo "    [OK] $(ls -lh "$backup2" | awk '{print $5, $9}')"
  fi

  # 0.0c CC CLI cache（M4 新增）
  log_step "0.0c 备份 CC CLI cache（~/Library/Caches/claude-cli-nodejs/-Users-xuke-githubProject-cc-space*）"
  local backup3="${HOME_DIR}/Downloads/cc-cli-cache-backup-20260520.tar.gz"
  if [ -f "$backup3" ]; then
    echo "    已存在跳过: $(ls -lh "$backup3" | awk '{print $5, $9}')"
  elif is_dry; then
    log_dry "tar czf $backup3 -C ~/Library/Caches/claude-cli-nodejs *cc-space*"
  else
    local cache_dirs
    # 同 0.0b：用 find + tar -T - 避开 BSD tar `-` 开头当 option 解析
    local cache_count
    cache_count="$(cd "${HOME_DIR}/Library/Caches/claude-cli-nodejs" 2>/dev/null && find . -maxdepth 1 -type d -name "*cc-space*" 2>/dev/null | wc -l | tr -d ' ' || echo 0)"
    if [ "$cache_count" -gt 0 ]; then
      (cd "${HOME_DIR}/Library/Caches/claude-cli-nodejs" && find . -maxdepth 1 -type d -name "*cc-space*") \
        | tar czf "$backup3" -C "${HOME_DIR}/Library/Caches/claude-cli-nodejs" -T -
      echo "    [OK] $(ls -lh "$backup3" | awk '{print $5, $9}')"
    else
      echo "    无 cc-space cache 目录，跳过"
    fi
  fi

  # 0.0d 小项 + ~/.agents（M4 扩充：.claude.json / .cc-connect / .gk / agents/gg.md）
  log_step "0.0d 备份小项（.claude/settings.json + .agents + .claude.json + .cc-connect/config.toml + .gk/repoMapping.json + .claude/agents/gg.md）"
  local small_items=(
    "${HOME_DIR}/.claude/settings.json"
    "${HOME_DIR}/.claude.json"
    "${HOME_DIR}/.cc-connect/config.toml"
    "${HOME_DIR}/.gk/repoMapping.json"
    "${HOME_DIR}/.claude/agents/gg.md"
  )
  for f in "${small_items[@]}"; do
    if [ ! -f "$f" ]; then
      echo "    跳过（不存在）: $f"
      continue
    fi
    local bf="${f}.${BAK_SUFFIX}"
    if [ -f "$bf" ]; then
      echo "    已备份: $bf"
    elif is_dry; then
      log_dry "cp $f $bf"
    else
      cp "$f" "$bf"
      echo "    [OK] $bf"
    fi
  done

  # ~/.agents 整目录
  if [ ! -d "${HOME_DIR}/.agents-backup-20260520" ]; then
    if is_dry; then
      log_dry "cp -r ~/.agents ~/.agents-backup-20260520"
    else
      cp -r "${HOME_DIR}/.agents" "${HOME_DIR}/.agents-backup-20260520"
      echo "    [OK] ~/.agents → ~/.agents-backup-20260520"
    fi
  fi

  # 0.0e ~/.claude/scheduled-tasks/ 整目录（M4 + M8 配套）
  log_step "0.0e 备份 ~/.claude/scheduled-tasks/ 整目录"
  if [ -d "${HOME_DIR}/.claude/scheduled-tasks-${BAK_SUFFIX}" ]; then
    echo "    已备份: ~/.claude/scheduled-tasks-${BAK_SUFFIX}"
  elif [ ! -d "${HOME_DIR}/.claude/scheduled-tasks" ]; then
    echo "    跳过（~/.claude/scheduled-tasks 不存在）"
  elif is_dry; then
    log_dry "cp -r ~/.claude/scheduled-tasks ~/.claude/scheduled-tasks-${BAK_SUFFIX}"
  else
    cp -r "${HOME_DIR}/.claude/scheduled-tasks" "${HOME_DIR}/.claude/scheduled-tasks-${BAK_SUFFIX}"
    echo "    [OK] ~/.claude/scheduled-tasks-${BAK_SUFFIX}"
  fi

  # 0.0f 跨仓 baseline tag（M4：cc-copilot / Voca / kebao-cc / voca-mic / cookie-arcade + gg）
  log_step "0.0f 跨仓 + gg 自身打 baseline tag '${BASELINE_TAG}'"
  local tag_repos=(
    "${HOME_DIR}/githubProject/gg"
    "${HOME_DIR}/githubProject/cc-copilot"
    "${HOME_DIR}/githubProject/Voca"
    "${HOME_DIR}/githubProject/kebao-cc"
    "${HOME_DIR}/githubProject/voca-mic"
    "${HOME_DIR}/githubProject/cookie-arcade"
  )
  for repo in "${tag_repos[@]}"; do
    if [ ! -d "$repo/.git" ]; then
      echo "    跳过（非 git 仓）: $repo"
      continue
    fi
    if is_dry; then
      log_dry "(in $repo) git commit dirty + git tag $BASELINE_TAG"
      continue
    fi
    (
      cd "$repo"
      # 先 commit dirty（如有），避免 tag 漂浮
      if ! git diff --quiet || ! git diff --staged --quiet; then
        git add -A
        git commit -m "checkpoint: dirty baseline before monster rename

Co-Authored-By: Claude Opus 4.7 <noreply@anthropic.com>" || true
      fi
      if git rev-parse "$BASELINE_TAG" >/dev/null 2>&1; then
        echo "    [tag exists] $repo: $BASELINE_TAG"
      else
        git tag "$BASELINE_TAG" && echo "    [OK] $repo: $BASELINE_TAG"
      fi
    )
  done

  # 0.1-0.3：cc-space 自身 worktree 清理 + commit + 验证（保留原流程）
  if is_dry; then
    log_dry "0.1 worktree-cleanup audit.py --clean"
    log_dry "0.2 git add -A + commit baseline (in $OLD_REPO)"
    log_dry "0.3 git worktree list 验证"
  else
    cd "$OLD_REPO"
    log_step "0.1 跑 worktree-cleanup"
    if [ -f .claude/skills/worktree-cleanup/scripts/audit.py ]; then
      python3 .claude/skills/worktree-cleanup/scripts/audit.py --clean \
        agent-a4b2f324907e57fc1 agent-a98a0a22ecafc84a3 \
        done-noise-exemption-dogfood nw-clear-mechanical || true
    else
      echo "    跳过（audit.py 不存在）"
    fi

    log_step "0.2 commit dirty 基线"
    git add -A
    if ! git diff --staged --quiet; then
      git commit -m "checkpoint: dirty files baseline before monster rename

Co-Authored-By: Claude Opus 4.7 <noreply@anthropic.com>"
    else
      log_step "  无 dirty 改动，跳过"
    fi
    # cc-space 仓自身也打 baseline tag
    if ! git rev-parse "$BASELINE_TAG" >/dev/null 2>&1; then
      git tag "$BASELINE_TAG"
      log_step "  cc-space baseline tag: $BASELINE_TAG"
    fi

    log_step "0.3 验证"
    [ "$(git worktree list | wc -l | tr -d ' ')" = "1" ] || log_fail "worktree 残留"
    [ -z "$(git status --short)" ] || log_fail "git status 非干净"
  fi

  log_ok "Phase 0 done"
}

# === Phase 1: grep 收集命中清单 ===
phase_1() {
  log_phase 1 "本机准备 - grep 命中清单"
  local repo
  repo="$(CUR_REPO)"
  cd "$repo"

  local hist_v
  hist_v="$(build_historical_grep_v)"

  log_step "1.1 cc-space 字面命中"
  grep -rln "${OLD_NAME}" . \
    --exclude-dir=.git --exclude-dir=__pycache__ --exclude-dir=node_modules \
    --exclude-dir=.venv --exclude-dir=.build --exclude-dir=build \
    | grep -Ev "$hist_v" \
    > /tmp/monster-targets.txt || true
  echo "  总命中文件: $(wc -l < /tmp/monster-targets.txt | tr -d ' ')"

  log_step "1.2 绝对路径命中"
  grep -rln "/Users/xuke/githubProject/${OLD_NAME}" . \
    --exclude-dir=.git --exclude-dir=__pycache__ \
    > /tmp/monster-paths.txt || true
  echo "  路径硬编码文件: $(wc -l < /tmp/monster-paths.txt | tr -d ' ')"

  log_ok "Phase 1 done — 清单 /tmp/monster-targets.txt + /tmp/monster-paths.txt"
}

# === Phase 2: launchd 卸载（13 个 cc-space label） ===
phase_2() {
  log_phase 2 "launchd 安全卸载（13 个 com.cc-space.*）"
  : > /tmp/monster-launchd-bak.txt

  for label in "${LAUNCHD_LABELS_OLD[@]}"; do
    local full="${OLD_LABEL_PREFIX}.${label}"
    if is_dry; then
      log_dry "launchctl bootout gui/${UID_NUM}/${full}"
    else
      log_step "bootout ${full}"
      launchctl bootout "gui/${UID_NUM}/${full}" 2>&1 \
        | grep -v "Could not find specified service" || true
    fi
    echo "${full}" >> /tmp/monster-launchd-bak.txt
  done

  if is_dry; then
    log_ok "Phase 2 dry-run done"
    return 0
  fi

  local remaining
  remaining="$(launchctl list | grep -c "${OLD_LABEL_PREFIX}" || true)"
  [ "$remaining" = "0" ] || log_fail "仍有 $remaining 个 ${OLD_LABEL_PREFIX} label 未卸"

  log_ok "Phase 2 done — 13 个 label 全卸"
}

# === M5: Phase 2.5 cc-connect bootout ===
phase_2_5() {
  log_phase 2.5 "cc-connect 卸载（第 14 个独立 label，M5）"
  if is_dry; then
    log_dry "launchctl bootout gui/${UID_NUM}/com.cc-connect"
  else
    launchctl bootout "gui/${UID_NUM}/com.cc-connect" 2>&1 \
      | grep -v "Could not find specified service" \
      | grep -v "Boot-out failed: 3: No such process" || true
    # bootout 异步——retry 直到 launchctl list 不含 cc-connect（max 6 次 × 1s = 6s 等待）
    local has retry
    for retry in 1 2 3 4 5 6; do
      sleep 1
      has="$(launchctl list | grep -c "com.cc-connect" || true)"
      [ "$has" = "0" ] && break
    done
    [ "$has" = "0" ] || log_fail "com.cc-connect 仍存活（6s retry 后）"
  fi
  log_ok "Phase 2.5 done"
}

# === Phase 3: 仓内 P0 必改 ===
phase_3() {
  log_phase 3 "仓内 P0 必改（含 M1 行级保护 + M3 plist 全量替换）"
  local repo
  repo="$(CUR_REPO)"

  log_step "3.1 批量 sed：绝对路径 + 单词 cc-space（行级 historical token 保护）"
  if is_dry; then
    log_dry "sed_in_repo /Users/xuke/githubProject/cc-space → monster"
    log_dry "sed_in_repo cc-space → monster (含 historical token 行保留)"
  else
    sed_in_repo "/Users/xuke/githubProject/${OLD_NAME}" "/Users/xuke/githubProject/${NEW_NAME}" "$repo"
    sed_in_repo "${OLD_NAME}" "${NEW_NAME}" "$repo"
  fi

  log_step "3.2 plist 文件重命名（M3 全量替换 + auto-cc-space → auto-monster）"
  if [ -d "${repo}/scheduled/plists" ]; then
    for old_plist in "${repo}/scheduled/plists/${OLD_LABEL_PREFIX}".*.plist \
                     "${repo}/scheduled/plists/_disabled/${OLD_LABEL_PREFIX}".*.plist; do
      [ -f "$old_plist" ] || continue
      # 1) 前缀全量替换 com.cc-space → com.monster
      local new_plist="${old_plist//${OLD_LABEL_PREFIX}/${NEW_LABEL_PREFIX}}"
      # 2) 末段 auto-cc-space → auto-monster（Q1=A 决策）
      new_plist="${new_plist//auto-cc-space/auto-monster}"
      if [ "$old_plist" = "$new_plist" ]; then continue; fi
      if is_dry; then
        log_dry "mv $(basename "$old_plist") → $(basename "$new_plist")"
      else
        mv "$old_plist" "$new_plist"
        log_step "    rename: $(basename "$old_plist") → $(basename "$new_plist")"
      fi
    done
  fi

  log_ok "Phase 3 done"
}

# === Phase 4: 仓内 P1 文档级（已在 phase_3 sed 中完成） ===
phase_4() {
  log_phase 4 "仓内 P1 文档级"
  log_step "MEMORY.md 由 threads_sync.py 派生，Phase 9 重跑即可"
  log_ok "Phase 4 done（已在 Phase 3 sed 中完成）"
}

# === Phase 5: git mv 仓路径 ===
phase_5() {
  log_phase 5 "git mv 仓路径"
  if is_dry; then
    log_dry "(in $OLD_REPO) git add -A + commit rename"
    log_dry "mv ${OLD_REPO} → ${NEW_REPO}"
    log_ok "Phase 5 dry-run done"
    return 0
  fi
  cd "$OLD_REPO"

  log_step "5.1 提交 rename commit"
  git add -A
  if ! git diff --staged --quiet; then
    git commit -m "rename: cc-space → monster (full rename)

Co-Authored-By: Claude Opus 4.7 <noreply@anthropic.com>"
  fi

  log_step "5.2 mv 仓目录 ${OLD_REPO} → ${NEW_REPO}"
  cd "${HOME_DIR}/githubProject"
  mv "${OLD_NAME}" "${NEW_NAME}"

  log_step "5.3 验证"
  cd "$NEW_REPO"
  [ -z "$(git status --short)" ] || log_fail "git status 非干净"
  git remote -v | grep "${OLD_NAME}" >/dev/null && log_step "  ⚠️  remote 仍指旧 URL，Phase 8 处理"

  log_ok "Phase 5 done"
}

# === Phase 6: launchd 重新装载（13 个 com.monster.*） ===
phase_6() {
  log_phase 6 "launchd 重新装载（13 个 com.monster.*）"

  local i=0
  for old_lbl in "${LAUNCHD_LABELS_OLD[@]}"; do
    local new_lbl="${LAUNCHD_LABELS_NEW[$i]}"
    i=$((i + 1))
    local plist="${NEW_REPO}/scheduled/plists/${NEW_LABEL_PREFIX}.${new_lbl}.plist"
    if [ ! -f "$plist" ]; then
      if is_dry; then
        log_dry "(skip, plist not found in dry-run target): $plist"
      else
        log_step "  ⚠️ plist 不存在: $plist（_disabled? 跳过）"
      fi
      continue
    fi
    if is_dry; then
      log_dry "launchctl bootstrap gui/${UID_NUM} $plist"
    else
      log_step "bootstrap ${NEW_LABEL_PREFIX}.${new_lbl}"
      launchctl bootstrap "gui/${UID_NUM}" "$plist"
    fi
  done

  if is_dry; then
    log_ok "Phase 6 dry-run done"
    return 0
  fi

  local loaded
  loaded="$(launchctl list | grep -c "${NEW_LABEL_PREFIX}" || true)"
  [ "$loaded" -ge 13 ] || log_fail "仅装载 $loaded 个（预期 13）"

  log_step "6.3 kickstart chat-prep 验证可执行"
  launchctl kickstart "gui/${UID_NUM}/${NEW_LABEL_PREFIX}.chat-prep" || true

  log_ok "Phase 6 done — $loaded 个 label 装载"
}

# === M5: Phase 6.5 cc-connect bootstrap ===
phase_6_5() {
  log_phase 6.5 "cc-connect 重新装载 + PID 验证（M5）"
  local plist="${HOME_DIR}/Library/LaunchAgents/com.cc-connect.plist"
  if [ ! -f "$plist" ]; then
    log_step "  ⚠️ plist 不存在: $plist 跳过"
    log_ok "Phase 6.5 done (skipped)"
    return 0
  fi
  if is_dry; then
    log_dry "launchctl bootstrap gui/${UID_NUM} $plist"
    log_dry "sleep 2 && launchctl list | grep com.cc-connect (验证 PID 非空非 0)"
    log_ok "Phase 6.5 dry-run done"
    return 0
  fi
  launchctl bootstrap "gui/${UID_NUM}" "$plist"
  sleep 2
  local line pid
  line="$(launchctl list | grep com.cc-connect || true)"
  if [ -z "$line" ]; then
    log_fail "com.cc-connect 未出现在 launchctl list"
  fi
  pid="$(echo "$line" | awk '{print $1}')"
  if [ -z "$pid" ] || [ "$pid" = "-" ] || [ "$pid" = "0" ]; then
    log_fail "com.cc-connect PID 异常: '$pid'（line: $line）"
  fi
  log_ok "Phase 6.5 done — cc-connect PID=$pid"
}

# === Phase 7: 本机仓外（M7 大改） ===
phase_7() {
  log_phase 7 "本机仓外（M7 多项扩充）"

  # 7.0a ~/.claude.json（Q2=b：只改绝对路径，不改单词 cc-space）
  log_step "7.0a ~/.claude.json（M7：只改绝对路径，保留 GitHub identifier / task history 字面）"
  sed_file_simple \
    "/Users/xuke/githubProject/${OLD_NAME}" \
    "/Users/xuke/githubProject/${NEW_NAME}" \
    "${HOME_DIR}/.claude.json"

  # 7.0b ~/.gk/repoMapping.json（绝对路径 + keithMonster/cc-space identifier）
  log_step "7.0b ~/.gk/repoMapping.json（绝对路径 + keithMonster/cc-space → keithMonster/monster）"
  sed_file_simple \
    "/Users/xuke/githubProject/${OLD_NAME}" \
    "/Users/xuke/githubProject/${NEW_NAME}" \
    "${HOME_DIR}/.gk/repoMapping.json"
  sed_file_simple \
    "keithMonster/${OLD_NAME}" \
    "keithMonster/${NEW_NAME}" \
    "${HOME_DIR}/.gk/repoMapping.json"

  # 7.0c ~/.claude/agents/gg.md（单词 cc-space → monster）
  log_step "7.0c ~/.claude/agents/gg.md（M7：单词 cc-space → monster）"
  sed_file_simple "${OLD_NAME}" "${NEW_NAME}" "${HOME_DIR}/.claude/agents/gg.md"

  # 7.0d ~/.cc-connect/config.toml（只改 work_dir = ".../cc-space" 这一种 pattern）
  log_step "7.0d ~/.cc-connect/config.toml（M7：只改 work_dir 行，避免改 bot_secret/app_id）"
  local cccfg="${HOME_DIR}/.cc-connect/config.toml"
  if [ -f "$cccfg" ]; then
    if is_dry; then
      local hit
      set +e
      hit=$(grep -c "work_dir.*${OLD_NAME}" "$cccfg" 2>/dev/null)
      set -e
      hit="${hit:-0}"
      log_dry "would sed work_dir lines in ${cccfg} (hits=$hit)"
    else
      # 只对包含 work_dir 字面的行做 sed
      local tmp
      tmp="$(mktemp)"
      awk -v old="$OLD_NAME" -v new="$NEW_NAME" '
        {
          if (index($0, "work_dir") > 0 && index($0, old) > 0) {
            gsub(old, new)
          }
          print
        }
      ' "$cccfg" > "$tmp"
      if ! cmp -s "$cccfg" "$tmp"; then
        cat "$tmp" > "$cccfg"
        log_step "    [OK] work_dir 行已改"
      fi
      rm -f "$tmp"
      # 验证 monster work_dir 数 = 4
      local new_cnt
      set +e
      new_cnt=$(grep -c "work_dir.*${NEW_NAME}" "$cccfg" 2>/dev/null)
      set -e
      new_cnt="${new_cnt:-0}"
      [ "$new_cnt" = "4" ] || log_step "    ⚠️ monster work_dir 数=$new_cnt（预期 4，请手工确认）"
    fi
  else
    log_step "    跳过（~/.cc-connect/config.toml 不存在）"
  fi

  # 7.1 ~/.claude/settings.json statusline hook（原有）
  log_step "7.1 ~/.claude/settings.json statusline hook"
  sed_file_simple \
    "/Users/xuke/githubProject/${OLD_NAME}" \
    "/Users/xuke/githubProject/${NEW_NAME}" \
    "${HOME_DIR}/.claude/settings.json"

  # 7.2-7.4 ~/.agents/skills/ 全量 find + sed（M7：从 3 个扩到全量）
  # 排除 notify/sent + notify/dedup + done/logs 历史档（事件叙事/会话复盘/launchd dedup，按 essence fast-slow-divide 不改）
  log_step "7.2-7.4 ~/.agents/skills/ 全量 find + sed（排除 notify/sent + notify/dedup + done/logs）"
  if [ -d "${HOME_DIR}/.agents/skills" ]; then
    find -L "${HOME_DIR}/.agents/skills" \
      -not -path "*/notify/sent/*" \
      -not -path "*/notify/dedup/*" \
      -not -path "*/done/logs/*" \
      -type f \( -name "*.md" -o -name "*.sh" -o -name "*.py" -o -name "*.json" -o -name "*.toml" -o -name "*.yml" -o -name "*.yaml" \) \
      2>/dev/null \
      | while read -r f; do
          if grep -q -F "${OLD_NAME}" "$f" 2>/dev/null; then
            if is_dry; then
              local hit
              hit=$(grep -c -F "${OLD_NAME}" "$f")
              log_dry "would sed ($hit hits): $f"
            else
              sed -i '' "s|${OLD_NAME}|${NEW_NAME}|g" "$f"
              echo "    修改: $f"
            fi
          fi
        done
  fi

  # 7.4b ~/.agents/skill-notes/done.md（M7 单独处理）
  log_step "7.4b ~/.agents/skill-notes/done.md"
  sed_file_simple "${OLD_NAME}" "${NEW_NAME}" "${HOME_DIR}/.agents/skill-notes/done.md"

  # 7.5 gg 自身 13 个活文件（M6 + 修复 4：改用 sed_file_line_safe 行级保护）
  # 让 HISTORICAL_TOKENS（含 8 个 gg 内历史档 slug）的整行被保留，保护活文件里的 cross-ref
  log_step "7.5 gg 自身 13 个活文件（M6 硬编码清单 + 行级 historical token 保护）"
  local gg_root="${HOME_DIR}/githubProject/gg"
  for rel in "${GG_ACTIVE_FILES[@]}"; do
    local f="${gg_root}/${rel}"
    if [ ! -f "$f" ]; then
      log_step "    跳过（不存在）: $rel"
      continue
    fi
    if grep -q -F "${OLD_NAME}" "$f" 2>/dev/null; then
      sed_file_line_safe "${OLD_NAME}" "${NEW_NAME}" "$f"
      is_dry || echo "    修改: gg/$rel"
    fi
  done

  # M6 验证：essence.md 中 monster 字面数应 = 0（essence.md NOT IN）
  log_step "7.5a 验证 essence.md NOT IN（M6：monster 字面数应 = 0）"
  local ess="${gg_root}/memory/essence.md"
  if [ -f "$ess" ]; then
    # grep -c 总是打印数字到 stdout，0 命中时 exit 1。用 set +e 隔离
    local mon_cnt
    set +e
    mon_cnt=$(grep -c "${NEW_NAME}" "$ess" 2>/dev/null)
    set -e
    mon_cnt="${mon_cnt:-0}"
    if [ "$mon_cnt" != "0" ]; then
      if is_dry; then
        log_dry "essence.md 已含 monster 字面 ($mon_cnt 处) — dry-run 不阻断"
      else
        log_fail "essence.md 含 ${NEW_NAME} 字面 ($mon_cnt 处)，违反 NOT IN 铁律"
      fi
    fi
  fi

  # 7.6 cg-platform-template
  log_step "7.6 cg-platform-template"
  for f in "${HOME_DIR}/CGProject/cg-platform-template/AGENTS.md" \
           "${HOME_DIR}/CGProject/cg-platform-template/ENGINEERING-STANDARD.md"; do
    sed_file_simple "${OLD_NAME}" "${NEW_NAME}" "$f"
  done

  # 7.7 跨仓 sed 前 ack（M10）
  log_step "7.7 跨仓 sed（kebao-cc/cc-copilot/Voca/voca-mic/cookie-arcade）+ M10 ack"
  echo ""
  echo "── 跨仓命中清单 ──────────────────────────────"
  for repo in kebao-cc cc-copilot Voca voca-mic cookie-arcade; do
    local rp="${HOME_DIR}/githubProject/${repo}"
    [ -d "$rp" ] || { echo "  [skip] $repo 不存在"; continue; }
    echo "  ── $repo ──"
    grep -rln "${OLD_NAME}" "$rp" \
      --exclude-dir=.git --exclude-dir=node_modules --exclude-dir=.venv \
      --exclude-dir=.build --exclude-dir=build --exclude-dir=dist \
      --exclude-dir=.next --exclude-dir=Contents 2>/dev/null \
      | grep -v "/history/" | grep -v "/log/" \
      | sed 's/^/    /' || true
  done
  echo "──────────────────────────────────────────────"

  ack "上方跨仓命中清单确认无误？yes 继续 sed"

  for repo in kebao-cc cc-copilot Voca voca-mic cookie-arcade; do
    local rp="${HOME_DIR}/githubProject/${repo}"
    [ -d "$rp" ] || continue
    grep -rln "${OLD_NAME}" "$rp" \
      --exclude-dir=.git --exclude-dir=node_modules --exclude-dir=.venv \
      --exclude-dir=.build --exclude-dir=build --exclude-dir=dist \
      --exclude-dir=.next --exclude-dir=Contents 2>/dev/null \
      | while read -r f; do
          [[ "$f" == *"/history/"* ]] && continue
          [[ "$f" == *"/log/"* ]] && continue
          # 二进制兜底检测（sed_in_repo 同款逻辑）
          if perl -e 'exit (-B $ARGV[0] ? 0 : 1)' "$f" 2>/dev/null; then continue; fi
          if is_dry; then
            log_dry "would sed: $f"
          else
            sed -i '' "s|${OLD_NAME}|${NEW_NAME}|g" "$f"
            echo "    修改: $f"
          fi
        done
  done

  # 7.8 scheduled-tasks/auto_cc_space → auto_monster（M8）
  phase_7_8

  log_ok "Phase 7 done"
}

# === M8: Phase 7.8 scheduled-tasks 目录改名 + 内部 sed ===
phase_7_8() {
  log_phase 7.8 "scheduled-tasks/auto_cc_space → auto_monster（M8）"
  local src="${HOME_DIR}/.claude/scheduled-tasks/auto_cc_space"
  local dst="${HOME_DIR}/.claude/scheduled-tasks/auto_monster"
  if [ ! -d "$src" ]; then
    log_step "  跳过（$src 不存在）"
    log_ok "Phase 7.8 done (skipped)"
    return 0
  fi
  if is_dry; then
    log_dry "mv $src → $dst"
    log_dry "find $dst -type f \\( -name SKILL.md -o -name '*.json' -o -name '*.sh' \\) -exec sed cc-space/cc_space → monster"
  else
    mv "$src" "$dst"
    log_step "  mv: auto_cc_space → auto_monster"
    find "$dst" -type f \( -name "SKILL.md" -o -name "*.json" -o -name "*.sh" -o -name "*.md" \) \
      | while read -r f; do
          local changed=0
          if grep -q -F "${OLD_NAME}" "$f" 2>/dev/null; then
            sed -i '' "s|${OLD_NAME}|${NEW_NAME}|g" "$f"
            changed=1
          fi
          # 下划线变体 cc_space → monster
          if grep -q -F "cc_space" "$f" 2>/dev/null; then
            sed -i '' "s|cc_space|${NEW_NAME}|g" "$f"
            changed=1
          fi
          [ "$changed" = "1" ] && echo "    修改: ${f#$dst/}"
        done
  fi
  log_ok "Phase 7.8 done"
}

# === Phase 8: GitHub 改名 ===
phase_8() {
  log_phase 8 "GitHub 远端改名"
  if is_dry; then
    log_dry "ack + gh repo rename ${NEW_NAME} --repo keithMonster/${OLD_NAME} --yes"
    log_dry "git remote set-url origin git@github.com:keithMonster/${NEW_NAME}.git"
    log_dry "git fetch + git push"
    log_ok "Phase 8 dry-run done"
    return 0
  fi
  cd "$NEW_REPO"

  ack "准备执行 GitHub 远端改名:
  gh repo rename ${NEW_NAME} --repo keithMonster/${OLD_NAME}
  git remote set-url origin git@github.com:keithMonster/${NEW_NAME}.git
这是对外身份变更（GitHub 自动 301 但仓名公开变了）。"

  log_step "8.1 gh repo rename"
  gh repo rename "${NEW_NAME}" --repo "keithMonster/${OLD_NAME}" --yes

  log_step "8.2 git remote set-url"
  git remote set-url origin "git@github.com:keithMonster/${NEW_NAME}.git"

  log_step "8.3 验证"
  git remote -v
  git fetch origin

  log_step "8.4 push"
  git push origin main

  log_ok "Phase 8 done — GitHub 仓名 = ${NEW_NAME}"
}

# === Phase 9: 验证收尾 ===
phase_9() {
  log_phase 9 "验证收尾"
  if is_dry; then
    log_dry "9.1-9.6 验证项（dry-run 跳过实际验证，仅打印目标）"
    log_ok "Phase 9 dry-run done"
    return 0
  fi
  cd "$NEW_REPO"

  log_step "9.1 CC statusline hook 路径"
  grep "/Users/xuke/githubProject/${NEW_NAME}" "${HOME_DIR}/.claude/settings.json" \
    | head -2 || log_fail "statusline hook 未指向 monster"

  log_step "9.2 threads_sync.py 派生 MEMORY.md"
  if [ -f shared/scripts/threads_sync.py ]; then
    python3 shared/scripts/threads_sync.py || log_step "  ⚠️ threads_sync.py 失败"
  fi

  log_step "9.3 抽 launchd kickstart 验证"
  launchctl kickstart "gui/${UID_NUM}/${NEW_LABEL_PREFIX}.chat-prep" || true

  log_step "9.4 notify.sh 推测试消息"
  "${HOME_DIR}/.agents/skills/notify/bin/notify.sh" info monster-rename-test \
    "改名 cc-space → monster Phase 9 验收测试" || log_step "  ⚠️ notify 失败"

  log_step "9.5 done skill Glob 测试"
  ls "${NEW_REPO}/threads/"*.md > /dev/null 2>&1 && log_step "  threads/*.md 可 Glob"

  log_step "9.6 git status / log"
  git status
  git log --oneline -5

  log_ok "Phase 9 done — 验证全过"
}

# === Phase 10: CC transcript 迁移 + Library/Caches（M9） ===
phase_10() {
  log_phase 10 "CC transcript + cli-cache 迁移（D2 + M9）"

  ack "准备迁移：
  - ~/.claude/projects/ 下 12 个 -Users-xuke-githubProject-cc-space* 目录 + jsonl cwd 字段全替换
  - ~/Library/Caches/claude-cli-nodejs/ 下 8 个 -Users-xuke-githubProject-cc-space* 目录前缀 mv（不动内部）
备份: ~/Downloads/cc-projects-backup-20260520.tar.gz + ~/Downloads/cc-cli-cache-backup-20260520.tar.gz"

  log_step "10.1 mv 12 个 projects/ 目录前缀"
  for d in "${HOME_DIR}/.claude/projects/-Users-xuke-githubProject-${OLD_NAME}"*; do
    [ -d "$d" ] || continue
    local newd="${d/${OLD_NAME}/${NEW_NAME}}"
    if is_dry; then
      log_dry "mv $(basename "$d") → $(basename "$newd")"
    else
      mv "$d" "$newd"
      log_step "    $(basename "$d") → $(basename "$newd")"
    fi
  done

  log_step "10.2 sed 替换所有 jsonl 内部 cwd 字段"
  if is_dry; then
    log_dry "find projects/ -name '*.jsonl' -exec sed cwd"
  else
    find "${HOME_DIR}/.claude/projects/-Users-xuke-githubProject-${NEW_NAME}"* \
      -name "*.jsonl" \
      -exec sed -i '' "s|/Users/xuke/githubProject/${OLD_NAME}|/Users/xuke/githubProject/${NEW_NAME}|g" {} +
  fi

  # M9: Library/Caches 8 目录前缀 mv（不动内部，cache 内容是 CC 自管）
  log_step "10.3 mv ~/Library/Caches/claude-cli-nodejs/ 8 个目录前缀（M9）"
  local cache_root="${HOME_DIR}/Library/Caches/claude-cli-nodejs"
  if [ -d "$cache_root" ]; then
    for d in "${cache_root}/-Users-xuke-githubProject-${OLD_NAME}"*; do
      [ -d "$d" ] || continue
      local newd="${d/${OLD_NAME}/${NEW_NAME}}"
      if is_dry; then
        log_dry "mv $(basename "$d") → $(basename "$newd")"
      else
        mv "$d" "$newd"
        log_step "    $(basename "$d") → $(basename "$newd")"
      fi
    done
  else
    log_step "    跳过（$cache_root 不存在）"
  fi

  log_step "10.4 实测提示"
  echo "    请 Keith 跑: claude --resume <一个旧 sessionId>"
  echo "    如果失败回滚: bash $SELF_DIR/rollback.sh（或手动 tar xzf 还原）"

  log_ok "Phase 10 done — D2 + M9 迁移完成（实测请 Keith 验）"
}

# === Main ===
main() {
  local target="${1:-all}"

  # M11: dry-run 模式判定
  if [ "$target" = "dry-run" ]; then
    DRY_RUN=1
    target="all"
  fi
  export DRY_RUN

  echo "════════════════════════════════════════════════"
  echo "  cc-space → monster 改名脚本 v2"
  echo "  目标 phase: $target"
  echo "  脚本位置: $0"
  echo "  当前 cwd: $(pwd)"
  echo "  DRY_RUN: $DRY_RUN"
  echo "  MONSTER_RENAME_DIR: $MONSTER_RENAME_DIR"
  echo "════════════════════════════════════════════════"

  # 安全检查：cwd 不能在 cc-space/monster 内
  case "$(pwd)" in
    "$OLD_REPO"*|"$NEW_REPO"*)
      log_fail "cwd 在 cc-space/monster 内，Phase 5 mv 会失效。请 cd 到 gg/ 或其他外部目录"
      ;;
  esac

  case "$target" in
    0)    phase_0 ;;
    1)    phase_1 ;;
    2)    phase_2 ;;
    2.5)  phase_2_5 ;;
    3)    phase_3 ;;
    4)    phase_4 ;;
    5)    phase_5 ;;
    6)    phase_6 ;;
    6.5)  phase_6_5 ;;
    7)    phase_7 ;;
    7.8)  phase_7_8 ;;
    8)    phase_8 ;;
    9)    phase_9 ;;
    10)   phase_10 ;;
    all)
      phase_0
      phase_1
      phase_2
      phase_2_5
      phase_3
      phase_4
      phase_5
      phase_6
      phase_6_5
      phase_7
      phase_8
      phase_9
      echo ""
      echo "════════════════════════════════════════════════"
      echo "  Phase 0-9 完成，phase 10 单独跑"
      echo "    bash $0 10"
      echo "════════════════════════════════════════════════"
      ;;
    *)
      echo "用法: bash $0 {0|1|2|2.5|3|4|5|6|6.5|7|7.8|8|9|10|all|dry-run}" >&2
      exit 1
      ;;
  esac
}

main "$@"
