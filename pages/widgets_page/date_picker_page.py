from pages.base_page import BasePage
from locators.widgets_locators.date_picker_locators import DatePickerLocators
from generator.generator import generated_date


class DatePickerPage(BasePage):
    locators = DatePickerLocators()

    def select_date(self):
        log = self.get_logger()
        date = next(generated_date())
        log.info(f"Generated date data: {date}")
        input_date = self.element_is_visible(
            self.locators.DATE_INPUT)
        value_date_before = input_date.get_attribute("value")
        input_date.click()
        self.select_option_by_text(
            self.locators.DATE_SELECT_MONTH,
            date.month
        )
        self.select_option_by_text(
            self.locators.DATE_SELECT_YEAR,
            date.year
        )
        self.set_date_item_from_list(
            self.locators.DATE_SELECT_DAY_LIST,
            date.day
        )
        value_date_after = input_date.get_attribute("value")
        log.info(f"Returned before, after values: "
                 f"{value_date_before}, {value_date_after}")
        return value_date_before, value_date_after

    def select_date_and_time(self):
        log = self.get_logger()
        date = next(generated_date())
        log.info(f"Generated date data: {date}")
        input_date_time = self.element_is_visible(
            self.locators.DATE_AND_TIME_INPUT)
        value_date_time_before = \
            input_date_time.get_attribute("value")
        input_date_time.click()
        log.info("Opened date time picker")

        self.set_date_item_from_list(
            self.locators.DATE_SELECT_DAY_LIST,
            date.day
        )

        self.element_is_visible(
            self.locators.DATE_AND_TIME_MONTH).click()
        self.set_date_item_from_list(
            self.locators.DATE_AND_TIME_MONTH_LIST,
            date.month
        )

        self.element_is_visible(
            self.locators.DATE_AND_TIME_YEAR).click()
        self.set_date_item_from_list(
            self.locators.DATE_AND_TIME_YEAR_LIST,
            "2020"
        )

        self.set_date_item_from_list(
            self.locators.DATE_AND_TIME_TIME_LIST,
            date.time
        )

        input_date_time_after = self.element_is_visible(
            self.locators.DATE_AND_TIME_INPUT)
        value_date_time_after = \
            input_date_time_after.get_attribute("value")
        log.info(f"Returned before and after values: "
                 f"{value_date_time_before}, "
                 f"{value_date_time_after}")
        return value_date_time_before, value_date_time_after

    def set_date_item_from_list(self, elements, value):
        item_list = self.elements_are_present(elements)
        for item in item_list:
            if item.text == value:
                item.click()
                break
