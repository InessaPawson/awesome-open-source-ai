"""Optional GitHub repository metadata. Never infer it from a project name."""
from __future__ import annotations

from urllib.parse import urlparse
import requests


@__import__('functools').lru_cache(maxsize=512)
def github_metadata(owner: str, repo: str) -> dict:
    try:
        response = requests.get(f"https://api.github.com/repos/{owner}/{repo}", timeout=8,
                                headers={"Accept": "application/vnd.github+json", "User-Agent": "OpenTeams-AI-Explorer"})
        if response.status_code == 403 and response.headers.get("X-RateLimit-Remaining") == "0":
            return {"error": "GitHub API rate limit reached"}
        response.raise_for_status()
        data = response.json()
        return {key: data.get(key) for key in ("language", "license", "stargazers_count", "open_issues_count", "pushed_at", "archived")}
    except (requests.RequestException, ValueError) as exc:
        return {"error": str(exc)[:160]}


def project_metadata(url: str) -> dict:
    parsed = urlparse(url)
    parts = parsed.path.strip("/").split("/")
    if parsed.hostname not in ("github.com", "www.github.com") or len(parts) < 2:
        return {"error": "GitHub metadata only available for GitHub repositories"}
    return github_metadata(parts[0], parts[1].removesuffix(".git"))
