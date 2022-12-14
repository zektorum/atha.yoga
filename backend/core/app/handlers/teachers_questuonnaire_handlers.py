from typing import Any

from rest_framework.generics import GenericAPIView
from rest_framework.request import Request
from rest_framework.response import Response

from core.app.http.requests.teachers_questuonnaire_requests import QuestionnaireTeacherRequest

from core.app.http.resources.teachers_questuonnaire_resources import QuestionnaireTeacherResource
from core.app.services.teachers_questuonnaire_services import QuestionnaireTeacherRegister


class QuestionnaireTeacherHandler(GenericAPIView):
    serializer_class = QuestionnaireTeacherRequest

    def post(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        data = self.serializer_class(data=request.data)
        data.is_valid(raise_exception=True)

        user, token = QuestionnaireTeacherRegister(data=data.validated_data).create_questionnaire()
        return Response(
            {"data": {"user": QuestionnaireTeacherResource(user).data, "tokens": token._asdict()}}
        )
