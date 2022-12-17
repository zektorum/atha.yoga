from typing import Any

from rest_framework.decorators import permission_classes
from rest_framework.generics import GenericAPIView
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from lessons.app.http.requests.review_requests import LessonReviewCreateRequest
from lessons.app.http.resources.review_resources import LessonReviewResource
from lessons.app.repositories.review_repository import LessonReviewRepository
from lessons.app.services.review_service import LessonReviewCreate, LessonReviewRemove


class LessonReviewListHandler(APIView):
    def get(self, request: Request, pk: int, *args: Any, **kwargs: Any) -> Response:
        reviews = LessonReviewRepository().find_by_lesson_id(lesson_id=pk)
        return Response({"reviews": LessonReviewResource(reviews, many=True).data})


@permission_classes([IsAuthenticated])
class LessonReviewCreateHandler(GenericAPIView):
    serializer_class = LessonReviewCreateRequest

    def post(self, request: Request, pk: int, *args: Any, **kwargs: Any) -> Response:
        data = self.serializer_class(data=request.data)
        data.is_valid(raise_exception=True)

        review = LessonReviewCreate(
            lesson_id=pk, data=data.validated_data, user=request.user
        ).create()
        return Response({"review": LessonReviewResource(review).data})


@permission_classes([IsAuthenticated])
class LessonReviewRemoveHandler(APIView):
    def delete(
        self,
        request: Request,
        lesson_pk: int,
        review_pk: int,
        *args: Any,
        **kwargs: Any
    ) -> Response:
        review = LessonReviewRemove(
            lesson_id=lesson_pk, review_id=review_pk, user=request.user
        ).remove()
        return Response({"review": LessonReviewResource(review).data})
