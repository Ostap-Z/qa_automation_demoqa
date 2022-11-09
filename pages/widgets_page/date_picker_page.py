from pages.base_page import BasePage
from locators.widgets_locators.date_picker_locators import DatePickerLocators
from generator.generator import generated_date


class DatePickerPage(BasePage):
    locators = DatePickerLocators()

    def select_date(self):
        log = self.get_logger()
        date = next(generated_date())
        log.info(f"Generated date with data: {date}")
        input_date = self.element_is_clickable(self.locators.DATE_INPUT)
        value_date_before = input_date.get_attribute("value")
        input_date.click()
        log.info("Opened date picker section")
        self.select_option_by_text(self.locators.DATE_SELECT_MONTH, date.month)
        self.select_option_by_text(self.locators.DATE_SELECT_YEAR, date.year)
        self.set_date_item_from_list(self.locators.DATE_SELECT_DAY_LIST, date.day)
        value_date_after = input_date.get_attribute("value")
        log.info(f"Date value before test: {value_date_before}")
        log.info(f"Date value after test: {value_date_after}")
        return value_date_before, value_date_after

    def set_date_item_from_list(self, elements, value):
        log = self.get_logger()
        item_list = self.elements_are_present(elements)
        for item in item_list:
            if item.text == value:
                item.click()
                log.info(f"Chose item: {item.text}")
                break
