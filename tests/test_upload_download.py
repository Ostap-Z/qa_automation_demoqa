from pages.upload_download_page import UploadAndDownloadPage


class TestUploadAndDownload:

    def test_upload_file(self, driver):
        upload_page = UploadAndDownloadPage(driver, "https://demoqa.com/upload-download")
        upload_page.open()

    def test_download_file(self, driver):
        download_page = UploadAndDownloadPage(driver, "https://demoqa.com/upload-download")
        download_page.open()
