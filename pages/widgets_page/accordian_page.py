from selenium.common import TimeoutException, ElementClickInterceptedException

from pages.base_page import BasePage
from locators.widgets_locators.accordian_locators import AccordianLocators


class AccordianPage(BasePage):
    locators = AccordianLocators()

    def check_accordian(self, accordian_num):
        accordian = {
            'first': {
                'title': self.locators.FIRST_HEADING,
                'content': self.locators.FIRST_CONTENT
            },
            'second': {
                'title': self.locators.SECOND_HEADING,
                'content': self.locators.SECOND_CONTENT
            },
            'third': {
                'title': self.locators.THIRD_HEADING,
                'content': self.locators.THIRD_CONTENT
            }
        }
        self.hide_ads()
        accordian_title = self.element_is_visible(accordian[accordian_num]['title'])
        accordian_title.click()
        try:
            accordian_content = self.element_is_visible(accordian[accordian_num]['content']).text
        except TimeoutException:
            accordian_title.click()
            accordian_content = self.element_is_visible(accordian[accordian_num]['content']).text
            accordian_title.click()
        except ElementClickInterceptedException:
            self.hide_ads()
            self.hide_image_ads()
            self.element_is_visible(accordian_title)
            accordian_title.click()
            accordian_content = self.element_is_visible(accordian[accordian_num]['content']).text
            accordian_title.click()
        return [accordian_title.text, accordian_content]
