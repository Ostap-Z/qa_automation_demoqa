from random import sample, randint

import allure
from selenium.webdriver import Keys

from pages.base_page import BasePage
from locators.widgets_locators.auto_complete_locators import AutoCompleteLocators
from generator.generator import generated_color


class AutoCompletePage(BasePage):
    locators = AutoCompleteLocators()

    @allure.step(
        "Fill in the input with multiple values"
    )
    def fill_multiple_input(self):
        log = self.get_logger()

        with allure.step("Generate random colors"):
            colors = sample(next(
                generated_color()).color_name,
                            k=randint(2, 6)
                            )

        log.info(f"Generated colors: {colors}")

        with allure.step("Fill in the 'Multiple Colors' field"):
            for color in colors:
                with allure.step(f"Fill in the 'Multiple Colors' "
                                 f"field with {color} color"):
                    multiple_input = self.element_is_clickable(
                        self.locators.MULTIPLE_INPUT)
                    multiple_input.send_keys(color)
                    multiple_input.send_keys(Keys.ENTER)

                log.info(f"Filled in field with value: {color}")
        log.info(f"Filled in multiple input with data: {colors}")
        return colors

    @allure.step(
        "Remove multiple colors"
    )
    def remove_multiple_value(self):
        log = self.get_logger()

        with allure.step("Get amount of values before remove"):
            count_value_before = len(self.elements_are_present(
                self.locators.MULTIPLE_VALUE))

        remove_button_list = self.elements_are_visible(
            self.locators.MULTIPLE_VALUE_REMOVE)

        with allure.step("Remove values from the field"):
            for value in remove_button_list:
                with allure.step(f"Remove a value"):
                    value.click()

                log.info(f"Removed value from color list")
                break

        with allure.step("Get amount of values after remove"):
            count_value_after = len(self.elements_are_present(
                self.locators.MULTIPLE_VALUE))

        log.info(f"Count of values before, after: "
                 f"{count_value_before}, "
                 f"{count_value_after}")
        return count_value_before, count_value_after

    @allure.step(
        "Check multiple values"
    )
    def check_multiple_values(self):
        log = self.get_logger()
        color_list = self.elements_are_present(
            self.locators.MULTIPLE_VALUE)
        colors = [color.text for color in color_list]
        log.info(f"Returned colors: {colors} ")
        return colors

    @allure.step(
        "Fill in the input with single value"
    )
    def fill_single_input(self):
        log = self.get_logger()

        with allure.step("Generate a random color"):
            color = sample(next(
                generated_color()).color_name, k=1)

        log.info(f"Generated color: {color}")

        with allure.step(f"Fill in the 'Single Color' "
                         f"field with {color[0]} color"):
            single_input = self.element_is_clickable(
                self.locators.SINGLE_INPUT)
            single_input.send_keys(color)
            single_input.send_keys(Keys.ENTER)
        log.info(f"Filled in single input with data: {color}")
        return color[0]

    @allure.step(
        "Check single value"
    )
    def check_single_value(self):
        log = self.get_logger()
        color = self.element_is_visible(
            self.locators.SINGLE_VALUE)
        log.info(f"Returned color: '{color.text}'")
        return color.text
