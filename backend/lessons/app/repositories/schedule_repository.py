from typing import List, Optional

from core.app.repositories.base_repository import BaseRepository
from lessons.models import Schedule


class ScheduleRepository(BaseRepository):
    model = Schedule

    def bulk_create(self, objs: List[Schedule]) -> None:
        self.model.objects.bulk_create(objs)

    def find(self, id_: int) -> Optional[Schedule]:
        return self.model.objects.filter(pk=id_).first()
