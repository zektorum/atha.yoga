from django.urls import path

from classes.app.handlers.comment_handler import CommentAddHandler, CommentsGetHandler

urlpatterns = [
    path("comments/add", CommentAddHandler.as_view(), name="add_comment"),
    path("comments/", CommentsGetHandler.as_view(), name="comments"),
]
