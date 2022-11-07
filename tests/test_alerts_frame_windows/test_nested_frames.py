from pages.alerts_frame_windows_page.nested_frames_page import NestedFramesPage


class TestNestedFrames:

    def test_nested_frames(self, driver):
        nested_frames_page = NestedFramesPage(driver, "https://demoqa.com/nestedframes")
        nested_frames_page.open()
        parent_text, child_text = nested_frames_page.check_nested_frame()
        assert parent_text == "Parent frame", f"Actual result: parent frame text is '{parent_text}'"\
                                              "Expected result: parent frame text should be 'Parent frame'"
        assert child_text == "Child Iframe", f"Actual result: parent frame text is '{child_text}'"\
                                             "Expected result: parent frame text should be 'Child Iframe'"
