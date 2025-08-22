#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
gg智能体用户体验优化系统

功能:
- 分析用户交互模式
- 收集用户反馈和满意度
- 生成UX改进建议
- 优化响应时间和交互流程
- 个性化用户体验
"""

import json
import time
import re
from datetime import datetime, timedelta
from pathlib import Path
from typing import Dict, List, Optional, Any, Tuple
from dataclasses import dataclass, asdict
from collections import defaultdict, Counter
from enum import Enum

class InteractionType(Enum):
    """交互类型枚举"""
    COMMAND = "command"
    QUESTION = "question"
    REQUEST = "request"
    FEEDBACK = "feedback"
    ERROR = "error"

class SatisfactionLevel(Enum):
    """满意度级别"""
    VERY_DISSATISFIED = 1
    DISSATISFIED = 2
    NEUTRAL = 3
    SATISFIED = 4
    VERY_SATISFIED = 5

@dataclass
class UserInteraction:
    """用户交互记录"""
    interaction_id: str
    timestamp: str
    user_input: str
    interaction_type: str
    response_time_ms: float
    success: bool
    error_message: Optional[str]
    user_satisfaction: Optional[int]
    context: Dict[str, Any]
    session_id: str

@dataclass
class UXMetric:
    """用户体验指标"""
    metric_name: str
    value: float
    unit: str
    timestamp: str
    context: Dict[str, Any]

@dataclass
class UXRecommendation:
    """UX改进建议"""
    recommendation_id: str
    category: str
    priority: str  # high, medium, low
    title: str
    description: str
    expected_impact: str
    implementation_effort: str
    metrics_to_improve: List[str]
    created_at: str

class UXOptimizer:
    """用户体验优化器"""
    
    def __init__(self, config_path: str = "config/ux_config.json"):
        self.config_path = Path(config_path)
        self.ux_dir = Path("ux_data")
        self.ux_dir.mkdir(exist_ok=True)
        
        # 加载配置
        self.config = self.load_config()
        
        # 数据存储
        self.interactions: List[UserInteraction] = []
        self.metrics: List[UXMetric] = []
        self.session_id = f"session_{int(time.time())}"
        
        # 分析缓存
        self.analysis_cache = {}
        self.last_analysis_time = None
    
    def load_config(self) -> Dict[str, Any]:
        """加载配置文件"""
        if self.config_path.exists():
            with open(self.config_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        else:
            # 默认配置
            default_config = {
                "response_time_targets": {
                    "excellent": 1000,  # ms
                    "good": 3000,
                    "acceptable": 5000
                },
                "satisfaction_thresholds": {
                    "high": 4.0,
                    "medium": 3.0,
                    "low": 2.0
                },
                "interaction_patterns": {
                    "max_session_length_minutes": 60,
                    "ideal_interactions_per_session": 10,
                    "max_error_rate": 0.1
                },
                "personalization": {
                    "enable_adaptive_responses": True,
                    "track_user_preferences": True,
                    "customize_interaction_style": True
                },
                "analysis_intervals": {
                    "real_time_minutes": 5,
                    "daily_analysis": True,
                    "weekly_report": True
                }
            }
            
            # 保存默认配置
            self.config_path.parent.mkdir(exist_ok=True)
            with open(self.config_path, 'w', encoding='utf-8') as f:
                json.dump(default_config, f, indent=2, ensure_ascii=False)
            return default_config
    
    def record_interaction(self, 
                          user_input: str,
                          response_time_ms: float,
                          success: bool = True,
                          error_message: Optional[str] = None,
                          user_satisfaction: Optional[int] = None,
                          context: Optional[Dict] = None) -> str:
        """记录用户交互"""
        
        interaction_id = f"int_{int(time.time() * 1000)}"
        interaction_type = self._classify_interaction(user_input)
        
        interaction = UserInteraction(
            interaction_id=interaction_id,
            timestamp=datetime.now().isoformat(),
            user_input=user_input,
            interaction_type=interaction_type.value,
            response_time_ms=response_time_ms,
            success=success,
            error_message=error_message,
            user_satisfaction=user_satisfaction,
            context=context or {},
            session_id=self.session_id
        )
        
        self.interactions.append(interaction)
        
        # 实时分析
        self._update_real_time_metrics(interaction)
        
        # 保存到文件
        self._save_interaction(interaction)
        
        return interaction_id
    
    def _classify_interaction(self, user_input: str) -> InteractionType:
        """分类用户交互类型"""
        user_input_lower = user_input.lower().strip()
        
        # 命令模式
        if any(user_input_lower.startswith(cmd) for cmd in ['/', '!', 'run', 'execute', '执行']):
            return InteractionType.COMMAND
        
        # 问题模式
        if any(word in user_input_lower for word in ['?', '？', 'how', 'what', 'why', 'when', 'where', '如何', '什么', '为什么', '怎么']):
            return InteractionType.QUESTION
        
        # 反馈模式
        if any(word in user_input_lower for word in ['feedback', 'suggest', 'improve', '反馈', '建议', '改进']):
            return InteractionType.FEEDBACK
        
        # 错误模式
        if any(word in user_input_lower for word in ['error', 'bug', 'problem', 'issue', '错误', '问题', '故障']):
            return InteractionType.ERROR
        
        # 默认为请求
        return InteractionType.REQUEST
    
    def _update_real_time_metrics(self, interaction: UserInteraction):
        """更新实时指标"""
        timestamp = datetime.now().isoformat()
        
        # 响应时间指标
        self.metrics.append(UXMetric(
            metric_name="response_time",
            value=interaction.response_time_ms,
            unit="milliseconds",
            timestamp=timestamp,
            context={"interaction_type": interaction.interaction_type}
        ))
        
        # 成功率指标
        self.metrics.append(UXMetric(
            metric_name="success_rate",
            value=1.0 if interaction.success else 0.0,
            unit="boolean",
            timestamp=timestamp,
            context={"interaction_type": interaction.interaction_type}
        ))
        
        # 满意度指标
        if interaction.user_satisfaction is not None:
            self.metrics.append(UXMetric(
                metric_name="user_satisfaction",
                value=float(interaction.user_satisfaction),
                unit="rating",
                timestamp=timestamp,
                context={"interaction_type": interaction.interaction_type}
            ))
    
    def collect_feedback(self, 
                        interaction_id: str,
                        satisfaction: int,
                        feedback_text: Optional[str] = None,
                        suggestions: Optional[List[str]] = None) -> bool:
        """收集用户反馈"""
        
        # 验证满意度范围
        if not 1 <= satisfaction <= 5:
            return False
        
        # 查找对应的交互记录
        for interaction in self.interactions:
            if interaction.interaction_id == interaction_id:
                interaction.user_satisfaction = satisfaction
                break
        
        # 保存反馈数据
        feedback_data = {
            "interaction_id": interaction_id,
            "satisfaction": satisfaction,
            "feedback_text": feedback_text,
            "suggestions": suggestions or [],
            "timestamp": datetime.now().isoformat(),
            "session_id": self.session_id
        }
        
        feedback_file = self.ux_dir / "feedback.jsonl"
        with open(feedback_file, 'a', encoding='utf-8') as f:
            f.write(json.dumps(feedback_data, ensure_ascii=False) + '\n')
        
        return True
    
    def analyze_user_patterns(self, days: int = 7) -> Dict[str, Any]:
        """分析用户行为模式"""
        
        # 加载历史数据
        interactions = self._load_interactions(days)
        
        if not interactions:
            return {"error": "没有足够的数据进行分析"}
        
        analysis = {
            "analysis_period": {
                "days": days,
                "total_interactions": len(interactions),
                "analysis_time": datetime.now().isoformat()
            },
            "interaction_patterns": self._analyze_interaction_patterns(interactions),
            "performance_metrics": self._analyze_performance_metrics(interactions),
            "satisfaction_analysis": self._analyze_satisfaction(interactions),
            "error_analysis": self._analyze_errors(interactions),
            "session_analysis": self._analyze_sessions(interactions)
        }
        
        return analysis
    
    def _analyze_interaction_patterns(self, interactions: List[Dict]) -> Dict[str, Any]:
        """分析交互模式"""
        
        # 交互类型分布
        type_counter = Counter(i['interaction_type'] for i in interactions)
        
        # 时间分布分析
        hours = [datetime.fromisoformat(i['timestamp']).hour for i in interactions]
        hour_counter = Counter(hours)
        
        # 交互频率分析
        dates = [datetime.fromisoformat(i['timestamp']).date() for i in interactions]
        daily_counts = Counter(dates)
        
        return {
            "interaction_types": dict(type_counter),
            "peak_hours": dict(sorted(hour_counter.items(), key=lambda x: x[1], reverse=True)[:5]),
            "daily_interaction_counts": {str(k): v for k, v in daily_counts.items()},
            "avg_daily_interactions": sum(daily_counts.values()) / len(daily_counts) if daily_counts else 0
        }
    
    def _analyze_performance_metrics(self, interactions: List[Dict]) -> Dict[str, Any]:
        """分析性能指标"""
        
        response_times = [i['response_time_ms'] for i in interactions if i.get('response_time_ms')]
        success_rate = sum(1 for i in interactions if i.get('success', True)) / len(interactions)
        
        if not response_times:
            return {"error": "没有响应时间数据"}
        
        # 响应时间统计
        avg_response_time = sum(response_times) / len(response_times)
        max_response_time = max(response_times)
        min_response_time = min(response_times)
        
        # 响应时间分级
        targets = self.config['response_time_targets']
        excellent_count = sum(1 for rt in response_times if rt <= targets['excellent'])
        good_count = sum(1 for rt in response_times if targets['excellent'] < rt <= targets['good'])
        acceptable_count = sum(1 for rt in response_times if targets['good'] < rt <= targets['acceptable'])
        poor_count = sum(1 for rt in response_times if rt > targets['acceptable'])
        
        return {
            "response_time": {
                "average_ms": avg_response_time,
                "max_ms": max_response_time,
                "min_ms": min_response_time,
                "distribution": {
                    "excellent": excellent_count,
                    "good": good_count,
                    "acceptable": acceptable_count,
                    "poor": poor_count
                }
            },
            "success_rate": success_rate,
            "total_samples": len(interactions)
        }
    
    def _analyze_satisfaction(self, interactions: List[Dict]) -> Dict[str, Any]:
        """分析用户满意度"""
        
        satisfactions = [i['user_satisfaction'] for i in interactions if i.get('user_satisfaction')]
        
        if not satisfactions:
            return {"error": "没有满意度数据"}
        
        avg_satisfaction = sum(satisfactions) / len(satisfactions)
        satisfaction_counter = Counter(satisfactions)
        
        # 满意度分级
        thresholds = self.config['satisfaction_thresholds']
        high_satisfaction = sum(1 for s in satisfactions if s >= thresholds['high'])
        medium_satisfaction = sum(1 for s in satisfactions if thresholds['medium'] <= s < thresholds['high'])
        low_satisfaction = sum(1 for s in satisfactions if s < thresholds['medium'])
        
        return {
            "average_satisfaction": avg_satisfaction,
            "satisfaction_distribution": dict(satisfaction_counter),
            "satisfaction_levels": {
                "high": high_satisfaction,
                "medium": medium_satisfaction,
                "low": low_satisfaction
            },
            "total_ratings": len(satisfactions)
        }
    
    def _analyze_errors(self, interactions: List[Dict]) -> Dict[str, Any]:
        """分析错误模式"""
        
        errors = [i for i in interactions if not i.get('success', True)]
        error_rate = len(errors) / len(interactions) if interactions else 0
        
        if not errors:
            return {"error_rate": 0, "total_errors": 0}
        
        # 错误类型分析
        error_messages = [e.get('error_message', 'Unknown') for e in errors]
        error_counter = Counter(error_messages)
        
        # 错误时间分析
        error_hours = [datetime.fromisoformat(e['timestamp']).hour for e in errors]
        error_hour_counter = Counter(error_hours)
        
        return {
            "error_rate": error_rate,
            "total_errors": len(errors),
            "common_errors": dict(error_counter.most_common(5)),
            "error_peak_hours": dict(sorted(error_hour_counter.items(), key=lambda x: x[1], reverse=True)[:3])
        }
    
    def _analyze_sessions(self, interactions: List[Dict]) -> Dict[str, Any]:
        """分析会话模式"""
        
        # 按会话分组
        sessions = defaultdict(list)
        for interaction in interactions:
            sessions[interaction['session_id']].append(interaction)
        
        # 会话统计
        session_lengths = []
        session_durations = []
        
        for session_interactions in sessions.values():
            session_lengths.append(len(session_interactions))
            
            if len(session_interactions) > 1:
                start_time = datetime.fromisoformat(session_interactions[0]['timestamp'])
                end_time = datetime.fromisoformat(session_interactions[-1]['timestamp'])
                duration_minutes = (end_time - start_time).total_seconds() / 60
                session_durations.append(duration_minutes)
        
        avg_session_length = sum(session_lengths) / len(session_lengths) if session_lengths else 0
        avg_session_duration = sum(session_durations) / len(session_durations) if session_durations else 0
        
        return {
            "total_sessions": len(sessions),
            "avg_interactions_per_session": avg_session_length,
            "avg_session_duration_minutes": avg_session_duration,
            "session_length_distribution": dict(Counter(session_lengths))
        }
    
    def generate_ux_recommendations(self, analysis: Dict[str, Any]) -> List[UXRecommendation]:
        """生成UX改进建议"""
        
        recommendations = []
        
        # 基于响应时间的建议
        if 'performance_metrics' in analysis:
            perf = analysis['performance_metrics']
            if 'response_time' in perf:
                avg_time = perf['response_time']['average_ms']
                targets = self.config['response_time_targets']
                
                if avg_time > targets['acceptable']:
                    recommendations.append(UXRecommendation(
                        recommendation_id=f"perf_{int(time.time())}",
                        category="performance",
                        priority="high",
                        title="优化响应时间",
                        description=f"当前平均响应时间为{avg_time:.0f}ms，超过可接受阈值{targets['acceptable']}ms。建议优化算法和缓存机制。",
                        expected_impact="显著提升用户体验和满意度",
                        implementation_effort="medium",
                        metrics_to_improve=["response_time", "user_satisfaction"],
                        created_at=datetime.now().isoformat()
                    ))
        
        # 基于满意度的建议
        if 'satisfaction_analysis' in analysis:
            sat = analysis['satisfaction_analysis']
            if 'average_satisfaction' in sat:
                avg_sat = sat['average_satisfaction']
                thresholds = self.config['satisfaction_thresholds']
                
                if avg_sat < thresholds['medium']:
                    recommendations.append(UXRecommendation(
                        recommendation_id=f"sat_{int(time.time())}",
                        category="satisfaction",
                        priority="high",
                        title="提升用户满意度",
                        description=f"当前平均满意度为{avg_sat:.1f}，低于期望水平。建议改进交互流程和响应质量。",
                        expected_impact="提高用户留存和推荐率",
                        implementation_effort="high",
                        metrics_to_improve=["user_satisfaction", "success_rate"],
                        created_at=datetime.now().isoformat()
                    ))
        
        # 基于错误率的建议
        if 'error_analysis' in analysis:
            err = analysis['error_analysis']
            if err.get('error_rate', 0) > self.config['interaction_patterns']['max_error_rate']:
                recommendations.append(UXRecommendation(
                    recommendation_id=f"err_{int(time.time())}",
                    category="reliability",
                    priority="high",
                    title="降低错误率",
                    description=f"当前错误率为{err['error_rate']:.1%}，超过可接受水平。建议加强错误处理和输入验证。",
                    expected_impact="提高系统可靠性和用户信任",
                    implementation_effort="medium",
                    metrics_to_improve=["success_rate", "error_rate"],
                    created_at=datetime.now().isoformat()
                ))
        
        # 基于交互模式的建议
        if 'interaction_patterns' in analysis:
            patterns = analysis['interaction_patterns']
            ideal_interactions = self.config['interaction_patterns']['ideal_interactions_per_session']
            
            if 'avg_daily_interactions' in patterns:
                avg_daily = patterns['avg_daily_interactions']
                if avg_daily < ideal_interactions * 0.5:
                    recommendations.append(UXRecommendation(
                        recommendation_id=f"eng_{int(time.time())}",
                        category="engagement",
                        priority="medium",
                        title="提升用户参与度",
                        description=f"日均交互次数为{avg_daily:.1f}，低于理想水平。建议增加引导性提示和功能推荐。",
                        expected_impact="增加用户活跃度和使用频率",
                        implementation_effort="low",
                        metrics_to_improve=["interaction_frequency", "session_length"],
                        created_at=datetime.now().isoformat()
                    ))
        
        return recommendations
    
    def _load_interactions(self, days: int) -> List[Dict]:
        """加载历史交互数据"""
        interactions = []
        end_date = datetime.now()
        start_date = end_date - timedelta(days=days)
        
        # 加载当前会话的交互
        interactions.extend([asdict(i) for i in self.interactions])
        
        # 加载历史文件
        current_date = start_date.date()
        while current_date <= end_date.date():
            file_path = self.ux_dir / f"interactions_{current_date.strftime('%Y-%m-%d')}.jsonl"
            if file_path.exists():
                with open(file_path, 'r', encoding='utf-8') as f:
                    for line in f:
                        interaction_data = json.loads(line.strip())
                        interaction_time = datetime.fromisoformat(interaction_data['timestamp'])
                        if start_date <= interaction_time <= end_date:
                            interactions.append(interaction_data)
            current_date += timedelta(days=1)
        
        return interactions
    
    def _save_interaction(self, interaction: UserInteraction):
        """保存交互记录到文件"""
        date_str = datetime.now().strftime('%Y-%m-%d')
        file_path = self.ux_dir / f"interactions_{date_str}.jsonl"
        
        with open(file_path, 'a', encoding='utf-8') as f:
            f.write(json.dumps(asdict(interaction), ensure_ascii=False) + '\n')
    
    def get_ux_dashboard(self) -> Dict[str, Any]:
        """获取UX仪表板数据"""
        
        # 实时指标
        recent_interactions = self.interactions[-10:] if self.interactions else []
        
        dashboard = {
            "real_time_metrics": {
                "active_session": self.session_id,
                "recent_interactions": len(recent_interactions),
                "avg_response_time_ms": sum(i.response_time_ms for i in recent_interactions) / len(recent_interactions) if recent_interactions else 0,
                "success_rate": sum(1 for i in recent_interactions if i.success) / len(recent_interactions) if recent_interactions else 1.0
            },
            "daily_summary": self.analyze_user_patterns(days=1),
            "weekly_trends": self.analyze_user_patterns(days=7),
            "recommendations": []
        }
        
        # 生成建议
        if dashboard['weekly_trends'] and 'error' not in dashboard['weekly_trends']:
            recommendations = self.generate_ux_recommendations(dashboard['weekly_trends'])
            dashboard['recommendations'] = [asdict(rec) for rec in recommendations]
        
        return dashboard

# 全局UX优化器实例
_ux_optimizer = None

def get_ux_optimizer() -> UXOptimizer:
    """获取全局UX优化器实例"""
    global _ux_optimizer
    if _ux_optimizer is None:
        _ux_optimizer = UXOptimizer()
    return _ux_optimizer

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description="gg智能体用户体验优化系统")
    parser.add_argument('action', choices=['analyze', 'dashboard', 'feedback', 'recommendations'],
                       help='执行的操作')
    parser.add_argument('--days', type=int, default=7,
                       help='分析时间范围(天)')
    parser.add_argument('--output', type=str,
                       help='输出文件路径')
    parser.add_argument('--interaction-id', type=str,
                       help='交互ID(用于反馈)')
    parser.add_argument('--satisfaction', type=int, choices=[1,2,3,4,5],
                       help='满意度评分(1-5)')
    parser.add_argument('--feedback-text', type=str,
                       help='反馈文本')
    
    args = parser.parse_args()
    
    optimizer = UXOptimizer()
    
    if args.action == 'analyze':
        analysis = optimizer.analyze_user_patterns(days=args.days)
        
        if args.output:
            with open(args.output, 'w', encoding='utf-8') as f:
                json.dump(analysis, f, indent=2, ensure_ascii=False)
            print(f"分析结果已保存到: {args.output}")
        else:
            print(json.dumps(analysis, indent=2, ensure_ascii=False))
    
    elif args.action == 'dashboard':
        dashboard = optimizer.get_ux_dashboard()
        print(json.dumps(dashboard, indent=2, ensure_ascii=False))
    
    elif args.action == 'feedback':
        if not args.interaction_id or not args.satisfaction:
            print("错误: 需要提供 --interaction-id 和 --satisfaction 参数")
            exit(1)
        
        success = optimizer.collect_feedback(
            args.interaction_id,
            args.satisfaction,
            args.feedback_text
        )
        
        if success:
            print("反馈记录成功")
        else:
            print("反馈记录失败")
    
    elif args.action == 'recommendations':
        analysis = optimizer.analyze_user_patterns(days=args.days)
        if 'error' not in analysis:
            recommendations = optimizer.generate_ux_recommendations(analysis)
            
            if args.output:
                # 保存为JSON格式
                recommendations_dict = [asdict(rec) for rec in recommendations]
                with open(args.output, 'w', encoding='utf-8') as f:
                    json.dump(recommendations_dict, f, indent=2, ensure_ascii=False)
                print(f"建议已保存到: {args.output}")
            else:
                print(f"生成了 {len(recommendations)} 条改进建议:")
                for rec in recommendations:
                    print(f"\n[{rec.priority.upper()}] {rec.title}")
                    print(f"类别: {rec.category}")
                    print(f"描述: {rec.description}")
                    print(f"预期影响: {rec.expected_impact}")
        else:
            print("数据不足，无法生成建议")