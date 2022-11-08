from random import randint

from faker import Faker

from data.data import Person, Color

faker_ru = Faker("ru_RU")
Faker.seed()


def generated_person():
    yield Person(
        full_name=f"{faker_ru.first_name()} {faker_ru.last_name()} {faker_ru.middle_name()}",
        first_name=faker_ru.first_name(),
        last_name=faker_ru.last_name(),
        age=randint(0, 100),
        department=faker_ru.job(),
        salary=randint(300, 10_000),
        email=faker_ru.email(),
        current_address=faker_ru.address(),
        permanent_address=faker_ru.address(),
        mobile=faker_ru.msisdn()
    )


def generated_file():
    path = rf"C:\Users\OstapZherebetskyi\Desktop\test_examples\qa_automation_demo\qa_automation_demoqa\filetest{randint(0, 999)}.txt"
    with open(path, "w+") as file:
        file.write(f"Hello World")

    return file.name, path


def generated_color():
    yield Color(
        color_name=["Red", "Blue", "Green", "Yellow", "Purple", "Black", "White", "Voilet", "Indigo", "Magenta", "Aqua"]
    )
