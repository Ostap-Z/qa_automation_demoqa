from pages.base_page import BasePage
from locators.alerts_frame_windows_locators.frames_locators import FramesLocators


class FramesPage(BasePage):
    locators = FramesLocators()

    def check_frame(self, frame_num):
        log = self.get_logger()
        if frame_num == 1:
            frame = self.element_is_present(
                self.locators.FIRST_FRAME)
            log.info("First frame is presented in the DOM")
            width = frame.get_attribute("width")
            height = frame.get_attribute("height")
            log.info(f"First frame width, height: {width}, {height}")
            self.go_to_frame(frame)
            log.info("Switched to the first frame")
            text = self.element_is_present(
                self.locators.TITLE_FRAME).text
            log.info(f"Presented text in the first frame: '{text}'")
            self.go_to_default_content()
            log.info("Switched back to the default content")
            log.info(f"Returned data for the first frame: "
                     f"[{text}, {width}, {height}]")
            return [text, width, height]

        elif frame_num == 2:
            frame = self.element_is_present(
                self.locators.SECOND_FRAME)
            log.info("Second frame is presented in the DOM")
            width = frame.get_attribute("width")
            height = frame.get_attribute("height")
            log.info(f"Second frame width, height: "
                     f"{width}, {height}")
            self.go_to_frame(frame)
            log.info("Switched to the second frame")
            text = self.element_is_present(
                self.locators.TITLE_FRAME).text
            log.info(f"Presented text in the second frame: '{text}'")
            self.go_to_default_content()
            log.info("Switched back to the default content")
            log.info(f"Returned data for the second frame: "
                     f"[{text}, {width}, {height}]")
            return [text, width, height]
