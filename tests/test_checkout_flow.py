from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


def test_complete_checkout_flow(driver):
    # Step 1: Login
    login = LoginPage(driver)
    login.open()
    login.login("standard_user", "secret_sauce")

    # Step 2: Add product
    products = ProductsPage(driver)
    products.add_first_product_to_cart()

    # Step 3: Go to cart
    cart = CartPage(driver)
    cart.open()
    cart.click_checkout()

    # Step 4: Checkout process
    checkout = CheckoutPage(driver)
    checkout.fill_customer_info("Pavan", "Chinta", "500001")
    checkout.click_continue()
    checkout.click_finish()

    # Step 5: Verify success
    assert checkout.is_order_successful()
