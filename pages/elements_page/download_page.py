import base64
import os.path
from random import randint

from pages.base_page import BasePage
from locators.elements_locators.download_locators import DownloadLocators


class DownloadPage(BasePage):
    locators = DownloadLocators()

    def download_file(self):
        log = self.get_logger()
        link = self.element_is_present(
            self.locators.DOWNLOAD_FILE).get_attribute("href")
        link_b = base64.b64decode(link)
        path_name_file = rf"C:\Users\OstapZherebetskyi\Desktop\test_examples\qa_automation_demo\qa_automation_demoqa\filetest{randint(0, 999)}.jpg"
        with open(path_name_file, "wb+") as file:
            offset = link_b.find(b'\xff\xd8')
            file.write(link_b[offset:])
            check_file = os.path.exists(path_name_file)
            log.info(f"File {file} was created: {check_file}")
        self.remove_file(path_name_file)
        log.info(f"File {file} was removed")
        return check_file

    @staticmethod
    def remove_file(file):
        os.remove(file)


