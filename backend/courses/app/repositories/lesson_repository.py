from typing import List, Optional

from core.app.repositories.base_repository import BaseRepository
from core.models import User
from courses.models import Lesson


class LessonRepository(BaseRepository):
    model = Lesson

    def bulk_create(self, objs: List[Lesson]) -> None:
        self.model.objects.bulk_create(objs)

    def find_by_id(self, id_: int) -> Optional[Lesson]:
        return self.model.objects.filter(pk=id_).first()

    def find_by_id_creator(self, id_: int, user_id: int) -> Optional[Lesson]:
        return self.model.objects.filter(pk=id_, course__teacher_id=user_id).first()

    def is_participant(self, lesson: Lesson, user: User) -> Optional[Lesson]:
        return lesson.participants.filter(id=user.id)

    def add_participant(self, lesson: Lesson, user: User) -> None:
        return lesson.participants.add(user)
