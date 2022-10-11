from pages.web_table_page import WebTablePage


class TestWebTable:

    def test_web_table_add_person(self, driver):
        web_table_page = WebTablePage(driver, "https://demoqa.com/webtables")
        web_table_page.open()
        web_table_page.add_new_person()
