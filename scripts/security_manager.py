#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
gg智能体安全管理器
实现权限控制、操作审计和安全策略管理
"""

import os
import json
import hashlib
import time
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Set, Any
from dataclasses import dataclass, asdict
from enum import Enum
import logging

class SecurityLevel(Enum):
    """安全级别枚举"""
    PUBLIC = "public"
    RESTRICTED = "restricted"
    CONFIDENTIAL = "confidential"
    SECRET = "secret"

class OperationType(Enum):
    """操作类型枚举"""
    READ = "read"
    WRITE = "write"
    EXECUTE = "execute"
    DELETE = "delete"
    ADMIN = "admin"

@dataclass
class SecurityEvent:
    """安全事件数据结构"""
    timestamp: str
    event_type: str
    user_id: str
    resource: str
    operation: str
    result: str
    risk_level: str
    details: Dict[str, Any]

@dataclass
class Permission:
    """权限数据结构"""
    resource_pattern: str
    operations: List[str]
    conditions: Dict[str, Any]
    expires_at: Optional[str] = None

@dataclass
class SecurityPolicy:
    """安全策略数据结构"""
    name: str
    description: str
    rules: List[Dict[str, Any]]
    enabled: bool = True
    priority: int = 0

class SecurityManager:
    """安全管理器主类"""
    
    def __init__(self, config_path: str = "config/security_config.json"):
        self.config_path = config_path
        self.config = self._load_config()
        self.audit_log_path = self.config.get("audit_log_path", "logs/security_audit.log")
        self.permissions_path = self.config.get("permissions_path", "config/permissions.json")
        self.policies_path = self.config.get("policies_path", "config/security_policies.json")
        
        # 确保目录存在
        os.makedirs(os.path.dirname(self.audit_log_path), exist_ok=True)
        os.makedirs(os.path.dirname(self.permissions_path), exist_ok=True)
        os.makedirs(os.path.dirname(self.policies_path), exist_ok=True)
        
        # 初始化日志
        self._setup_logging()
        
        # 加载权限和策略
        self.permissions = self._load_permissions()
        self.policies = self._load_policies()
        
        # 会话管理
        self.active_sessions: Dict[str, Dict] = {}
        self.failed_attempts: Dict[str, List[float]] = {}
    
    def _load_config(self) -> Dict:
        """加载安全配置"""
        if os.path.exists(self.config_path):
            with open(self.config_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        return self._get_default_config()
    
    def _get_default_config(self) -> Dict:
        """获取默认安全配置"""
        return {
            "max_failed_attempts": 5,
            "lockout_duration": 300,  # 5分钟
            "session_timeout": 3600,  # 1小时
            "password_min_length": 8,
            "require_2fa": False,
            "audit_retention_days": 90,
            "risk_thresholds": {
                "low": 0.3,
                "medium": 0.6,
                "high": 0.8
            },
            "allowed_file_extensions": [".py", ".json", ".md", ".txt", ".yaml", ".yml"],
            "restricted_paths": ["/etc", "/usr/bin", "/system"],
            "max_file_size": 10485760  # 10MB
        }
    
    def _setup_logging(self):
        """设置安全日志"""
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler(self.audit_log_path),
                logging.StreamHandler()
            ]
        )
        self.logger = logging.getLogger('SecurityManager')
    
    def _load_permissions(self) -> Dict[str, List[Permission]]:
        """加载权限配置"""
        if os.path.exists(self.permissions_path):
            with open(self.permissions_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                return {
                    user_id: [Permission(**perm) for perm in perms]
                    for user_id, perms in data.items()
                }
        return self._get_default_permissions()
    
    def _get_default_permissions(self) -> Dict[str, List[Permission]]:
        """获取默认权限配置"""
        return {
            "admin": [
                Permission(
                    resource_pattern="*",
                    operations=["read", "write", "execute", "delete", "admin"],
                    conditions={}
                )
            ],
            "user": [
                Permission(
                    resource_pattern="outputs/*",
                    operations=["read", "write"],
                    conditions={"time_range": "09:00-18:00"}
                ),
                Permission(
                    resource_pattern="scripts/*.py",
                    operations=["read", "execute"],
                    conditions={}
                )
            ],
            "guest": [
                Permission(
                    resource_pattern="outputs/public/*",
                    operations=["read"],
                    conditions={}
                )
            ]
        }
    
    def _load_policies(self) -> List[SecurityPolicy]:
        """加载安全策略"""
        if os.path.exists(self.policies_path):
            with open(self.policies_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                return [SecurityPolicy(**policy) for policy in data]
        return self._get_default_policies()
    
    def _get_default_policies(self) -> List[SecurityPolicy]:
        """获取默认安全策略"""
        return [
            SecurityPolicy(
                name="file_extension_check",
                description="检查文件扩展名是否在允许列表中",
                rules=[
                    {
                        "condition": "file_operation",
                        "action": "check_extension",
                        "parameters": {"allowed_extensions": self.config["allowed_file_extensions"]}
                    }
                ]
            ),
            SecurityPolicy(
                name="path_restriction",
                description="限制访问敏感路径",
                rules=[
                    {
                        "condition": "path_access",
                        "action": "deny_restricted_paths",
                        "parameters": {"restricted_paths": self.config["restricted_paths"]}
                    }
                ]
            ),
            SecurityPolicy(
                name="rate_limiting",
                description="限制操作频率",
                rules=[
                    {
                        "condition": "operation_frequency",
                        "action": "rate_limit",
                        "parameters": {"max_operations_per_minute": 60}
                    }
                ]
            )
        ]
    
    def authenticate_user(self, user_id: str, credentials: Dict[str, Any]) -> bool:
        """用户认证"""
        try:
            # 检查是否被锁定
            if self._is_user_locked(user_id):
                self._log_security_event(
                    "authentication_blocked", user_id, "system", "authenticate", 
                    "blocked", "high", {"reason": "user_locked"}
                )
                return False
            
            # 验证凭据（这里简化处理，实际应该使用更安全的方法）
            password = credentials.get("password", "")
            if len(password) < self.config["password_min_length"]:
                self._record_failed_attempt(user_id)
                return False
            
            # 创建会话
            session_id = self._generate_session_id(user_id)
            self.active_sessions[session_id] = {
                "user_id": user_id,
                "created_at": time.time(),
                "last_activity": time.time(),
                "permissions": self.permissions.get(user_id, [])
            }
            
            self._log_security_event(
                "authentication_success", user_id, "system", "authenticate", 
                "success", "low", {"session_id": session_id}
            )
            
            return True
            
        except Exception as e:
            self._log_security_event(
                "authentication_error", user_id, "system", "authenticate", 
                "error", "high", {"error": str(e)}
            )
            return False
    
    def check_permission(self, user_id: str, resource: str, operation: str, 
                        context: Optional[Dict] = None) -> bool:
        """检查用户权限"""
        try:
            user_permissions = self.permissions.get(user_id, [])
            
            for permission in user_permissions:
                if self._match_resource_pattern(resource, permission.resource_pattern):
                    if operation in permission.operations:
                        if self._check_permission_conditions(permission.conditions, context):
                            # 检查权限是否过期
                            if permission.expires_at:
                                expires = datetime.fromisoformat(permission.expires_at)
                                if datetime.now() > expires:
                                    continue
                            
                            self._log_security_event(
                                "permission_granted", user_id, resource, operation, 
                                "granted", "low", {"permission": permission.resource_pattern}
                            )
                            return True
            
            self._log_security_event(
                "permission_denied", user_id, resource, operation, 
                "denied", "medium", {"reason": "insufficient_permissions"}
            )
            return False
            
        except Exception as e:
            self._log_security_event(
                "permission_error", user_id, resource, operation, 
                "error", "high", {"error": str(e)}
            )
            return False
    
    def validate_operation(self, user_id: str, operation_type: str, 
                          target: str, parameters: Dict = None) -> Dict[str, Any]:
        """验证操作安全性"""
        result = {
            "allowed": False,
            "risk_level": "low",
            "warnings": [],
            "blocked_reasons": []
        }
        
        try:
            # 应用安全策略
            for policy in self.policies:
                if not policy.enabled:
                    continue
                    
                policy_result = self._apply_security_policy(policy, {
                    "user_id": user_id,
                    "operation_type": operation_type,
                    "target": target,
                    "parameters": parameters or {}
                })
                
                if not policy_result["allowed"]:
                    result["blocked_reasons"].extend(policy_result["reasons"])
                
                result["warnings"].extend(policy_result["warnings"])
                
                # 更新风险级别
                if policy_result["risk_level"] == "high":
                    result["risk_level"] = "high"
                elif policy_result["risk_level"] == "medium" and result["risk_level"] == "low":
                    result["risk_level"] = "medium"
            
            # 如果没有被阻止的原因，则允许操作
            result["allowed"] = len(result["blocked_reasons"]) == 0
            
            self._log_security_event(
                "operation_validation", user_id, target, operation_type, 
                "allowed" if result["allowed"] else "blocked", result["risk_level"], 
                {"result": result}
            )
            
        except Exception as e:
            result["blocked_reasons"].append(f"Validation error: {str(e)}")
            result["risk_level"] = "high"
            
        return result
    
    def _apply_security_policy(self, policy: SecurityPolicy, context: Dict) -> Dict[str, Any]:
        """应用安全策略"""
        result = {
            "allowed": True,
            "reasons": [],
            "warnings": [],
            "risk_level": "low"
        }
        
        for rule in policy.rules:
            condition = rule["condition"]
            action = rule["action"]
            parameters = rule.get("parameters", {})
            
            if condition == "file_operation" and action == "check_extension":
                target = context.get("target", "")
                if "." in target:
                    ext = "." + target.split(".")[-1]
                    if ext not in parameters["allowed_extensions"]:
                        result["allowed"] = False
                        result["reasons"].append(f"File extension {ext} not allowed")
                        result["risk_level"] = "medium"
            
            elif condition == "path_access" and action == "deny_restricted_paths":
                target = context.get("target", "")
                for restricted_path in parameters["restricted_paths"]:
                    if target.startswith(restricted_path):
                        result["allowed"] = False
                        result["reasons"].append(f"Access to {restricted_path} is restricted")
                        result["risk_level"] = "high"
            
            elif condition == "operation_frequency" and action == "rate_limit":
                # 简化的频率限制检查
                user_id = context.get("user_id")
                if self._check_rate_limit(user_id, parameters["max_operations_per_minute"]):
                    result["warnings"].append("Approaching rate limit")
                    result["risk_level"] = "medium"
        
        return result
    
    def _match_resource_pattern(self, resource: str, pattern: str) -> bool:
        """匹配资源模式"""
        if pattern == "*":
            return True
        
        # 简单的通配符匹配
        if pattern.endswith("*"):
            return resource.startswith(pattern[:-1])
        
        if pattern.startswith("*"):
            return resource.endswith(pattern[1:])
        
        return resource == pattern
    
    def _check_permission_conditions(self, conditions: Dict, context: Optional[Dict]) -> bool:
        """检查权限条件"""
        if not conditions:
            return True
        
        # 时间范围检查
        if "time_range" in conditions:
            time_range = conditions["time_range"]
            start_time, end_time = time_range.split("-")
            current_time = datetime.now().strftime("%H:%M")
            return start_time <= current_time <= end_time
        
        return True
    
    def _is_user_locked(self, user_id: str) -> bool:
        """检查用户是否被锁定"""
        if user_id not in self.failed_attempts:
            return False
        
        attempts = self.failed_attempts[user_id]
        recent_attempts = [t for t in attempts if time.time() - t < self.config["lockout_duration"]]
        
        return len(recent_attempts) >= self.config["max_failed_attempts"]
    
    def _record_failed_attempt(self, user_id: str):
        """记录失败尝试"""
        if user_id not in self.failed_attempts:
            self.failed_attempts[user_id] = []
        
        self.failed_attempts[user_id].append(time.time())
        
        # 清理旧的尝试记录
        cutoff_time = time.time() - self.config["lockout_duration"]
        self.failed_attempts[user_id] = [
            t for t in self.failed_attempts[user_id] if t > cutoff_time
        ]
    
    def _generate_session_id(self, user_id: str) -> str:
        """生成会话ID"""
        data = f"{user_id}_{time.time()}_{os.urandom(16).hex()}"
        return hashlib.sha256(data.encode()).hexdigest()[:32]
    
    def _check_rate_limit(self, user_id: str, max_per_minute: int) -> bool:
        """检查频率限制"""
        # 简化实现，实际应该使用更精确的算法
        return False
    
    def _log_security_event(self, event_type: str, user_id: str, resource: str, 
                           operation: str, result: str, risk_level: str, 
                           details: Dict[str, Any]):
        """记录安全事件"""
        event = SecurityEvent(
            timestamp=datetime.now().isoformat(),
            event_type=event_type,
            user_id=user_id,
            resource=resource,
            operation=operation,
            result=result,
            risk_level=risk_level,
            details=details
        )
        
        self.logger.info(f"Security Event: {json.dumps(asdict(event), ensure_ascii=False)}")
    
    def get_security_report(self, days: int = 7) -> Dict[str, Any]:
        """生成安全报告"""
        try:
            # 读取审计日志
            events = self._read_audit_log(days)
            
            report = {
                "period": f"Last {days} days",
                "generated_at": datetime.now().isoformat(),
                "summary": {
                    "total_events": len(events),
                    "high_risk_events": len([e for e in events if e.get("risk_level") == "high"]),
                    "failed_authentications": len([e for e in events if e.get("event_type") == "authentication_blocked"]),
                    "permission_denials": len([e for e in events if e.get("event_type") == "permission_denied"])
                },
                "top_users": self._get_top_users(events),
                "risk_analysis": self._analyze_risks(events),
                "recommendations": self._generate_security_recommendations(events)
            }
            
            return report
            
        except Exception as e:
            self.logger.error(f"Error generating security report: {str(e)}")
            return {"error": str(e)}
    
    def _read_audit_log(self, days: int) -> List[Dict]:
        """读取审计日志"""
        events = []
        cutoff_date = datetime.now() - timedelta(days=days)
        
        try:
            with open(self.audit_log_path, 'r', encoding='utf-8') as f:
                for line in f:
                    if "Security Event:" in line:
                        try:
                            event_json = line.split("Security Event: ", 1)[1]
                            event = json.loads(event_json)
                            event_date = datetime.fromisoformat(event["timestamp"])
                            if event_date >= cutoff_date:
                                events.append(event)
                        except (json.JSONDecodeError, KeyError, ValueError):
                            continue
        except FileNotFoundError:
            pass
        
        return events
    
    def _get_top_users(self, events: List[Dict]) -> List[Dict]:
        """获取活跃用户统计"""
        user_stats = {}
        for event in events:
            user_id = event.get("user_id", "unknown")
            if user_id not in user_stats:
                user_stats[user_id] = {"total_events": 0, "high_risk_events": 0}
            
            user_stats[user_id]["total_events"] += 1
            if event.get("risk_level") == "high":
                user_stats[user_id]["high_risk_events"] += 1
        
        return sorted(
            [{"user_id": k, **v} for k, v in user_stats.items()],
            key=lambda x: x["total_events"],
            reverse=True
        )[:10]
    
    def _analyze_risks(self, events: List[Dict]) -> Dict[str, Any]:
        """分析风险"""
        risk_levels = {"low": 0, "medium": 0, "high": 0}
        event_types = {}
        
        for event in events:
            risk_level = event.get("risk_level", "low")
            risk_levels[risk_level] += 1
            
            event_type = event.get("event_type", "unknown")
            event_types[event_type] = event_types.get(event_type, 0) + 1
        
        return {
            "risk_distribution": risk_levels,
            "event_types": event_types,
            "risk_score": self._calculate_risk_score(risk_levels)
        }
    
    def _calculate_risk_score(self, risk_levels: Dict[str, int]) -> float:
        """计算风险评分"""
        total_events = sum(risk_levels.values())
        if total_events == 0:
            return 0.0
        
        score = (
            risk_levels["low"] * 0.1 +
            risk_levels["medium"] * 0.5 +
            risk_levels["high"] * 1.0
        ) / total_events
        
        return round(score, 2)
    
    def _generate_security_recommendations(self, events: List[Dict]) -> List[str]:
        """生成安全建议"""
        recommendations = []
        
        # 分析高风险事件
        high_risk_events = [e for e in events if e.get("risk_level") == "high"]
        if len(high_risk_events) > 10:
            recommendations.append("检测到大量高风险事件，建议加强安全监控")
        
        # 分析认证失败
        auth_failures = [e for e in events if e.get("event_type") == "authentication_blocked"]
        if len(auth_failures) > 5:
            recommendations.append("频繁的认证失败，建议启用双因素认证")
        
        # 分析权限拒绝
        permission_denials = [e for e in events if e.get("event_type") == "permission_denied"]
        if len(permission_denials) > 20:
            recommendations.append("大量权限拒绝事件，建议审查用户权限配置")
        
        if not recommendations:
            recommendations.append("安全状况良好，继续保持当前安全策略")
        
        return recommendations

def main():
    """主函数 - 命令行接口"""
    import sys
    
    if len(sys.argv) < 2:
        print("用法: python security_manager.py <command> [args]")
        print("命令:")
        print("  report [days]     - 生成安全报告")
        print("  check-user <id>   - 检查用户状态")
        print("  validate <user> <operation> <target> - 验证操作")
        return
    
    command = sys.argv[1]
    security_manager = SecurityManager()
    
    if command == "report":
        days = int(sys.argv[2]) if len(sys.argv) > 2 else 7
        report = security_manager.get_security_report(days)
        print(json.dumps(report, indent=2, ensure_ascii=False))
    
    elif command == "check-user":
        if len(sys.argv) < 3:
            print("请提供用户ID")
            return
        
        user_id = sys.argv[2]
        is_locked = security_manager._is_user_locked(user_id)
        permissions = security_manager.permissions.get(user_id, [])
        
        print(f"用户: {user_id}")
        print(f"状态: {'锁定' if is_locked else '正常'}")
        print(f"权限数量: {len(permissions)}")
    
    elif command == "validate":
        if len(sys.argv) < 5:
            print("请提供: 用户ID 操作类型 目标")
            return
        
        user_id, operation, target = sys.argv[2:5]
        result = security_manager.validate_operation(user_id, operation, target)
        print(json.dumps(result, indent=2, ensure_ascii=False))
    
    else:
        print(f"未知命令: {command}")

if __name__ == "__main__":
    main()