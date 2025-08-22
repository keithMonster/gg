#!/bin/bash

# 技能发现系统函数库
# 版本: v1.0.0

# 获取项目根目录
get_project_root() {
    local script_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
    echo "$(dirname "$script_dir")"
}

# 全局变量
PROJECT_ROOT="$(get_project_root)"
SKILL_DISCOVERY_ROOT="$PROJECT_ROOT/skills"
CONFIG_FILE="$SKILL_DISCOVERY_ROOT/config/discovery_config.json"
INDEX_FILE="$SKILL_DISCOVERY_ROOT/index/skill_index.json"
STATS_FILE="$SKILL_DISCOVERY_ROOT/statistics/recommendation_stats.json"
LOG_FILE="$SKILL_DISCOVERY_ROOT/logs/skill_discovery.log"

# 日志记录函数
log_discovery() {
    local level="$1"
    local message="$2"
    local timestamp=$(date '+%Y-%m-%d %H:%M:%S')
    echo "[$timestamp] [$level] $message" | tee -a "$LOG_FILE"
}

log_info() {
    log_discovery "INFO" "$1"
}

log_warn() {
    log_discovery "WARN" "$1"
}

log_error() {
    log_discovery "ERROR" "$1"
}

log_success() {
    log_discovery "SUCCESS" "$1"
}

# 加载配置
load_discovery_config() {
    if [[ ! -f "$CONFIG_FILE" ]]; then
        log_error "配置文件不存在: $CONFIG_FILE"
        return 1
    fi
    
    log_info "加载技能发现配置: $CONFIG_FILE"
    return 0
}

# 构建技能索引
build_skill_index() {
    log_info "开始构建技能索引..."
    
    local skills_dir="$PROJECT_ROOT/prompts"
    local skill_count=0
    local skills_array="[]"
    
    # 确保索引目录存在
    mkdir -p "$(dirname "$INDEX_FILE")"
    
    # 创建基础索引结构
    local temp_file=$(mktemp)
    cat > "$temp_file" << 'EOF'
{
  "index_info": {
    "version": "1.0.0",
    "created_at": "2024-12-20T00:00:00Z",
    "last_updated": "",
    "total_skills": 0,
    "index_status": "built"
  },
  "skills": [],
  "categories": {
    "development": {
      "name": "开发技能",
      "description": "软件开发相关技能",
      "subcategories": ["frontend", "backend", "mobile", "desktop"]
    },
    "analysis": {
      "name": "分析技能",
      "description": "数据分析和处理技能",
      "subcategories": ["data_analysis", "reporting", "visualization"]
    },
    "automation": {
      "name": "自动化技能",
      "description": "自动化和脚本技能",
      "subcategories": ["scripting", "workflow", "deployment"]
    },
    "management": {
      "name": "管理技能",
      "description": "项目和系统管理技能",
      "subcategories": ["project_management", "system_admin", "monitoring"]
    }
  },
  "keyword_index": {},
  "tag_index": {},
  "dependency_graph": {}
}
EOF
    
    if [[ -d "$skills_dir" ]]; then
        # 扫描技能目录
        for skill_file in "$skills_dir"/*.md; do
            if [[ -f "$skill_file" ]]; then
                local skill_name=$(basename "$skill_file" .md)
                log_info "发现技能: $skill_name"
                
                # 读取文件内容获取描述
                local description=$(head -n 10 "$skill_file" | grep -E "^(#|##|描述|Description)" | head -n 1 | sed 's/^[#]* *//' || echo "$skill_name 技能")
                
                # 确定技能类别
                local category="general"
                case "$skill_name" in
                    *quality*|*test*) category="automation" ;;
                    *state*|*management*) category="management" ;;
                    *discovery*|*skill*) category="analysis" ;;
                    *report*|*generator*) category="analysis" ;;
                    *) category="development" ;;
                esac
                
                # 生成关键词
                local keywords
                case "$skill_name" in
                    *quality*) keywords='["质量", "测试", "检查", "自动化"]' ;;
                    *state*) keywords='["状态", "管理", "监控", "系统"]' ;;
                    *discovery*) keywords='["发现", "推荐", "技能", "匹配"]' ;;
                    *report*) keywords='["报告", "生成", "分析", "数据"]' ;;
                    *react*|*frontend*) keywords='["React", "前端", "组件", "开发"]' ;;
                    *) keywords='["开发", "工具", "系统"]' ;;
                esac
                
                # 构建技能对象
                local skill_obj=$(jq -n \
                    --arg id "$skill_name" \
                    --arg name "$skill_name" \
                    --arg desc "$description" \
                    --arg cat "$category" \
                    --argjson keywords "$keywords" \
                    --arg path "prompts/$skill_name.md" \
                    --arg created "$(date -u '+%Y-%m-%dT%H:%M:%SZ')" \
                    '{
                        "id": $id,
                        "name": $name,
                        "description": $desc,
                        "category": $cat,
                        "keywords": $keywords,
                        "tags": [$cat],
                        "file_path": $path,
                        "created_at": $created,
                        "usage_count": 0,
                        "last_used": null
                    }')
                
                # 添加到技能数组
                skills_array=$(echo "$skills_array" | jq ". += [$skill_obj]")
                ((skill_count++))
            fi
        done
    fi
    
    # 更新索引文件
    local timestamp=$(date -u '+%Y-%m-%dT%H:%M:%SZ')
    jq --argjson skills "$skills_array" --arg count "$skill_count" --arg timestamp "$timestamp" \
        '.skills = $skills | .index_info.total_skills = ($count | tonumber) | .index_info.last_updated = $timestamp | .index_info.index_status = "built"' \
        "$temp_file" > "$INDEX_FILE"
    rm "$temp_file"
    
    log_success "技能索引构建完成，共发现 $skill_count 个技能"
    return 0
}

# 推荐技能
recommend_skills() {
    local task_description="$1"
    
    if [[ -z "$task_description" ]]; then
        log_error "任务描述不能为空"
        return 1
    fi
    
    log_info "开始为任务推荐技能: $task_description"
    
    # 简单的关键词匹配推荐（演示版本）
    local recommendations="[]"
    
    # 检查是否包含开发相关关键词
    if echo "$task_description" | grep -qi -E "(开发|创建|构建|编程|代码)"; then
        recommendations=$(echo "$recommendations" | jq '. + [{"skill_id": "development", "confidence": 0.8, "reason": "包含开发相关关键词"}]')
    fi
    
    # 检查是否包含分析相关关键词
    if echo "$task_description" | grep -qi -E "(分析|统计|数据|报告)"; then
        recommendations=$(echo "$recommendations" | jq '. + [{"skill_id": "analysis", "confidence": 0.7, "reason": "包含分析相关关键词"}]')
    fi
    
    # 检查是否包含自动化相关关键词
    if echo "$task_description" | grep -qi -E "(自动化|脚本|批处理)"; then
        recommendations=$(echo "$recommendations" | jq '. + [{"skill_id": "automation", "confidence": 0.75, "reason": "包含自动化相关关键词"}]')
    fi
    
    # 生成推荐结果
    local recommendation_id="rec_$(date +%s)_$(jot -r 1 1000 9999)"
    local timestamp=$(date -u '+%Y-%m-%dT%H:%M:%SZ')
    
    local result=$(jq -n \
        --arg id "$recommendation_id" \
        --arg task "$task_description" \
        --arg timestamp "$timestamp" \
        --argjson recommendations "$recommendations" \
        '{
            "recommendation_id": $id,
            "task_description": $task,
            "timestamp": $timestamp,
            "recommendations": $recommendations,
            "algorithm_used": "simple_keyword_matching",
            "processing_time_ms": 100
        }')
    
    echo "$result"
    log_success "技能推荐完成，推荐ID: $recommendation_id"
    
    # 保存推荐记录
    echo "$result" > "$SKILL_DISCOVERY_ROOT/recommendations/${recommendation_id}.json"
    
    return 0
}

# 记录反馈
record_feedback() {
    local recommendation_id="$1"
    local result="$2"
    local rating="$3"
    local comments="$4"
    
    if [[ -z "$recommendation_id" || -z "$result" ]]; then
        log_error "推荐ID和结果不能为空"
        return 1
    fi
    
    log_info "记录反馈: $recommendation_id -> $result"
    
    local timestamp=$(date -u '+%Y-%m-%dT%H:%M:%SZ')
    local feedback=$(jq -n \
        --arg id "$recommendation_id" \
        --arg result "$result" \
        --arg rating "${rating:-0}" \
        --arg comments "${comments:-}" \
        --arg timestamp "$timestamp" \
        '{
            "recommendation_id": $id,
            "result": $result,
            "rating": ($rating | tonumber),
            "comments": $comments,
            "timestamp": $timestamp
        }')
    
    # 保存反馈记录
    local feedback_file="$SKILL_DISCOVERY_ROOT/feedback/feedback_$(date +%Y%m%d).json"
    if [[ -f "$feedback_file" ]]; then
        # 追加到现有文件
        jq --argjson feedback "$feedback" '. + [$feedback]' "$feedback_file" > "$feedback_file.tmp" && mv "$feedback_file.tmp" "$feedback_file"
    else
        # 创建新文件
        echo "[$feedback]" > "$feedback_file"
    fi
    
    log_success "反馈记录完成"
    return 0
}

# 显示统计信息
show_discovery_stats() {
    log_info "显示技能发现统计信息"
    
    if [[ ! -f "$STATS_FILE" ]]; then
        log_error "统计文件不存在: $STATS_FILE"
        return 1
    fi
    
    echo "=== 技能发现系统统计 ==="
    echo "时间: $(date '+%Y-%m-%d %H:%M:%S')"
    echo
    
    # 显示全局指标
    local total_recommendations=$(jq -r '.global_metrics.total_recommendations' "$STATS_FILE")
    local total_feedback=$(jq -r '.global_metrics.total_feedback' "$STATS_FILE")
    local avg_accuracy=$(jq -r '.global_metrics.average_accuracy' "$STATS_FILE")
    
    echo "全局指标:"
    echo "  总推荐次数: $total_recommendations"
    echo "  总反馈次数: $total_feedback"
    echo "  平均准确率: $avg_accuracy"
    echo
    
    # 显示技能索引信息
    if [[ -f "$INDEX_FILE" ]]; then
        local total_skills=$(jq -r '.index_info.total_skills' "$INDEX_FILE")
        local index_status=$(jq -r '.index_info.index_status' "$INDEX_FILE")
        local last_updated=$(jq -r '.index_info.last_updated' "$INDEX_FILE")
        
        echo "技能索引:"
        echo "  技能总数: $total_skills"
        echo "  索引状态: $index_status"
        echo "  最后更新: $last_updated"
    fi
    
    return 0
}

# 运行技能发现查询
run_skill_discovery() {
    local command="$1"
    shift
    
    case "$command" in
        "recommend")
            recommend_skills "$@"
            ;;
        "feedback")
            record_feedback "$@"
            ;;
        "build-index")
            build_skill_index
            ;;
        "stats")
            show_discovery_stats
            ;;
        "help")
            show_help
            ;;
        "status")
            check_system_status
            ;;
        "analyze")
            analyze_code_file "$@"
            ;;
        *)
            log_error "未知命令: $command"
            echo "使用 'help' 查看可用命令"
            return 1
            ;;
    esac
}

# 显示帮助信息
show_help() {
    echo "技能发现系统命令:"
    echo "  recommend <task_description>  - 获取技能推荐"
    echo "  feedback <rec_id> <result> [rating] [comments]  - 记录反馈"
    echo "  build-index  - 构建技能索引"
    echo "  stats  - 显示统计信息"
    echo "  status  - 检查系统状态"
    echo "  analyze <file_path>  - 分析代码文件"
    echo "  help  - 显示帮助信息"
}

# 检查系统状态
check_system_status() {
    echo "[INFO] 技能发现系统状态:"
    
    # 检查配置文件
    if [ -f "$CONFIG_FILE" ]; then
        echo "配置文件: ✓ 存在"
    else
        echo "配置文件: ✗ 缺失"
    fi
    
    # 检查技能索引
    if [ -f "$INDEX_FILE" ]; then
        local skill_count=$(jq -r '.index_info.total_skills // 0' "$INDEX_FILE" 2>/dev/null || echo "0")
        echo "技能索引: ✓ 存在 ($skill_count 个技能)"
    else
        echo "技能索引: ✗ 缺失"
    fi
    
    # 检查推荐记录
    local rec_count=$(find "$SKILL_DISCOVERY_ROOT/recommendations" -name "*.json" 2>/dev/null | wc -l | tr -d ' ')
    echo "推荐记录: $rec_count 个"
    
    # 检查反馈记录
    local feedback_count=$(find "$SKILL_DISCOVERY_ROOT/feedback" -name "*.json" 2>/dev/null | wc -l | tr -d ' ')
    echo "反馈记录: $feedback_count 个"
    
    # 检查目录结构
    if [ -d "$SKILL_DISCOVERY_ROOT" ]; then
        echo "技能目录: ✓ 存在"
    else
        echo "技能目录: ✗ 缺失"
    fi
}

# 分析代码文件
analyze_code_file() {
    local file_path="$1"
    
    if [ ! -f "$file_path" ]; then
        log_error "文件不存在: $file_path"
        return 1
    fi
    
    log_info "分析代码文件: $file_path"
    
    # 简单的代码分析
    local file_ext="${file_path##*.}"
    local skills_found=()
    
    case "$file_ext" in
        "js"|"jsx")
            if grep -q "React" "$file_path"; then
                skills_found+=("React开发")
            fi
            if grep -q "function\|const.*=>" "$file_path"; then
                skills_found+=("JavaScript编程")
            fi
            ;;
        "py")
            if grep -q "import\|def" "$file_path"; then
                skills_found+=("Python编程")
            fi
            if grep -q "pandas\|numpy" "$file_path"; then
                skills_found+=("数据分析")
            fi
            ;;
        "sh"|"bash")
            skills_found+=("Shell脚本")
            if grep -q "function\|()" "$file_path"; then
                skills_found+=("自动化脚本")
            fi
            ;;
        *)
            skills_found+=("通用编程")
            ;;
    esac
    
    echo "分析完成: 发现 ${#skills_found[@]} 个相关技能"
    for skill in "${skills_found[@]}"; do
        echo "  - $skill"
    done
    
    return 0
}

# 如果直接执行此脚本
if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
    # 加载配置
    load_discovery_config
    
    # 执行命令
    run_skill_discovery "$@"
fi
