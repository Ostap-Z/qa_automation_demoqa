import allure

from pages.interactions_page.resizable_page import ResizablePage


@allure.suite("Interactions suite")
@allure.feature("Resizable page")
class TestResizable:

    @allure.title(
        "Verify that the user has an opportunity "
        "to resize 'Resizable' elements "
        "and their max, min size equals to the expected"
    )
    def test_resizable(self, driver):
        resizable_page = ResizablePage(
            driver,
            "https://demoqa.com/resizable"
        )
        resizable_page.open()
        max_large_box, min_large_box = \
            resizable_page.change_size_large_resizable_box()
        max_resize, min_resize = \
            resizable_page.change_size_small_resizable_box()

        assert ('500px', '300px') == max_large_box, \
            f"\nActual result:" \
            f"\n\tMax large size is not equals to the expected." \
            f"\n\tActual max size: {max_large_box}" \
            f"\nExpected result:" \
            f"\n\tMax large size should equals to: ('500px', '300px')"

        assert ('150px', '150px') == min_large_box, \
            f"\nActual result:" \
            f"\n\tMin large size is not equals to the expected." \
            f"\n\tActual min size: {min_large_box}" \
            f"\nExpected result:" \
            f"\n\tMin large size should equals to: ('150px', '150px')"

        assert max_resize != min_resize, \
            f"\nActual result:" \
            f"\n\tResize item has not been changed." \
            f"\n\tMax size: {max_resize}" \
            f"\n\tMin size: {min_resize}" \
            f"\nExpected result:" \
            f"\n\tResize min and max should be different. " \
            f"So, the user has been changed a resizable item."
