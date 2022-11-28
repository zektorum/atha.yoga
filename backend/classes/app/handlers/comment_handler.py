from typing import Any

from rest_framework.generics import GenericAPIView
from rest_framework.request import Request
from rest_framework.response import Response

from classes.app.http.requests.comment_requests import (
    CommentCreateRequest,
    CommentListRequest,
)
from classes.app.http.resources.comment_resources import CommentResource
from classes.app.repositories.comment_repository import CommentRepository
from classes.app.services.comment_service import CommentCreate


class CommentCreateHandler(GenericAPIView):
    serializer_class = CommentCreateRequest

    def post(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        data = self.serializer_class(data=request.data)
        data.is_valid(raise_exception=True)

        comment = CommentCreate(data=data.validated_data).create()
        return Response({"comment": CommentResource(comment).data})


class CommentListHandler(GenericAPIView):
    serializer_class = CommentListRequest

    def get(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        data = self.serializer_class(data=request.data)
        data.is_valid(raise_exception=True)

        comments = CommentRepository().find_comments_by_class_id(
            data.validated_data["class_id"]
        )
        return Response({"comments": CommentResource(comments, many=True).data})
