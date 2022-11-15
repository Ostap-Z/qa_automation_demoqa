from pages.base_page import BasePage
from locators.interactions_locators.droppable_locators import DroppableLocators


class DroppablePage(BasePage):
    locators = DroppableLocators()

    def drop_simple(self):
        self.element_is_visible(self.locators.SIMPLE_TAB).click()
        drag_div = self.element_is_visible(self.locators.SIMPLE_DRAG_ME)
        drop_div = self.element_is_visible(self.locators.SIMPLE_DROP_HERE)
        self.action_drag_and_drop_to_element(drag_div, drop_div)
        return drop_div.text

    def drop_accept(self):
        self.element_is_visible(self.locators.ACCEPT_TAB).click()
        acceptable_div = self.element_is_visible(self.locators.ACCEPT_ACCEPTABLE)
        not_acceptable_div = self.element_is_visible(self.locators.ACCEPT_NOT_ACCEPTABLE)
        drop_div = self.element_is_visible(self.locators.ACCEPT_DROP_HERE)
        self.action_drag_and_drop_to_element(not_acceptable_div, drop_div)
        drop_text_not_acceptable = drop_div.text
        self.action_drag_and_drop_to_element(acceptable_div, drop_div)
        drop_text_acceptable = drop_div.text
        return drop_text_not_acceptable, drop_text_acceptable
