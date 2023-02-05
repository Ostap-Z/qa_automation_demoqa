import allure

from pages.base_page import BasePage
from locators.widgets_locators.date_picker_locators import DatePickerLocators
from generator.generator import generated_date


class DatePickerPage(BasePage):
    locators = DatePickerLocators()

    @allure.step(
        "Select a date"
    )
    def select_date(self):
        log = self.get_logger()

        with allure.step("Generate a date"):
            date = next(generated_date())

        log.info(f"Generated date data: {date}")

        input_date = self.element_is_visible(
            self.locators.DATE_INPUT)

        with allure.step("Get the date before changes"):
            value_date_before = input_date.get_attribute("value")

        with allure.step("Open the date section"):
            input_date.click()

        with allure.step(f"Select a {date.month} month"):
            self.select_option_by_text(
                self.locators.DATE_SELECT_MONTH,
                date.month
            )

        with allure.step(f"Select a {date.year} year"):
            self.select_option_by_text(
                self.locators.DATE_SELECT_YEAR,
                date.year
            )

        with allure.step(f"Select a {date.day} day"):
            self.set_date_item_from_list(
                self.locators.DATE_SELECT_DAY_LIST,
                date.day
            )

        with allure.step("Get the date after changes"):
            value_date_after = input_date.get_attribute("value")

        log.info(f"Returned before, after values: "
                 f"{value_date_before}, {value_date_after}")
        return value_date_before, value_date_after

    @allure.step(
        "Select a date and time"
    )
    def select_date_and_time(self):
        log = self.get_logger()

        with allure.step("Generate a date"):
            date = next(generated_date())

        log.info(f"Generated date data: {date}")
        input_date_time = self.element_is_visible(
            self.locators.DATE_AND_TIME_INPUT)

        with allure.step("Get the date and time before changes"):
            value_date_time_before = \
                input_date_time.get_attribute("value")

        with allure.step("Open the date and time section"):
            input_date_time.click()

        log.info("Opened date time picker")

        with allure.step(f"Select a {date.day} day"):
            self.set_date_item_from_list(
                self.locators.DATE_SELECT_DAY_LIST,
                date.day
            )

        with allure.step("Open the month section"):
            self.element_is_visible(
                self.locators.DATE_AND_TIME_MONTH).click()

        with allure.step(f"Select a {date.month} month"):
            self.set_date_item_from_list(
                self.locators.DATE_AND_TIME_MONTH_LIST,
                date.month
            )

        with allure.step("Open the year section"):
            self.element_is_visible(
                self.locators.DATE_AND_TIME_YEAR).click()

        with allure.step(f"Select a {date.year} year"):
            self.set_date_item_from_list(
                self.locators.DATE_AND_TIME_YEAR_LIST,
                "2020"
            )

        with allure.step(f"Select a {date.time} time"):
            self.set_date_item_from_list(
                self.locators.DATE_AND_TIME_TIME_LIST,
                date.time
            )

        input_date_time_after = self.element_is_visible(
            self.locators.DATE_AND_TIME_INPUT)

        with allure.step("Get the date and time after changes"):
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
