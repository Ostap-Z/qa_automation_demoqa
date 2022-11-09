from selenium.webdriver.support.select import Select

from pages.base_page import BasePage
from locators.widgets_locators.date_picker_locators import DatePickerLocators
from generator.generator import generated_date


class DatePickerPage(BasePage):
    locators = DatePickerLocators()

    def select_date(self):
        date = next(generated_date())
        input_date = self.element_is_visible(self.locators.DATE_INPUT)
        value_date_before = input_date.get_attribute("value")
        input_date.click()
        self.select_option_by_text(self.locators.DATE_SELECT_MONTH, date.month)
        self.select_option_by_text(self.locators.DATE_SELECT_YEAR, date.year)
        self.set_date_item_from_list(self.locators.DATE_SELECT_DAY_LIST, date.day)
        value_date_after = input_date.get_attribute("value")
        return value_date_before, value_date_after

    def set_date_item_from_list(self, elements, value):
        item_list = self.elements_are_present(elements)
        for item in item_list:
            if item.text == value:
                item.click()
                break
