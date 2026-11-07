"""Parse the upstream awesome list without maintaining a second database."""
from __future__ import annotations
import re
from dataclasses import dataclass
from pathlib import Path
import requests

REPO = 'https://github.com/InessaPawson/awesome-open-source-ai'
RAW = 'https://raw.githubusercontent.com/InessaPawson/awesome-open-source-ai/main/README.md'
LOCAL = Path(__file__).with_name('README.snapshot.md')

@dataclass(frozen=True)
class Project:
    name: str
    url: str
    description: str
    area: str
    category: str
    status: str


def read_readme(live: bool = True) -> tuple[str, str]:
    if live:
        try:
            resp = requests.get(RAW, timeout=8, headers={'User-Agent':'awesome-open-source-ai-explorer/1.0'})
            resp.raise_for_status()
            if '## Foundations' in resp.text:
                return resp.text, 'Live GitHub README'
        except requests.RequestException:
            pass
    return LOCAL.read_text(encoding='utf-8'), 'Bundled snapshot (offline fallback)'


def parse_projects(markdown: str) -> list[Project]:
    area, category = '', ''
    projects = []
    seen = set()
    # Supports both standard markdown links and bullet text with an explicit GitHub URL.
    link = re.compile(r'^\s*[-*]\s+\[([^\]]+)\]\((https?://[^)]+)\)\s*(?:[-–—:]\s*)?(.*)$')
    for line in markdown.splitlines():
        line = line.strip()
        if line.startswith('## '):
            area = re.sub(r'\s+#+$', '', line[3:]).strip()
            category = ''
        elif line.startswith('### '):
            category = re.sub(r'\s+#+$', '', line[4:]).strip()
        elif area and category:
            match = link.match(line)
            if not match:
                continue
            name, url, description = match.groups()
            if url in seen:
                continue
            seen.add(url)
            desc = re.sub(r'\s+', ' ', description).strip()
            status = 'Archived' if re.search(r'\barchived\b', desc, re.I) else ('Inactive' if re.search(r'not actively maintained|development wound down', desc, re.I) else 'Listed')
            projects.append(Project(name.strip(), url.strip(), desc, area, category, status))
    return projects


def search_projects(projects: list[Project], query: str = '', areas: list[str] | None = None,
                    categories: list[str] | None = None, statuses: list[str] | None = None) -> list[Project]:
    tokens = query.lower().split()
    return [p for p in projects
            if (not areas or p.area in areas)
            and (not categories or p.category in categories)
            and (not statuses or p.status in statuses)
            and all(t in f'{p.name} {p.description} {p.area} {p.category}'.lower() for t in tokens)]
