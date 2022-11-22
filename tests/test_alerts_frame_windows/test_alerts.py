from pages.alerts_frame_windows_page.alerts_page import AlertsPage


class TestAlerts:

    def test_default_alert(self, driver):
        alert_page = AlertsPage(
            driver,
            "https://demoqa.com/alerts"
        )
        alert_page.open()
        alert_result = alert_page.check_default_alert()
        assert alert_result == "You clicked a button", \
            f"\nActual result: alert is not presented. " \
            f"Alert text: {alert_result}" \
            "\nExpected result: " \
            "alert should be presented with text 'You clicked a button'"

    def test_timer_alert(self, driver):
        alert_page = AlertsPage(
            driver,
            "https://demoqa.com/alerts"
        )
        alert_page.open()
        alert_result = alert_page.check_timer_alert()
        assert alert_result == "This alert appeared after 5 seconds", \
            f"\nActual result: alert is not presented. " \
            f"Alert text: {alert_result}" \
            "\nExpected result: alert should be presented with text" \
            " 'This alert appeared after 5 seconds'"

    def test_confirm_alert(self, driver):
        alert_page = AlertsPage(
            driver,
            "https://demoqa.com/alerts"
        )
        alert_page.open()
        confirm_alert_result = alert_page.check_confirm_alert()
        assert confirm_alert_result == "ok".lower(), \
            f"\nActual result: alert is not presented or confirmed, " \
            f"text result is {confirm_alert_result}"\
            "\nExpected result: message 'ok' should be shown" \
            " after the alert confirmation"

    def test_prompt_alert(self, driver):
        alert_page = AlertsPage(
            driver,
            "https://demoqa.com/alerts"
        )
        alert_page.open()
        prompt_text_result, text = alert_page.check_prompt_alert()
        assert text == prompt_text_result, \
            f"Actual result: text presented in the span is " \
            f"'{prompt_text_result}'"\
            f"Expected result: result text in the span" \
            f" should be '{text}'"
