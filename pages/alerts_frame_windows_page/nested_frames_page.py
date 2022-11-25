import allure

from pages.base_page import BasePage
from locators.alerts_frame_windows_locators.nested_frames_locators import NestedFramesLocators


class NestedFramesPage(BasePage):
    locators = NestedFramesLocators()

    @allure.step("Check the 'Nested' frames")
    def check_nested_frame(self):
        log = self.get_logger()

        with allure.step("Check if the 'Parent' frame is presented "
                         "on the 'Nested Frames' page"):
            parent_frame = self.element_is_present(
                self.locators.PARENT_FRAME)
        log.info("Parent frame is presented in the DOM")

        with allure.step("Switch to the 'Parent' frame"):
            self.go_to_frame(parent_frame)
        log.info("Went to the parent frame")

        with allure.step("Get a text from the 'Parent' frame"):
            parent_text = self.element_is_present(
                self.locators.PARENT_TEXT).text
        log.info(f"Taken parent text: '{parent_text}'")

        with allure.step("Check if the 'Child' frame is presented "
                         "on the 'Nested Frames' page"):
            child_frame = self.element_is_present(
                self.locators.CHILD_FRAME)
        log.info("Child frame is presented in the DOM")

        with allure.step("Switch to the 'Child' frame"):
            self.go_to_frame(child_frame)
        log.info("Went to the child frame")

        with allure.step("Get a text from the 'Child' frame"):
            child_text = self.element_is_present(
                self.locators.CHILD_TEXT).text
        log.info(f"Taken child text: '{child_text}'")

        log.info(f"Returned texts for parent_frame, child_frame: "
                 f"'{parent_text}', '{child_text}'")
        return parent_text, child_text
