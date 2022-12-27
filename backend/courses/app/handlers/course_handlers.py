from typing import Any

from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from rest_framework.decorators import permission_classes
from rest_framework.exceptions import NotFound
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from core.app.utils.pagination import paginate
from core.app.utils.permissions import IsTeacher
from courses.app.http.requests.course_requests import (
    CourseFilterRequest,
    CourseCreateRequest,
    CourseUpdateRequest,
    FavoriteCourseAddRemoveRequest,
    CourseTicketBuyRequest,
    CourseTicketUseRequest,
)
from courses.app.http.resources.course_resources import CourseResource, LessonResource
from courses.app.repositories.course_repository import CourseRepository
from courses.app.repositories.lesson_repository import LessonRepository
from courses.app.repositories.transaction_repository import TicketTransactionRepository
from courses.app.services.course_service import (
    CourseCreator,
    FavoriteCoursesWork,
    TicketBuy,
)
from courses.app.services.course_service import (
    CourseUpdator,
    CourseParticipateService,
)


class CourseFilterHandler(GenericAPIView):
    serializer_class = CourseFilterRequest

    def post(self, *args: Any, **kwargs: Any) -> Response:
        data = self.serializer_class(data=self.request.data, partial=True)
        data.is_valid(raise_exception=True)

        courses = CourseRepository().filter(data=data.validated_data)

        return Response(
            paginate(data=courses, request=self.request, resource=CourseResource)
        )


class CourseRetrieveHandler(APIView):
    repository = CourseRepository()

    def get(self, request: Request, pk: int, *args: Any, **kwargs: Any) -> Response:
        course = self.repository.find_by_id(id_=pk)
        if not course:
            raise NotFound(f"Undefined course with pk {pk}")
        return Response(
            {
                "data": CourseResource(
                    course, context={"user": self.request.user.pk}
                ).data
            }
        )


@permission_classes([IsTeacher])
class CourseCreateHandler(GenericAPIView):
    serializer_class = CourseCreateRequest

    def post(self, *args: Any, **kwargs: Any) -> Response:
        data = self.serializer_class(data=self.request.data)
        data.is_valid(raise_exception=True)

        course = CourseCreator(
            data=data.validated_data, user=self.request.user
        ).create()

        return Response(
            {
                "data": CourseResource(
                    course, context={"user": self.request.user.pk}
                ).data
            }
        )


@permission_classes([IsTeacher])
class CourseUpdateHandler(GenericAPIView):
    serializer_class = CourseUpdateRequest

    def patch(self, request: Request, pk: int, *args: Any, **kwargs: Any) -> Response:
        data = self.serializer_class(data=request.data, partial=True)
        data.is_valid(raise_exception=True)

        course = CourseUpdator(
            user=request.user, data=data.validated_data, pk=pk
        ).update()

        return Response(
            {
                "data": CourseResource(
                    course, context={"user": self.request.user.pk}
                ).data
            }
        )


@permission_classes([IsAuthenticated])
class FavoriteCourseAddHandler(GenericAPIView):
    serializer_class = FavoriteCourseAddRemoveRequest

    def post(self, *args: Any, **kwargs: Any) -> Response:
        data = self.serializer_class(data=self.request.data)
        data.is_valid(raise_exception=True)

        course = FavoriteCoursesWork(
            user=self.request.user, course_id=data.validated_data["course_id"]
        ).add()

        return Response(
            {
                "data": CourseResource(
                    course, context={"user": self.request.user.pk}
                ).data
            }
        )


@permission_classes([IsAuthenticated])
class FavoriteCourseRemoveHandler(GenericAPIView):
    serializer_class = FavoriteCourseAddRemoveRequest

    def post(self, *args: Any, **kwargs: Any) -> Response:
        data = self.serializer_class(data=self.request.data)
        data.is_valid(raise_exception=True)

        course = FavoriteCoursesWork(
            user=self.request.user, course_id=data.validated_data["course_id"]
        ).remove()

        return Response(
            {
                "data": CourseResource(
                    course, context={"user": self.request.user.pk}
                ).data
            }
        )


@permission_classes([IsAuthenticated])
class FavoriteCourseListHandler(APIView):
    def get(self, *args: Any, **kwargs: Any) -> Response:
        courses = CourseRepository().find_user_favorite_courses(user=self.request.user)
        return Response(
            {
                "data": CourseResource(
                    courses, context={"user": self.request.user.pk}, many=True
                ).data
            }
        )


@permission_classes([IsAuthenticated])
class CourseTicketBuyHandler(GenericAPIView):
    serializer_class = CourseTicketBuyRequest

    def post(self, *args: Any, **kwargs: Any) -> Response:
        data = self.serializer_class(data=self.request.data)
        data.is_valid(raise_exception=True)

        payment_url = TicketBuy().buy(
            course_id=data.validated_data["course_id"],
            user=self.request.user,
            amount=data.validated_data["amount"],
        )

        return Response({"data": payment_url})


class SuccessTicketPaymentHandler(APIView):
    repos = TicketTransactionRepository()

    def get(self, request: Request, transaction_id: str) -> HttpResponseRedirect:
        redirect_url = TicketBuy().confirm(transaction_id=transaction_id)
        return redirect(redirect_url)


@permission_classes([IsAuthenticated])
class CourseTicketUseHandler(GenericAPIView):
    serializer_class = CourseTicketUseRequest

    def put(self, *args: Any, **kwargs: Any) -> Response:
        data = self.serializer_class(data=self.request.data)
        data.is_valid(raise_exception=True)

        link = CourseParticipateService(
            lesson_id=data.validated_data["lesson_id"], user=self.request.user
        ).participate()

        return Response({"data": {"course_link": link}})


class LessonRetrieveHandler(APIView):
    def get(self, request: Request, pk: int, *args: Any, **kwargs: Any) -> Response:
        lesson = LessonRepository().find_by_id(id_=pk)
        if not lesson:
            raise NotFound(f"Undefined lesson with pk {pk}")
        return Response({"data": LessonResource(lesson).data})


class LessonListHandler(APIView):
    def get(self, request: Request, pk: int, *args: Any, **kwargs: Any) -> Response:
        lessons = LessonRepository().find_by_course_id(course_id=pk)
        return Response(
            paginate(data=lessons, request=self.request, resource=LessonResource)
        )
