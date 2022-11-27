from typing import Any

from rest_framework.generics import GenericAPIView
from rest_framework.request import Request
from rest_framework.response import Response

from classes.app.http.requests.comment_requests import (
    CommentAddRequest,
    CommentsGetRequest,
)
from classes.app.http.resources.comment_resources import CommentResource
from classes.app.services.comment_service import CommentAddService, CommentsGetService


class CommentAddHandler(GenericAPIView):
    serializer_class = CommentAddRequest

    def post(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        data = self.serializer_class(data=request.data)
        data.is_valid(raise_exception=True)

        comment = CommentAddService(data=data.validated_data).add()
        return Response({"data": {"comment": CommentResource(comment).data}})


class CommentsGetHandler(GenericAPIView):
    serializer_class = CommentsGetRequest

    def post(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        data = self.serializer_class(data=request.data)
        data.is_valid(raise_exception=True)

        comments = CommentsGetService(data=data.validated_data).get()
        return Response(
            {"data": {"comments": CommentResource(comments, many=True).data}}
        )
