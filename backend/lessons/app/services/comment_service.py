from functools import cached_property

from rest_framework.exceptions import NotFound, PermissionDenied

from core.app.repositories.user_repository import UserRepository
from core.models import User
from lessons.app.repositories.comment_repository import LessonCommentRepository
from lessons.app.repositories.lesson_repository import LessonRepository
from lessons.models import LessonComment


class LessonCommentCreate:
    repository = LessonCommentRepository()
    user_repository = UserRepository()
    lesson_repository = LessonRepository()

    def __init__(self, lesson_id: int, user: User, text: str):
        self.text = text
        self.user = user
        self.lesson_id = lesson_id

    @cached_property
    def comment(self) -> LessonComment:
        lesson = self.lesson_repository.find_by_id(id_=self.lesson_id)
        if not lesson:
            raise NotFound(f"Undefined lesson with id {self.lesson_id}")

        comment = LessonComment()
        comment.user = self.user
        comment.lesson = lesson
        comment.text = self.text

        self.repository.store(comment=comment)
        return comment

    def create(self) -> LessonComment:
        return self.comment


class LessonCommentRemove:
    repository = LessonCommentRepository()

    def __init__(self, lesson_id: int, comment_id: int, user: User):
        self.lesson_id = lesson_id
        self.comment_id = comment_id
        self.user = user

    @cached_property
    def comment(self) -> LessonComment:
        comment = self.repository.find_by_id(id_=self.comment_id)
        if not comment:
            raise NotFound(f"Undefined comment with id {self.comment_id}")
        if comment.lesson.id != self.lesson_id:
            raise NotFound(
                f"Undefined comment with id {self.comment_id} for lesson with id {self.lesson_id}"
            )
        if comment.user.id != self.user.id:
            raise PermissionDenied(
                f"User with id {self.user.id} can't remove comment with id {self.comment_id}"
            )

        return comment

    def remove(self) -> LessonComment:
        self.repository.remove(comment=self.comment)
        return self.comment
