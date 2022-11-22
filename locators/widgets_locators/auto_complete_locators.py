from selenium.webdriver.common.by import By


class AutoCompleteLocators:
    MULTIPLE_INPUT = (
        By.CSS_SELECTOR,
        "input#autoCompleteMultipleInput"
    )
    MULTIPLE_VALUE = (
        By.CSS_SELECTOR,
        "div.css-1rhbuit-multiValue.auto-complete__multi-value"
    )
    MULTIPLE_VALUE_REMOVE = (
        By.CSS_SELECTOR,
        "div.css-1rhbuit-multiValue.auto-complete__multi-value"
        " svg > path"
    )

    SINGLE_INPUT = (
        By.CSS_SELECTOR,
        "input#autoCompleteSingleInput"
    )
    SINGLE_VALUE = (
        By.CSS_SELECTOR,
        "div.auto-complete__single-value.css-1uccc91-singleValue"
    )
