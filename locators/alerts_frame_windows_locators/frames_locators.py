from selenium.webdriver.common.by import By


class FramesLocators:
    FIRST_FRAME = (
        By.CSS_SELECTOR,
        "iframe#frame1"
    )
    SECOND_FRAME = (
        By.CSS_SELECTOR,
        "iframe#frame2"
    )
    TITLE_FRAME = (
        By.CSS_SELECTOR,
        "h1#sampleHeading"
    )
