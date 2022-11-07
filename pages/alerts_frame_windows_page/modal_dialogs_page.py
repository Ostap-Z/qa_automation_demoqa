from pages.base_page import BasePage
from locators.alerts_frame_windows_locators.modal_dialogs_locators import ModalDialogsLocators


class ModalDialogsPage(BasePage):
    locators = ModalDialogsLocators()

    def check_small_modal_dialog(self):
        self.element_is_visible(self.locators.SMALL_MODAL_BUTTON).click()
        small_modal_title = self.element_is_visible(self.locators.SMALL_MODAL_TITLE).text
        small_modal_text = self.element_is_visible(self.locators.SMALL_MODAL_TEXT).text
        self.element_is_visible(self.locators.SMALL_MODAL_CLOSE_BUTTON).click()
        return [small_modal_title, len(small_modal_text)]

    def check_large_modal_dialog(self):
        self.element_is_visible(self.locators.LARGE_MODAL_BUTTON).click()
        large_modal_title = self.element_is_visible(self.locators.LARGE_MODAL_TITLE).text
        large_modal_text = self.element_is_visible(self.locators.LARGE_MODAL_TEXT).text
        return [large_modal_title, len(large_modal_text)]
