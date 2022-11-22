from random import sample

from pages.base_page import BasePage
from locators.interactions_locators.sortable_locators import SortableLocators


class SortablePage(BasePage):
    locators = SortableLocators()

    def get_sortable_items(self, elements):
        item_list = self.elements_are_visible(elements)
        return [item.text for item in item_list]

    def change_item_order(self, item_type):
        log = self.get_logger()
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
        tab = self.element_is_visible(item[item_type]['tab'])
        tab.click()
        log.info(f"Opened tab: {tab.text}")
        order_before = self.get_sortable_items(
            item[item_type]['items']
        )
        item_list = sample(self.elements_are_visible(
            item[item_type]['items']), k=2
        )
        chosen_draggable_item = item_list[0]
        drag_to_position = item_list[1]
        self.action_drag_and_drop_to_element(
            chosen_draggable_item,
            drag_to_position
        )
        log.info(f"{chosen_draggable_item.text} changed position"
                 f" with {drag_to_position.text}")
        order_after = self.get_sortable_items(
            item[item_type]['items']
        )
        log.info(f"Returned before, after order: "
                 f"{order_before}, {order_after}")
        return order_before, order_after
