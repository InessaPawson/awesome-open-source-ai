# UI redesign

This update keeps Streamlit and the public Markdown README as the catalog source.

## Included

- Search-first OpenTeams hero and workflow navigation
- Responsive 2-column project cards, detail expanders, README status notes
- Four-page app navigation: Discover, Compare, Landscape, Contribute
- Comparison of two to four projects
- Optional GitHub metadata (language, license, stars, last push, archive status)
- Language and license filters scoped to the metadata retrieved in the current session
- Interactive Plotly area/category/project topology (not a dependency graph)
- Prefilled GitHub issue contribution form (user submits on GitHub)
- CSV/JSON exports and updated responsive styling

## Important caveats

The GitHub REST API may limit unauthenticated queries to 60 per hour. Metadata
is optional, fetched on demand (bulk at most 40 requests at a time), and the
app clearly distinguishes unverified fields. The catalog's maintenance notes
are not a security audit or project health score. The graph describes catalog
membership only; it does not claim actual package dependencies.

No secrets, GitHub write access, or database are required for hosting.

Run: `python -m pip install -r requirements.txt && python -m streamlit run app.py`.
