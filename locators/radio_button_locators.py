from selenium.webdriver.common.by import By


class RadioButtonPageLocators:
    RADIOBUTTON_YES = (By.CSS_SELECTOR, "label[class^='custom-control'][for='yesRadio']")
    RADIOBUTTON_IMPRESSIVE = (By.CSS_SELECTOR, "label[class^='custom-control'][for='impressiveRadio']")
    RADIOBUTTON_NO = (By.CSS_SELECTOR, "label[class^='custom-control'][for='noRadio']")
    OUTPUT_RESULT = (By.CSS_SELECTOR, "p > span[class='text-success']")
