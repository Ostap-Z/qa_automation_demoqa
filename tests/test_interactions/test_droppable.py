from pages.interactions_page.droppable_page import DroppablePage


class TestDroppable:

    def test_simple_droppable(self, driver):
        droppable_page = DroppablePage(
            driver,
            "https://demoqa.com/droppable"
        )
        droppable_page.open()
        drop_text_result = droppable_page.drop_simple()
        assert drop_text_result == "Dropped!", \
            f"\nActual result:\n\t" \
            f"Item has not been dropped." \
            f"\n\tActual drop text: {drop_text_result}" \
            f"\nExpected result:" \
            f"\n\tActual drop text should be 'Dropped!'. " \
            f"So, the item was successfully dropped."

    def test_accept_droppable(self, driver):
        droppable_page = DroppablePage(
            driver,
            "https://demoqa.com/droppable"
        )
        droppable_page.open()
        drop_text_not_acceptable, drop_text_acceptable = \
            droppable_page.drop_accept()
        assert drop_text_not_acceptable == "Drop here", \
            f"\nActual result:\n\t" \
            f"Actual not acceptable text result: " \
            f"{drop_text_not_acceptable}" \
            f"\nExpected result:\n\t" \
            f"Expected not acceptable " \
            f"text result should be: Drop here"

        assert drop_text_acceptable == "Dropped!", \
            f"\nActual result:" \
            f"\n\tActual acceptable text result: " \
            f"{drop_text_acceptable}" \
            f"\nExpected result:\n\t" \
            f"Expected acceptable text result should be: Dropped!"

    def test_prevent_propogation_droppable(self, driver):
        droppable_page = DroppablePage(
            driver,
            "https://demoqa.com/droppable"
        )
        droppable_page.open()
        text_not_greedy_box, text_not_greedy_inner_box, \
        text_greedy_box, text_greedy_inner_box = \
            droppable_page.drop_prevent_propogation()

        assert text_not_greedy_box == "Dropped!", \
            f"\nActual result:" \
            f"\n\tA text has not been changed." \
            f"\n\tActual text: {text_not_greedy_box}" \
            f"\nExpected result:" \
            f"\n\tA text should be changed." \
            f"\n\tExpected text: Dropped!"

        assert text_not_greedy_inner_box == "Dropped!", \
            f"\nActual result:" \
            f"\n\tA text has not been changed." \
            f"\n\tActual text: {text_not_greedy_inner_box}" \
            f"\nExpected result:" \
            f"\n\tA text should be changed." \
            f"\n\tExpected text: Dropped!"

        assert text_greedy_box == "Outer droppable", \
            f"\nActual result:" \
            f"\n\tA text is not equal to expected." \
            f"\n\tActual text: {text_greedy_box}" \
            f"\nExpected result:" \
            f"\n\tExpected text: Outer droppable"

        assert text_greedy_inner_box == "Dropped!", \
            f"\nActual result:" \
            f"\n\tA text has not been changed." \
            f"\n\tActual text: {text_greedy_inner_box}" \
            f"\nExpected result:" \
            f"\n\tA text should be changed." \
            f"\n\tExpected text: Outer droppable"

    def test_revert_draggable_droppable(self, driver):
        droppable_page = DroppablePage(
            driver,
            "https://demoqa.com/droppable"
        )
        droppable_page.open()
        will_after_move, will_after_revert = \
            droppable_page.drop_revert_draggable("will_revert")
        not_will_after_move, not_will_after_revert = \
            droppable_page.drop_revert_draggable("not_will_revert")
        assert will_after_move != will_after_revert, \
            f"\nActual result:" \
            f"\n\tPositions after move and after revert are equal." \
            f"\n\tActual positions after_move, after_revert: " \
            f"{will_after_move}, {will_after_revert}" \
            f"\nExpected result:" \
            f"\n\tPositions after move and after revert" \
            f" should not be equaled."

        assert not_will_after_move == not_will_after_revert, \
            f"\nActual result:" \
            f"\n\tPositions after move and after revert " \
            f"are not equal." \
            f"\n\tActual positions after_move, after_revert: " \
            f"{not_will_after_move}, {not_will_after_revert}" \
            f"\nExpected result:" \
            f"\n\tPositions after move and after revert " \
            f"should be equaled."
