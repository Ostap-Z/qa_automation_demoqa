import os

import allure
from selenium.webdriver import Keys

from pages.base_page import BasePage
from locators.forms_locators.form_locators import FormLocators
from generator.generator import generated_person, generated_file


class FormPage(BasePage):
    locators = FormLocators()

    @allure.step(
        "Fills in a registration form"
    )
    def fill_form_fields(self):
        log = self.get_logger()

        with allure.step("Generate a person info"):
            person = next(generated_person())

        with allure.step("Generate a file"):
            file_name, path = generated_file()

        with allure.step("Remove ads and footer on the 'Form' page"):
            self.hide_ads()
            self.remove_footer()

        with allure.step("Fill in the 'First Name' field"):
            self.element_is_visible(self.locators.FIRST_NAME).\
                send_keys(person.first_name)

        with allure.step("Fill in the 'Last Name' field"):
            self.element_is_visible(self.locators.LAST_NAME).\
                send_keys(person.last_name)

        with allure.step("Fill in the 'Email' field"):
            self.element_is_visible(self.locators.EMAIL).\
                send_keys(person.email)

        with allure.step("Chose a gender"):
            self.element_is_visible(self.locators.GENDER).click()

        with allure.step("Fill in the 'Mobile' field"):
            self.element_is_visible(self.locators.MOBILE).\
                send_keys(person.mobile)

        with allure.step("Fill in the 'Subject' field"):
            self.element_is_visible(self.locators.SUBJECT).\
                send_keys("Maths")
            self.element_is_visible(self.locators.SUBJECT).\
                send_keys(Keys.RETURN)

        with allure.step("Chose hobbies"):
            self.element_is_visible(self.locators.HOBBIES).click()

        with allure.step(f"Upload a file in the input: {path}"):
            self.element_is_present(self.locators.FILE_INPUT).\
                send_keys(path)

        self.remove_file(path)

        with allure.step("Fill in the 'Current Address' field"):
            self.element_is_visible(self.locators.CURRENT_ADDRESS).\
                send_keys(person.current_address)

        with allure.step("Select a state"):
            self.element_is_visible(self.locators.SELECT_STATE).click()
            self.element_is_visible(self.locators.STATE_INPUT).\
                send_keys(Keys.RETURN)

        with allure.step("Select a city"):
            self.element_is_visible(self.locators.SELECT_CITY).click()
            self.element_is_visible(self.locators.CITY_INPUT).\
                send_keys(Keys.RETURN)

        with allure.step("Remove ads on the 'Form' page"):
            self.hide_ads()

        with allure.step("Submit the registration form"):
            self.element_is_visible(self.locators.SUBMIT_BUTTON).click()
        log.info(f"Filled in form with data: {person}")
        return person

    @allure.step(
        "Get form result"
    )
    def get_form_result(self):
        log = self.get_logger()

        with allure.step("Open a form result table"):
            result = self.elements_are_present(self.locators.RESULT_TABLE)

        with allure.step("Append results in the list"):
            data = []
            for item in result:
                self.go_to_element(item)
                data.append(item.text)
        log.info(f"Form data presented in the result: {data}")
        return data

    @staticmethod
    @allure.step(
        "Remove a file: {0}"
    )
    def remove_file(file):
        os.remove(file)
