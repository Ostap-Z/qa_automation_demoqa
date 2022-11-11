from pages.interactions_page.resizable_page import ResizablePage


class TestResizable:

    def test_resizable(self, driver):
        resizable_page = ResizablePage(driver, "https://demoqa.com/resizable")
        resizable_page.open()
        max_large_box, min_large_box = resizable_page.change_size_large_resizable_box()
        max_resize, min_resize = resizable_page.change_size_small_resizable_box()
        assert ('500px', '300px') == max_large_box, \
            f"\nActual result\n\tMax large size is not equals to the expected." \
            f"\n\tActual max size: {max_large_box}" \
            f"\nExpected result:\n\tMax large size should equals to: ('500px', '300px')"

        assert ('150px', '150px') == min_large_box, \
            f"\nActual result\n\tMin large size is not equals to the expected." \
            f"\n\tActual min size: {min_large_box}" \
            f"\nExpected result:\n\tMin large size should equals to: ('150px', '150px')"

        assert max_resize != min_resize, \
            f"\nActual result:\n\tResize item has not been changed." \
            f"\n\tMax size: {max_resize}\n\tMin size: {min_resize}" \
            f"\nExpected result:\n\tResize min and max should be different. So, the user has been changed a resizable item."
