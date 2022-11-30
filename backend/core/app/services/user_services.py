from functools import cached_property
from typing import Tuple

from rest_framework.exceptions import PermissionDenied, ValidationError

from core.app.repositories.user_repository import UserRepository
from core.app.services.types import UserRegisterData, UserLoginData, UserChangePassData
from core.app.utils.jwt import UserToken, get_tokens_for_user
from core.models import User


class UserRegister:
    repository = UserRepository()

    def __init__(self, data: UserRegisterData):
        self.data = data

    @cached_property
    def user(self) -> User:
        user = User()
        if self.repository.find_user_by_email(self.data["email"]):
             raise ValidationError('User with this email already exists')
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
            raise PermissionDenied()
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
            raise PermissionDenied()
        user.set_password(self.data["new_password"])
        self.repository.store(user=user)
        return user

    def change(self) -> Tuple[User, UserToken]:
        token_data = get_tokens_for_user(self.user)
        return self.user, token_data






