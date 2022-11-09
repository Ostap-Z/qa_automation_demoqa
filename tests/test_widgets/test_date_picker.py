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
