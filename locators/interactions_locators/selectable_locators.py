from selenium.webdriver.common.by import By


class SelectableLocators:
    TAB_LIST = (
        By.CSS_SELECTOR,
        "a#demo-tab-list"
    )
    LIST_ITEMS = (
        By.CSS_SELECTOR,
        "ul#verticalListContainer"
        " > li.mt-2.list-group-item.list-group-item-action"
    )
    LIST_ITEM_ACTIVE = (
        By.CSS_SELECTOR,
        "ul#verticalListContainer"
        " > li.list-group-item.active.list-group-item-action"
    )

    TAB_GRID = (
        By.CSS_SELECTOR,
        "a#demo-tab-grid"
    )
    GRID_ITEMS = (
        By.CSS_SELECTOR,
        "div#gridContainer li.list-group-item.list-group-item-action")
    GRID_ITEM_ACTIVE = (
        By.CSS_SELECTOR,
        "div#gridContainer"
        " li.list-group-item.active.list-group-item-action"
    )
