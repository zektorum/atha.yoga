from typing import Any

from rest_framework.decorators import permission_classes
from rest_framework.exceptions import NotFound
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from core.app.utils.pagination import paginate
from core.app.utils.permissions import IsTeacher
from lessons.app.http.requests.lesson_requests import (
    LessonFilterRequest,
    LessonCreateRequest,
    LessonUpdateRequest,
    FavoriteLessonAddRemoveRequest,
    LessonTicketBuyRequest,
    LessonTicketUseRequest,
)
from lessons.app.http.resources.lesson_resources import LessonResource
from lessons.app.repositories.lesson_repository import LessonRepository
from lessons.app.services.lesson_service import (
    LessonCreator,
    FavoriteLessonsWork,
    TicketWorkService,
)
from lessons.app.services.lesson_service import (
    LessonUpdator,
    LessonParticipateService,
)


class LessonsFilterHandler(GenericAPIView):
    serializer_class = LessonFilterRequest

    def post(self, *args: Any, **kwargs: Any) -> Response:
        data = self.serializer_class(data=self.request.data, partial=True)
        data.is_valid(raise_exception=True)

        lessons = LessonRepository().filter(data=data.validated_data)

        return Response(
            paginate(data=lessons, request=self.request, resource=LessonResource)
        )


class LessonRetrieveHandler(APIView):
    repository = LessonRepository()

    def get(self, request: Request, pk: int, *args: Any, **kwargs: Any) -> Response:
        lesson = self.repository.find_by_id(id_=pk)
        if not lesson:
            raise NotFound(f"Undefined lesson with pk {pk}")
        return Response({"data": LessonResource(lesson).data})


@permission_classes([IsTeacher])
class LessonCreateHandler(GenericAPIView):
    serializer_class = LessonCreateRequest

    def post(self, *args: Any, **kwargs: Any) -> Response:
        data = self.serializer_class(data=self.request.data)
        data.is_valid(raise_exception=True)

        lesson = LessonCreator(
            data=data.validated_data, user=self.request.user
        ).create()

        return Response({"data": LessonResource(lesson).data})


@permission_classes([IsTeacher])
class LessonUpdateHandler(GenericAPIView):
    serializer_class = LessonUpdateRequest

    def patch(self, request: Request, pk: int, *args: Any, **kwargs: Any) -> Response:
        data = self.serializer_class(data=request.data, partial=True)
        data.is_valid(raise_exception=True)

        lesson = LessonUpdator(
            user=request.user, data=data.validated_data, pk=pk
        ).update()

        return Response({"data": LessonResource(lesson).data})


@permission_classes([IsAuthenticated])
class FavoriteLessonAddHandler(GenericAPIView):
    serializer_class = FavoriteLessonAddRemoveRequest

    def post(self, *args: Any, **kwargs: Any) -> Response:
        data = self.serializer_class(data=self.request.data)
        data.is_valid(raise_exception=True)

        lesson = FavoriteLessonsWork(
            user=self.request.user, lesson_id=data.validated_data["lesson_id"]
        ).add()

        return Response({"data": LessonResource(lesson).data})


@permission_classes([IsAuthenticated])
class FavoriteLessonRemoveHandler(GenericAPIView):
    serializer_class = FavoriteLessonAddRemoveRequest

    def post(self, *args: Any, **kwargs: Any) -> Response:
        data = self.serializer_class(data=self.request.data)
        data.is_valid(raise_exception=True)

        lesson = FavoriteLessonsWork(
            user=self.request.user, lesson_id=data.validated_data["lesson_id"]
        ).remove()

        return Response({"data": LessonResource(lesson).data})


@permission_classes([IsAuthenticated])
class FavoriteLessonListHandler(APIView):
    def get(self, *args: Any, **kwargs: Any) -> Response:
        lessons = LessonRepository().find_user_favorite_lessons(user=self.request.user)
        return Response({"data": LessonResource(lessons, many=True).data})


@permission_classes([IsAuthenticated])
class LessonTicketBuyHandler(GenericAPIView):
    serializer_class = LessonTicketBuyRequest

    def post(self, *args: Any, **kwargs: Any) -> Response:
        data = self.serializer_class(data=self.request.data)
        data.is_valid(raise_exception=True)

        TicketWorkService().buy(
            lesson_id=data.validated_data["lesson_id"],
            user=self.request.user,
            amount=data.validated_data["amount"],
        )

        return Response("Ticket obtained")


@permission_classes([IsAuthenticated])
class LessonTicketUseHandler(GenericAPIView):
    serializer_class = LessonTicketUseRequest

    def put(self, *args: Any, **kwargs: Any) -> Response:
        data = self.serializer_class(data=self.request.data)
        data.is_valid(raise_exception=True)

        link = LessonParticipateService(
            schedule_id=data.validated_data["schedule_id"], user=self.request.user
        ).participate()

        return Response({"data": {"lesson_link": link}})
