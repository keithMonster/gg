---
version: 1.0.0
author: gg (v9.2.4 evolution)
description: "提示词系统审查与重构技能 - 系统性管理大规模提示词库的质量保证和模块化重构方案"
created: 2025-08-14
---

# 提示词系统审查与重构技能 (Prompt System Audit & Refactoring)

## 1. 核心挑战与解决思路

### 1.1 大规模提示词系统面临的挑战
- **模块依赖复杂性**: 模块间隐性依赖关系难以追踪
- **内容一致性**: 不同模块间概念、术语、格式的一致性
- **功能重叠**: 多个模块可能包含相似或重复的功能
- **质量参差不齐**: 不同时期创建的模块质量标准不统一
- **维护成本**: 随着模块增长，维护和更新成本指数级增长

### 1.2 解决方案架构
基于模块化提示工程最佳实践，采用**分层审查 + 自动化验证 + 持续重构**的三维管理框架。

## 2. 分层审查框架 (Layered Audit Framework)

### 2.1 架构层审查 (Architecture Layer)
**目标**: 确保整体系统架构的合理性和可扩展性

**审查维度**:
- **模块分类**: 按功能域重新分类（核心系统、技能模块、工具模块、配置模块）
- **依赖关系**: 绘制模块依赖图，识别循环依赖和过度耦合
- **接口标准**: 检查模块间接口的一致性和标准化程度
- **扩展性**: 评估新增模块的便利性和对现有系统的影响

**审查工具**:
```bash
# 模块依赖分析脚本
find /prompts -name "*.md" -exec grep -l "参考\|引用\|调用" {} \; | \
while read file; do
    echo "=== $file ==="
    grep -n "参考\|引用\|调用" "$file"
done
```

### 2.2 模块层审查 (Module Layer)
**目标**: 确保每个模块的内部质量和功能完整性

**审查清单**:
- [ ] **元数据完整性**: version, author, description, created/updated
- [ ] **功能边界清晰**: 单一职责原则，避免功能泛化
- [ ] **文档结构**: 标准化的章节结构和格式
- [ ] **示例完整性**: 包含足够的使用示例和边界案例
- [ ] **错误处理**: 明确的错误处理和异常情况说明

**质量评分矩阵**:
| 维度 | 优秀(4) | 良好(3) | 一般(2) | 需改进(1) |
|------|---------|---------|---------|----------|
| 文档完整性 | 所有必需元素齐全 | 缺少1-2个次要元素 | 缺少重要元素 | 严重不完整 |
| 功能清晰度 | 职责明确，边界清晰 | 基本清晰，有小幅重叠 | 职责模糊 | 功能混乱 |
| 可维护性 | 结构清晰，易于修改 | 结构较好 | 结构一般 | 难以维护 |

### 2.3 内容层审查 (Content Layer)
**目标**: 确保内容的准确性、一致性和实用性

**审查维度**:
- **术语一致性**: 跨模块术语使用的统一性
- **格式标准**: Markdown格式、代码块、引用格式的一致性
- **内容时效性**: 技术信息的时效性和准确性
- **实用性验证**: 通过实际测试验证指令的可执行性

## 3. 自动化验证系统 (Automated Validation System)

### 3.1 静态分析工具
**文件结构验证**:
```bash
#!/bin/bash
# prompt_structure_validator.sh

validate_prompt_file() {
    local file="$1"
    local errors=0
    
    # 检查必需的元数据
    if ! grep -q "^version:" "$file"; then
        echo "ERROR: Missing version in $file"
        ((errors++))
    fi
    
    if ! grep -q "^author:" "$file"; then
        echo "ERROR: Missing author in $file"
        ((errors++))
    fi
    
    if ! grep -q "^description:" "$file"; then
        echo "ERROR: Missing description in $file"
        ((errors++))
    fi
    
    # 检查标题结构
    if ! grep -q "^# " "$file"; then
        echo "ERROR: Missing main title in $file"
        ((errors++))
    fi
    
    return $errors
}

# 批量验证
find /prompts -name "*.md" | while read file; do
    validate_prompt_file "$file"
done
```

**内容一致性检查**:
```bash
#!/bin/bash
# content_consistency_checker.sh

# 术语一致性检查
check_terminology() {
    echo "=== 术语使用统计 ==="
    # 检查常见术语的不同表达方式
    grep -r "智能体\|AI智能体\|AI助手\|助手" /prompts --include="*.md" | \
    cut -d: -f2 | sort | uniq -c | sort -nr
    
    echo "\n=== 时间格式统计 ==="
    grep -r "[0-9]\{4\}-[0-9]\{2\}-[0-9]\{2\}" /prompts --include="*.md" | \
    grep -o "[0-9]\{4\}-[0-9]\{2\}-[0-9]\{2\}" | sort | uniq -c
}

# 重复内容检测
detect_duplicates() {
    echo "=== 潜在重复内容检测 ==="
    find /prompts -name "*.md" -exec basename {} \; | sort | uniq -d
    
    # 检查相似的章节标题
    grep -r "^## " /prompts --include="*.md" | \
    cut -d: -f2 | sort | uniq -c | sort -nr | head -20
}
```

### 3.2 功能测试框架
**模块功能验证**:
```bash
#!/bin/bash
# module_function_tester.sh

# 测试模块的基本功能
test_module_functionality() {
    local module_path="$1"
    local module_name=$(basename "$module_path" .md)
    
    echo "Testing module: $module_name"
    
    # 检查是否有示例代码
    if grep -q "```" "$module_path"; then
        echo "✓ Contains code examples"
    else
        echo "✗ Missing code examples"
    fi
    
    # 检查是否有使用说明
    if grep -q "使用\|用法\|示例\|例子" "$module_path"; then
        echo "✓ Contains usage instructions"
    else
        echo "✗ Missing usage instructions"
    fi
    
    # 检查是否有错误处理说明
    if grep -q "错误\|异常\|失败\|问题" "$module_path"; then
        echo "✓ Contains error handling"
    else
        echo "✗ Missing error handling"
    fi
}
```

## 4. 持续重构策略 (Continuous Refactoring Strategy)

### 4.1 重构优先级矩阵
基于**影响范围 × 修改复杂度**的二维矩阵确定重构优先级：

| 影响范围\复杂度 | 低复杂度 | 中复杂度 | 高复杂度 |
|----------------|----------|----------|----------|
| **高影响** | 🔴 立即重构 | 🟡 计划重构 | 🟠 谨慎重构 |
| **中影响** | 🟢 批量重构 | 🟡 计划重构 | 🟠 评估重构 |
| **低影响** | 🟢 维护重构 | 🟢 维护重构 | ⚪ 暂缓重构 |

### 4.2 重构执行流程
**阶段1: 预重构分析**
1. **影响分析**: 识别重构对其他模块的潜在影响
2. **备份策略**: 创建重构前的完整备份
3. **测试计划**: 制定重构后的验证测试计划
4. **回滚方案**: 准备重构失败时的回滚策略

**阶段2: 渐进式重构**
1. **小步快跑**: 将大型重构分解为多个小步骤
2. **增量验证**: 每个步骤后立即进行功能验证
3. **版本控制**: 每个重构步骤独立提交
4. **文档同步**: 同步更新相关文档和changelog

**阶段3: 后重构验证**
1. **功能测试**: 运行完整的功能测试套件
2. **集成测试**: 验证与其他模块的集成效果
3. **性能测试**: 确保重构未影响系统性能
4. **用户验收**: 通过实际使用验证重构效果

### 4.3 重构模式库
**常见重构模式**:

1. **模块拆分 (Module Split)**
   - 适用场景: 单个模块功能过于复杂
   - 执行步骤: 识别功能边界 → 创建新模块 → 迁移功能 → 更新引用

2. **模块合并 (Module Merge)**
   - 适用场景: 多个小模块功能高度相关
   - 执行步骤: 分析依赖关系 → 设计合并结构 → 内容整合 → 清理冗余

3. **接口标准化 (Interface Standardization)**
   - 适用场景: 模块间接口不一致
   - 执行步骤: 定义标准接口 → 逐步迁移 → 验证兼容性 → 清理旧接口

4. **内容去重 (Content Deduplication)**
   - 适用场景: 多个模块包含重复内容
   - 执行步骤: 识别重复内容 → 提取公共模块 → 建立引用关系 → 清理重复

## 5. 实施计划与工具集成

### 5.1 审查执行计划
**第一阶段: 基础设施建设 (1-2天)**
- 创建自动化验证脚本
- 建立质量评分体系
- 设置持续集成检查

**第二阶段: 全面审查 (3-5天)**
- 执行架构层审查
- 完成模块层质量评估
- 进行内容层一致性检查

**第三阶段: 重构实施 (根据发现的问题确定)**
- 按优先级矩阵执行重构
- 持续验证和测试
- 更新文档和变更记录

### 5.2 工具集成方案
**Git Hooks集成**:
```bash
#!/bin/bash
# .git/hooks/pre-commit
# 提交前自动运行质量检查

echo "Running prompt system quality checks..."

# 运行结构验证
./scripts/prompt_structure_validator.sh
if [ $? -ne 0 ]; then
    echo "Structure validation failed. Commit aborted."
    exit 1
fi

# 运行内容一致性检查
./scripts/content_consistency_checker.sh

echo "Quality checks passed. Proceeding with commit."
```

**持续监控**:
```bash
#!/bin/bash
# scripts/daily_health_check.sh
# 每日系统健康检查

echo "=== Daily Prompt System Health Check ==="
echo "Date: $(date)"

# 统计模块数量
echo "Total modules: $(find /prompts -name '*.md' | wc -l)"

# 检查最近修改
echo "Recently modified:"
find /prompts -name '*.md' -mtime -7 -exec ls -la {} \;

# 运行质量检查
./scripts/prompt_structure_validator.sh > /tmp/health_check.log 2>&1
if [ $? -eq 0 ]; then
    echo "✓ All modules pass structure validation"
else
    echo "✗ Some modules have structure issues"
    cat /tmp/health_check.log
fi
```

## 6. 成功指标与持续改进

### 6.1 关键绩效指标 (KPIs)
- **模块质量分数**: 平均质量评分 > 3.5/4.0
- **一致性指标**: 术语一致性 > 90%
- **维护效率**: 新模块创建时间 < 30分钟
- **错误率**: 模块功能错误率 < 5%
- **用户满意度**: 基于实际使用效果的反馈评分

### 6.2 持续改进机制
- **月度审查**: 每月进行一次全面的系统健康检查
- **季度重构**: 每季度执行一次重点重构项目
- **年度架构评估**: 每年评估整体架构的适应性
- **反馈循环**: 建立用户反馈到系统改进的闭环机制

通过这套完整的审查与重构体系，gg系统能够在规模增长的同时保持高质量和高效率，确保每个模块都能准确、完善地发挥其应有的作用。