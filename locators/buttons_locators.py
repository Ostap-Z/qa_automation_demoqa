from selenium.webdriver.common.by import By


class ButtonsPageLocators:

    # Locators for buttons on the buttons page
    DOUBLE_CLICK_BUTTON = (By.CSS_SELECTOR, "button#doubleClickBtn")
    RIGHT_CLICK_BUTTON = (By.CSS_SELECTOR, "button#rightClickBtn")
    LEFT_CLICK_BUTTON = (By.CSS_SELECTOR, "button#UdmHn")

    # Locators for the result of clicked buttons
    SUCCESS_DOUBLE_CLICK = (By.CSS_SELECTOR, "p#doubleClickMessage")
    SUCCESS_RIGHT_CLICK = (By.CSS_SELECTOR, "p#rightClickMessage")
    SUCCESS_LEFT_CLICK = (By.CSS_SELECTOR, "p#dynamicClickMessage")
