#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
gg智能体性能监控系统

功能:
- 实时监控任务执行性能
- 收集和分析性能指标
- 生成性能报告和优化建议
- 检测性能异常和瓶颈
"""

import json
import time
import psutil
import threading
from datetime import datetime, timedelta
from pathlib import Path
from typing import Dict, List, Optional, Any
from dataclasses import dataclass, asdict
from collections import defaultdict, deque

@dataclass
class PerformanceMetric:
    """性能指标数据结构"""
    timestamp: str
    metric_type: str
    value: float
    unit: str
    context: Dict[str, Any]
    session_id: str

@dataclass
class TaskPerformance:
    """任务性能数据结构"""
    task_id: str
    task_type: str
    start_time: str
    end_time: Optional[str]
    duration_ms: Optional[float]
    cpu_usage: float
    memory_usage: float
    success: Optional[bool]
    error_message: Optional[str]
    metrics: List[PerformanceMetric]

class PerformanceMonitor:
    """性能监控器"""
    
    def __init__(self, config_path: str = "config/performance_config.json"):
        self.config_path = Path(config_path)
        self.metrics_dir = Path("metrics")
        self.metrics_dir.mkdir(exist_ok=True)
        
        # 加载配置
        self.config = self.load_config()
        
        # 性能数据存储
        self.current_tasks: Dict[str, TaskPerformance] = {}
        self.metrics_buffer = deque(maxlen=self.config.get('buffer_size', 1000))
        self.session_id = f"session_{int(time.time())}"
        
        # 监控线程
        self.monitoring = False
        self.monitor_thread = None
        
        # 性能统计
        self.stats = {
            'total_tasks': 0,
            'successful_tasks': 0,
            'failed_tasks': 0,
            'avg_duration': 0.0,
            'avg_cpu_usage': 0.0,
            'avg_memory_usage': 0.0
        }
    
    def load_config(self) -> Dict[str, Any]:
        """加载配置文件"""
        if self.config_path.exists():
            with open(self.config_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        else:
            # 默认配置
            default_config = {
                'monitoring_interval': 1.0,  # 秒
                'buffer_size': 1000,
                'alert_thresholds': {
                    'cpu_usage': 80.0,
                    'memory_usage': 80.0,
                    'task_duration': 30000  # 毫秒
                },
                'metrics_retention_days': 7,
                'auto_cleanup': True
            }
            # 保存默认配置
            self.config_path.parent.mkdir(exist_ok=True)
            with open(self.config_path, 'w', encoding='utf-8') as f:
                json.dump(default_config, f, indent=2, ensure_ascii=False)
            return default_config
    
    def start_monitoring(self):
        """开始性能监控"""
        if not self.monitoring:
            self.monitoring = True
            self.monitor_thread = threading.Thread(target=self._monitor_loop, daemon=True)
            self.monitor_thread.start()
            print(f"[PERF] 性能监控已启动 (会话ID: {self.session_id})")
    
    def stop_monitoring(self):
        """停止性能监控"""
        if self.monitoring:
            self.monitoring = False
            if self.monitor_thread:
                self.monitor_thread.join(timeout=2.0)
            self.save_metrics()
            print("[PERF] 性能监控已停止")
    
    def _monitor_loop(self):
        """监控循环"""
        interval = self.config.get('monitoring_interval', 1.0)
        
        while self.monitoring:
            try:
                # 收集系统指标
                cpu_percent = psutil.cpu_percent()
                memory_info = psutil.virtual_memory()
                
                # 记录系统指标
                self.record_metric(
                    metric_type="system_cpu",
                    value=cpu_percent,
                    unit="percent",
                    context={"cores": psutil.cpu_count()}
                )
                
                self.record_metric(
                    metric_type="system_memory",
                    value=memory_info.percent,
                    unit="percent",
                    context={
                        "total_gb": round(memory_info.total / (1024**3), 2),
                        "available_gb": round(memory_info.available / (1024**3), 2)
                    }
                )
                
                # 检查告警阈值
                self._check_alerts(cpu_percent, memory_info.percent)
                
                time.sleep(interval)
                
            except Exception as e:
                print(f"[PERF] 监控循环错误: {e}")
                time.sleep(interval)
    
    def start_task(self, task_id: str, task_type: str) -> str:
        """开始任务监控"""
        task_perf = TaskPerformance(
            task_id=task_id,
            task_type=task_type,
            start_time=datetime.now().isoformat(),
            end_time=None,
            duration_ms=None,
            cpu_usage=psutil.cpu_percent(),
            memory_usage=psutil.virtual_memory().percent,
            success=None,
            error_message=None,
            metrics=[]
        )
        
        self.current_tasks[task_id] = task_perf
        print(f"[PERF] 开始监控任务: {task_id} ({task_type})")
        return task_id
    
    def end_task(self, task_id: str, success: bool = True, error_message: Optional[str] = None):
        """结束任务监控"""
        if task_id not in self.current_tasks:
            print(f"[PERF] 警告: 任务 {task_id} 未找到")
            return
        
        task_perf = self.current_tasks[task_id]
        end_time = datetime.now()
        start_time = datetime.fromisoformat(task_perf.start_time)
        
        task_perf.end_time = end_time.isoformat()
        task_perf.duration_ms = (end_time - start_time).total_seconds() * 1000
        task_perf.success = success
        task_perf.error_message = error_message
        
        # 更新统计信息
        self._update_stats(task_perf)
        
        # 保存任务性能数据
        self._save_task_performance(task_perf)
        
        # 从当前任务中移除
        del self.current_tasks[task_id]
        
        print(f"[PERF] 任务完成: {task_id} (耗时: {task_perf.duration_ms:.1f}ms)")
    
    def record_metric(self, metric_type: str, value: float, unit: str, context: Optional[Dict] = None):
        """记录性能指标"""
        metric = PerformanceMetric(
            timestamp=datetime.now().isoformat(),
            metric_type=metric_type,
            value=value,
            unit=unit,
            context=context or {},
            session_id=self.session_id
        )
        
        self.metrics_buffer.append(metric)
    
    def _check_alerts(self, cpu_percent: float, memory_percent: float):
        """检查告警阈值"""
        thresholds = self.config.get('alert_thresholds', {})
        
        if cpu_percent > thresholds.get('cpu_usage', 80):
            print(f"[PERF] 🚨 CPU使用率告警: {cpu_percent:.1f}%")
        
        if memory_percent > thresholds.get('memory_usage', 80):
            print(f"[PERF] 🚨 内存使用率告警: {memory_percent:.1f}%")
    
    def _update_stats(self, task_perf: TaskPerformance):
        """更新统计信息"""
        self.stats['total_tasks'] += 1
        
        if task_perf.success:
            self.stats['successful_tasks'] += 1
        else:
            self.stats['failed_tasks'] += 1
        
        # 计算平均值
        total = self.stats['total_tasks']
        if task_perf.duration_ms:
            self.stats['avg_duration'] = (
                (self.stats['avg_duration'] * (total - 1) + task_perf.duration_ms) / total
            )
        
        self.stats['avg_cpu_usage'] = (
            (self.stats['avg_cpu_usage'] * (total - 1) + task_perf.cpu_usage) / total
        )
        
        self.stats['avg_memory_usage'] = (
            (self.stats['avg_memory_usage'] * (total - 1) + task_perf.memory_usage) / total
        )
    
    def _save_task_performance(self, task_perf: TaskPerformance):
        """保存任务性能数据"""
        date_str = datetime.now().strftime('%Y-%m-%d')
        file_path = self.metrics_dir / f"tasks_{date_str}.jsonl"
        
        with open(file_path, 'a', encoding='utf-8') as f:
            f.write(json.dumps(asdict(task_perf), ensure_ascii=False) + '\n')
    
    def save_metrics(self):
        """保存指标数据"""
        if not self.metrics_buffer:
            return
        
        date_str = datetime.now().strftime('%Y-%m-%d')
        file_path = self.metrics_dir / f"metrics_{date_str}.jsonl"
        
        with open(file_path, 'a', encoding='utf-8') as f:
            for metric in self.metrics_buffer:
                f.write(json.dumps(asdict(metric), ensure_ascii=False) + '\n')
        
        self.metrics_buffer.clear()
    
    def get_performance_report(self, days: int = 1) -> Dict[str, Any]:
        """生成性能报告"""
        end_date = datetime.now()
        start_date = end_date - timedelta(days=days)
        
        # 读取指定时间范围内的数据
        tasks_data = self._load_tasks_data(start_date, end_date)
        metrics_data = self._load_metrics_data(start_date, end_date)
        
        # 分析数据
        report = {
            'report_period': {
                'start': start_date.isoformat(),
                'end': end_date.isoformat(),
                'days': days
            },
            'task_summary': self._analyze_tasks(tasks_data),
            'system_metrics': self._analyze_metrics(metrics_data),
            'performance_trends': self._analyze_trends(tasks_data, metrics_data),
            'recommendations': self._generate_recommendations(tasks_data, metrics_data),
            'current_stats': self.stats
        }
        
        return report
    
    def _load_tasks_data(self, start_date: datetime, end_date: datetime) -> List[Dict]:
        """加载任务数据"""
        tasks = []
        current_date = start_date.date()
        
        while current_date <= end_date.date():
            file_path = self.metrics_dir / f"tasks_{current_date.strftime('%Y-%m-%d')}.jsonl"
            if file_path.exists():
                with open(file_path, 'r', encoding='utf-8') as f:
                    for line in f:
                        task_data = json.loads(line.strip())
                        task_time = datetime.fromisoformat(task_data['start_time'])
                        if start_date <= task_time <= end_date:
                            tasks.append(task_data)
            current_date += timedelta(days=1)
        
        return tasks
    
    def _load_metrics_data(self, start_date: datetime, end_date: datetime) -> List[Dict]:
        """加载指标数据"""
        metrics = []
        current_date = start_date.date()
        
        while current_date <= end_date.date():
            file_path = self.metrics_dir / f"metrics_{current_date.strftime('%Y-%m-%d')}.jsonl"
            if file_path.exists():
                with open(file_path, 'r', encoding='utf-8') as f:
                    for line in f:
                        metric_data = json.loads(line.strip())
                        metric_time = datetime.fromisoformat(metric_data['timestamp'])
                        if start_date <= metric_time <= end_date:
                            metrics.append(metric_data)
            current_date += timedelta(days=1)
        
        return metrics
    
    def _analyze_tasks(self, tasks_data: List[Dict]) -> Dict[str, Any]:
        """分析任务数据"""
        if not tasks_data:
            return {'total_tasks': 0}
        
        total_tasks = len(tasks_data)
        successful_tasks = sum(1 for task in tasks_data if task.get('success', False))
        failed_tasks = total_tasks - successful_tasks
        
        durations = [task['duration_ms'] for task in tasks_data if task.get('duration_ms')]
        avg_duration = sum(durations) / len(durations) if durations else 0
        
        task_types = defaultdict(int)
        for task in tasks_data:
            task_types[task['task_type']] += 1
        
        return {
            'total_tasks': total_tasks,
            'successful_tasks': successful_tasks,
            'failed_tasks': failed_tasks,
            'success_rate': successful_tasks / total_tasks if total_tasks > 0 else 0,
            'avg_duration_ms': avg_duration,
            'task_types': dict(task_types),
            'slowest_tasks': sorted(tasks_data, key=lambda x: x.get('duration_ms', 0), reverse=True)[:5]
        }
    
    def _analyze_metrics(self, metrics_data: List[Dict]) -> Dict[str, Any]:
        """分析系统指标"""
        if not metrics_data:
            return {}
        
        cpu_metrics = [m for m in metrics_data if m['metric_type'] == 'system_cpu']
        memory_metrics = [m for m in metrics_data if m['metric_type'] == 'system_memory']
        
        analysis = {}
        
        if cpu_metrics:
            cpu_values = [m['value'] for m in cpu_metrics]
            analysis['cpu'] = {
                'avg': sum(cpu_values) / len(cpu_values),
                'max': max(cpu_values),
                'min': min(cpu_values),
                'samples': len(cpu_values)
            }
        
        if memory_metrics:
            memory_values = [m['value'] for m in memory_metrics]
            analysis['memory'] = {
                'avg': sum(memory_values) / len(memory_values),
                'max': max(memory_values),
                'min': min(memory_values),
                'samples': len(memory_values)
            }
        
        return analysis
    
    def _analyze_trends(self, tasks_data: List[Dict], metrics_data: List[Dict]) -> Dict[str, Any]:
        """分析性能趋势"""
        # 简化的趋势分析
        trends = {
            'task_frequency': 'stable',  # 可以基于时间分布计算
            'performance_trend': 'stable',  # 可以基于duration变化计算
            'resource_usage': 'normal'  # 可以基于CPU/内存使用率计算
        }
        
        return trends
    
    def _generate_recommendations(self, tasks_data: List[Dict], metrics_data: List[Dict]) -> List[str]:
        """生成优化建议"""
        recommendations = []
        
        # 基于任务分析的建议
        if tasks_data:
            avg_duration = sum(task.get('duration_ms', 0) for task in tasks_data) / len(tasks_data)
            if avg_duration > 10000:  # 10秒
                recommendations.append("任务平均执行时间较长，建议优化任务执行逻辑")
            
            failed_rate = sum(1 for task in tasks_data if not task.get('success', True)) / len(tasks_data)
            if failed_rate > 0.1:  # 10%失败率
                recommendations.append("任务失败率较高，建议检查错误处理机制")
        
        # 基于系统指标的建议
        cpu_metrics = [m for m in metrics_data if m['metric_type'] == 'system_cpu']
        if cpu_metrics:
            avg_cpu = sum(m['value'] for m in cpu_metrics) / len(cpu_metrics)
            if avg_cpu > 70:
                recommendations.append("CPU使用率较高，建议优化计算密集型操作")
        
        memory_metrics = [m for m in metrics_data if m['metric_type'] == 'system_memory']
        if memory_metrics:
            avg_memory = sum(m['value'] for m in memory_metrics) / len(memory_metrics)
            if avg_memory > 70:
                recommendations.append("内存使用率较高，建议优化内存管理")
        
        if not recommendations:
            recommendations.append("系统性能良好，继续保持")
        
        return recommendations
    
    def monitor_command(self, command):
        """监控命令执行"""
        import subprocess
        import time
        
        print(f"[PERF] 开始监控命令: {command}")
        
        start_time = time.time()
        start_cpu = psutil.cpu_percent()
        start_memory = psutil.virtual_memory().percent
        
        try:
            # 执行命令
            result = subprocess.run(command, shell=True, capture_output=True, text=True)
            
            end_time = time.time()
            end_cpu = psutil.cpu_percent()
            end_memory = psutil.virtual_memory().percent
            
            # 计算性能差异
            execution_time = end_time - start_time
            cpu_usage_change = end_cpu - start_cpu
            memory_usage_change = end_memory - start_memory
            
            # 记录监控结果
            monitoring_result = {
                "command": command,
                "execution_time": execution_time,
                "cpu_usage_change": cpu_usage_change,
                "memory_usage_change": memory_usage_change,
                "exit_code": result.returncode,
                "stdout": result.stdout,
                "stderr": result.stderr,
                "timestamp": datetime.now().isoformat()
            }
            
            print(f"[PERF] 命令监控完成: {execution_time:.2f}s")
            return monitoring_result
            
        except Exception as e:
            print(f"[PERF] 命令监控失败: {e}")
            return None

# 全局监控器实例
_monitor_instance = None

def get_monitor() -> PerformanceMonitor:
    """获取全局监控器实例"""
    global _monitor_instance
    if _monitor_instance is None:
        _monitor_instance = PerformanceMonitor()
    return _monitor_instance

def start_monitoring():
    """启动性能监控"""
    monitor = get_monitor()
    monitor.start_monitoring()

def stop_monitoring():
    """停止性能监控"""
    monitor = get_monitor()
    monitor.stop_monitoring()

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description="gg智能体性能监控系统")
    parser.add_argument('action', choices=['start', 'stop', 'report', 'status'],
                       help='执行的操作')
    parser.add_argument('--days', type=int, default=1,
                       help='报告时间范围(天)')
    parser.add_argument('--output', type=str,
                       help='报告输出文件路径')
    
    args = parser.parse_args()
    
    monitor = PerformanceMonitor()
    
    if args.action == 'start':
        monitor.start_monitoring()
        try:
            # 保持监控运行
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            monitor.stop_monitoring()
    
    elif args.action == 'stop':
        monitor.stop_monitoring()
    
    elif args.action == 'report':
        report = monitor.get_performance_report(days=args.days)
        
        if args.output:
            with open(args.output, 'w', encoding='utf-8') as f:
                json.dump(report, f, indent=2, ensure_ascii=False)
            print(f"报告已保存到: {args.output}")
        else:
            print(json.dumps(report, indent=2, ensure_ascii=False))
    
    elif args.action == 'status':
        print(f"当前统计: {json.dumps(monitor.stats, indent=2, ensure_ascii=False)}")
        print(f"活跃任务数: {len(monitor.current_tasks)}")
        print(f"缓存指标数: {len(monitor.metrics_buffer)}")