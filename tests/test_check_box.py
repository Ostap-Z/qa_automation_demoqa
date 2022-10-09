from pages.check_box_page import CheckBoxPage


class TestCheckBox:

    def test_check_box(self, driver):
        check_box_page = CheckBoxPage(driver, "https://demoqa.com/checkbox")
        check_box_page.open()
        check_box_page.open_full_list()
        check_box_page.click_random_check_box()
