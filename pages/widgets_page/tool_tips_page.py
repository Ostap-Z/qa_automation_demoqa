import time

from pages.base_page import BasePage
from locators.widgets_locators.tool_tips_locators import ToolTipsLocators


class ToolTipsPage(BasePage):
    locators = ToolTipsLocators()

    def get_tool_tips_text(self, hover_elem, wait_elem):
        element = self.element_is_present(hover_elem)
        self.action_move_to_element(element)
        self.element_is_visible(wait_elem)
        tool_tip = self.element_is_visible(self.locators.TOOL_TIPS_INNER)
        tool_tip_text = tool_tip.text
        time.sleep(0.5)
        return tool_tip_text

    def check_tool_tips(self):
        tool_tip_text_button = self.get_tool_tips_text(self.locators.HOVER_BUTTON, self.locators.TOOL_TIP_BUTTON)
        tool_tip_text_input = self.get_tool_tips_text(self.locators.HOVER_INPUT, self.locators.TOOL_TIP_INPUT)
        tool_tip_text_contrary = self.get_tool_tips_text(self.locators.HOVER_CONTRARY_LINK, self.locators.TOOL_TIP_CONTRARY)
        tool_tip_text_section = self.get_tool_tips_text(self.locators.HOVER_SECTION_LINK, self.locators.TOOL_TIP_SECTION)
        return tool_tip_text_button, tool_tip_text_input, tool_tip_text_contrary, tool_tip_text_section
