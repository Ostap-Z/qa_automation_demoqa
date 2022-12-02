import allure

from pages.forms_page.form_page import FormPage


@allure.suite("Form suite")
@allure.feature("Form page")
class TestForm:

    @allure.title(
        "Verify that the user has an opportunity to do a registration "
        "and registration data is presented in the table"
    )
    def test_registration_form(self, driver):
        form_page = FormPage(
            driver,
            "https://demoqa.com/automation-practice-form"
        )
        form_page.open()
        person = form_page.fill_form_fields()
        result = form_page.get_form_result()
        assert [f"{person.first_name} {person.last_name}",
                person.email] == [result[0], result[1]], \
               "\nActual result:" \
               f"\n\t{result[0]} {result[1]}" \
               "\nExpected result:" \
               f"\n\t{person.first_name} " \
               f"{person.last_name} " \
               f"{person.email}"
