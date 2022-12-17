from django.db.models import QuerySet

from core.app.repositories.base_repository import BaseRepository
from lessons.models import LessonComment


class LessonCommentRepository(BaseRepository):
    model = LessonComment

    def store(self, comment: LessonComment) -> None:
        comment.save()

    def find_by_lesson_id(self, lesson_id: int) -> QuerySet[LessonComment]:
        return self.model.objects.filter(lesson_id=lesson_id)

    def find_by_id(self, id_: int) -> LessonComment:
        return self.model.objects.filter(pk=id_).first()

    def remove(self, comment: LessonComment) -> None:
        comment.delete()
