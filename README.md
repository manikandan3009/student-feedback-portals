
# Student Feedback Portal (Flask) — CI/CD with GitHub Actions + Docker + Render

A minimal Flask app that collects anonymous course feedback and shows an admin view.
CI/CD via GitHub Actions:
- **install** → **lint/test** → **build** → **deploy (optional to Render)**.

## Quick Start (Local)

Open http://localhost:8000

## Run tests & lint locally
```bash
pip install -r requirements.txt
pip install pytest flake8
flake8 .
pytest -q
```

## Docker (Local)
```bash
docker build -t student-feedback-portal:dev .
docker run -p 8000:8000 student-feedback-portal:dev
```

## CI/CD
GitHub Actions runs on every push/PR to `main`:
1. **Lint & Test** (`flake8`, `pytest`).
2. **Build** Docker image.
3. **Deploy** (optional): triggers a Render deploy hook (if configured).

### Set up Deploy (Render)

1. Create a new **Web Service** in [Render](https://render.com/), connect it to **your fork** of this repo.
   - Runtime: Docker
   - Build/Start are taken from `Dockerfile` and default CMD.
   - Free tier is OK for classroom demo; app will spin down when idle.

2. In Render, go to: **Settings → Deploy Hooks → Create Deploy Hook**. Copy the URL.

3. In your **GitHub repo → Settings → Secrets and variables → Actions → New repository secret**
   - Name: `RENDER_DEPLOY_HOOK_URL`
   - Value: *paste the Render deploy hook URL*

4. Push a commit to `main`. The `deploy` job will `POST` to that hook and Render will rebuild & redeploy.

> If `RENDER_DEPLOY_HOOK_URL` is not set, the workflow **skips deploy** but still runs install/test/build.

## Screenshots to include in your report
- GitHub Actions run showing the three jobs: **lint_test**, **build**, **deploy**.
- Render dashboard showing a successful deployment (event list).
- The running app URL (landing page, Admin page).

## Admin page
Visit `/admin` to see collected feedback (in-memory, reset on restart).

## Project Structure
```
.
├─ app.py
├─ templates/
│  ├─ index.html
│  ├─ thanks.html
│  └─ admin.html
├─ static/
│  └─ styles.css
├─ tests/
│  ├─ conftest.py
│  └─ test_app.py
├─ requirements.txt
├─ Dockerfile
├─ .flake8
├─ .gitignore
├─ .github/workflows/ci-cd.yml
└─ report/Report_Template.md  (fill and export to PDF)
```

## License
MIT (for coursework use)
