from random import sample

import allure

from pages.base_page import BasePage
from locators.interactions_locators.selectable_locators import SelectableLocators


class SelectablePage(BasePage):
    locators = SelectableLocators()

    @allure.step(
        "Chose a random 'Selectable' item "
        "from the presented list"
    )
    def click_selectable_item(self, locators):
        item_list = self.elements_are_visible(locators)
        sample(item_list, k=1)[0].click()

    @allure.step(
        "Check the selectable 'List' items"
    )
    def select_list_item(self):
        log = self.get_logger()

        with allure.step("Open the 'List' tab"):
            self.element_is_visible(
                self.locators.TAB_LIST).click()

        log.info(f"Opened LIST tab")
        self.click_selectable_item(self.locators.LIST_ITEMS)

        with allure.step("Get a text of the "
                         "active 'Selectable' element"):
            active_element = self.element_is_visible(
                self.locators.LIST_ITEM_ACTIVE).text

        log.info(f"Selected list item: {active_element}")
        log.info(f"Length of selected list item: "
                 f"{len(active_element)}")
        return active_element

    @allure.step(
        "Check the selectable 'Grid' items"
    )
    def select_grid_item(self):
        log = self.get_logger()
        self.element_is_visible(self.locators.TAB_GRID).click()
        log.info(f"Opened GRID tab")
        self.click_selectable_item(self.locators.GRID_ITEMS)
        active_element = self.element_is_visible(
            self.locators.GRID_ITEM_ACTIVE).text
        log.info(f"Selected grid item: {active_element}")
        log.info(f"Length of selected grid item: "
                 f"{len(active_element)}")
        return active_element
