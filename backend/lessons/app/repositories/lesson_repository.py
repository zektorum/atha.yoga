from typing import Optional

from core.app.repositories.base_repository import BaseRepository
from lessons.models import Lesson


class LessonRepository(BaseRepository):
    model = Lesson

    def store(self, lesson: Lesson) -> None:
        lesson.save()

    def find_lesson_by_id(self, _id: int) -> Optional[Lesson]:
        return Lesson.objects.filter(pk=_id).first()
