from typing import NamedTuple

from rest_framework_simplejwt.tokens import RefreshToken, Token

from core.models import User


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
