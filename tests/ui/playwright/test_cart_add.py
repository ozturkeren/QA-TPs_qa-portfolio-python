import pytest
import allure

@pytest.mark.ui
def test_add_item_to_cart(pw_page):
    with allure.step("Open login page"):
        pw_page.goto("https://www.saucedemo.com/")
    with allure.step("Login"):
        pw_page.fill("#user-name", "standard_user")
        pw_page.fill("#password", "secret_sauce")
        pw_page.click("#login-button")
    with allure.step("Add first item to cart"):
        pw_page.get_by_role("button", name="Add to cart").first.click()
    with allure.step("Check cart badge"):
        assert pw_page.locator(".shopping_cart_badge").inner_text() == "1"
