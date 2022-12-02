import allure
import pytest

from pages.widgets_page.tabs_page import TabsPage


@allure.suite("Widgets suite")
@allure.feature("Tabs page")
class TestTabs:

    @allure.title(
        "Verify that the user has an opportunity "
        "to open and get a correct 'What' tab title"
    )
    def test_what_title_tab(self, driver):
        tabs_page = TabsPage(
            driver,
            "https://demoqa.com/tabs"
        )
        tabs_page.open()
        what_tab_title = tabs_page.check_tabs("what")[0]
        assert what_tab_title == "What", \
            "\nActual result:" \
            "\n\tThe 'What' tab title is not equal to the expected " \
            f"\n\tActual 'What' tab title: {what_tab_title}" \
            "\nExpected result:" \
            "\n\tThe 'What' tab title should be 'What'"

    @allure.title(
        "Verify that the user has an opportunity "
        "to get a 'What' tab content"
    )
    def test_what_content_tab(self, driver):
        tabs_page = TabsPage(
            driver,
            "https://demoqa.com/tabs"
        )
        tabs_page.open()
        what_tab_content = tabs_page.check_tabs("what")[1]
        assert what_tab_content > 0, \
            "\nActual result:" \
            "\n\tThe 'What' tab content is empty on the page" \
            f"\n\tActual 'What' tab content len: {what_tab_content}" \
            "\nExpected result:" \
            "\n\tThe 'What' tab content len should be > 0"

    @allure.title(
        "Verify that the user has an opportunity "
        "to open and get a correct 'Origin' tab title"
    )
    def test_origin_title_tab(self, driver):
        tabs_page = TabsPage(
            driver,
            "https://demoqa.com/tabs"
        )
        tabs_page.open()
        origin_tab_title = tabs_page.check_tabs("origin")[0]
        assert origin_tab_title == "Origin", \
            "\nActual result:" \
            "\n\tThe 'Origin' tab title is not equal to the expected " \
            f"\n\tActual 'Origin' tab title: {origin_tab_title}" \
            "\nExpected result:" \
            "\n\tThe 'Origin' tab title should be 'Origin'"

    @allure.title(
        "Verify that the user has an opportunity "
        "to get a 'Origin' tab content"
    )
    def test_origin_content_tab(self, driver):
        tabs_page = TabsPage(
            driver,
            "https://demoqa.com/tabs"
        )
        tabs_page.open()
        origin_tab_content = tabs_page.check_tabs("origin")[1]
        assert origin_tab_content > 0, \
            "\nActual result:" \
            "\n\tThe 'Origin' tab content is empty on the page" \
            f"\n\tActual 'Origin' tab content len: {origin_tab_content}" \
            "\nExpected result:" \
            "\n\tThe 'Origin' tab content len should be > 0"

    @allure.title(
        "Verify that the user has an opportunity "
        "to open and get a correct 'Use' tab title"
    )
    def test_use_title_tab(self, driver):
        tabs_page = TabsPage(
            driver,
            "https://demoqa.com/tabs"
        )
        tabs_page.open()
        use_tab_title = tabs_page.check_tabs("use")[0]
        assert use_tab_title == "Use", \
            "\nActual result:" \
            "\n\tThe 'Use' tab title is not equal to the expected " \
            f"\n\tActual 'Use' tab title: {use_tab_title}" \
            "\nExpected result:" \
            "\n\tThe 'Use' tab title should be 'Use'"

    @allure.title(
        "Verify that the user has an opportunity "
        "to get a 'Use' tab content"
    )
    def test_use_content_tab(self, driver):
        tabs_page = TabsPage(
            driver,
            "https://demoqa.com/tabs"
        )
        tabs_page.open()
        use_tab_content = tabs_page.check_tabs("use")[1]
        assert use_tab_content > 0, \
            "\nActual result:" \
            "\n\tThe 'Use' tab content is empty on the page" \
            f"\n\tActual 'Use' tab content len: {use_tab_content}" \
            "\nExpected result:" \
            "\n\tThe 'Use' tab content len should be > 0"

    @allure.title(
        "Verify that the user has an opportunity "
        "to open and get a correct 'More' tab title"
    )
    @pytest.mark.xfail(
        reason="There's a known bug - "
               "The 'More' button tab is not clickable. "
               "So, a user can't open the 'More' tab content"
    )
    def test_more_title_tab(self, driver):
        tabs_page = TabsPage(
            driver,
            "https://demoqa.com/tabs"
        )
        tabs_page.open()
        more_tab_title = tabs_page.check_tabs("more")[0]
        assert more_tab_title == "More", \
            "\nActual result:" \
            "\n\tThe 'More' tab title is not equal to the expected " \
            f"\n\tActual 'More' tab title: {more_tab_title}" \
            "\nExpected result:" \
            "\n\tThe 'More' tab title should be 'More'"
