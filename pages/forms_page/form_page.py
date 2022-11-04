import os

from selenium.webdriver import Keys

from pages.base_page import BasePage
from locators.forms_locators.form_locators import FormLocators
from generator.generator import generated_person, generated_file


class FormPage(BasePage):
    locators = FormLocators()

    def fill_form_fields(self):
        person = next(generated_person())
        file_name, path = generated_file()
        self.hide_ads()
        self.remove_footer()
        self.element_is_visible(self.locators.FIRST_NAME).send_keys(person.first_name)
        self.element_is_visible(self.locators.LAST_NAME).send_keys(person.last_name)
        self.element_is_visible(self.locators.EMAIL).send_keys(person.email)
        self.element_is_visible(self.locators.GENDER).click()
        self.element_is_visible(self.locators.MOBILE).send_keys(person.mobile)
        self.element_is_visible(self.locators.SUBJECT).send_keys("Maths")
        self.element_is_visible(self.locators.SUBJECT).send_keys(Keys.RETURN)
        self.element_is_visible(self.locators.HOBBIES).click()
        self.element_is_present(self.locators.FILE_INPUT).send_keys(path)
        self.remove_file(path)
        self.element_is_visible(self.locators.CURRENT_ADDRESS).send_keys(person.current_address)
        self.element_is_visible(self.locators.SELECT_STATE).click()
        self.element_is_visible(self.locators.STATE_INPUT).send_keys(Keys.RETURN)
        self.element_is_visible(self.locators.SELECT_CITY).click()
        self.element_is_visible(self.locators.CITY_INPUT).send_keys(Keys.RETURN)
        self.hide_ads()
        self.element_is_visible(self.locators.SUBMIT_BUTTON).click()
        return person

    def get_form_result(self):
        result = self.elements_are_present(self.locators.RESULT_TABLE)
        data = []
        for item in result:
            self.go_to_element(item)
            data.append(item.text)
        return data

    @staticmethod
    def remove_file(file):
        os.remove(file)
