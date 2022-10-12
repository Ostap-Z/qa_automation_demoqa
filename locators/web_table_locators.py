from selenium.webdriver.common.by import By


class WebTablePageLocators:
    # Locators for the registration a new user
    ADD_BUTTON = (By.ID, "addNewRecordButton")
    FIRST_NAME_INPUT = (By.ID, "firstName")
    LAST_NAME_INPUT = (By.ID, "lastName")
    EMAIL_INPUT = (By.ID, "userEmail")
    AGE_INPUT = (By.ID, "age")
    SALARY_INPUT = (By.ID, "salary")
    DEPARTMENT_INPUT = (By.ID, "department")
    SUBMIT_BUTTON = (By.ID, "submit")

    # Locators for the table
    FULL_PERSON_LIST = (By.CSS_SELECTOR, "div.rt-tr-group")
