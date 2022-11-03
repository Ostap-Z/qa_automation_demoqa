from pages.base_page import BasePage
from locators.buttons_locators import ButtonsPageLocators


class ButtonsPage(BasePage):
    locators = ButtonsPageLocators()

    def click_on_the_different_button(self, type_click):
        log = self.get_logger()
        if type_click == "double":
            self.action_double_click(self.element_is_visible(self.locators.DOUBLE_CLICK_BUTTON))
            log.info(f"Button {type_click} was pressed")
            return self.check_clicked_button(self.locators.SUCCESS_DOUBLE_CLICK)

        if type_click == "right":
            right_button = self.element_is_visible(self.locators.RIGHT_CLICK_BUTTON)
            self.action_right_click(right_button)
            # self.action_right_click(self.element_is_visible(self.locators.RIGHT_CLICK_BUTTON))
            log.info(f"Button {type_click} was pressed")
            return self.check_clicked_button(self.locators.SUCCESS_RIGHT_CLICK)

        if type_click == "left":
            left_button = self.element_is_visible(self.locators.LEFT_CLICK_BUTTON)
            self.go_to_element(left_button)
            left_button.click()
            log.info(f"Button {type_click} was pressed")
            return self.check_clicked_button(self.locators.SUCCESS_LEFT_CLICK)

    def check_clicked_button(self, element):
        log = self.get_logger()
        result = self.element_is_present(element).text
        log.info(f"Result text: {result}")
        return result
