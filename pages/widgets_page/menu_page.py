from pages.base_page import BasePage
from locators.widgets_locators.menu_locators import MenuLocators


class MenuPage(BasePage):
    locators = MenuLocators()

    def check_menu(self):
        log = self.get_logger()
        menu_item_list = self.elements_are_present(
            self.locators.MENU_ITEMS_LIST)
        data = []
        for item in menu_item_list:
            self.action_move_to_element(item)
            data.append(item.text)
            log.info(f"Collected item: {item.text}")
        log.info(f"Returned data: {data}")
        return data
