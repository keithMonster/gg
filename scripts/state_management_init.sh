#!/bin/bash

# 状态管理系统初始化脚本
# 创建必要的状态文件和目录结构

set -e

# 项目根目录
PROJECT_ROOT="/Users/xuke/OtherProject/_self/gg"
STATE_DIR="$PROJECT_ROOT/state"

# 颜色输出
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo -e "${GREEN}=== 状态管理系统初始化 ===${NC}"

# 检查jq是否安装
if ! command -v jq &> /dev/null; then
    echo -e "${RED}错误: jq 未安装，请先安装 jq${NC}"
    echo "安装命令: brew install jq"
    exit 1
fi

# 创建目录结构
echo "创建状态目录结构..."
mkdir -p "$STATE_DIR"/{tasks,system,sessions,checkpoints}
mkdir -p "$STATE_DIR/tasks"/{task_history,task_templates}
mkdir -p "$STATE_DIR/sessions/session_history"

# 创建初始系统状态文件
echo "初始化系统状态文件..."
cat > "$STATE_DIR/system/system_state.json" << 'EOF'
{
  "systemId": "gg_v9.3.4",
  "currentVersion": "9.3.4",
  "activeSkills": [
    "enhanced_state_management",
    "self_evolution",
    "time_management",
    "content_deduplication",
    "reference_formatting"
  ],
  "performanceMetrics": {
    "averageResponseTime": 0,
    "taskSuccessRate": 0,
    "errorRecoveryRate": 0
  },
  "lastHealthCheck": null,
  "systemHealth": "INITIALIZING",
  "createdAt": "TIMESTAMP_PLACEHOLDER",
  "updatedAt": "TIMESTAMP_PLACEHOLDER"
}
EOF

# 更新时间戳
current_time=$(date '+%Y-%m-%d %H:%M:%S')
jq --arg time "$current_time" \
   '.createdAt = $time | .updatedAt = $time | .lastHealthCheck = $time | .systemHealth = "HEALTHY"' \
   "$STATE_DIR/system/system_state.json" > "$STATE_DIR/system/system_state.json.tmp" && \
   mv "$STATE_DIR/system/system_state.json.tmp" "$STATE_DIR/system/system_state.json"

# 创建初始性能指标文件
echo "初始化性能指标文件..."
cat > "$STATE_DIR/system/performance.json" << EOF
{
  "totalTasks": 0,
  "successfulTasks": 0,
  "totalResponseTime": 0,
  "averageResponseTime": 0,
  "taskSuccessRate": 0,
  "errorRecoveryRate": 0,
  "lastUpdated": "$current_time",
  "createdAt": "$current_time"
}
EOF

# 创建健康检查文件
echo "初始化健康检查文件..."
cat > "$STATE_DIR/system/health_check.json" << EOF
{
  "timestamp": "$current_time",
  "overallHealth": "HEALTHY",
  "checks": {
    "stateIntegrity": "OK",
    "diskUsage": "OK",
    "diskUsagePercent": 0,
    "memoryUsage": "OK",
    "systemLoad": "OK"
  },
  "lastCheck": "$current_time"
}
EOF

# 创建任务模板
echo "创建任务模板..."
cat > "$STATE_DIR/tasks/task_templates/default_task.json" << 'EOF'
{
  "taskId": "TASK_ID_PLACEHOLDER",
  "executionState": "PLANNING",
  "currentPlan": [],
  "planProgress": 0,
  "taskContext": {
    "userRequest": "",
    "priority": "medium",
    "estimatedDuration": "",
    "intermediateResults": {},
    "errorHistory": []
  },
  "createdAt": "TIMESTAMP_PLACEHOLDER",
  "updatedAt": "TIMESTAMP_PLACEHOLDER",
  "completedAt": null
}
EOF

# 创建会话模板
echo "创建会话模板..."
cat > "$STATE_DIR/sessions/session_template.json" << 'EOF'
{
  "sessionId": "SESSION_ID_PLACEHOLDER",
  "userId": "user_001",
  "conversationHistory": [],
  "userPreferences": {
    "language": "zh-CN",
    "verbosity": "detailed",
    "outputFormat": "markdown"
  },
  "contextData": {},
  "createdAt": "TIMESTAMP_PLACEHOLDER",
  "updatedAt": "TIMESTAMP_PLACEHOLDER"
}
EOF

# 创建状态管理函数库
echo "创建状态管理函数库..."
cat > "$PROJECT_ROOT/scripts/state_functions.sh" << 'EOF'
#!/bin/bash

# 状态管理函数库
# 提供状态操作的核心函数

STATE_DIR="/Users/xuke/OtherProject/_self/gg/state"

# 任务状态管理函数
create_task_state() {
    local user_request="$1"
    local priority="${2:-medium}"
    local task_id="task_$(date +%Y%m%d_%H%M%S)"
    local state_file="$STATE_DIR/tasks/current_task.json"
    local timestamp=$(date '+%Y-%m-%d %H:%M:%S')
    
    # 如果存在当前任务，先归档
    if [[ -f "$state_file" ]]; then
        local old_task_id=$(jq -r '.taskId' "$state_file" 2>/dev/null || echo "unknown")
        mv "$state_file" "$STATE_DIR/tasks/task_history/${old_task_id}.json"
    fi
    
    # 创建新任务状态
    jq --arg task_id "$task_id" \
       --arg user_request "$user_request" \
       --arg priority "$priority" \
       --arg timestamp "$timestamp" \
       '.taskId = $task_id |
        .taskContext.userRequest = $user_request |
        .taskContext.priority = $priority |
        .createdAt = $timestamp |
        .updatedAt = $timestamp' \
       "$STATE_DIR/tasks/task_templates/default_task.json" > "$state_file"
    
    echo "$task_id"
}

update_task_state() {
    local field="$1"
    local value="$2"
    local state_file="$STATE_DIR/tasks/current_task.json"
    local timestamp=$(date '+%Y-%m-%d %H:%M:%S')
    
    if [[ ! -f "$state_file" ]]; then
        echo "错误: 当前任务状态文件不存在" >&2
        return 1
    fi
    
    jq --arg field "$field" --arg value "$value" --arg timestamp "$timestamp" \
       '.[$field] = $value | .updatedAt = $timestamp' \
       "$state_file" > "${state_file}.tmp" && mv "${state_file}.tmp" "$state_file"
}

add_plan_step() {
    local action="$1"
    local description="${2:-}"
    local state_file="$STATE_DIR/tasks/current_task.json"
    local timestamp=$(date '+%Y-%m-%d %H:%M:%S')
    
    if [[ ! -f "$state_file" ]]; then
        echo "错误: 当前任务状态文件不存在" >&2
        return 1
    fi
    
    jq --arg action "$action" --arg desc "$description" --arg timestamp "$timestamp" \
       '.currentPlan += [{
         "stepId": (.currentPlan | length + 1),
         "action": $action,
         "description": $desc,
         "status": "PENDING",
         "startTime": null,
         "endTime": null,
         "result": null
       }] | .updatedAt = $timestamp' \
       "$state_file" > "${state_file}.tmp" && mv "${state_file}.tmp" "$state_file"
}

start_current_step() {
    local state_file="$STATE_DIR/tasks/current_task.json"
    local timestamp=$(date '+%Y-%m-%d %H:%M:%S')
    
    if [[ ! -f "$state_file" ]]; then
        echo "错误: 当前任务状态文件不存在" >&2
        return 1
    fi
    
    jq --arg timestamp "$timestamp" \
       '.currentPlan[.planProgress].status = "IN_PROGRESS" |
        .currentPlan[.planProgress].startTime = $timestamp |
        .updatedAt = $timestamp' \
       "$state_file" > "${state_file}.tmp" && mv "${state_file}.tmp" "$state_file"
}

complete_current_step() {
    local result="$1"
    local state_file="$STATE_DIR/tasks/current_task.json"
    local timestamp=$(date '+%Y-%m-%d %H:%M:%S')
    
    if [[ ! -f "$state_file" ]]; then
        echo "错误: 当前任务状态文件不存在" >&2
        return 1
    fi
    
    jq --arg result "$result" --arg timestamp "$timestamp" \
       '.currentPlan[.planProgress].status = "COMPLETED" |
        .currentPlan[.planProgress].endTime = $timestamp |
        .currentPlan[.planProgress].result = $result |
        .planProgress += 1 |
        .updatedAt = $timestamp' \
       "$state_file" > "${state_file}.tmp" && mv "${state_file}.tmp" "$state_file"
}

# 状态查询函数
get_execution_state() {
    local state_file="$STATE_DIR/tasks/current_task.json"
    jq -r '.executionState // "IDLE"' "$state_file" 2>/dev/null
}

get_current_step() {
    local state_file="$STATE_DIR/tasks/current_task.json"
    jq -r '.currentPlan[.planProgress].action // "none"' "$state_file" 2>/dev/null
}

get_task_progress() {
    local state_file="$STATE_DIR/tasks/current_task.json"
    local progress=$(jq -r '.planProgress // 0' "$state_file" 2>/dev/null)
    local total=$(jq -r '.currentPlan | length' "$state_file" 2>/dev/null || echo "0")
    echo "$progress/$total"
}

get_task_id() {
    local state_file="$STATE_DIR/tasks/current_task.json"
    jq -r '.taskId // "none"' "$state_file" 2>/dev/null
}

# 健康检查函数
system_health_check() {
    local health_file="$STATE_DIR/system/health_check.json"
    local timestamp=$(date '+%Y-%m-%d %H:%M:%S')
    
    # 检查状态文件完整性
    local state_integrity="OK"
    if [[ ! -f "$STATE_DIR/tasks/current_task.json" ]] && [[ ! -f "$STATE_DIR/system/system_state.json" ]]; then
        state_integrity="ERROR"
    fi
    
    # 检查磁盘空间
    local disk_usage=$(df -h "$STATE_DIR" | awk 'NR==2 {print $5}' | sed 's/%//' || echo "0")
    local disk_status="OK"
    if [[ $disk_usage -gt 90 ]]; then
        disk_status="CRITICAL"
    elif [[ $disk_usage -gt 80 ]]; then
        disk_status="WARNING"
    fi
    
    # 检查内存使用
    local memory_usage=$(vm_stat | grep "Pages free" | awk '{print $3}' | sed 's/\.//' || echo "0")
    local memory_status="OK"
    
    # 检查系统负载
    local system_load=$(uptime | awk -F'load averages:' '{print $2}' | awk '{print $1}' | sed 's/,//' || echo "0")
    local load_status="OK"
    
    # 确定整体健康状态
    local overall_health="HEALTHY"
    if [[ "$state_integrity" == "ERROR" ]]; then
        overall_health="CRITICAL"
    elif [[ "$disk_status" == "CRITICAL" ]]; then
        overall_health="CRITICAL"
    elif [[ "$disk_status" == "WARNING" ]]; then
        overall_health="WARNING"
    fi
    
    # 生成健康报告
    jq --arg timestamp "$timestamp" \
       --arg overall "$overall_health" \
       --arg state_int "$state_integrity" \
       --arg disk_stat "$disk_status" \
       --arg disk_usage "$disk_usage" \
       --arg mem_stat "$memory_status" \
       --arg load_stat "$load_status" \
       '.timestamp = $timestamp |
        .overallHealth = $overall |
        .checks.stateIntegrity = $state_int |
        .checks.diskUsage = $disk_stat |
        .checks.diskUsagePercent = ($disk_usage | tonumber) |
        .checks.memoryUsage = $mem_stat |
        .checks.systemLoad = $load_stat |
        .lastCheck = $timestamp' \
       "$health_file" > "${health_file}.tmp" && mv "${health_file}.tmp" "$health_file"
    
    echo "健康检查完成: $overall_health"
}

# 性能指标更新
update_performance_metrics() {
    local response_time="$1"
    local success="$2"  # true/false
    local metrics_file="$STATE_DIR/system/performance.json"
    local timestamp=$(date '+%Y-%m-%d %H:%M:%S')
    
    if [[ ! -f "$metrics_file" ]]; then
        echo "错误: 性能指标文件不存在" >&2
        return 1
    fi
    
    jq --arg rt "$response_time" --arg success "$success" --arg timestamp "$timestamp" \
       '.totalTasks += 1 |
        .totalResponseTime += ($rt | tonumber) |
        .averageResponseTime = (.totalResponseTime / .totalTasks) |
        if $success == "true" then .successfulTasks += 1 else . end |
        .taskSuccessRate = (.successfulTasks / .totalTasks) |
        .lastUpdated = $timestamp' \
       "$metrics_file" > "${metrics_file}.tmp" && mv "${metrics_file}.tmp" "$metrics_file"
}

# 检查点管理
create_checkpoint() {
    local checkpoint_name="$1"
    local checkpoint_dir="$STATE_DIR/checkpoints"
    local timestamp=$(date +%Y%m%d_%H%M%S)
    
    mkdir -p "$checkpoint_dir"
    
    # 复制当前状态到检查点
    if [[ -f "$STATE_DIR/tasks/current_task.json" ]]; then
        cp "$STATE_DIR/tasks/current_task.json" \
           "$checkpoint_dir/${checkpoint_name}_${timestamp}.json"
        echo "检查点已创建: ${checkpoint_name}_${timestamp}"
        return 0
    else
        echo "警告: 当前任务状态文件不存在，无法创建检查点" >&2
        return 1
    fi
}

restore_from_checkpoint() {
    local checkpoint_file="$1"
    local current_state="$STATE_DIR/tasks/current_task.json"
    
    if [[ -f "$checkpoint_file" ]]; then
        cp "$checkpoint_file" "$current_state"
        echo "状态已从检查点恢复: $checkpoint_file"
        return 0
    else
        echo "错误: 检查点文件不存在: $checkpoint_file" >&2
        return 1
    fi
}

# 显示当前状态摘要
show_state_summary() {
    echo "=== 当前状态摘要 ==="
    
    # 任务状态
    local task_id=$(get_task_id)
    local exec_state=$(get_execution_state)
    local progress=$(get_task_progress)
    local current_step=$(get_current_step)
    
    echo "任务ID: $task_id"
    echo "执行状态: $exec_state"
    echo "进度: $progress"
    echo "当前步骤: $current_step"
    
    # 系统健康
    if [[ -f "$STATE_DIR/system/health_check.json" ]]; then
        local health=$(jq -r '.overallHealth' "$STATE_DIR/system/health_check.json" 2>/dev/null || echo "UNKNOWN")
        echo "系统健康: $health"
    fi
    
    # 性能指标
    if [[ -f "$STATE_DIR/system/performance.json" ]]; then
        local success_rate=$(jq -r '.taskSuccessRate' "$STATE_DIR/system/performance.json" 2>/dev/null || echo "0")
        local avg_time=$(jq -r '.averageResponseTime' "$STATE_DIR/system/performance.json" 2>/dev/null || echo "0")
        echo "任务成功率: $(printf "%.1f%%" $(echo "$success_rate * 100" | bc -l 2>/dev/null || echo "0"))"
        echo "平均响应时间: ${avg_time}秒"
    fi
}
EOF

# 设置脚本可执行权限
chmod +x "$PROJECT_ROOT/scripts/state_functions.sh"

# 执行初始健康检查
echo "执行初始健康检查..."
source "$PROJECT_ROOT/scripts/state_functions.sh"
system_health_check

echo -e "${GREEN}状态管理系统初始化完成！${NC}"
echo -e "${YELLOW}使用方法:${NC}"
echo "  source $PROJECT_ROOT/scripts/state_functions.sh"
echo "  show_state_summary"
echo ""
echo -e "${YELLOW}主要功能:${NC}"
echo "  - 任务状态管理: create_task_state, update_task_state"
echo "  - 执行步骤控制: add_plan_step, start_current_step, complete_current_step"
echo "  - 健康监控: system_health_check"
echo "  - 性能指标: update_performance_metrics"
echo "  - 检查点管理: create_checkpoint, restore_from_checkpoint"