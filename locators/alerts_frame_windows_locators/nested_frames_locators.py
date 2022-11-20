from selenium.webdriver.common.by import By


class NestedFramesLocators:
    PARENT_FRAME = (
        By.CSS_SELECTOR, "iframe#frame1"
    )
    CHILD_FRAME = (
        By.CSS_SELECTOR, "iframe[srcdoc='<p>Child Iframe</p>']"
    )
    PARENT_TEXT = (
        By.XPATH, "//*[text()='Parent frame']"
    )
    CHILD_TEXT = (
        By.XPATH, "//p[text()='Child Iframe']"
    )
