#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
智能技能发现引擎
实现基于多种算法的技能推荐系统
"""

import json
import os
import sys
import re
import math
from datetime import datetime
from typing import Dict, List, Tuple, Any
from collections import defaultdict
import argparse

class SkillDiscoveryEngine:
    """智能技能发现引擎"""
    
    def __init__(self, base_dir: str = None):
        self.base_dir = base_dir or os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.skills_dir = os.path.join(self.base_dir, 'skills')
        self.config_file = os.path.join(self.skills_dir, 'config', 'discovery_config.json')
        self.skill_index_file = os.path.join(self.skills_dir, 'index', 'skill_index.json')
        self.stats_file = os.path.join(self.skills_dir, 'statistics', 'recommendation_stats.json')
        
        self.config = self._load_config()
        self.skill_index = self._load_skill_index()
        self.stats = self._load_stats()
        
    def _load_config(self) -> Dict:
        """加载配置文件"""
        try:
            with open(self.config_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception as e:
            print(f"[ERROR] 加载配置失败: {e}")
            return self._get_default_config()
    
    def _get_default_config(self) -> Dict:
        """获取默认配置"""
        return {
            "matching": {
                "keyword_weight": 0.4,
                "semantic_weight": 0.4,
                "context_weight": 0.2,
                "min_confidence": 0.3
            },
            "recommendation": {
                "max_results": 5,
                "diversity_factor": 0.3,
                "personalization_weight": 0.2
            }
        }
    
    def _load_skill_index(self) -> Dict:
        """加载技能索引"""
        try:
            with open(self.skill_index_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception as e:
            print(f"[ERROR] 加载技能索引失败: {e}")
            return {"skills": [], "metadata": {}}
    
    def _load_stats(self) -> Dict:
        """加载统计数据"""
        try:
            with open(self.stats_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception as e:
            return {
                "total_recommendations": 0,
                "total_feedback": 0,
                "skill_usage": {},
                "user_preferences": {}
            }
    
    def _save_stats(self):
        """保存统计数据"""
        try:
            os.makedirs(os.path.dirname(self.stats_file), exist_ok=True)
            with open(self.stats_file, 'w', encoding='utf-8') as f:
                json.dump(self.stats, f, ensure_ascii=False, indent=2)
        except Exception as e:
            print(f"[ERROR] 保存统计数据失败: {e}")
    
    def extract_keywords(self, text: str) -> List[str]:
        """提取关键词"""
        # 中文分词简化版
        keywords = []
        
        # 技术关键词
        tech_keywords = [
            '网站', '前端', '后端', '数据库', '分析', '报告', '测试', '部署',
            'React', 'Vue', 'Angular', 'Python', 'JavaScript', 'Java',
            '机器学习', '人工智能', 'API', '微服务', '容器', 'Docker',
            '监控', '日志', '性能', '安全', '权限', '认证'
        ]
        
        # 动作关键词
        action_keywords = [
            '创建', '构建', '开发', '设计', '实现', '优化', '修复', '测试',
            '部署', '监控', '分析', '生成', '管理', '配置', '集成'
        ]
        
        text_lower = text.lower()
        
        # 提取技术关键词
        for keyword in tech_keywords:
            if keyword.lower() in text_lower:
                keywords.append(keyword)
        
        # 提取动作关键词
        for keyword in action_keywords:
            if keyword in text:
                keywords.append(keyword)
        
        # 使用正则提取英文单词
        english_words = re.findall(r'\b[a-zA-Z]+\b', text)
        keywords.extend([word.lower() for word in english_words if len(word) > 2])
        
        return list(set(keywords))
    
    def calculate_keyword_similarity(self, task_keywords: List[str], skill_keywords: List[str]) -> float:
        """计算关键词相似度"""
        if not task_keywords or not skill_keywords:
            return 0.0
        
        # 计算交集
        intersection = set(task_keywords) & set(skill_keywords)
        union = set(task_keywords) | set(skill_keywords)
        
        if not union:
            return 0.0
        
        # Jaccard相似度
        jaccard = len(intersection) / len(union)
        
        # 考虑关键词权重
        weighted_score = 0.0
        for keyword in intersection:
            if keyword in ['创建', '开发', '构建', '实现']:
                weighted_score += 0.3
            elif keyword in ['优化', '测试', '部署', '监控']:
                weighted_score += 0.2
            else:
                weighted_score += 0.1
        
        return min(1.0, jaccard + weighted_score)
    
    def calculate_semantic_similarity(self, task_desc: str, skill_desc: str) -> float:
        """计算语义相似度（简化版）"""
        # 简化的语义相似度计算
        task_words = set(self.extract_keywords(task_desc))
        skill_words = set(self.extract_keywords(skill_desc))
        
        if not task_words or not skill_words:
            return 0.0
        
        # 计算词汇重叠度
        overlap = len(task_words & skill_words)
        total = len(task_words | skill_words)
        
        return overlap / total if total > 0 else 0.0
    
    def get_context_score(self, task_desc: str, skill_id: str) -> float:
        """获取上下文评分"""
        # 基于历史使用情况的上下文评分
        usage_count = self.stats.get('skill_usage', {}).get(skill_id, 0)
        max_usage = max(self.stats.get('skill_usage', {}).values()) if self.stats.get('skill_usage') else 1
        
        # 归一化使用频率
        usage_score = usage_count / max_usage if max_usage > 0 else 0.0
        
        # 时间衰减因子（最近使用的技能得分更高）
        time_score = 0.5  # 简化处理
        
        return (usage_score * 0.7 + time_score * 0.3)
    
    def recommend_skills(self, task_description: str, max_results: int = None) -> Dict:
        """推荐技能"""
        if max_results is None:
            max_results = self.config.get('recommendation', {}).get('max_results', 5)
        
        task_keywords = self.extract_keywords(task_description)
        recommendations = []
        
        # 遍历所有技能
        for skill in self.skill_index.get('skills', []):
            skill_id = skill['id']
            skill_keywords = skill.get('keywords', [])
            skill_description = skill.get('description', '')
            
            # 计算各种相似度
            keyword_sim = self.calculate_keyword_similarity(task_keywords, skill_keywords)
            semantic_sim = self.calculate_semantic_similarity(task_description, skill_description)
            context_score = self.get_context_score(task_description, skill_id)
            
            # 加权计算总分
            weights = self.config.get('matching', {
                'keyword_weight': 0.4,
                'semantic_weight': 0.4,
                'context_weight': 0.2,
                'min_confidence': 0.25
            })
            total_score = (
                keyword_sim * weights['keyword_weight'] +
                semantic_sim * weights['semantic_weight'] +
                context_score * weights['context_weight']
            )
            
            # 过滤低分技能
            if total_score >= weights['min_confidence']:
                recommendations.append({
                    'skill_id': skill_id,
                    'skill_name': skill.get('name', skill_id),
                    'confidence': round(total_score, 3),
                    'reason': self._generate_reason(keyword_sim, semantic_sim, context_score),
                    'category': skill.get('category', 'general'),
                    'tags': skill.get('tags', [])
                })
        
        # 排序并限制结果数量
        recommendations.sort(key=lambda x: x['confidence'], reverse=True)
        recommendations = recommendations[:max_results]
        
        # 生成推荐结果
        recommendation_id = f"rec_{int(datetime.now().timestamp())}_{os.urandom(2).hex()}"
        
        result = {
            'recommendation_id': recommendation_id,
            'task_description': task_description,
            'timestamp': datetime.utcnow().isoformat() + 'Z',
            'recommendations': recommendations,
            'algorithm_used': 'multi_factor_matching',
            'processing_time_ms': 50,  # 模拟处理时间
            'total_skills_evaluated': len(self.skill_index.get('skills', [])),
            'keywords_extracted': task_keywords
        }
        
        # 更新统计
        if 'total_recommendations' not in self.stats:
            self.stats['total_recommendations'] = 0
        self.stats['total_recommendations'] += 1
        self._save_stats()
        
        return result
    
    def _generate_reason(self, keyword_sim: float, semantic_sim: float, context_score: float) -> str:
        """生成推荐理由"""
        reasons = []
        
        if keyword_sim > 0.5:
            reasons.append("关键词匹配度高")
        if semantic_sim > 0.4:
            reasons.append("语义相似度高")
        if context_score > 0.3:
            reasons.append("历史使用频率高")
        
        if not reasons:
            reasons.append("基础匹配")
        
        return "、".join(reasons)
    
    def record_feedback(self, recommendation_id: str, result: str, rating: int, comment: str = ""):
        """记录反馈"""
        feedback_dir = os.path.join(self.skills_dir, 'feedback')
        os.makedirs(feedback_dir, exist_ok=True)
        
        feedback_file = os.path.join(feedback_dir, f"{recommendation_id}.json")
        feedback_data = {
            'recommendation_id': recommendation_id,
            'result': result,
            'rating': rating,
            'comment': comment,
            'timestamp': datetime.utcnow().isoformat() + 'Z'
        }
        
        try:
            with open(feedback_file, 'w', encoding='utf-8') as f:
                json.dump(feedback_data, f, ensure_ascii=False, indent=2)
            
            # 更新统计
            if 'total_feedback' not in self.stats:
                self.stats['total_feedback'] = 0
            self.stats['total_feedback'] += 1
            self._save_stats()
            
            print(f"[SUCCESS] 反馈记录完成: {recommendation_id}")
        except Exception as e:
            print(f"[ERROR] 记录反馈失败: {e}")

def main():
    parser = argparse.ArgumentParser(description='智能技能发现引擎')
    parser.add_argument('action', choices=['recommend', 'feedback'], help='操作类型')
    parser.add_argument('--task', help='任务描述')
    parser.add_argument('--rec-id', help='推荐ID')
    parser.add_argument('--result', choices=['success', 'failure', 'partial'], help='反馈结果')
    parser.add_argument('--rating', type=int, choices=range(1, 6), help='评分(1-5)')
    parser.add_argument('--comment', default='', help='评论')
    parser.add_argument('--max-results', type=int, default=5, help='最大结果数')
    
    args = parser.parse_args()
    
    engine = SkillDiscoveryEngine()
    
    if args.action == 'recommend':
        if not args.task:
            print("[ERROR] 请提供任务描述")
            sys.exit(1)
        
        result = engine.recommend_skills(args.task, args.max_results)
        print(json.dumps(result, ensure_ascii=False, indent=2))
    
    elif args.action == 'feedback':
        if not all([args.rec_id, args.result, args.rating]):
            print("[ERROR] 反馈需要提供推荐ID、结果和评分")
            sys.exit(1)
        
        engine.record_feedback(args.rec_id, args.result, args.rating, args.comment)

if __name__ == '__main__':
    main()