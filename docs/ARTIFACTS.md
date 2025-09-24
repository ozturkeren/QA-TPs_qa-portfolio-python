# Test Artifacts (Manual Screenshots)

This folder tracks manually saved screenshots taken from Allure reports for demo failures.

## Files (expected)
- `docs/screenshots/selenium_demo_fail.png` — Selenium failure screenshot
- `docs/screenshots/playwright_demo_fail.png` — Playwright failure screenshot

## How to update these screenshots
1) Run the demo-fail tests locally:
   ```bash
   pytest -m "demo_fail" --alluredir=allure-results-demo
   ```
   
2) Generate a static Allure report:
   ```bash
   allure generate allure-results-demo -o allure-report-demo --clean
   allure open allure-report-demo
   ```

3) Save screenshots to:

   - docs/screenshots/selenium_demo_fail.png
   - docs/screenshots/playwright_demo_fail.png

