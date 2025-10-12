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
    bs_user = os.environ.get("BROWSERSTACK_USERNAME")
    bs_key = os.environ.get("BROWSERSTACK_ACCESS_KEY")

    if lt_user and lt_key:
        # LambdaTest remote configuration
        lt_url = f"https://{lt_user}:{lt_key}@hub.lambdatest.com/wd/hub"
        # caps = {
        #     "platformName": "Windows 10",
        #     "browserName": "Chrome",
        #     "browserVersion": "120.0",
        #     "LT:Options": {
        #         "build": "pytest-lambdatest-build",
        #         "name": "pytest-lambdatest-session",
        #         "selenium_version": "3.14",
        #     },
        # }
        chrome_options = webdriver.ChromeOptions()
        option = {
            "platform": "Windows 10",
            "version": "latest",
            "name": "pytest-lambdatest-pom",
            "Build": "pytest-lambdatest-pom",
            "video": True,
            "visual": True,
            "network": True,
            "console": True
        }
        chrome_options.set_capability("LT:Options", option)
        # driver = webdriver.Remote(command_executor=lt_url, desired_capabilities=caps)
        driver = webdriver.Remote(command_executor=lt_url, options=chrome_options)
        yield driver
        driver.quit()

    elif bs_user and bs_key:
        # BrowserStack remote configuration
        bs_url = f"https://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub"
        bs_caps = {
            "browserName": "Chrome",
            "browserVersion": "latest",
            "bstack:options": {
                "os": "Windows",
                "osVersion": "11",
                "projectName": "pytest-browserstack-project",
                "sessionName": "pytest-browserstack-session",
            },
        }
        driver = webdriver.Remote(command_executor=bs_url, desired_capabilities=bs_caps)
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
