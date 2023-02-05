import allure

from pages.base_page import BasePage
from locators.alerts_frame_windows_locators.browser_windows_locators \
    import BrowserWindowsLocators


class BrowserWindowsPage(BasePage):
    locators = BrowserWindowsLocators()

    @allure.step(
        "Check the 'Opened New Tab'"
    )
    def check_opened_new_tab(self):
        log = self.get_logger()

        with allure.step("Click on the 'New Tab' button"):
            self.element_is_visible(self.locators.NEW_TAB_BUTTON)\
                .click()
        log.info("Clicked on the new tab button")

        with allure.step("Switch to the 'New Tab'"):
            self.go_to_new_window(1)
        log.info("Switched to the new tab")

        with allure.step("Get tab text result"):
            text_title = self.element_is_present(
                self.locators.TITLE_NEW).text
        log.info(f"Text presented in the new tab: {text_title}")
        return text_title

    @allure.step(
        "Check the 'Opened New Window'"
    )
    def check_opened_new_window(self):
        log = self.get_logger()

        with allure.step("Click on the 'New Window' button"):
            self.element_is_visible(self.locators.NEW_WINDOW_BUTTON)\
                .click()
        log.info("Clicked on the new window button")

        with allure.step("Switch to the 'New Window'"):
            self.go_to_new_window(1)
        log.info("Switched to the new window")

        with allure.step("Get tab text result"):
            text_title = self.element_is_present(
                self.locators.TITLE_NEW).text
        log.info(f"Text presented in the new window: {text_title}")
        return text_title
