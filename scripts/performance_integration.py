#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
gg智能体性能监控集成接口

提供简单的装饰器和上下文管理器，方便在其他脚本中集成性能监控功能。
"""

import time
import functools
from contextlib import contextmanager
from typing import Optional, Any, Callable
from performance_monitor import get_monitor

class PerformanceTracker:
    """性能跟踪器"""
    
    def __init__(self):
        self.monitor = get_monitor()
        self.current_task_id = None
    
    def start_task_monitoring(self, task_id: str, task_type: str = "general") -> str:
        """开始任务监控"""
        self.current_task_id = self.monitor.start_task(task_id, task_type)
        return self.current_task_id
    
    def end_task_monitoring(self, success: bool = True, error_message: Optional[str] = None):
        """结束任务监控"""
        if self.current_task_id:
            self.monitor.end_task(self.current_task_id, success, error_message)
            self.current_task_id = None
    
    def record_metric(self, metric_type: str, value: float, unit: str = "count", context: Optional[dict] = None):
        """记录自定义指标"""
        self.monitor.record_metric(metric_type, value, unit, context)

# 全局跟踪器实例
_tracker = PerformanceTracker()

def monitor_task(task_type: str = "function", task_id: Optional[str] = None):
    """任务监控装饰器"""
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # 生成任务ID
            actual_task_id = task_id or f"{func.__name__}_{int(time.time() * 1000)}"
            
            # 开始监控
            _tracker.start_task_monitoring(actual_task_id, task_type)
            
            try:
                # 执行函数
                result = func(*args, **kwargs)
                
                # 成功结束监控
                _tracker.end_task_monitoring(success=True)
                
                return result
                
            except Exception as e:
                # 失败结束监控
                _tracker.end_task_monitoring(success=False, error_message=str(e))
                raise
        
        return wrapper
    return decorator

@contextmanager
def monitor_context(task_id: str, task_type: str = "context"):
    """性能监控上下文管理器"""
    _tracker.start_task_monitoring(task_id, task_type)
    
    try:
        yield _tracker
        _tracker.end_task_monitoring(success=True)
    except Exception as e:
        _tracker.end_task_monitoring(success=False, error_message=str(e))
        raise

def record_metric(metric_type: str, value: float, unit: str = "count", context: Optional[dict] = None):
    """记录性能指标的便捷函数"""
    _tracker.record_metric(metric_type, value, unit, context)

def start_monitoring():
    """启动全局性能监控"""
    _tracker.monitor.start_monitoring()

def stop_monitoring():
    """停止全局性能监控"""
    _tracker.monitor.stop_monitoring()

def get_performance_report(days: int = 1) -> dict:
    """获取性能报告"""
    return _tracker.monitor.get_performance_report(days)

# 使用示例
if __name__ == "__main__":
    import json
    
    # 启动监控
    start_monitoring()
    
    # 使用装饰器监控函数
    @monitor_task(task_type="calculation")
    def calculate_fibonacci(n: int) -> int:
        """计算斐波那契数列"""
        if n <= 1:
            return n
        return calculate_fibonacci(n-1) + calculate_fibonacci(n-2)
    
    # 使用上下文管理器监控代码块
    with monitor_context("data_processing", "processing") as tracker:
        # 模拟数据处理
        data = list(range(10000))
        processed_data = [x * 2 for x in data]
        
        # 记录自定义指标
        tracker.record_metric("data_size", len(data), "items")
        tracker.record_metric("processing_rate", len(data) / 0.1, "items_per_second")
    
    # 执行被监控的函数
    print("计算斐波那契数列...")
    result = calculate_fibonacci(10)
    print(f"结果: {result}")
    
    # 等待一段时间收集指标
    time.sleep(2)
    
    # 生成报告
    print("\n性能报告:")
    report = get_performance_report()
    print(json.dumps(report, indent=2, ensure_ascii=False))
    
    # 停止监控
    stop_monitoring()