import os
import pytest
import allure

@pytest.mark.ui
@pytest.mark.demo_fail
@pytest.mark.skipif(os.getenv("CI") == "true", reason="demo fail only runs locally to verify screenshots")
def test_demo_fail_playwright_cart(pw_page):
    with allure.step("Open login page"):
        pw_page.goto("https://www.saucedemo.com/")
    with allure.step("Login"):
        pw_page.fill("#user-name", "standard_user")
        pw_page.fill("#password", "secret_sauce")
        pw_page.click("#login-button")
    with allure.step("Add first item to cart"):
        pw_page.get_by_role("button", name="Add to cart").first.click()
    with allure.step("Intentionally assert wrong cart count"):
        # Actual badge will be "1" — assert "2" to force a failure and trigger a screenshot
        assert pw_page.locator(".shopping_cart_badge").inner_text() == "2"
