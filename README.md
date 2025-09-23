# QA Portfolio (Python) — Selenium + Playwright + API + SQL

**Stack:** Python, Pytest, Selenium 4, Playwright, Requests, Allure, GitHub Actions CI, Docker.

- UI (Selenium + Playwright) on a demo shop  
- API testing against a public demo API  
- SQL checks (SQLite)  
- Headless CI + Allure artifacts

## Quick start
```bash
python -m venv .venv
# Windows PowerShell:
. .\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python -m playwright install
pytest -m "ui or api" --alluredir=allure-results
allure serve allure-results
```
