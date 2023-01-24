from datetime import datetime

import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name",
        action="store",
        default="chrome",
        help="Choose browser: [Chrome, Firefox, Edge]"
    )
    parser.addoption(
        "--headless",
        action="store",
        default="no",
        help="Run tests in headless mode: yes, no"
    )


@pytest.fixture
def driver(request):
    browser_name = request.config.getoption("--browser_name").lower()
    headless_mode = request.config.getoption("--headless").lower()
    chrome_options = ChromeOptions()
    firefox_options = FirefoxOptions()
    edge_options = EdgeOptions()

    if browser_name == "chrome":
        if headless_mode == "yes":
            chrome_options.add_argument("headless")
        else:
            chrome_options.add_argument("start-maximized")
        driver = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install()),
            options=chrome_options)

    elif browser_name == "firefox":
        if headless_mode == "yes":
            firefox_options.headless = True
        driver = webdriver.Firefox(
            service=FirefoxService(GeckoDriverManager().install()),
            options=firefox_options
        )
        driver.maximize_window()

    elif browser_name == "edge":
        if headless_mode == "yes":
            edge_options.add_argument("headless")
        driver = webdriver.Edge(
            service=EdgeService(EdgeChromiumDriverManager().install()),
            options=edge_options
        )
        driver.maximize_window()

    yield driver

    if request.node.rep_call.failed:
        allure.attach(
            driver.get_screenshot_as_png(),
            name=f"Screenshot {request.function.__name__} {datetime.today()}",
            attachment_type=allure.attachment_type.PNG
        )
    driver.quit()


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep


def pytest_html_report_title(report):
    report.title = "Demoqa UI test results"
