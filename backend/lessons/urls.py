from django.urls import path

from lessons.app.handlers.comment_handler import (
    CommentCreateHandler,
    CommentListHandler,
)

urlpatterns = [
    path("comments/create/", CommentCreateHandler.as_view(), name="comment_create"),
    path("comments/", CommentListHandler.as_view(), name="comment_list"),
]
