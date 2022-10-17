from pages.base_page import BasePage
from locators.buttons_locators import ButtonsPageLocators


class ButtonsPage(BasePage):
    locators = ButtonsPageLocators()

    def click_on_the_different_button(self, type_click):
        if type_click == "double":
            self.action_double_click(self.element_is_visible(self.locators.DOUBLE_CLICK_BUTTON))
            return self.check_clicked_button(self.locators.SUCCESS_DOUBLE_CLICK)

        if type_click == "right":
            self.action_right_click(self.element_is_visible(self.locators.RIGHT_CLICK_BUTTON))
            return self.check_clicked_button(self.locators.SUCCESS_RIGHT_CLICK)

        if type_click == "left":
            self.element_is_visible(self.locators.LEFT_CLICK_BUTTON).click()
            return self.check_clicked_button(self.locators.SUCCESS_LEFT_CLICK)

    def check_clicked_button(self, element):
        return self.element_is_present(element).text
