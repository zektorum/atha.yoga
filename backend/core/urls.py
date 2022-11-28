from django.urls import path

from core.app.handlers.user_handlers import UserRegisterHandler, UserLoginHandler, UserChangePassHandler


urlpatterns = [
    path("register/", UserRegisterHandler.as_view(), name="registration"),
    path("login/", UserLoginHandler.as_view(), name="login"),
    path("switchpass/", UserChangePassHandler.as_view(), name="switchpass"),
]
