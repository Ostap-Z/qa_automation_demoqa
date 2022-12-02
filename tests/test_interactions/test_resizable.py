import allure

from pages.interactions_page.resizable_page import ResizablePage


@allure.suite("Interactions suite")
@allure.feature("Resizable page")
class TestResizable:

    @allure.title(
        "Verify that the user has an opportunity "
        "to resize the 'Large' resizable item "
        "to their max, min positions "
        "and they are equal to the expected"
    )
    def test_range_large_resizable(self, driver):
        resizable_page = ResizablePage(
            driver,
            "https://demoqa.com/resizable"
        )
        resizable_page.open()
        max_large_box, min_large_box = \
            resizable_page.change_size_large_resizable_box()
        assert ('500px', '300px') == max_large_box \
               and ('150px', '150px') == min_large_box, \
               "\nActual result:" \
               "\n\tA range of the 'Large' resizable item " \
               "is not equals to the expected." \
               f"\n\tActual max size: {max_large_box}" \
               f"\n\tActual min size: {min_large_box}" \
               "\nExpected result:" \
               "\n\tMax range should equals to: " \
               "('500px', '300px')" \
               "\n\tMin range should equals to: " \
               "('150px', '150px')"

    @allure.title(
        "Verify that the user has an opportunity "
        "to resize the 'Small' resizable item"
    )
    def test_resize_small_resizable(self, driver):
        resizable_page = ResizablePage(
            driver,
            "https://demoqa.com/resizable"
        )
        resizable_page.open()
        stretched_size, pulled_size = \
            resizable_page.change_size_small_resizable_box()
        assert stretched_size != pulled_size, \
            "\nActual result:" \
            "\n\tThe 'Small' resizable item has not been changed." \
            "\n\tStretched_size, pulled_size values: " \
            f"{stretched_size}, {pulled_size}" \
            f"\nExpected result:" \
            f"\n\tThe stretched_size and pulled_size " \
            f"should not be the same." \
            f"\n\tSo, the 'Small' resizable item has been changed"
