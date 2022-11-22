from typing import Optional

from core.app.repositories.base_repository import BaseRepository
from core.models import User
from django.db.models import Q


class UserRepository(BaseRepository):
    model = User

    def store(self, user: User) -> None:
        user.save()

    def find_user_by_login_data(self, login: str, password: str) -> Optional[User]:
        user = User.objects.filter(Q(username=login) | Q(email=login)).first()
        if user and user.check_password(password):
            return user
        return None
