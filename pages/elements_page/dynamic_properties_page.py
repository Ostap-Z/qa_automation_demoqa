import time

import allure
from selenium.common import TimeoutException

from pages.base_page import BasePage
from locators.elements_locators.dynamic_properties_locators \
    import DynamicPropertiesLocators


class DynamicPropertiesPage(BasePage):
    locators = DynamicPropertiesLocators()

    @allure.step(
        "Check the 'Enable' button"
    )
    def check_enable_button(self):
        log = self.get_logger()
        try:
            with allure.step("Wait an expectation time "
                             "to be clickable "
                             "the 'Enable After' button"):
                self.element_is_clickable(
                    self.locators.ENABLE_AFTER_FIVE_SEC_BUTTON)

            log.info("Clicked on the enable after 5 seconds button")
        except TimeoutException:
            return False
        return True

    @allure.step(
        "Check the 'Change Color' button"
    )
    def check_changed_color(self):
        log = self.get_logger()
        color_button = self.element_is_present(
            self.locators.COLOR_CHANGE_BUTTON)
        log.info("Color button is presented in the DOM")
        with allure.step("Get the button color before"):
            color_button_before = \
                color_button.value_of_css_property("color")

        log.info(f"Color button before: {color_button_before}")

        with allure.step("Wait an expectation time "
                         "to change a color of the "
                         "'Change Color' button"):
            time.sleep(5)

        with allure.step("Get the button color after"):
            color_button_after = \
                color_button.value_of_css_property("color")

        log.info(f"Color button after: {color_button_after}")
        return color_button_before, color_button_after

    @allure.step(
        "Check the 'Visible After' button"
    )
    def check_appear_button(self):
        log = self.get_logger()
        try:
            with allure.step("Wait an expectation time to be visible "
                             "the 'Visible After' button"):
                self.element_is_visible(
                    self.locators.VISIBLE_AFTER_FIVE_SEC_BUTTON)

            log.info("Visible after 5 seconds button is visible")
        except TimeoutException:
            return False
        return True
