from django.urls import path

from core.app.handlers.teachers_questionnaire_handlers import (
    QuestionnaireTeacherHandler,
)
from core.app.handlers.user_handlers import (
    UserRegisterHandler,
    UserRegisterConfirmHandler,
    UserLoginHandler,
    UserChangePassHandler,
    UserSendPwdResetMailHandler,
    UserResetPassHandler,
    LoggedUserProfileHandler,
    UserProfileHandler,
    UserProfileUpdateHandler,
)

urlpatterns = [
    path("register/", UserRegisterHandler.as_view(), name="registration"),
    path(
        "register/confirm/",
        UserRegisterConfirmHandler.as_view(),
        name="registration_confirm",
    ),
    path("login/", UserLoginHandler.as_view(), name="login"),
    path("changepass/", UserChangePassHandler.as_view(), name="changepass"),
    path(
        "questionnaireteacher/",
        QuestionnaireTeacherHandler.as_view(),
        name="questionnaireteacherregestration",
    ),
    path("resetpass/", UserSendPwdResetMailHandler.as_view(), name="resetpass"),
    path("resetpass/confirm/", UserResetPassHandler.as_view(), name="resetpass_change"),
    path("im/", LoggedUserProfileHandler.as_view(), name="im"),
    path("im/update/", UserProfileUpdateHandler.as_view(), name="im_update"),
    path("profile/<int:pk>/", UserProfileHandler.as_view(), name="im"),
]
