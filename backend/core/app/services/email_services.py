from django.core.mail import EmailMessage, EmailMultiAlternatives
from django.conf import settings
from django.template.loader import render_to_string
from core.app.services.types import TextMailData, HtmlMailData


class SimpleEmailTextService:
    def __init__(self, data: TextMailData):
        self.data = data

    def send(self) -> None:
        email = EmailMessage(
            subject=self.data.subject,
            body=self.data.message,
            from_email=settings.EMAIL_HOST_USER,
            to=self.data.receivers,
        )
        email.send(fail_silently=False)


class EmailHtmlService:
    def __init__(self, data: HtmlMailData):
        self.data = data

    def send(self, context: dict) -> None:
        html_body = render_to_string(self.data.template_path, context)
        email = EmailMultiAlternatives(
            subject=self.data.subject,
            body=self.data.message,
            from_email=settings.EMAIL_HOST_USER,
            to=self.data.receivers,
        )
        email.attach_alternative(html_body, "text/html")
        email.send(fail_silently=False)
