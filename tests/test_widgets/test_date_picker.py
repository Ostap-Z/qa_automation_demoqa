import allure

from pages.widgets_page.date_picker_page import DatePickerPage


@allure.suite("Widgets suite")
@allure.feature("Date Picker page")
class TestDatePicker:

    @allure.title(
        "Verify that the user has an opportunity "
        "to change a date"
    )
    def test_change_date(self, driver):
        date_picker_page = DatePickerPage(
            driver,
            "https://demoqa.com/date-picker"
        )
        date_picker_page.open()
        date_value_before, date_value_after = date_picker_page.select_date()

        assert date_value_before != date_value_after, \
            f"\nActual result:" \
            f"\n\tDate input was not changed." \
            f"\n\tDate value before: {date_value_before}" \
            f"\n\tDate value after: {date_value_after}" \
            f"\nExpected result:" \
            f"\n\tDate input and output should be different. " \
            f"\n\tSo, the user changed a date."

    @allure.title(
        "Verify that the user has an opportunity "
        "to change the date and time"
    )
    def test_change_date_and_time(self, driver):
        date_picker_page = DatePickerPage(
            driver,
            "https://demoqa.com/date-picker"
        )
        date_picker_page.open()
        date_time_value_before, date_time_value_after = \
            date_picker_page.select_date_and_time()
        assert date_time_value_before != date_time_value_after, \
            f"\nActual result:" \
            f"\n\tDate or time was not changed." \
            f"\n\tDate time values before: {date_time_value_before}" \
            f"\n\tDate time values after: {date_time_value_after}" \
            f"\nExpected result:" \
            f"\n\tDate should be changed." \
            f"\n\tSo, before and after values should be different."
