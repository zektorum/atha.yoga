from functools import cached_property

from rest_framework.exceptions import NotFound

from core.models import User
from courses.app.repositories.lesson_repository import LessonRepository
from courses.models import Lesson


class LessonCancel:
    def __init__(self, lesson_id: int, user: User) -> None:
        self.lesson_id = lesson_id
        self.user = user

    @cached_property
    def lesson(self) -> Lesson:
        lesson = LessonRepository().find_by_id_creator(
            id_=self.lesson_id, user_id=self.user.id
        )
        if not lesson:
            raise NotFound(f"Undefined lesson with pk {self.lesson_id}")
        return lesson

    def cancel(self) -> None:
        ...
