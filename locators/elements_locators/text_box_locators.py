from selenium.webdriver.common.by import By


class TextBoxPageLocators:
    # Locators for form field
    FULL_NAME = (By.ID, "userName")
    EMAIL = (By.ID, "userEmail")
    CURRENT_ADDRESS = (By.ID, "currentAddress")
    PERMANENT_ADDRESS = (By.ID, "permanentAddress")
    SUBMIT_BUTTON = (By.ID, "submit")

    # Locators for form validation
    CREATED_FULL_NAME = (By.ID, "name")
    CREATED_EMAIL = (By.ID, "email")
    CREATED_CURRENT_ADDRESS = (By.ID, "currentAddress")
    CREATED_PERMANENT_ADDRESS = (By.ID, "permanentAddress")
