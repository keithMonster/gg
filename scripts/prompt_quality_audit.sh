#!/bin/bash
# prompt_quality_audit.sh
# 提示词系统质量审查自动化脚本
# Author: gg (v9.2.4 evolution)
# Created: 2025-08-14

set -e

# 颜色定义
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# 配置
PROMPTS_DIR="/Users/xuke/OtherProject/_self/gg/prompts"
REPORT_FILE="./outputs/prompt_audit_report_$(date +%Y%m%d_%H%M%S).md"
ERROR_COUNT=0
WARNING_COUNT=0

# 日志函数
log_info() {
    echo -e "${BLUE}[INFO]${NC} $1"
}

log_success() {
    echo -e "${GREEN}[SUCCESS]${NC} $1"
}

log_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
    ((WARNING_COUNT++))
}

log_error() {
    echo -e "${RED}[ERROR]${NC} $1"
    ((ERROR_COUNT++))
}

# 初始化报告文件
init_report() {
    cat > "$REPORT_FILE" << 'EOF'
# 提示词系统质量审查报告

**生成时间**: TIMESTAMP_PLACEHOLDER
**审查范围**: PROMPTS_DIR_PLACEHOLDER
**审查版本**: VERSION_PLACEHOLDER

## 执行摘要

SUMMARY_PLACEHOLDER

EOF
    
    # 替换占位符
    sed -i '' "s/TIMESTAMP_PLACEHOLDER/$(date '+%Y-%m-%d %H:%M:%S')/g" "$REPORT_FILE"
    sed -i '' "s|PROMPTS_DIR_PLACEHOLDER|$PROMPTS_DIR|g" "$REPORT_FILE"
    
    local version=$(cd "$(dirname "$PROMPTS_DIR")" && git rev-parse --short HEAD 2>/dev/null || echo "未知")
    sed -i '' "s/VERSION_PLACEHOLDER/$version/g" "$REPORT_FILE"
}

# 1. 文件结构验证
validate_file_structure() {
    log_info "开始文件结构验证..."
    
    echo "" >> "$REPORT_FILE"
    echo "## 1. 文件结构验证" >> "$REPORT_FILE"
    echo "" >> "$REPORT_FILE"
    echo "### 1.1 必需元数据检查" >> "$REPORT_FILE"
    echo "" >> "$REPORT_FILE"
    echo "| 文件 | version | author | description | 状态 |" >> "$REPORT_FILE"
    echo "|------|---------|--------|-------------|------|" >> "$REPORT_FILE"
    
    find "$PROMPTS_DIR" -name "*.md" | while read file; do
        local filename=$(basename "$file")
        local has_version="✗"
        local has_author="✗"
        local has_description="✗"
        
        if grep -q "^version:" "$file"; then
            has_version="✓"
        fi
        
        if grep -q "^author:" "$file"; then
            has_author="✓"
        fi
        
        if grep -q "^description:" "$file"; then
            has_description="✓"
        fi
        
        local status="正常"
        if [[ "$has_version" == "✗" ]] || [[ "$has_author" == "✗" ]] || [[ "$has_description" == "✗" ]]; then
            status="需修复"
            log_warning "$filename 缺少必需元数据"
        fi
        
        echo "| $filename | $has_version | $has_author | $has_description | $status |" >> "$REPORT_FILE"
    done
    
    log_success "文件结构验证完成"
}

# 2. 内容一致性检查
check_content_consistency() {
    log_info "开始内容一致性检查..."
    
    echo "" >> "$REPORT_FILE"
    echo "### 1.2 术语一致性分析" >> "$REPORT_FILE"
    
    # 检查智能体相关术语
    echo "" >> "$REPORT_FILE"
    echo "**智能体术语使用统计**:" >> "$REPORT_FILE"
    echo "" >> "$REPORT_FILE"
    echo '```' >> "$REPORT_FILE"
    
    # 创建临时文件来处理复杂的管道操作
    local temp_file="./outputs/temp_term_stats.txt"
    grep -r "智能体\|AI智能体\|AI助手\|助手" "$PROMPTS_DIR" --include="*.md" | \
    cut -d: -f2 | sed 's/.*\(智能体\|AI智能体\|AI助手\|助手\).*/\1/' | \
    sort | uniq -c | sort -nr > "$temp_file"
    
    cat "$temp_file" >> "$REPORT_FILE"
    rm -f "$temp_file"
    
    echo '```' >> "$REPORT_FILE"
    
    # 检查时间格式一致性
    echo "" >> "$REPORT_FILE"
    echo "**时间格式使用统计**:" >> "$REPORT_FILE"
    echo "" >> "$REPORT_FILE"
    echo '```' >> "$REPORT_FILE"
    
    local temp_time_file="./outputs/temp_time_stats.txt"
    grep -r "[0-9]\{4\}-[0-9]\{2\}-[0-9]\{2\}" "$PROMPTS_DIR" --include="*.md" | \
    grep -o "[0-9]\{4\}-[0-9]\{2\}-[0-9]\{2\}" | sort | uniq -c | sort -nr | head -10 > "$temp_time_file"
    
    cat "$temp_time_file" >> "$REPORT_FILE"
    rm -f "$temp_time_file"
    
    echo '```' >> "$REPORT_FILE"
    
    log_success "内容一致性检查完成"
}

# 3. 重复内容检测
detect_duplicates() {
    log_info "开始重复内容检测..."
    
    echo "" >> "$REPORT_FILE"
    echo "### 1.3 重复内容分析" >> "$REPORT_FILE"
    
    # 检查重复的文件名
    echo "" >> "$REPORT_FILE"
    echo "**重复文件名检查**:" >> "$REPORT_FILE"
    
    local duplicate_files=$(find "$PROMPTS_DIR" -name "*.md" -exec basename {} \; | sort | uniq -d)
    if [[ -n "$duplicate_files" ]]; then
        echo "" >> "$REPORT_FILE"
        echo '```' >> "$REPORT_FILE"
        echo "$duplicate_files" >> "$REPORT_FILE"
        echo '```' >> "$REPORT_FILE"
        log_warning "发现重复的文件名"
    else
        echo "" >> "$REPORT_FILE"
        echo "✓ 未发现重复文件名" >> "$REPORT_FILE"
    fi
    
    # 检查相似的章节标题
    echo "" >> "$REPORT_FILE"
    echo "**高频章节标题 (可能重复)**:" >> "$REPORT_FILE"
    echo "" >> "$REPORT_FILE"
    echo '```' >> "$REPORT_FILE"
    
    local temp_section_file="./outputs/temp_section_stats.txt"
    grep -r "^## " "$PROMPTS_DIR" --include="*.md" | \
    cut -d: -f2 | sort | uniq -c | sort -nr | head -15 > "$temp_section_file"
    
    cat "$temp_section_file" >> "$REPORT_FILE"
    rm -f "$temp_section_file"
    
    echo '```' >> "$REPORT_FILE"
    
    log_success "重复内容检测完成"
}

# 4. 模块质量评分
module_quality_scoring() {
    log_info "开始模块质量评分..."
    
    echo "" >> "$REPORT_FILE"
    echo "## 2. 模块质量评分" >> "$REPORT_FILE"
    echo "" >> "$REPORT_FILE"
    echo "| 模块 | 文档完整性 | 功能清晰度 | 可维护性 | 总分 | 等级 |" >> "$REPORT_FILE"
    echo "|------|------------|------------|----------|------|------|" >> "$REPORT_FILE"
    
    local total_score=0
    local module_count=0
    
    find "$PROMPTS_DIR" -name "*.md" | while read file; do
        local filename=$(basename "$file")
        
        # 文档完整性评分 (1-4)
        local doc_score=1
        grep -q "^version:" "$file" && ((doc_score++))
        grep -q "^description:" "$file" && ((doc_score++))
        grep -q "^# " "$file" && ((doc_score++))
        
        # 功能清晰度评分 (1-4)
        local clarity_score=1
        grep -q "## " "$file" && ((clarity_score++))
        grep -q "\`\`\`" "$file" && ((clarity_score++))
        grep -q "示例\|例子\|用法" "$file" && ((clarity_score++))
        
        # 可维护性评分 (1-4)
        local maintain_score=1
        local line_count=$(wc -l < "$file")
        [[ $line_count -lt 200 ]] && ((maintain_score++))
        grep -q "错误\|异常" "$file" && ((maintain_score++))
        grep -q "注意\|提示" "$file" && ((maintain_score++))
        
        local total=$((doc_score + clarity_score + maintain_score))
        local grade="需改进"
        [[ $total -ge 9 ]] && grade="优秀"
        [[ $total -ge 7 ]] && [[ $total -lt 9 ]] && grade="良好"
        [[ $total -ge 5 ]] && [[ $total -lt 7 ]] && grade="一般"
        
        echo "| $filename | $doc_score/4 | $clarity_score/4 | $maintain_score/4 | $total/12 | $grade |" >> "$REPORT_FILE"
        
        if [[ $total -lt 7 ]]; then
            log_warning "$filename 质量评分较低: $total/12"
        fi
        
        total_score=$((total_score + total))
        ((module_count++))
    done
    
    log_success "模块质量评分完成"
}

# 5. 依赖关系分析
analyze_dependencies() {
    log_info "开始依赖关系分析..."
    
    echo "" >> "$REPORT_FILE"
    echo "## 3. 模块依赖关系分析" >> "$REPORT_FILE"
    echo "" >> "$REPORT_FILE"
    echo "### 3.1 模块间引用关系" >> "$REPORT_FILE"
    echo "" >> "$REPORT_FILE"
    echo '```' >> "$REPORT_FILE"
    
    # 查找模块间的引用关系
    find "$PROMPTS_DIR" -name "*.md" -exec grep -l "参考\|引用\|调用\|使用.*技能" {} \; | \
    while read file; do
        echo "=== $(basename "$file") ===" >> "$REPORT_FILE"
        grep -n "参考\|引用\|调用\|使用.*技能" "$file" | head -5 >> "$REPORT_FILE"
        echo "" >> "$REPORT_FILE"
    done
    
    echo '```' >> "$REPORT_FILE"
    
    log_success "依赖关系分析完成"
}

# 6. 生成改进建议
generate_recommendations() {
    log_info "生成改进建议..."
    
    echo "" >> "$REPORT_FILE"
    echo "## 4. 改进建议" >> "$REPORT_FILE"
    
    echo "" >> "$REPORT_FILE"
    echo "### 4.1 高优先级改进项" >> "$REPORT_FILE"
    
    if [[ $ERROR_COUNT -gt 0 ]]; then
        echo "- 🔴 **立即修复**: 发现 $ERROR_COUNT 个严重问题需要立即处理" >> "$REPORT_FILE"
    fi
    
    if [[ $WARNING_COUNT -gt 5 ]]; then
        echo "- 🟡 **计划改进**: 发现 $WARNING_COUNT 个警告项，建议在下次迭代中处理" >> "$REPORT_FILE"
    fi
    
    echo "" >> "$REPORT_FILE"
    echo "### 4.2 系统优化建议" >> "$REPORT_FILE"
    echo "- 建立术语词典，统一关键概念的表达方式" >> "$REPORT_FILE"
    echo "- 创建模块模板，确保新模块符合质量标准" >> "$REPORT_FILE"
    echo "- 实施定期审查机制，每月进行一次质量检查" >> "$REPORT_FILE"
    echo "- 建立模块间接口标准，减少隐性依赖" >> "$REPORT_FILE"
    
    log_success "改进建议生成完成"
}

# 7. 生成执行摘要
generate_summary() {
    log_info "生成执行摘要..."
    
    local module_count=$(find "$PROMPTS_DIR" -name '*.md' | wc -l)
    local status="✓ 通过"
    local action="进行常规维护即可"
    
    if [[ $ERROR_COUNT -gt 0 ]]; then
        status="✗ 需要修复"
    fi
    
    if [[ $WARNING_COUNT -gt 5 ]]; then
        action="建议进行系统性重构"
    fi
    
    local summary="- **总模块数**: $module_count\n- **发现问题**: $ERROR_COUNT 个错误, $WARNING_COUNT 个警告\n- **审查状态**: $status\n- **建议行动**: $action"
    
    # 替换摘要占位符
    sed -i '' "s/SUMMARY_PLACEHOLDER/$summary/g" "$REPORT_FILE"
    
    log_success "执行摘要生成完成"
}

# 主函数
main() {
    log_info "开始提示词系统质量审查..."
    log_info "审查目录: $PROMPTS_DIR"
    log_info "报告文件: $REPORT_FILE"
    
    # 检查目录是否存在
    if [[ ! -d "$PROMPTS_DIR" ]]; then
        log_error "提示词目录不存在: $PROMPTS_DIR"
        exit 1
    fi
    
    # 初始化报告
    init_report
    
    # 执行各项检查
    validate_file_structure
    check_content_consistency
    detect_duplicates
    module_quality_scoring
    analyze_dependencies
    generate_recommendations
    generate_summary
    
    # 输出结果
    echo "" >> "$REPORT_FILE"
    echo "---" >> "$REPORT_FILE"
    echo "*报告生成时间: $(date)*" >> "$REPORT_FILE"
    
    log_info "审查完成!"
    log_info "详细报告: $REPORT_FILE"
    
    if [[ $ERROR_COUNT -eq 0 ]]; then
        log_success "✓ 系统质量检查通过"
        exit 0
    else
        log_error "✗ 发现 $ERROR_COUNT 个严重问题需要修复"
        exit 1
    fi
}

# 脚本入口
if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
    main "$@"
fi