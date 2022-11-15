from pages.interactions_page.droppable_page import DroppablePage


class TestDroppable:

    def test_simple_droppable(self, driver):
        droppable_page = DroppablePage(driver, "https://demoqa.com/droppable")
        droppable_page.open()
        drop_text_result = droppable_page.drop_simple()
        assert drop_text_result == "Dropped!", \
            f"\nActual result:\n\tItem has not been dropped.\n\tActual drop text: {drop_text_result}" \
            f"\nExpected result:\n\tActual drop text should be 'Dropped!'. So, the item was successfully dropped."

