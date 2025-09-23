import allure
import pytest
from src.pages.swag_login_page import SwagLoginPage

@pytest.mark.ui
def test_valid_login_opens_inventory():
    page = SwagLoginPage(headless=True)
    try:
        with allure.step("Open login page"):
            page.open()
        with allure.step("Login with standard_user"):
            page.login("standard_user", "secret_sauce")
        with allure.step("Verify we navigated"):
            assert "Swag Labs" in page.landing_title()
    finally:
        page.close()
