from backend.core.app.services.types import UserRegisterData
from core.models import User


class UserRegister:
    def __init__(self, data: UserRegisterData):
        self._data = data

    def register(self) -> User:
        user = User()
        user.username = user.email = self._data["email"]
        user.set_password(self._data["password"])
        user.save()

        return user
