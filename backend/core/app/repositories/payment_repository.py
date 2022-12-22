from typing import Optional

from core.app.repositories.base_repository import BaseRepository
from core.models import Transaction


class PaymentRepository(BaseRepository):
    model = Transaction

    def find_by_id(self, id_: str) -> Optional[Transaction]:
        return self.model.objects.filter(pk=id_).first()
