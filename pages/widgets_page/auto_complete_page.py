from random import sample, randint

from selenium.webdriver import Keys

from pages.base_page import BasePage
from locators.widgets_locators.auto_complete_locators import AutoCompleteLocators
from generator.generator import generated_color


class AutoCompletePage(BasePage):
    locators = AutoCompleteLocators()

    def fill_multiple_input(self):
        colors = sample(next(generated_color()).color_name, k=randint(2, 6))
        for color in colors:
            multiple_input = self.element_is_clickable(self.locators.MULTIPLE_INPUT)
            multiple_input.send_keys(color)
            multiple_input.send_keys(Keys.ENTER)
        return colors

    def remove_multiple_value(self):
        count_value_before = len(self.elements_are_present(self.locators.MULTIPLE_VALUE))
        remove_button_list = self.elements_are_visible(self.locators.MULTIPLE_VALUE_REMOVE)
        for value in remove_button_list:
            value.click()
            break
        count_value_after = len(self.elements_are_present(self.locators.MULTIPLE_VALUE))
        return count_value_before, count_value_after

    def check_multiple_color(self):
        color_list = self.elements_are_present(self.locators.MULTIPLE_VALUE)
        colors = [color.text for color in color_list]
        return colors


















