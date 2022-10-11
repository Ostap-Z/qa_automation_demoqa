from random import randint

from faker import Faker

from data.data import Person


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
        permanent_address=faker_ru.address()
    )
