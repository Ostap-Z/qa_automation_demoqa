from pages.widgets_page.tool_tips_page import ToolTipsPage


class TestToolTips:

    def test_tool_tips(self, driver):
        tool_tips_page = ToolTipsPage(driver, "https://demoqa.com/tool-tips")
        tool_tips_page.open()
        button_text, input_text, contrary_text, section_text = tool_tips_page.check_tool_tips()
        assert button_text == "You hovered over the Button", \
            f"\nActual result:\n\tHovered text is empty or not equal to expected.\n\tHovered text: {button_text}"\
            F"\nExpected result:\n\tHovered text should be: You hovered over the Button"

        assert input_text == "You hovered over the text field", \
            f"\nActual result:\n\tHovered text is empty or not equal to expected.\n\tHovered text: {input_text}" \
            F"\nExpected result:\n\tHovered text should be: You hovered over the text field"

        assert contrary_text == "You hovered over the Contrary", \
            f"\nActual result:\n\tHovered text is empty or not equal to expected.\n\tHovered text: {contrary_text}" \
            F"\nExpected result:\n\tHovered text should be: You hovered over the Contrary"

        assert section_text == "You hovered over the 1.10.32", \
            f"\nActual result:\n\tHovered text is empty or not equal to expected.\n\tHovered text: {section_text}" \
            F"\nExpected result:\n\tHovered text should be: You hovered over the 1.10.32"
