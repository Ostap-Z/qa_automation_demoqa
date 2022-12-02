import allure

from pages.alerts_frame_windows_page.frames_page import FramesPage


@allure.suite("Alerts, frames and windows suite")
@allure.feature("Frames page")
class TestFrames:

    @allure.title(
        "Verify that the 'First' frame "
        "is active on the 'Frames' page"
    )
    def test_first_frame(self, driver):
        frames_page = FramesPage(
            driver,
            "https://demoqa.com/frames"
        )
        frames_page.open()
        result_frame = frames_page.check_frame(1)
        assert result_frame == ['This is a sample page',
                                '500px',
                                '350px'],\
            f"\nActual result:" \
            f"\n\t{result_frame}"\
            "\nExpected result:" \
            "\n\t['This is a sample page', '500px', '350px']"

    @allure.title(
        "Verify that the 'Second' frame "
        "is active on the 'Frames' page"
    )
    def test_second_frame(self, driver):
        frames_page = FramesPage(
            driver,
            "https://demoqa.com/frames"
        )
        frames_page.open()
        result_frame = frames_page.check_frame(2)
        assert result_frame == ['This is a sample page',
                                '100px',
                                '100px'], \
            f"\nActual result:" \
            f"\n\t{result_frame}"\
            "\nExpected result:" \
            "\n\t['This is a sample page', '100px', '100px']"
