from django.core.mail import EmailMessage, EmailMultiAlternatives
from django.conf import settings
from django.shortcuts import redirect
from django.template.loader import render_to_string
from core.app.services.types import SendTextData, SendHTMLData



class MailSendText:

    def __init__(self, data: SendTextData):
        self.data = data

    def send_text(self) -> None:
        subject = self.data['subject']
        message = self.data['message']
        receivers = self.data['receivers']
        email = EmailMessage(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            receivers
        )
        email.send(fail_silently=False)
        return redirect('success')


class MailSendHTML:

    def __init__(self, data: SendHTMLData):
        self.data = data

    def send_html(self) -> None:
        template = self.data['template_name']
        html_body = render_to_string(template)
        email = EmailMultiAlternatives(
            self.data['subject'],
            self.data['message'],
            settings.EMAIL_HOST_USER,
            self.data['receivers']
        )
        email.attach_alternative(html_body, "text/html")
        email.send(fail_silently=False)
        return redirect('success')