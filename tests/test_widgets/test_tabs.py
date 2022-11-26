import allure
import pytest

from pages.widgets_page.tabs_page import TabsPage


@allure.suite("Widgets suite")
@allure.feature("Tabs page")
class TestTabs:

    @allure.title(
        "Verify that the user has an opportunity "
        "to open different tabs and get "
        "their content: [what_tab, use_tab, origin_tab, more_tab]"
    )
    @pytest.mark.xfail(
        reason="There's a known bug - "
               "The 'More' button tab is not clickable. "
               "So, a user can't open the 'More' tab content"
    )
    def test_tabs(self, driver):
        tabs_page = TabsPage(
            driver,
            "https://demoqa.com/tabs"
        )
        tabs_page.open()
        what_button, what_content = \
            tabs_page.check_tabs("what")
        use_button, use_content = \
            tabs_page.check_tabs("use")
        origin_button, origin_content = \
            tabs_page.check_tabs("origin")
        more_button, more_content = \
            tabs_page.check_tabs("more")

        assert what_button == "What" and what_content > 0, \
            f"\nActual result:" \
            f"\n\tWhat button is not equal to expected " \
            f"or what content is empty." \
            f"\n\tWhat button: {what_button}" \
            f"\n\tWhat content: {what_content}" \
            f"\nExpected result:" \
            f"\n\tWhat button should be 'What' " \
            f"and what content length should be more than 0"

        assert use_button == "Use" and use_content > 0, \
            f"\nActual result:" \
            f"\n\tUse button is not equal to expected " \
            f"or use content is empty." \
            f"\n\tUse button: {use_button}" \
            f"\n\tUse content: {use_content}" \
            f"\nExpected result:" \
            f"\n\tUse button should be 'Use' " \
            f"and use content length should be more than 0"

        assert origin_button == "Origin" and origin_content > 0, \
            f"\nActual result:" \
            f"\n\tOrigin button is not equal to expected " \
            f"or origin content is empty." \
            f"\n\tOrigin button: {origin_button}" \
            f"\n\tOrigin content: {origin_content}" \
            f"\nExpected result:" \
            f"\n\tOrigin button should be 'Origin' " \
            f"and origin content length should be more than 0"

        assert more_button == "More" and more_content > 0, \
            f"\nActual result:" \
            f"\n\tMore button is not equal to expected " \
            f"or more content is empty." \
            f"\n\tMore button: {more_button}" \
            f"\n\tMore content: {more_content}" \
            f"\nExpected result:" \
            f"\n\tMore button should be 'More' " \
            f"and more content length should be more than 0"
