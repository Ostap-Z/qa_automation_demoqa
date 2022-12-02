import time

import allure

from pages.base_page import BasePage
from locators.interactions_locators.droppable_locators import DroppableLocators


class DroppablePage(BasePage):
    locators = DroppableLocators()

    @allure.step(
        "Check the 'Simple' drop"
    )
    def drop_simple(self):
        log = self.get_logger()

        with allure.step("Open the 'Simple' tab"):
            self.element_is_visible(
                self.locators.SIMPLE_TAB).click()
        log.info("Opened simple droppable page")

        drag_div = self.element_is_visible(
            self.locators.SIMPLE_DRAG_ME)
        drop_div = self.element_is_visible(
            self.locators.SIMPLE_DROP_HERE)

        with allure.step(f"Drag {drag_div.text} "
                         f"and drop to {drop_div.text} element"):
            self.action_drag_and_drop_to_element(
                drag_div,
                drop_div
            )

        log.info(f"Droppable info: source = {drag_div.text}, "
                 f"target = {drop_div.text}")
        log.info(f"Dragged and dropped {drag_div.text} element "
                 f"to the target {drop_div.text}")

        with allure.step("Get the 'Simple Drop' text"):
            drop_text = drop_div.text

        log.info(f"Returned text result: {drop_div.text}")
        return drop_text

    @allure.step(
        "Check the 'Accept' drop"
    )
    def drop_accept(self, draggable_type):
        log = self.get_logger()

        with allure.step("Open the 'Accept' tab"):
            self.element_is_visible(self.locators.ACCEPT_TAB).click()
        log.info("Opened accept droppable page")

        acceptable_div = self.element_is_visible(
            self.locators.ACCEPT_ACCEPTABLE)

        not_acceptable_div = self.element_is_visible(
            self.locators.ACCEPT_NOT_ACCEPTABLE)

        drop_div = self.element_is_visible(
            self.locators.ACCEPT_DROP_HERE)

        with allure.step("Work with the 'Not Acceptable' draggable item"):
            if draggable_type == "not acceptable":
                with allure.step(f"Drag {not_acceptable_div.text} "
                                 f"and drop to {drop_div.text} element"):
                    self.action_drag_and_drop_to_element(
                        not_acceptable_div,
                        drop_div
                    )

                log.info(f"Droppable not acceptable info: "
                         f"source = {not_acceptable_div.text}, "
                         f"target = {drop_div.text}")
                log.info(f"Dragged and dropped {not_acceptable_div.text} "
                         f"element to the target {drop_div.text}")

                with allure.step("Get the 'Not Acceptable' text"):
                    drop_text_not_acceptable = drop_div.text
                    log.info(
                        f"Returns text results for not acceptable item: "
                        f"{drop_text_not_acceptable}"
                        )
                    return drop_text_not_acceptable

        with allure.step(
                "Work with the 'Acceptable' draggable item"):
            if draggable_type == "acceptable":

                with allure.step(f"Drag {acceptable_div.text} "
                                 f"and drop to {drop_div.text} element"):
                    self.action_drag_and_drop_to_element(
                        acceptable_div,
                        drop_div
                    )

                log.info(f"Droppable acceptable info: "
                         f"source = {acceptable_div.text}, "
                         f"target = {drop_div.text}")
                log.info(f"Dragged and dropped {acceptable_div.text} "
                         f"element to the target {drop_div.text}")

                with allure.step("Get the 'Acceptable' text"):
                    drop_text_acceptable = drop_div.text
                    log.info(
                        f"Returns text results for acceptable item: "
                        f"{drop_text_acceptable}"
                        )
                    return drop_text_acceptable











    @allure.step(
        "Check the 'Prevent Propogation' drop"
    )
    def drop_prevent_propogation(self, drag_type):
        log = self.get_logger()

        with allure.step("Open the 'Prevent Propogation' tab"):
            self.element_is_visible(
                self.locators.PREVENT_TAB).click()
        log.info("Opened prevent propogation droppable page")

        drag_div = self.element_is_visible(
            self.locators.PREVENT_DRAG_ME)

        not_greedy_inner_box = self.element_is_visible(
            self.locators.PREVENT_NOT_GREEDY_INNER_BOX)

        greedy_inner_box = self.element_is_visible(
            self.locators.PREVENT_GREEDY_INNER_BOX)

        with allure.step("Work with the 'Not Greedy' item"):
            if drag_type == "not greedy":
                with allure.step(
                        f"Drag {drag_div.text} and drop item "
                        f"to {not_greedy_inner_box.text} element"):
                    self.action_drag_and_drop_to_element(
                        drag_div,
                        not_greedy_inner_box
                    )
                log.info(f"Dragged and dropped {drag_div.text} element "
                         f"to the target {not_greedy_inner_box.text}")

                with allure.step("Get the 'Not Greedy Box' text"):
                    text_not_greedy_box = self.element_is_visible(
                        self.locators.PREVENT_NOT_GREEDY_DROP_BOX_TEXT).text

                with allure.step("Get the 'Not Greedy Inner Box' text"):
                    text_not_greedy_inner_box = not_greedy_inner_box.text

                log.info(f"Returns not greedy text for box, inner box: "
                         f"{text_not_greedy_box}, "
                         f"{text_not_greedy_inner_box}")
                return text_not_greedy_box, text_not_greedy_inner_box

        with allure.step("Work with the 'Greedy' item"):
            if drag_type == "greedy":
                with allure.step(
                        f"Drag {drag_div.text} and drop "
                        f"to {greedy_inner_box.text} element"):
                    self.action_drag_and_drop_to_element(
                        drag_div,
                        greedy_inner_box
                    )

                log.info(f"Dragged and dropped {drag_div.text} element "
                         f"to the target {greedy_inner_box.text}")

                with allure.step("Get the 'Greedy Box' text"):
                    text_greedy_box = self.element_is_visible(
                        self.locators.PREVENT_GREEDY_DROP_BOX_TEXT).text

                with allure.step("Get the 'Greedy Inner Box' text"):
                    text_greedy_inner_box = greedy_inner_box.text

                log.info(f"Returns greedy text for box, inner box: "
                         f"{text_greedy_box}, "
                         f"{text_greedy_inner_box}")
                return text_greedy_box, text_greedy_inner_box











    @allure.step(
        "Check the 'Revert Draggable' drop"
    )
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

        with allure.step("Open the 'Revert Draggable' tab"):
            self.element_is_visible(
                self.locators.REVERT_TAB).click()
        log.info("Opened revert draggable tab")

        revert = self.element_is_visible(drags[drag_type]["revert"])
        drop_div = self.element_is_visible(
            self.locators.REVERT_DROP_HERE)
        log.info(f"Drag and drop info: {revert.text}, "
                 f"{drop_div.text}")

        with allure.step(f"Drag {revert.text} "
                         f"and drop to {drop_div.text} element"):
            self.action_drag_and_drop_to_element(
                revert,
                drop_div
            )

        log.info(f"Dragged and dropped {revert.text} element"
                 f" to the target {drop_div.text}")

        with allure.step("Get the 'After Move' position"):
            position_after_move = revert.get_attribute("style")

        with allure.step("Wait 1 second for element revert"):
            time.sleep(1)

        with allure.step("Get the 'After Revert' position"):
            position_after_revert = revert.get_attribute("style")

        log.info(f"Returned data: "
                 f"{position_after_move=}, "
                 f"{position_after_revert=}")
        return position_after_move, position_after_revert
