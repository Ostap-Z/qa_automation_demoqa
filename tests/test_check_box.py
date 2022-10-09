from pages.check_box_page import CheckBoxPage


class TestCheckBox:

    def test_check_box(self, driver):
        check_box_page = CheckBoxPage(driver, "https://demoqa.com/checkbox")
        check_box_page.open()
