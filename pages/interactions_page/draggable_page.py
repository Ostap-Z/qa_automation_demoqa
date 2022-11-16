from random import randint

from pages.base_page import BasePage
from locators.interactions_locators.draggable_locators import DraggableLocators


class DraggablePage(BasePage):
    locators = DraggableLocators()

    def get_before_after_positions(self, drag_element):
        self.action_drag_and_drop_by_offset(drag_element, randint(0, 50), randint(0, 50))
        before_position = drag_element.get_attribute("style")
        self.action_drag_and_drop_by_offset(drag_element, randint(0, 50), randint(0, 50))
        after_position = drag_element.get_attribute("style")
        return before_position, after_position

    def simple_drag_box(self):
        self.element_is_visible(self.locators.SIMPLE_TAB).click()
        drag_div = self.element_is_visible(self.locators.SIMPLE_DRAG_ME)
        before_position, after_position = self.get_before_after_positions(drag_div)
        return before_position, after_position
