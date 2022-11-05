from selenium.webdriver.common.by import By


class BrowserWindowsLocators:
    NEW_TAB_BUTTON = (By.CSS_SELECTOR, "button#tabButton")
    NEW_WINDOW_BUTTON = (By.CSS_SELECTOR, "button#windowButton")
    NEW_WINDOW_MESSAGE_BUTTON = (By.CSS_SELECTOR, "messageWindowButton")
