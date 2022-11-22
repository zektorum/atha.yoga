from django.urls import path

from core.app.handlers.user_handlers import UserRegisterHandler

urlpatterns = [path("register/", UserRegisterHandler.as_view())]
