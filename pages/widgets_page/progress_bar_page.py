from time import sleep
from random import randint

import allure

from pages.base_page import BasePage
from locators.widgets_locators.progress_bar_locators import ProgressBarLocators


class ProgressBarPage(BasePage):
    locators = ProgressBarLocators()

    @allure.step(
        "Check the 'Progress Bar' value"
    )
    def change_progress_bar_value(self):
        log = self.get_logger()

        with allure.step("Get the 'Progress Bar' value "
                         "before movement"):
            value_before = \
                self.element_is_present(
                    self.locators.PROGRESS_BAR_VALUE).get_attribute(
                    "aria-valuenow")

        log.info(f"Progress bar value before: {value_before}")

        with allure.step("Start the 'Progress Bar'"):
            progress_bar_button = self.element_is_present(
                self.locators.PROGRESS_BAR_BUTTON)
            progress_bar_button.click()

        with allure.step("Waiting random time from 0 to 7 seconds "
                         "for change the 'Progress Bar' value"):
            sleep(randint(0, 7))

        log.info("Progress bar was moved")

        with allure.step("Stop the 'Progress Bar'"):
            progress_bar_button.click()

        with allure.step("Get the 'Progress Bar' value "
                         "after movement"):
            value_after = \
                self.element_is_present(
                    self.locators.PROGRESS_BAR_VALUE).get_attribute(
                    "aria-valuenow")

        log.info(f"Progress bar value after: {value_after}")
        return value_before, value_after
