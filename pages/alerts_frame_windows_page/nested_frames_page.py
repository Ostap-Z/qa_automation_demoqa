from pages.base_page import BasePage
from locators.alerts_frame_windows_locators.nested_frames_locators import NestedFramesLocators


class NestedFramesPage(BasePage):
    locators = NestedFramesLocators()

    def check_nested_frame(self):
        parent_frame = self.element_is_present(self.locators.PARENT_FRAME)
        self.go_to_frame(parent_frame)
        parent_text = self.element_is_present(self.locators.PARENT_TEXT).text

        child_frame = self.element_is_present(self.locators.CHILD_FRAME)
        self.go_to_frame(child_frame)
        child_text = self.element_is_present(self.locators.CHILD_TEXT).text
        return parent_text, child_text
