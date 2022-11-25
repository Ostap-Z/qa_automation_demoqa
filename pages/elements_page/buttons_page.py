import allure

from pages.base_page import BasePage
from locators.elements_locators.buttons_locators import ButtonsPageLocators


class ButtonsPage(BasePage):
    locators = ButtonsPageLocators()

    @allure.step(
        "Click on different buttons"
    )
    def click_on_the_different_button(self, type_click):
        log = self.get_logger()

        with allure.step("Clicks on the 'double' button"):
            if type_click == "double":
                self.action_double_click(self.element_is_visible(
                    self.locators.DOUBLE_CLICK_BUTTON))
                log.info(f"Button {type_click} was pressed")
                return self.check_clicked_button(
                    self.locators.SUCCESS_DOUBLE_CLICK)

        with allure.step("Clicks on the 'right' button"):
            if type_click == "right":
                right_button = self.element_is_visible(
                    self.locators.RIGHT_CLICK_BUTTON)
                self.action_right_click(right_button)
                log.info(f"Button {type_click} was pressed")
                return self.check_clicked_button(
                    self.locators.SUCCESS_RIGHT_CLICK)

        with allure.step("Clicks on the 'left' button"):
            if type_click == "left":
                left_button = self.element_is_visible(
                    self.locators.LEFT_CLICK_BUTTON)
                self.go_to_element(left_button)
                left_button.click()
                log.info(f"Button {type_click} was pressed")
                return self.check_clicked_button(
                    self.locators.SUCCESS_LEFT_CLICK)

    @allure.step(
        "Check clicked button"
    )
    def check_clicked_button(self, element):
        log = self.get_logger()
        result = self.element_is_present(element).text
        log.info(f"Result text: {result}")
        return result
