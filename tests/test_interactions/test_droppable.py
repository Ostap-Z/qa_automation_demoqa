import allure

from pages.interactions_page.droppable_page import DroppablePage


@allure.suite("Interactions suite")
@allure.feature("Droppable page")
class TestDroppable:

    @allure.title(
        "Verify that the user has an opportunity to "
        "drag and drop the 'Simple' droppable item"
    )
    def test_simple_droppable(self, driver):
        droppable_page = DroppablePage(
            driver,
            "https://demoqa.com/droppable"
        )
        droppable_page.open()
        drop_text_result = droppable_page.drop_simple()
        assert drop_text_result == "Dropped!", \
            f"\nActual result:" \
            f"\n\tItem has not been dropped." \
            f"\n\tActual drop text: {drop_text_result}" \
            f"\nExpected result:" \
            f"\n\tActual drop text should be 'Dropped!'. " \
            f"\n\tSo, the item was successfully dropped."

    @allure.title(
        "Verify that droppable item doesn't react "
        "to the 'Not Acceptable' draggable item"
    )
    def test_not_acceptable_droppable(self, driver):
        droppable_page = DroppablePage(
            driver,
            "https://demoqa.com/droppable"
        )
        droppable_page.open()
        drop_text_not_acceptable = droppable_page.drop_accept(
            "not acceptable"
        )
        assert drop_text_not_acceptable == "Drop here", \
            f"\nActual result:" \
            f"\n\tActual not acceptable text result: " \
            f"{drop_text_not_acceptable}" \
            f"\nExpected result:" \
            f"\n\tText result should be: Drop here"

    @allure.title(
        "Verify that droppable item reacts "
        "to the 'Acceptable' draggable item"
    )
    def test_acceptable_droppable(self, driver):
        droppable_page = DroppablePage(
            driver,
            "https://demoqa.com/droppable"
        )
        droppable_page.open()
        drop_text_acceptable = droppable_page.drop_accept(
            "acceptable"
        )
        assert drop_text_acceptable == "Dropped!", \
            f"\nActual result:" \
            f"\n\tActual acceptable text result: " \
            f"{drop_text_acceptable}" \
            f"\nExpected result:" \
            f"\n\tText result should be: Dropped!"

    @allure.title(
        "Verify that the 'Not Greedy' inner "
        "and outer boxes are marked as dropped "
        "when the user drags the draggable item "
        "and drops to the 'Not Greedy Inner' item"
    )
    def test_not_greedy_prevent_propogation_droppable(self, driver):
        droppable_page = DroppablePage(
            driver,
            "https://demoqa.com/droppable"
        )
        droppable_page.open()
        text_not_greedy_box, text_not_greedy_inner_box = \
            droppable_page.drop_prevent_propogation("not greedy")
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

    @allure.title(
        "Verify that the 'Greedy' inner "
        "and outer boxes are marked as dropped "
        "those items that the user dragged and dropped a item"
    )
    def test_greedy_prevent_propogation_droppable(self, driver):
        droppable_page = DroppablePage(
            driver,
            "https://demoqa.com/droppable"
        )
        droppable_page.open()
        text_greedy_box, text_greedy_inner_box = \
            droppable_page.drop_prevent_propogation("greedy")
        assert text_greedy_box == "Outer droppable", \
            "\nActual result:" \
            "\n\tA text is not equal to expected." \
            f"\n\tActual text: {text_greedy_box}" \
            "\nExpected result:" \
            "\n\tExpected text: Outer droppable"

        assert text_greedy_inner_box == "Dropped!", \
            "\nActual result:" \
            "\n\tA text has not been changed." \
            f"\n\tActual text: {text_greedy_inner_box}" \
            "\nExpected result:" \
            "\n\tA text should be changed." \
            "\n\tExpected text: Outer droppable"

    @allure.title(
        "Verify that the 'Will Revert' draggable item "
        "reverts to the start position after move"
    )
    def test_revert_draggable_droppable(self, driver):
        droppable_page = DroppablePage(
            driver,
            "https://demoqa.com/droppable"
        )
        droppable_page.open()
        will_after_move, will_after_revert = \
            droppable_page.drop_revert_draggable("will_revert")
        assert will_after_move != will_after_revert, \
            "\nActual result:" \
            "\n\tPositions after move and after revert are equal." \
            "\n\tActual positions after_move, after_revert: " \
            f"{will_after_move}, {will_after_revert}" \
            "\nExpected result:" \
            "\n\tPositions after move and after revert" \
            " should not be equaled."

    @allure.title(
        "Verify that the 'Not Revert' draggable item "
        "still located in the droppable item after a move"
    )
    def test_not_revert_draggable_droppable(self, driver):
        droppable_page = DroppablePage(
            driver,
            "https://demoqa.com/droppable"
        )
        droppable_page.open()
        not_will_after_move, not_will_after_revert = \
            droppable_page.drop_revert_draggable("not_will_revert")
        assert not_will_after_move == not_will_after_revert, \
            "\nActual result:" \
            "\n\tPositions after move " \
            "and after revert are not equal." \
            "\n\tActual positions after_move, after_revert: " \
            f"{not_will_after_move}, {not_will_after_revert}" \
            "\nExpected result:" \
            "\n\tPositions after move and after revert " \
            "should be equaled."
