import allure
from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from locators.elements_locators.web_table_locators import WebTablePageLocators
from generator.generator import generated_person


class WebTablePage(BasePage):
    locators = WebTablePageLocators()

    @allure.step(
        "Add a new person"
    )
    def add_new_person(self):
        log = self.get_logger()
        count = 1
        while count != 0:
            person_info = next(generated_person())
            first_name = person_info.first_name
            last_name = person_info.last_name
            email = person_info.email
            age = person_info.age
            salary = person_info.salary
            department = person_info.department

            with allure.step("Opens a registration person form"):
                self.element_is_visible(
                    self.locators.ADD_BUTTON).click()
            log.info("Registration person form is opened")

            with allure.step(f"Fills in the 'First Name' field with data: {first_name}"):
                self.element_is_visible(
                    self.locators.FIRST_NAME_INPUT).send_keys(first_name)

            with allure.step(f"Fills in the 'Last Name' field with data: {last_name}"):
                self.element_is_visible(
                    self.locators.LAST_NAME_INPUT).send_keys(last_name)

            with allure.step(f"Fills in the 'Email' field with data: {email}"):
                self.element_is_visible(
                    self.locators.EMAIL_INPUT).send_keys(email)

            with allure.step(f"Fills in the 'Age' field with data: {age}"):
                self.element_is_visible(
                    self.locators.AGE_INPUT).send_keys(age)

            with allure.step(f"Fills in the 'Salary' field with data: {salary}"):
                self.element_is_visible(
                    self.locators.SALARY_INPUT).send_keys(salary)

            with allure.step(f"Fills in the 'Department' field with data: {department}"):
                self.element_is_visible(
                    self.locators.DEPARTMENT_INPUT).send_keys(department)
            log.info(f"Filled in registration person form with data: "
                     f"{first_name, last_name, email, age, salary, department}")

            with allure.step("Submits a registration form"):
                self.element_is_visible(
                    self.locators.SUBMIT_BUTTON).click()
            log.info("Registration person form is sent")

            count -= 1
            return [first_name, last_name,
                    str(age), email,
                    str(salary), department]

    @allure.step(
        "Check new added person in the table"
    )
    def check_new_added_person(self):
        log = self.get_logger()
        full_person_list = \
            self.elements_are_present(self.locators.FULL_PERSON_LIST)
        data = [item.text.splitlines() for item in full_person_list]
        log.info(f"Found items in the table: {data}")
        return data

    @allure.step(
        "Search a person in the table by key word"
    )
    def search_person(self, key_word):
        log = self.get_logger()

        with allure.step(f"Fills in the search field with key word: {key_word}"):
            self.element_is_visible(
                self.locators.SEARCH_INPUT).send_keys(key_word)
        log.info(f"Searching person in the table")

    @allure.step(
        "Validate a search result"
    )
    def check_search_person(self):
        log = self.get_logger()
        delete_button = \
            self.element_is_present(self.locators.DELETE_BUTTON)
        row = delete_button.find_element(*self.locators.ROW_PARENT)
        result = row.text.splitlines()
        log.info(f"Found items in the table: {result}")
        return result

    @allure.step(
        "Update a person info"
    )
    def update_person_info(self):
        log = self.get_logger()
        person_info = next(generated_person())
        age = person_info.age

        with allure.step("Opens the update section"):
            self.element_is_visible(
                self.locators.UPDATE_BUTTON).click()
        log.info("Update person form is opened")

        with allure.step(f"Clear the presented 'Age' data"):
            self.element_is_visible(
                self.locators.AGE_INPUT).clear()
        log.info("Cleared the age field")

        with allure.step(f"Fills in the 'Age' field with data: {age}"):
            self.element_is_visible(
                self.locators.AGE_INPUT).send_keys(age)
        log.info(f"Updated age field with {age}")

        with allure.step("Submits the updated person form"):
            self.element_is_visible(
                self.locators.SUBMIT_BUTTON).click()
        log.info("Person form is updated")
        return str(age)

    @allure.step(
        "Delete a person from the table by 'Delete' button"
    )
    def delete_person(self):
        self.element_is_visible(
            self.locators.DELETE_BUTTON).click()

    @allure.step(
        "Check the person was deleted"
    )
    def check_deleted_person(self):
        log = self.get_logger()
        result = self.element_is_present(
            self.locators.NO_ROWS_FOUND).text
        log.info("Person was deleted from the table")
        return result

    @allure.step(
        "Select different amount of table rows"
    )
    def select_up_to_rows(self):
        log = self.get_logger()
        count = [5, 10, 20, 25, 50, 100]
        data = []
        for x in count:
            count_row_button = self.element_is_visible(
                self.locators.ROW_COUNT_LIST)
            self.go_to_element(count_row_button)
            count_row_button.click()

            with allure.step(f"Chose amount of table rows: {x}"):
                self.element_is_visible((
                    By.CSS_SELECTOR,
                    f"option[value='{x}']")).click()
            log.info(f"Opened {x} rows in the table")

            data.append(self.check_count_rows())
        return data

    @allure.step(
        "Check amount of opened table rows"
    )
    def check_count_rows(self):
        list_rows = self.elements_are_present(
            self.locators.FULL_PERSON_LIST)
        return len(list_rows)
