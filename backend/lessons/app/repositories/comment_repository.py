from django.db.models import QuerySet

from core.app.repositories.base_repository import BaseRepository
from lessons.models import Comment


class CommentRepository(BaseRepository):
    model = Comment

    def store(self, comment: Comment) -> None:
        comment.save()

    def find_by_lesson_id(self, lesson_id: int) -> QuerySet[Comment]:
        return Comment.objects.filter(_class_id=lesson_id)
