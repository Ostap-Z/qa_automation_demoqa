import time

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
