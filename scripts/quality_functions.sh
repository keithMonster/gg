#!/bin/bash

# 质量保证函数库
# Author: gg (v9.3.5 evolution)
# Created: 2024-12-20

# 获取项目根目录
if [[ -n "${BASH_SOURCE[0]}" ]]; then
    QA_PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
else
    QA_PROJECT_ROOT="$(pwd)"
fi
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
    local check_status="$2"
    local score="$3"
    local execution_time="$4"
    
    local metrics_file="$QA_DIR/metrics/quality_metrics.json"
    local temp_file="$QA_DIR/metrics/quality_metrics.tmp"
    
    # 使用jq更新指标（如果可用）
    if command -v jq >/dev/null 2>&1; then
        jq --arg checker "$checker_name" \
           --arg status "$check_status" \
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
    
    local check_status="PASS"
    if [[ $errors -gt 0 ]]; then
        check_status="FAIL"
    fi
    
    update_quality_metrics "fileIntegrity" "$check_status" "$pass_rate" "$execution_time"
    log_qa "INFO" "文件完整性检查完成: $check_status (通过率: ${pass_rate}%)"
    
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
    
    local check_status="PASS"
    if [[ $errors -gt 0 ]]; then
        check_status="FAIL"
    fi
    
    update_quality_metrics "stateConsistency" "$check_status" "$pass_rate" "$execution_time"
    log_qa "INFO" "状态一致性检查完成: $check_status (通过率: ${pass_rate}%)"
    
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
    
    local check_status="PASS"
    if [[ $warnings -gt 0 ]]; then
        check_status="WARN"
    fi
    
    update_quality_metrics "performanceThreshold" "$check_status" "$pass_rate" "$execution_time"
    log_qa "INFO" "性能阈值检查完成: $check_status (通过率: ${pass_rate}%)"
    
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
