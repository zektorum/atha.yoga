from django.db.models import QuerySet

from core.app.repositories.base_repository import BaseRepository
from lessons.models import LessonComment


class CommentRepository(BaseRepository):
    model = LessonComment

    def store(self, comment: LessonComment) -> None:
        comment.save()

    def find_by_lesson_id(self, lesson_id: int) -> QuerySet[LessonComment]:
        return LessonComment.objects.filter(_class_id=lesson_id)
