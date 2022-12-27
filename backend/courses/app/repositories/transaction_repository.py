from typing import Optional

from core.app.repositories.base_repository import BaseRepository
from courses.models import TicketTransaction


class TicketTransactionRepository(BaseRepository):
    model = TicketTransaction

    def store(self, transaction: TicketTransaction) -> None:
        transaction.save()

    def find_by_id(self, id_: str) -> Optional[TicketTransaction]:
        return self.model.objects.filter(pk=id_).first()
