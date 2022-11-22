from selenium.webdriver.common.by import By


class TabsLocators:
    WHAT_TAB = (
        By.CSS_SELECTOR,
        "a#demo-tab-what"
    )
    WHAT_CONTENT = (
        By.CSS_SELECTOR,
        "div#demo-tabpane-what > p"
    )

    ORIGIN_TAB = (
        By.CSS_SELECTOR,
        "a#demo-tab-origin"
    )
    ORIGIN_CONTENT = (
        By.CSS_SELECTOR,
        "div#demo-tabpane-origin > p"
    )

    USE_TAB = (
        By.CSS_SELECTOR,
        "a#demo-tab-use"
    )
    USE_CONTENT = (
        By.CSS_SELECTOR,
        "div#demo-tabpane-use > p"
    )

    MORE_TAB = (
        By.CSS_SELECTOR,
        "demo-tab-more"
    )
    MORE_CONTENT = (
        By.CSS_SELECTOR,
        "div#demo-tabpane-more"
    )
