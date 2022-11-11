from selenium.webdriver.common.by import By


class SortableLocators:
    TAB_LIST = (By.CSS_SELECTOR, "a#demo-tab-list")
    LIST_ITEMS = (By.CSS_SELECTOR, "div#demo-tabpane-list div.list-group-item.list-group-item-action")

    TAB_GRID = (By.CSS_SELECTOR, "a#demo-tab-grid")
    GRID_ITEMS = (By.CSS_SELECTOR, "div#demo-tabpane-grid div.list-group-item.list-group-item-action")
