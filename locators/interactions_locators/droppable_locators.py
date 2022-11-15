from selenium.webdriver.common.by import By


class DroppableLocators:
    # Locators for simple tab
    SIMPLE_TAB = (By.CSS_SELECTOR, "nav.nav.nav-tabs > a#droppableExample-tab-simple")
    SIMPLE_DRAG_ME = (By.CSS_SELECTOR, "div#draggable")
    SIMPLE_DROP_HERE = (By.CSS_SELECTOR, "div#simpleDropContainer > div#droppable")

    # Locators for accept tab
    ACCEPT_TAB = (By.CSS_SELECTOR, "nav.nav.nav-tabs > a#droppableExample-tab-accept")
    ACCEPTABLE = (By.CSS_SELECTOR, "div#acceptable")
    NOT_ACCEPTABLE = (By.CSS_SELECTOR, "div#notAcceptable")
    ACCEPT_DROP_HERE = (By.CSS_SELECTOR, "div#acceptDropContainer > div#droppable")

    # Locators for prevent propogation tab
    PREVENT_TAB = (By.CSS_SELECTOR, "nav.nav.nav-tabs > a#droppableExample-tab-preventPropogation")
    PREVENT_DRAG_ME = (By.CSS_SELECTOR, "div#dragBox")
    NOT_GREEDY_DROP_BOX_TEXT = (By.CSS_SELECTOR, "div#notGreedyDropBox > p")
    NOT_GREEDY_INNER_BOX = (By.CSS_SELECTOR, "div#notGreedyInnerDropBox")
    GREEDY_DROP_BOX_TEXT = (By.CSS_SELECTOR, "div#greedyDropBoxInner> p")
    GREEDY_INNER_BOX = (By.CSS_SELECTOR, "div#greedyDropBox")

    # Locators for revert draggable
    REVERT_TAB = (By.CSS_SELECTOR, "nav.nav.nav-tabs > a#droppableExample-tab-revertable")
    REVERT_WILL_REVERT = (By.CSS_SELECTOR, "div#revertable")
    REVERT_WILL_NOT_REVERT = (By.CSS_SELECTOR, "div#notRevertable")
    REVERT_DROP_HERE = (By.CSS_SELECTOR, "div#revertableDropContainer > div#droppable")
