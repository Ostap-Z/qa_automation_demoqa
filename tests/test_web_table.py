from random import randint

import pytest

from pages.web_table_page import WebTablePage


class TestWebTable:

    def test_web_table_add_person(self, driver):
        web_table_page = WebTablePage(driver, "https://demoqa.com/webtables")
        web_table_page.open()
        new_person = web_table_page.add_new_person()
        table_result = web_table_page.check_new_added_person()
        assert new_person in table_result, f"\nActual result: {new_person} not in the {table_result}" \
                                           f"\nExpected result: {new_person} should be in the {table_result}"

    def test_web_table_search_person(self, driver):
        web_table_page = WebTablePage(driver, "https://demoqa.com/webtables")
        web_table_page.open()
        key_word = web_table_page.add_new_person()[randint(0, 5)]
        web_table_page.search_person(key_word)
        table_result = web_table_page.check_search_person()
        assert key_word in table_result, f"\nActual result: {key_word} not in the table {table_result}" \
                                         f"\nExpected result: {key_word} should be in the table {table_result}"

    def test_web_table_edit_person(self, driver):
        web_table_page = WebTablePage(driver, "https://demoqa.com/webtables")
        web_table_page.open()
        last_name = web_table_page.add_new_person()[1]
        web_table_page.search_person(last_name)
        age = web_table_page.update_person_info()
        row = web_table_page.check_search_person()
        assert age in row, f"Actual result: {age} is not present in the {row}" \
                           f"Expected result: {age} should be present in the {row}"

    def test_web_table_delete_person(self, driver):
        web_table_page = WebTablePage(driver, "https://demoqa.com/webtables")
        web_table_page.open()
        email = web_table_page.add_new_person()[3]
        web_table_page.search_person(email)
        web_table_page.delete_person()
        deleted_text = web_table_page.check_deleted_person()
        assert deleted_text == "No rows found"

    @pytest.mark.xfail(reason="Expected failed due to there is a bug - the user can't see count_rows dropdown when more than 25 rows are opened")
    def test_web_table_change_row_count(self, driver):
        web_table_page = WebTablePage(driver, "https://demoqa.com/webtables")
        web_table_page.open()
        count = web_table_page.select_up_to_rows()
        assert count == [5, 10, 20, 25, 50, 100], \
            "The number of rows in the table hasn't benn changed or changed incorrect "
