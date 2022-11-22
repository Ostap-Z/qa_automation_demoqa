from pages.base_page import BasePage
from locators.widgets_locators.tabs_locators import TabsLocators


class TabsPage(BasePage):
    locators = TabsLocators()

    def check_tabs(self, tab_name):
        log = self.get_logger()
        tab = {
            "what": {
                "button": self.locators.WHAT_TAB,
                "content": self.locators.WHAT_CONTENT
            },
            "origin": {
                "button": self.locators.ORIGIN_TAB,
                "content": self.locators.ORIGIN_CONTENT
            },
            "use": {
                "button": self.locators.USE_TAB,
                "content": self.locators.USE_CONTENT
            },
            "more": {
                "button": self.locators.MORE_TAB,
                "content": self.locators.MORE_CONTENT
            }
        }
        tab_button = self.element_is_visible(
            tab[tab_name]["button"])
        tab_button.click()
        log.info(f"Opened {tab_button.text} tab")
        tab_content = self.element_is_visible(
            tab[tab_name]["content"]).text
        log.info(f"Got {tab_button.text} content data: {tab_content}")
        log.info(f"Returned data: {tab_button.text}, "
                 f"{len(tab_content)}")
        return tab_button.text, len(tab_content)
