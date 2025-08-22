#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
知识图谱集成接口

功能:
- 自动知识提取和建模
- 与其他系统的集成
- 知识推理和推荐
- 实时知识更新
"""

import json
import os
import sys
import logging
import re
from datetime import datetime
from typing import Dict, List, Any, Optional, Tuple, Set
from functools import wraps
from contextlib import contextmanager

# 添加项目根目录到路径
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

try:
    from scripts.knowledge_graph import KnowledgeGraphManager, KnowledgeEntity, KnowledgeRelation
except ImportError:
    # 如果无法导入，创建简化版本
    class KnowledgeGraphManager:
        def __init__(self, *args, **kwargs):
            pass
        def add_entity(self, *args, **kwargs):
            return "dummy_id"
        def add_relation(self, *args, **kwargs):
            return "dummy_id"

class KnowledgeExtractor:
    """知识提取器"""
    
    def __init__(self, kg_manager: KnowledgeGraphManager):
        self.kg_manager = kg_manager
        self.extraction_patterns = {
            'function_def': r'def\s+(\w+)\s*\(',
            'class_def': r'class\s+(\w+)\s*[\(:]',
            'import_stmt': r'(?:from\s+(\w+)\s+)?import\s+([\w\s,]+)',
            'variable_assign': r'(\w+)\s*=\s*',
            'method_call': r'(\w+)\.(\w+)\s*\(',
            'error_pattern': r'(\w*Error|\w*Exception):\s*(.+)',
            'config_key': r'["\']([\w_]+)["\']\s*:\s*',
            'file_extension': r'\.(\w+)$'
        }
        
        self.entity_type_mapping = {
            'function_def': 'function',
            'class_def': 'class',
            'import_stmt': 'library',
            'variable_assign': 'variable',
            'method_call': 'method',
            'error_pattern': 'error',
            'config_key': 'configuration',
            'file_extension': 'file_type'
        }
    
    def extract_from_code(self, code: str, source: str = "code_analysis") -> List[str]:
        """从代码中提取知识"""
        extracted_entities = []
        
        for pattern_name, pattern in self.extraction_patterns.items():
            matches = re.findall(pattern, code, re.MULTILINE)
            entity_type = self.entity_type_mapping.get(pattern_name, 'concept')
            
            for match in matches:
                if isinstance(match, tuple):
                    # 处理多组匹配
                    for item in match:
                        if item and item.strip():
                            entity_id = self.kg_manager.add_entity(
                                name=item.strip(),
                                entity_type=entity_type,
                                properties={'pattern': pattern_name, 'source_code': True},
                                confidence=0.8,
                                source=source
                            )
                            extracted_entities.append(entity_id)
                else:
                    if match and match.strip():
                        entity_id = self.kg_manager.add_entity(
                            name=match.strip(),
                            entity_type=entity_type,
                            properties={'pattern': pattern_name, 'source_code': True},
                            confidence=0.8,
                            source=source
                        )
                        extracted_entities.append(entity_id)
        
        return extracted_entities
    
    def extract_from_text(self, text: str, source: str = "text_analysis") -> List[str]:
        """从文本中提取知识"""
        extracted_entities = []
        
        # 提取技术术语（大写字母开头的词汇）
        tech_terms = re.findall(r'\b[A-Z][a-zA-Z]+(?:[A-Z][a-zA-Z]*)*\b', text)
        for term in set(tech_terms):
            if len(term) > 2:  # 过滤太短的词
                entity_id = self.kg_manager.add_entity(
                    name=term,
                    entity_type='concept',
                    properties={'source_text': True},
                    confidence=0.6,
                    source=source
                )
                extracted_entities.append(entity_id)
        
        # 提取文件路径
        file_paths = re.findall(r'[\w/\\.-]+\.[a-zA-Z]{2,4}', text)
        for path in set(file_paths):
            entity_id = self.kg_manager.add_entity(
                name=path,
                entity_type='file',
                properties={'source_text': True},
                confidence=0.7,
                source=source
            )
            extracted_entities.append(entity_id)
        
        return extracted_entities
    
    def extract_from_error(self, error_msg: str, source: str = "error_analysis") -> List[str]:
        """从错误信息中提取知识"""
        extracted_entities = []
        
        # 提取错误类型
        error_types = re.findall(r'(\w*Error|\w*Exception)', error_msg)
        for error_type in set(error_types):
            entity_id = self.kg_manager.add_entity(
                name=error_type,
                entity_type='error',
                properties={'source_error': True},
                confidence=0.9,
                source=source
            )
            extracted_entities.append(entity_id)
        
        # 提取文件名
        file_names = re.findall(r'File "([^"]+)"', error_msg)
        for file_name in set(file_names):
            entity_id = self.kg_manager.add_entity(
                name=os.path.basename(file_name),
                entity_type='file',
                properties={'source_error': True, 'full_path': file_name},
                confidence=0.8,
                source=source
            )
            extracted_entities.append(entity_id)
        
        return extracted_entities

class KnowledgeReasoner:
    """知识推理器"""
    
    def __init__(self, kg_manager: KnowledgeGraphManager):
        self.kg_manager = kg_manager
    
    def infer_transitive_relations(self, relation_type: str) -> List[Tuple[str, str]]:
        """推理传递关系"""
        new_relations = []
        
        # 获取所有指定类型的关系
        relations = self.kg_manager.query_relations(relation_type=relation_type)
        
        # 构建关系图
        relation_graph = {}
        for relation in relations:
            if relation.source_id not in relation_graph:
                relation_graph[relation.source_id] = []
            relation_graph[relation.source_id].append(relation.target_id)
        
        # 查找传递关系
        for source in relation_graph:
            for intermediate in relation_graph[source]:
                if intermediate in relation_graph:
                    for target in relation_graph[intermediate]:
                        if target != source:  # 避免自环
                            # 检查是否已存在直接关系
                            existing = self.kg_manager.query_relations(
                                source_id=source,
                                target_id=target,
                                relation_type=relation_type
                            )
                            if not existing:
                                new_relations.append((source, target))
        
        # 添加推理出的关系
        for source_id, target_id in new_relations:
            self.kg_manager.add_relation(
                source_id=source_id,
                target_id=target_id,
                relation_type=relation_type,
                properties={'inferred': True, 'inference_type': 'transitive'},
                confidence=0.6,
                source="reasoning"
            )
        
        return new_relations
    
    def find_similar_entities(self, entity_id: str, similarity_threshold: float = 0.7) -> List[str]:
        """查找相似实体"""
        if entity_id not in self.kg_manager.entities:
            return []
        
        target_entity = self.kg_manager.entities[entity_id]
        similar_entities = []
        
        for other_id, other_entity in self.kg_manager.entities.items():
            if other_id == entity_id:
                continue
            
            # 计算相似度
            similarity = self._calculate_similarity(target_entity, other_entity)
            
            if similarity >= similarity_threshold:
                similar_entities.append((other_id, similarity))
                
                # 添加相似关系
                existing = self.kg_manager.query_relations(
                    source_id=entity_id,
                    target_id=other_id,
                    relation_type="similar_to"
                )
                if not existing:
                    self.kg_manager.add_relation(
                        source_id=entity_id,
                        target_id=other_id,
                        relation_type="similar_to",
                        properties={'similarity_score': similarity, 'inferred': True},
                        confidence=similarity,
                        source="reasoning"
                    )
        
        return [entity_id for entity_id, _ in sorted(similar_entities, key=lambda x: x[1], reverse=True)]
    
    def _calculate_similarity(self, entity1: KnowledgeEntity, entity2: KnowledgeEntity) -> float:
        """计算实体相似度"""
        similarity = 0.0
        
        # 类型相似度
        if entity1.type == entity2.type:
            similarity += 0.3
        
        # 名称相似度（简单的字符串相似度）
        name1_words = set(entity1.name.lower().split())
        name2_words = set(entity2.name.lower().split())
        
        if name1_words and name2_words:
            intersection = len(name1_words.intersection(name2_words))
            union = len(name1_words.union(name2_words))
            name_similarity = intersection / union if union > 0 else 0
            similarity += name_similarity * 0.4
        
        # 属性相似度
        props1 = set(entity1.properties.keys())
        props2 = set(entity2.properties.keys())
        
        if props1 and props2:
            prop_intersection = len(props1.intersection(props2))
            prop_union = len(props1.union(props2))
            prop_similarity = prop_intersection / prop_union if prop_union > 0 else 0
            similarity += prop_similarity * 0.3
        
        return min(similarity, 1.0)
    
    def recommend_relations(self, entity_id: str, max_recommendations: int = 5) -> List[Dict[str, Any]]:
        """推荐可能的关系"""
        if entity_id not in self.kg_manager.entities:
            return []
        
        entity = self.kg_manager.entities[entity_id]
        recommendations = []
        
        # 基于类型推荐关系
        type_based_relations = {
            'function': ['uses', 'implements', 'calls'],
            'class': ['extends', 'implements', 'contains'],
            'library': ['provides', 'depends_on'],
            'error': ['caused_by', 'related_to'],
            'file': ['contains', 'imports']
        }
        
        suggested_relations = type_based_relations.get(entity.type, ['related_to'])
        
        # 查找潜在的目标实体
        for other_id, other_entity in self.kg_manager.entities.items():
            if other_id == entity_id:
                continue
            
            for relation_type in suggested_relations:
                # 检查是否已存在关系
                existing = self.kg_manager.query_relations(
                    source_id=entity_id,
                    target_id=other_id,
                    relation_type=relation_type
                )
                
                if not existing:
                    # 计算推荐置信度
                    confidence = self._calculate_relation_confidence(
                        entity, other_entity, relation_type
                    )
                    
                    if confidence > 0.5:
                        recommendations.append({
                            'source_id': entity_id,
                            'target_id': other_id,
                            'relation_type': relation_type,
                            'confidence': confidence,
                            'reason': f"Based on entity types: {entity.type} -> {other_entity.type}"
                        })
        
        # 按置信度排序并返回前N个
        recommendations.sort(key=lambda x: x['confidence'], reverse=True)
        return recommendations[:max_recommendations]
    
    def _calculate_relation_confidence(self, source: KnowledgeEntity, target: KnowledgeEntity, 
                                     relation_type: str) -> float:
        """计算关系推荐置信度"""
        confidence = 0.0
        
        # 基于实体类型的置信度
        type_compatibility = {
            ('function', 'library', 'uses'): 0.8,
            ('class', 'class', 'extends'): 0.9,
            ('function', 'function', 'calls'): 0.7,
            ('error', 'file', 'occurs_in'): 0.8,
            ('file', 'library', 'imports'): 0.8
        }
        
        key = (source.type, target.type, relation_type)
        if key in type_compatibility:
            confidence += type_compatibility[key]
        else:
            confidence += 0.3  # 默认基础置信度
        
        # 基于名称相似度的调整
        name_similarity = self._calculate_similarity(source, target)
        confidence += name_similarity * 0.2
        
        return min(confidence, 1.0)

class KnowledgeTracker:
    """知识跟踪器"""
    
    def __init__(self, config_path: str = "config/knowledge_config.json"):
        self.kg_manager = KnowledgeGraphManager(config_path)
        self.extractor = KnowledgeExtractor(self.kg_manager)
        self.reasoner = KnowledgeReasoner(self.kg_manager)
        
        # 设置日志
        self.logger = logging.getLogger(__name__)
    
    def track_code_execution(self, code: str, context: Dict[str, Any] = None):
        """跟踪代码执行"""
        try:
            # 提取知识
            entities = self.extractor.extract_from_code(code, "code_execution")
            
            # 记录上下文信息
            if context:
                for key, value in context.items():
                    if isinstance(value, str) and value:
                        entity_id = self.kg_manager.add_entity(
                            name=value,
                            entity_type='context',
                            properties={'context_key': key},
                            confidence=0.7,
                            source="context_tracking"
                        )
                        entities.append(entity_id)
            
            self.logger.info(f"Tracked code execution: extracted {len(entities)} entities")
            return entities
            
        except Exception as e:
            self.logger.error(f"Error tracking code execution: {e}")
            return []
    
    def track_error(self, error_msg: str, context: Dict[str, Any] = None):
        """跟踪错误"""
        try:
            # 提取错误相关知识
            entities = self.extractor.extract_from_error(error_msg, "error_tracking")
            
            # 添加错误上下文
            if context:
                error_context_id = self.kg_manager.add_entity(
                    name=f"error_context_{datetime.now().strftime('%Y%m%d_%H%M%S')}",
                    entity_type='error_context',
                    properties=context,
                    confidence=0.8,
                    source="error_tracking"
                )
                entities.append(error_context_id)
            
            self.logger.info(f"Tracked error: extracted {len(entities)} entities")
            return entities
            
        except Exception as e:
            self.logger.error(f"Error tracking error: {e}")
            return []
    
    def track_user_interaction(self, interaction_data: Dict[str, Any]):
        """跟踪用户交互"""
        try:
            entities = []
            
            # 提取交互中的文本知识
            if 'input' in interaction_data:
                text_entities = self.extractor.extract_from_text(
                    interaction_data['input'], "user_interaction"
                )
                entities.extend(text_entities)
            
            # 记录交互模式
            if 'action' in interaction_data:
                action_id = self.kg_manager.add_entity(
                    name=interaction_data['action'],
                    entity_type='user_action',
                    properties={
                        'timestamp': interaction_data.get('timestamp', datetime.now().isoformat()),
                        'success': interaction_data.get('success', True)
                    },
                    confidence=0.9,
                    source="user_interaction"
                )
                entities.append(action_id)
            
            self.logger.info(f"Tracked user interaction: extracted {len(entities)} entities")
            return entities
            
        except Exception as e:
            self.logger.error(f"Error tracking user interaction: {e}")
            return []
    
    def get_recommendations(self, context: str = None) -> List[Dict[str, Any]]:
        """获取知识推荐"""
        try:
            recommendations = []
            
            # 获取最近的实体
            recent_entities = sorted(
                self.kg_manager.entities.values(),
                key=lambda x: x.updated_at,
                reverse=True
            )[:10]
            
            # 为每个实体生成关系推荐
            for entity in recent_entities:
                entity_recommendations = self.reasoner.recommend_relations(entity.id)
                recommendations.extend(entity_recommendations)
            
            # 执行推理
            transitive_relations = self.reasoner.infer_transitive_relations('uses')
            if transitive_relations:
                recommendations.append({
                    'type': 'inference',
                    'description': f"Inferred {len(transitive_relations)} transitive 'uses' relations",
                    'confidence': 0.6
                })
            
            return recommendations[:10]  # 返回前10个推荐
            
        except Exception as e:
            self.logger.error(f"Error getting recommendations: {e}")
            return []
    
    def get_status(self) -> Dict[str, Any]:
        """获取知识图谱状态"""
        try:
            stats = self.kg_manager.get_statistics()
            
            # 添加推理统计
            inferred_relations = len([
                r for r in self.kg_manager.relations.values()
                if r.properties.get('inferred', False)
            ])
            
            stats['reasoning'] = {
                'inferred_relations': inferred_relations,
                'inference_ratio': inferred_relations / max(stats['relations']['total'], 1)
            }
            
            return stats
            
        except Exception as e:
            self.logger.error(f"Error getting status: {e}")
            return {}

# 装饰器和上下文管理器
def knowledge_tracking(track_code: bool = True, track_errors: bool = True):
    """知识跟踪装饰器"""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            tracker = KnowledgeTracker()
            
            # 跟踪函数调用
            if track_code:
                import inspect
                source_code = inspect.getsource(func)
                tracker.track_code_execution(source_code, {
                    'function_name': func.__name__,
                    'args_count': len(args),
                    'kwargs_count': len(kwargs)
                })
            
            try:
                result = func(*args, **kwargs)
                return result
            except Exception as e:
                if track_errors:
                    tracker.track_error(str(e), {
                        'function_name': func.__name__,
                        'error_type': type(e).__name__
                    })
                raise
        
        return wrapper
    return decorator

@contextmanager
def knowledge_context(context_name: str, track_interactions: bool = True):
    """知识上下文管理器"""
    tracker = KnowledgeTracker()
    
    # 记录上下文开始
    start_time = datetime.now()
    context_id = tracker.kg_manager.add_entity(
        name=context_name,
        entity_type='context',
        properties={
            'start_time': start_time.isoformat(),
            'status': 'active'
        },
        confidence=0.9,
        source="context_management"
    )
    
    try:
        yield tracker
    except Exception as e:
        # 记录上下文错误
        tracker.track_error(str(e), {
            'context_name': context_name,
            'context_id': context_id
        })
        raise
    finally:
        # 记录上下文结束
        end_time = datetime.now()
        duration = (end_time - start_time).total_seconds()
        
        # 更新上下文实体
        if context_id in tracker.kg_manager.entities:
            entity = tracker.kg_manager.entities[context_id]
            entity.properties.update({
                'end_time': end_time.isoformat(),
                'duration': duration,
                'status': 'completed'
            })
            entity.updated_at = end_time.isoformat()

def main():
    """测试知识图谱集成功能"""
    print("=== 知识图谱集成测试 ===")
    
    # 初始化跟踪器
    tracker = KnowledgeTracker()
    
    # 测试代码跟踪
    print("\n1. 测试代码跟踪:")
    sample_code = """
def example_function():
    import json
    from datetime import datetime
    
    data = {'key': 'value'}
    result = json.dumps(data)
    return result
"""
    
    entities = tracker.track_code_execution(sample_code)
    print(f"   提取了 {len(entities)} 个实体")
    
    # 测试错误跟踪
    print("\n2. 测试错误跟踪:")
    error_msg = 'File "/path/to/file.py", line 10, in function\n    ValueError: invalid value'
    error_entities = tracker.track_error(error_msg)
    print(f"   提取了 {len(error_entities)} 个错误相关实体")
    
    # 测试用户交互跟踪
    print("\n3. 测试用户交互跟踪:")
    interaction = {
        'input': 'Create a Python function to parse JSON data',
        'action': 'code_generation',
        'success': True,
        'timestamp': datetime.now().isoformat()
    }
    interaction_entities = tracker.track_user_interaction(interaction)
    print(f"   提取了 {len(interaction_entities)} 个交互实体")
    
    # 测试推荐系统
    print("\n4. 测试推荐系统:")
    recommendations = tracker.get_recommendations()
    print(f"   生成了 {len(recommendations)} 个推荐")
    for i, rec in enumerate(recommendations[:3], 1):
        if 'relation_type' in rec:
            print(f"   {i}. 建议关系: {rec['relation_type']} (置信度: {rec['confidence']:.2f})")
        else:
            print(f"   {i}. {rec.get('description', 'Unknown recommendation')}")
    
    # 获取状态
    print("\n5. 知识图谱状态:")
    status = tracker.get_status()
    if status:
        print(f"   实体数量: {status.get('entities', {}).get('total', 0)}")
        print(f"   关系数量: {status.get('relations', {}).get('total', 0)}")
        print(f"   推理关系: {status.get('reasoning', {}).get('inferred_relations', 0)}")
    
    print("\n=== 测试完成 ===")

if __name__ == "__main__":
    main()