from selenium.webdriver.common.by import By


class WebTablePageLocators:
    # Locators for the registration a new user
    ADD_BUTTON = (
        By.ID,
        "addNewRecordButton"
    )
    FIRST_NAME_INPUT = (
        By.ID,
        "firstName"
    )
    LAST_NAME_INPUT = (
        By.ID,
        "lastName"
    )
    EMAIL_INPUT = (
        By.ID,
        "userEmail"
    )
    AGE_INPUT = (
        By.ID,
        "age"
    )
    SALARY_INPUT = (
        By.ID,
        "salary"
    )
    DEPARTMENT_INPUT = (
        By.ID,
        "department"
    )
    SUBMIT_BUTTON = (
        By.ID,
        "submit"
    )

    # Locators for the table
    FULL_PERSON_LIST = (
        By.CSS_SELECTOR,
        "div.rt-tr-group"
    )
    DELETE_BUTTON = (
        By.CSS_SELECTOR,
        "span[title='Delete']"
    )
    UPDATE_BUTTON = (
        By.CSS_SELECTOR,
        "span[title='Edit']"
    )
    ROW_PARENT = (
        By.XPATH,
        ".//ancestor::div[@class='rt-tr-group']"
    )
    NO_ROWS_FOUND = (
        By.CLASS_NAME,
        "rt-noData"
    )
    ROW_COUNT_LIST = (
        By.CSS_SELECTOR,
        "select[aria-label='rows per page']"
    )

    # Locator for the search
    SEARCH_INPUT = (
        By.ID,
        "searchBox"
    )
