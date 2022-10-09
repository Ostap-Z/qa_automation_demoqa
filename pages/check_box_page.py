from random import randint

from pages.base_page import BasePage
from locators.check_box_locators import CheckBoxPageLocators


class CheckBoxPage(BasePage):
    locators = CheckBoxPageLocators()

    def open_full_list(self):
        self.element_is_visible(self.locators.EXPAND_ALL_BUTTON).click()

    def click_random_check_box(self):
        item_list = self.elements_are_visible(self.locators.CHECK_BOXES_ITEM_LIST)

        count = 10
        while count != 0:
            item = item_list[randint(1, 5)]
            if count > 0:
                self.go_to_element(item)
                item.click()
                print(item.text)
                count -= 1
            else:
                break
