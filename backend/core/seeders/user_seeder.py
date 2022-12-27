import random

from django.contrib.auth.hashers import make_password
from faker import Faker

from core.models import User, Transaction, QuestionnaireTeacher


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
        )


class TransactionSeeder:

    def seed(self) -> Transaction:
        return Transaction(
            amount=random.randint(1, 10),
            payment_id=random.randint(1, 100)
        )


class QuestionnaireTeacherSeeder:
    def __init__(self, user: User) -> None:
        self.faker = Faker("ru-RU")
        self.user = user

    def seed(self) -> QuestionnaireTeacher:
        profile = self.faker.simple_profile()
        return QuestionnaireTeacher(
            user=self.user,
            name=profile["name"].split()[0],
            surname=profile["name"].split()[1],
            date_of_birth=profile['birthdate'],
            gender=profile['sex'],
            about_me=" ".join(self.faker.words(self.faker.random_int(0, 20)))[:100],
            work_experience=" ".join(self.faker.words(self.faker.random_int(0, 20)))[:100],
            vk_link=self.faker.url(),
            telegram_link=self.faker.url(),
            status="ACCEPTED",
            user_photo="Image.user." + self.user.username,
            passport_photo="Image.passport_photo." + self.user.username,
            user_with_passport_photo="Image.user_with_passport." + self.user.username,
        )
