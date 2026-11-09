"""Open Source AI Compass — plan your AI stack with open source.

Run: python -m streamlit run app.py
"""
from __future__ import annotations

import json
from html import escape
from urllib.parse import quote

import pandas as pd
import streamlit as st

from catalog import REPO, Project, parse_projects, read_readme, search_projects
from builder_ui import render_builder

st.set_page_config(page_title="Open Source AI Comppass", page_icon="🧭", layout="wide")

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
.build-flow{display:flex;align-items:stretch;gap:6px;flex-wrap:wrap;margin:12px 0 8px}.build-tile{flex:1 1 135px;min-width:128px;min-height:90px;padding:14px;border-radius:12px;background:white;border:1px solid #CDD9F3;display:flex;flex-direction:column;gap:12px}.build-step{font-size:.75rem;color:#5C6A88;font-weight:700}.build-tile strong{font-size:.9rem;color:#082B80;overflow-wrap:anywhere}.build-arrow{align-self:center;color:#5275F7;font-size:1.3rem;font-weight:700}
@media(max-width:700px){.hero{padding:22px}.hero h1{font-size:1.7rem}.block-container{padding-left:1rem;padding-right:1rem}}
</style>""", unsafe_allow_html=True)


@st.cache_data(ttl=3600, show_spinner=False)
def load_catalog():
    markdown, provenance = read_readme(live=True)
    return parse_projects(markdown), provenance


projects, provenance = load_catalog()
by_url = {p.url: p for p in projects}
areas = list(dict.fromkeys(p.area for p in projects))

st.markdown("""<div class='hero'><div class='eyebrow'>Open Source AI Compass</div>
<h1>Build with open source</h1>
<p>Design a blueprint of your end-to-end AI stack.</p></div>""", unsafe_allow_html=True)

with st.sidebar:
    page = st.radio("Navigation", ["Build", "Discover"], label_visibility="collapsed")
    st.divider()
    if st.button("↻ Refresh README", use_container_width=True):
        load_catalog.clear()
        st.rerun()
    st.caption(f"Catalog: {provenance}")
    st.link_button("GitHub source ↗", REPO, use_container_width=True)
    st.caption("Listings are not endorsements or security assessments.")


def show_project(project: Project):
    with st.container(border=True):
        st.markdown(f"#### {escape(project.name)}")
        st.caption(f"{project.area} / {project.category}")
        st.write(project.description)
        if project.status != "Listed":
            st.warning(f"README note: {project.status}")
        st.link_button("Repository ↗", project.url, use_container_width=True)


if page == "Build":
    render_builder(projects)

elif page == "Discover":
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
        st.info("No projects match. Try broader filters.")
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
