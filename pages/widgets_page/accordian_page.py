import allure
from selenium.common import TimeoutException, ElementClickInterceptedException

from pages.base_page import BasePage
from locators.widgets_locators.accordian_locators import AccordianLocators


class AccordianPage(BasePage):
    locators = AccordianLocators()

    @allure.step(
        "Check the 'Accordian'"
    )
    def check_accordian(self, accordian_num):
        log = self.get_logger()
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
        with allure.step("Remove ads"):
            self.hide_ads()

        with allure.step(f"Open the tab"):
            accordian_title = self.element_is_visible(
                accordian[accordian_num]['title'])
            accordian_title.click()

        log.info("Opened accordian title section")
        try:
            with allure.step("Get the 'Accordian' content"):
                accordian_content = self.element_is_visible(
                    accordian[accordian_num]['content']).text

            log.info(f"Get accordian content: {accordian_content}")
        except TimeoutException:
            accordian_title.click()
            log.info("Opened accordian title section")
            accordian_content = self.element_is_visible(
                accordian[accordian_num]['content']).text
            log.info(f"Get accordian content: {accordian_content}")
            accordian_title.click()
            log.info("Closed accordian title section")
        except ElementClickInterceptedException:
            with allure.step("Remove ads"):
                self.hide_ads()
                self.hide_image_ads()

            self.element_is_visible(accordian_title)
            log.info("Accordian title is visible on the page")
            accordian_title.click()
            log.info("Opened accordian title section")
            accordian_content = self.element_is_visible(
                accordian[accordian_num]['content']).text
            log.info(f"Get accordian content: {accordian_content}")
            accordian_title.click()
            log.info("Closed accordian title section")
        log.info(f"Returned title, content: {accordian_title.text}"
                 f"\n{accordian_content}")

        with allure.step("Return accordian title, accordian content: "
                         f"{accordian_title.text}, "
                         f"{accordian_content}"):

            return [accordian_title.text, accordian_content]
