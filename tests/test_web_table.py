import time

from pages.web_table_page import WebTablePage


class TestWebTable:

    def test_web_table_add_person(self, driver):
        web_table_page = WebTablePage(driver, "https://demoqa.com/webtables")
        web_table_page.open()
        new_person = web_table_page.add_new_person()
        table_result = web_table_page.check_new_added_person()
        print(f"New person: {new_person}")
        print(f"Table: {table_result}")
        assert new_person in table_result, f"\nActual result: {new_person} not in the {table_result}"\
                                           f"\nExpected result: {new_person} should be in the {table_result}"
