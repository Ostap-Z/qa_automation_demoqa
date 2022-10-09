from pages.text_box_page import TextBoxPage


class TestTextBox:

    def test_fill_in_fields(self, driver):
        text_box_page = TextBoxPage(driver, "https://demoqa.com/text-box")
        text_box_page.open()
        input_data = text_box_page.fill_in_form_fields()
        output_data = text_box_page.validate_filled_form()
        assert input_data == output_data, f"\nActual output data: {output_data}\n"\
                                          f"Expected data: {input_data}\n"
