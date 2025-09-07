
# Tool Demo & Report — Student Feedback Portal (CI/CD)

**Author:** _Your Name_  
**Date:** _YYYY-MM-DD_  
**Repo URL:** _https://github.com/yourname/student-feedback-portal_  
**Deployed URL (if any):** _https://..._

---

## 1) Problem Understanding

- Current state: manual testing and manual deploy to a dev server.  
- Goals of Agile DevOps adoption:
  - Run tests/linters automatically on each push.
  - Trigger build on changes to `main`.
  - Automatically deploy to a simulated environment on passing tests.
- Scope for this demo:
  - Minimal Flask app with anonymous feedback (in-memory store).
  - CI/CD via GitHub Actions.
  - Deploy via Render (Deploy Hook).

## 2) Repository Structure

```
<root>
├─ app.py
├─ templates/
├─ static/
├─ tests/
├─ Dockerfile
├─ requirements.txt
├─ .github/workflows/ci-cd.yml
└─ report/
```

Rationale:
- `tests/` contains automated tests for core routes.
- Dockerfile ensures consistent build.
- GitHub Actions workflow defines install → test → build → deploy.

## 3) Workflow `.yml` with Explanation

> File: `.github/workflows/ci-cd.yml`

```yaml
# (Paste the full YAML here)
```

**Explanation (stage-by-stage):**
- **Install → Lint → Test:** Checks out code, sets up Python, installs deps, runs flake8 + pytest.
- **Build:** Builds Docker image and uploads as artifact (proof of successful build).
- **Deploy:** POSTs to Render Deploy Hook URL (stored as a GitHub Secret). Render rebuilds & redeploys from the repo.

## 4) Screenshots of Pipeline Runs

Include the following with captions:
1. **GitHub Actions** — successful run showing green checks for all three jobs.
2. **Job details** — console logs for `Lint`, `Test`, and `Build` steps.
3. **Render dashboard** — deploy event and service status `Live`.
4. **App UI** — Home page and Admin page screenshots.

_Place images here:_  
![CI Pipeline](./images/ci-pipeline.png)  
![Build Logs](./images/build-logs.png)  
![Render Deploy](./images/render-deploy.png)  
![App Running](./images/app-running.png)

## 5) How CI/CD Reduced Manual Effort

- Eliminated manual testing by running automated tests on each push.
- Prevented broken main branch with immediate feedback on failures.
- Automated deployments minimized human error and reduced cycle time.
- Reproducible builds with Docker improved consistency across environments.

## 6) Challenges & Resolutions

- **Secret management:** Used GitHub Actions Secrets to store the Render deploy hook securely.
- **Flaky tests initially:** Added minimal deterministic tests based on HTTP status codes.
- **Docker build time:** Cached Python dependencies locally (not necessary in GH Actions for small project).

## 7) Reflections on Agile DevOps Practices

- Iterative development with small commits and PRs improves traceability.
- Automated quality gates (lint/test) keep `main` stable.
- The pipeline aligns with Continuous Integration (test early/often) and Continuous Deployment (automated release upon success).
- Observability via Action logs and Render events supports fast feedback loops.

## 8) Conclusion

The configured pipeline meets the assignment objectives: automatic testing, building, and deployment to a simulated environment with documentation and evidence of runs.

---

> **Export to PDF:** Use VS Code (`Markdown: Print to PDF`), a Markdown-to-PDF extension, or `pandoc`:
> ```bash
> pandoc report/Report_Template.md -o report/StudentFeedbackPortal_Report.pdf
> ```
