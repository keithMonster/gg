#!/bin/bash
# simple_audit.sh - 简化版提示词系统质量审查
# Author: gg (v9.2.4 evolution)

set -e

PROMPTS_DIR="./prompts"
REPORT_FILE="./outputs/simple_audit_$(date +%Y%m%d_%H%M%S).md"

echo "# 提示词系统简化审查报告" > "$REPORT_FILE"
echo "" >> "$REPORT_FILE"
echo "**生成时间**: $(date '+%Y-%m-%d %H:%M:%S')" >> "$REPORT_FILE"
echo "**审查范围**: $PROMPTS_DIR" >> "$REPORT_FILE"
echo "" >> "$REPORT_FILE"

echo "## 1. 模块统计" >> "$REPORT_FILE"
echo "" >> "$REPORT_FILE"

# 统计模块数量
module_count=$(find "$PROMPTS_DIR" -name "*.md" | wc -l | tr -d ' ')
echo "- **总模块数**: $module_count" >> "$REPORT_FILE"

# 检查元数据完整性
echo "" >> "$REPORT_FILE"
echo "## 2. 元数据检查" >> "$REPORT_FILE"
echo "" >> "$REPORT_FILE"
echo "| 文件 | version | author | description |" >> "$REPORT_FILE"
echo "|------|---------|--------|-------------|" >> "$REPORT_FILE"

find "$PROMPTS_DIR" -name "*.md" | while read file; do
    filename=$(basename "$file")
    has_version="✗"
    has_author="✗"
    has_description="✗"
    
    if grep -q "^version:" "$file"; then
        has_version="✓"
    fi
    
    if grep -q "^author:" "$file"; then
        has_author="✓"
    fi
    
    if grep -q "^description:" "$file"; then
        has_description="✓"
    fi
    
    echo "| $filename | $has_version | $has_author | $has_description |" >> "$REPORT_FILE"
done

echo "" >> "$REPORT_FILE"
echo "## 3. 质量评分" >> "$REPORT_FILE"
echo "" >> "$REPORT_FILE"
echo "| 模块 | 结构完整性 | 内容丰富度 | 总分 |" >> "$REPORT_FILE"
echo "|------|------------|------------|------|" >> "$REPORT_FILE"

find "$PROMPTS_DIR" -name "*.md" | while read file; do
    filename=$(basename "$file")
    score=0
    
    # 检查基本结构
    grep -q "^# " "$file" && ((score++))
    grep -q "^## " "$file" && ((score++))
    grep -q "^version:" "$file" && ((score++))
    
    # 检查内容丰富度
    grep -q "示例\|例子" "$file" && ((score++))
    grep -q '```' "$file" && ((score++))
    
    echo "| $filename | $score/3 | $((score-3 > 0 ? score-3 : 0))/2 | $score/5 |" >> "$REPORT_FILE"
done

echo "" >> "$REPORT_FILE"
echo "## 4. 改进建议" >> "$REPORT_FILE"
echo "" >> "$REPORT_FILE"
echo "- 确保所有模块包含完整的元数据（version, author, description）" >> "$REPORT_FILE"
echo "- 添加更多使用示例和代码块" >> "$REPORT_FILE"
echo "- 建立统一的文档结构标准" >> "$REPORT_FILE"
echo "- 实施定期质量检查机制" >> "$REPORT_FILE"

echo "" >> "$REPORT_FILE"
echo "---" >> "$REPORT_FILE"
echo "*报告生成完成: $(date)*" >> "$REPORT_FILE"

echo "✓ 审查完成，报告已生成: $REPORT_FILE"
echo "✓ 发现 $module_count 个模块"