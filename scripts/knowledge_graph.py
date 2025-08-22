#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
知识图谱构建和管理系统

功能:
- 知识实体提取和关系建模
- 图谱构建和更新
- 知识查询和推理
- 知识可视化
- 知识质量评估
"""

import json
import os
import sys
import logging
import argparse
from datetime import datetime, timedelta
from typing import Dict, List, Any, Optional, Tuple, Set
from dataclasses import dataclass, asdict
from collections import defaultdict, Counter
import hashlib
import re

# 添加项目根目录到路径
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

@dataclass
class KnowledgeEntity:
    """知识实体"""
    id: str
    name: str
    type: str
    properties: Dict[str, Any]
    confidence: float
    created_at: str
    updated_at: str
    source: str
    
    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)

@dataclass
class KnowledgeRelation:
    """知识关系"""
    id: str
    source_id: str
    target_id: str
    relation_type: str
    properties: Dict[str, Any]
    confidence: float
    created_at: str
    updated_at: str
    source: str
    
    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)

@dataclass
class KnowledgeQuery:
    """知识查询"""
    query_id: str
    query_text: str
    query_type: str  # entity, relation, path, pattern
    parameters: Dict[str, Any]
    timestamp: str
    
    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)

@dataclass
class KnowledgeInsight:
    """知识洞察"""
    insight_id: str
    title: str
    description: str
    insight_type: str  # pattern, anomaly, trend, recommendation
    confidence: float
    evidence: List[str]
    created_at: str
    
    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)

class KnowledgeGraphManager:
    """知识图谱管理器"""
    
    def __init__(self, config_path: str = "config/knowledge_config.json"):
        self.config_path = config_path
        self.config = self._load_config()
        self.data_dir = self.config.get('data_directory', 'data/knowledge')
        self.entities_file = os.path.join(self.data_dir, 'entities.json')
        self.relations_file = os.path.join(self.data_dir, 'relations.json')
        self.queries_file = os.path.join(self.data_dir, 'queries.json')
        self.insights_file = os.path.join(self.data_dir, 'insights.json')
        
        # 确保数据目录存在
        os.makedirs(self.data_dir, exist_ok=True)
        
        # 初始化数据结构
        self.entities: Dict[str, KnowledgeEntity] = {}
        self.relations: Dict[str, KnowledgeRelation] = {}
        self.queries: List[KnowledgeQuery] = []
        self.insights: List[KnowledgeInsight] = []
        
        # 加载现有数据
        self._load_data()
        
        # 设置日志
        self._setup_logging()
    
    def _load_config(self) -> Dict[str, Any]:
        """加载配置"""
        if os.path.exists(self.config_path):
            with open(self.config_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        return {
            'data_directory': 'data/knowledge',
            'entity_types': ['concept', 'skill', 'tool', 'pattern', 'problem', 'solution'],
            'relation_types': ['uses', 'requires', 'implements', 'solves', 'related_to', 'part_of'],
            'confidence_threshold': 0.7,
            'max_entities': 10000,
            'max_relations': 50000,
            'retention_days': 365
        }
    
    def _setup_logging(self):
        """设置日志"""
        log_dir = "logs"
        os.makedirs(log_dir, exist_ok=True)
        
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler(os.path.join(log_dir, 'knowledge_graph.log')),
                logging.StreamHandler()
            ]
        )
        self.logger = logging.getLogger(__name__)
    
    def _load_data(self):
        """加载数据"""
        # 加载实体
        if os.path.exists(self.entities_file):
            with open(self.entities_file, 'r', encoding='utf-8') as f:
                entities_data = json.load(f)
                for entity_data in entities_data:
                    entity = KnowledgeEntity(**entity_data)
                    self.entities[entity.id] = entity
        
        # 加载关系
        if os.path.exists(self.relations_file):
            with open(self.relations_file, 'r', encoding='utf-8') as f:
                relations_data = json.load(f)
                for relation_data in relations_data:
                    relation = KnowledgeRelation(**relation_data)
                    self.relations[relation.id] = relation
        
        # 加载查询历史
        if os.path.exists(self.queries_file):
            with open(self.queries_file, 'r', encoding='utf-8') as f:
                queries_data = json.load(f)
                self.queries = [KnowledgeQuery(**query_data) for query_data in queries_data]
        
        # 加载洞察
        if os.path.exists(self.insights_file):
            with open(self.insights_file, 'r', encoding='utf-8') as f:
                insights_data = json.load(f)
                self.insights = [KnowledgeInsight(**insight_data) for insight_data in insights_data]
    
    def _save_data(self):
        """保存数据"""
        # 保存实体
        with open(self.entities_file, 'w', encoding='utf-8') as f:
            json.dump([entity.to_dict() for entity in self.entities.values()], f, indent=2, ensure_ascii=False)
        
        # 保存关系
        with open(self.relations_file, 'w', encoding='utf-8') as f:
            json.dump([relation.to_dict() for relation in self.relations.values()], f, indent=2, ensure_ascii=False)
        
        # 保存查询历史
        with open(self.queries_file, 'w', encoding='utf-8') as f:
            json.dump([query.to_dict() for query in self.queries], f, indent=2, ensure_ascii=False)
        
        # 保存洞察
        with open(self.insights_file, 'w', encoding='utf-8') as f:
            json.dump([insight.to_dict() for insight in self.insights], f, indent=2, ensure_ascii=False)
    
    def add_entity(self, name: str, entity_type: str, properties: Dict[str, Any] = None, 
                   confidence: float = 1.0, source: str = "manual") -> str:
        """添加知识实体"""
        entity_id = hashlib.md5(f"{name}_{entity_type}".encode()).hexdigest()[:16]
        
        if entity_id in self.entities:
            # 更新现有实体
            entity = self.entities[entity_id]
            entity.properties.update(properties or {})
            entity.confidence = max(entity.confidence, confidence)
            entity.updated_at = datetime.now().isoformat()
        else:
            # 创建新实体
            entity = KnowledgeEntity(
                id=entity_id,
                name=name,
                type=entity_type,
                properties=properties or {},
                confidence=confidence,
                created_at=datetime.now().isoformat(),
                updated_at=datetime.now().isoformat(),
                source=source
            )
            self.entities[entity_id] = entity
        
        self._save_data()
        self.logger.info(f"Added/Updated entity: {name} ({entity_type})")
        return entity_id
    
    def add_relation(self, source_id: str, target_id: str, relation_type: str, 
                     properties: Dict[str, Any] = None, confidence: float = 1.0, 
                     source: str = "manual") -> str:
        """添加知识关系"""
        relation_id = hashlib.md5(f"{source_id}_{relation_type}_{target_id}".encode()).hexdigest()[:16]
        
        if relation_id in self.relations:
            # 更新现有关系
            relation = self.relations[relation_id]
            relation.properties.update(properties or {})
            relation.confidence = max(relation.confidence, confidence)
            relation.updated_at = datetime.now().isoformat()
        else:
            # 创建新关系
            relation = KnowledgeRelation(
                id=relation_id,
                source_id=source_id,
                target_id=target_id,
                relation_type=relation_type,
                properties=properties or {},
                confidence=confidence,
                created_at=datetime.now().isoformat(),
                updated_at=datetime.now().isoformat(),
                source=source
            )
            self.relations[relation_id] = relation
        
        self._save_data()
        self.logger.info(f"Added/Updated relation: {source_id} -{relation_type}-> {target_id}")
        return relation_id
    
    def query_entities(self, entity_type: str = None, name_pattern: str = None, 
                       min_confidence: float = 0.0) -> List[KnowledgeEntity]:
        """查询实体"""
        results = []
        
        for entity in self.entities.values():
            if entity_type and entity.type != entity_type:
                continue
            if name_pattern and not re.search(name_pattern, entity.name, re.IGNORECASE):
                continue
            if entity.confidence < min_confidence:
                continue
            
            results.append(entity)
        
        # 记录查询
        query = KnowledgeQuery(
            query_id=hashlib.md5(f"entities_{datetime.now().isoformat()}".encode()).hexdigest()[:16],
            query_text=f"type={entity_type}, pattern={name_pattern}, min_confidence={min_confidence}",
            query_type="entity",
            parameters={
                "entity_type": entity_type,
                "name_pattern": name_pattern,
                "min_confidence": min_confidence
            },
            timestamp=datetime.now().isoformat()
        )
        self.queries.append(query)
        
        return sorted(results, key=lambda x: x.confidence, reverse=True)
    
    def query_relations(self, source_id: str = None, target_id: str = None, 
                        relation_type: str = None, min_confidence: float = 0.0) -> List[KnowledgeRelation]:
        """查询关系"""
        results = []
        
        for relation in self.relations.values():
            if source_id and relation.source_id != source_id:
                continue
            if target_id and relation.target_id != target_id:
                continue
            if relation_type and relation.relation_type != relation_type:
                continue
            if relation.confidence < min_confidence:
                continue
            
            results.append(relation)
        
        # 记录查询
        query = KnowledgeQuery(
            query_id=hashlib.md5(f"relations_{datetime.now().isoformat()}".encode()).hexdigest()[:16],
            query_text=f"source={source_id}, target={target_id}, type={relation_type}, min_confidence={min_confidence}",
            query_type="relation",
            parameters={
                "source_id": source_id,
                "target_id": target_id,
                "relation_type": relation_type,
                "min_confidence": min_confidence
            },
            timestamp=datetime.now().isoformat()
        )
        self.queries.append(query)
        
        return sorted(results, key=lambda x: x.confidence, reverse=True)
    
    def find_path(self, source_id: str, target_id: str, max_depth: int = 3) -> List[List[str]]:
        """查找实体间路径"""
        paths = []
        visited = set()
        
        def dfs(current_id: str, path: List[str], depth: int):
            if depth > max_depth:
                return
            
            if current_id == target_id and len(path) > 1:
                paths.append(path.copy())
                return
            
            if current_id in visited:
                return
            
            visited.add(current_id)
            
            # 查找从当前节点出发的关系
            for relation in self.relations.values():
                if relation.source_id == current_id:
                    next_path = path + [relation.relation_type, relation.target_id]
                    dfs(relation.target_id, next_path, depth + 1)
            
            visited.remove(current_id)
        
        dfs(source_id, [source_id], 0)
        
        # 记录查询
        query = KnowledgeQuery(
            query_id=hashlib.md5(f"path_{datetime.now().isoformat()}".encode()).hexdigest()[:16],
            query_text=f"path from {source_id} to {target_id}, max_depth={max_depth}",
            query_type="path",
            parameters={
                "source_id": source_id,
                "target_id": target_id,
                "max_depth": max_depth
            },
            timestamp=datetime.now().isoformat()
        )
        self.queries.append(query)
        
        return paths
    
    def analyze_patterns(self) -> List[KnowledgeInsight]:
        """分析知识模式"""
        insights = []
        
        # 分析实体类型分布
        entity_types = Counter(entity.type for entity in self.entities.values())
        if entity_types:
            most_common_type = entity_types.most_common(1)[0]
            insight = KnowledgeInsight(
                insight_id=hashlib.md5(f"entity_distribution_{datetime.now().isoformat()}".encode()).hexdigest()[:16],
                title="实体类型分布分析",
                description=f"最常见的实体类型是 '{most_common_type[0]}'，占比 {most_common_type[1]/len(self.entities)*100:.1f}%",
                insight_type="pattern",
                confidence=0.9,
                evidence=[f"实体类型统计: {dict(entity_types)}"],
                created_at=datetime.now().isoformat()
            )
            insights.append(insight)
        
        # 分析关系类型分布
        relation_types = Counter(relation.relation_type for relation in self.relations.values())
        if relation_types:
            most_common_relation = relation_types.most_common(1)[0]
            insight = KnowledgeInsight(
                insight_id=hashlib.md5(f"relation_distribution_{datetime.now().isoformat()}".encode()).hexdigest()[:16],
                title="关系类型分布分析",
                description=f"最常见的关系类型是 '{most_common_relation[0]}'，占比 {most_common_relation[1]/len(self.relations)*100:.1f}%",
                insight_type="pattern",
                confidence=0.9,
                evidence=[f"关系类型统计: {dict(relation_types)}"],
                created_at=datetime.now().isoformat()
            )
            insights.append(insight)
        
        # 分析连接度
        node_degrees = defaultdict(int)
        for relation in self.relations.values():
            node_degrees[relation.source_id] += 1
            node_degrees[relation.target_id] += 1
        
        if node_degrees:
            max_degree_node = max(node_degrees.items(), key=lambda x: x[1])
            if max_degree_node[0] in self.entities:
                entity_name = self.entities[max_degree_node[0]].name
                insight = KnowledgeInsight(
                    insight_id=hashlib.md5(f"connectivity_{datetime.now().isoformat()}".encode()).hexdigest()[:16],
                    title="连接度分析",
                    description=f"'{entity_name}' 是连接度最高的实体，有 {max_degree_node[1]} 个连接",
                    insight_type="pattern",
                    confidence=0.8,
                    evidence=[f"节点连接度: {dict(sorted(node_degrees.items(), key=lambda x: x[1], reverse=True)[:5])}"],
                    created_at=datetime.now().isoformat()
                )
                insights.append(insight)
        
        # 保存洞察
        self.insights.extend(insights)
        self._save_data()
        
        return insights
    
    def get_statistics(self) -> Dict[str, Any]:
        """获取统计信息"""
        entity_types = Counter(entity.type for entity in self.entities.values())
        relation_types = Counter(relation.relation_type for relation in self.relations.values())
        
        # 计算平均置信度
        avg_entity_confidence = sum(entity.confidence for entity in self.entities.values()) / len(self.entities) if self.entities else 0
        avg_relation_confidence = sum(relation.confidence for relation in self.relations.values()) / len(self.relations) if self.relations else 0
        
        # 计算连接度统计
        node_degrees = defaultdict(int)
        for relation in self.relations.values():
            node_degrees[relation.source_id] += 1
            node_degrees[relation.target_id] += 1
        
        avg_degree = sum(node_degrees.values()) / len(node_degrees) if node_degrees else 0
        max_degree = max(node_degrees.values()) if node_degrees else 0
        
        return {
            "entities": {
                "total": len(self.entities),
                "types": dict(entity_types),
                "avg_confidence": round(avg_entity_confidence, 3)
            },
            "relations": {
                "total": len(self.relations),
                "types": dict(relation_types),
                "avg_confidence": round(avg_relation_confidence, 3)
            },
            "connectivity": {
                "avg_degree": round(avg_degree, 2),
                "max_degree": max_degree,
                "connected_nodes": len(node_degrees)
            },
            "queries": {
                "total": len(self.queries),
                "recent_24h": len([q for q in self.queries if 
                                  datetime.fromisoformat(q.timestamp) > datetime.now() - timedelta(days=1)])
            },
            "insights": {
                "total": len(self.insights),
                "recent_7d": len([i for i in self.insights if 
                                 datetime.fromisoformat(i.created_at) > datetime.now() - timedelta(days=7)])
            }
        }
    
    def export_graph(self, format_type: str = "json") -> str:
        """导出知识图谱"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        
        if format_type == "json":
            export_data = {
                "metadata": {
                    "export_time": datetime.now().isoformat(),
                    "version": "1.0",
                    "statistics": self.get_statistics()
                },
                "entities": [entity.to_dict() for entity in self.entities.values()],
                "relations": [relation.to_dict() for relation in self.relations.values()],
                "insights": [insight.to_dict() for insight in self.insights]
            }
            
            export_path = f"outputs/knowledge/knowledge_graph_export_{timestamp}.json"
            os.makedirs(os.path.dirname(export_path), exist_ok=True)
            
            with open(export_path, 'w', encoding='utf-8') as f:
                json.dump(export_data, f, indent=2, ensure_ascii=False)
            
            return export_path
        
        elif format_type == "graphml":
            # 简化的GraphML格式
            graphml_content = ['<?xml version="1.0" encoding="UTF-8"?>']
            graphml_content.append('<graphml xmlns="http://graphml.graphdrawing.org/xmlns">')
            graphml_content.append('<graph id="knowledge_graph" edgedefault="directed">')
            
            # 添加节点
            for entity in self.entities.values():
                graphml_content.append(f'<node id="{entity.id}">')
                graphml_content.append(f'<data key="name">{entity.name}</data>')
                graphml_content.append(f'<data key="type">{entity.type}</data>')
                graphml_content.append(f'<data key="confidence">{entity.confidence}</data>')
                graphml_content.append('</node>')
            
            # 添加边
            for relation in self.relations.values():
                graphml_content.append(f'<edge source="{relation.source_id}" target="{relation.target_id}">')
                graphml_content.append(f'<data key="type">{relation.relation_type}</data>')
                graphml_content.append(f'<data key="confidence">{relation.confidence}</data>')
                graphml_content.append('</edge>')
            
            graphml_content.append('</graph>')
            graphml_content.append('</graphml>')
            
            export_path = f"outputs/knowledge/knowledge_graph_export_{timestamp}.graphml"
            os.makedirs(os.path.dirname(export_path), exist_ok=True)
            
            with open(export_path, 'w', encoding='utf-8') as f:
                f.write('\n'.join(graphml_content))
            
            return export_path
        
        else:
            raise ValueError(f"Unsupported export format: {format_type}")
    
    def cleanup_old_data(self, days: int = None):
        """清理旧数据"""
        if days is None:
            days = self.config.get('retention_days', 365)
        
        cutoff_date = datetime.now() - timedelta(days=days)
        
        # 清理旧查询
        old_queries = [q for q in self.queries if datetime.fromisoformat(q.timestamp) < cutoff_date]
        self.queries = [q for q in self.queries if datetime.fromisoformat(q.timestamp) >= cutoff_date]
        
        # 清理旧洞察
        old_insights = [i for i in self.insights if datetime.fromisoformat(i.created_at) < cutoff_date]
        self.insights = [i for i in self.insights if datetime.fromisoformat(i.created_at) >= cutoff_date]
        
        self._save_data()
        
        self.logger.info(f"Cleaned up {len(old_queries)} old queries and {len(old_insights)} old insights")
        
        return {
            "cleaned_queries": len(old_queries),
            "cleaned_insights": len(old_insights),
            "remaining_queries": len(self.queries),
            "remaining_insights": len(self.insights)
        }

def main():
    parser = argparse.ArgumentParser(description='知识图谱管理系统')
    parser.add_argument('command', choices=[
        'stats', 'entities', 'relations', 'path', 'analyze', 'export', 'cleanup'
    ], help='要执行的命令')
    parser.add_argument('--type', help='实体或关系类型')
    parser.add_argument('--pattern', help='名称模式')
    parser.add_argument('--source', help='源实体ID')
    parser.add_argument('--target', help='目标实体ID')
    parser.add_argument('--confidence', type=float, default=0.0, help='最小置信度')
    parser.add_argument('--depth', type=int, default=3, help='最大搜索深度')
    parser.add_argument('--format', default='json', choices=['json', 'graphml'], help='导出格式')
    parser.add_argument('--days', type=int, help='数据保留天数')
    
    args = parser.parse_args()
    
    # 初始化知识图谱管理器
    kg_manager = KnowledgeGraphManager()
    
    if args.command == 'stats':
        stats = kg_manager.get_statistics()
        print(json.dumps(stats, indent=2, ensure_ascii=False))
    
    elif args.command == 'entities':
        entities = kg_manager.query_entities(
            entity_type=args.type,
            name_pattern=args.pattern,
            min_confidence=args.confidence
        )
        print(f"找到 {len(entities)} 个实体:")
        for entity in entities[:10]:  # 限制显示前10个
            print(f"- {entity.name} ({entity.type}) [置信度: {entity.confidence}]")
    
    elif args.command == 'relations':
        relations = kg_manager.query_relations(
            source_id=args.source,
            target_id=args.target,
            relation_type=args.type,
            min_confidence=args.confidence
        )
        print(f"找到 {len(relations)} 个关系:")
        for relation in relations[:10]:  # 限制显示前10个
            source_name = kg_manager.entities.get(relation.source_id, {}).name if relation.source_id in kg_manager.entities else relation.source_id
            target_name = kg_manager.entities.get(relation.target_id, {}).name if relation.target_id in kg_manager.entities else relation.target_id
            print(f"- {source_name} -{relation.relation_type}-> {target_name} [置信度: {relation.confidence}]")
    
    elif args.command == 'path':
        if not args.source or not args.target:
            print("错误: 路径查询需要指定 --source 和 --target")
            return
        
        paths = kg_manager.find_path(args.source, args.target, args.depth)
        print(f"找到 {len(paths)} 条路径:")
        for i, path in enumerate(paths[:5], 1):  # 限制显示前5条路径
            path_str = " -> ".join(path)
            print(f"{i}. {path_str}")
    
    elif args.command == 'analyze':
        insights = kg_manager.analyze_patterns()
        print(f"生成了 {len(insights)} 个洞察:")
        for insight in insights:
            print(f"\n{insight.title}:")
            print(f"  {insight.description}")
            print(f"  置信度: {insight.confidence}")
            print(f"  类型: {insight.insight_type}")
    
    elif args.command == 'export':
        export_path = kg_manager.export_graph(args.format)
        print(f"知识图谱已导出到: {export_path}")
    
    elif args.command == 'cleanup':
        result = kg_manager.cleanup_old_data(args.days)
        print(f"清理完成:")
        print(f"  清理的查询: {result['cleaned_queries']}")
        print(f"  清理的洞察: {result['cleaned_insights']}")
        print(f"  剩余查询: {result['remaining_queries']}")
        print(f"  剩余洞察: {result['remaining_insights']}")

if __name__ == "__main__":
    main()