from typing import List

from core.app.repositories.base_repository import BaseRepository
from classes.models import Comment


class CommentRepository(BaseRepository):
    model = Comment

    def store(self, comment: Comment) -> None:
        comment.save()

    def find_comments_by_class_id(self, class_id: int) -> List[Comment]:
        return Comment.objects.filter(_class_id=class_id)
