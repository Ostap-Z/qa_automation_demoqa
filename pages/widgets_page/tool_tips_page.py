import time

import allure

from pages.base_page import BasePage
from locators.widgets_locators.tool_tips_locators import ToolTipsLocators


class ToolTipsPage(BasePage):
    locators = ToolTipsLocators()

    @allure.step(
        "Check the 'Tool Tips' text"
    )
    def get_tool_tips_text(self, hover_element, tool_tip_element):
        element = self.element_is_present(hover_element)

        with allure.step("Hover over the element"):
            self.action_move_to_element(element)

        self.element_is_visible(tool_tip_element)
        tool_tip = self.element_is_visible(
            self.locators.TOOL_TIPS_INNER)

        with allure.step("Get the 'Tool Tip' text"):
            tool_tip_text = tool_tip.text

        time.sleep(0.5)
        return tool_tip_text

    @allure.step(
        "Check the different 'Tool Tips'"
    )
    def check_tool_tips(self):
        log = self.get_logger()

        with allure.step("Check the 'Hover Me Tool Tip' button"):
            tool_tip_text_button = \
                self.get_tool_tips_text(
                    self.locators.HOVER_BUTTON,
                    self.locators.TOOL_TIP_BUTTON
                )

        log.info(f"Got tool tip text button: "
                 f"{tool_tip_text_button}")

        with allure.step("Check the 'Hover Me Tool Tip' input"):
            tool_tip_text_input = self.get_tool_tips_text(
                self.locators.HOVER_INPUT,
                self.locators.TOOL_TIP_INPUT
            )

        log.info(f"Got tool tip text button: "
                 f"{tool_tip_text_input}")

        with allure.step("Check the 'Contrary Tool Tip' link"):
            tool_tip_text_contrary = self.get_tool_tips_text(
                self.locators.HOVER_CONTRARY_LINK,
                self.locators.TOOL_TIP_CONTRARY
            )

        log.info(f"Got tool tip text button: "
                 f"{tool_tip_text_contrary}")

        with allure.step("Check the 'Section Tool Tip' link"):
            tool_tip_text_section = self.get_tool_tips_text(
                self.locators.HOVER_SECTION_LINK,
                self.locators.TOOL_TIP_SECTION
            )

        log.info(f"Got tool tip text button: "
                 f"{tool_tip_text_section}")
        return tool_tip_text_button, tool_tip_text_input, \
               tool_tip_text_contrary, tool_tip_text_section
