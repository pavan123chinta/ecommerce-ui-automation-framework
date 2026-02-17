import pytest

from pages.login_page import LoginPage
from pages.products_page import ProductsPage


def test_products_page_loaded_after_login(driver):
    """
    Verify products page loads after valid login
    """
    login = LoginPage(driver)
    login.open()
    login.login("standard_user", "secret_sauce")

    products = ProductsPage(driver)

    assert products.is_loaded(), "Products page did not load"


def test_add_product_updates_cart_badge(driver):
    """
    Verify adding a product updates cart badge count
    """
    login = LoginPage(driver)
    login.open()
    login.login("standard_user", "secret_sauce")

    products = ProductsPage(driver)
    products.add_first_product_to_cart()

    assert products.is_cart_badge_visible(), "Cart badge not visible"
    assert products.get_cart_count() == 1, "Cart count should be 1"