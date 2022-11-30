from django.urls import path
from core import views
from core.app.handlers.user_handlers import UserRegisterHandler, UserLoginHandler, UserChangePassHandler, MailSendTextHandler, MailSendHTMLHandler


urlpatterns = [
    path("register/", UserRegisterHandler.as_view(), name="registration"),
    path("login/", UserLoginHandler.as_view(), name="login"),
    path("changepass/", UserChangePassHandler.as_view(), name="changepass"),
    path("send_text/", MailSendTextHandler.as_view(), name="send_text"),
    path("send_html/", MailSendHTMLHandler.as_view(), name="send_HTML"),

]
