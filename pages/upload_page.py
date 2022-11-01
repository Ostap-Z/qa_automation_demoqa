import os

from pages.base_page import BasePage
from locators.upload_locators import UploadLocators
from generator.generator import generated_file


class UploadPage(BasePage):
    locators = UploadLocators()

    def upload_file(self):
        file_name, path = generated_file()
        self.element_is_present(self.locators.UPLOAD_FILE).send_keys(path)
        self.remove_file(path)
        return file_name.split("\\")[-1], self.uploaded_result.split("\\")[-1]

    @property
    def uploaded_result(self):
        return self.element_is_present(self.locators.UPLOADED_RESULT).text

    @staticmethod
    def remove_file(file):
        os.remove(file)
