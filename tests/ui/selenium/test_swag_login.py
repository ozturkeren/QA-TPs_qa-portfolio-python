import allure
import pytest

@pytest.mark.ui
def test_valid_login_opens_inventory(selenium_page):
    with allure.step("Open login page"):
        selenium_page.open()
    with allure.step("Login with standard_user"):
        selenium_page.login("standard_user", "secret_sauce")
    with allure.step("Verify we navigated"):
        assert "Swag Labs" in selenium_page.landing_title()
