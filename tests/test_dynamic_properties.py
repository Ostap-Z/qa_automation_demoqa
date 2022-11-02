from pages.dynamic_properties_page import DynamicPropertiesPage


class TestDynamicProperties:

    def test_dynamic_properties(self, driver):
        dynamic_properties = DynamicPropertiesPage(driver, "https://demoqa.com/dynamic-properties")
        dynamic_properties.open()
        color_before, color_after = dynamic_properties.check_changed_color()
        assert color_before != color_after, f"\nColors should be different" \
                                            f"\nActual coloc before: {color_before}" \
                                            f"\nActual color after: {color_after}"

