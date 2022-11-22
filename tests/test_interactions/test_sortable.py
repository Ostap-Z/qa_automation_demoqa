from pages.interactions_page.sortable_page import SortablePage


class TestSortable:

    def test_sortable(self, driver):
        sortable_page = SortablePage(
            driver,
            "https://demoqa.com/sortable"
        )
        sortable_page.open()
        list_order_before, list_order_after = \
            sortable_page.change_item_order("list")
        grid_order_before, grid_order_after = \
            sortable_page.change_item_order("grid")

        assert list_order_before != list_order_after, \
            f"\nActual result:" \
            f"\n\tSortable items were not changed." \
            f"\n\tSortable items order before: {list_order_before}" \
            f"\n\tSortable items order after: {list_order_after}" \
            f"\nExpected result:" \
            f"\n\tSortable items order before and after " \
            f"should be different. So, items order was changed"

        assert grid_order_before != grid_order_after, \
            f"\nActual result:" \
            f"\n\tSortable items were not changed." \
            f"\n\tSortable items order before: {grid_order_before}" \
            f"\n\tSortable items order after: {grid_order_after}" \
            f"\nExpected result:" \
            f"\n\tSortable items order before and after " \
            f"should be different. So, items order was changed"
