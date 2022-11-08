from random import sample, randint

from selenium.webdriver import Keys

from pages.base_page import BasePage
from locators.widgets_locators.auto_complete_locators import AutoCompleteLocators
from generator.generator import generated_color


class AutoCompletePage(BasePage):
    locators = AutoCompleteLocators()

    def fill_multiple_input(self):
        log = self.get_logger()
        colors = sample(next(generated_color()).color_name, k=randint(2, 6))
        log.info(f"Generated colors with data: {colors}")
        for color in colors:
            multiple_input = self.element_is_clickable(self.locators.MULTIPLE_INPUT)
            multiple_input.send_keys(color)
            multiple_input.send_keys(Keys.ENTER)
            log.info(f"Filled in field with value: {color}")
        log.info(f"Filled in multiple input with data: {colors}")
        return colors

    def remove_multiple_value(self):
        log = self.get_logger()
        count_value_before = len(self.elements_are_present(self.locators.MULTIPLE_VALUE))
        remove_button_list = self.elements_are_visible(self.locators.MULTIPLE_VALUE_REMOVE)
        for value in remove_button_list:
            value.click()
            log.info(f"Removed value from color list")
            break
        count_value_after = len(self.elements_are_present(self.locators.MULTIPLE_VALUE))
        log.info(f"Count of values before, after: {count_value_before}, {count_value_after}")
        return count_value_before, count_value_after

    def check_multiple_color(self):
        log = self.get_logger()
        color_list = self.elements_are_present(self.locators.MULTIPLE_VALUE)
        colors = [color.text for color in color_list]
        log.info(f"Returned colors: {colors} ")
        return colors


















