from selenium.webdriver.common.by import By


class DatePickerLocators:
    # Date locators
    DATE_INPUT = (By.CSS_SELECTOR, "input#datePickerMonthYearInput")
    DATE_SELECT_MONTH = (By.CSS_SELECTOR, "select.react-datepicker__month-select")
    DATE_SELECT_YEAR = (By.CSS_SELECTOR, "select.react-datepicker__year-select")
    DATE_SELECT_DAY_LIST = (By.CSS_SELECTOR, "div[class*='react-datepicker__day react-datepicker__day']")
