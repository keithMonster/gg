---
version: 1.0.0
author: gg (v9.3.4 evolution)
description: "引用格式规范技能。明确定义不同场景下的引用格式使用规则，确保对话回复和用户输出文档使用适当的格式，提升文档的可移植性和用户体验。"
category: content_creation
tags: [formatting, references, documentation, user_experience]
---

# 引用格式规范技能 (Reference Formatting Skill)

## 核心原则

### 场景区分原则
引用格式的选择必须基于输出的目标场景和受众：

1. **对话回复场景**: 使用Trae IDE专用的引用格式
2. **用户输出文档场景**: 使用标准通用格式
3. **内部工作记录场景**: 使用项目内部约定格式

## 格式规范详解

### 1. 对话回复场景 (Conversation Reply Context)

**适用情况**: 在与用户的对话交流中，我的回复消息内容

**使用格式**:
- **网络搜索引用**: `<mcreference link="{url}" index="{index}">{index}</mcreference>`
- **代码文件引用**: `<mcfile name="{filename}" path="{path}"></mcfile>`
- **代码符号引用**: `<mcsymbol name="{symbol}" filename="{file}" path="{path}" startline="{line}" type="{type}"></mcsymbol>`
- **URL引用**: `<mcurl name="{text}" url="{url}"></mcurl>`
- **文件夹引用**: `<mcfolder name="{name}" path="{path}"></mcfolder>`

**示例**:
```
根据<mcreference link="https://example.com" index="1">1</mcreference>的研究，我建议修改<mcfile name="config.js" path="/src/config.js"></mcfile>中的配置。
```

### 2. 用户输出文档场景 (User Output Document Context)

**适用情况**: 创建存储在`/outputs`目录下的用户文档，如文章、报告、简报等

**使用格式**:
- **网络链接**: `[链接文本](URL)`
- **内部链接**: `[文档标题](相对路径)`
- **脚注引用**: `文本内容[^1]` + `[^1]: 引用说明`
- **参考文献**: 使用标准学术格式或简化引用格式

**示例**:
```markdown
正如[阮一峰周刊第305期](https://www.ruanyifeng.com/blog/2024/06/weekly-issue-305.html)中所说，"编程语言提供的随机数，是伪随机数。"

更多信息请参考[Random.org官网](https://www.random.org/)。
```

### 3. 内部工作记录场景 (Internal Work Record Context)

**适用情况**: changelog.md、对话记录、内部文档等

**使用格式**:
- **版本引用**: `v{major}.{minor}.{patch}`
- **文件路径**: 使用反引号包围的相对路径
- **提交引用**: `commit {hash}`
- **日期格式**: `YYYY-MM-DD`

## 格式转换规则

### 从对话格式转换为文档格式

1. **mcreference → Markdown链接**:
   ```
   <mcreference link="https://example.com" index="1">1</mcreference>
   ↓
   [相关资源](https://example.com)
   ```

2. **mcurl → Markdown链接**:
   ```
   <mcurl name="官方文档" url="https://docs.example.com"></mcurl>
   ↓
   [官方文档](https://docs.example.com)
   ```

3. **mcfile → 文件路径引用**:
   ```
   <mcfile name="config.js" path="/src/config.js"></mcfile>
   ↓
   `config.js`文件 或 `/src/config.js`
   ```

## 质量检查清单

### 创建用户文档前的检查

- [ ] 确认输出目标：是对话回复还是用户文档？
- [ ] 检查所有链接是否使用了正确的格式
- [ ] 验证链接的可访问性和有效性
- [ ] 确保引用格式的一致性
- [ ] 测试文档在标准Markdown阅读器中的显示效果

### 常见错误识别

1. **格式混用错误**:
   - 在用户文档中使用`<mcreference>`标签
   - 在对话回复中使用不完整的Markdown链接

2. **链接失效错误**:
   - 使用过期或无效的URL
   - 内部链接路径错误

3. **格式不一致错误**:
   - 同一文档中混用不同的引用风格
   - 链接文本与实际内容不符

## 自动修正机制

### 检测规则

1. **扫描用户输出文档**:
   ```regex
   <mcreference.*?>.*?</mcreference>
   <mcurl.*?>.*?</mcurl>
   <mcfile.*?>.*?</mcfile>
   ```

2. **提取转换信息**:
   - 解析标签属性
   - 提取链接URL和显示文本
   - 生成对应的Markdown格式

3. **执行替换**:
   - 批量替换所有匹配的标签
   - 保持原有的语义和上下文
   - 验证转换结果的正确性

## 使用指南

### 执行步骤

1. **场景识别**: 明确当前任务的输出目标
2. **格式选择**: 根据场景选择合适的引用格式
3. **内容创建**: 使用选定格式创建内容
4. **质量检查**: 执行相应的检查清单
5. **错误修正**: 发现问题时及时修正

### 最佳实践

1. **预防优于修正**: 在创建内容时就使用正确格式
2. **保持一致性**: 同一文档内使用统一的引用风格
3. **用户优先**: 优先考虑用户的使用体验和文档的可移植性
4. **定期检查**: 对已创建的文档进行定期格式检查

## 技能边界

### 职责范围
- 引用格式的规范和转换
- 格式错误的识别和修正
- 不同场景下的格式选择指导

### 不包含内容
- 具体的内容创作
- 链接有效性的深度验证
- 复杂的文档结构设计

### 与其他技能的协作
- **content_deduplication**: 确保引用内容的多样性
- **documentation_standards**: 遵循整体文档规范
- **time_management**: 在时间相关的引用中保持一致性

---

**注意**: 此技能专注于格式规范，不涉及具体内容的创作或评估。在使用时应结合具体的内容创作技能，确保既符合格式要求又满足内容质量标准。