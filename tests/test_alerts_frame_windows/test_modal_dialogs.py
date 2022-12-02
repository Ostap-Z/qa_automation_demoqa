import allure

from pages.alerts_frame_windows_page.modal_dialogs_page import ModalDialogsPage


@allure.suite("Alerts, frames and windows suite")
@allure.feature("Alerts page")
class TestModalDialogs:

    @allure.title(
        "Verify that the user has an opportunity to "
        "get a correct title name of the 'Small' modal dialog"
    )
    def test_title_small_modal_dialog(self, driver):
        modal_dialogs_page = ModalDialogsPage(
            driver,
            "https://demoqa.com/modal-dialogs"
        )
        modal_dialogs_page.open()
        small_modal = modal_dialogs_page.check_small_modal_dialog()
        assert small_modal[0] == "Small Modal", \
            f"\nActual result:" \
            f"\n\tThe 'Small' modal title is '{small_modal[0]}'"\
            "\nExpected result:" \
            "\n\tThe 'Small' modal title should be 'Small Modal'"

    @allure.title(
        "Verify that the user has an opportunity to "
        "get a content of the 'Small' modal dialog"
    )
    def test_content_small_modal_dialog(self, driver):
        modal_dialogs_page = ModalDialogsPage(
            driver,
            "https://demoqa.com/modal-dialogs"
        )
        modal_dialogs_page.open()
        small_modal = modal_dialogs_page.check_small_modal_dialog()
        assert small_modal[1] > 0, \
            f"\nActual result:" \
            f"\n\tThe 'Small' modal dialog content length is " \
            f"{small_modal[1]}'"\
            "\nExpected result:" \
            "\n\tThe 'Small' modal dialog content " \
            "length should be > 0"





    @allure.title(
        "Verify that the user has an opportunity to "
        "get a correct title name of the 'Large' modal dialog"
    )
    def test_title_large_modal_dialog(self, driver):
        modal_dialogs_page = ModalDialogsPage(
            driver,
            "https://demoqa.com/modal-dialogs"
        )
        modal_dialogs_page.open()
        large_modal = modal_dialogs_page.check_large_modal_dialog()
        assert large_modal[0] == "Large Modal", \
            f"\nActual result:" \
            f"\n\tThe 'Large' modal title is '{large_modal[0]}'"\
            "\nExpected result:" \
            "\n\tThe 'Large' modal title should be 'Large Modal'"

    @allure.title(
        "Verify that the user has an opportunity to "
        "get a content of the 'Large' modal dialog"
    )
    def test_content_large_modal_dialog(self, driver):
        modal_dialogs_page = ModalDialogsPage(
            driver,
            "https://demoqa.com/modal-dialogs"
        )
        modal_dialogs_page.open()
        large_modal = modal_dialogs_page.check_large_modal_dialog()
        assert large_modal[1] > 0, \
            f"\nActual result:" \
            f"\n\tThe 'Large' modal content length is '{large_modal[1]}'"\
            "\nExpected result:" \
            "\n\tThe 'Large' modal content length should be > 0"
