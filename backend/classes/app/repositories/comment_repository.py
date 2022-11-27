from core.app.repositories.base_repository import BaseRepository
from classes.models import Comment


class CommentRepository(BaseRepository):
    model = Comment

    def store(self, comment: Comment) -> None:
        comment.save()
