"""Open Source AI Compass — design a blueprint of your AI stack with open source.

Run: python -m streamlit run app.py
"""
from __future__ import annotations

import streamlit as st

from catalog import REPO, parse_projects, read_readme
from builder_ui import render_builder

st.set_page_config(page_title="Open Source AI Compass", page_icon="✳️", layout="wide", initial_sidebar_state="collapsed")

st.markdown("""<style>
:root {--navy:#082B80;--blue:#5275F7;--coral:#FF8B73;--orange:#FFB34F;--ink:#172549;--muted:#5C6A88;}
.stApp {background:#F7F9FE;color:var(--ink)}
.block-container {max-width:1450px;padding-top:1.5rem}
h1,h2,h3 {color:var(--navy);letter-spacing:-.025em}
[data-testid="stSidebar"],[data-testid="collapsedControl"] {display:none}
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
.build-flow{display:flex;align-items:stretch;gap:6px;flex-wrap:wrap;margin:12px 0 8px}.build-tile{flex:1 1 135px;min-width:128px;min-height:90px;padding:14px;border-radius:12px;background:white;border:1px solid #CDD9F3;display:flex;flex-direction:column;gap:12px}.build-step{font-size:.75rem;color:#5C6A88;font-weight:700}.build-tile strong{font-size:.9rem;color:#082B80;overflow-wrap:anywhere}.build-arrow{align-self:center;color:#5275F7;font-size:1.3rem;font-weight:700}
@media(max-width:700px){.hero{padding:22px}.hero h1{font-size:1.7rem}.block-container{padding-left:1rem;padding-right:1rem}}
</style>""", unsafe_allow_html=True)


@st.cache_data(ttl=3600, show_spinner=False)
def load_catalog():
    markdown, provenance = read_readme(live=True)
    return parse_projects(markdown), provenance


projects, provenance = load_catalog()

st.markdown("""<div class='hero'><div class='eyebrow'>Open Source AI Compass</div>
<h1>Build with open source</h1>
<p>Design a blueprint for your AI stack with open source tools.</p></div>""", unsafe_allow_html=True)

render_builder(projects)

st.divider()
f1, f2, f3 = st.columns([3, 1, 1])
f1.caption(f"Catalog: {provenance} · Listings are not endorsements or security assessments.")
if f2.button("↻ Refresh catalog", use_container_width=True):
    load_catalog.clear()
    st.rerun()
f3.link_button("Catalog on GitHub ↗", REPO, use_container_width=True)
st.caption("Data from the community-curated Awesome Open Source AI list · Built with Python and Streamlit")
