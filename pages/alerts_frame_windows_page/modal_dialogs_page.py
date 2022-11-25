import allure

from pages.base_page import BasePage
from locators.alerts_frame_windows_locators.modal_dialogs_locators import ModalDialogsLocators


class ModalDialogsPage(BasePage):
    locators = ModalDialogsLocators()

    @allure.step(
        "Check the 'Small' modal dialog"
    )
    def check_small_modal_dialog(self):
        log = self.get_logger()

        with allure.step("Open the 'Small' modal dialog"):
            self.element_is_visible(
                self.locators.SMALL_MODAL_BUTTON).click()
        log.info("Opened small modal dialog")

        with allure.step("Get a title from the "
                         "'Small' modal dialog"):
            small_modal_title = self.element_is_visible(
                self.locators.SMALL_MODAL_TITLE).text

        with allure.step("Get a text from the "
                         "'Small' modal dialog"):
            small_modal_text = self.element_is_visible(
                self.locators.SMALL_MODAL_TEXT).text

        with allure.step("Close the 'Small' modal dialog"):
            self.element_is_visible(
                self.locators.SMALL_MODAL_CLOSE_BUTTON).click()
        log.info("Closed the small modal dialog")

        log.info(f"Returned data from the small modal dialog: "
                 f"['{small_modal_title}', {len(small_modal_text)}]")
        return [small_modal_title, len(small_modal_text)]

    @allure.step(
        "Check the 'Large' modal dialog"
    )
    def check_large_modal_dialog(self):
        log = self.get_logger()

        with allure.step("Open the 'Large' modal dialog"):
            self.element_is_visible(
                self.locators.LARGE_MODAL_BUTTON).click()
        log.info("Opened large modal dialog")

        with allure.step("Get a title from the "
                         "'Large' modal dialog"):
            large_modal_title = self.element_is_visible(
                self.locators.LARGE_MODAL_TITLE).text

        with allure.step("Get a text from the "
                         "'Large' modal dialog"):
            large_modal_text = self.element_is_visible(
                self.locators.LARGE_MODAL_TEXT).text

        with allure.step("Close the 'Large' modal dialog"):
            self.element_is_visible(
                self.locators.LARGE_MODAL_CLOSE_BUTTON).click()
        log.info("Closed the large modal dialog")

        log.info(f"Returned data from the large modal dialog: "
                 f"['{large_modal_title}', {len(large_modal_text)}]")
        return [large_modal_title, len(large_modal_text)]
