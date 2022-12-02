import allure

from pages.elements_page.links_page import LinksPage


@allure.suite("Elements suite")
@allure.feature("Links page")
class TestLinks:

    @allure.title(
        "Verify that new tab opens with correct url"
    )
    def test_check_link(self, driver):
        links_page = LinksPage(
            driver,
            "https://demoqa.com/links"
        )
        links_page.open()
        href_link, current_url = \
            links_page.check_new_tab_simple_link()
        assert href_link == current_url, \
            "\nActual result:" \
            f"\n\t{current_url}" \
            "\nExpected result:" \
            f"\n\t{href_link}"

    @allure.title(
        "Verify that a response code of the "
        "'Broken Link' is 400"
    )
    def test_broken_link(self, driver):
        links_page = LinksPage(
            driver,
            "https://demoqa.com/links"
        )
        links_page.open()
        response_code = links_page.check_broken_link(
            "https://demoqa.com/bad-request")
        assert response_code == 400, \
            f"\nActual result:" \
            f"\n\tStatus code is {response_code}" \
            f"\nExpected result:" \
            f"\n\tStatus code should be 400"
