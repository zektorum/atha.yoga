from django.core.mail import EmailMessage, EmailMultiAlternatives
from django.conf import settings
from django.shortcuts import redirect
from django.template.loader import render_to_string
from core.app.services.types import TextMailData, HtmlMailData


class SimpleEmailTextService:
    def __init__(self, data: TextMailData):
        self.data = data

    def send(self) -> None:
        subject = self.data["subject"]
        message = self.data["message"]
        receivers = self.data["receivers"]
        email = EmailMessage(
            subject=subject,
            body=message,
            from_email=settings.EMAIL_HOST_USER,
            to=receivers,
        )
        email.send(fail_silently=False)


class EmailHtmlService:
    def __init__(self, data: HtmlMailData):
        self.data = data

    def send(self, context: dict) -> None:
        subject = self.data["subject"]
        message = self.data["message"]
        receivers = self.data["receivers"]
        template = self.data["template_path"]
        html_body = render_to_string(template, context)
        email = EmailMultiAlternatives(
            subject=subject,
            body=message,
            from_email=settings.EMAIL_HOST_USER,
            to=receivers,
        )
        email.attach_alternative(html_body, "text/html")
        email.send(fail_silently=False)
