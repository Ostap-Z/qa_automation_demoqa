import allure

from pages.elements_page.download_page import DownloadPage


@allure.suite("Elements suite")
@allure.feature("Download page")
class TestDownload:

    @allure.title("Check download a file")
    def test_download(self, driver):
        download_page = DownloadPage(
            driver,
            "https://demoqa.com/upload-download"
        )
        download_page.open()
        result = download_page.download_file()
        assert result is True, \
            "The file has not been downloaded"
