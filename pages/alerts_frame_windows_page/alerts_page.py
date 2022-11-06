from pages.base_page import BasePage
from locators.alerts_frame_windows_locators.alerts_locators import AlertsLocators


class AlertsPage(BasePage):
    locators = AlertsLocators()

    def check_default_alert(self):
        self.element_is_visible(self.locators.ALERT_BUTTON).click()
        alert_window = self.driver.switch_to.alert
        return alert_window.text
