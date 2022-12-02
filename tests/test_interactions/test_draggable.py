import allure

from pages.interactions_page.draggable_page import DraggablePage


@allure.suite("Interactions suite")
@allure.feature("Draggable page")
class TestDraggable:

    @allure.title(
        "Verify that the user has an opportunity "
        "to move draggable elements"
    )
    def test_simple_draggable(self, driver):
        draggable_page = DraggablePage(
            driver,
            "https://demoqa.com/dragabble"
        )
        draggable_page.open()
        before_position, after_position = \
            draggable_page.simple_drag_box()
        assert before_position != after_position, \
            f"\nActual result:" \
            f"\n\tThe position of the box has not been changed." \
            f"\n\tActual before and after positions: " \
            f"{before_position=}; " \
            f"{after_position=}" \
            f"\nExpected result:" \
            f"\n\tThe after and before positions should be different. " \
            f"\n\tSo, the position of the box has been successfully changed."
