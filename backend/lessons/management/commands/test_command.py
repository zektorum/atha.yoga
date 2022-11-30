from typing import Any

from django.core.management import BaseCommand

from core.seeders.user_seeder import UserSeeder
from lessons.seeders.lesson_seeder import LessonSeeder


class Command(BaseCommand):
    def handle(self, *args: Any, **options: Any) -> None:
        user = UserSeeder().seed()
        user.save()
        for i in range(30):
            lesson = LessonSeeder(user=user).seed()
            lesson.save()
