from typing import Any

from django.core.management import BaseCommand

from core.models import User
from core.seeders.user_seeder import UserSeeder, TransactionSeeder, QuestionnaireTeacherSeeder
from courses.models import Course
from courses.seeders.course_seeder import CourseSeeder, TicketSeeder, CourseCommentSeeder, CourseReviewSeeder, \
    LessonSeeder

DEFAULT_USERS_COUNT = 5
DEFAULT_LESSONS_COUNT = DEFAULT_USERS_COUNT * 10


class Command(BaseCommand):
    def handle(self, *args: Any, **options: Any) -> None:
        self._seed_users()
        self._seed_courses()
        self._seed_transactions()
        self._seed_tickets()
        self._seed_comments()
        self._seed_questionnaires()
        self._seed_coursereviews()
        self._seed_lessonseeder()

    def _seed_users(self, count: int = DEFAULT_USERS_COUNT) -> None:
        for i in range(count):
            UserSeeder().seed().save()

    def _seed_courses(self, count: int = DEFAULT_LESSONS_COUNT) -> None:
        for i in range(count):
            CourseSeeder(user=User.objects.order_by("?").first()).seed().save()

    def _seed_transactions(self, count: int = DEFAULT_LESSONS_COUNT) -> None:
        for i in range(count):
            TransactionSeeder().seed().save()

    def _seed_tickets(self, count: int = DEFAULT_LESSONS_COUNT) -> None:
        for i in range(count):
            TicketSeeder(
                user=User.objects.order_by("?").first(),
                course=Course.objects.order_by("?").first()
            ).seed().save()

    def _seed_comments(self, count: int = DEFAULT_LESSONS_COUNT) -> None:
        for i in range(count):
            CourseCommentSeeder(
                user=User.objects.order_by("?").first(),
                course=Course.objects.order_by("?").first()
            ).seed().save()

    def _seed_questionnaires(self, count: int = DEFAULT_LESSONS_COUNT) -> None:
        for i in range(count):
            QuestionnaireTeacherSeeder(
                user=User.objects.order_by("?").first(),
            ).seed().save()

    def _seed_coursereviews(self, count: int = DEFAULT_LESSONS_COUNT) -> None:
        for i in range(count):
            CourseReviewSeeder(
                user=User.objects.order_by("?").first(),
                course=Course.objects.order_by("?").first()
            ).seed().save()

    def _seed_lessonseeder(self, count: int = DEFAULT_LESSONS_COUNT) -> None:
        for i in range(count):
            LessonSeeder(
                course=Course.objects.order_by("?").first()
            ).seed().save()
