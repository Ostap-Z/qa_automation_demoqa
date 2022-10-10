from selenium.webdriver.common.by import By


class RadioButtonPageLocators:
    RADIO_BUTTONS_LIST = (By.CLASS_NAME, "custom-radio")
    TITLE_ITEM = (By.XPATH, ".//ancestor::label[@class='custom-control-label']")
    OUTPUT_RESULT = (By.CLASS_NAME, "text-success")
