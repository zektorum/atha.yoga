from typing import List, Optional

from django.db.models import QuerySet, F

from core.app.repositories.base_repository import BaseRepository
from core.models import User
from courses.models import Lesson


class LessonRepository(BaseRepository):
    model = Lesson

    def fetch_relations(self, lessons: QuerySet[Lesson]) -> QuerySet[Lesson]:
        return lessons.annotate(end_at=F("start_at") + F("course__duration"))

    def bulk_create(self, objs: List[Lesson]) -> None:
        self.model.objects.bulk_create(objs)

    def find_by_id(self, id_: int, fetch_rels: bool = False) -> Optional[Lesson]:
        lesson_queryset = self.model.objects.filter(pk=id_)
        if fetch_rels:
            lesson_queryset = self.fetch_relations(lesson_queryset)
        return lesson_queryset.first()

    def find_by_course_id(self, course_id: int) -> QuerySet[Lesson]:
        return self.model.objects.filter(course_id=course_id)

    def is_participant(self, lesson: Lesson, user: User) -> Optional[Lesson]:
        return lesson.participants.filter(id=user.id)

    def add_participant(self, lesson: Lesson, user: User) -> None:
        return lesson.participants.add(user)
