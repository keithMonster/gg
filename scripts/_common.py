"""共享常量和工具函数。python3 标准库零依赖。

职责边界：本模块只提供"数据层"工具——文件遍历、路径分类、引用提取。
不做任何语义判断（是否应该修、是否漂移、是否矛盾）。
"""
from __future__ import annotations
import os
import re
from pathlib import Path

# gg 项目根（scripts/ 的上一级）
ROOT = Path(__file__).resolve().parent.parent

# 归档目录：里面的死链/漂移是时间戳的自然结果，脚本不报
ARCHIVE_PREFIXES = (
    "memory/archival/",
    "memory/design_sessions/",
    "memory/reflections/",
    "memory/audit/",
    "memory/auto_gg/",
)

# 入口文件：它们是被外部 Read 的，不需要被其他文件"引用"才算活着
ENTRY_FILES = frozenset({
    "README.md", "KERNEL.md", "CLAUDE.md", "CORE.md",
    "cc_agent.md", "auto_gg.md", "constitution.md",
    "daily_knowledge.md", "reasoning_modules.md",
})

# 跨项目前缀：这些不是死链，是指向别的仓库
CROSS_PROJECT_PREFIXES = (
    "cc-space/",
    "harness-engineering/",
    "gg/.claude/",  # 历史会话里出现过的完整项目路径
)

# 噪音模式：glob / 占位符 / 模板日期 / 正则转义 / 示例
NOISE_CHARS = set("*?<>{}[]\\")
NOISE_TOKENS = re.compile(r"\bYYYY\b|\bMM\b|\bDD\b|\bHN\b|\bpath/to\b|pattern-X")

# 引用提取正则
MD_LINK_RE = re.compile(r"\[([^\]]*)\]\(([^)]+)\)")
BACKTICK_MD_RE = re.compile(r"`([^`\s]+\.md)`")


def is_archive(rel_path: str) -> bool:
    """rel_path 以归档目录前缀开头"""
    return any(rel_path.startswith(p) for p in ARCHIVE_PREFIXES)


def is_noise_target(target: str) -> bool:
    """target 是 glob / 占位符 / 模板 / 正则 / 示例——不参与死链检查"""
    if any(c in target for c in NOISE_CHARS):
        return True
    if NOISE_TOKENS.search(target):
        return True
    return False


def is_cross_project(target: str) -> bool:
    return any(target.startswith(p) for p in CROSS_PROJECT_PREFIXES)


def walk_md_files(root: Path = ROOT, include_archive: bool = True):
    """产出所有 .md 文件的相对路径（POSIX 风格）"""
    for dp, dns, fns in os.walk(root):
        dns[:] = [d for d in dns if d != ".git"]
        for fn in fns:
            if not fn.endswith(".md"):
                continue
            full = Path(dp) / fn
            rel = full.relative_to(root).as_posix()
            if not include_archive and is_archive(rel):
                continue
            yield rel


def extract_refs(file_rel: str, line: str):
    """从一行文本提取所有 .md 引用。
    返回 [(kind, raw_target)] —— kind ∈ {'md-link', 'backtick'}。
    已过滤：外部协议（http/mailto）、绝对路径、锚点、home（~）。
    未过滤：噪音模式和跨项目——留给上层按需分流。
    """
    out = []
    for m in MD_LINK_RE.finditer(line):
        t = m.group(2).strip()
        if t.startswith(("http://", "https://", "#", "mailto:", "tel:", "/", "~")):
            continue
        t_clean = t.split("#")[0]
        if not t_clean.endswith(".md"):
            continue
        out.append(("md-link", t_clean))
    for m in BACKTICK_MD_RE.finditer(line):
        t = m.group(1).strip()
        if t.startswith(("http://", "https://", "/", "~")):
            continue
        t_clean = t.split("#")[0]
        out.append(("backtick", t_clean))
    return out


def resolve_target(src_rel: str, target: str) -> tuple[str, str]:
    """返回 (相对 src 的绝对路径, 相对 ROOT 的绝对路径) —— 两者只要有一个存在即非死链"""
    src_dir = (ROOT / src_rel).parent
    from_src = (src_dir / target).resolve()
    from_root = (ROOT / target).resolve()
    return str(from_src), str(from_root)
