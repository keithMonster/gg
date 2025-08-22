#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
gg智能体安全集成接口
提供简化的安全功能集成方法
"""

import os
import sys
import json
import functools
from typing import Dict, Any, Optional, Callable
from contextlib import contextmanager

# 添加脚本目录到路径
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

try:
    from security_manager import SecurityManager
except ImportError:
    print("警告: 无法导入 SecurityManager，安全功能将被禁用")
    SecurityManager = None

class SecurityTracker:
    """安全跟踪器 - 简化的安全功能接口"""
    
    def __init__(self, user_id: str = "system", config_path: Optional[str] = None):
        self.user_id = user_id
        self.enabled = SecurityManager is not None
        
        if self.enabled:
            try:
                self.security_manager = SecurityManager(config_path) if config_path else SecurityManager()
                self.authenticated = False
            except Exception as e:
                print(f"安全管理器初始化失败: {e}")
                self.enabled = False
                self.security_manager = None
        else:
            self.security_manager = None
    
    def authenticate(self, credentials: Dict[str, Any]) -> bool:
        """用户认证"""
        if not self.enabled:
            return True
        
        try:
            self.authenticated = self.security_manager.authenticate_user(self.user_id, credentials)
            return self.authenticated
        except Exception as e:
            print(f"认证失败: {e}")
            return False
    
    def check_permission(self, resource: str, operation: str, context: Optional[Dict] = None) -> bool:
        """检查权限"""
        if not self.enabled:
            return True
        
        try:
            return self.security_manager.check_permission(self.user_id, resource, operation, context)
        except Exception as e:
            print(f"权限检查失败: {e}")
            return False
    
    def validate_operation(self, operation_type: str, target: str, parameters: Optional[Dict] = None) -> Dict[str, Any]:
        """验证操作安全性"""
        if not self.enabled:
            return {"allowed": True, "risk_level": "low", "warnings": [], "blocked_reasons": []}
        
        try:
            return self.security_manager.validate_operation(self.user_id, operation_type, target, parameters)
        except Exception as e:
            print(f"操作验证失败: {e}")
            return {"allowed": False, "risk_level": "high", "warnings": [], "blocked_reasons": [str(e)]}
    
    def log_security_event(self, event_type: str, resource: str, operation: str, 
                          result: str, risk_level: str = "low", details: Optional[Dict] = None):
        """记录安全事件"""
        if not self.enabled:
            return
        
        try:
            self.security_manager._log_security_event(
                event_type, self.user_id, resource, operation, result, risk_level, details or {}
            )
        except Exception as e:
            print(f"安全事件记录失败: {e}")
    
    def get_security_status(self) -> Dict[str, Any]:
        """获取安全状态"""
        if not self.enabled:
            return {"enabled": False, "status": "disabled"}
        
        try:
            return {
                "enabled": True,
                "authenticated": self.authenticated,
                "user_id": self.user_id,
                "permissions_count": len(self.security_manager.permissions.get(self.user_id, [])),
                "policies_count": len(self.security_manager.policies)
            }
        except Exception as e:
            return {"enabled": True, "status": "error", "error": str(e)}

# 全局安全跟踪器实例
_global_tracker = None

def get_security_tracker(user_id: str = "system") -> SecurityTracker:
    """获取安全跟踪器实例"""
    global _global_tracker
    if _global_tracker is None or _global_tracker.user_id != user_id:
        _global_tracker = SecurityTracker(user_id)
    return _global_tracker

def secure_operation(operation_type: str, resource_pattern: str = "*", 
                    required_permission: str = "execute"):
    """安全操作装饰器"""
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            tracker = get_security_tracker()
            
            # 检查权限
            if not tracker.check_permission(resource_pattern, required_permission):
                error_msg = f"权限不足: 需要 {required_permission} 权限访问 {resource_pattern}"
                tracker.log_security_event(
                    "permission_denied", resource_pattern, required_permission, 
                    "denied", "medium", {"function": func.__name__}
                )
                raise PermissionError(error_msg)
            
            # 验证操作
            validation_result = tracker.validate_operation(
                operation_type, resource_pattern, {"function": func.__name__}
            )
            
            if not validation_result["allowed"]:
                error_msg = f"操作被阻止: {', '.join(validation_result['blocked_reasons'])}"
                tracker.log_security_event(
                    "operation_blocked", resource_pattern, operation_type, 
                    "blocked", validation_result["risk_level"], 
                    {"function": func.__name__, "reasons": validation_result["blocked_reasons"]}
                )
                raise SecurityError(error_msg)
            
            # 记录操作开始
            tracker.log_security_event(
                "operation_start", resource_pattern, operation_type, 
                "started", "low", {"function": func.__name__}
            )
            
            try:
                # 执行原函数
                result = func(*args, **kwargs)
                
                # 记录操作成功
                tracker.log_security_event(
                    "operation_success", resource_pattern, operation_type, 
                    "success", "low", {"function": func.__name__}
                )
                
                return result
                
            except Exception as e:
                # 记录操作失败
                tracker.log_security_event(
                    "operation_error", resource_pattern, operation_type, 
                    "error", "medium", {"function": func.__name__, "error": str(e)}
                )
                raise
        
        return wrapper
    return decorator

@contextmanager
def security_context(user_id: str, operation_type: str, resource: str):
    """安全上下文管理器"""
    tracker = get_security_tracker(user_id)
    
    # 记录上下文开始
    tracker.log_security_event(
        "context_start", resource, operation_type, "started", "low", {}
    )
    
    try:
        yield tracker
        
        # 记录上下文成功结束
        tracker.log_security_event(
            "context_end", resource, operation_type, "success", "low", {}
        )
        
    except Exception as e:
        # 记录上下文异常
        tracker.log_security_event(
            "context_error", resource, operation_type, "error", "medium", 
            {"error": str(e)}
        )
        raise

class SecurityError(Exception):
    """安全相关异常"""
    pass

def secure_file_operation(file_path: str, operation: str = "write"):
    """安全文件操作装饰器"""
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            tracker = get_security_tracker()
            
            # 验证文件操作
            validation_result = tracker.validate_operation(
                "file_operation", file_path, {"operation": operation}
            )
            
            if not validation_result["allowed"]:
                raise SecurityError(f"文件操作被阻止: {', '.join(validation_result['blocked_reasons'])}")
            
            # 检查文件权限
            if not tracker.check_permission(file_path, operation):
                raise PermissionError(f"文件权限不足: {file_path}")
            
            return func(*args, **kwargs)
        
        return wrapper
    return decorator

def validate_input(input_data: Any, validation_rules: Dict[str, Any]) -> Dict[str, Any]:
    """输入验证"""
    tracker = get_security_tracker()
    
    result = {
        "valid": True,
        "errors": [],
        "warnings": [],
        "sanitized_data": input_data
    }
    
    try:
        # 基本类型检查
        if "type" in validation_rules:
            expected_type = validation_rules["type"]
            if not isinstance(input_data, expected_type):
                result["valid"] = False
                result["errors"].append(f"类型错误: 期望 {expected_type.__name__}, 得到 {type(input_data).__name__}")
        
        # 长度检查
        if "max_length" in validation_rules and hasattr(input_data, '__len__'):
            if len(input_data) > validation_rules["max_length"]:
                result["valid"] = False
                result["errors"].append(f"长度超限: 最大 {validation_rules['max_length']}, 实际 {len(input_data)}")
        
        # 模式检查
        if "pattern" in validation_rules and isinstance(input_data, str):
            import re
            if not re.match(validation_rules["pattern"], input_data):
                result["valid"] = False
                result["errors"].append("格式不匹配")
        
        # 安全内容检查
        if isinstance(input_data, str):
            validation_result = tracker.validate_operation(
                "input_validation", "user_input", {"content": input_data}
            )
            
            if not validation_result["allowed"]:
                result["valid"] = False
                result["errors"].extend(validation_result["blocked_reasons"])
            
            result["warnings"].extend(validation_result["warnings"])
        
        # 记录验证事件
        tracker.log_security_event(
            "input_validation", "user_input", "validate", 
            "success" if result["valid"] else "failed", 
            "low" if result["valid"] else "medium",
            {"errors": result["errors"], "warnings": result["warnings"]}
        )
        
    except Exception as e:
        result["valid"] = False
        result["errors"].append(f"验证异常: {str(e)}")
        
        tracker.log_security_event(
            "validation_error", "user_input", "validate", "error", "high", 
            {"error": str(e)}
        )
    
    return result

def main():
    """测试和演示安全集成功能"""
    print("=== 安全集成测试 ===")
    
    # 创建安全跟踪器
    tracker = get_security_tracker("test_user")
    print(f"安全状态: {tracker.get_security_status()}")
    
    # 测试认证
    auth_result = tracker.authenticate({"password": "test123456"})
    print(f"认证结果: {auth_result}")
    
    # 测试权限检查
    perm_result = tracker.check_permission("outputs/test.txt", "write")
    print(f"权限检查: {perm_result}")
    
    # 测试操作验证
    validation_result = tracker.validate_operation("file_write", "outputs/test.txt")
    print(f"操作验证: {validation_result}")
    
    # 测试装饰器
    @secure_operation("test_operation", "outputs/*", "execute")
    def test_function():
        return "测试函数执行成功"
    
    try:
        result = test_function()
        print(f"装饰器测试: {result}")
    except (PermissionError, SecurityError) as e:
        print(f"装饰器测试失败: {e}")
    
    # 测试上下文管理器
    try:
        with security_context("test_user", "context_test", "outputs/context.txt") as ctx:
            print(f"上下文管理器测试: {ctx.get_security_status()}")
    except Exception as e:
        print(f"上下文管理器测试失败: {e}")
    
    # 测试输入验证
    validation_rules = {
        "type": str,
        "max_length": 100,
        "pattern": r"^[a-zA-Z0-9_\-\.]+$"
    }
    
    test_inputs = [
        "valid_input_123",
        "invalid input with spaces",
        "a" * 150,  # 太长
        123  # 错误类型
    ]
    
    for test_input in test_inputs:
        result = validate_input(test_input, validation_rules)
        print(f"输入验证 '{test_input}': {result['valid']}, 错误: {result['errors']}")

if __name__ == "__main__":
    main()