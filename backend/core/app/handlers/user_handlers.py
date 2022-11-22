from typing import Any

from rest_framework.generics import GenericAPIView
from rest_framework.request import Request
from rest_framework.response import Response

from backend.core.app.http.requests.user_requests import UserRegisterRequest
from core.app.http.resources.user_resources import UserResource
from core.app.services.user_services import UserRegister


class UserRegisterHandler(GenericAPIView):
    serializer_class = UserRegisterRequest

    def post(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        data = self.serializer_class(data=request.data)
        data.is_valid(raise_exception=True)

        user = UserRegister(data=data.validated_data).register()
        return Response({"data": UserResource(user).data})
