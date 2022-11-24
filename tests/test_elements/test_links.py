import allure

from pages.elements_page.links_page import LinksPage


@allure.suite("Elements suite")
@allure.feature("Links page")
class TestLinks:

    @allure.title("Check simple link")
    def test_check_link(self, driver):
        links_page = LinksPage(
            driver,
            "https://demoqa.com/links"
        )
        links_page.open()
        href_link, current_url = \
            links_page.check_new_tab_simple_link()
        assert href_link == current_url, \
            f"\nActual result: {current_url}" \
            f"\nExpected result: {href_link}"

    @allure.title("Check broken link")
    def test_broken_link(self, driver):
        links_page = LinksPage(
            driver,
            "https://demoqa.com/links"
        )
        links_page.open()
        response_code = links_page.check_broken_link(
            "https://demoqa.com/bad-request")
        assert response_code == 400, \
            f"Actual result: {response_code}" \
            f"Expected result: 400"
