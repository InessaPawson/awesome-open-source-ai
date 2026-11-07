# Deployment to Streamlit Community Cloud

This folder contains deployable files for https://github.com/InessaPawson/awesome-open-source-ai.

Copy its contents to the root of the GitHub repository without replacing the existing README.md or models/ directory.

```bash
cd ~/Downloads
git clone https://github.com/InessaPawson/awesome-open-source-ai.git
cd awesome-open-source-ai
unzip -o ~/Downloads/openteams-deploy-ready.zip
git add app.py catalog.py requirements.txt README.snapshot.md .streamlit/config.toml .gitignore DEPLOY.md
git commit -m "Add OpenTeams-themed Streamlit catalog"
git push origin main
```

Then visit https://share.streamlit.io, create an app using branch `main` and entrypoint `app.py`. Select your preferred app subdomain.

The app reads project data from the fork README on each Streamlit data-cache refresh (hourly) and falls back to README.snapshot.md if GitHub is unreachable.
