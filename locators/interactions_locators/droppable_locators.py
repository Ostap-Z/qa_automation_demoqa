from selenium.webdriver.common.by import By


class DroppableLocators:
    # Locators for simple tab
    SIMPLE_TAB = (By.CSS_SELECTOR, "nav.nav.nav-tabs > a#droppableExample-tab-simple")
    SIMPLE_DRAG_ME = (By.CSS_SELECTOR, "div#draggable")
    SIMPLE_DROP_HERE = (By.CSS_SELECTOR, "div#simpleDropContainer > div#droppable")

    # Locators for accept tab
    ACCEPT_TAB = (By.CSS_SELECTOR, "nav.nav.nav-tabs > a#droppableExample-tab-accept")
    ACCEPT_ACCEPTABLE = (By.CSS_SELECTOR, "div#acceptable")
    ACCEPT_NOT_ACCEPTABLE = (By.CSS_SELECTOR, "div#notAcceptable")
    ACCEPT_DROP_HERE = (By.CSS_SELECTOR, "div#acceptDropContainer > div#droppable")

    # Locators for prevent propogation tab
    PREVENT_TAB = (By.CSS_SELECTOR, "nav.nav.nav-tabs > a#droppableExample-tab-preventPropogation")
    PREVENT_DRAG_ME = (By.CSS_SELECTOR, "div#dragBox")
    PREVENT_NOT_GREEDY_DROP_BOX_TEXT = (By.CSS_SELECTOR, "div#notGreedyDropBox > p")
    PREVENT_NOT_GREEDY_INNER_BOX = (By.CSS_SELECTOR, "div#notGreedyInnerDropBox")
    PREVENT_GREEDY_DROP_BOX_TEXT = (By.CSS_SELECTOR, "div#greedyDropBox > p")
    PREVENT_GREEDY_INNER_BOX = (By.CSS_SELECTOR, "div#greedyDropBoxInner > p")

    # Locators for revert draggable
    REVERT_TAB = (By.CSS_SELECTOR, "nav.nav.nav-tabs > a#droppableExample-tab-revertable")
    REVERT_WILL_REVERT = (By.CSS_SELECTOR, "div#revertable")
    REVERT_WILL_NOT_REVERT = (By.CSS_SELECTOR, "div#notRevertable")
    REVERT_DROP_HERE = (By.CSS_SELECTOR, "div#revertableDropContainer > div#droppable")
