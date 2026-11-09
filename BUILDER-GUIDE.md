# OpenTeams AI System Builder

This redesign changes the default page from project browsing to a **guided architecture planner**. The catalog remains the source of truth for recommended repository links.

## User journey

1. Choose a blueprint: Document Q&A (RAG), Tool-using AI agent, Local private assistant, or Fine-tune and serve a model.
2. State deployment environment, data sensitivity, and target outcome.
3. Pick a listed open-source project for each relevant system stage, or leave it unselected.
4. Review the conceptual flow, unresolved implementation gaps, and test checklist.
5. Export the architecture as Markdown or JSON for a design review or GitHub issue.

The **Discover** and **Contribute** pages remain available.

## Source of recommendations

`system_builder.py` defines curated, version-controlled starter recipes. Each recipe references GitHub repository URLs from the awesome list. `candidates()` returns a recommendation **only if the URL currently exists in the parsed catalog**. No license, capability, model compatibility, security or deployment fitness is automatically certified. This is a planning assistant, not an autonomous system builder.

To add a template or recommendation, edit `RECIPES` in `system_builder.py`, then run `python -m unittest discover -s tests -v`. Confirm that candidates exist in the live README and the guidance is technically appropriate. Include explicit operational gaps and acceptance tests.

## Deployment

The app needs no additional dependencies beyond the existing `requirements.txt`. On Streamlit Community Cloud, keep main file path `app.py` on the `main` branch. The app will update upon pushing your code to GitHub.

## Security and limitations

- Templates never execute, deploy or install selected projects.
- Downloaded Markdown/JSON records proposed choices only; it is not a reproducible lockfile.
- Model weights, embedding stores, authentication, hosting, secrets, compliance, observability, and integration testing often need additional decisions.
- Check licenses, maintenance, compatibility, and vulnerability state before adopting anything.
- The app fetches the live README from a public GitHub endpoint; avoid pasting sensitive data into the planning fields of a public deployment.
