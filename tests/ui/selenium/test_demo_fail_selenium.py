import os
import pytest
import allure

@pytest.mark.ui
@pytest.mark.demo_fail
@pytest.mark.skipif(os.getenv("CI") == "true", reason="demo fail only runs locally to verify screenshots")
def test_demo_fail_selenium_title(selenium_page):
    with allure.step("Open login page"):
        selenium_page.open()
    with allure.step("Intentionally assert a wrong title to trigger screenshot"):
        # Real title contains "Swag Labs" — I assert something impossible to force a failure
        assert "Totally Not The Title" in selenium_page.landing_title()
