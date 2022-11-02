import time

from pages.base_page import BasePage
from locators.dynamic_properties_locators import DynamicPropertiesLocators


class DynamicPropertiesPage(BasePage):
    locators = DynamicPropertiesLocators()

    def check_changed_color(self):
        color_button = self.element_is_present(self.locators.COLOR_CHANGE_BUTTON)
        color_button_before = color_button.value_of_css_property("color")
        time.sleep(5)
        color_button_after = color_button.value_of_css_property("color")
        return color_button_before, color_button_after
