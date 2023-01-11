from typing import Any

from django.core.management import BaseCommand

from core.models import User
from courses.models import Course
from courses.seeders.course_seeder import CourseReviewSeeder


class Command(BaseCommand):
    def handle(self, *args: Any, **options: Any) -> None:
        for _ in range(300):
            CourseReviewSeeder(
                user=User.objects.order_by("?").first(),
                course=Course.objects.get(pk=134),
            ).seed().save()
