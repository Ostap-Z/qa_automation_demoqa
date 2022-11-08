from time import sleep
from random import randint

from pages.base_page import BasePage
from locators.widgets_locators.progress_bar_locators import ProgressBarLocators


class ProgressBarPage(BasePage):
    locators = ProgressBarLocators()

    def change_progress_bar_value(self):
        log = self.get_logger()
        value_before = self.element_is_present(self.locators.PROGRESS_BAR_VALUE).get_attribute("aria-valuenow")
        log.info(f"Progress bar value before: {value_before}")
        progress_bar_button = self.element_is_present(self.locators.PROGRESS_BAR_BUTTON)
        progress_bar_button.click()
        sleep(randint(0, 7))
        log.info("Progress bar was moved")
        progress_bar_button.click()
        value_after = self.element_is_present(self.locators.PROGRESS_BAR_VALUE).get_attribute("aria-valuenow")
        log.info(f"Progress bar value after: {value_after}")
        return value_before, value_after
