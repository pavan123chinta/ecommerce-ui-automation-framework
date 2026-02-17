from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:

    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    POSTAL_CODE = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    FINISH_BUTTON = (By.ID, "finish")
    SUCCESS_HEADER = (By.CLASS_NAME, "complete-header")

    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)
        self.wait.until(EC.url_contains("checkout-step-one"))

    def fill_customer_info(self, first, last, zip_code):
        self.wait.until(EC.visibility_of_element_located(self.FIRST_NAME)).send_keys(first)
        self.wait.until(EC.visibility_of_element_located(self.LAST_NAME)).send_keys(last)
        self.wait.until(EC.visibility_of_element_located(self.POSTAL_CODE)).send_keys(zip_code)

    def click_continue(self):
        self.wait.until(EC.element_to_be_clickable(self.CONTINUE_BUTTON)).click()

    def click_finish(self):
        self.wait.until(EC.element_to_be_clickable(self.FINISH_BUTTON)).click()

    def is_order_successful(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.SUCCESS_HEADER)
        ).is_displayed()
