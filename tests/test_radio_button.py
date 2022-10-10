import time

from pages.radio_button_page import RadioButtonPage


class TestRadioButton:

    def test_radio_button(self, driver):
        radio_button_page = RadioButtonPage(driver, "https://demoqa.com/radio-button")
        radio_button_page.open()
        radio_button_page.click_on_the_radio_button('yes')
        output_yes = radio_button_page.output_result()
        radio_button_page.click_on_the_radio_button('impressive')
        output_impressive = radio_button_page.output_result()
        radio_button_page.click_on_the_radio_button('no')
        output_no = radio_button_page.output_result()

        assert output_yes == "Yes", f"\nActual result: {output_yes!r}\n"\
                                    f"Expected result: 'Yes'"

        assert output_impressive == "Impressive", f"\nActual result: {output_impressive!r}\n"\
                                                  f"Expected result: 'Impressive'"

        assert output_no == "No", f"\nActual result: {output_no!r}\n"\
                                  f"Expected result: 'No'"
