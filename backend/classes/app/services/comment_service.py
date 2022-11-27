from functools import cached_property
from typing import List

from rest_framework.exceptions import PermissionDenied

from classes.app.repositories.class_repository import ClassRepository
from classes.app.repositories.comment_repository import CommentRepository
from core.app.repositories.user_repository import UserRepository
from classes.app.services.types import CommentAddData, CommentsGetData
from classes.models import Comment


class CommentAddService:
    repository = CommentRepository()

    def __init__(self, data: CommentAddData):
        self.data = data

    @cached_property
    def comment(self) -> Comment:
        user_repository = UserRepository()
        class_repository = ClassRepository()

        user = user_repository.find_user_by_email(self.data["email"])
        _class = class_repository.find_class_by_id(self.data["class_id"])
        if not user or not _class:
            raise PermissionDenied()

        comment = Comment()
        comment.user = user
        comment._class = _class
        comment.text = self.data["text"]

        self.repository.store(comment=comment)
        return comment

    def add(self) -> Comment:
        return self.comment


class CommentsGetService:
    def __init__(self, data: CommentsGetData):
        self.data = data

    @cached_property
    def comments(self) -> List[Comment]:
        class_repository = ClassRepository()
        _class = class_repository.find_class_by_id(self.data["class_id"])
        if not _class:
            raise PermissionDenied()
        return _class.comments

    def get(self) -> List[Comment]:
        return self.comments
