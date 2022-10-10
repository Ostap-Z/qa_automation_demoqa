from pages.base_page import BasePage
from locators.radio_button_locators import RadioButtonPageLocators


class RadioButtonPage(BasePage):
    locators = RadioButtonPageLocators()

    def click_on_the_radio_button(self, choice):
        choices = {'yes': self.locators.RADIOBUTTON_YES,
                   'impressive': self.locators.RADIOBUTTON_IMPRESSIVE,
                   'no': self.locators.RADIOBUTTON_NO}

        radio = self.element_is_visible(choices[choice]).click()

    def output_result(self):
        return self.element_is_present(self.locators.OUTPUT_RESULT).text