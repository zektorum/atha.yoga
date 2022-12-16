import random

from faker import Faker

from core.models import User
from lessons.models import LessonComment, Lesson


class LessonCommentSeeder:
    def __init__(self) -> None:
        self.faker = Faker("ru-RU")

    def seed(self) -> LessonComment:
        user_ids = User.objects.all().values("id")
        if not user_ids.exists():
            raise Exception("no users in db")
        random_user_id = random.choice(user_ids)["id"]
        lesson_ids = Lesson.objects.all().values("id")
        if not lesson_ids.exists():
            raise Exception("no lessons in db")
        random_lesson_id = random.choice(lesson_ids)["id"]

        return LessonComment(
            user=User.objects.get(pk=random_user_id),
            text=" ".join(self.faker.words(self.faker.random_int(1, 20))),
            _class=User.objects.get(pk=random_lesson_id),
        )
