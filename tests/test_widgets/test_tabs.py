from pages.widgets_page.tabs_page import TabsPage


class TestTabs:

    def test_tabs(self, driver):
        tabs_page = TabsPage(driver, "https://demoqa.com/tabs")
        tabs_page.open()
        what_button, what_content = tabs_page.check_tabs("what")
        use_button, use_content = tabs_page.check_tabs("use")
        origin_button, origin_content = tabs_page.check_tabs("origin")
        more_button, more_content = tabs_page.check_tabs("more")
        assert what_button == "What" and what_content > 0, \
            f"\nActual result:\n\tWhat button is not equal to expected or what content is empty." \
            f"\n\tWhat button: {what_button}\n\tWhat content: {what_content}" \
            f"\nExpected result:\n\tWhat button should be 'What' and what content length should be more than 0"

        assert use_button == "Use" and use_content > 0, \
            f"\nActual result:\n\tUse button is not equal to expected or use content is empty." \
            f"\n\tUse button: {use_button}\n\tUse content: {use_content}" \
            f"\nExpected result:\n\tUse button should be 'Use' and use content length should be more than 0"

        assert origin_button == "Origin" and origin_content > 0, \
            f"\nActual result:\n\tOrigin button is not equal to expected or origin content is empty." \
            f"\n\tOrigin button: {origin_button}\n\tOrigin content: {origin_content}" \
            f"\nExpected result:\n\tOrigin button should be 'Origin' and origin content length should be more than 0"

        assert more_button == "More" and more_content > 0, \
            f"\nActual result:\n\tMore button is not equal to expected or more content is empty." \
            f"\n\tMore button: {more_button}\n\tMore content: {more_content}" \
            f"\nExpected result:\n\tMore button should be 'More' and more content length should be more than 0"
