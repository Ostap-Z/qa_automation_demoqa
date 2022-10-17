from .base_page import BasePage
from locators.text_box_locators import TextBoxPageLocators
from generator.generator import generated_person


class TextBoxPage(BasePage):
    locators = TextBoxPageLocators()

    def fill_in_form_fields(self):
        log = self.get_logger()
        person_info = next(generated_person())
        full_name = person_info.full_name
        email = person_info.email
        current_address = person_info.current_address
        permanent_address = person_info.permanent_address

        self.element_is_visible(self.locators.FULL_NAME).send_keys(full_name)
        self.element_is_visible(self.locators.EMAIL).send_keys(email)
        self.element_is_visible(self.locators.CURRENT_ADDRESS).send_keys(current_address)
        self.element_is_visible(self.locators.PERMANENT_ADDRESS).send_keys(permanent_address)
        log.info(f"Filled in form with data: {full_name, email, current_address, permanent_address}")
        self.element_is_visible(self.locators.SUBMIT_BUTTON).click()
        log.info("Submitted form")
        return full_name, email, current_address, permanent_address

    def validate_filled_form(self):
        log = self.get_logger()
        full_name = self.element_is_present(self.locators.CREATED_FULL_NAME).text.split(":")[1]
        email = self.element_is_present(self.locators.CREATED_EMAIL).text.split(":")[1]
        current_address = self.element_is_present(self.locators.CREATED_CURRENT_ADDRESS).text
        permanent_address = self.element_is_present(self.locators.CREATED_PERMANENT_ADDRESS).text
        log.info(f"Received form with data: {full_name, email, current_address, permanent_address}")
        return full_name, email, current_address, permanent_address
