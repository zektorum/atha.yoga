from typing import NamedTuple

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from rest_framework_simplejwt.tokens import RefreshToken, Token


class User(AbstractUser):
    # from AbstractUser, modified:
    first_name = models.CharField(_('first name'), max_length=100, blank=False)
    last_name = models.CharField(_('last name'), max_length=100, blank=False)
    email = models.EmailField(_('email address'), unique=True, blank=False)

    about = models.CharField(max_length=100, blank=True)
    avatar = models.ImageField(upload_to='user_avatars/', blank=True)
    is_instructor = models.BooleanField()


class UserToken(NamedTuple):
    refresh: str
    access: str


def get_tokens_for_user(user: User) -> UserToken:
    refresh = RefreshToken.for_user(user)
    user_token = UserToken(str(refresh), str(refresh.access_token))
    return user_token


def refresh_auth_token(token: Token) -> str:
    refresh = RefreshToken(token)
    return str(refresh.access_token)
