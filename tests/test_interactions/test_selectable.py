from pages.interactions_page.selectable_page import SelectablePage


class TestSelectable:

    def test_selectable(self, driver):
        selectable_page = SelectablePage(driver, "https://demoqa.com/selectable")
        selectable_page.open()
        list_result = selectable_page.select_list_item()
        grid_result = selectable_page.select_grid_item()
        assert len(list_result) > 0, \
            f"\nActual result:\n\tItem was not selected.\n\tItem length: {list_result}" \
            f"\nExpected result:\n\tItem length should be more than 0. So, item was selected."

        assert len(grid_result) > 0, \
            f"\nActual result:\n\tItem was not selected.\n\tActual item length: {grid_result}" \
            f"\nExpected result:\n\tItem length should be more than 0. So, item was selected."
