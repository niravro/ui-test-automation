import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="session")
def browser():
    """Create a WebDriver for tests.

    Priority:
    - If LambdaTest credentials present (LT_USERNAME / LT_ACCESS_KEY), use LambdaTest remote webdriver.
    - Otherwise, fall back to local headless Chrome.
    """
    lt_user = os.environ.get("LT_USERNAME")
    lt_key = os.environ.get("LT_ACCESS_KEY")

    if lt_user and lt_key:
        # LambdaTest remote configuration
        lt_url = f"https://{lt_user}:{lt_key}@hub.lambdatest.com/wd/hub"
        caps = {
            "platformName": "Windows 10",
            "browserName": "Chrome",
            "browserVersion": "120.0",
            "LT:Options": {
                "build": "pytest-lambdatest-build",
                "name": "pytest-lambdatest-session",
                "selenium_version": "4.10.0",
            },
        }
        driver = webdriver.Remote(command_executor=lt_url, desired_capabilities=caps)
        yield driver
        driver.quit()

    else:
        options = Options()
        options.add_argument("--headless=new")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--window-size=1920,1080")

        service = ChromeService(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=options)
        yield driver
        driver.quit()
