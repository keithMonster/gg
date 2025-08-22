#!/bin/bash

# 智能化技能发现和推荐系统初始化脚本
# 版本: v1.0.0
# 创建时间: 2024-12-20

set -e

# 获取脚本所在目录的绝对路径
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(dirname "$SCRIPT_DIR")"

echo "=== 智能化技能发现和推荐系统初始化 ==="
echo "项目根目录: $PROJECT_ROOT"
echo "开始时间: $(date '+%Y-%m-%d %H:%M:%S')"
echo

# 创建目录结构
echo "[INFO] 创建技能发现系统目录结构..."
mkdir -p "$PROJECT_ROOT/skills" || true
mkdir -p "$PROJECT_ROOT/skills/index" || true
mkdir -p "$PROJECT_ROOT/skills/metadata" || true
mkdir -p "$PROJECT_ROOT/skills/cache" || true
mkdir -p "$PROJECT_ROOT/skills/models" || true
mkdir -p "$PROJECT_ROOT/skills/logs" || true
mkdir -p "$PROJECT_ROOT/skills/config" || true
mkdir -p "$PROJECT_ROOT/skills/recommendations" || true
mkdir -p "$PROJECT_ROOT/skills/feedback" || true
mkdir -p "$PROJECT_ROOT/skills/statistics" || true

echo "[SUCCESS] 目录结构创建完成"

# 生成技能发现配置文件
echo "[INFO] 生成技能发现配置文件..."
cat > "$PROJECT_ROOT/skills/config/discovery_config.json" << 'EOF'
{
  "system_info": {
    "name": "智能化技能发现和推荐系统",
    "version": "1.0.0",
    "created_at": "2024-12-20T00:00:00Z",
    "description": "基于机器学习的智能技能发现和推荐系统"
  },
  "matching_algorithms": {
    "keyword_matching": {
      "enabled": true,
      "weight": 0.3,
      "algorithm": "tfidf_with_edit_distance",
      "parameters": {
        "min_similarity": 0.3,
        "max_edit_distance": 2,
        "case_sensitive": false
      }
    },
    "semantic_similarity": {
      "enabled": true,
      "weight": 0.4,
      "algorithm": "word_vector_cosine",
      "parameters": {
        "min_similarity": 0.4,
        "vector_dimension": 300,
        "model_path": "models/word_vectors.bin"
      }
    },
    "collaborative_filtering": {
      "enabled": true,
      "weight": 0.2,
      "algorithm": "user_based_cf",
      "parameters": {
        "min_users": 5,
        "similarity_threshold": 0.5,
        "max_neighbors": 10
      }
    },
    "rule_based": {
      "enabled": true,
      "weight": 0.1,
      "algorithm": "expert_rules",
      "parameters": {
        "rules_file": "config/expert_rules.json",
        "confidence_threshold": 0.8
      }
    }
  },
  "recommendation_settings": {
    "max_single_recommendations": 10,
    "max_combination_recommendations": 5,
    "max_skills_per_combination": 4,
    "min_confidence_score": 0.3,
    "high_confidence_threshold": 0.8,
    "combination_synergy_threshold": 0.6
  },
  "performance_settings": {
    "cache": {
      "enabled": true,
      "ttl_seconds": 3600,
      "max_entries": 1000,
      "cleanup_interval": 300
    },
    "execution": {
      "max_concurrent_requests": 10,
      "request_timeout_seconds": 30,
      "max_processing_time_seconds": 60
    },
    "indexing": {
      "auto_rebuild_interval": "daily",
      "incremental_update": true,
      "batch_size": 100
    }
  },
  "learning_settings": {
    "feedback_processing": {
      "batch_size": 100,
      "processing_interval": "hourly",
      "min_feedback_count": 10
    },
    "model_training": {
      "auto_retrain": true,
      "retrain_frequency": "daily",
      "validation_split": 0.2,
      "early_stopping": true
    },
    "pattern_discovery": {
      "enabled": true,
      "confidence_threshold": 0.7,
      "min_pattern_support": 5,
      "discovery_frequency": "weekly"
    }
  },
  "integration_settings": {
    "state_management": {
      "enabled": true,
      "state_file": "../state/skill_discovery_state.json",
      "checkpoint_interval": 300
    },
    "quality_assurance": {
      "enabled": true,
      "quality_checks": ["recommendation_quality", "performance_monitoring", "data_consistency"],
      "alert_thresholds": {
        "low_accuracy": 0.6,
        "high_latency": 5.0,
        "error_rate": 0.1
      }
    }
  },
  "logging": {
    "level": "INFO",
    "file": "logs/skill_discovery.log",
    "max_size_mb": 100,
    "backup_count": 5,
    "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
  }
}
EOF

echo "[SUCCESS] 配置文件生成完成"

# 生成专家规则配置
echo "[INFO] 生成专家规则配置..."
cat > "$PROJECT_ROOT/skills/config/expert_rules.json" << 'EOF'
{
  "rules": [
    {
      "id": "web_development_rule",
      "name": "Web开发技能规则",
      "condition": {
        "keywords": ["网站", "前端", "后端", "API", "数据库"],
        "task_type": "development"
      },
      "recommendations": [
        {
          "skill_category": "web_development",
          "confidence": 0.9,
          "priority": 1
        }
      ]
    },
    {
      "id": "data_analysis_rule",
      "name": "数据分析技能规则",
      "condition": {
        "keywords": ["数据", "分析", "统计", "图表", "报告"],
        "task_type": "analysis"
      },
      "recommendations": [
        {
          "skill_category": "data_analysis",
          "confidence": 0.85,
          "priority": 1
        }
      ]
    },
    {
      "id": "automation_rule",
      "name": "自动化技能规则",
      "condition": {
        "keywords": ["自动化", "脚本", "批处理", "定时任务"],
        "task_type": "automation"
      },
      "recommendations": [
        {
          "skill_category": "automation",
          "confidence": 0.8,
          "priority": 1
        }
      ]
    }
  ],
  "combination_rules": [
    {
      "id": "full_stack_combination",
      "name": "全栈开发组合",
      "condition": {
        "keywords": ["全栈", "完整项目", "端到端"],
        "complexity": "high"
      },
      "skill_combination": [
        "frontend_development",
        "backend_development",
        "database_management",
        "deployment"
      ],
      "synergy_score": 0.9
    }
  ]
}
EOF

echo "[SUCCESS] 专家规则配置生成完成"

# 生成技能索引初始数据
echo "[INFO] 生成技能索引初始数据..."
cat > "$PROJECT_ROOT/skills/index/skill_index.json" << 'EOF'
{
  "index_info": {
    "version": "1.0.0",
    "created_at": "2024-12-20T00:00:00Z",
    "last_updated": "2024-12-20T00:00:00Z",
    "total_skills": 0,
    "index_status": "initialized"
  },
  "skills": {},
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

echo "[SUCCESS] 技能索引初始数据生成完成"

# 生成推荐统计初始数据
echo "[INFO] 生成推荐统计初始数据..."
cat > "$PROJECT_ROOT/skills/statistics/recommendation_stats.json" << 'EOF'
{
  "statistics_info": {
    "version": "1.0.0",
    "created_at": "2024-12-20T00:00:00Z",
    "last_updated": "2024-12-20T00:00:00Z",
    "data_retention_days": 90
  },
  "global_metrics": {
    "total_recommendations": 0,
    "total_feedback": 0,
    "average_accuracy": 0.0,
    "average_response_time": 0.0,
    "user_satisfaction": 0.0
  },
  "skill_metrics": {},
  "algorithm_performance": {
    "keyword_matching": {
      "accuracy": 0.0,
      "precision": 0.0,
      "recall": 0.0,
      "f1_score": 0.0
    },
    "semantic_similarity": {
      "accuracy": 0.0,
      "precision": 0.0,
      "recall": 0.0,
      "f1_score": 0.0
    },
    "collaborative_filtering": {
      "accuracy": 0.0,
      "precision": 0.0,
      "recall": 0.0,
      "f1_score": 0.0
    },
    "rule_based": {
      "accuracy": 0.0,
      "precision": 0.0,
      "recall": 0.0,
      "f1_score": 0.0
    }
  },
  "user_behavior": {
    "popular_skills": [],
    "common_combinations": [],
    "usage_patterns": {}
  }
}
EOF

echo "[SUCCESS] 推荐统计初始数据生成完成"

# 生成技能发现函数库
echo "[INFO] 生成技能发现函数库..."
cat > "$PROJECT_ROOT/scripts/skill_discovery_functions.sh" << 'EOF'
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
    
    local skills_dir="$PROJECT_ROOT/prompts/skills"
    local index_data="{}"
    local skill_count=0
    
    if [[ -d "$skills_dir" ]]; then
        # 扫描技能目录
        for skill_file in "$skills_dir"/*.md; do
            if [[ -f "$skill_file" ]]; then
                local skill_name=$(basename "$skill_file" .md)
                log_info "发现技能: $skill_name"
                ((skill_count++))
            fi
        done
    fi
    
    # 更新索引文件
    local timestamp=$(date -u '+%Y-%m-%dT%H:%M:%SZ')
    jq --arg count "$skill_count" --arg timestamp "$timestamp" \
        '.index_info.total_skills = ($count | tonumber) | .index_info.last_updated = $timestamp | .index_info.index_status = "built"' \
        "$INDEX_FILE" > "$INDEX_FILE.tmp" && mv "$INDEX_FILE.tmp" "$INDEX_FILE"
    
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
    local recommendation_id="rec_$(date +%s)_$(shuf -i 1000-9999 -n 1)"
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
            echo "技能发现系统命令:"
            echo "  recommend <task_description>  - 获取技能推荐"
            echo "  feedback <rec_id> <result> [rating] [comments]  - 记录反馈"
            echo "  build-index  - 构建技能索引"
            echo "  stats  - 显示统计信息"
            echo "  help  - 显示帮助信息"
            ;;
        *)
            log_error "未知命令: $command"
            echo "使用 'help' 查看可用命令"
            return 1
            ;;
    esac
}

# 如果直接执行此脚本
if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
    # 加载配置
    load_discovery_config
    
    # 执行命令
    run_skill_discovery "$@"
fi
EOF

chmod +x "$PROJECT_ROOT/scripts/skill_discovery_functions.sh"
echo "[SUCCESS] 技能发现函数库生成完成"

# 创建CLI命令别名
echo "[INFO] 创建CLI命令别名..."
cat > "$PROJECT_ROOT/scripts/gg-skill-discovery" << 'EOF'
#!/bin/bash

# 技能发现系统CLI入口
# 使用方法: gg-skill-discovery <command> [args...]

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
source "$SCRIPT_DIR/skill_discovery_functions.sh"

run_skill_discovery "$@"
EOF

chmod +x "$PROJECT_ROOT/scripts/gg-skill-discovery"
echo "[SUCCESS] CLI命令创建完成"

# 初始化日志文件
echo "[INFO] 初始化日志文件..."
touch "$PROJECT_ROOT/skills/logs/skill_discovery.log"
echo "$(date '+%Y-%m-%d %H:%M:%S') [INFO] 技能发现系统初始化完成" >> "$PROJECT_ROOT/skills/logs/skill_discovery.log"
echo "[SUCCESS] 日志文件初始化完成"

# 构建初始技能索引
echo "[INFO] 构建初始技能索引..."
source "$PROJECT_ROOT/scripts/skill_discovery_functions.sh"
build_skill_index

echo
echo "=== 初始化完成 ==="
echo "技能发现系统已成功初始化！"
echo
echo "目录结构:"
echo "  $PROJECT_ROOT/skills/                    - 技能发现系统根目录"
echo "  $PROJECT_ROOT/skills/config/             - 配置文件目录"
echo "  $PROJECT_ROOT/skills/index/              - 技能索引目录"
echo "  $PROJECT_ROOT/skills/recommendations/    - 推荐记录目录"
echo "  $PROJECT_ROOT/skills/feedback/           - 反馈数据目录"
echo "  $PROJECT_ROOT/skills/statistics/         - 统计数据目录"
echo "  $PROJECT_ROOT/skills/logs/               - 日志文件目录"
echo
echo "使用指南:"
echo "  # 获取技能推荐"
echo "  ./scripts/gg-skill-discovery recommend \"创建一个React组件\""
echo
echo "  # 记录反馈"
echo "  ./scripts/gg-skill-discovery feedback rec_123 success 5 \"很好用\""
echo
echo "  # 查看统计"
echo "  ./scripts/gg-skill-discovery stats"
echo
echo "  # 重建索引"
echo "  ./scripts/gg-skill-discovery build-index"
echo
echo "  # 查看帮助"
echo "  ./scripts/gg-skill-discovery help"
echo
echo "完成时间: $(date '+%Y-%m-%d %H:%M:%S')"