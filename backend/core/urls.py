from django.urls import path
from core import views
from core.app.handlers.user_handlers import (UserRegisterHandler,
                                             UserLoginHandler,
                                             UserChangePassHandler,
                                             )
from core.app.handlers.teachers_questuonnaire_handlers import QuestionnaireTeacherHandler


urlpatterns = [
    path("register/", UserRegisterHandler.as_view(), name="registration"),
    path("login/", UserLoginHandler.as_view(), name="login"),
    path("changepass/", UserChangePassHandler.as_view(), name="changepass"),
    path("questionnaireteacher/", QuestionnaireTeacherHandler.as_view(), name="questionnaireteacherregestration")
]
