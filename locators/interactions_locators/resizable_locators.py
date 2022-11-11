from selenium.webdriver.common.by import By


class ResizableLocators:
    RESIZABLE_LARGE_BOX_HANDLE = (By.CSS_SELECTOR, "div.constraint-area span.react-resizable-handle.react-resizable-handle-se")
    RESIZABLE_LARGE_BOX = (By.CSS_SELECTOR, "div#resizableBoxWithRestriction")

    RESIZABLE_SMALL_BOX_HANDLE = (By.CSS_SELECTOR, "div#resizable span.react-resizable-handle.react-resizable-handle-se")
    RESIZABLE_SMALL_BOX = (By.CSS_SELECTOR, "div#resizable")
