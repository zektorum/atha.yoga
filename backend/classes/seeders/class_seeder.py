from faker import Faker

from backend.classes.models import Class


class ClassSeeder:
    def __init__(self) -> None:
        self.faker = Faker()

    def seed(self) -> Class:
        return Class(
            name=" ".join(self.faker.words(self.faker.random_int(1, 5))),
            start_datetime=self.faker.date_time(),
        )
