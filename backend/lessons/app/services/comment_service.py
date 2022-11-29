from functools import cached_property

from rest_framework.exceptions import NotFound

from lessons.app.repositories.lesson_repository import LessonRepository
from lessons.app.repositories.comment_repository import CommentRepository
from core.app.repositories.user_repository import UserRepository
from lessons.app.services.types import CommentCreateData
from lessons.models import Comment


class CommentCreate:
    repository = CommentRepository()
    user_repository = UserRepository()
    lesson_repository = LessonRepository()

    def __init__(self, data: CommentCreateData):
        self.data = data

    @cached_property
    def comment(self) -> Comment:
        user = self.user_repository.find_user_by_email(email=self.data["email"])
        lesson = self.lesson_repository.find_lesson_by_id(_id=self.data["lesson_id"])
        if not user or not lesson:
            raise NotFound()

        comment = Comment()
        comment.user = user
        comment.lesson = lesson
        comment.text = self.data["text"]

        self.repository.store(comment=comment)
        return comment

    def create(self) -> Comment:
        return self.comment
