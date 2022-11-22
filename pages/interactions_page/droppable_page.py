import time

from pages.base_page import BasePage
from locators.interactions_locators.droppable_locators import DroppableLocators


class DroppablePage(BasePage):
    locators = DroppableLocators()

    def drop_simple(self):
        log = self.get_logger()
        self.element_is_visible(
            self.locators.SIMPLE_TAB).click()
        log.info("Opened simple droppable page")
        drag_div = self.element_is_visible(
            self.locators.SIMPLE_DRAG_ME)
        drop_div = self.element_is_visible(
            self.locators.SIMPLE_DROP_HERE)
        self.action_drag_and_drop_to_element(
            drag_div,
            drop_div
        )
        log.info(f"Droppable info: source = {drag_div.text}, "
                 f"target = {drop_div.text}")
        log.info(f"Dragged and dropped {drag_div.text} element "
                 f"to the target {drop_div.text}")
        log.info(f"Returned text result: {drop_div.text}")
        return drop_div.text

    def drop_accept(self):
        log = self.get_logger()
        self.element_is_visible(self.locators.ACCEPT_TAB).click()
        log.info("Opened accept droppable page")
        acceptable_div = self.element_is_visible(
            self.locators.ACCEPT_ACCEPTABLE)
        not_acceptable_div = self.element_is_visible(
            self.locators.ACCEPT_NOT_ACCEPTABLE)
        drop_div = self.element_is_visible(
            self.locators.ACCEPT_DROP_HERE)

        self.action_drag_and_drop_to_element(
            not_acceptable_div,
            drop_div
        )
        log.info(f"Droppable not acceptable info: "
                 f"source = {not_acceptable_div.text}, "
                 f"target = {drop_div.text}")
        log.info(f"Dragged and dropped {not_acceptable_div.text} "
                 f"element to the target {drop_div.text}")
        drop_text_not_acceptable = drop_div.text

        self.action_drag_and_drop_to_element(
            acceptable_div,
            drop_div
        )
        log.info(f"Droppable acceptable info: "
                 f"source = {acceptable_div.text}, "
                 f"target = {drop_div.text}")
        log.info(f"Dragged and dropped {acceptable_div.text} "
                 f"element to the target {drop_div.text}")
        drop_text_acceptable = drop_div.text
        log.info(f"Returned text results for not acceptable and acceptable: "
                 f"{not_acceptable_div.text}, {acceptable_div.text}")
        return drop_text_not_acceptable, drop_text_acceptable

    def drop_prevent_propogation(self):
        log = self.get_logger()
        self.element_is_visible(
            self.locators.PREVENT_TAB).click()
        log.info("Opened prevent propogation droppable page")
        drag_div = self.element_is_visible(
            self.locators.PREVENT_DRAG_ME)
        not_greedy_inner_box = self.element_is_visible(
            self.locators.PREVENT_NOT_GREEDY_INNER_BOX)
        greedy_inner_box = self.element_is_visible(
            self.locators.PREVENT_GREEDY_INNER_BOX)

        log.info(f"Droppable not greedy box info: "
                 f"source = {drag_div.text}, "
                 f"target = {not_greedy_inner_box.text}")
        self.action_drag_and_drop_to_element(
            drag_div,
            not_greedy_inner_box
        )
        log.info(f"Dragged and dropped {drag_div.text} element"
                 f" to the target {not_greedy_inner_box.text}")
        text_not_greedy_box = self.element_is_visible(
            self.locators.PREVENT_NOT_GREEDY_DROP_BOX_TEXT).text
        text_not_greedy_inner_box = not_greedy_inner_box.text
        log.info(f"Returned not greedy text for box, inner box:"
                 f" {text_not_greedy_box}, "
                 f"{text_not_greedy_inner_box}")

        log.info(f"Droppable greedy box info: "
                 f"source = {drag_div.text}, "
                 f"target = {greedy_inner_box.text}")
        self.action_drag_and_drop_to_element(
            drag_div,
            greedy_inner_box
        )
        log.info(f"Dragged and dropped {drag_div.text} element "
                 f"to the target {greedy_inner_box.text}")
        text_greedy_box = self.element_is_visible(
            self.locators.PREVENT_GREEDY_DROP_BOX_TEXT).text
        text_greedy_inner_box = greedy_inner_box.text
        log.info(f"Returned greedy text for box, inner box: "
                 f"{text_greedy_box}, "
                 f"{text_greedy_inner_box}")
        return text_not_greedy_box, text_not_greedy_inner_box,\
               text_greedy_box, text_greedy_inner_box

    def drop_revert_draggable(self, drag_type):
        log = self.get_logger()
        drags = {
            'will_revert': {
                'revert': self.locators.REVERT_WILL_REVERT
            },
            'not_will_revert': {
                'revert': self.locators.REVERT_WILL_NOT_REVERT
            }
        }
        self.element_is_visible(
            self.locators.REVERT_TAB).click()
        log.info("Opened revert draggable tab")
        revert = self.element_is_visible(drags[drag_type]["revert"])
        drop_div = self.element_is_visible(
            self.locators.REVERT_DROP_HERE)
        log.info(f"Drag and drop info: {revert.text}, "
                 f"{drop_div.text}")
        self.action_drag_and_drop_to_element(
            revert,
            drop_div
        )
        log.info(f"Dragged and dropped {revert.text} element"
                 f" to the target {drop_div.text}")
        position_after_move = revert.get_attribute("style")
        time.sleep(1)
        position_after_revert = revert.get_attribute("style")
        log.info(f"Returned data: "
                 f"{position_after_move=}, "
                 f"{position_after_revert=}")
        return position_after_move, position_after_revert
