import allure

from pages.widgets_page.accordian_page import AccordianPage


@allure.suite("Widgets suite")
@allure.feature("Accordian page")
class TestAccordian:

    @allure.title(
        "Verify that the 'What is Lorem Ipsum?' "
        "accordian title is equal to the expected "
    )
    def test_first_title_accordian(self, driver):
        accordian_page = AccordianPage(
            driver,
            "https://demoqa.com/accordian"
        )
        accordian_page.open()
        first_accordian_title = \
            accordian_page.check_accordian('first')[0]
        assert first_accordian_title == "What is Lorem Ipsum?", \
            f"\nActual result:" \
            f"\n\tAccordian title: {first_accordian_title}\n" \
            "\nExpected result:" \
            "\n\tAccordian title should be 'What is Lorem Ipsum?'"

    @allure.title(
        "Verify that the user has an opportunity "
        "to get content of the 'What is Lorem Ipsum?' accordian"
    )
    def test_first_content_accordian(self, driver):
        accordian_page = AccordianPage(
            driver,
            "https://demoqa.com/accordian"
        )
        accordian_page.open()
        first_accordian_content = \
            accordian_page.check_accordian('first')[1]
        assert len(first_accordian_content) > 0, \
            f"\nActual result:" \
            f"\n\tContent of the 'What is Lorem Ipsum' " \
            f"accordian is empty on the page. " \
            f"\ntAccordian len: {len(first_accordian_content)}" \
            "\nExpected result:" \
            "\n\tA content of the 'What is Lorem Ipsum' accordian " \
            "should be presented on the page" \
            "\n\tAccordian length should be > 0"

    @allure.title(
        "Verify that the 'Where does it come from?' "
        "accordian title is equal to the expected "
    )
    def test_second_title_accordian(self, driver):
        accordian_page = AccordianPage(
            driver,
            "https://demoqa.com/accordian"
        )
        accordian_page.open()
        second_accordian_title = \
            accordian_page.check_accordian('second')[0]
        assert second_accordian_title == "Where does it come from?", \
            f"\nActual result:" \
            f"\n\tAccordian title: {second_accordian_title}\n" \
            "\nExpected result:" \
            "\n\tAccordian title should be 'Where does it come from?'"

    @allure.title(
        "Verify that the user has an opportunity "
        "to get content of the 'Where does it come from?' accordian"
    )
    def test_second_content_accordian(self, driver):
        accordian_page = AccordianPage(
            driver,
            "https://demoqa.com/accordian"
        )
        accordian_page.open()
        second_accordian_content = \
            accordian_page.check_accordian('second')[1]
        assert len(second_accordian_content) > 0, \
            f"\nActual result:" \
            f"\n\tContent of the 'Where does it come from?' " \
            f"accordian is empty on the page. " \
            f"\ntAccordian len: {len(second_accordian_content)}" \
            "\nExpected result:" \
            "\n\tA content of the 'Where does it come from?' " \
            "accordian should be presented on the page" \
            "\n\tAccordian length should be > 0"

    @allure.title(
        "Verify that the 'Why do we use it?' "
        "accordian title is equal to the expected "
    )
    def test_third_title_accordian(self, driver):
        accordian_page = AccordianPage(
            driver,
            "https://demoqa.com/accordian"
        )
        accordian_page.open()
        third_accordian_title = \
            accordian_page.check_accordian('third')[0]
        assert third_accordian_title == "Why do we use it?", \
            f"\nActual result:" \
            f"\n\tAccordian title: {third_accordian_title}\n" \
            "\nExpected result:" \
            "\n\tAccordian title should be 'Why do we use it?'"

    @allure.title(
        "Verify that the user has an opportunity "
        "to get content of the 'Why do we use it?' accordian"
    )
    def test_third_content_accordian(self, driver):
        accordian_page = AccordianPage(
            driver,
            "https://demoqa.com/accordian"
        )
        accordian_page.open()
        third_accordian_content = \
            accordian_page.check_accordian('third')[1]
        assert len(third_accordian_content) > 0, \
            f"\nActual result:" \
            f"\n\tContent of the 'Why do we use it?' " \
            f"accordian is empty on the page. " \
            f"\ntAccordian len: {len(third_accordian_content)}" \
            "\nExpected result:" \
            "\n\tA content of the 'Why do we use it?' " \
            "accordian should be presented on the page" \
            "\n\tAccordian length should be > 0"
