from typing import Optional

from django.db.models import QuerySet, Prefetch, OuterRef

from core.app.repositories.base_repository import BaseRepository
from core.models import User, QuestionnaireTeacher, QuestionnaireTeacherStatuses
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

    def find_user_tickets(self, user_id: int) -> QuerySet[Ticket]:
        return self.model.objects.filter(user_id=user_id)

    def fetch_relations(self, queryset: QuerySet[Ticket]) -> QuerySet[Ticket]:
        return queryset.select_related("course__base_course__teacher").prefetch_related(
            Prefetch(
                "course__base_course__teacher",
                queryset=User.objects.filter(
                    pk=OuterRef("teacher_id")
                ).prefetch_related(
                    Prefetch(
                        "teacher_profiles",
                        queryset=QuestionnaireTeacher.objects.filter(
                            user_id=OuterRef("id"),
                            status=QuestionnaireTeacherStatuses.ACCEPTED,
                        ),
                    )
                ),
            ),
        )
