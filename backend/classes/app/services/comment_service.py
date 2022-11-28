from functools import cached_property

from rest_framework.exceptions import NotFound

from classes.app.repositories.class_repository import ClassRepository
from classes.app.repositories.comment_repository import CommentRepository
from core.app.repositories.user_repository import UserRepository
from classes.app.services.types import CommentCreateData
from classes.models import Comment


class CommentCreate:
    repository = CommentRepository()
    user_repository = UserRepository()
    class_repository = ClassRepository()

    def __init__(self, data: CommentCreateData):
        self.data = data

    @cached_property
    def comment(self) -> Comment:
        from classes.models import Class
        from datetime import datetime

        Class.objects.create(name="jfifjqe fojqf qef", start_datetime=datetime.now())
        user = self.user_repository.find_user_by_email(email=self.data["email"])
        _class = self.class_repository.find_class_by_id(_id=self.data["class_id"])
        if not user or not _class:
            raise NotFound()

        comment = Comment()
        comment.user = user
        comment._class = _class
        comment.text = self.data["text"]

        self.repository.store(comment=comment)
        return comment

    def create(self) -> Comment:
        return self.comment
