import time
from random import randint

from selenium.common import UnexpectedAlertPresentException

from pages.base_page import BasePage
from locators.alerts_frame_windows_locators.alerts_locators import AlertsLocators


class AlertsPage(BasePage):
    locators = AlertsLocators()

    def check_default_alert(self):
        log = self.get_logger()
        self.element_is_visible(self.locators.ALERT_BUTTON).click()
        log.info("Clicked on the alert button")
        try:
            alert = self.go_to_alert()
            log.info("Went to the alert")
            log.info(f"Alert text is '{alert.text}'")
            return alert.text
        except UnexpectedAlertPresentException:
            alert = self.go_to_alert()
            log.info("Went to the alert")
            log.info(f"Alert text is '{alert.text}'")
            return alert.text

    def check_timer_alert(self):
        log = self.get_logger()
        self.element_is_visible(self.locators.ALERT_TIMER_BUTTON).click()
        log.info("Clicked on the timer alert button")
        time.sleep(5)
        try:
            alert = self.go_to_alert()
            log.info("Went to the alert")
            log.info(f"Alert text is '{alert.text}'")
            return alert.text
        except UnexpectedAlertPresentException:
            alert = self.go_to_alert()
            log.info("Went to the alert")
            log.info(f"Alert text is '{alert.text}'")
            return alert.text

    def check_confirm_alert(self):
        log = self.get_logger()
        self.element_is_visible(self.locators.ALERT_CONFIRM_BUTTON).click()
        log.info("Clicked on the confirm alert button")
        alert = self.go_to_alert()
        log.info("Went to the alert")
        alert.accept()
        log.info("Accepted alert")
        confirm_result_text = self.element_is_present(self.locators.CONFIRM_TEXT_RESULT).text
        log.info(f"Text presented in the result: '{confirm_result_text.split(' ')[-1].lower()}'")
        return confirm_result_text.split(" ")[-1].lower()

    def check_prompt_alert(self):
        log = self.get_logger()
        text = f"autotest{randint(0, 1000)}"
        self.element_is_visible(self.locators.ALERT_PROMPT_BUTTON).click()
        log.info("Clicked on the prompt alert button")
        alert = self.go_to_alert()
        log.info("Went to the alert")
        alert.send_keys(text)
        log.info(f"Filled in alert prompt with data: '{text}'")
        alert.accept()
        log.info("Accepted alert")
        prompt_text_result = self.element_is_present(self.locators.PROMPT_TEXT_RESULT).text
        log.info(f"Text presented in the result: '{prompt_text_result.split(' ')[-1]}'")
        return prompt_text_result.split(" ")[-1], text
