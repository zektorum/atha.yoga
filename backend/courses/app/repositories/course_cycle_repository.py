from django.db.models import Q
from django.utils.timezone import now

from core.app.repositories.base_repository import BaseRepository
from courses.models import CourseCycle, Course


class CourseCycleRepository(BaseRepository):
    model = CourseCycle

    def store(self, cycle: CourseCycle) -> None:
        cycle.save()

    def current_course_cycle(self, course: Course) -> CourseCycle:
        current_date = now()
        return CourseCycle.objects.filter(
            Q(
                Q(start_at__lte=current_date, end_at__gte=current_date)
                | Q(start_at__gte=current_date)
            ),
            course_id=course.id,
        ).first()
