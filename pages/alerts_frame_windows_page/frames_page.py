from pages.base_page import BasePage
from locators.alerts_frame_windows_locators.frames_locators import FramesLocators


class FramesPage(BasePage):
    locators = FramesLocators()

    def check_frame(self, frame_num):
        if frame_num == 1:
            frame = self.element_is_present(self.locators.FIRST_FRAME)
            width = frame.get_attribute("width")
            height = frame.get_attribute("height")
            self.go_to_frame(frame)
            text = self.element_is_present(self.locators.TITLE_FRAME).text
            self.go_to_default_content()
            return [text, width, height]

        elif frame_num == 2:
            frame = self.element_is_present(self.locators.SECOND_FRAME)
            width = frame.get_attribute("width")
            height = frame.get_attribute("height")
            self.go_to_frame(frame)
            text = self.element_is_present(self.locators.TITLE_FRAME).text
            self.go_to_default_content()
            return [text, width, height]
