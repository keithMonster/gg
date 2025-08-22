#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
gg智能体UX优化系统集成接口

提供简单的装饰器和上下文管理器，方便在其他脚本中集成UX监控功能。
"""

import time
import functools
from typing import Any, Callable, Optional, Dict
from contextlib import contextmanager
from ux_optimizer import get_ux_optimizer, UXOptimizer

class UXTracker:
    """UX跟踪器 - 简化的接口"""
    
    def __init__(self):
        self.optimizer = get_ux_optimizer()
        self._current_interaction_id = None
        self._start_time = None
    
    def start_interaction(self, user_input: str, context: Optional[Dict] = None) -> str:
        """开始一个交互跟踪"""
        self._start_time = time.time()
        self._current_interaction_id = f"temp_{int(self._start_time * 1000)}"
        return self._current_interaction_id
    
    def end_interaction(self, 
                       success: bool = True, 
                       error_message: Optional[str] = None,
                       user_satisfaction: Optional[int] = None,
                       context: Optional[Dict] = None) -> Optional[str]:
        """结束交互跟踪并记录"""
        if self._start_time is None:
            return None
        
        response_time_ms = (time.time() - self._start_time) * 1000
        
        # 这里需要用户输入，但在简化接口中我们使用占位符
        user_input = context.get('user_input', 'Unknown') if context else 'Unknown'
        
        interaction_id = self.optimizer.record_interaction(
            user_input=user_input,
            response_time_ms=response_time_ms,
            success=success,
            error_message=error_message,
            user_satisfaction=user_satisfaction,
            context=context
        )
        
        # 重置状态
        self._start_time = None
        self._current_interaction_id = None
        
        return interaction_id
    
    def record_quick_interaction(self,
                                user_input: str,
                                response_time_ms: float,
                                success: bool = True,
                                error_message: Optional[str] = None,
                                user_satisfaction: Optional[int] = None,
                                context: Optional[Dict] = None) -> str:
        """快速记录一个完整的交互"""
        return self.optimizer.record_interaction(
            user_input=user_input,
            response_time_ms=response_time_ms,
            success=success,
            error_message=error_message,
            user_satisfaction=user_satisfaction,
            context=context
        )
    
    def collect_feedback(self, 
                        interaction_id: str,
                        satisfaction: int,
                        feedback_text: Optional[str] = None) -> bool:
        """收集用户反馈"""
        return self.optimizer.collect_feedback(
            interaction_id=interaction_id,
            satisfaction=satisfaction,
            feedback_text=feedback_text
        )

# 全局跟踪器实例
_ux_tracker = None

def get_ux_tracker() -> UXTracker:
    """获取全局UX跟踪器实例"""
    global _ux_tracker
    if _ux_tracker is None:
        _ux_tracker = UXTracker()
    return _ux_tracker

def track_interaction(user_input: str = None, 
                     include_context: bool = True,
                     auto_success_detection: bool = True):
    """装饰器：自动跟踪函数执行的UX指标
    
    Args:
        user_input: 用户输入内容，如果为None则尝试从函数参数中获取
        include_context: 是否包含函数执行上下文
        auto_success_detection: 是否自动检测执行成功/失败
    """
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            tracker = get_ux_tracker()
            
            # 确定用户输入
            actual_user_input = user_input
            if actual_user_input is None:
                # 尝试从参数中获取
                if args:
                    actual_user_input = str(args[0])
                elif 'user_input' in kwargs:
                    actual_user_input = kwargs['user_input']
                elif 'input' in kwargs:
                    actual_user_input = kwargs['input']
                elif 'query' in kwargs:
                    actual_user_input = kwargs['query']
                else:
                    actual_user_input = f"Function call: {func.__name__}"
            
            # 准备上下文
            context = {
                'user_input': actual_user_input,
                'function_name': func.__name__,
                'module': func.__module__
            }
            
            if include_context:
                context.update({
                    'args_count': len(args),
                    'kwargs_keys': list(kwargs.keys())
                })
            
            # 开始跟踪
            start_time = time.time()
            success = True
            error_message = None
            result = None
            
            try:
                result = func(*args, **kwargs)
                return result
            except Exception as e:
                success = False
                error_message = str(e)
                raise
            finally:
                # 记录交互
                response_time_ms = (time.time() - start_time) * 1000
                
                if auto_success_detection and result is not None:
                    # 简单的成功检测逻辑
                    if isinstance(result, dict) and 'error' in result:
                        success = False
                        error_message = result.get('error')
                    elif isinstance(result, bool):
                        success = result
                
                tracker.record_quick_interaction(
                    user_input=actual_user_input,
                    response_time_ms=response_time_ms,
                    success=success,
                    error_message=error_message,
                    context=context
                )
        
        return wrapper
    return decorator

@contextmanager
def ux_monitoring_context(user_input: str, context: Optional[Dict] = None):
    """上下文管理器：监控代码块的UX指标
    
    Usage:
        with ux_monitoring_context("用户查询数据") as tracker:
            # 执行代码
            result = process_query()
            
            # 可选：设置满意度
            if result_is_good:
                tracker.set_satisfaction(4)
    """
    
    class ContextTracker:
        def __init__(self, tracker_instance, interaction_id):
            self.tracker = tracker_instance
            self.interaction_id = interaction_id
            self.satisfaction = None
            self.success = True
            self.error_message = None
        
        def set_satisfaction(self, satisfaction: int):
            """设置用户满意度"""
            self.satisfaction = satisfaction
        
        def set_error(self, error_message: str):
            """设置错误信息"""
            self.success = False
            self.error_message = error_message
        
        def set_success(self, success: bool):
            """设置成功状态"""
            self.success = success
    
    tracker = get_ux_tracker()
    start_time = time.time()
    
    # 创建上下文跟踪器
    context_tracker = ContextTracker(tracker, None)
    
    try:
        yield context_tracker
    except Exception as e:
        context_tracker.set_error(str(e))
        raise
    finally:
        # 记录交互
        response_time_ms = (time.time() - start_time) * 1000
        
        interaction_id = tracker.record_quick_interaction(
            user_input=user_input,
            response_time_ms=response_time_ms,
            success=context_tracker.success,
            error_message=context_tracker.error_message,
            user_satisfaction=context_tracker.satisfaction,
            context=context
        )
        
        context_tracker.interaction_id = interaction_id

# 便捷函数
def quick_feedback(interaction_id: str, satisfaction: int, feedback_text: str = None) -> bool:
    """快速提交反馈"""
    tracker = get_ux_tracker()
    return tracker.collect_feedback(interaction_id, satisfaction, feedback_text)

def get_ux_dashboard() -> Dict[str, Any]:
    """获取UX仪表板数据"""
    optimizer = get_ux_optimizer()
    return optimizer.get_ux_dashboard()

def analyze_ux_patterns(days: int = 7) -> Dict[str, Any]:
    """分析UX模式"""
    optimizer = get_ux_optimizer()
    return optimizer.analyze_user_patterns(days)

def get_ux_recommendations(days: int = 7) -> list:
    """获取UX改进建议"""
    optimizer = get_ux_optimizer()
    analysis = optimizer.analyze_user_patterns(days)
    
    if 'error' in analysis:
        return []
    
    return optimizer.generate_ux_recommendations(analysis)

# 示例使用
if __name__ == "__main__":
    # 示例1: 使用装饰器
    @track_interaction()
    def example_function(user_query: str):
        """示例函数"""
        time.sleep(0.1)  # 模拟处理时间
        return f"处理结果: {user_query}"
    
    # 示例2: 使用上下文管理器
    def example_with_context():
        with ux_monitoring_context("用户数据查询") as tracker:
            time.sleep(0.2)  # 模拟处理
            tracker.set_satisfaction(4)
            return "查询完成"
    
    # 示例3: 手动跟踪
    def example_manual_tracking():
        tracker = get_ux_tracker()
        
        interaction_id = tracker.record_quick_interaction(
            user_input="手动跟踪测试",
            response_time_ms=150.0,
            success=True
        )
        
        # 稍后收集反馈
        tracker.collect_feedback(interaction_id, 5, "很好的体验")
    
    # 运行示例
    print("运行UX跟踪示例...")
    
    # 测试装饰器
    result1 = example_function("测试查询1")
    print(f"装饰器结果: {result1}")
    
    # 测试上下文管理器
    result2 = example_with_context()
    print(f"上下文管理器结果: {result2}")
    
    # 测试手动跟踪
    example_manual_tracking()
    print("手动跟踪完成")
    
    # 获取仪表板
    dashboard = get_ux_dashboard()
    print(f"\n当前UX指标:")
    print(f"- 活跃会话: {dashboard['real_time_metrics']['active_session']}")
    print(f"- 最近交互数: {dashboard['real_time_metrics']['recent_interactions']}")
    print(f"- 平均响应时间: {dashboard['real_time_metrics']['avg_response_time_ms']:.1f}ms")
    print(f"- 成功率: {dashboard['real_time_metrics']['success_rate']:.1%}")