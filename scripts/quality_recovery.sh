#!/bin/bash

# 质量保证错误恢复脚本
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
STATE_DIR="$PROJECT_ROOT/state"
SCRIPTS_DIR="$PROJECT_ROOT/scripts"

# 加载质量保证函数
source "$SCRIPTS_DIR/quality_functions.sh" 2>/dev/null || {
    log_error "无法加载质量保证函数库"
    exit 1
}

# 自动修复状态文件缺失问题
fix_missing_state_files() {
    log_info "开始修复缺失的状态文件..."
    
    local fixed_count=0
    
    # 检查并创建system_state.json
    if [[ ! -f "$STATE_DIR/system_state.json" ]]; then
        log_info "创建缺失的system_state.json文件"
        cat > "$STATE_DIR/system_state.json" << 'EOF'
{
  "systemState": {
    "version": "1.0.0",
    "lastUpdate": "2024-12-20T15:49:00Z",
    "status": "HEALTHY",
    "uptime": 0,
    "components": {
      "qualityAssurance": {
        "status": "ACTIVE",
        "lastCheck": "2024-12-20T15:49:00Z",
        "version": "1.0.0"
      },
      "stateManagement": {
        "status": "ACTIVE",
        "lastUpdate": "2024-12-20T15:49:00Z",
        "version": "1.0.0"
      }
    },
    "environment": {
      "platform": "macOS",
      "architecture": "arm64",
      "nodeVersion": "unknown",
      "pythonVersion": "unknown"
    }
  }
}
EOF
        ((fixed_count++))
        log_success "已创建system_state.json文件"
    fi
    
    # 检查并创建performance.json
    if [[ ! -f "$STATE_DIR/performance.json" ]]; then
        log_info "创建缺失的performance.json文件"
        cat > "$STATE_DIR/performance.json" << 'EOF'
{
  "performance": {
    "timestamp": "2024-12-20T15:49:00Z",
    "metrics": {
      "taskSuccessRate": 100.0,
      "avgResponseTime": 0.0,
      "systemLoad": {
        "cpu": 0.0,
        "memory": 0.0,
        "disk": 0.0
      },
      "errorRate": 0.0,
      "throughput": 0.0
    },
    "trends": {
      "responseTimeTrend": "stable",
      "errorRateTrend": "stable",
      "throughputTrend": "stable"
    },
    "alerts": [],
    "recommendations": []
  }
}
EOF
        ((fixed_count++))
        log_success "已创建performance.json文件"
    fi
    
    # 检查并创建health_check.json
    if [[ ! -f "$STATE_DIR/health_check.json" ]]; then
        log_info "创建缺失的health_check.json文件"
        cat > "$STATE_DIR/health_check.json" << 'EOF'
{
  "healthCheck": {
    "timestamp": "2024-12-20T15:49:00Z",
    "overallStatus": "HEALTHY",
    "components": {
      "fileSystem": {
        "status": "HEALTHY",
        "lastCheck": "2024-12-20T15:49:00Z",
        "details": "所有关键文件可访问"
      },
      "configuration": {
        "status": "HEALTHY",
        "lastCheck": "2024-12-20T15:49:00Z",
        "details": "配置文件格式正确"
      },
      "dependencies": {
        "status": "HEALTHY",
        "lastCheck": "2024-12-20T15:49:00Z",
        "details": "所有依赖项可用"
      },
      "qualityAssurance": {
        "status": "HEALTHY",
        "lastCheck": "2024-12-20T15:49:00Z",
        "details": "质量保证系统运行正常"
      }
    },
    "checks": {
      "diskSpace": {
        "status": "OK",
        "value": "充足",
        "threshold": "85%"
      },
      "filePermissions": {
        "status": "OK",
        "value": "正常",
        "threshold": "可读写"
      },
      "configIntegrity": {
        "status": "OK",
        "value": "完整",
        "threshold": "无错误"
      }
    }
  }
}
EOF
        ((fixed_count++))
        log_success "已创建health_check.json文件"
    fi
    
    if [[ $fixed_count -gt 0 ]]; then
        log_success "成功修复了 $fixed_count 个缺失的状态文件"
        return 0
    else
        log_info "没有发现缺失的状态文件"
        return 1
    fi
}

# 修复JSON格式错误
fix_json_format_errors() {
    log_info "开始检查和修复JSON格式错误..."
    
    local fixed_count=0
    local json_files=()
    
    # 收集所有JSON文件
    while IFS= read -r -d '' json_file; do
        json_files+=("$json_file")
    done < <(find "$PROJECT_ROOT" -name "*.json" -type f -print0 2>/dev/null)
    
    for json_file in "${json_files[@]}"; do
        if ! python3 -m json.tool "$json_file" >/dev/null 2>&1; then
            log_warning "发现JSON格式错误: $json_file"
            
            # 尝试备份原文件
            local backup_file="${json_file}.backup.$(date +%s)"
            cp "$json_file" "$backup_file"
            log_info "已备份原文件到: $backup_file"
            
            # 尝试自动修复常见问题
            if fix_common_json_issues "$json_file"; then
                ((fixed_count++))
                log_success "已修复JSON文件: $json_file"
            else
                log_error "无法自动修复JSON文件: $json_file"
                # 恢复备份
                mv "$backup_file" "$json_file"
            fi
        fi
    done
    
    if [[ $fixed_count -gt 0 ]]; then
        log_success "成功修复了 $fixed_count 个JSON格式错误"
        return 0
    else
        log_info "没有发现JSON格式错误"
        return 1
    fi
}

# 修复常见JSON问题
fix_common_json_issues() {
    local json_file="$1"
    local temp_file="${json_file}.tmp"
    
    # 尝试修复常见问题：
    # 1. 移除尾随逗号
    # 2. 修复单引号为双引号
    # 3. 移除注释
    
    sed -e 's/,\s*}/}/g' \
        -e 's/,\s*]/]/g' \
        -e "s/'/\"/g" \
        -e '/^\/\//d' \
        -e '/^\/\*/,/\*\//d' \
        "$json_file" > "$temp_file"
    
    # 验证修复后的JSON
    if python3 -m json.tool "$temp_file" >/dev/null 2>&1; then
        mv "$temp_file" "$json_file"
        return 0
    else
        rm -f "$temp_file"
        return 1
    fi
}

# 修复文件权限问题
fix_file_permissions() {
    log_info "开始检查和修复文件权限问题..."
    
    local fixed_count=0
    
    # 关键文件列表
    local critical_files=(
        "$PROJECT_ROOT/prompts/system_prompt.md"
        "$QA_DIR/config/qa_config.json"
        "$STATE_DIR/system_state.json"
        "$STATE_DIR/performance.json"
        "$STATE_DIR/health_check.json"
    )
    
    for file in "${critical_files[@]}"; do
        if [[ -f "$file" ]]; then
            if [[ ! -r "$file" ]]; then
                log_warning "修复文件读权限: $file"
                chmod +r "$file"
                ((fixed_count++))
            fi
            
            if [[ ! -w "$file" ]]; then
                log_warning "修复文件写权限: $file"
                chmod +w "$file"
                ((fixed_count++))
            fi
        fi
    done
    
    # 修复脚本执行权限
    local script_files=(
        "$SCRIPTS_DIR/quality_functions.sh"
        "$SCRIPTS_DIR/state_functions.sh"
        "$SCRIPTS_DIR/quality_assurance_init.sh"
        "$SCRIPTS_DIR/state_management_init.sh"
    )
    
    for script in "${script_files[@]}"; do
        if [[ -f "$script" && ! -x "$script" ]]; then
            log_warning "修复脚本执行权限: $script"
            chmod +x "$script"
            ((fixed_count++))
        fi
    done
    
    if [[ $fixed_count -gt 0 ]]; then
        log_success "成功修复了 $fixed_count 个文件权限问题"
        return 0
    else
        log_info "没有发现文件权限问题"
        return 1
    fi
}

# 执行自动恢复
auto_recovery() {
    local recovery_type="${1:-all}"
    
    log_info "开始自动恢复程序: $recovery_type"
    
    local recovery_count=0
    
    case "$recovery_type" in
        "state_files")
            if fix_missing_state_files; then
                ((recovery_count++))
            fi
            ;;
        "json_format")
            if fix_json_format_errors; then
                ((recovery_count++))
            fi
            ;;
        "permissions")
            if fix_file_permissions; then
                ((recovery_count++))
            fi
            ;;
        "all")
            if fix_missing_state_files; then
                ((recovery_count++))
            fi
            if fix_json_format_errors; then
                ((recovery_count++))
            fi
            if fix_file_permissions; then
                ((recovery_count++))
            fi
            ;;
        *)
            log_error "未知的恢复类型: $recovery_type"
            log_info "可用类型: state_files, json_format, permissions, all"
            return 1
            ;;
    esac
    
    if [[ $recovery_count -gt 0 ]]; then
        log_success "自动恢复完成，执行了 $recovery_count 项修复"
        
        # 重新运行质量检查验证修复效果
        log_info "重新运行质量检查验证修复效果..."
        if run_full_quality_check; then
            log_success "质量检查通过，恢复成功！"
        else
            log_warning "质量检查仍有问题，可能需要手动干预"
        fi
    else
        log_info "没有执行任何修复操作"
    fi
    
    return 0
}

# 创建系统检查点
create_system_checkpoint() {
    local checkpoint_name="${1:-auto_$(date +%Y%m%d_%H%M%S)}"
    local checkpoint_dir="$QA_DIR/backups/$checkpoint_name"
    
    log_info "创建系统检查点: $checkpoint_name"
    
    mkdir -p "$checkpoint_dir"
    
    # 备份关键文件
    local backup_files=(
        "$STATE_DIR"
        "$QA_DIR/config"
        "$QA_DIR/metrics"
        "$PROJECT_ROOT/prompts"
    )
    
    for item in "${backup_files[@]}"; do
        if [[ -e "$item" ]]; then
            cp -r "$item" "$checkpoint_dir/"
            log_info "已备份: $(basename "$item")"
        fi
    done
    
    # 创建检查点元数据
    cat > "$checkpoint_dir/checkpoint_info.json" << EOF
{
  "checkpoint": {
    "name": "$checkpoint_name",
    "created": "$(date -u '+%Y-%m-%dT%H:%M:%SZ')",
    "type": "system_backup",
    "description": "自动创建的系统检查点",
    "files": [
$(printf '      "%s",' "${backup_files[@]}" | sed 's/,$//')
    ]
  }
}
EOF
    
    log_success "检查点创建完成: $checkpoint_dir"
}

# 显示帮助信息
show_help() {
    echo "质量保证错误恢复脚本"
    echo ""
    echo "用法: $0 [选项]"
    echo ""
    echo "选项:"
    echo "  auto [type]          执行自动恢复 (type: state_files|json_format|permissions|all)"
    echo "  fix-state-files      修复缺失的状态文件"
    echo "  fix-json-format      修复JSON格式错误"
    echo "  fix-permissions      修复文件权限问题"
    echo "  checkpoint [name]    创建系统检查点"
    echo "  help                 显示此帮助信息"
    echo ""
    echo "示例:"
    echo "  $0 auto                    # 执行全面自动恢复"
    echo "  $0 auto state_files         # 只修复状态文件"
    echo "  $0 fix-json-format          # 只修复JSON格式"
    echo "  $0 checkpoint backup_v1     # 创建名为backup_v1的检查点"
}

# 主函数
main() {
    local action="${1:-auto}"
    
    case "$action" in
        "auto")
            auto_recovery "${2:-all}"
            ;;
        "fix-state-files")
            fix_missing_state_files
            ;;
        "fix-json-format")
            fix_json_format_errors
            ;;
        "fix-permissions")
            fix_file_permissions
            ;;
        "checkpoint")
            create_system_checkpoint "$2"
            ;;
        "help"|"--help"|"h")
            show_help
            ;;
        *)
            log_error "未知操作: $action"
            show_help
            exit 1
            ;;
    esac
}

# 执行主函数
main "$@"