from random import randint

import allure

from pages.base_page import BasePage
from locators.interactions_locators.draggable_locators import DraggableLocators


class DraggablePage(BasePage):
    locators = DraggableLocators()

    @allure.step(
        "Drag and drop elements "
        "and get their before drag and after drag positions"
    )
    def get_before_after_positions(self, drag_element):
        log = self.get_logger()

        with allure.step("Drag and drop element by offset"):
            self.action_drag_and_drop_by_offset(
                drag_element,
                randint(0, 50),
                randint(0, 50)
            )

        with allure.step("Get before drag position"):
            before_position = drag_element.get_attribute("style")
        log.info(f"Dragged item to the position: {before_position}")

        with allure.step("Drag and drop element by offset"):
            self.action_drag_and_drop_by_offset(
                drag_element,
                randint(0, 50),
                randint(0, 50)
            )

        with allure.step("Get after drag position"):
            after_position = drag_element.get_attribute("style")
        log.info(f"Dragged item to the position: {after_position}")

        log.info(f"Returned before, after positions: "
                 f"{before_position=}; {after_position=}")
        return before_position, after_position

    @allure.step("Simple drag box")
    def simple_drag_box(self):
        log = self.get_logger()

        with allure.step("Open the 'Draggable Simple' tab"):
            self.element_is_visible(
                self.locators.SIMPLE_TAB).click()
        log.info("Opened simple tab")

        with allure.step("Check if the 'Draggable' element "
                         "is visible on the page"):
            drag_div = self.element_is_visible(
                self.locators.SIMPLE_DRAG_ME)

        before_position, after_position = \
            self.get_before_after_positions(drag_div)
        return before_position, after_position
