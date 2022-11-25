import allure

from pages.elements_page.buttons_page import ButtonsPage


@allure.suite("Elements suite")
@allure.feature("Buttons page")
class TestButtons:

    @allure.title(
        "Verify that the user has an opportunity "
        "to do action with each button presented "
        "on the 'Buttons' page"
    )
    def test_different_click_on_the_buttons(self, driver):
        buttons_page = ButtonsPage(
            driver,
            "https://demoqa.com/buttons"
        )
        buttons_page.open()
        double_click = \
            buttons_page.click_on_the_different_button('double')
        right_click = \
            buttons_page.click_on_the_different_button('right')
        left_click = \
            buttons_page.click_on_the_different_button('left')

        assert double_click == "You have done a double click", \
                               "The double click button is not pressed"

        assert right_click == "You have done a right click", \
                              "The right click button is not pressed"

        assert left_click == "You have done a dynamic click", \
                             "The left click button is not pressed"
