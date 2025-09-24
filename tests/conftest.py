import os
import sys
import pytest
import allure
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent  # tests/.. => project root
SRC_DIR = PROJECT_ROOT / "src"

for p in (str(PROJECT_ROOT), str(SRC_DIR)):
    if p not in sys.path:
        sys.path.insert(0, p)

@pytest.fixture(scope="session")
def base_url():
    return "https://www.saucedemo.com/"

@pytest.fixture(autouse=True)
def add_allure_environment():
    allure.dynamic.label("base_url", os.getenv("BASE_URL", "https://www.saucedemo.com/"))

# Selenium page fixture (if it is put above, it gives "No module named 'src'" error again)
from src.pages.swag_login_page import SwagLoginPage

@pytest.fixture
def selenium_page():
    p = SwagLoginPage(headless=True)
    try:
        yield p
    finally:
        p.close()

# Playwright page fixture
@pytest.fixture
def pw_page(playwright):
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()
    try:
        yield page
    finally:
        context.close()
        browser.close()

# Attach screenshots on failure
@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call" and rep.failed:
        # Selenium
        sp = item.funcargs.get("selenium_page")
        if sp:
            try:
                png = sp.driver.get_screenshot_as_png()
                allure.attach(png, name="selenium-failure", attachment_type=allure.attachment_type.PNG)
            except Exception:
                pass
        # Playwright
        pp = item.funcargs.get("pw_page")
        if pp:
            try:
                png = pp.screenshot()
                allure.attach(png, name="playwright-failure", attachment_type=allure.attachment_type.PNG)
            except Exception:
                pass
