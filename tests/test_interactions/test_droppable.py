from pages.interactions_page.droppable_page import DroppablePage


class TestDroppable:

    def test_simple_droppable(self, driver):
        droppable_page = DroppablePage(driver, "https://demoqa.com/droppable")
        droppable_page.open()
        drop_text_result = droppable_page.drop_simple()
        assert drop_text_result == "Dropped!", \
            f"\nActual result:\n\tItem has not been dropped.\n\tActual drop text: {drop_text_result}" \
            f"\nExpected result:\n\tActual drop text should be 'Dropped!'. So, the item was successfully dropped."

    def test_accept_droppable(self, driver):
        droppable_page = DroppablePage(driver, "https://demoqa.com/droppable")
        droppable_page.open()
        drop_text_not_acceptable, drop_text_acceptable = droppable_page.drop_accept()
        assert drop_text_not_acceptable == "Drop here", \
            f"\nActual result:\n\tActual not acceptable text result: {drop_text_not_acceptable}" \
            f"\nExpected result:\n\tExpected not acceptable text result should be: Drop here"

        assert drop_text_acceptable == "Dropped!", \
            f"\nActual result:\n\tActual acceptable text result: {drop_text_acceptable}" \
            f"\nExpected result:\n\tExpected acceptable text result should be: Dropped!"
