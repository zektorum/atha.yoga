from functools import cached_property
from typing import Tuple
from random import randint

from rest_framework.exceptions import ValidationError, AuthenticationFailed

from core.app.repositories.user_repository import UserRepository
from core.app.services.types import (
    UserRegisterData,
    UserLoginData,
    UserChangePassData,
)
from core.app.services.email_services import SimpleEmailTextService
from core.app.utils.jwt import UserToken, get_tokens_for_user
from core.models import User
from core.app.services.types import TextMailData


class UserRegister:
    repository = UserRepository()

    def __init__(self, data: UserRegisterData):
        self.data = data

    @cached_property
    def user(self) -> User:
        user = User()
        if self.repository.find_user_by_email(self.data["email"]):
            raise ValidationError("User with this email already exists")
        user.username = user.email = self.data["email"]
        user.set_password(self.data["password"])
        self.repository.store(user=user)
        return user

    def register(self) -> Tuple[User, UserToken]:
        token_data = get_tokens_for_user(user=self.user)
        return self.user, token_data


class UserLogin:
    repository = UserRepository()

    def __init__(self, data: UserLoginData):
        self.data = data

    @cached_property
    def user(self) -> User:
        user = self.repository.find_user_by_email(self.data["email"])
        if not user or not user.check_password(self.data["password"]):
            raise AuthenticationFailed()
        return user

    def login(self) -> Tuple[User, UserToken]:
        token_data = get_tokens_for_user(self.user)
        return self.user, token_data


class UserChangePass:
    repository = UserRepository()

    def __init__(self, data: UserChangePassData):
        self.data = data

    @cached_property
    def user(self) -> User:
        user = self.repository.find_user_by_email(self.data["email"])
        if not user or not user.check_password(self.data["password"]):
            raise AuthenticationFailed()
        user.set_password(self.data["new_password"])
        self.repository.store(user=user)
        return user

    def change(self) -> Tuple[User, UserToken]:
        token_data = get_tokens_for_user(self.user)
        return self.user, token_data


class UserResetPass:
    repository = UserRepository()

    def reset(self, email) -> Tuple[User, int]:
        user = self.repository.find_user_by_email(email)
        pwd_reset_token = randint(100000, 999999)

        if not user:
            raise AuthenticationFailed("User with this email does not exist")
        SimpleEmailTextService(TextMailData(
            subject="Please reset your password",
            message=f"""Reset your Atha.Yoga password
            Click here: http://athayoga.su/?token={pwd_reset_token}/""",
            receivers=[email]
        )).send()
        user.pwd_reset_token = pwd_reset_token
        user.save(update_fields=["pwd_reset_token"])
        return user, pwd_reset_token

    def find_user(self, email) -> User:
        user = self.repository.find_user_by_email(email)
        return user

    def change(self, new_password, email, pwd_reset_token) -> Tuple[User, UserToken]:
        user = self.repository.find_user_by_email(email=email)
        if not user:
            raise AuthenticationFailed("User with this email does not exist")
        if pwd_reset_token != user.pwd_reset_token:
            raise AuthenticationFailed(f"Tokens don't match")
        user.set_password(new_password)
        self.repository.store(user=user)
        token_data = get_tokens_for_user(user)
        return user, token_data
