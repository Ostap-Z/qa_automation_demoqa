import allure

from pages.widgets_page.accordian_page import AccordianPage


@allure.suite("Widgets suite")
@allure.feature("Accordian page")
class TestAccordian:

    @allure.title(
        "Verify that accordian title is equal to the expected "
        "and accordian content length is more than 0"
    )
    def test_accordian(self, driver):
        accordian_page = AccordianPage(
            driver,
            "https://demoqa.com/accordian"
        )
        accordian_page.open()
        first_accordian_title, first_accordian_content = \
            accordian_page.check_accordian('first')
        second_accordian_title, second_accordian_content = \
            accordian_page.check_accordian('second')
        third_accordian_title, third_accordian_content = \
            accordian_page.check_accordian('third')

        assert first_accordian_title == "What is Lorem Ipsum?" \
               and len(first_accordian_content) > 0,\
               f"\nActual result:" \
               f"\nAccordian title: {first_accordian_title}\n" \
               f"Accordian length: {first_accordian_content}"\
               "\nExpected result:" \
               "\nAccordian title: What is Lorem Ipsum?" \
               "\nAccordian length: > 0"

        assert second_accordian_title == "Where does it come from?"\
               and len(second_accordian_content) > 0,\
               f"\nActual result:" \
               f"\nAccordian title: {second_accordian_title}" \
               f"\nAccordian length: {second_accordian_content}"\
               "\nExpected result:" \
               "\nAccordian title: Where does it come from?" \
               "\nAccordian length: > 0"

        assert third_accordian_title == "Why do we use it?" \
               and len(third_accordian_content) > 0,\
               f"\nActual result:" \
               f"\nAccordian title: {third_accordian_title}" \
               f"\nAccordian length: {third_accordian_content}" \
               "\nExpected result:" \
               "\nAccordian title: Why do we use it?" \
               "\nAccordian length: > 0"
