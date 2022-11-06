from pages.alerts_frame_windows_page.alerts_page import AlertsPage


class TestAlerts:

    def test_default_alert(self, driver):
        alert_page = AlertsPage(driver, "https://demoqa.com/alerts")
        alert_page.open()
        alert_result = alert_page.check_default_alert()
        assert alert_result == "You clicked a button", f"\nActual result: alert is not presented. Alert text: {alert_result}" \
                                                       "\nExpected result: alert should be presented with text 'You clicked a button'"
