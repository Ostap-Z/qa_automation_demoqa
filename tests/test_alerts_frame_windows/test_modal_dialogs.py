import allure

from pages.alerts_frame_windows_page.modal_dialogs_page import ModalDialogsPage


@allure.suite("Alerts, frames and windows suite")
@allure.feature("Alerts page")
class TestModalDialogs:

    @allure.title(
        "Verify that the user has an opportunity to "
        "open the 'Small' modal dialog and see a text there"
    )
    def test_small_modal_dialog(self, driver):
        modal_dialogs_page = ModalDialogsPage(
            driver,
            "https://demoqa.com/modal-dialogs"
        )
        modal_dialogs_page.open()
        small_modal = modal_dialogs_page.check_small_modal_dialog()
        assert small_modal[0] == "Small Modal", \
            f"Actual result: " \
            f"small modal title is '{small_modal[0]}'"\
            "Expected result: " \
            "small modal title should be 'Small Modal'"

        assert small_modal[1] > 0, \
            f"Actual result: small modal text length is " \
            f"'{small_modal[1]}'"\
            "Expected result: small modal text length should be > 0"

    @allure.title(
        "Verify that the user has an opportunity to "
        "open the 'Large' modal dialog and see a text there"
    )
    def test_large_modal_dialog(self, driver):
        modal_dialogs_page = ModalDialogsPage(
            driver,
            "https://demoqa.com/modal-dialogs"
        )
        modal_dialogs_page.open()
        large_modal = modal_dialogs_page.check_large_modal_dialog()

        assert large_modal[0] == "Large Modal", \
            f"Actual result: " \
            f"large modal title is '{large_modal[0]}'"\
            "Expected result: " \
            "large modal title should be 'Large Modal'"

        assert large_modal[1] > 0, \
            f"Actual result: " \
            f"large modal text length is '{large_modal[1]}'"\
            "Expected result: " \
            "large modal text length should be > 0"
