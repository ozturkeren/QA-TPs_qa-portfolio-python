import pytest
import allure

@pytest.mark.ui
def test_add_item_to_cart(playwright):
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()
    try:
        with allure.step("Open login page"):
            page.goto("https://www.saucedemo.com/")
        with allure.step("Login"):
            page.fill("#user-name", "standard_user")
            page.fill("#password", "secret_sauce")
            page.click("#login-button")
        with allure.step("Add first item to cart"):
            page.click("button:has-text(\"Add to cart\")")
        with allure.step("Check cart badge"):
            assert page.locator(".shopping_cart_badge").inner_text() == "1"
    finally:
        context.close()
        browser.close()
