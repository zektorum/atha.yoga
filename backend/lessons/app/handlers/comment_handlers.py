from typing import Any

from rest_framework.decorators import permission_classes
from rest_framework.generics import GenericAPIView
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from lessons.app.http.requests.comment_requests import LessonCommentCreateRequest
from lessons.app.http.resources.comment_resources import LessonCommentResource
from lessons.app.repositories.comment_repository import LessonCommentRepository
from lessons.app.services.comment_service import (
    LessonCommentCreate,
    LessonCommentRemove,
)


class LessonCommentListHandler(APIView):
    def get(self, request: Request, pk: int, *args: Any, **kwargs: Any) -> Response:
        comments = LessonCommentRepository().find_by_lesson_id(lesson_id=pk)
        return Response({"comments": LessonCommentResource(comments, many=True).data})


@permission_classes([IsAuthenticated])
class LessonCommentCreateHandler(GenericAPIView):
    serializer_class = LessonCommentCreateRequest

    def post(self, request: Request, pk: int, *args: Any, **kwargs: Any) -> Response:
        data = self.serializer_class(data=request.data)
        data.is_valid(raise_exception=True)

        comment = LessonCommentCreate(
            lesson_id=pk, text=data.validated_data["text"], user=request.user
        ).create()
        return Response({"comment": LessonCommentResource(comment).data})


@permission_classes([IsAuthenticated])
class LessonCommentRemoveHandler(APIView):
    def delete(self, request: Request, pk: int, *args: Any, **kwargs: Any) -> Response:
        comment = LessonCommentRemove(comment_id=pk, user=request.user).remove()
        return Response({"comment": LessonCommentResource(comment).data})
