from selenium.webdriver.common.by import By


class DynamicPropertiesLocators:
    ENABLE_AFTER_FIVE_SEC_BUTTON = (
        By.CSS_SELECTOR,
        "button#enableAfter"
    )
    COLOR_CHANGE_BUTTON = (
        By.CSS_SELECTOR,
        "button#colorChange"
    )
    VISIBLE_AFTER_FIVE_SEC_BUTTON = (
        By.CSS_SELECTOR,
        "button#visibleAfter"
    )
    TEXT_RANDOM_ID = (
        By.CSS_SELECTOR,
        "div[class='col-12 mt-4 col-md-6'] > div:nth-child(2) > p"
    )
