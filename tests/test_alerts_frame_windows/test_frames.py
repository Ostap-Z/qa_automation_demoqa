import allure

from pages.alerts_frame_windows_page.frames_page import FramesPage


@allure.suite("Alerts, frames and windows suite")
@allure.feature("Frames page")
class TestFrames:

    @allure.title(
        "Verify that both frames are active on the 'Frames' page"
    )
    def test_frames(self, driver):
        frames_page = FramesPage(
            driver,
            "https://demoqa.com/frames"
        )
        frames_page.open()
        result_frame1 = frames_page.check_frame(1)
        result_frame2 = frames_page.check_frame(2)
        assert result_frame1 == ['This is a sample page',
                                 '500px',
                                 '350px'],\
            f"\nActual result: {result_frame1}"\
            "\nExpected result: " \
            "['This is a sample page', '500px', '350px']"

        assert result_frame2 == ['This is a sample page',
                                 '100px',
                                 '100px'], \
            f"\nActual result: {result_frame2}"\
            "\nExpected result: " \
            "['This is a sample page', '100px', '100px']"
