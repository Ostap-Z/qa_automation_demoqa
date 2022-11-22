from selenium.webdriver.common.by import By


class AccordianLocators:
    FIRST_HEADING = (
        By.CSS_SELECTOR,
        "div#section1Heading"
    )
    FIRST_CONTENT = (
        By.CSS_SELECTOR,
        "div#section1Content > p"
    )

    SECOND_HEADING = (
        By.CSS_SELECTOR,
        "div#section2Heading"
    )
    SECOND_CONTENT = (
        By.CSS_SELECTOR,
        "div#section2Content > p"
    )

    THIRD_HEADING = (
        By.CSS_SELECTOR,
        "div#section3Heading"
    )
    THIRD_CONTENT = (
        By.CSS_SELECTOR,
        "div#section3Content > p"
    )
