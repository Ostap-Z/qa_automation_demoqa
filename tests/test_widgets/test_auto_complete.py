from pages.widgets_page.auto_complete_page import AutoCompletePage


class TestAutoComplete:

    def test_multiple_auto_complete(self, driver):
        auto_complete_page = AutoCompletePage(driver, "https://demoqa.com/auto-complete")
        auto_complete_page.open()
        colors = auto_complete_page.fill_multiple_input()
        colors_result = auto_complete_page.check_multiple_values()
        assert colors == colors_result, \
            f"\nActual result:\n\tColors are not the same.\n\tInput colors: {colors}\n\tOutput colors: {colors_result}"\
            f"\nExpected result:\n\tInput and output colors should be the same"

    def test_remove_multiple_value(self, driver):
        auto_complete_page = AutoCompletePage(driver, "https://demoqa.com/auto-complete")
        auto_complete_page.open()
        colors = auto_complete_page.fill_multiple_input()
        before, after = auto_complete_page.remove_multiple_value()
        assert before > after, \
            f"\nActual result:\n\tColors were not removed.\n\tInput colors: {colors}" \
            f"\n\tInput amount of colors: {before}\n\tOutput amount of colors: {after}" \
            "\nExpected result:\n\tOutput colors should be less than input colors. So, some colors were removed."

    def test_single_auto_complete(self, driver):
        auto_complete_page = AutoCompletePage(driver, "https://demoqa.com/auto-complete")
        auto_complete_page.open()
        color = auto_complete_page.fill_single_input()
        color_result = auto_complete_page.check_single_value()
        assert color == color_result, \
            f"\nActual result:\n\tInput and output color is not the same."\
            f"\n\tInput color: {color}\n\tOutput color: {color_result}"\
            f"\nExpected result:\n\tInput and output color should be the same."
