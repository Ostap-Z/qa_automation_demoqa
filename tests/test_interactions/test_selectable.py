import allure

from pages.interactions_page.selectable_page import SelectablePage


@allure.suite("Interactions suite")
@allure.feature("Selectable page")
class TestSelectable:

    @allure.title(
        "Verify that the user has an opportunity "
        "to chose the 'List' selectable elements"
    )
    def test_list_selectable(self, driver):
        selectable_page = SelectablePage(
            driver,
            "https://demoqa.com/selectable"
        )
        selectable_page.open()
        list_result = selectable_page.select_list_item()
        assert len(list_result) > 0, \
            f"\nActual result:" \
            f"\n\tItem was not selected." \
            f"\n\tItem length: {list_result}" \
            f"\nExpected result:" \
            f"\n\tItem length should be more than 0. " \
            f"\n\tSo, item was selected."

    @allure.title(
        "Verify that the user has an opportunity "
        "to chose the 'Grid' selectable elements"
    )
    def test_grid_selectable(self, driver):
        selectable_page = SelectablePage(
            driver,
            "https://demoqa.com/selectable"
        )
        selectable_page.open()
        grid_result = selectable_page.select_grid_item()
        assert len(grid_result) > 0, \
            f"\nActual result:" \
            f"\n\tItem was not selected." \
            f"\n\tActual item length: {grid_result}" \
            f"\nExpected result:" \
            f"\n\tItem length should be more than 0. " \
            f"\n\tSo, item was selected."
