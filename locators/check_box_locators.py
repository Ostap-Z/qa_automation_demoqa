from selenium.webdriver.common.by import By


class CheckBoxPageLocators:

    EXPAND_ALL_BUTTON = (By.CSS_SELECTOR, "button[title='Expand all']")
    CHECK_BOXES_ITEM_LIST = (By.CLASS_NAME, "rct-title")
    CHECKED_ITEMS_LIST = (By.CLASS_NAME, "rct-icon-check")
    TITLE_ITEM = (By.XPATH, ".//ancestor::span[@class='rct-text']")
    OUTPUT_RESULT = (By.CLASS_NAME, "text-success")
