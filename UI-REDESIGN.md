# UI redesign

This update keeps Streamlit and the public Markdown README as the catalog source.

## Included

- Search-first OpenTeams hero and workflow navigation
- Responsive 2-column project cards with README status notes
- Single-page app: the Builder, no sidebar navigation
- Prefilled GitHub issue contribution form (user submits on GitHub)
- CSV/JSON exports and updated responsive styling

## Important caveats

The catalog's maintenance notes are not a security audit or project health
score. The app makes no GitHub API calls; it only fetches the public README.

No secrets, GitHub write access, or database are required for hosting.

Run: `python -m pip install -r requirements.txt && python -m streamlit run app.py`.
