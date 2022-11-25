import allure

from pages.base_page import BasePage
from locators.elements_locators.text_box_locators import TextBoxPageLocators
from generator.generator import generated_person


class TextBoxPage(BasePage):
    locators = TextBoxPageLocators()

    @allure.step(
        "Fill in form fields"
    )
    def fill_in_form_fields(self):
        log = self.get_logger()
        person_info = next(generated_person())
        full_name = person_info.full_name
        email = person_info.email
        current_address = person_info.current_address
        permanent_address = person_info.permanent_address

        with allure.step("Fills in the 'Full Name' field"):
            self.element_is_visible(
                self.locators.FULL_NAME).send_keys(full_name)

        with allure.step("Fills in the 'Email' field"):
            self.element_is_visible(
                self.locators.EMAIL).send_keys(email)

        with allure.step("Fills in the 'Current Address' field"):
            self.element_is_visible(
                self.locators.CURRENT_ADDRESS).send_keys(current_address)

        with allure.step("Fills in the 'Permanent Address' field"):
            self.element_is_visible(
                self.locators.PERMANENT_ADDRESS).\
                send_keys(permanent_address)

        log.info(f"Filled in form with data: "
                 f"{full_name, email, current_address, permanent_address}")

        with allure.step("Sends a form"):
            self.element_is_visible(self.locators.SUBMIT_BUTTON).click()

        log.info("Submitted a form")
        return full_name, email, current_address, permanent_address

    @allure.step(
        "Validate the filled form"
    )
    def validate_filled_form(self):
        log = self.get_logger()

        with allure.step("Validate the 'Full Name' field"):
            full_name = self.element_is_present(
                self.locators.CREATED_FULL_NAME).text.split(":")[1]

        with allure.step("Validate the 'Email' field"):
            email = self.element_is_present(
                self.locators.CREATED_EMAIL).text.split(":")[1]

        with allure.step("Validate the 'Current Address' field"):
            current_address = self.element_is_present(
                self.locators.CREATED_CURRENT_ADDRESS).text

        with allure.step("Validate the 'Permanent Address' field"):
            permanent_address = self.element_is_present(
                self.locators.CREATED_PERMANENT_ADDRESS).text

        log.info(f"Received form with data: "
                 f"{full_name, email, current_address, permanent_address}")
        return full_name, email, current_address, permanent_address
