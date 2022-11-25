import allure

from pages.base_page import BasePage
from locators.elements_locators.radio_button_locators import RadioButtonPageLocators


class RadioButtonPage(BasePage):
    locators = RadioButtonPageLocators()

    @allure.step(
        f"Click on the different radio buttons"
    )
    def click_on_the_radio_button(self, choice):
        log = self.get_logger()
        choices = {'yes': self.locators.RADIOBUTTON_YES,
                   'impressive': self.locators.RADIOBUTTON_IMPRESSIVE,
                   'no': self.locators.RADIOBUTTON_NO}

        with allure.step(f"Click on the radio button: {choice}"):
            self.element_is_visible(choices[choice]).click()
        log.info(f"Clicked on the radio button: {choices[choice]}")

    @allure.step(
        "Get output result"
    )
    def output_result(self):
        log = self.get_logger()
        result = self.element_is_present(
            self.locators.OUTPUT_RESULT).text
        log.info(f"Clicked radio button displayed in the output result: "
                 f"{result}")
        return result
