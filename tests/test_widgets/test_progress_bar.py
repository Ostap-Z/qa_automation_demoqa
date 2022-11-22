from pages.widgets_page.progress_bar_page import ProgressBarPage


class TestProgressBar:

    def test_progress_bar(self, driver):
        progress_bar_page = ProgressBarPage(
            driver,
            "https://demoqa.com/progress-bar"
        )
        progress_bar_page.open()
        progress_bar_value_before, progress_bar_value_after = \
            progress_bar_page.change_progress_bar_value()
        assert int(progress_bar_value_before) \
               < int(progress_bar_value_after), \
               f"\nActual result:" \
               f"\n\tThe progress bar was not changed."\
               f"\n\tProgress bar before value: " \
               f"{progress_bar_value_before}" \
               f"\n\tProgress bar after value: " \
               f"{progress_bar_value_after}"\
               f"\nExpected result:" \
               f"\n\tThe progress bar should change a value. " \
               f"So, progress bar after value " \
               f"should be more than before."
