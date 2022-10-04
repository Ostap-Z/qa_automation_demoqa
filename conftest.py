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


@pytest.fixture
def driver(request):
    browser_name = request.config.getoption("--browser_name").lower()

    if browser_name == "chrome":
        chrome_options = ChromeOptions()
        chrome_options.add_argument("headless")
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)

    elif browser_name == "firefox":
        firefox_options = FirefoxOptions()
        firefox_options.headless = True
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=firefox_options)

    elif browser_name == "edge":
        edge_options = EdgeOptions()
        edge_options.add_argument("headless")
        driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()), options=edge_options)

    yield driver
    driver.quit()
