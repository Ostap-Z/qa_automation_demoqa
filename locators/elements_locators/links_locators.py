from selenium.webdriver.common.by import By


class LinksPageLocators:
    SIMPLE_LINK = (
        By.CSS_SELECTOR,
        "a#simpleLink"
    )
    BAD_REQUEST_LINK = (
        By.CSS_SELECTOR,
        "a#bad-request"
    )
