#!/bin/bash
# Continuous Monitoring Script for Prompt System Quality
# 提示词系统持续监控脚本

set -e

# 配置
MONITOR_DIR="./prompts"
REPORT_DIR="./outputs/monitoring"
LOG_FILE="$REPORT_DIR/monitoring.log"
ALERT_THRESHOLD_ERRORS=5
ALERT_THRESHOLD_WARNINGS=10

# 颜色定义
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
PURPLE='\033[0;35m'
NC='\033[0m'

# 日志函数
log_info() {
    local msg="[$(date '+%Y-%m-%d %H:%M:%S')] [INFO] $1"
    echo -e "${BLUE}$msg${NC}"
    echo "$msg" >> "$LOG_FILE"
}

log_success() {
    local msg="[$(date '+%Y-%m-%d %H:%M:%S')] [SUCCESS] $1"
    echo -e "${GREEN}$msg${NC}"
    echo "$msg" >> "$LOG_FILE"
}

log_warning() {
    local msg="[$(date '+%Y-%m-%d %H:%M:%S')] [WARNING] $1"
    echo -e "${YELLOW}$msg${NC}"
    echo "$msg" >> "$LOG_FILE"
}

log_error() {
    local msg="[$(date '+%Y-%m-%d %H:%M:%S')] [ERROR] $1"
    echo -e "${RED}$msg${NC}"
    echo "$msg" >> "$LOG_FILE"
}

log_metric() {
    local msg="[$(date '+%Y-%m-%d %H:%M:%S')] [METRIC] $1"
    echo -e "${PURPLE}$msg${NC}"
    echo "$msg" >> "$LOG_FILE"
}

# 初始化
init_monitoring() {
    mkdir -p "$REPORT_DIR"
    
    if [ ! -f "$LOG_FILE" ]; then
        touch "$LOG_FILE"
        log_info "初始化监控日志文件"
    fi
    
    log_info "开始持续监控 - 监控目录: $MONITOR_DIR"
}

# 系统健康检查
health_check() {
    log_info "执行系统健康检查..."
    
    # 检查关键目录
    local critical_dirs=("prompts" "scripts" "outputs")
    for dir in "${critical_dirs[@]}"; do
        if [ ! -d "$dir" ]; then
            log_error "关键目录缺失: $dir"
            return 1
        fi
    done
    
    # 检查关键脚本
    local critical_scripts=("scripts/simple_audit.sh" "scripts/prompt_quality_audit.sh")
    for script in "${critical_scripts[@]}"; do
        if [ ! -x "$script" ]; then
            log_error "关键脚本不可执行: $script"
            return 1
        fi
    done
    
    log_success "系统健康检查通过"
    return 0
}

# 质量指标收集
collect_metrics() {
    # 确保关闭调试模式，避免意外输出
    set +x
    log_info "收集质量指标..."
    
    # 模块统计 - 增强错误处理
    local total_modules=0
    if [ -d "$MONITOR_DIR" ]; then
        total_modules=$(find "$MONITOR_DIR" -name "*.md" -type f 2>/dev/null | wc -l | tr -d ' ' || echo "0")
    fi
    # 确保是数字
    total_modules=${total_modules:-0}
    log_metric "总模块数: $total_modules"
    
    # 元数据完整性统计 - 改进逻辑
    local modules_with_metadata=0
    local modules_without_metadata=0
    
    if [ "$total_modules" -gt 0 ]; then
        while IFS= read -r file; do
            if [ -f "$file" ]; then
                # 安全地检查YAML前置内容
                local has_yaml=false
                if head -20 "$file" 2>/dev/null | grep -q '^---$'; then
                    # 检查YAML元数据字段，避免变量赋值输出
                    if awk '/^---$/{flag=!flag; if(!flag) exit} flag && !/^---$/' "$file" 2>/dev/null | \
                       grep -q '^version:' && \
                       awk '/^---$/{flag=!flag; if(!flag) exit} flag && !/^---$/' "$file" 2>/dev/null | \
                       grep -q '^author:' && \
                       awk '/^---$/{flag=!flag; if(!flag) exit} flag && !/^---$/' "$file" 2>/dev/null | \
                       grep -q '^description:'; then
                        modules_with_metadata=$((modules_with_metadata + 1))
                        has_yaml=true
                    fi
                fi
                
                if [ "$has_yaml" = false ]; then
                    modules_without_metadata=$((modules_without_metadata + 1))
                fi
            fi
        done < <(find "$MONITOR_DIR" -name "*.md" -type f 2>/dev/null || true)
    fi
    
    # 计算完整性百分比
    local metadata_completeness=0
    if [ "$total_modules" -gt 0 ]; then
        metadata_completeness=$((modules_with_metadata * 100 / total_modules))
    fi
    log_metric "元数据完整性: $metadata_completeness% ($modules_with_metadata/$total_modules)"
    
    # 文件大小统计 - 改进计算方式
    local total_size=0
    local avg_size=0
    if [ "$total_modules" -gt 0 ]; then
        # 使用更安全的方式计算总大小
        total_size=$(find "$MONITOR_DIR" -name "*.md" -type f -exec stat -f%z {} + 2>/dev/null | awk '{sum+=$1} END {print sum+0}' || echo "0")
        if [ "$total_size" -gt 0 ]; then
            avg_size=$((total_size / total_modules))
        fi
    fi
    log_metric "平均文件大小: $avg_size 字节"
    
    # 最近更新统计
    local recently_updated=0
    recently_updated=$(find "$MONITOR_DIR" -name "*.md" -type f -mtime -7 2>/dev/null | wc -l | tr -d ' ' || echo "0")
    recently_updated=${recently_updated:-0}
    log_metric "最近7天更新的模块: $recently_updated"
    
    # Git状态 - 增强错误处理
    local uncommitted_changes=0
    if git rev-parse --git-dir >/dev/null 2>&1; then
        uncommitted_changes=$(git status --porcelain 2>/dev/null | wc -l | tr -d ' ' || echo "0")
        uncommitted_changes=${uncommitted_changes:-0}
        local last_commit=$(git log -1 --format="%h %s" 2>/dev/null || echo "无提交记录")
        log_metric "未提交变更: $uncommitted_changes"
        log_metric "最后提交: $last_commit"
    fi
    
    # 返回关键指标用于告警判断（确保都是有效数字）
    modules_without_metadata=${modules_without_metadata:-0}
    metadata_completeness=${metadata_completeness:-0}
    uncommitted_changes=${uncommitted_changes:-0}
    
    echo "$modules_without_metadata $metadata_completeness $uncommitted_changes"
}

# 运行质量审查
run_quality_audit() {
    log_info "运行质量审查..."
    
    if [ -x "scripts/simple_audit.sh" ]; then
        local audit_output
        local audit_exit_code
        
        audit_output=$(./scripts/simple_audit.sh 2>&1 || true)
        audit_exit_code=$?
        
        if [ $audit_exit_code -eq 0 ]; then
            log_success "质量审查完成"
            
            # 提取并记录关键信息
            local module_count=$(echo "$audit_output" | grep -o '发现 [0-9]\+ 个模块' | grep -o '[0-9]\+' || echo "0")
            log_metric "审查发现模块数: $module_count"
            
            # 检查是否有新的审查报告
            local latest_report=$(ls -t outputs/simple_audit_*.md 2>/dev/null | head -1 || echo "")
            if [ -n "$latest_report" ]; then
                log_info "最新审查报告: $latest_report"
            fi
        else
            log_error "质量审查失败，退出代码: $audit_exit_code"
            return 1
        fi
    else
        log_warning "质量审查脚本不可用"
        return 1
    fi
}

# 告警检查
check_alerts() {
    local metrics_result="$1"
    
    # 安全地解析指标结果
    local modules_without_metadata=$(echo "$metrics_result" | cut -d' ' -f1 2>/dev/null || echo "0")
    local metadata_completeness=$(echo "$metrics_result" | cut -d' ' -f2 2>/dev/null || echo "0")
    local uncommitted_changes=$(echo "$metrics_result" | cut -d' ' -f3 2>/dev/null || echo "0")
    
    # 确保所有变量都是有效数字
    modules_without_metadata=${modules_without_metadata:-0}
    metadata_completeness=${metadata_completeness:-0}
    uncommitted_changes=${uncommitted_changes:-0}
    
    # 验证数字格式
    if ! [[ "$modules_without_metadata" =~ ^[0-9]+$ ]]; then
        modules_without_metadata=0
    fi
    if ! [[ "$metadata_completeness" =~ ^[0-9]+$ ]]; then
        metadata_completeness=0
    fi
    if ! [[ "$uncommitted_changes" =~ ^[0-9]+$ ]]; then
        uncommitted_changes=0
    fi
    
    log_info "检查告警条件..."
    log_info "指标值: 缺失元数据=$modules_without_metadata, 完整性=$metadata_completeness%, 未提交=$uncommitted_changes"
    
    # 元数据完整性告警 - 增强数值验证
    if [ "$modules_without_metadata" -gt "$ALERT_THRESHOLD_ERRORS" ] 2>/dev/null; then
        log_error "告警: 缺少元数据的模块过多 ($modules_without_metadata > $ALERT_THRESHOLD_ERRORS)"
    elif [ "$modules_without_metadata" -gt "$ALERT_THRESHOLD_WARNINGS" ] 2>/dev/null; then
        log_warning "警告: 缺少元数据的模块较多 ($modules_without_metadata > $ALERT_THRESHOLD_WARNINGS)"
    fi
    
    # 元数据完整性百分比告警 - 增强数值验证
    if [ "$metadata_completeness" -lt 80 ] 2>/dev/null; then
        log_error "告警: 元数据完整性过低 ($metadata_completeness% < 80%)"
    elif [ "$metadata_completeness" -lt 90 ] 2>/dev/null; then
        log_warning "警告: 元数据完整性偏低 ($metadata_completeness% < 90%)"
    fi
    
    # 未提交变更告警 - 增强数值验证
    if [ "$uncommitted_changes" -gt 20 ] 2>/dev/null; then
        log_warning "警告: 未提交变更较多 ($uncommitted_changes > 20)"
    fi
    
    log_info "告警检查完成"
}

# 生成监控报告
generate_report() {
    local report_file="$REPORT_DIR/monitoring_report_$(date +%Y%m%d_%H%M%S).md"
    
    log_info "生成监控报告: $report_file"
    
    # 重新收集指标用于报告生成
    local metrics_output
    metrics_output=$(collect_metrics 2>/dev/null | grep "\[METRIC\]" | sed 's/.*\[METRIC\] /- /' || echo "- 指标收集失败")
    
    cat > "$report_file" << EOF
# 提示词系统监控报告

**生成时间**: $(date '+%Y-%m-%d %H:%M:%S')
**监控周期**: 持续监控
**系统状态**: $(if health_check >/dev/null 2>&1; then echo "健康"; else echo "异常"; fi)

## 系统概览

$metrics_output

## 最近活动

### Git状态
\`\`\`
$(git status --short 2>/dev/null || echo "Git状态不可用")
\`\`\`

### 最近提交
\`\`\`
$(git log --oneline -5 2>/dev/null || echo "提交历史不可用")
\`\`\`

## 质量趋势

[此处可添加历史趋势分析]

## 建议行动

- 定期运行完整质量审查
- 修复发现的元数据问题
- 保持文档标准的一致性
- 及时提交重要变更

---
*报告由持续监控系统自动生成*
EOF

    log_success "监控报告已生成"
}

# 清理旧报告
cleanup_old_reports() {
    log_info "清理旧监控报告..."
    
    # 保留最近30天的报告
    find "$REPORT_DIR" -name "monitoring_report_*.md" -mtime +30 -delete 2>/dev/null || true
    
    # 保留最近1000行日志
    if [ -f "$LOG_FILE" ] && [ $(wc -l < "$LOG_FILE") -gt 1000 ]; then
        tail -1000 "$LOG_FILE" > "$LOG_FILE.tmp"
        mv "$LOG_FILE.tmp" "$LOG_FILE"
        log_info "日志文件已轮转"
    fi
}

# 主函数
main() {
    local mode="${1:-single}"
    
    init_monitoring
    
    case "$mode" in
        "single")
            log_info "执行单次监控检查"
            if health_check; then
                local metrics_result
                metrics_result=$(collect_metrics 2>&1 | tail -1)
                check_alerts "$metrics_result"
                run_quality_audit
                generate_report
                cleanup_old_reports
                log_success "单次监控检查完成"
            else
                log_error "系统健康检查失败，终止监控"
                exit 1
            fi
            ;;
        "continuous")
            log_info "启动持续监控模式 (每30分钟检查一次)"
            while true; do
                if health_check; then
                    local metrics_result
                    metrics_result=$(collect_metrics 2>&1 | tail -1)
                    check_alerts "$metrics_result"
                    
                    # 每2小时运行一次完整审查
                    local hour=$(date +%H)
                    if [ $((hour % 2)) -eq 0 ] && [ $(date +%M) -lt 5 ]; then
                        run_quality_audit
                        generate_report
                    fi
                    
                    cleanup_old_reports
                else
                    log_error "系统健康检查失败"
                fi
                
                log_info "等待30分钟后进行下次检查..."
                sleep 1800  # 30分钟
            done
            ;;
        "help")
            echo "用法: $0 [single|continuous|help]"
            echo "  single     - 执行单次监控检查 (默认)"
            echo "  continuous - 启动持续监控模式"
            echo "  help       - 显示此帮助信息"
            ;;
        *)
            log_error "未知模式: $mode"
            echo "使用 '$0 help' 查看可用选项"
            exit 1
            ;;
    esac
}

# 信号处理
trap 'log_info "收到终止信号，正在退出..."; exit 0' SIGTERM SIGINT

# 执行主函数
main "$@"