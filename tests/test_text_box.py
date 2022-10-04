from pages.text_box_page import TextBoxPage


class TestTextBox:

    def test_fill_in_fields(self, driver):
        text_box_page = TextBoxPage(driver, "https://demoqa.com/text-box")
        text_box_page.open()
        text_box_page.fill_in_form_fields()
        output_name, output_email, output_current_addr, output_pernament_addr = text_box_page.validate_filled_form()
        print(output_name)
        print(output_email)
        print(output_current_addr)
        print(output_pernament_addr)
