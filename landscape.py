"""Deterministic, unambiguous catalog-only network for the Streamlit Landscape view."""
from __future__ import annotations

from collections import Counter
from typing import Sequence

import plotly.graph_objects as go

from catalog import Project


def category_counts(projects: Sequence[Project]) -> dict[str, int]:
    """Count listings per category in case-insensitive alphabetical order."""
    counts = Counter(p.category for p in projects)
    return dict(sorted(counts.items(), key=lambda row: row[0].casefold()))


def landscape_nodes(projects: Sequence[Project], area: str) -> tuple[list[dict], list[tuple[str, str]]]:
    """Stable, uniquely keyed nodes and edges for an area/category/project hierarchy.

    Category identifiers include the area; project identifiers use repository URLs.
    This avoids ambiguous edges for projects with duplicate display names.
    """
    subset = [p for p in projects if p.area == area]
    counts = category_counts(subset)
    nodes: list[dict] = []
    edges: list[tuple[str, str]] = []
    area_id = f"area:{area}"
    total = len(subset)
    nodes.append({"id": area_id, "kind": "area", "label": area, "category": "", "x": 0, "y": (total - 1) / 2 if total else 0, "count": total, "url": ""})
    offset = 0
    for cat, n in counts.items():
        cat_id = f"category:{area}:{cat}"
        midpoint = offset + (n - 1) / 2
        nodes.append({"id": cat_id, "kind": "category", "label": cat, "category": cat, "x": 1, "y": midpoint, "count": n, "url": ""})
        edges.append((area_id, cat_id))
        ordered = sorted((p for p in subset if p.category == cat), key=lambda p: (p.name.casefold(), p.url))
        for index, p in enumerate(ordered):
            project_id = f"project:{p.url}"
            nodes.append({"id": project_id, "kind": "project", "label": p.name, "category": cat, "x": 2, "y": offset + index, "count": 1, "url": p.url})
            edges.append((cat_id, project_id))
        offset += n
    return nodes, edges


def build_landscape(projects: Sequence[Project], area: str, highlight_category: str | None = None) -> go.Figure:
    """Build a readable three-column category membership diagram.

    The x/y coordinates are for layout only, not ranking or similarity.
    """
    nodes, edges = landscape_nodes(projects, area)
    by_id = {node["id"]: node for node in nodes}
    fig = go.Figure()
    for source, target in edges:
        start, end = by_id[source], by_id[target]
        emphasized = highlight_category is None or end["category"] == highlight_category or (end["kind"] == "category" and end["label"] == highlight_category)
        fig.add_trace(go.Scatter(
            x=[start["x"], end["x"]], y=[start["y"], end["y"]],
            mode="lines", line={"color": "#B6C8EF" if emphasized else "#E8EDF7", "width": 1.5 if emphasized else 0.7},
            hoverinfo="skip", showlegend=False,
        ))
    for kind, color in (("area", "#082B80"), ("category", "#FF8B73"), ("project", "#5275F7")):
        members = [node for node in nodes if node["kind"] == kind]
        if not members:
            continue
        sizes = [max(17, min(40, 14 + node["count"] * 2.5)) if kind == "category" else (28 if kind == "area" else 11) for node in members]
        opacity = [1.0 if highlight_category is None or kind == "area" or node["category"] == highlight_category else 0.24 for node in members]
        fig.add_trace(go.Scatter(
            x=[node["x"] for node in members], y=[node["y"] for node in members],
            mode="markers+text" if kind != "project" else "markers",
            text=[node["label"] for node in members] if kind != "project" else None,
            textposition="middle left", textfont={"size": 11, "color": "#082B80"},
            name=kind.title(),
            marker={"size": sizes, "color": color, "opacity": opacity, "line": {"color": "white", "width": 1.5}},
            customdata=[[node["kind"], node["url"], node["category"], node["label"]] for node in members],
            hovertemplate="<b>%{customdata[2]}</b><br>%{text}<extra></extra>" if kind == "category" else ("<b>%{text}</b><extra></extra>" if kind == "area" else "<b>%{customdata[3]}</b><br>%{customdata[2]}<br>%{customdata[1]}<extra></extra>"),
            hovertext=[node["label"] for node in members],
            selected={"marker": {"opacity": 1}}, unselected={"marker": {"opacity": 0.35}},
        ))
    fig.update_layout(
        height=max(460, len([n for n in nodes if n["kind"] == "project"]) * 27),
        paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
        margin={"l": 30, "r": 30, "t": 42, "b": 16},
        xaxis={"tickvals": [0, 1, 2], "ticktext": ["Area", "Category", "Project"], "side": "top", "range": [-0.12, 2.12], "fixedrange": True, "showgrid": False, "zeroline": False},
        yaxis={"visible": False, "autorange": "reversed", "fixedrange": True},
        showlegend=False, dragmode="select", clickmode="event+select",
    )
    return fig
