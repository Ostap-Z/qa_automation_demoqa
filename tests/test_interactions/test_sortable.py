import allure

from pages.interactions_page.sortable_page import SortablePage


@allure.suite("Interactions suite")
@allure.feature("Sortable page")
class TestSortable:

    @allure.title(
        "Verify that the user has an opportunity "
        "to change an order of the 'Sortable' elements"
    )
    def test_list_sortable(self, driver):
        sortable_page = SortablePage(
            driver,
            "https://demoqa.com/sortable"
        )
        sortable_page.open()
        list_order_before, list_order_after = \
            sortable_page.change_item_order("list")
        assert list_order_before != list_order_after, \
            f"\nActual result:" \
            f"\n\tSortable items were not changed." \
            f"\n\tSortable items order before: {list_order_before}" \
            f"\n\tSortable items order after: {list_order_after}" \
            f"\nExpected result:" \
            f"\n\tSortable items order before and after " \
            f"should be different. So, items order was changed"

    @allure.title(
        "Verify that the user has an opportunity "
        "to change an order of the 'Grid' sortable elements"
    )
    def test_grid_sortable(self, driver):
        sortable_page = SortablePage(
            driver,
            "https://demoqa.com/sortable"
        )
        sortable_page.open()
        grid_order_before, grid_order_after = \
            sortable_page.change_item_order("grid")
        assert grid_order_before != grid_order_after, \
            f"\nActual result:" \
            f"\n\tSortable items were not changed." \
            f"\n\tSortable items order before: {grid_order_before}" \
            f"\n\tSortable items order after: {grid_order_after}" \
            f"\nExpected result:" \
            f"\n\tSortable items order before and after " \
            f"should be different. So, items order was changed"
