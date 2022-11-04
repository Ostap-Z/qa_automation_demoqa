import os

from pages.base_page import BasePage
from locators.elements_locators.upload_locators import UploadLocators
from generator.generator import generated_file


class UploadPage(BasePage):
    locators = UploadLocators()

    def upload_file(self):
        log = self.get_logger()
        file_name, path = generated_file()
        log.info(f"Generated file: {file_name}")
        self.element_is_present(self.locators.UPLOAD_FILE).send_keys(path)
        log.info(f"Uploaded a file {file_name}")
        self.remove_file(path)
        log.info(f"Removed a file {file_name} from project directory")
        return file_name.split("\\")[-1], self.uploaded_result.split("\\")[-1]

    @property
    def uploaded_result(self):
        log = self.get_logger()
        result = self.element_is_present(self.locators.UPLOADED_RESULT).text.split("\\")[-1]
        log.info(f'Uploaded file presented in text: {result}')
        return result

    @staticmethod
    def remove_file(file):
        os.remove(file)
