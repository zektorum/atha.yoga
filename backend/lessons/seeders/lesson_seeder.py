from faker import Faker

from backend.lessons.models import Lesson


class ClassSeeder:
    def __init__(self) -> None:
        self.faker = Faker()

    def seed(self) -> Lesson:
        return Lesson(
            name=" ".join(self.faker.words(self.faker.random_int(1, 5))),
            start_datetime=self.faker.date_time(),
        )
