import time
from random import randint

from selenium.common import UnexpectedAlertPresentException

from pages.base_page import BasePage
from locators.alerts_frame_windows_locators.alerts_locators import AlertsLocators


class AlertsPage(BasePage):
    locators = AlertsLocators()

    def check_default_alert(self):
        self.element_is_visible(self.locators.ALERT_BUTTON).click()
        try:
            alert = self.go_to_alert()
            return alert.text
        except UnexpectedAlertPresentException:
            alert = self.go_to_alert()
            return alert.text

    def check_timer_alert(self):
        self.element_is_visible(self.locators.ALERT_TIMER_BUTTON).click()
        time.sleep(5)
        try:
            alert = self.go_to_alert()
            return alert.text
        except UnexpectedAlertPresentException:
            alert = self.go_to_alert()
            return alert.text

    def check_confirm_alert(self):
        self.element_is_visible(self.locators.ALERT_CONFIRM_BUTTON).click()
        alert = self.go_to_alert()
        alert.accept()
        confirm_result_text = self.element_is_present(self.locators.CONFIRM_TEXT_RESULT).text
        return confirm_result_text.split(" ")[-1].lower()

    def check_prompt_alert(self):
        text = f"autotest{randint(0, 1000)}"
        self.element_is_visible(self.locators.ALERT_PROMPT_BUTTON).click()
        alert = self.go_to_alert()
        alert.send_keys(text)
        alert.accept()
        prompt_text_result = self.element_is_present(self.locators.PROMPT_TEXT_RESULT).text
        return prompt_text_result.split(" ")[-1], text
