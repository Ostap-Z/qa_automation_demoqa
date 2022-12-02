import allure

from pages.elements_page.download_page import DownloadPage


@allure.suite("Elements suite")
@allure.feature("Download page")
class TestDownload:

    @allure.title(
        "Verify that the user has an opportunity "
        "to download a file"
    )
    def test_download(self, driver):
        download_page = DownloadPage(
            driver,
            "https://demoqa.com/upload-download"
        )
        download_page.open()
        result = download_page.download_file()
        assert result is True, \
            "\nActual result:" \
            "\n\tThe file has not been downloaded" \
            "\nExpected result:" \
            "\n\tThe user should has an opportunity " \
            "to download a file"
