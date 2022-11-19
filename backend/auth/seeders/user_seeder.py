from faker import Faker
from backend.auth.models import User


class UserSeeder:
    def __init__(self):
        self.faker = Faker()

    def seed(self) -> User:
        profile = self.faker.simple_profile()
        return User(username=profile['username'],
                    email=profile['mail'],
                    password=self.faker.password(),
                    status=' '.join(self.faker.words(self.faker.random_int(0, 20))),
                    is_instructor=self.faker.random_element((None, True, False)))
