from pages.elements_page import TextBoxPage


class TestTextBox:

    def test_fill_in_fields(self, driver):
        text_box_page = TextBoxPage(driver, "https://demoqa.com/text-box")
        text_box_page.open()
        text_box_page.fill_in_form_fields()
        print(text_box_page.validate_filled_form())
