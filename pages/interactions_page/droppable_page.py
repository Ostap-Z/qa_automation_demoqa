from pages.base_page import BasePage
from locators.interactions_locators.droppable_locators import DroppableLocators


class DroppablePage(BasePage):
    locators = DroppableLocators()

    def drop_simple(self):
        log = self.get_logger()
        self.element_is_visible(self.locators.SIMPLE_TAB).click()
        log.info("Opened simple tab page")
        drag_div = self.element_is_visible(self.locators.SIMPLE_DRAG_ME)
        drop_div = self.element_is_visible(self.locators.SIMPLE_DROP_HERE)
        self.action_drag_and_drop_to_element(drag_div, drop_div)
        log.info(f"Droppable info: source = {drag_div.text}, target = {drop_div.text}")
        log.info(f"Dragged and dropped {drag_div.text} element to the target {drop_div.text}")
        log.info(f"Returned text result: {drop_div.text}")
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
