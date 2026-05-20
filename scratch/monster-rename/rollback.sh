#!/usr/bin/env bash
# rollback.sh — monster-rename 单行回滚脚本
# 用法：bash ~/githubProject/gg/scratch/monster-rename/rollback.sh
#
# 物理含义：执行后系统状态等价于 monster-rename.sh 运行前的备份点
# (cc-space-backup-20260520 / cc-projects-backup-20260520 / cc-cli-cache-backup-20260520
#  / scheduled-tasks-bak-20260520 / .agents-backup-20260520 / 各 .bak-20260520 + 各仓 rename-baseline-20260520 tag)
#
# 设计原则（见 audit.md §4）：
#   - set -uo pipefail（不用 -e，单步失败不 abort 后续，回滚要尽量跑完所有可逆步骤）
#   - 每步独立 try-catch：失败 → [WARN] 继续
#   - 幂等：第二次跑基本 no-op
#   - 单次 ack：启动一次 yes 确认，中途不打断
#   - 关键安全闸：禁止任何 sed/find 全文跑；备份缺失直接 exit 2
#   - 退出码：完全 OK = 0 / 部分失败 = 1 / 关键备份缺失 = 2

set -uo pipefail

# ============================================================================
# 配置 / 常量
# ============================================================================

readonly STAMP="20260520"
readonly HOME_DIR="${HOME}"
readonly GH_PROJECT_DIR="${HOME_DIR}/githubProject"
readonly BACKUP_TARBALL_REPO="${HOME_DIR}/Downloads/cc-space-backup-${STAMP}.tar.gz"
readonly BACKUP_TARBALL_PROJECTS="${HOME_DIR}/Downloads/cc-projects-backup-${STAMP}.tar.gz"
readonly BACKUP_TARBALL_CLI_CACHE="${HOME_DIR}/Downloads/cc-cli-cache-backup-${STAMP}.tar.gz"
readonly BACKUP_DIR_SCHEDULED="${HOME_DIR}/.claude/scheduled-tasks-bak-${STAMP}"
readonly BACKUP_DIR_AGENTS="${HOME_DIR}/.agents-backup-${STAMP}"
readonly LAUNCHD_BAK_LIST="/tmp/monster-launchd-bak.txt"
readonly BASELINE_TAG="rename-baseline-${STAMP}"

# 跨仓清单（含 gg 自己）
readonly CROSS_REPOS=(
  "${GH_PROJECT_DIR}/gg"
  "${GH_PROJECT_DIR}/cc-copilot"
  "${GH_PROJECT_DIR}/Voca"
  "${GH_PROJECT_DIR}/kebao-cc"
  "${GH_PROJECT_DIR}/voca-mic"
  "${GH_PROJECT_DIR}/cookie-arcade"
)

# 小项备份（src .bak → dst 还原路径）
# 用并行数组（macOS bash 3.x 无关联数组）
readonly SMALL_ITEMS=(
  "${HOME_DIR}/.claude.json.bak-${STAMP}|${HOME_DIR}/.claude.json"
  "${HOME_DIR}/.cc-connect/config.toml.bak-${STAMP}|${HOME_DIR}/.cc-connect/config.toml"
  "${HOME_DIR}/.gk/repoMapping.json.bak-${STAMP}|${HOME_DIR}/.gk/repoMapping.json"
  "${HOME_DIR}/.claude/settings.json.bak-${STAMP}|${HOME_DIR}/.claude/settings.json"
  "${HOME_DIR}/.claude/agents/gg.md.bak-${STAMP}|${HOME_DIR}/.claude/agents/gg.md"
)

# ============================================================================
# 状态聚合
# ============================================================================

declare -i STEP_OK=0
declare -i STEP_SKIP=0
declare -i STEP_WARN=0
REPORT_LINES=()

log_ok()   { echo "  [OK]   $*";   STEP_OK=$((STEP_OK+1));     REPORT_LINES+=("[OK]   $*"); }
log_skip() { echo "  [SKIP] $*";   STEP_SKIP=$((STEP_SKIP+1)); REPORT_LINES+=("[SKIP] $*"); }
log_warn() { echo "  [WARN] $*" >&2; STEP_WARN=$((STEP_WARN+1)); REPORT_LINES+=("[WARN] $*"); }

phase_banner() {
  echo ""
  echo "── 步骤 $1 / 11 — $2 ──"
}

# 每步用 || true 兜底，单步失败不 abort 全局（即便 pipefail）
safe() {
  # safe "<描述>" <cmd...>
  local desc="$1"; shift
  if "$@"; then
    log_ok "$desc"
    return 0
  else
    log_warn "$desc — 命令失败 (exit $?)"
    return 1
  fi
}

# ============================================================================
# 启动横幅 + 关键备份存在性闸
# ============================================================================

cat <<EOF

================================================================================
  monster-rename 单行回滚脚本
  时间戳: ${STAMP}
================================================================================

将依次回滚以下 11 项：

   1) 仓本身              ~/githubProject/monster → ~/githubProject/cc-space (tar 还原)
   2) CC projects jsonl   ~/.claude/projects/...-monster* → cc-space* (tar 还原)
   3) CC CLI cache        ~/Library/Caches/claude-cli-nodejs/...-monster* → cc-space* (tar 还原)
   4) scheduled-tasks     ~/.claude/scheduled-tasks → 备份副本
   5) launchd com.monster.*  bootout → bootstrap com.cc-space.* (13 个)
   6) launchd cc-connect  bootout → bootstrap com.cc-connect
   7) 小项备份            .claude.json / cc-connect config.toml / gk repoMapping.json
                          / .claude/settings.json / .claude/agents/gg.md
   8) ~/.agents           rm -rf + 备份副本
   9) gg 自身             git reset --hard ${BASELINE_TAG}
  10) 跨仓 (5 个)         cc-copilot / Voca / kebao-cc / voca-mic / cookie-arcade git reset
  11) GitHub rename       仅提示（不自动执行——gh repo rename 是 GitHub 端显式动作）

EOF

# 关键备份缺失闸（核心三 tarball + agents/scheduled 备份目录）—— 缺一就 exit 2
echo "── 备份存在性检查 ──"
MISSING=()
for f in "${BACKUP_TARBALL_REPO}" "${BACKUP_TARBALL_PROJECTS}" "${BACKUP_TARBALL_CLI_CACHE}"; do
  if [[ ! -f "$f" ]]; then
    MISSING+=("$f")
    echo "  [MISSING] $f"
  else
    echo "  [PRESENT] $f"
  fi
done
for d in "${BACKUP_DIR_SCHEDULED}" "${BACKUP_DIR_AGENTS}"; do
  if [[ ! -d "$d" ]]; then
    MISSING+=("$d")
    echo "  [MISSING] $d"
  else
    echo "  [PRESENT] $d"
  fi
done

if (( ${#MISSING[@]} > 0 )); then
  echo ""
  echo "[FATAL] 关键备份缺失 ${#MISSING[@]} 项，拒绝执行半还原。"
  echo "        请人工恢复或参见 ROLLBACK.md §失败兜底。"
  exit 2
fi

echo ""
echo -n "确认开始回滚？(输入 yes 继续): "
read -r ACK
if [[ "${ACK}" != "yes" ]]; then
  echo "已取消。"
  exit 0
fi

echo ""
echo "开始回滚……"

# ============================================================================
# 步骤 1：仓本身
# ============================================================================
phase_banner 1 "仓本身（~/githubProject/monster → cc-space）"

if [[ -d "${GH_PROJECT_DIR}/monster" ]]; then
  if rm -rf "${GH_PROJECT_DIR}/monster"; then
    log_ok "rm -rf ~/githubProject/monster"
  else
    log_warn "rm -rf ~/githubProject/monster 失败"
  fi
else
  log_skip "~/githubProject/monster 不存在（已还原或未改名）"
fi

# tar 还原 cc-space（幂等：cc-space 存在则跳过覆盖，避免吃掉新提交）
if [[ -d "${GH_PROJECT_DIR}/cc-space" ]]; then
  log_skip "~/githubProject/cc-space 已存在（幂等：不覆盖）"
else
  if tar xzf "${BACKUP_TARBALL_REPO}" -C "${GH_PROJECT_DIR}/" 2>/dev/null; then
    log_ok "tar xzf cc-space-backup → ~/githubProject/"
  else
    log_warn "tar 解包失败 ${BACKUP_TARBALL_REPO}"
  fi
fi

# ============================================================================
# 步骤 2：CC projects jsonl
# ============================================================================
phase_banner 2 "CC projects jsonl 目录"

# 删除 monster* 前缀目录
MONSTER_PROJ_DIRS=( "${HOME_DIR}"/.claude/projects/-Users-xuke-githubProject-monster* )
if [[ -d "${MONSTER_PROJ_DIRS[0]:-/nonexistent}" ]]; then
  if rm -rf "${HOME_DIR}"/.claude/projects/-Users-xuke-githubProject-monster*; then
    log_ok "rm -rf ~/.claude/projects/-Users-xuke-githubProject-monster*"
  else
    log_warn "删除 monster projects 目录失败"
  fi
else
  log_skip "无 monster projects 目录可删"
fi

# 还原 cc-space*（幂等检查）
CC_SPACE_PROJ_DIRS=( "${HOME_DIR}"/.claude/projects/-Users-xuke-githubProject-cc-space* )
if [[ -d "${CC_SPACE_PROJ_DIRS[0]:-/nonexistent}" ]]; then
  log_skip "cc-space projects 目录已存在（幂等：不覆盖）"
else
  if tar xzf "${BACKUP_TARBALL_PROJECTS}" -C "${HOME_DIR}/.claude/projects/" 2>/dev/null; then
    log_ok "tar xzf cc-projects-backup → ~/.claude/projects/"
  else
    log_warn "tar 解包失败 ${BACKUP_TARBALL_PROJECTS}"
  fi
fi

# ============================================================================
# 步骤 3：CC CLI cache
# ============================================================================
phase_banner 3 "CC CLI cache (~/Library/Caches/claude-cli-nodejs/)"

CC_CACHE_DIR="${HOME_DIR}/Library/Caches/claude-cli-nodejs"
MONSTER_CACHE_DIRS=( "${CC_CACHE_DIR}"/-Users-xuke-githubProject-monster* )
if [[ -d "${MONSTER_CACHE_DIRS[0]:-/nonexistent}" ]]; then
  if rm -rf "${CC_CACHE_DIR}"/-Users-xuke-githubProject-monster*; then
    log_ok "rm -rf claude-cli-nodejs/...-monster*"
  else
    log_warn "删除 monster cli cache 失败"
  fi
else
  log_skip "无 monster cli cache 可删"
fi

CC_SPACE_CACHE_DIRS=( "${CC_CACHE_DIR}"/-Users-xuke-githubProject-cc-space* )
if [[ -d "${CC_SPACE_CACHE_DIRS[0]:-/nonexistent}" ]]; then
  log_skip "cc-space cli cache 已存在（幂等：不覆盖）"
else
  if tar xzf "${BACKUP_TARBALL_CLI_CACHE}" -C "${CC_CACHE_DIR}/" 2>/dev/null; then
    log_ok "tar xzf cc-cli-cache-backup → ${CC_CACHE_DIR}/"
  else
    log_warn "tar 解包失败 ${BACKUP_TARBALL_CLI_CACHE}"
  fi
fi

# ============================================================================
# 步骤 4：scheduled-tasks
# ============================================================================
phase_banner 4 "~/.claude/scheduled-tasks 还原"

SCHEDULED_DIR="${HOME_DIR}/.claude/scheduled-tasks"
if [[ -d "${SCHEDULED_DIR}" ]]; then
  if rm -rf "${SCHEDULED_DIR}"; then
    log_ok "rm -rf ${SCHEDULED_DIR}"
  else
    log_warn "rm -rf ${SCHEDULED_DIR} 失败"
  fi
else
  log_skip "${SCHEDULED_DIR} 不存在"
fi

if cp -r "${BACKUP_DIR_SCHEDULED}" "${SCHEDULED_DIR}" 2>/dev/null; then
  log_ok "cp -r 备份 → ${SCHEDULED_DIR}"
else
  log_warn "cp 备份失败 ${BACKUP_DIR_SCHEDULED}"
fi

# ============================================================================
# 步骤 5：launchd com.monster.* → com.cc-space.*
# ============================================================================
phase_banner 5 "launchd monster 系列 → cc-space 系列（13 个）"

GUI_DOMAIN="gui/$(id -u)"

# bootout 全部 com.monster.* （从当前活跃列表抓）
MONSTER_LABELS=$(launchctl list 2>/dev/null | awk '$3 ~ /^com\.monster\./ {print $3}')
if [[ -n "${MONSTER_LABELS}" ]]; then
  while IFS= read -r label; do
    [[ -z "${label}" ]] && continue
    if launchctl bootout "${GUI_DOMAIN}/${label}" 2>/dev/null; then
      log_ok "bootout ${label}"
    else
      log_warn "bootout ${label} 失败（可能已 bootout）"
    fi
  done <<< "${MONSTER_LABELS}"
else
  log_skip "无 com.monster.* 活跃 label"
fi

# bootstrap 全部 com.cc-space.*（从 LAUNCHD_BAK_LIST 留档清单读）
if [[ -f "${LAUNCHD_BAK_LIST}" ]]; then
  while IFS= read -r plist_path; do
    [[ -z "${plist_path}" ]] && continue
    [[ "${plist_path}" =~ cc-connect ]] && continue  # 步骤 6 单独处理
    if [[ ! -f "${plist_path}" ]]; then
      log_warn "plist 不存在 ${plist_path}（已被步骤 1 tar 还原？检查路径）"
      continue
    fi
    label=$(basename "${plist_path}" .plist)
    # 幂等：已 load 则跳过
    if launchctl list 2>/dev/null | awk '{print $3}' | grep -qx "${label}"; then
      log_skip "bootstrap ${label}（已 load）"
      continue
    fi
    if launchctl bootstrap "${GUI_DOMAIN}" "${plist_path}" 2>/dev/null; then
      log_ok "bootstrap ${label}"
    else
      log_warn "bootstrap ${label} 失败 (${plist_path})"
    fi
  done < "${LAUNCHD_BAK_LIST}"
else
  log_warn "launchd 留档清单不存在 ${LAUNCHD_BAK_LIST}——cc-space 系列无法自动 bootstrap，需手工"
fi

# ============================================================================
# 步骤 6：cc-connect launchd
# ============================================================================
phase_banner 6 "cc-connect launchd 重启（config.toml 还原后）"

CC_CONNECT_PLIST="${HOME_DIR}/Library/LaunchAgents/com.cc-connect.plist"
CC_CONNECT_LABEL="com.cc-connect"

# bootout（可能已 bootout，无所谓）
if launchctl list 2>/dev/null | awk '{print $3}' | grep -qx "${CC_CONNECT_LABEL}"; then
  if launchctl bootout "${GUI_DOMAIN}/${CC_CONNECT_LABEL}" 2>/dev/null; then
    log_ok "bootout ${CC_CONNECT_LABEL}"
  else
    log_warn "bootout ${CC_CONNECT_LABEL} 失败"
  fi
else
  log_skip "${CC_CONNECT_LABEL} 当前未 load"
fi

# bootstrap（注意：config.toml 在步骤 7 还原；这里假设步骤 7 已跑或会跑——
# 在主流程顺序里 5/6 在 7 之前，这里 cc-connect 暂时用 monster work_dir bootstrap 也无害，
# 因为步骤 7 还原后下一次 KeepAlive 重启会读新 config。不过更严格的顺序应该是步骤 7 先做。
# 改为：step 6 只 bootout，bootstrap 移到 step 7 后做）—— 这里保持简单：
# 我们在所有步骤跑完后用一个尾部钩子重新 bootstrap cc-connect。
if [[ -f "${CC_CONNECT_PLIST}" ]]; then
  log_skip "cc-connect bootstrap 延迟到步骤 7（config.toml 还原）之后"
else
  log_warn "cc-connect plist 不存在 ${CC_CONNECT_PLIST}"
fi

# ============================================================================
# 步骤 7：小项备份还原
# ============================================================================
phase_banner 7 "小项 .bak-${STAMP} 还原"

for pair in "${SMALL_ITEMS[@]}"; do
  src="${pair%%|*}"
  dst="${pair##*|}"
  if [[ -f "${src}" ]]; then
    if cp "${src}" "${dst}" 2>/dev/null; then
      log_ok "cp ${src##*/} → ${dst}"
    else
      log_warn "cp 失败 ${src} → ${dst}"
    fi
  else
    log_skip "备份不存在 ${src}"
  fi
done

# 步骤 7 跑完后再 bootstrap cc-connect（config.toml 已还原）
if [[ -f "${CC_CONNECT_PLIST}" ]]; then
  if launchctl list 2>/dev/null | awk '{print $3}' | grep -qx "${CC_CONNECT_LABEL}"; then
    log_skip "bootstrap ${CC_CONNECT_LABEL}（已 load）"
  else
    if launchctl bootstrap "${GUI_DOMAIN}" "${CC_CONNECT_PLIST}" 2>/dev/null; then
      log_ok "bootstrap ${CC_CONNECT_LABEL}（config.toml 还原后）"
    else
      log_warn "bootstrap ${CC_CONNECT_LABEL} 失败"
    fi
  fi
fi

# ============================================================================
# 步骤 8：~/.agents
# ============================================================================
phase_banner 8 "~/.agents 还原"

if [[ -d "${HOME_DIR}/.agents" ]]; then
  if rm -rf "${HOME_DIR}/.agents"; then
    log_ok "rm -rf ~/.agents"
  else
    log_warn "rm -rf ~/.agents 失败"
  fi
else
  log_skip "~/.agents 不存在"
fi

if cp -r "${BACKUP_DIR_AGENTS}" "${HOME_DIR}/.agents" 2>/dev/null; then
  log_ok "cp -r ${BACKUP_DIR_AGENTS} → ~/.agents"
else
  log_warn "cp 失败 ${BACKUP_DIR_AGENTS}"
fi

# ============================================================================
# 步骤 9：gg 自身 git reset
# ============================================================================
phase_banner 9 "gg 自身 git reset --hard ${BASELINE_TAG}"

GG_DIR="${GH_PROJECT_DIR}/gg"
if [[ -d "${GG_DIR}/.git" ]]; then
  if git -C "${GG_DIR}" rev-parse --verify "${BASELINE_TAG}" >/dev/null 2>&1; then
    if git -C "${GG_DIR}" reset --hard "${BASELINE_TAG}" 2>/dev/null; then
      log_ok "git -C gg reset --hard ${BASELINE_TAG}"
    else
      log_warn "git reset 失败 (gg)"
    fi
  else
    log_warn "gg 无 tag ${BASELINE_TAG}（改名脚本未跑或未打 tag）"
  fi
else
  log_warn "${GG_DIR} 不是 git 仓库"
fi

# ============================================================================
# 步骤 10：跨仓 git reset
# ============================================================================
phase_banner 10 "跨仓 git reset --hard ${BASELINE_TAG}"

for repo in "${CROSS_REPOS[@]}"; do
  # gg 已在步骤 9 处理，跳过
  [[ "${repo}" == "${GG_DIR}" ]] && continue
  if [[ ! -d "${repo}/.git" ]]; then
    log_skip "${repo} 不是 git 仓库（或不存在）"
    continue
  fi
  if git -C "${repo}" rev-parse --verify "${BASELINE_TAG}" >/dev/null 2>&1; then
    if git -C "${repo}" reset --hard "${BASELINE_TAG}" 2>/dev/null; then
      log_ok "git -C $(basename "${repo}") reset --hard ${BASELINE_TAG}"
    else
      log_warn "git reset 失败 ($(basename "${repo}"))"
    fi
  else
    log_skip "$(basename "${repo}") 无 tag ${BASELINE_TAG}"
  fi
done

# ============================================================================
# 步骤 11：GitHub rename — 仅提示
# ============================================================================
phase_banner 11 "GitHub rename 检测 + 提示（不自动执行）"

if [[ -d "${GH_PROJECT_DIR}/cc-space/.git" ]]; then
  REMOTE_URL=$(git -C "${GH_PROJECT_DIR}/cc-space" remote get-url origin 2>/dev/null || echo "")
  if [[ "${REMOTE_URL}" =~ keithMonster/monster ]]; then
    cat <<'NOTICE' >&2

  ┌──────────────────────────────────────────────────────────────────────┐
  │ [MANUAL] GitHub repo 当前名称仍是 keithMonster/monster                │
  │   gh repo rename 是 GitHub 端不可逆动作，rollback.sh 不自动执行。     │
  │   如需还原 GitHub 端仓名，请手工跑：                                  │
  │                                                                      │
  │     gh repo rename cc-space --repo keithMonster/monster              │
  │     cd ~/githubProject/cc-space                                      │
  │     git remote set-url origin git@github.com:keithMonster/cc-space.git│
  │     git fetch && git remote -v                                       │
  └──────────────────────────────────────────────────────────────────────┘

NOTICE
    REPORT_LINES+=("[MANUAL] GitHub rename 需手工 gh repo rename cc-space --repo keithMonster/monster")
    STEP_WARN=$((STEP_WARN+1))
  elif [[ "${REMOTE_URL}" =~ keithMonster/cc-space ]]; then
    log_ok "GitHub remote 已是 keithMonster/cc-space（无需手工动作）"
  else
    log_skip "GitHub remote 形态未知：${REMOTE_URL}"
  fi
else
  log_skip "~/githubProject/cc-space/.git 不存在（仓未还原？）"
fi

# ============================================================================
# 后置：essence.md 完整性检测（改名脚本不该动 essence.md）
# ============================================================================
phase_banner "X" "essence.md 完整性自检（informational）"

ESSENCE="${GG_DIR}/memory/essence.md"
if [[ -f "${ESSENCE}" ]]; then
  if grep -q "monster" "${ESSENCE}" 2>/dev/null; then
    log_warn "essence.md 含 'monster' 字面——这是改名脚本 bug。rollback 不自动修。请人工检查"
  else
    log_ok "essence.md 无 monster 字面（健康）"
  fi
else
  log_skip "essence.md 不存在"
fi

# ============================================================================
# 总报告
# ============================================================================

echo ""
echo "================================================================================"
echo "  回滚报告"
echo "================================================================================"
echo "  OK   : ${STEP_OK}"
echo "  SKIP : ${STEP_SKIP}"
echo "  WARN : ${STEP_WARN}"
echo ""
echo "  逐步明细："
for line in "${REPORT_LINES[@]}"; do
  echo "    ${line}"
done
echo ""

if (( STEP_WARN > 0 )); then
  echo "  退出码: 1（部分失败——见 [WARN] 行，参照 ROLLBACK.md §失败兜底）"
  exit 1
else
  echo "  退出码: 0（完全 OK）"
  exit 0
fi
