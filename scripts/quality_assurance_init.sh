#!/bin/bash

# 自动化质量保证系统初始化脚本
# Author: gg (v9.3.5 evolution)
# Created: 2024-12-20

set -euo pipefail

# 颜色定义
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# 日志函数
log_info() {
    echo -e "${BLUE}[INFO]${NC} $1"
}

log_success() {
    echo -e "${GREEN}[SUCCESS]${NC} $1"
}

log_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

log_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

# 获取项目根目录
PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
QA_DIR="$PROJECT_ROOT/quality"
SCRIPTS_DIR="$PROJECT_ROOT/scripts"
STATE_DIR="$PROJECT_ROOT/state"

log_info "初始化自动化质量保证系统..."
log_info "项目根目录: $PROJECT_ROOT"

# 创建质量保证目录结构
create_qa_directories() {
    log_info "创建质量保证目录结构..."
    
    local directories=(
        "$QA_DIR"
        "$QA_DIR/checkers"
        "$QA_DIR/reports"
        "$QA_DIR/backups"
        "$QA_DIR/logs"
        "$QA_DIR/config"
        "$QA_DIR/metrics"
        "$QA_DIR/recovery"
    )
    
    for dir in "${directories[@]}"; do
        if [[ ! -d "$dir" ]]; then
            mkdir -p "$dir"
            log_success "创建目录: $dir"
        else
            log_info "目录已存在: $dir"
        fi
    done
}

# 创建质量保证配置文件
create_qa_config() {
    log_info "创建质量保证配置文件..."
    
    local config_file="$QA_DIR/config/qa_config.json"
    
    cat > "$config_file" << 'EOF'
{
  "qualityAssurance": {
    "version": "1.0.0",
    "lastUpdated": "2024-12-20T15:30:00Z",
    "globalSettings": {
      "enableAutoRecovery": true,
      "maxRecoveryAttempts": 3,
      "checkInterval": 300,
      "reportingLevel": "WARN",
      "enableRealTimeMonitoring": true,
      "qualityThreshold": 85
    },
    "checkers": {
      "fileIntegrity": {
        "enabled": true,
        "priority": "high",
        "schedule": "*/5 * * * *",
        "timeout": 30,
        "config": {
          "jsonValidation": true,
          "permissionCheck": true,
          "sizeThreshold": 10485760,
          "checksumValidation": false
        }
      },
      "configConsistency": {
        "enabled": true,
        "priority": "high",
        "schedule": "*/10 * * * *",
        "timeout": 60,
        "config": {
          "versionCompatibility": true,
          "parameterValidation": true,
          "dependencyCheck": true
        }
      },
      "stateConsistency": {
        "enabled": true,
        "priority": "critical",
        "schedule": "*/1 * * * *",
        "timeout": 45,
        "config": {
          "timestampTolerance": 60,
          "dataIntegrityCheck": true,
          "crossReferenceValidation": true
        }
      },
      "performanceThreshold": {
        "enabled": true,
        "priority": "medium",
        "schedule": "*/2 * * * *",
        "timeout": 30,
        "config": {
          "responseTimeThreshold": 5.0,
          "memoryUsageThreshold": 80,
          "diskUsageThreshold": 85,
          "cpuUsageThreshold": 90
        }
      },
      "securityCompliance": {
        "enabled": true,
        "priority": "critical",
        "schedule": "0 */6 * * *",
        "timeout": 120,
        "config": {
          "permissionAudit": true,
          "sensitiveDataCheck": true,
          "accessControlValidation": true
        }
      }
    },
    "recovery": {
      "strategies": {
        "INFO": "log_only",
        "WARN": "notify",
        "ERROR": "auto_fix",
        "CRITICAL": "rollback"
      },
      "checkpointRetention": 7,
      "backupLocation": "quality/backups",
      "maxRollbackDepth": 5,
      "recoveryTimeout": 300
    },
    "monitoring": {
      "metricsRetention": 30,
      "reportGeneration": true,
      "alerting": {
        "enabled": true,
        "channels": ["log", "file"]
      },
      "alertThresholds": {
        "qualityScore": 85,
        "errorRate": 0.1,
        "responseTime": 5.0,
        "recoveryTime": 60
      },
      "dashboardRefreshInterval": 30
    }
  }
}
EOF
    
    log_success "创建配置文件: $config_file"
}

# 创建质量指标初始文件
create_quality_metrics() {
    log_info "创建质量指标文件..."
    
    local metrics_file="$QA_DIR/metrics/quality_metrics.json"
    
    cat > "$metrics_file" << 'EOF'
{
  "qualityMetrics": {
    "timestamp": "2024-12-20T15:30:00Z",
    "systemHealth": "HEALTHY",
    "overallQualityScore": 100.0,
    "metrics": {
      "checkPassRate": 100.0,
      "errorRecoveryRate": 0.0,
      "systemAvailability": 100.0,
      "avgResponseTime": 0.0,
      "avgRecoveryTime": 0.0
    },
    "checkerResults": {
      "fileIntegrity": {
        "lastRun": "2024-12-20T15:30:00Z",
        "status": "PASS",
        "score": 100.0,
        "executionTime": 0.0
      },
      "configConsistency": {
        "lastRun": "2024-12-20T15:30:00Z",
        "status": "PASS",
        "score": 100.0,
        "executionTime": 0.0
      },
      "stateConsistency": {
        "lastRun": "2024-12-20T15:30:00Z",
        "status": "PASS",
        "score": 100.0,
        "executionTime": 0.0
      },
      "performanceThreshold": {
        "lastRun": "2024-12-20T15:30:00Z",
        "status": "PASS",
        "score": 100.0,
        "executionTime": 0.0
      },
      "securityCompliance": {
        "lastRun": "2024-12-20T15:30:00Z",
        "status": "PASS",
        "score": 100.0,
        "executionTime": 0.0
      }
    },
    "trends": {
      "qualityTrend": "stable",
      "errorTrend": "decreasing",
      "performanceTrend": "stable"
    },
    "alerts": [],
    "recommendations": []
  }
}
EOF
    
    log_success "创建指标文件: $metrics_file"
}

# 创建质量检查日志文件
create_qa_logs() {
    log_info "创建质量检查日志文件..."
    
    local log_file="$QA_DIR/logs/qa_system.log"
    
    cat > "$log_file" << EOF
[$(date '+%Y-%m-%d %H:%M:%S')] [INFO] 质量保证系统初始化完成
[$(date '+%Y-%m-%d %H:%M:%S')] [INFO] 系统版本: 1.0.0
[$(date '+%Y-%m-%d %H:%M:%S')] [INFO] 配置加载成功
[$(date '+%Y-%m-%d %H:%M:%S')] [INFO] 所有检查器已注册
EOF
    
    log_success "创建日志文件: $log_file"
}

# 创建质量保证函数库
create_qa_functions() {
    log_info "创建质量保证函数库..."
    
    local functions_file="$SCRIPTS_DIR/quality_functions.sh"
    
    cat > "$functions_file" << 'EOF'
#!/bin/bash

# 质量保证函数库
# Author: gg (v9.3.5 evolution)
# Created: 2024-12-20

# 获取项目根目录
QA_PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
QA_DIR="$QA_PROJECT_ROOT/quality"
STATE_DIR="$QA_PROJECT_ROOT/state"

# 加载配置
load_qa_config() {
    local config_file="$QA_DIR/config/qa_config.json"
    if [[ -f "$config_file" ]]; then
        QA_CONFIG=$(cat "$config_file")
        return 0
    else
        echo "错误: 质量保证配置文件不存在: $config_file"
        return 1
    fi
}

# 记录质量检查日志
log_qa() {
    local level="$1"
    local message="$2"
    local log_file="$QA_DIR/logs/qa_system.log"
    
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] [$level] $message" >> "$log_file"
}

# 更新质量指标
update_quality_metrics() {
    local checker_name="$1"
    local status="$2"
    local score="$3"
    local execution_time="$4"
    
    local metrics_file="$QA_DIR/metrics/quality_metrics.json"
    local temp_file="$QA_DIR/metrics/quality_metrics.tmp"
    
    # 使用jq更新指标（如果可用）
    if command -v jq >/dev/null 2>&1; then
        jq --arg checker "$checker_name" \
           --arg status "$status" \
           --arg score "$score" \
           --arg time "$execution_time" \
           --arg timestamp "$(date -u '+%Y-%m-%dT%H:%M:%SZ')" \
           '.qualityMetrics.checkerResults[$checker] = {
               "lastRun": $timestamp,
               "status": $status,
               "score": ($score | tonumber),
               "executionTime": ($time | tonumber)
           } | .qualityMetrics.timestamp = $timestamp' \
           "$metrics_file" > "$temp_file" && mv "$temp_file" "$metrics_file"
    else
        log_qa "WARN" "jq不可用，跳过指标更新"
    fi
}

# 文件完整性检查器
check_file_integrity() {
    local target_dir="${1:-$QA_PROJECT_ROOT}"
    local start_time=$(date +%s.%N)
    local errors=0
    local total_checks=0
    
    log_qa "INFO" "开始文件完整性检查: $target_dir"
    
    # 检查JSON文件格式
    while IFS= read -r -d '' json_file; do
        ((total_checks++))
        if ! python3 -m json.tool "$json_file" >/dev/null 2>&1; then
            log_qa "ERROR" "JSON格式错误: $json_file"
            ((errors++))
        fi
    done < <(find "$target_dir" -name "*.json" -type f -print0 2>/dev/null)
    
    # 检查关键文件权限
    local critical_files=(
        "$QA_PROJECT_ROOT/prompts/system_prompt.md"
        "$QA_DIR/config/qa_config.json"
        "$STATE_DIR/system_state.json"
    )
    
    for file in "${critical_files[@]}"; do
        if [[ -f "$file" ]]; then
            ((total_checks++))
            if [[ ! -r "$file" ]]; then
                log_qa "ERROR" "文件不可读: $file"
                ((errors++))
            fi
        fi
    done
    
    local end_time=$(date +%s.%N)
    local execution_time=$(echo "$end_time - $start_time" | bc -l 2>/dev/null || echo "0")
    
    local pass_rate=100
    if [[ $total_checks -gt 0 ]]; then
        pass_rate=$(echo "scale=2; ($total_checks - $errors) * 100 / $total_checks" | bc -l 2>/dev/null || echo "100")
    fi
    
    local status="PASS"
    if [[ $errors -gt 0 ]]; then
        status="FAIL"
    fi
    
    update_quality_metrics "fileIntegrity" "$status" "$pass_rate" "$execution_time"
    log_qa "INFO" "文件完整性检查完成: $status (通过率: ${pass_rate}%)"
    
    return $errors
}

# 状态一致性检查器
check_state_consistency() {
    local start_time=$(date +%s.%N)
    local errors=0
    local total_checks=0
    
    log_qa "INFO" "开始状态一致性检查"
    
    # 检查状态文件存在性
    local state_files=(
        "$STATE_DIR/system_state.json"
        "$STATE_DIR/performance.json"
        "$STATE_DIR/health_check.json"
    )
    
    for file in "${state_files[@]}"; do
        ((total_checks++))
        if [[ ! -f "$file" ]]; then
            log_qa "ERROR" "状态文件缺失: $file"
            ((errors++))
        fi
    done
    
    # 检查时间戳合理性
    if [[ -f "$STATE_DIR/system_state.json" ]] && command -v jq >/dev/null 2>&1; then
        ((total_checks++))
        local last_update=$(jq -r '.lastUpdate // empty' "$STATE_DIR/system_state.json" 2>/dev/null)
        if [[ -n "$last_update" ]]; then
            local current_time=$(date +%s)
            local update_time=$(date -d "$last_update" +%s 2>/dev/null || echo "0")
            local time_diff=$((current_time - update_time))
            
            # 如果时间戳超过1小时，认为异常
            if [[ $time_diff -gt 3600 ]]; then
                log_qa "WARN" "状态文件时间戳过旧: $last_update"
            fi
        fi
    fi
    
    local end_time=$(date +%s.%N)
    local execution_time=$(echo "$end_time - $start_time" | bc -l 2>/dev/null || echo "0")
    
    local pass_rate=100
    if [[ $total_checks -gt 0 ]]; then
        pass_rate=$(echo "scale=2; ($total_checks - $errors) * 100 / $total_checks" | bc -l 2>/dev/null || echo "100")
    fi
    
    local status="PASS"
    if [[ $errors -gt 0 ]]; then
        status="FAIL"
    fi
    
    update_quality_metrics "stateConsistency" "$status" "$pass_rate" "$execution_time"
    log_qa "INFO" "状态一致性检查完成: $status (通过率: ${pass_rate}%)"
    
    return $errors
}

# 性能阈值检查器
check_performance_thresholds() {
    local start_time=$(date +%s.%N)
    local warnings=0
    local total_checks=0
    
    log_qa "INFO" "开始性能阈值检查"
    
    # 检查磁盘使用率
    ((total_checks++))
    local disk_usage=$(df "$QA_PROJECT_ROOT" | awk 'NR==2 {print $5}' | sed 's/%//')
    if [[ $disk_usage -gt 85 ]]; then
        log_qa "WARN" "磁盘使用率过高: ${disk_usage}%"
        ((warnings++))
    fi
    
    # 检查文件数量（避免过多小文件）
    ((total_checks++))
    local file_count=$(find "$QA_PROJECT_ROOT" -type f | wc -l)
    if [[ $file_count -gt 10000 ]]; then
        log_qa "WARN" "项目文件数量过多: $file_count"
        ((warnings++))
    fi
    
    local end_time=$(date +%s.%N)
    local execution_time=$(echo "$end_time - $start_time" | bc -l 2>/dev/null || echo "0")
    
    local pass_rate=100
    if [[ $total_checks -gt 0 ]]; then
        pass_rate=$(echo "scale=2; ($total_checks - $warnings) * 100 / $total_checks" | bc -l 2>/dev/null || echo "100")
    fi
    
    local status="PASS"
    if [[ $warnings -gt 0 ]]; then
        status="WARN"
    fi
    
    update_quality_metrics "performanceThreshold" "$status" "$pass_rate" "$execution_time"
    log_qa "INFO" "性能阈值检查完成: $status (通过率: ${pass_rate}%)"
    
    return $warnings
}

# 运行所有质量检查
run_full_quality_check() {
    log_qa "INFO" "开始全面质量检查"
    
    local total_errors=0
    
    # 加载配置
    if ! load_qa_config; then
        return 1
    fi
    
    # 运行各项检查
    check_file_integrity
    total_errors=$((total_errors + $?))
    
    check_state_consistency
    total_errors=$((total_errors + $?))
    
    check_performance_thresholds
    total_errors=$((total_errors + $?))
    
    # 计算总体质量分数
    local overall_score=100
    if [[ $total_errors -gt 0 ]]; then
        overall_score=$((100 - total_errors * 10))
        if [[ $overall_score -lt 0 ]]; then
            overall_score=0
        fi
    fi
    
    log_qa "INFO" "全面质量检查完成，总体分数: $overall_score"
    
    return $total_errors
}

# 显示质量仪表板
show_quality_dashboard() {
    local metrics_file="$QA_DIR/metrics/quality_metrics.json"
    
    if [[ ! -f "$metrics_file" ]]; then
        echo "质量指标文件不存在"
        return 1
    fi
    
    echo "=== 质量保证仪表板 ==="
    echo "时间: $(date '+%Y-%m-%d %H:%M:%S')"
    echo ""
    
    if command -v jq >/dev/null 2>&1; then
        echo "系统健康状态: $(jq -r '.qualityMetrics.systemHealth' "$metrics_file")"
        echo "总体质量分数: $(jq -r '.qualityMetrics.overallQualityScore' "$metrics_file")"
        echo ""
        echo "检查器状态:"
        jq -r '.qualityMetrics.checkerResults | to_entries[] | "  \(.key): \(.value.status) (分数: \(.value.score))"' "$metrics_file"
    else
        echo "需要安装jq来显示详细信息"
        cat "$metrics_file"
    fi
}

# 运行特定检查器
run_specific_checker() {
    local checker_name="$1"
    
    case "$checker_name" in
        "file_integrity")
            check_file_integrity
            ;;
        "state_consistency")
            check_state_consistency
            ;;
        "performance_threshold")
            check_performance_thresholds
            ;;
        *)
            echo "未知的检查器: $checker_name"
            echo "可用检查器: file_integrity, state_consistency, performance_threshold"
            return 1
            ;;
    esac
}
EOF
    
    chmod +x "$functions_file"
    log_success "创建函数库: $functions_file"
}

# 主初始化流程
main() {
    log_info "=== 自动化质量保证系统初始化 ==="
    
    # 创建目录结构
    create_qa_directories
    
    # 创建配置文件
    create_qa_config
    
    # 创建指标文件
    create_quality_metrics
    
    # 创建日志文件
    create_qa_logs
    
    # 创建函数库
    create_qa_functions
    
    log_success "质量保证系统初始化完成！"
    log_info "使用方法:"
    log_info "  1. 加载函数库: source ./scripts/quality_functions.sh"
    log_info "  2. 运行全面检查: run_full_quality_check"
    log_info "  3. 查看仪表板: show_quality_dashboard"
    log_info "  4. 运行特定检查: run_specific_checker <checker_name>"
}

# 执行主函数
main "$@"