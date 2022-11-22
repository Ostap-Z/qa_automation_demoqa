from pages.elements_page.upload_page import UploadPage


class TestUpload:

    def test_upload_file(self, driver):
        upload_page = UploadPage(
            driver,
            "https://demoqa.com/upload-download"
        )
        upload_page.open()
        file_name, result = upload_page.upload_file()
        assert file_name == result, \
            f"\nActual result: {result}" \
            f"\nExpected result: {file_name}"
