import random

from faker import Faker

from classes.models import Comment, Class
from core.models import User


class CommentSeeder:
    def __init__(self) -> None:
        self.faker = Faker()

    def seed(self) -> Comment:
        user_ids = User.objects.all().values("id")
        if not user_ids.exists():
            raise Exception("no users in db")
        random_user_id = random.choice(user_ids)["id"]
        class_ids = Class.objects.all().values("id")
        if not class_ids.exists():
            raise Exception("no classes in db")
        random_class_id = random.choice(class_ids)["id"]

        return Comment(
            user=User.objects.get(pk=random_user_id),
            text=" ".join(self.faker.words(self.faker.random_int(1, 20))),
            _class=User.objects.get(pk=random_class_id),
        )
