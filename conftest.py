import pytest
import os
from datetime import datetime
from utils.driver_factory import DriverFactory


@pytest.fixture
def driver():
    driver = DriverFactory.get_driver(headless=False)
    yield driver
    driver.quit()


#  Screenshot hook on failure
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    # Only capture screenshot on test failure
    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver", None)

        if driver:
            screenshots_dir = "screenshots"
            os.makedirs(screenshots_dir, exist_ok=True)

            timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            test_name = item.name

            file_name = f"{screenshots_dir}/{test_name}_{timestamp}.png"
            driver.save_screenshot(file_name)

            print(f"\n📸 Screenshot saved: {file_name}")
