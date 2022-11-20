from selenium.webdriver.common.by import By


class AlertsLocators:
    # Button locators
    ALERT_BUTTON = (
        By.CSS_SELECTOR, "button#alertButton"
    )
    ALERT_TIMER_BUTTON = (
        By.CSS_SELECTOR, "button#timerAlertButton"
    )
    ALERT_CONFIRM_BUTTON = (
        By.CSS_SELECTOR, "button#confirmButton"
    )
    ALERT_PROMPT_BUTTON = (
        By.CSS_SELECTOR, "button#promtButton"
    )

    # Verification text results
    CONFIRM_TEXT_RESULT = (
        By.CSS_SELECTOR, "span#confirmResult"
    )
    PROMPT_TEXT_RESULT = (
        By.CSS_SELECTOR, "span#promptResult"
    )
