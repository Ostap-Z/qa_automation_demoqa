from selenium.webdriver.common.by import By


class UploadLocators:
    UPLOAD_FILE = (By.CSS_SELECTOR, "input#uploadFile")
    UPLOADED_RESULT = (By.CSS_SELECTOR, "p#uploadedFilePath")
