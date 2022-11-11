from random import sample

from pages.base_page import BasePage
from locators.interactions_locators.sortable_locators import SortableLocators


class SortablePage(BasePage):
    locators = SortableLocators()

    def get_sortable_items(self, elements):
        item_list = self.elements_are_visible(elements)
        return [item.text for item in item_list]

    def change_item_order(self, item_type):
        item = {
            'list': {
                'tab': self.locators.TAB_LIST,
                'items': self.locators.LIST_ITEMS
            },
            'grid': {
                'tab': self.locators.TAB_GRID,
                'items': self.locators.GRID_ITEMS
            }
        }
        self.element_is_visible(item[item_type]['tab']).click()
        order_before = self.get_sortable_items(item[item_type]['items'])
        item_list = sample(self.elements_are_visible(item[item_type]['items']), k=2)
        chosen_draggable_item = item_list[0]
        drag_to_position = item_list[1]
        self.action_drag_and_drop_to_element(chosen_draggable_item, drag_to_position)
        order_after = self.get_sortable_items(item[item_type]['items'])
        return order_before, order_after
