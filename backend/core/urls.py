from django.urls import path

from core.app.handlers.user_handlers import UserRegisterHandler, UserLoginHandler


urlpatterns = [
    path("register/", UserRegisterHandler.as_view(), name="registration"),
    path("login/", UserLoginHandler.as_view(), name="login"),
]
