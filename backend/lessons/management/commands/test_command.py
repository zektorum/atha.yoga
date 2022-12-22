from typing import Any

from django.core.management import BaseCommand

from core.seeders.user_seeder import UserSeeder
from lessons.seeders.lesson_seeder import LessonSeeder


class Command(BaseCommand):
    def handle(self, *args: Any, **options: Any) -> None:
        user = UserSeeder().seed()
        user.save()

        LessonSeeder(user=user).seed().save()
