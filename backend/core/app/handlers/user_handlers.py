from typing import Any

from rest_framework.generics import GenericAPIView
from rest_framework.request import Request
from rest_framework.response import Response

from core.app.http.requests.user_requests import UserRegisterRequest, UserLoginRequest, UserChangePassRequest, SendTextRequest, SendHTMLRequest
from core.app.http.resources.user_resources import UserResource
from core.app.services.user_services import UserRegister, UserLogin, UserChangePass
from core.app.services.email_services import MailSendText, MailSendHTML


class UserRegisterHandler(GenericAPIView):
    serializer_class = UserRegisterRequest

    def post(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        data = self.serializer_class(data=request.data)
        data.is_valid(raise_exception=True)

        user, token = UserRegister(data=data.validated_data).register()
        return Response(
            {"data": {"user": UserResource(user).data, "tokens": token._asdict()}}
        )


class UserLoginHandler(GenericAPIView):
    serializer_class = UserLoginRequest

    def post(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        data = self.serializer_class(data=request.data)
        data.is_valid(raise_exception=True)

        user, token = UserLogin(data=data.validated_data).login()
        return Response(
            {"data": {"user": UserResource(user).data, "tokens": token._asdict()}}
        )

class UserChangePassHandler(GenericAPIView):
    serializer_class = UserChangePassRequest

    def post(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        data = self.serializer_class(data=request.data)
        data.is_valid(raise_exception=True)

        user, token = UserChangePass(data=data.validated_data).change()
        return Response(
            {"data": {"user": UserResource(user).data, "tokens": token._asdict()}}
        )

class MailSendTextHandler(GenericAPIView):
    serializer_class = SendTextRequest

    def post(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        data = self.serializer_class(data=request.data)
        data.is_valid(raise_exception=True)
        try:
            MailSendText(data=data.validated_data).send_text()
            return Response('Mail was sent succesfully!')
        except Exception as e:
            return Response(e)


class MailSendHTMLHandler(GenericAPIView):
    serializer_class = SendHTMLRequest

    def post(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        data = self.serializer_class(data=request.data)
        data.is_valid(raise_exception=True)
        try:
            MailSendHTML(data=data.validated_data).send_html()
            return Response('Mail was sent succesfully!')
        except Exception as e:
            return Response(e)


