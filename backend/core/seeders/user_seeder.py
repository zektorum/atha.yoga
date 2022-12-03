from django.contrib.auth.hashers import make_password
from faker import Faker

from core.models import User


class UserSeeder:
    def __init__(self) -> None:
        self.faker = Faker("ru-RU")

    def seed(self) -> User:
        profile = self.faker.simple_profile()
        return User(
            username=profile["username"],
            email=profile["mail"],
            password=make_password(self.faker.password()),
            about=" ".join(self.faker.words(self.faker.random_int(0, 20)))[:100],
            is_teacher=self.faker.random_element((False, True)),
        )
