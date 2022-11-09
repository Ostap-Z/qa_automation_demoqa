from pages.base_page import BasePage
from locators.widgets_locators.menu_locators import MenuLocators


class MenuPage(BasePage):
    locators = MenuLocators()

    def check_menu(self):
        menu_item_list = self.elements_are_present(self.locators.MENU_ITEMS_LIST)
        data = []
        for item in menu_item_list:
            self.action_move_to_element(item)
            data.append(item.text)
        return data
