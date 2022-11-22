from selenium.webdriver.common.by import By


class ProgressBarLocators:
    PROGRESS_BAR_BUTTON = (
        By.CSS_SELECTOR,
        "button#startStopButton"
    )
    PROGRESS_BAR_VALUE = (
        By.CSS_SELECTOR,
        "div.progress-bar.bg-info"
    )
