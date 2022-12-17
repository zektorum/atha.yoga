from django.db.models import QuerySet

from core.app.repositories.base_repository import BaseRepository
from lessons.models import LessonReview, Lesson


class LessonReviewRepository(BaseRepository):
    model = LessonReview

    def store(self, review: LessonReview) -> None:
        review.save()

    def find_by_lesson_id(self, lesson_id: int) -> QuerySet[LessonReview]:
        return self.model.objects.filter(lesson_id=lesson_id)

    def find_by_id(self, id_: int) -> LessonReview:
        return self.model.objects.filter(pk=id_).first()

    def check_for_user_review(self, user_id: int, lesson: Lesson) -> bool:
        return lesson.reviews.filter(user_id=user_id).exists()

    def remove(self, review: LessonReview) -> None:
        review.delete()
