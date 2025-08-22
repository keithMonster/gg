# 数据分析与报告生成技能

## 描述
专门用于数据分析、处理和报告生成的技能，包括数据清洗、统计分析、可视化和报告输出。

## 核心能力
- 数据收集和清洗
- 统计分析和数据挖掘
- 数据可视化
- 报告生成和格式化
- 趋势分析和预测
- 数据质量评估
- 自动化报告流程

## 适用场景
- 业务数据分析
- 用户行为分析
- 性能指标报告
- 财务数据分析
- 市场研究报告
- 运营数据监控

## 技术栈
- Python (pandas, numpy, matplotlib, seaborn)
- R语言
- SQL数据库查询
- Excel/Google Sheets
- Tableau/Power BI
- Jupyter Notebook

## 示例代码
```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

def generate_user_analysis_report(data_file):
    # 读取数据
    df = pd.read_csv(data_file)
    
    # 数据清洗
    df = df.dropna()
    df['date'] = pd.to_datetime(df['date'])
    
    # 基础统计
    total_users = len(df)
    active_users = len(df[df['status'] == 'active'])
    
    # 生成可视化
    plt.figure(figsize=(12, 8))
    
    # 用户状态分布
    plt.subplot(2, 2, 1)
    df['status'].value_counts().plot(kind='pie', autopct='%1.1f%%')
    plt.title('用户状态分布')
    
    # 用户注册趋势
    plt.subplot(2, 2, 2)
    df.groupby(df['date'].dt.date).size().plot()
    plt.title('用户注册趋势')
    plt.xticks(rotation=45)
    
    # 年龄分布
    plt.subplot(2, 2, 3)
    df['age'].hist(bins=20)
    plt.title('用户年龄分布')
    plt.xlabel('年龄')
    plt.ylabel('人数')
    
    # 地区分布
    plt.subplot(2, 2, 4)
    df['region'].value_counts().head(10).plot(kind='bar')
    plt.title('用户地区分布(Top 10)')
    plt.xticks(rotation=45)
    
    plt.tight_layout()
    plt.savefig('user_analysis_report.png', dpi=300, bbox_inches='tight')
    
    # 生成报告
    report = f"""
    # 用户数据分析报告
    
    生成时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
    
    ## 概览
    - 总用户数: {total_users:,}
    - 活跃用户数: {active_users:,}
    - 活跃率: {active_users/total_users*100:.1f}%
    
    ## 详细分析
    ### 用户状态分布
    {df['status'].value_counts().to_string()}
    
    ### 年龄统计
    - 平均年龄: {df['age'].mean():.1f}岁
    - 年龄中位数: {df['age'].median():.1f}岁
    - 年龄范围: {df['age'].min()}-{df['age'].max()}岁
    
    ### 地区分布
    {df['region'].value_counts().head().to_string()}
    """
    
    with open('user_analysis_report.md', 'w', encoding='utf-8') as f:
        f.write(report)
    
    return report
```

## 最佳实践
1. 数据质量检查和清洗
2. 选择合适的可视化类型
3. 提供清晰的数据解释
4. 自动化重复性分析任务
5. 保护数据隐私和安全