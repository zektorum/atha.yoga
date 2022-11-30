from django.core.mail import EmailMessage, send_mail
from django.conf import settings
from django.shortcuts import render

# def sendmail(request) -> None:
#     if request.method == 'POST':
#         subject = request.POST['subject']
#         message = request.POST['message']
#         receivers = request.POST['receivers'].split()
#         email = EmailMessage(
#                 subject,
#                 message,
#                 settings.EMAIL_HOST_USER,
#                 receivers
#                 )
#         email.send(fail_silently=False)
#     return render(request, 'email_template.html')

def success(request):
    return render(request, 'success.html')

