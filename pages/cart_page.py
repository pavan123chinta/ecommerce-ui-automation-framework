from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage:

    # ===== Locators =====
    CART_ITEMS = (By.CLASS_NAME, "cart_item")
    CHECKOUT_BUTTON = (By.ID, "checkout")

    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def open(self):
        self.driver.get("https://www.saucedemo.com/cart.html")
        self.wait.until(EC.url_contains("cart.html"))

    def get_cart_items_count(self):
        items = self.wait.until(
            EC.visibility_of_all_elements_located(self.CART_ITEMS)
        )
        return len(items)

    def click_checkout(self):
        self.wait.until(
            EC.element_to_be_clickable(self.CHECKOUT_BUTTON)
        ).click()
