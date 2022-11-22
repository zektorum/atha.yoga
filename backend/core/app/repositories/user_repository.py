from core.app.repositories.base_repository import BaseRepository
from core.models import User


class UserRepository(BaseRepository):
    model = User

    def store(self, user: User) -> None:
        user.save()