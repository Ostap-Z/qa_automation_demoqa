import allure

from pages.alerts_frame_windows_page.browser_windows_page import BrowserWindowsPage


@allure.suite("Alerts, frames and windows suite")
@allure.feature("Browser Windows page")
class TestBrowserWindows:

    @allure.title(
        "Verify that a 'New Tab' opens"
    )
    def test_new_tab(self, driver):
        new_tab_page = BrowserWindowsPage(
            driver,
            "https://demoqa.com/browser-windows"
        )
        new_tab_page.open()
        text_result = new_tab_page.check_opened_new_tab()
        assert text_result == "This is a sample page", \
            f"\nActual result:" \
            f"\n\t{text_result}" \
            "\nExpected result:" \
            "\n\tThis is a sample page"

    @allure.title(
        "Verify that a 'New Window' opens"
    )
    def test_new_window(self, driver):
        new_window_page = BrowserWindowsPage(
            driver,
            "https://demoqa.com/browser-windows"
        )
        new_window_page.open()
        text_result = new_window_page.check_opened_new_window()
        assert text_result == "This is a sample page", \
            f"\nActual result:" \
            f"\n\t{text_result}" \
            "\nExpected result:" \
            "\n\tThis is a sample page"
