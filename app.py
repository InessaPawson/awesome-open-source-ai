"""Interactive directory for OpenTeams' Awesome Open Source AI catalog.
Run: streamlit run app.py
"""
import csv
import io
from collections import Counter
import pandas as pd
import streamlit as st
from catalog import REPO, read_readme, parse_projects, search_projects

st.set_page_config(page_title='Open Source AI Explorer · OpenTeams', page_icon='✳️', layout='wide', initial_sidebar_state='expanded')
st.markdown('''<style>
:root {--ot-navy:#082B80;--ot-blue:#5275F7;--ot-coral:#FF8B73;--ot-orange:#FFB34F;--ot-ink:#172549;--ot-muted:#5C6A88;--ot-background:#F7F9FE;}
.stApp {background:var(--ot-background);color:var(--ot-ink)}
.block-container {padding-top:2rem;max-width:1450px}
h1,h2,h3 {letter-spacing:-.035em;color:var(--ot-navy)}
[data-testid="stSidebar"] {background:#EFF3FF;border-right:1px solid #DCE5FC}
[data-testid="stSidebar"] h3 {color:var(--ot-navy)}
.hero {position:relative;overflow:hidden;padding:35px 38px;border:1px solid #244BB4;border-radius:20px;background:linear-gradient(115deg,#07266E 0%,#123C9C 53%,#5275F7 100%);color:white;margin-bottom:24px;box-shadow:0 10px 28px #102D831A}
.hero:after {content:'';position:absolute;right:-45px;top:-95px;width:295px;height:295px;border:45px solid #FFFFFF19;border-radius:50%;pointer-events:none}
.hero:before {content:'';position:absolute;right:210px;bottom:-75px;width:145px;height:145px;border:26px solid #FFB34F55;border-radius:50%;pointer-events:none}
.hero h1 {color:white;font-size:2.5rem;margin:4px 0 12px;max-width:800px;position:relative;z-index:1}
.hero p {color:#E4EBFF;font-size:1.02rem;margin:0;position:relative;z-index:1}
.hero .eyebrow {color:#FFCB8E!important;font-size:.8rem!important;letter-spacing:.16em;text-transform:uppercase;font-weight:700;margin-bottom:10px}
.hero .spark {display:inline-block;width:9px;height:9px;background:var(--ot-coral);border-radius:50%;margin-right:8px}
[data-testid="stMetric"] {background:white;border:1px solid #DFE6F6;border-radius:14px;padding:18px;box-shadow:0 3px 12px #102D8309}
[data-testid="stMetricLabel"] {color:var(--ot-muted)}
[data-testid="stMetricValue"] {color:var(--ot-navy)}
[data-testid="stVerticalBlockBorderWrapper"] > div {border-color:#DFE6F6!important;border-radius:15px!important;background:#FFFFFF}
.stButton button[kind="primary"], .stDownloadButton button[kind="primary"] {background:var(--ot-blue);border-color:var(--ot-blue);color:white}
.stButton button:hover, .stDownloadButton button:hover, .stLinkButton a:hover {border-color:var(--ot-blue);color:var(--ot-navy)}
.stLinkButton a {border-color:#B8C9F6;color:var(--ot-navy);background:#F4F7FF;font-weight:650}
[data-baseweb="tab-highlight"] {background:var(--ot-blue)!important}
[data-testid="stCaptionContainer"] {color:var(--ot-muted)}
a {color:#315BCB}
@media(max-width:700px){.hero{padding:24px}.hero h1{font-size:1.85rem}}
</style>''', unsafe_allow_html=True)

@st.cache_data(ttl=3600, show_spinner=False)
def get_catalog():
    md, provenance = read_readme(live=True)
    return parse_projects(md), provenance

if st.sidebar.button('↻ Refresh from GitHub', use_container_width=True):
    get_catalog.clear()

projects, provenance = get_catalog()
areas = list(dict.fromkeys(p.area for p in projects))
categories = list(dict.fromkeys(p.category for p in projects))

st.markdown('''<div class="hero"><p class="eyebrow"><span class="spark"></span>OpenTeams / Field guide</p><h1>Explore the open source AI ecosystem.</h1><p>Discover the libraries, frameworks, infrastructure and tools behind modern AI systems.</p></div>''', unsafe_allow_html=True)

with st.sidebar:
    st.markdown('### Explore')
    query = st.text_input('Search projects', placeholder='e.g. agents, inference, testing', key='query')
    selected_areas = st.multiselect('Areas', areas, placeholder='All areas')
    choices = sorted({p.category for p in projects if not selected_areas or p.area in selected_areas})
    selected_categories = st.multiselect('Categories', choices, placeholder='All categories')
    selected_statuses = st.multiselect('Maintenance note', ['Listed','Inactive','Archived'], placeholder='All statuses', help='Based on explicit notes in the README; Listed is not a health or security assessment.')
    st.divider()
    st.caption(f'Source: {provenance}')
    st.link_button('View source repository ↗', REPO, use_container_width=True)
    st.caption('The upstream README remains the source of truth. No GitHub API key is required.')

filtered = search_projects(projects, query, selected_areas, selected_categories, selected_statuses)
counts = Counter(p.category for p in filtered)
c1,c2,c3,c4 = st.columns(4)
c1.metric('Projects', len(filtered)); c2.metric('Categories', len(counts)); c3.metric('Areas', len(set(p.area for p in filtered)))
c4.metric('With maintenance notes', sum(p.status!='Listed' for p in filtered))
st.caption('Inclusion is not an endorsement or security audit. Verify current licensing, maintenance, releases and supply-chain posture before adoption.')

tab1, tab2, tab3 = st.tabs(['▦  Directory', '◫  Ecosystem overview', '⇩  Export'])
with tab1:
    toolbar_left, toolbar_right = st.columns([2,1])
    with toolbar_left:
        view = st.segmented_control('Display', ['Cards', 'Table'], default='Cards', label_visibility='collapsed')
    with toolbar_right:
        sort_by = st.selectbox('Sort', ['By category', 'Project name A–Z', 'Area A–Z'], label_visibility='collapsed')
    if sort_by == 'Project name A–Z':
        filtered = sorted(filtered, key=lambda p:p.name.casefold())
    elif sort_by == 'Area A–Z':
        filtered = sorted(filtered, key=lambda p:(p.area.casefold(),p.category.casefold(),p.name.casefold()))
    if not filtered:
        st.info('No projects match those filters. Try another search or clear a filter.')
    elif view == 'Table':
        frame = pd.DataFrame([dict(Project=p.name, Area=p.area, Category=p.category, Description=p.description, Status=p.status, Repository=p.url) for p in filtered])
        st.dataframe(frame, use_container_width=True, hide_index=True, column_config={'Repository':st.column_config.LinkColumn('Repository',display_text='Open ↗')})
    else:
        # Streamlit native cards with safe text rendering and working repo links.
        for i in range(0,len(filtered),3):
            cols=st.columns(3, gap='medium')
            for col,p in zip(cols,filtered[i:i+3]):
                with col:
                    with st.container(border=True):
                        st.markdown(f'#### {p.name}')
                        st.caption(f'{p.area} · {p.category}')
                        st.write(p.description)
                        if p.status != 'Listed':
                            st.warning(p.status, icon='⚠️')
                        st.link_button('View repository ↗',p.url,use_container_width=True)
with tab2:
    if filtered:
        st.subheader('Projects by area')
        df=pd.DataFrame([{'Area':p.area,'Category':p.category} for p in filtered])
        st.bar_chart(df['Area'].value_counts(), horizontal=True, x_label='Projects', y_label='')
        st.subheader('Category breakdown')
        breakdown=pd.DataFrame([{'Category':cat,'Projects':count} for cat,count in counts.most_common()])
        st.dataframe(breakdown,use_container_width=True,hide_index=True)
    else:
        st.info('No data to chart. Adjust your filters.')
with tab3:
    st.subheader('Export your selection')
    st.write('Download the currently filtered projects, including their descriptions and source repository links.')
    rows=[dict(name=p.name,url=p.url,description=p.description,area=p.area,category=p.category,status=p.status) for p in filtered]
    frame=pd.DataFrame(rows, columns=['name','url','description','area','category','status'])
    st.download_button('Download CSV',frame.to_csv(index=False).encode('utf-8'),file_name='awesome-open-source-ai.csv',mime='text/csv',disabled=not filtered)
    st.download_button('Download JSON',frame.to_json(orient='records',indent=2,force_ascii=False).encode('utf-8'),file_name='awesome-open-source-ai.json',mime='application/json',disabled=not filtered)

st.divider()
st.caption('Data: OpenTeams awesome-open-source-ai · CC0-1.0 · Built with Python and Streamlit')
