from pages.base_page import BasePage
from locators.alerts_frame_windows_locators.browser_windows_locators import BrowserWindowsLocators


class BrowserWindowsPage(BasePage):
    locators = BrowserWindowsLocators()

    def check_opened_new_tab(self):
        log = self.get_logger()
        self.element_is_visible(self.locators.NEW_TAB_BUTTON).click()
        log.info("Clicked on the new tab button")
        self.go_to_new_window(1)
        log.info("Switched to the new tab")
        text_title = self.element_is_present(self.locators.TITLE_NEW).text
        log.info(f"Text presented in the new tab: {text_title}")
        return text_title

    def check_opened_new_window(self):
        log = self.get_logger()
        self.element_is_visible(self.locators.NEW_WINDOW_BUTTON).click()
        log.info("Clicked on the new window button")
        self.go_to_new_window(1)
        log.info("Switched to the new window")
        text_title = self.element_is_present(self.locators.TITLE_NEW).text
        log.info(f"Text presented in the new window: {text_title}")
        return text_title
