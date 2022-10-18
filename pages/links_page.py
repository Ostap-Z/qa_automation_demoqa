import requests

from pages.base_page import BasePage
from locators.links_locators import LinksPageLocators


class LinksPage(BasePage):
    locators = LinksPageLocators()

    def check_new_tab_simple_link(self):
        simple_link = self.element_is_visible(self.locators.SIMPLE_LINK)
        link_href = simple_link.get_attribute("href")
        request = requests.get(link_href)

        if request.status_code == 200:
            simple_link.click()
            self.driver.switch_to.window(self.driver.window_handles[1])
            url = self.driver.current_url
            return link_href, url

        else:
            return link_href, request.status_code

    def check_broken_link(self, url):
        request = requests.get(url)

        if request.status_code == 200:
            self.element_is_present(self.locators.BAD_REQUEST_LINK).click()
        else:
            return request.status_code