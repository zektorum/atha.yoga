from typing import Optional

from core.app.repositories.base_repository import BaseRepository
from core.models import User
from courses.models import Ticket


class TicketRepository(BaseRepository):
    model = Ticket

    def store(self, ticket: Ticket) -> None:
        ticket.save()

    def ticket_for_course(self, course_id: int, user: User) -> Optional[Ticket]:
        return self.model.objects.filter(course_id=course_id, user=user.id).first()

    def ticket_for_course_to_update(
        self, course_id: int, user: User
    ) -> Optional[Ticket]:
        return (
            self.model.objects.select_for_update()
            .filter(course_id=course_id, user=user.id)
            .first()
        )

    def find_by_id_to_update(self, id_: int, user: User) -> Optional[Ticket]:
        return (
            self.model.objects.select_for_update().filter(pk=id_, user=user.id).first()
        )
