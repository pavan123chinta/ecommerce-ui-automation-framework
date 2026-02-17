from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


class DriverFactory:

    @staticmethod
    def get_driver(headless=False):
        chrome_options = Options()

        # DO NOT use your real Chrome profile
        chrome_options.add_argument("--disable-extensions")
        chrome_options.add_argument("--disable-notifications")
        chrome_options.add_argument("--disable-infobars")
        chrome_options.add_argument("--disable-save-password-bubble")
        chrome_options.add_argument("--disable-password-manager")
        chrome_options.add_argument("--disable-features=PasswordManager")
        chrome_options.add_argument("--disable-features=AutofillServerCommunication")
        chrome_options.add_argument("--incognito")  # 🔥 critical

        if headless:
            chrome_options.add_argument("--headless=new")

        driver = webdriver.Chrome(options=chrome_options)
        driver.maximize_window()
        return driver
