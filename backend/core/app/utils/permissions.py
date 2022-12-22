from django.conf import settings
from django.core.cache import cache
from datetime import datetime, timedelta
from typing import TypedDict
from functools import wraps
from rest_framework.exceptions import Throttled
import requests
from rest_framework.permissions import BasePermission
from rest_framework.request import Request
from rest_framework.views import APIView

from core.models import UserRoles


class SenderInfo(TypedDict):
    count: int
    time: datetime


class ReCaptcha(object):

    def __init__(self, decorated_method_name: str):
        self.decorated_method_name = decorated_method_name

    def __call__(self, func):
        @wraps(func)
        def wrapper(self_, request, *args, **kwargs):
            sender, sender_info = self.get_sender(request)
            time = datetime.now() - sender_info["time"]
            counter = sender_info["count"] + 1
            if counter >= 5 and time < timedelta(days=1):
                captcha = self.check_recaptcha(request)
                if not captcha:
                    raise Throttled
                sender_info["count"] = -1
                sender_info["time"] = datetime.now()
            sender_info["count"] = counter
            cache.set(f"{sender}", sender_info)
            return func(self_, request, *args, **kwargs)
        return wrapper

    def get_sender(self, request):
        try:
            sender = request.user.email
        except:
            sender = self.get_ip(request)
        try:
            sender_info: SenderInfo = {"count": cache.get(f"{sender}")["count"], "time": cache.get(f"{sender}")["time"]}
        except:
            sender_info: SenderInfo = {"count": 0, "time": datetime.now()}
        return sender, sender_info

    def get_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip

    def check_recaptcha(self, request):
        recaptcha_response = request.POST.get('g-recaptcha-response')
        data = {
            'secret': settings.RECAPTCHA_PRIVATE_KEY,
            'response': recaptcha_response
        }
        r = requests.post('https://www.google.com/recaptcha/api/siteverify', data=data)
        result = r.json()
        return result['success']



class IsTeacher(BasePermission):
    """
    Allows access only to users with TEACHER role.
    """

    def has_permission(self, request: Request, view: APIView) -> bool:
        return bool(
            request.user
            and request.user.is_authenticated
            and request.user.has_role(UserRoles.TEACHER)
        )
