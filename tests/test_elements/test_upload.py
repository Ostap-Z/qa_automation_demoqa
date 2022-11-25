import allure

from pages.elements_page.upload_page import UploadPage


@allure.suite("Elements suite")
@allure.feature("Upload page")
class TestUpload:

    @allure.title(
        "Verify that the user has an opportunity to upload a file"
    )
    def test_upload_file(self, driver):
        upload_page = UploadPage(
            driver,
            "https://demoqa.com/upload-download"
        )
        upload_page.open()
        file_name = upload_page.upload_file()
        result = upload_page.get_uploaded_result()
        assert file_name == result, \
            f"\nActual result: {result}" \
            f"\nExpected result: {file_name}"
