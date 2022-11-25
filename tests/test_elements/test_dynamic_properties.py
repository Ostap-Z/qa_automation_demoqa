import allure

from pages.elements_page.dynamic_properties_page import DynamicPropertiesPage


@allure.suite("Elements suite")
@allure.feature("Dynamic Properties page")
class TestDynamicProperties:

    @allure.title(
        "Verify that the 'Enable' button "
        "is clickable after 5 seconds"
    )
    def test_dynamic_properties_enable_button(self, driver):
        dynamic_properties = DynamicPropertiesPage(
            driver,
            "https://demoqa.com/dynamic-properties"
        )
        dynamic_properties.open()
        enable_button = dynamic_properties.check_enable_button()
        assert enable_button is True, \
            f"\nActual result: appear_button is clickable: " \
            f"{enable_button}" \
            f"\nExpected result: " \
            f"appear_button should be clickable(True) after 5 seconds"

    @allure.title(
        "Verify that the 'Change Color' button text "
        "is different in 5 seconds"
    )
    def test_dynamic_properties_change_color(self, driver):
        dynamic_properties = DynamicPropertiesPage(
            driver,
            "https://demoqa.com/dynamic-properties"
        )
        dynamic_properties.open()
        color_before, color_after = \
            dynamic_properties.check_changed_color()
        assert color_before != color_after, \
            f"\nColors should be different" \
            f"\nActual coloc before: {color_before}" \
            f"\nActual color after: {color_after}"

    @allure.title(
        "Verify that the 'Visible After' button "
        "is visible after 5 seconds"
    )
    def test_dynamic_properties_appear_button(self, driver):
        dynamic_properties = DynamicPropertiesPage(
            driver,
            "https://demoqa.com/dynamic-properties"
        )
        dynamic_properties.open()
        appear_button = dynamic_properties.check_appear_button()
        assert appear_button is True, \
            f"\nActual result: " \
            f"appear_button is visible: {appear_button}" \
            f"\nExpected result: " \
            f"appear_button should be visible (True)"
