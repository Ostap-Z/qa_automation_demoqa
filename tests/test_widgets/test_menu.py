from pages.widgets_page.menu_page import MenuPage


class TestMenu:

    def test_menu(self, driver):
        menu_page = MenuPage(
            driver,
            "https://demoqa.com/menu#"
        )
        menu_page.open()
        result = menu_page.check_menu()
        expected_result = ['Main Item 1',
                           'Main Item 2',
                           'Sub Item',
                           'Sub Item',
                           'SUB SUB LIST »',
                           'Sub Sub Item 1',
                           'Sub Sub Item 2',
                           'Main Item 3']
        assert result == expected_result, \
            f"\nActual result:" \
            f"\n\tNav items: {result}" \
            f"\nExpected result:" \
            f"\n\tNav items should be: {expected_result}"
