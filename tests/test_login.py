import pytest
from pages.login_page import LoginPage


def test_login_with_valid_credentials(driver):
    """
    Verify that user can log in with valid credentials
    """
    login_page = LoginPage(driver)

    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    assert "inventory.html" in driver.current_url


def test_login_with_invalid_credentials(driver):
    """
    Verify error message is shown for invalid login
    """
    login_page = LoginPage(driver)

    login_page.open()
    login_page.login("invalid_user", "invalid_password")

    assert login_page.is_error_displayed()
    assert "Username and password do not match" in login_page.get_error_message()