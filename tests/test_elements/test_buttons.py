import allure

from pages.elements_page.buttons_page import ButtonsPage


@allure.suite("Elements suite")
@allure.feature("Buttons page")
class TestButtons:

    @allure.title(
        "Verify that the user has an opportunity "
        "to click the 'Double Click Me' button"
    )
    def test_double_click_on_the_button(self, driver):
        buttons_page = ButtonsPage(
            driver,
            "https://demoqa.com/buttons"
        )
        buttons_page.open()
        double_click = \
            buttons_page.click_on_the_different_button('double')
        assert double_click == "You have done a double click", \
            "\nActual result:" \
            "\n\tThe 'Double Click Me' button is not pressed." \
            "\nExpected result:" \
            "\n\tThe 'Double Click Me' button span text result " \
            f"when button was pressed should be {double_click}"

    @allure.title(
        "Verify that the user has an opportunity "
        "to click the 'Right Click Me' button"
    )
    def test_right_click_on_the_button(self, driver):
        buttons_page = ButtonsPage(
            driver,
            "https://demoqa.com/buttons"
        )
        buttons_page.open()
        right_click = \
            buttons_page.click_on_the_different_button('right')
        assert right_click == "You have done a right click", \
            "\nActual result:" \
            "\n\tThe 'Right Click Me' button is not pressed." \
            "\nExpected result:" \
            "\n\tThe 'Right Click Me' button span text result " \
            f"when button was pressed should be {right_click}"

    @allure.title(
        "Verify that the user has an opportunity "
        "to click the 'Click Me' button"
    )
    def test_left_click_on_the_button(self, driver):
        buttons_page = ButtonsPage(
            driver,
            "https://demoqa.com/buttons"
        )
        buttons_page.open()
        left_click = \
            buttons_page.click_on_the_different_button('left')
        assert left_click == "You have done a dynamic click", \
            "\nActual result:" \
            "\n\tThe 'Click Me' button is not pressed." \
            "\nExpected result:" \
            "\n\tThe 'Click Me' button span text result " \
            f"when button was pressed should be {left_click}"
