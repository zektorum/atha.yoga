from functools import cached_property

from rest_framework.exceptions import NotFound

from core.app.repositories.user_repository import UserRepository
from core.models import User
from lessons.app.repositories.comment_repository import CommentRepository
from lessons.app.repositories.lesson_repository import LessonRepository
from lessons.app.services.types import CommentCreateData
from lessons.models import LessonComment


class CommentCreate:
    repository = CommentRepository()
    user_repository = UserRepository()
    lesson_repository = LessonRepository()

    def __init__(self, user: User, data: CommentCreateData):
        self.data = data
        self.user = user

    @cached_property
    def comment(self) -> LessonComment:
        lesson = self.lesson_repository.find_by_id(id_=self.data["lesson_id"])
        if not lesson:
            raise NotFound(f"Undefined lesson with id {self.data['lesson_id']}")

        comment = LessonComment()
        comment.user = self.user
        comment.lesson = lesson
        comment.text = self.data["text"]

        self.repository.store(comment=comment)
        return comment

    def create(self) -> LessonComment:
        return self.comment
