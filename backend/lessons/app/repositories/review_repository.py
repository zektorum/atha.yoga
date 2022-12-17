from django.db.models import QuerySet

from core.app.repositories.base_repository import BaseRepository
from lessons.models import LessonReview


class LessonReviewRepository(BaseRepository):
    model = LessonReview

    def store(self, review: LessonReview) -> None:
        review.save()

    def find_by_lesson_id(self, lesson_id: int) -> QuerySet[LessonReview]:
        return self.model.objects.filter(lesson_id=lesson_id)

    def find_by_id(self, id_: int) -> LessonReview:
        return self.model.objects.filter(pk=id_).first()

    def remove(self, review: LessonReview) -> None:
        review.delete()
