from typing import Optional

from core.app.repositories.base_repository import BaseRepository
from classes.models import Class


class ClassRepository(BaseRepository):
    model = Class

    def store(self, class_: Class) -> None:
        class_.save()

    def find_class_by_id(self, _id: int) -> Optional[Class]:
        _class = Class.objects.filter(pk=_id).first()
        return _class
