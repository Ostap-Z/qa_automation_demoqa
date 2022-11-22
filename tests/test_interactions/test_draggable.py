from pages.interactions_page.draggable_page import DraggablePage


class TestDraggable:

    def test_simple_draggable(self, driver):
        draggable_page = DraggablePage(
            driver,
            "https://demoqa.com/dragabble"
        )
        draggable_page.open()
        before_position, after_position = \
            draggable_page.simple_drag_box()
        assert before_position != after_position, \
            f"\nActual result:\n\t" \
            f"The position of the box has not been changed." \
            f"\n\tActual before and after positions: " \
            f"{before_position=}; " \
            f"{after_position=}" \
            f"\nExpected result:\n\t" \
            f"The after and before positions should be different. " \
            f"So, the position of the box has been successfully changed."
