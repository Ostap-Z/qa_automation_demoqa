import allure

from pages.alerts_frame_windows_page.nested_frames_page import NestedFramesPage


@allure.suite("Alerts, frames and windows suite")
@allure.feature("Nested Frames page")
class TestNestedFrames:

    @allure.title(
        "Verify that nested frames are active "
        "on the 'Nested Frames' page "
        "and frame text equals to the expected result"
    )
    def test_nested_frames(self, driver):
        nested_frames_page = NestedFramesPage(
            driver,
            "https://demoqa.com/nestedframes"
        )
        nested_frames_page.open()
        parent_text, child_text = \
            nested_frames_page.check_nested_frame()
        assert parent_text == "Parent frame", \
            f"Actual result:" \
            f"\n\tThe 'Parent' frame text is '{parent_text}'"\
            "\nExpected result: " \
            "\n\tThe 'Parent' frame text should be 'Parent frame'"

        assert child_text == "Child Iframe", \
            f"\nActual result:" \
            f"\n\tThe 'Child' frame text is '{child_text}'"\
            "\nExpected result: " \
            "\n\tThe 'Child' frame text should be 'Child Iframe'"
