from selenium.webdriver.common.by import By


class DraggableLocators:
    # Locators for simple tab
    SIMPLE_TAB = (
        By.CSS_SELECTOR,
        "nav.nav.nav-tabs > a#draggableExample-tab-simple"
    )
    SIMPLE_DRAG_ME = (
        By.CSS_SELECTOR,
        "div#dragBox"
    )

    # Locators for axis restricted tab
    AXIS_RESTRICTED_TAB = (
        By.CSS_SELECTOR,
        "nav.nav.nav-tabs > a#draggableExample-tab-axisRestriction"
    )
    AXIS_RESTRICTED_ONLY_X = (
        By.CSS_SELECTOR,
        "div#restrictedX"
    )
    AXIS_RESTRICTED_ONLY_Y = (
        By.CSS_SELECTOR,
        "div#restrictedY"
    )
