from typing import List, Optional

from django.db.models import QuerySet

from core.app.repositories.base_repository import BaseRepository
from core.models import User
from courses.models import Lesson


class LessonRepository(BaseRepository):
    model = Lesson

    def prefetch_related(self, lessons: QuerySet[Lesson]) -> QuerySet[Lesson]:
        return lessons.prefetch_related("participants")

    def bulk_create(self, objs: List[Lesson]) -> None:
        self.model.objects.bulk_create(objs)

    def find_by_id(self, id_: int, prefetch_rels: bool = False) -> Optional[Lesson]:
        lesson_queryset = self.model.objects.filter(pk=id_)
        if prefetch_rels:
            lesson_queryset = self.prefetch_related(lesson_queryset)
        return lesson_queryset.first()

    def find_by_course_id(self, course_id: int) -> QuerySet[Lesson]:
        return self.model.objects.filter(course_id=course_id)

    def is_participant(self, lesson: Lesson, user: User) -> Optional[Lesson]:
        return lesson.participants.filter(id=user.id)

    def add_participant(self, lesson: Lesson, user: User) -> None:
        return lesson.participants.add(user)
