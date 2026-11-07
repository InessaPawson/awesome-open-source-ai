"""OpenTeams AI Explorer — discover, compare, visualize and contribute.

Run: python -m streamlit run app.py
"""
from __future__ import annotations

import json
from collections import Counter
from html import escape
from urllib.parse import quote

import pandas as pd
import plotly.graph_objects as go
import streamlit as st

from catalog import REPO, Project, parse_projects, read_readme, search_projects
from metadata import project_metadata

st.set_page_config(page_title="Open Source AI Explorer · OpenTeams", page_icon="✳️", layout="wide")

st.markdown("""<style>
:root {--navy:#082B80;--blue:#5275F7;--coral:#FF8B73;--orange:#FFB34F;--ink:#172549;--muted:#5C6A88;}
.stApp {background:#F7F9FE;color:var(--ink)}
.block-container {max-width:1450px;padding-top:1.5rem}
h1,h2,h3 {color:var(--navy);letter-spacing:-.025em}
[data-testid="stSidebar"] {background:#EFF3FF;border-right:1px solid #DCE5FC}
.hero {padding:34px;border-radius:20px;background:linear-gradient(110deg,#082B80,#19469D 60%,#5275F7);color:white;margin-bottom:18px;position:relative;overflow:hidden}
.hero:after {content:'';position:absolute;right:-35px;top:-100px;width:250px;height:250px;border:35px solid #FFFFFF1A;border-radius:50%}
.hero h1 {color:white;font-size:2.4rem;margin:6px 0 12px}
.hero p {color:#E1E9FF;margin:0;max-width:760px}
.hero .eyebrow {color:#FFCF91;text-transform:uppercase;letter-spacing:.14em;font-size:.8rem;font-weight:700}
[data-testid="stMetric"] {padding:13px 16px;background:white;border:1px solid #DFE6F6;border-radius:13px}
[data-testid="stMetricValue"] {color:var(--navy)}
[data-testid="stVerticalBlockBorderWrapper"] > div {border-color:#DFE6F6!important;border-radius:13px!important}
.stButton button[kind="primary"] {background:#5275F7;border-color:#5275F7}
.stLinkButton a {background:#F3F6FF;border-color:#B8C9F6;color:#082B80}
[data-testid="stCaptionContainer"] {color:#5C6A88}
.workflow {padding:13px 17px;background:white;border:1px solid #DFE6F6;border-radius:12px;margin-bottom:8px}
.workflow strong {color:#082B80}
.project-label {color:#5275F7;font-size:.8rem;font-weight:700}
@media(max-width:700px){.hero{padding:22px}.hero h1{font-size:1.7rem}.block-container{padding-left:1rem;padding-right:1rem}}
</style>""", unsafe_allow_html=True)


@st.cache_data(ttl=3600, show_spinner=False)
def load_catalog():
    markdown, provenance = read_readme(live=True)
    return parse_projects(markdown), provenance


projects, provenance = load_catalog()
by_url = {p.url: p for p in projects}
areas = list(dict.fromkeys(p.area for p in projects))

st.markdown("""<div class='hero'><div class='eyebrow'>OpenTeams / Open Source AI Explorer</div>
<h1>Find your place in the open source AI ecosystem.</h1>
<p>Discover the tools, compare alternatives and explore the building blocks of modern AI systems.</p></div>""", unsafe_allow_html=True)

if "compare_urls" not in st.session_state:
    st.session_state.compare_urls = []
if "metadata" not in st.session_state:
    st.session_state.metadata = {}

with st.sidebar:
    st.markdown("### Explore")
    page = st.radio("Navigation", ["Discover", "Compare", "Landscape", "Contribute"], label_visibility="collapsed")
    st.divider()
    if st.button("↻ Refresh README", use_container_width=True):
        load_catalog.clear()
        st.rerun()
    st.caption(f"Catalog: {provenance}")
    st.link_button("GitHub source ↗", REPO, use_container_width=True)
    st.caption("Listings are not endorsements or security assessments.")


def toggle_compare(url: str):
    selected = st.session_state.compare_urls
    if url in selected:
        selected.remove(url)
    elif len(selected) < 4:
        selected.append(url)


def compare_action(project: Project):
    selected = project.url in st.session_state.compare_urls
    st.button(
        "✓ Remove from comparison" if selected else "+ Compare",
        key=f"compare_{project.url}",
        disabled=not selected and len(st.session_state.compare_urls) >= 4,
        on_click=toggle_compare, args=(project.url,), use_container_width=True,
    )


def metadata_summary(data: dict | None):
    if not data:
        return "Metadata not loaded"
    if data.get("error"):
        return f"Metadata unavailable: {data['error']}"
    stars = data.get("stargazers_count")
    license_name = (data.get("license") or {}).get("spdx_id") or "Unknown"
    language = data.get("language") or "Unknown"
    return f"{language} · {license_name} · {stars:,} GitHub stars" if isinstance(stars, int) else f"{language} · {license_name}"


def show_project(project: Project):
    with st.container(border=True):
        st.markdown(f"#### {escape(project.name)}")
        st.caption(f"{project.area} / {project.category}")
        st.write(project.description)
        if project.status != "Listed":
            st.warning(f"README note: {project.status}")
        st.caption(metadata_summary(st.session_state.metadata.get(project.url)))
        left, right = st.columns(2)
        with left:
            st.link_button("Repository ↗", project.url, use_container_width=True)
        with right:
            compare_action(project)
        with st.expander("Project details"):
            st.write("**Category:**", project.category)
            st.write("**Area:**", project.area)
            st.write("**README status:**", project.status)
            meta = st.session_state.metadata.get(project.url)
            if meta and not meta.get("error"):
                st.write("**License:**", (meta.get("license") or {}).get("spdx_id") or "Unknown")
                st.write("**Primary language:**", meta.get("language") or "Unknown")
                st.write("**Open issues (GitHub count):**", meta.get("open_issues_count", "Unknown"))
                st.write("**Last push:**", meta.get("pushed_at", "Unknown"))
                st.write("**Archived on GitHub:**", bool(meta.get("archived")))
            if st.button("Fetch GitHub details", key=f"meta_{project.url}"):
                st.session_state.metadata[project.url] = project_metadata(project.url)
                st.rerun()


if page == "Discover":
    st.subheader("Discover projects")
    query = st.text_input("Search", placeholder="Search projects, tools, or use cases (e.g. RAG, agents, security)")
    shortcuts = st.columns(4)
    for column, (label, keyword) in zip(shortcuts, [("🤖 Agents", "agent"), ("⚡ Inference", "inference"), ("🛡️ Security", "security"), ("📊 Evaluation", "evaluation")]):
        with column:
            if st.button(label, use_container_width=True):
                st.session_state.quick_query = keyword
    quick_query = st.session_state.get("quick_query", "")
    if quick_query:
        st.caption(f"Quick filter active: {quick_query}")
        if st.button("Clear quick filter"):
            st.session_state.quick_query = ""
            st.rerun()
    st.markdown("#### Explore by workflow")
    area_columns = st.columns(3)
    for i, area in enumerate(areas):
        with area_columns[i % 3]:
            if st.button(f"{area}  ({sum(p.area == area for p in projects)})", key=f"area_{area}", use_container_width=True):
                st.session_state.area_selection = area
    area_selection = st.session_state.get("area_selection", "All areas")
    if area_selection not in ["All areas", *areas]:
        area_selection = "All areas"
    filter_col1, filter_col2, filter_col3 = st.columns(3)
    with filter_col1:
        chosen_area = st.selectbox("Area", ["All areas", *areas], index=["All areas", *areas].index(area_selection))
    with filter_col2:
        relevant_categories = sorted({p.category for p in projects if chosen_area == "All areas" or p.area == chosen_area})
        chosen_category = st.selectbox("Category", ["All categories", *relevant_categories])
    with filter_col3:
        chosen_status = st.selectbox("README maintenance note", ["All", "Listed", "Inactive", "Archived"])
    st.session_state.area_selection = chosen_area

    matches = search_projects(projects, " ".join(x for x in [query, quick_query] if x),
                              [] if chosen_area == "All areas" else [chosen_area],
                              [] if chosen_category == "All categories" else [chosen_category],
                              [] if chosen_status == "All" else [chosen_status])

    with st.expander("License and language filters (GitHub metadata)"):
        st.caption("GitHub API metadata is optional and rate-limited. When using metadata filters, only fetched projects are considered; missing metadata is not assumed to mean a missing license or language.")
        if st.button("Fetch GitHub metadata for visible projects (up to 40)"):
            selected = [p for p in matches if p.url not in st.session_state.metadata][:40]
            with st.spinner(f"Fetching metadata for {len(selected)} projects"):
                for p in selected:
                    result = project_metadata(p.url)
                    st.session_state.metadata[p.url] = result
                    if result.get("error") == "GitHub API rate limit reached":
                        break
            st.rerun()
        loaded = [m for m in st.session_state.metadata.values() if m and not m.get("error")]
        languages = sorted({m["language"] for m in loaded if m.get("language")})
        licenses = sorted({(m.get("license") or {}).get("spdx_id") for m in loaded if (m.get("license") or {}).get("spdx_id")})
        language = st.selectbox("Primary language", ["Any", *languages])
        license_id = st.selectbox("GitHub license SPDX ID", ["Any", *licenses])
    if language != "Any" or license_id != "Any":
        matches = [p for p in matches if p.url in st.session_state.metadata
                   and not st.session_state.metadata[p.url].get("error")
                   and (language == "Any" or st.session_state.metadata[p.url].get("language") == language)
                   and (license_id == "Any" or (st.session_state.metadata[p.url].get("license") or {}).get("spdx_id") == license_id)]
        st.info("Metadata filters are applied only to projects successfully enriched during this session.")

    m1, m2, m3 = st.columns(3)
    m1.metric("Matching projects", len(matches))
    m2.metric("Categories", len({p.category for p in matches}))
    m3.metric("Areas", len({p.area for p in matches}))
    st.caption("Catalog inclusion does not establish project security, suitability, licensing, or maintenance health.")
    a, b = st.columns([1, 1])
    with a:
        display = st.segmented_control("View", ["Cards", "Table"], default="Cards")
    with b:
        sort = st.selectbox("Sort", ["Category", "Name A–Z", "Area A–Z"])
    if sort == "Name A–Z":
        matches = sorted(matches, key=lambda p: p.name.casefold())
    elif sort == "Area A–Z":
        matches = sorted(matches, key=lambda p: (p.area.casefold(), p.category.casefold(), p.name.casefold()))
    if not matches:
        st.info("No projects match. Try broader filters or fetch GitHub metadata.")
    elif display == "Table":
        st.dataframe(pd.DataFrame([{"Project": p.name, "Area": p.area, "Category": p.category, "Description": p.description, "Repository": p.url} for p in matches]),
                     hide_index=True, use_container_width=True, column_config={"Repository": st.column_config.LinkColumn("Repository")})
    else:
        for i in range(0, len(matches), 2):
            cols = st.columns(2, gap="medium")
            for col, p in zip(cols, matches[i:i+2]):
                with col:
                    show_project(p)
    st.divider()
    export = [{"name":p.name, "url":p.url, "description":p.description, "area":p.area, "category":p.category, "status":p.status} for p in matches]
    c1, c2 = st.columns(2)
    c1.download_button("Download filtered CSV", pd.DataFrame(export).to_csv(index=False).encode(), "ai-catalog.csv", "text/csv")
    c2.download_button("Download filtered JSON", json.dumps(export, indent=2).encode(), "ai-catalog.json", "application/json")

elif page == "Compare":
    st.subheader("Compare open-source AI projects")
    st.caption("Select 2–4 projects. Comparisons describe their README listings and optionally verified GitHub repository metadata—not performance benchmarks.")
    candidates = st.multiselect("Projects to compare", options=list(by_url), default=[u for u in st.session_state.compare_urls if u in by_url],
                                format_func=lambda u: by_url[u].name, max_selections=4)
    st.session_state.compare_urls = candidates
    if len(candidates) < 2:
        st.info("Choose at least two projects here or use + Compare on Discover cards.")
    else:
        rows = []
        for url in candidates:
            p = by_url[url]
            meta = st.session_state.metadata.get(url)
            rows.append({"Project": p.name, "Area": p.area, "Category": p.category,
                         "Description": p.description, "README note": p.status,
                         "Language": (meta or {}).get("language") or "Not verified",
                         "License": ((meta or {}).get("license") or {}).get("spdx_id") or "Not verified",
                         "GitHub stars": (meta or {}).get("stargazers_count", "Not verified"),
                         "Repository": p.url})
        st.dataframe(pd.DataFrame(rows).set_index("Project").T, use_container_width=True)
        if st.button("Fetch GitHub details for comparison"):
            for url in candidates:
                st.session_state.metadata[url] = project_metadata(url)
            st.rerun()
        st.caption("GitHub stars are not measures of project quality or suitability. Verify licenses and project health independently.")

elif page == "Landscape":
    st.subheader("AI ecosystem landscape")
    st.caption("Interactive catalog topology: area → category → project. Links show catalog membership, NOT software dependencies.")
    area_counts = Counter(p.area for p in projects)
    st.bar_chart(pd.DataFrame([{"Area": a, "Projects": n} for a,n in area_counts.items()]).set_index("Area"), horizontal=True)
    selected_area = st.selectbox("Explore an area", areas)
    subset = [p for p in projects if p.area == selected_area]
    categories = sorted(set(p.category for p in subset))
    points = []
    for index, cat in enumerate(categories):
        category_projects = [p for p in subset if p.category == cat]
        points.append((0, index, cat, len(category_projects), "category"))
        for j, p in enumerate(category_projects):
            points.append((1+j % 4, index + (j // 4)*.12 - .15, p.name, 1, "project"))
    fig = go.Figure()
    for cat_index, cat in enumerate(categories):
        for x, y, name, _, kind in points:
            if kind == "project" and any(p.name == name and p.category == cat for p in subset):
                fig.add_trace(go.Scatter(x=[0,x], y=[cat_index,y], mode="lines", line=dict(color="#D8E2FA", width=1), hoverinfo="skip", showlegend=False))
    for kind, color in [("category", "#FF8B73"), ("project", "#5275F7")]:
        entries = [r for r in points if r[4] == kind]
        fig.add_trace(go.Scatter(x=[r[0] for r in entries],y=[r[1] for r in entries],text=[r[2] for r in entries],
                                 mode="markers", name=kind.title(), marker=dict(color=color,size=[18 if kind=="category" else 10 for _ in entries]),
                                 hovertemplate="%{text}<extra></extra>"))
    fig.update_layout(height=max(380, len(categories)*90), plot_bgcolor="white", paper_bgcolor="rgba(0,0,0,0)",
                      xaxis=dict(visible=False), yaxis=dict(visible=False), margin=dict(l=8,r=8,t=10,b=10))
    st.plotly_chart(fig, use_container_width=True)
    selected_category = st.selectbox("Explore category", categories)
    for p in [p for p in subset if p.category == selected_category]:
        st.markdown(f"- [{p.name}]({p.url}) — {p.description}")
    st.caption("A dependency graph would require independently sourced, maintained relationship data.")

elif page == "Contribute":
    st.subheader("Contribute to the open-source AI catalog")
    st.write("Suggest a missing project, improve a description or correct a category through a GitHub issue or pull request.")
    with st.form("suggestion"):
        name = st.text_input("Project name")
        url = st.text_input("Public repository URL")
        category = st.selectbox("Suggested category", sorted({p.category for p in projects}))
        description = st.text_area("Why should it be included?", max_chars=1500)
        submitted = st.form_submit_button("Prepare GitHub issue", type="primary")
    if submitted:
        if not name.strip() or not (url.startswith("https://github.com/") or url.startswith("http://github.com/")) or not description.strip():
            st.error("Enter a project name, GitHub repository URL, and description.")
        else:
            body = f"### Project\n{name.strip()}\n\n### Repository\n{url.strip()}\n\n### Suggested category\n{category}\n\n### Rationale\n{description.strip()}\n"
            link = REPO + "/issues/new?title=" + quote("Suggest project: " + name.strip()) + "&body=" + quote(body)
            st.link_button("Open prefilled GitHub issue ↗", link, type="primary")
            st.caption("Review your submission on GitHub before posting. No issue has been created yet.")
    st.divider()
    st.link_button("Open repository to submit a pull request ↗", REPO, use_container_width=True)
    st.info("Before suggesting a project, review existing listings and confirm the project's open-source license and maintenance state.")

st.divider()
st.caption("OpenTeams · Data from the public awesome-open-source-ai README · Built with Python and Streamlit")
