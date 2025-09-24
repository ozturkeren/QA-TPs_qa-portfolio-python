# QA Portfolio (Python) — Selenium + Playwright + API + SQL

[![CI](https://github.com/ozturkeren/QA-TPs_qa-portfolio-python/actions/workflows/ci.yml/badge.svg)](https://github.com/ozturkeren/QA-TPs_qa-portfolio-python/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
![Python 3.12](https://img.shields.io/badge/python-3.12-blue)

This project is part of my **QA Test Engineering portfolio**.  

---

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

---

## Screenshots (manual demo failures)

Selenium (intentional fail)  
![Selenium demo failure](docs/screenshots/selenium_demo_fail.png)

Playwright (intentional fail)  
![Playwright demo failure](docs/screenshots/playwright_demo_fail.png)