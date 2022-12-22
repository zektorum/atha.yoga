from typing import Any

from django.core.management import BaseCommand

from core.models import User
from core.seeders.user_seeder import UserSeeder
from courses.seeders.course_seeder import CourseSeeder

DEFAULT_USERS_COUNT = 5
DEFAULT_LESSONS_COUNT = DEFAULT_USERS_COUNT * 10


class Command(BaseCommand):
    def handle(self, *args: Any, **options: Any) -> None:
        self._init_superuser()
        self._seed_users()
        self._seed_courses()

    def _init_superuser(self) -> None:
        user = User()
        user.username = user.email = "test@user.ru"
        user.set_password("Dakk3YVnDakk3YVn")
        user.is_staff = user.is_superuser = True
        user.save()

    def _seed_users(self, count: int = DEFAULT_USERS_COUNT) -> None:
        for i in range(count):
            UserSeeder().seed().save()

    def _seed_courses(self, count: int = DEFAULT_LESSONS_COUNT) -> None:
        for i in range(count):
            CourseSeeder(user=User.objects.order_by("?").first()).seed().save()
