from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    """
    Page Object for SauceDemo Login Page
    URL: https://www.saucedemo.com
    """

    # ===== Locators =====
    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "h3[data-test='error']")

    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    # ===== Actions =====
    def open(self):
        self.driver.get("https://www.saucedemo.com")

    def enter_username(self, username: str):
        username_field = self.wait.until(
            EC.visibility_of_element_located(self.USERNAME_INPUT)
        )
        username_field.clear()
        username_field.send_keys(username)

    def enter_password(self, password: str):
        password_field = self.wait.until(
            EC.visibility_of_element_located(self.PASSWORD_INPUT)
        )
        password_field.clear()
        password_field.send_keys(password)

    def click_login(self):
        login_btn = self.wait.until(
            EC.element_to_be_clickable(self.LOGIN_BUTTON)
        )
        login_btn.click()

    def login(self, username: str, password: str):
        """
        Composite action: full login flow
        """
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()

    # ===== Assertions / State Checks =====
    def is_error_displayed(self) -> bool:
        return self.wait.until(
            EC.visibility_of_element_located(self.ERROR_MESSAGE)
        ).is_displayed()

    def get_error_message(self) -> str:
        return self.wait.until(
            EC.visibility_of_element_located(self.ERROR_MESSAGE)
        ).text