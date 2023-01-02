from typing import Any

from rest_framework.decorators import permission_classes
from rest_framework.generics import GenericAPIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from core.app.utils.permissions import IsTeacher
from courses.app.http.requests.lesson_requests import LessonRescheduleRequest
from courses.app.services.lessons_service import LessonReschedule, LessonCancel


@permission_classes([IsTeacher])
class LessonRescheduleHandler(GenericAPIView):
    serializer_class = LessonRescheduleRequest

    def post(
        self, request: Request, lesson_id: int, *args: Any, **kwargs: Any
    ) -> Response:
        data = self.serializer_class(data=self.request.data)
        data.is_valid(raise_exception=True)

        LessonReschedule(
            lesson_id=lesson_id,
            reschedule_to=data.validated_data["reschedule_to"],
            user=self.request.user,
        ).reschedule()

        return Response({"data": "Success rescheduled"})


@permission_classes([IsTeacher])
class LessonCancelHandler(APIView):
    def post(
        self, request: Request, lesson_id: int, *args: Any, **kwargs: Any
    ) -> Response:
        LessonCancel(lesson_id=lesson_id, user=self.request.user).cancel()

        return Response({"data": "Success canceled"})
