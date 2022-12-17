from django.urls import path

from lessons.app.handlers.comment_handlers import (
    LessonCommentListHandler,
    LessonCommentCreateHandler,
    LessonCommentRemoveHandler,
)
from lessons.app.handlers.lesson_handlers import (
    LessonsFilterHandler,
    LessonCreateHandler,
    LessonUpdateHandler,
    FavoriteLessonAddHandler,
    FavoriteLessonRemoveHandler,
    FavoriteLessonListHandler,
)

urlpatterns = [
    path("<int:pk>/comments/", LessonCommentListHandler.as_view(), name="comment_list"),
    path(
        "<int:pk>/comments/create/",
        LessonCommentCreateHandler.as_view(),
        name="comment_create",
    ),
    path(
        "<int:lesson_pk>/comments/<int:comment_pk>/remove/",
        LessonCommentRemoveHandler.as_view(),
        name="comment_remove",
    ),
    path("", LessonCreateHandler.as_view(), name="lesson_create"),
    path("<int:pk>", LessonUpdateHandler.as_view(), name="lesson_update"),
    path("filter/", LessonsFilterHandler.as_view(), name="lessons_filter"),
    path(
        "favorites/", FavoriteLessonListHandler.as_view(), name="favorite_lesson_list"
    ),
    path(
        "favorites/add/", FavoriteLessonAddHandler.as_view(), name="favorite_lesson_add"
    ),
    path(
        "favorites/remove/",
        FavoriteLessonRemoveHandler.as_view(),
        name="favorite_lesson_remove",
    ),
]
