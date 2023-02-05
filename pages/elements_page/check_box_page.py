from random import randint

import allure

from pages.base_page import BasePage
from locators.elements_locators.check_box_locators import CheckBoxPageLocators


class CheckBoxPage(BasePage):
    locators = CheckBoxPageLocators()

    @allure.step(
        "Open a full list of checkboxes"
    )
    def open_full_list(self):
        log = self.get_logger()
        self.element_is_visible(
            self.locators.EXPAND_ALL_BUTTON).click()
        log.info("Opened full list of checkboxes")

    @allure.step(
        "Click on the random check boxes"
    )
    def click_random_check_box(self):
        log = self.get_logger()
        item_list = self.elements_are_visible(
            self.locators.CHECK_BOXES_ITEM_LIST)

        log.info("I'm gonna click 10 times on the random items")
        count = 10
        while count != 0:
            item = item_list[randint(1, 5)]
            with allure.step(f"Find and click on the element: {item.text}"):
                if count > 0:
                    self.go_to_element(item)
                    item.click()
                    log.info(f"Clicked on the item: {item.text}")
                    count -= 1
                else:
                    break

    @allure.step(
        "Get a list of checked check boxes"
    )
    def get_checked_checkboxes(self):
        log = self.get_logger()
        checked_list = self.elements_are_present(
            self.locators.CHECKED_ITEMS_LIST)
        data = []
        for box in checked_list:
            title_item = box.find_element(*self.locators.TITLE_ITEM)
            data.append(title_item.text)
        log.info(f"List of checked checkboxes: {data}")
        return str(data).replace(' ', '').replace('.doc', '').lower()

    @allure.step(
        "Get an output results"
    )
    def get_output_result(self):
        log = self.get_logger()
        result_list = self.elements_are_present(
            self.locators.OUTPUT_RESULT)
        data = [item.text for item in result_list]
        log.info(f"List of checked checkboxes in the result output: "
                 f"{data}")
        return str(data).replace(" ", "").lower()
