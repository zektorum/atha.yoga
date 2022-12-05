import random
import time
from datetime import timedelta

import pytz
from faker import Faker

from core.models import User
from lessons.models import Lesson, LessonTypes, LessonLevels, LessonPrices
from lessons.models import LessonComplexities


class LessonSeeder:
    def __init__(self, user: User) -> None:
        self.faker = Faker("ru-RU")
        self.user = user

    def seed(self) -> Lesson:
        random.seed(time.time())
        return Lesson(
            name=" ".join(self.faker.words(self.faker.random_int(1, 5))),
            start_datetime=self.faker.date_time(tzinfo=pytz.UTC),
            description=self.faker.sentence(),
            lesson_type=random.choice([i[0] for i in LessonTypes.choices]),
            complexity=random.choice([i[0] for i in LessonComplexities.choices]),
            level=random.choice([i[0] for i in LessonLevels.choices]),
            single=random.choice([False, True]),
            duration=timedelta(minutes=random.randint(60, 300)),
            price=random.choice([i[0] for i in LessonPrices.choices]),
            cost=random.randint(1000, 100000),
            teacher=self.user,
        )
