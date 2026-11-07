"""Streamlit UI for catalog-grounded, end-to-end AI architecture planning."""
from __future__ import annotations

from html import escape

import streamlit as st

from catalog import Project
from system_builder import RECIPES, architecture, blueprint_json, blueprint_markdown, candidates, defaults


def render_builder(projects: list[Project]) -> None:
    st.markdown("### Build an open-source AI system")
    st.caption("Choose a goal → select catalog tools → inspect architecture → export an implementation checklist. Recommendations are examples, not tested integrations.")

    with st.container(border=True):
        st.markdown("#### 1 · Choose what you want to build")
        template = st.selectbox("System blueprint", list(RECIPES), help="These templates use only repositories actually found in the loaded catalog.")
        recipe = RECIPES[template]
        st.write(recipe.pitch)
        c1, c2 = st.columns(2)
        with c1:
            goal = st.text_input("Target outcome", placeholder="e.g. Answer support questions from internal docs", key="builder_goal")
            deployment = st.selectbox("Where will it run?", ["Not decided", "On my laptop", "Private cloud / on-prem", "Public cloud"], key="builder_deployment")
        with c2:
            sensitivity = st.selectbox("Data sensitivity", ["Not decided", "Public", "Internal", "Confidential / regulated"], key="builder_sensitivity")
            constraints = st.text_input("Constraints", placeholder="e.g. CPU-only, Python, low latency, offline", key="builder_constraints")

    st.markdown("#### 2 · Assemble your stack")
    st.caption("Each stage shows options mapped to the catalog. Select a different project or leave a stage unassigned; an unassigned stage is not implemented.")
    preset = defaults(recipe, projects)
    choices: dict[str, str | None] = {}
    stage_cards = st.columns(2, gap="medium")
    for i, stage in enumerate(recipe.stages):
        available = candidates(stage, projects)
        options = [None, *(p.url for p in available)]
        with stage_cards[i % 2]:
            with st.container(border=True):
                st.markdown(f"**{i+1:02d} · {stage.title}**")
                st.caption(stage.description)
                st.write(stage.why)
                # Template in the key ensures changing recipes resets its recommendations.
                value = st.selectbox(
                    "Catalog project", options,
                    index=options.index(preset[stage.id]) if preset[stage.id] in options else 0,
                    format_func=lambda url: (next((p.name for p in available if p.url == url), url) if url else "— Not selected —"),
                    key=f"builder_{template}_{stage.id}",
                    help="Suggested projects are filtered against the current parsed README."
                )
                choices[stage.id] = value
                matched = next((p for p in available if p.url == value), None)
                if matched:
                    st.link_button("View source repository ↗", matched.url, use_container_width=True)
                    with st.expander("What does this project do?"):
                        st.write(matched.description)
                        st.caption(f"Catalog: {matched.area} / {matched.category} · {matched.status}")
                elif not available:
                    st.warning("No listed catalog candidates for this stage. Document the gap before implementation.")
                else:
                    st.caption("Leave unselected if this stage needs further research.")

    ctx = {"goal": goal, "deployment": deployment, "data_sensitivity": sensitivity, "constraints": constraints}
    plan = architecture(template, projects, choices, ctx)
    count = sum(bool(s["tool"]) for s in plan["stages"])
    st.markdown("#### 3 · Review the end-to-end architecture")
    st.progress(count / len(plan["stages"]), text=f"{count} of {len(plan['stages'])} stages have a proposed catalog tool — not a readiness score")
    # Safe HTML: all values inserted as escaped plain text; arrows indicate a conceptual sequence.
    tiles = []
    for s in plan["stages"]:
        label = escape(s["stage"])
        tool = escape(s["tool"] or "Needs selection")
        tiles.append(f'<div class="build-tile"><span class="build-step">{label}</span><strong>{tool}</strong></div>')
    st.markdown('<div class="build-flow">' + '<span class="build-arrow">→</span>'.join(tiles) + '</div>', unsafe_allow_html=True)
    st.caption("Conceptual workflow, not a proven runtime dependency graph. Implementation may require additional components and integration work.")

    left, right = st.columns(2, gap="large")
    with left:
        st.markdown("#### 4 · Resolve architecture gaps")
        for gap in plan["gaps"]:
            st.checkbox(gap, key=f"gap_{template}_{gap}", help="A planning checklist, not a verified deployment status.")
    with right:
        st.markdown("#### 5 · Define acceptance tests")
        for test in plan["verification"]:
            st.checkbox(test, key=f"test_{template}_{test}", help="Check only when you have run the corresponding test.")
    if sensitivity == "Confidential / regulated":
        st.warning("Sensitive data selected: define a privacy/security review, retention policy and compliance requirements before putting real data into the system.")
    st.info("A complete production system needs model selection, credentials, data governance, integration tests, monitoring, and operational ownership. Not every component is present in the catalog.")

    st.markdown("#### 6 · Export your implementation plan")
    st.write("Share the blueprint in a GitHub issue, technical design review, or project kickoff. The output includes selected repositories, unresolved dependencies and tests.")
    c1, c2 = st.columns(2)
    c1.download_button("Download Markdown blueprint", blueprint_markdown(plan), file_name="open-source-ai-blueprint.md", mime="text/markdown", use_container_width=True, type="primary")
    c2.download_button("Download JSON blueprint", blueprint_json(plan), file_name="open-source-ai-blueprint.json", mime="application/json", use_container_width=True)
    with st.expander("Preview the full blueprint"):
        st.markdown(blueprint_markdown(plan))
