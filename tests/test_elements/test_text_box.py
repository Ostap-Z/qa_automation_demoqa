import allure
import pytest

from pages.elements_page.text_box_page import TextBoxPage


@allure.suite("Elements suite")
@allure.feature("Text Box page")
class TestTextBox:

    @allure.title("Check the form")
    @pytest.mark.xfail(
        reason="Expected failed due to "
               "returns empty strings instead of "
               "current and permanent addresses"
    )
    def test_fill_in_fields(self, driver):
        text_box_page = TextBoxPage(
            driver,
            "https://demoqa.com/text-box"
        )
        text_box_page.open()
        input_data = text_box_page.fill_in_form_fields()
        output_data = text_box_page.validate_filled_form()
        assert input_data == output_data, \
            f"\nActual result: {output_data}\n"\
            f"\nExpected result: {input_data}\n"
