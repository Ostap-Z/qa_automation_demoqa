import time

from selenium.common import TimeoutException

from pages.base_page import BasePage
from locators.dynamic_properties_locators import DynamicPropertiesLocators


class DynamicPropertiesPage(BasePage):
    locators = DynamicPropertiesLocators()

    def check_enable_button(self):
        try:
            self.element_is_clickable(self.locators.ENABLE_AFTER_FIVE_SEC_BUTTON)
        except TimeoutException:
            return False
        return True

    def check_changed_color(self):
        color_button = self.element_is_present(self.locators.COLOR_CHANGE_BUTTON)
        color_button_before = color_button.value_of_css_property("color")
        time.sleep(5)
        color_button_after = color_button.value_of_css_property("color")
        return color_button_before, color_button_after

    def check_appear_button(self):
        try:
            self.element_is_visible(self.locators.VISIBLE_AFTER_FIVE_SEC_BUTTON)
        except TimeoutException:
            return False
        return True
