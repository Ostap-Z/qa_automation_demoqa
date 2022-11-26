import allure

from pages.base_page import BasePage
from locators.widgets_locators.menu_locators import MenuLocators


class MenuPage(BasePage):
    locators = MenuLocators()

    @allure.step(
        "Check the menu"
    )
    def check_menu(self):
        log = self.get_logger()

        with allure.step("Check if menu items are presented "
                         "on the page"):
            menu_item_list = self.elements_are_present(
                self.locators.MENU_ITEMS_LIST)

        with allure.step("Append menu items to the list"):
            data = []
            for item in menu_item_list:
                with allure.step("Hover over element "
                                 "to collect menu items"):
                    self.action_move_to_element(item)

                with allure.step(f"Append menu item '{item.text}' to the list"):
                    data.append(item.text)
                log.info(f"Collected item: {item.text}")

        log.info(f"Returned data: {data}")
        return data
