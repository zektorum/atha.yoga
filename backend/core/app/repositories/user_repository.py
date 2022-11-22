from rest_framework.exceptions import PermissionDenied

from core.app.repositories.base_repository import BaseRepository
from core.models import User


class UserRepository(BaseRepository):
    model = User

    def store(self, user: User) -> None:
        user.save()

    def find_user_by_email(self, email: str) -> User:
        user = User.objects.filter(email=email).first()
        if not user:
            raise PermissionDenied("no user with this email")
        return user
