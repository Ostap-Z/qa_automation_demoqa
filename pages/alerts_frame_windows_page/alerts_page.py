import time
from random import randint

import allure
from selenium.common import UnexpectedAlertPresentException

from pages.base_page import BasePage
from locators.alerts_frame_windows_locators.alerts_locators import AlertsLocators


class AlertsPage(BasePage):
    locators = AlertsLocators()

    @allure.step(
        "Check the 'Default Alert'"
    )
    def check_default_alert(self):
        log = self.get_logger()

        with allure.step("Click on the 'Default Alert' button"):
            self.element_is_visible(self.locators.ALERT_BUTTON)\
                .click()
        log.info("Clicked on the 'Default Alert' button")

        with allure.step("Switch to the 'Default Alert'"):
            try:
                alert = self.go_to_alert()
                log.info("Went to the alert")
                log.info(f"Alert text is '{alert.text}'")
                # return alert.text
            except UnexpectedAlertPresentException:
                alert = self.go_to_alert()
                log.info("Went to the alert")
                log.info(f"Alert text is '{alert.text}'")
                # return alert.text
        with allure.step("Get alert text result"):
            return alert.text

    @allure.step(
        "Check the 'Timer Alert'"
    )
    def check_timer_alert(self):
        log = self.get_logger()

        with allure.step("Click on the 'Timer Alert'' button"):
            self.element_is_visible(self.locators.ALERT_TIMER_BUTTON)\
                .click()
        log.info("Clicked on the 'Timer Alert' button")

        with allure.step("Wait 5 seconds to be able"
                         " to switch to the 'Timer Alert'"):
            time.sleep(5)

        with allure.step("Switch to the 'Timer Alert'"):
            try:
                alert = self.go_to_alert()
                log.info("Went to the alert")
                log.info(f"Alert text is '{alert.text}'")
                # return alert.text
            except UnexpectedAlertPresentException:
                alert = self.go_to_alert()
                log.info("Went to the alert")
                log.info(f"Alert text is '{alert.text}'")
                # return alert.text
        with allure.step("Get alert text result"):
            return alert.text

    @allure.step(
        "Check the 'Confirm Alert'"
    )
    def check_confirm_alert(self):
        log = self.get_logger()

        with allure.step("Click on the 'Confirm Alert' button"):
            self.element_is_visible(self.locators.ALERT_CONFIRM_BUTTON)\
                .click()
        log.info("Clicked on the 'Confirm Alert' button")

        with allure.step("Switch to the 'Confirm Alert'"):
            alert = self.go_to_alert()
        log.info("Went to the alert")

        with allure.step("Accept the 'Confirm Alert'"):
            alert.accept()
        log.info("Accepted alert")

        with allure.step("Get alert text result"):
            confirm_result_text = self.element_is_present(
                self.locators.CONFIRM_TEXT_RESULT).text

        log.info(f"Text presented in the result: "
                 f"'{confirm_result_text.split(' ')[-1].lower()}'")
        return confirm_result_text.split(" ")[-1].lower()

    @allure.step(
        "Check the 'Prompt Alert'"
    )
    def check_prompt_alert(self):
        log = self.get_logger()

        with allure.step("Generate a random text"
                         " for the 'Prompt Alert'"):
            text = f"autotest{randint(0, 1000)}"

        with allure.step("Click on the 'Prompt Alert' button"):
            self.element_is_visible(self.locators.ALERT_PROMPT_BUTTON)\
                .click()
        log.info("Clicked on the prompt alert button")

        with allure.step("Switch to the 'Prompt Alert'"):
            alert = self.go_to_alert()
        log.info("Went to the alert")

        with allure.step("Fills in the 'Prompt Alert' field"
                         f" with data: {text}"):
            alert.send_keys(text)
        log.info(f"Filled in alert prompt with data: '{text}'")

        with allure.step("Accept the 'Prompt Alert'"):
            alert.accept()
        log.info("Accepted alert")

        with allure.step("Get alert text result"):
            prompt_text_result = self.element_is_present(
                self.locators.PROMPT_TEXT_RESULT).text

        log.info(f"Text presented in the result: "
                 f"'{prompt_text_result.split(' ')[-1]}'")
        return prompt_text_result.split(" ")[-1], text
