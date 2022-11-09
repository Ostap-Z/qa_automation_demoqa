from pages.widgets_page.menu_page import MenuPage


class TestMenu:

    def test_menu(self, driver):
        menu_page = MenuPage(driver, "https://demoqa.com/menu#")
        menu_page.open()
        data = menu_page.check_menu()
        expected_result = ['Main Item 1',
                           'Main Item 2',
                           'Sub Item',
                           'Sub Item',
                           'SUB SUB LIST »',
                           'Sub Sub Item 1',
                           'Sub Sub Item 2',
                           'Main Item 3']
        assert data == expected_result,