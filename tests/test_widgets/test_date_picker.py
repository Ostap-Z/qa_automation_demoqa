from pages.widgets_page.date_picker_page import DatePickerPage


class TestDatePicker:

    def test_change_date(self, driver):
        date_picker_page = DatePickerPage(driver, "https://demoqa.com/date-picker")
        date_picker_page.open()
        date_value_before, date_value_after = date_picker_page.select_date()
        assert date_value_before != date_value_after, \
            f"\nActual result:\n\tDate input was not changed." \
            f"\n\tDate value before: {date_value_before}\n\tDate value after: {date_value_after}" \
            f"\nExpected result:\n\tDate input and output should be different. So, the user changed a date."

    def test_change_date_and_time(self, driver):
        date_picker_page = DatePickerPage(driver, "https://demoqa.com/date-picker")
        date_picker_page.open()
        date_time_value_before, date_time_value_after = date_picker_page.select_date_and_time()
        assert date_time_value_before != date_time_value_after, \
            f"\nActual result:\n\tDate or time was not changed." \
            f"\n\tDate time values before: {date_time_value_before}\n\tDate time values after: {date_time_value_after}" \
            f"\nExpected result:\n\tDate should be changed. So, before and after values should be different."

