import allure

from pages.widgets_page.slider_page import SliderPage


@allure.suite("Widgets suite")
@allure.feature("Slider page")
class TestSlider:

    @allure.title(
        "Verify that the user has an opportunity "
        "to drag the 'Slider' element"
    )
    def test_slider(self, driver):
        slider_page = SliderPage(
            driver,
            "https://demoqa.com/slider"
        )
        slider_page.open()
        slider_value_before, slider_value_after = \
            slider_page.change_slider_value()

        assert slider_value_before != slider_value_after, \
            f"\nActual result:" \
            f"\n\tSlider was not dragged." \
            f"\n\tBefore position: {slider_value_before}" \
            f"\n\tAfter position: {slider_value_after}"\
            "\nExpected result:" \
            "\n\tThe slider should be dragged. " \
            "So, after and before positions should not be the same"
