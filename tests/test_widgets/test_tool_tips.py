import allure

from pages.widgets_page.tool_tips_page import ToolTipsPage


@allure.suite("Widgets suite")
@allure.feature("Tool Tips page")
class TestToolTips:

    @allure.title(
        "Verify that the user has an opportunity to "
        "hover over the element 'Button' item "
        "and get a correct tool tip text"
    )
    def test_button_tool_tip(self, driver):
        tool_tips_page = ToolTipsPage(
            driver,
            "https://demoqa.com/tool-tips"
        )
        tool_tips_page.open()
        button_text = tool_tips_page.check_tool_tips("button")
        assert button_text == "You hovered over the Button", \
            f"\nActual result:" \
            f"\n\tHovered text is empty or not equal to expected." \
            f"\n\tHovered text: {button_text}"\
            f"\nExpected result:" \
            f"\n\tHovered text should be: " \
            f"'You hovered over the Button'"

    @allure.title(
        "Verify that the user has an opportunity to "
        "hover over the element 'Input' item "
        "and get a correct tool tip text"
    )
    def test_input_tool_tip(self, driver):
        tool_tips_page = ToolTipsPage(
            driver,
            "https://demoqa.com/tool-tips"
        )
        tool_tips_page.open()
        input_text = tool_tips_page.check_tool_tips("input")
        assert input_text == "You hovered over the text field", \
            f"\nActual result:" \
            f"\n\tHovered text is empty or not equal to expected." \
            f"\n\tHovered text: {input_text}" \
            f"\nExpected result:" \
            f"\n\tHovered text should be: " \
            f"'You hovered over the text field'"

    @allure.title(
        "Verify that the user has an opportunity to "
        "hover over the element 'Contrary' item "
        "and get a correct tool tip text"
    )
    def test_contrary_tool_tip(self, driver):
        tool_tips_page = ToolTipsPage(
            driver,
            "https://demoqa.com/tool-tips"
        )
        tool_tips_page.open()
        contrary_text = tool_tips_page.check_tool_tips("contrary")
        assert contrary_text == "You hovered over the Contrary", \
            f"\nActual result:" \
            f"\n\tHovered text is empty or not equal to expected." \
            f"\n\tHovered text: {contrary_text}" \
            f"\nExpected result:" \
            f"\n\tHovered text should be: " \
            f"'You hovered over the Contrary'"

    @allure.title(
        "Verify that the user has an opportunity to "
        "hover over the element 'Section' item "
        "and get a correct tool tip text"
    )
    def test_section_tool_tip(self, driver):
        tool_tips_page = ToolTipsPage(
            driver,
            "https://demoqa.com/tool-tips"
        )
        tool_tips_page.open()
        section_text = tool_tips_page.check_tool_tips("section")
        assert section_text == "You hovered over the 1.10.32", \
            f"\nActual result:" \
            f"\n\tHovered text is empty or not equal to expected." \
            f"\n\tHovered text: {section_text}" \
            f"\nExpected result:" \
            f"\n\tHovered text should be: " \
            f"'You hovered over the 1.10.32'"
