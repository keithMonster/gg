#!/bin/bash
# Git Pre-commit Hook for Prompt Quality Assurance
# 提示词系统提交前质量检查钩子

set -e

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

# 检查是否在正确的目录
if [ ! -f "changelog.md" ] || [ ! -d "prompts" ]; then
    log_error "请在gg项目根目录下运行此脚本"
    exit 1
fi

log_info "开始提交前质量检查..."

# 检查暂存的文件
STAGED_FILES=$(git diff --cached --name-only --diff-filter=ACM | grep -E '\.(md)$' || true)

if [ -z "$STAGED_FILES" ]; then
    log_info "没有发现暂存的Markdown文件，跳过质量检查"
    exit 0
fi

log_info "发现暂存的Markdown文件:"
echo "$STAGED_FILES" | sed 's/^/  - /'

# 检查prompts目录下的文件
PROMPT_FILES=$(echo "$STAGED_FILES" | grep '^prompts/' || true)

if [ -n "$PROMPT_FILES" ]; then
    log_info "检查提示词模块文件..."
    
    # 检查元数据完整性
    METADATA_ERRORS=0
    
    while IFS= read -r file; do
        if [ -f "$file" ]; then
            # 检查YAML前置元数据
            if ! head -20 "$file" | grep -q '^---$'; then
                log_warning "文件 $file 缺少YAML前置元数据"
                METADATA_ERRORS=$((METADATA_ERRORS + 1))
            else
                # 检查必需字段
                YAML_CONTENT=$(sed -n '/^---$/,/^---$/p' "$file" | head -n -1 | tail -n +2)
                
                if ! echo "$YAML_CONTENT" | grep -q '^version:'; then
                    log_warning "文件 $file 缺少version字段"
                    METADATA_ERRORS=$((METADATA_ERRORS + 1))
                fi
                
                if ! echo "$YAML_CONTENT" | grep -q '^author:'; then
                    log_warning "文件 $file 缺少author字段"
                    METADATA_ERRORS=$((METADATA_ERRORS + 1))
                fi
                
                if ! echo "$YAML_CONTENT" | grep -q '^description:'; then
                    log_warning "文件 $file 缺少description字段"
                    METADATA_ERRORS=$((METADATA_ERRORS + 1))
                fi
            fi
            
            # 检查文档结构
            if ! grep -q '^# ' "$file"; then
                log_warning "文件 $file 缺少主标题(H1)"
                METADATA_ERRORS=$((METADATA_ERRORS + 1))
            fi
        fi
    done <<< "$PROMPT_FILES"
    
    if [ $METADATA_ERRORS -gt 0 ]; then
        log_error "发现 $METADATA_ERRORS 个元数据问题，请修复后重新提交"
        log_info "提示：使用 'prompts/templates/module_template.md' 作为新模块的模板"
        log_info "参考：'prompts/standards/documentation_standards.md' 了解完整标准"
        exit 1
    fi
fi

# 运行快速质量检查
if [ -x "scripts/simple_audit.sh" ]; then
    log_info "运行快速质量检查..."
    
    # 临时运行审查脚本
    AUDIT_OUTPUT=$(./scripts/simple_audit.sh 2>&1 || true)
    AUDIT_EXIT_CODE=$?
    
    if [ $AUDIT_EXIT_CODE -eq 0 ]; then
        log_success "质量检查通过"
        
        # 提取关键指标
        MODULE_COUNT=$(echo "$AUDIT_OUTPUT" | grep -o '发现 [0-9]\+ 个模块' | grep -o '[0-9]\+' || echo "未知")
        log_info "当前系统包含 $MODULE_COUNT 个模块"
    else
        log_warning "质量检查发现问题，但不阻止提交"
        log_info "建议运行完整审查：./scripts/prompt_quality_audit.sh"
    fi
else
    log_warning "未找到质量检查脚本，跳过自动检查"
fi

# 检查changelog更新
if echo "$STAGED_FILES" | grep -q '^prompts/'; then
    if ! echo "$STAGED_FILES" | grep -q '^changelog.md$'; then
        log_warning "修改了prompts目录但未更新changelog.md"
        log_info "建议在提交前更新变更日志"
    fi
fi

# 检查大文件
LARGE_FILES=$(git diff --cached --name-only | xargs -I {} sh -c 'if [ -f "{}" ] && [ $(wc -c < "{}") -gt 100000 ]; then echo "{}"; fi' || true)

if [ -n "$LARGE_FILES" ]; then
    log_warning "发现大文件(>100KB):"
    echo "$LARGE_FILES" | sed 's/^/  - /'
    log_info "请确认这些文件确实需要提交"
fi

# 检查敏感信息
SENSITIVE_PATTERNS="(password|secret|key|token|api_key|private)"
SENSITIVE_FILES=$(git diff --cached | grep -i -E "$SENSITIVE_PATTERNS" | head -5 || true)

if [ -n "$SENSITIVE_FILES" ]; then
    log_error "检测到可能的敏感信息:"
    echo "$SENSITIVE_FILES" | sed 's/^/  /'
    log_error "请移除敏感信息后重新提交"
    exit 1
fi

log_success "所有检查通过，允许提交"
log_info "提交后建议运行完整质量审查以获得详细报告"

exit 0