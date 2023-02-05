import allure

from pages.base_page import BasePage
from locators.alerts_frame_windows_locators.frames_locators \
    import FramesLocators


class FramesPage(BasePage):
    locators = FramesLocators()

    @allure.step(
        "Check frames"
    )
    def check_frame(self, frame_num):
        log = self.get_logger()

        with allure.step("Check the 'First' frame"):
            if frame_num == 1:

                with allure.step("Check if the 'First' frame "
                                 "is presented on the 'Frames' page"):
                    frame = self.element_is_present(
                        self.locators.FIRST_FRAME)
                log.info("First frame is presented in the DOM")

                with allure.step("Get width, height attributes "
                                 "of the 'First' frame"):
                    width = frame.get_attribute("width")
                    height = frame.get_attribute("height")
                log.info(f"First frame width, height: {width}, {height}")

                with allure.step("Switch to the 'First' frame"):
                    self.go_to_frame(frame)
                log.info("Switched to the first frame")

                with allure.step("Get the 'First' frame text result"):
                    text = self.element_is_present(
                        self.locators.TITLE_FRAME).text
                log.info(f"Presented text in the first frame: '{text}'")

                with allure.step("Switch back to the default content "
                                 "from the 'First' frame"):
                    self.go_to_default_content()
                log.info("Switched back to the default content")

                log.info(f"Returned data for the first frame: "
                         f"[{text}, {width}, {height}]")
                return [text, width, height]

        with allure.step("Check the 'Second' frame"):
            if frame_num == 2:
                with allure.step("Check if the 'Second' frame "
                                 "is presented on the 'Frames' page"):
                    frame = self.element_is_present(
                        self.locators.SECOND_FRAME)
                log.info("Second frame is presented in the DOM")

                with allure.step("Get width, height attributes "
                                 "of the 'Second' frame"):
                    width = frame.get_attribute("width")
                    height = frame.get_attribute("height")
                log.info(f"Second frame width, height: "
                         f"{width}, {height}")

                with allure.step("Switch to the 'Second' frame"):
                    self.go_to_frame(frame)
                log.info("Switched to the second frame")

                with allure.step("Get the 'Second' frame text result"):
                    text = self.element_is_present(
                        self.locators.TITLE_FRAME).text
                log.info(f"Presented text in the second frame: '{text}'")

                with allure.step("Switch back to the default content "
                                 "from the 'Second' frame"):
                    self.go_to_default_content()
                log.info("Switched back to the default content")

                log.info(f"Returned data for the second frame: "
                         f"[{text}, {width}, {height}]")
                return [text, width, height]
