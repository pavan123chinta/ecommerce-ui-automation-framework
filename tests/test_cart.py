import pytest

from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage


def test_added_product_visible_in_cart(driver):
    # Step 1: Login
    login = LoginPage(driver)
    login.open()
    login.login("standard_user", "secret_sauce")

    # Step 2: Add product from products page
    products = ProductsPage(driver)
    products.add_first_product_to_cart()

    # Step 3: Go to cart
    cart = CartPage(driver)
    cart.open()

    # Step 4: Assert product is visible
    assert cart.get_cart_items_count() == 1
