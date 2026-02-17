from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ProductsPage:
    """
    Page Object for SauceDemo Products Page
    URL: https://www.saucedemo.com/inventory.html
    """

    # ===== Locators =====
    INVENTORY_ITEMS = (By.CLASS_NAME, "inventory_item")
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "button.btn_inventory")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")

    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    # ===== State Checks =====
    def is_loaded(self) -> bool:
        """
        Verify products page is loaded by checking inventory items
        """
        items = self.wait.until(
            EC.visibility_of_all_elements_located(self.INVENTORY_ITEMS)
        )
        return len(items) > 0

    def get_products_count(self) -> int:
        items = self.driver.find_elements(*self.INVENTORY_ITEMS)
        return len(items)

    # ===== Actions =====
    def add_first_product_to_cart(self):
        add_buttons = self.wait.until(
            EC.visibility_of_all_elements_located(self.ADD_TO_CART_BUTTON)
        )
        add_buttons[0].click()

    # ===== Assertions =====
    def is_cart_badge_visible(self) -> bool:
        return self.wait.until(
            EC.visibility_of_element_located(self.CART_BADGE)
        ).is_displayed()

    def get_cart_count(self) -> int:
        badge = self.wait.until(
            EC.visibility_of_element_located(self.CART_BADGE)
        )
        return int(badge.text)