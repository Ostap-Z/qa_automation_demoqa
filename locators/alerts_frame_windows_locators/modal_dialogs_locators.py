from selenium.webdriver.common.by import By


class ModalDialogsLocators:
    SMALL_MODAL_BUTTON = (By.CSS_SELECTOR, "button#showSmallModal")
    SMALL_MODAL_CLOSE_BUTTON = (By.CSS_SELECTOR, "button#closeSmallModal")
    SMALL_MODAL_TITLE = (By.CSS_SELECTOR, "div#example-modal-sizes-title-sm")
    SMALL_MODAL_TEXT = (By.CSS_SELECTOR, "div.modal-body")

    LARGE_MODAL_BUTTON = (By.CSS_SELECTOR, "button#showLargeModal")
    LARGE_MODAL_CLOSE_BUTTON = (By.CSS_SELECTOR, "button#closeLargeModal")
    LARGE_MODAL_TITLE = (By.CSS_SELECTOR, "div#example-modal-sizes-title-lg")
    LARGE_MODAL_TEXT = (By.CSS_SELECTOR, "div.modal-body > p")
