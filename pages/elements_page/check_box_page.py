from random import randint

from pages.base_page import BasePage
from locators.check_box_locators import CheckBoxPageLocators


class CheckBoxPage(BasePage):
    locators = CheckBoxPageLocators()

    def open_full_list(self):
        log = self.get_logger()
        self.element_is_visible(self.locators.EXPAND_ALL_BUTTON).click()
        log.info("Opened full list of checkboxes")

    def click_random_check_box(self):
        log = self.get_logger()
        item_list = self.elements_are_visible(self.locators.CHECK_BOXES_ITEM_LIST)

        log.info(f"I'm gonna click 10 times on the random items")
        count = 10
        while count != 0:
            item = item_list[randint(1, 5)]
            if count > 0:
                self.go_to_element(item)
                item.click()
                log.info(f"Clicked on the item: {item.text}")
                count -= 1
            else:
                break

    def get_checked_checkboxes(self):
        log = self.get_logger()
        checked_list = self.elements_are_present(self.locators.CHECKED_ITEMS_LIST)
        data = []
        for box in checked_list:
            title_item = box.find_element(*self.locators.TITLE_ITEM)
            data.append(title_item.text)
        log.info(f"List of checked checkboxes: {data}")
        return str(data).replace(' ', '').replace('.doc', '').lower()

    def get_output_result(self):
        log = self.get_logger()
        result_list = self.elements_are_present(self.locators.OUTPUT_RESULT)
        data = [item.text for item in result_list]
        log.info(f"List of checked checkboxes in the result output: {data}")
        return str(data).replace(" ", "").lower()
