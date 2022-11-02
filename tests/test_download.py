from pages.download_page import DownloadPage


class TestDownload:

    def test_download(self, driver):
        download_page = DownloadPage(driver, "https://demoqa.com/upload-download")
        download_page.open()
        result = download_page.download_file()
        assert result is True, "The file has not been downloaded"
