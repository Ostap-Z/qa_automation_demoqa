from pages.forms_page.form_page import FormPage


class TestForm:

    def test_form(self, driver):
        form_page = FormPage(
            driver,
            "https://demoqa.com/automation-practice-form"
        )
        form_page.open()
        person = form_page.fill_form_fields()
        result = form_page.get_form_result()
        assert [f"{person.first_name} {person.last_name}", person.email] \
               == [result[0], result[1]], \
               f"\nActual result: {result[0]} {result[1]}" \
               f"\nExpected result: " \
               f"{person.first_name} {person.last_name} {person.email}"
