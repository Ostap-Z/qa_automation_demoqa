import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def driver():
    chrome_options = ChromeOptions()
    chrome_options.add_argument("headless")
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)

    yield driver
    driver.quit()
