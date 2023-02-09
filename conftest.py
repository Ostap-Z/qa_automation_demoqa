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
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.firefox.service import Service as FirefoxService


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name",
        action="store",
        default="chrome",
        help="Choose browser: [Chrome, Firefox, Edge]"
    )
    parser.addoption(
        "--browser_version",
        action="store",
        default=""
    )
    parser.addoption(
        "--headless",
        action="store",
        default=False,
        help="Run tests in headless mode"
    )
    parser.addoption(
        "--remote",
        action="store",
        default=False
    )
    parser.addoption(
        "--hub",
        action="store",
        default="localhost"
    )


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep


@pytest.fixture
def config(request):
    browser = request.config.getoption("--browser_name")
    browser_version = request.config.getoption("--browser_version")
    hub = request.config.getoption("--hub")
    headless = False
    remote = False

    if request.config.getoption("--headless") == "Yes".lower():
        headless = True
    if request.config.getoption("--remote") == "Yes".lower():
        remote = True

    return {
        "browser": browser,
        "browser_version": browser_version,
        "headless": headless,
        "remote": remote,
        "hub": hub
    }


def get_chrome_options(config):
    options = ChromeOptions()
    options.headless = config.get("headless", None)
    return options


def get_firefox_options(config):
    options = FirefoxOptions()
    options.headless = config.get("headless", None)
    return options


def get_edge_options(config):
    options = EdgeOptions()
    options.headless = config.get("headless", None)
    return options


def create_remote_driver(config):
    if config["browser"] == "chrome":
        options = get_chrome_options(config)
    elif config["browser"] == "edge":
        options = get_edge_options(config)
    elif config["browser"] == "firefox":
        options = get_firefox_options(config)

    desired_capabilities = {
        "browser_version": config["browser_version"],
        "acceptInsecureCerts": True,
        "screenResolution": "1280x1024x24"
    }

    return webdriver.Remote(
        command_executor=f"http://{config['hub']}:4444/wd/hub",
        options=options,
        desired_capabilities=desired_capabilities
    )


def create_local_driver(config):
    driver = None

    if config["browser"] == "chrome":
        options = get_chrome_options(config)
        driver = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install()),
            options=options
        )

    elif config["browser"] == "edge":
        options = get_edge_options(config)
        driver = webdriver.Edge(
            service=EdgeService(EdgeChromiumDriverManager().install()),
            options=options
        )

    elif config["browser"] == "firefox":
        options = get_firefox_options(config)
        driver = webdriver.Firefox(
            service=FirefoxService(GeckoDriverManager().install()),
            options=options
        )
    return driver


@pytest.fixture
def driver(request, config):
    driver = None

    if config.get("remote", False):
        driver = create_remote_driver(config)
    else:
        driver = create_local_driver(config)
        driver.maximize_window()

    yield driver

    if request.node.rep_call.failed:
        allure.attach(
            driver.get_screenshot_as_png(),
            name=f"Screenshot {request.function.__name__} {datetime.today()}",
            attachment_type=allure.attachment_type.PNG
        )
    driver.quit()


def pytest_html_report_title(report):
    report.title = "Demoqa UI test results"
