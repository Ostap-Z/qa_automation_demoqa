from .base_page import BasePage
from locators.text_box_locators import TextBoxPageLocators


class TextBoxPage(BasePage):
    locators = TextBoxPageLocators()

    def fill_in_form_fields(self):
        self.element_is_visible(self.locators.FULL_NAME).send_keys()
        self.element_is_visible(self.locators.EMAIL).send_keys()
        self.element_is_visible(self.locators.CURRENT_ADDRESS).send_keys()
        self.element_is_visible(self.locators.PERNAMENT_ADDRESS).send_keys()
        self.element_is_visible(self.locators.SUBMIT_BUTTON).click()

    def validate_filled_form(self):
        full_name = self.element_is_present(self.locators.CREATED_FULL_NAME).text.split(":")[1]
        email = self.element_is_present(self.locators.CREATED_EMAIL).text.split(":")[1]
        current_address = self.element_is_present(self.locators.CREATED_CURRENT_ADDRESS).text
        pernament_address = self.element_is_present(self.locators.CREATED_PERNAMENT_ADDRESS).text
        return full_name, email, current_address, pernament_address
