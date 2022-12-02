import allure
import pytest

from pages.elements_page.radio_button_page import RadioButtonPage


@allure.suite("Elements suite")
@allure.feature("Radio buttons page")
class TestRadioButton:

    @allure.title(
        "Verify that the user has an opportunity "
        "to click on the 'Yes' radio button and "
        "get correct output result"
    )
    def test_yes_radio_button(self, driver):
        radio_button_page = RadioButtonPage(
            driver,
            "https://demoqa.com/radio-button"
        )
        radio_button_page.open()
        radio_button_page.click_on_the_radio_button('yes')
        output_yes = radio_button_page.output_result()
        assert output_yes == "Yes", \
            "\nActual result:" \
            "\n\tThe 'Yes' radio button was not pressed" \
            f"\n\tResult text is {output_yes!r}"\
            "\nExpected result:" \
            "\n\tResult text should be 'Yes'. " \
            "So, the button was pressed'"

    @allure.title(
        "Verify that the user has an opportunity "
        "to click on the 'Impressive' radio button and "
        "get correct output result"
    )
    def test_impressive_radio_button(self, driver):
        radio_button_page = RadioButtonPage(
            driver,
            "https://demoqa.com/radio-button"
        )
        radio_button_page.open()
        radio_button_page.click_on_the_radio_button('impressive')
        output_impressive = radio_button_page.output_result()
        assert output_impressive == "Impressive", \
            "\nActual result:" \
            "\n\tThe 'Impressive' radio button was not pressed" \
            f"\n\tResult text is {output_impressive!r}"\
            "\nExpected result:" \
            "\n\tResult text should be 'Impressive'. " \
            "So, the button was pressed'"

    @allure.title(
        "Verify that the user has an opportunity "
        "to click on the 'No' radio button and "
        "get correct output result"
    )
    @pytest.mark.xfail(
        reason="There's a known bug "
               "that the user can't click the 'No' radio button"
    )
    def test_no_radio_button(self, driver):
        radio_button_page = RadioButtonPage(
            driver,
            "https://demoqa.com/radio-button"
        )
        radio_button_page.open()
        radio_button_page.click_on_the_radio_button('no')
        output_no = radio_button_page.output_result()
        assert output_no == "No", \
            "\nActual result:" \
            "\n\tThe 'No' radio button was not pressed" \
            f"\n\tResult text is {output_no!r}"\
            "\nExpected result:" \
            "\n\tResult text should be 'No'. " \
            "So, the button was pressed'"
