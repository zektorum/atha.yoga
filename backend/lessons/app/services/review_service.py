from functools import cached_property

from rest_framework.exceptions import NotFound, PermissionDenied
from core.models import User
from lessons.app.repositories.review_repository import LessonReviewRepository
from lessons.app.repositories.lesson_repository import LessonRepository
from lessons.app.services.types import LessonReviewCreateData
from lessons.models import LessonReview


class LessonReviewCreate:
    repository = LessonReviewRepository()
    lesson_repository = LessonRepository()

    def __init__(self, lesson_id: int, data: LessonReviewCreateData, user: User):
        self.data = data
        self.user = user
        self.lesson_id = lesson_id

    @cached_property
    def review(self) -> LessonReview:
        lesson = self.lesson_repository.find_by_id(id_=self.lesson_id)
        if not lesson:
            raise NotFound(f"Undefined lesson with id {self.lesson_id}")
        if lesson.teacher.id == self.user.id:
            raise PermissionDenied("Teacher can't review own lesson")
        if lesson.reviews.filter(user_id=self.user.id).exists():
            raise PermissionDenied("User can't review lesson twice")

        review = LessonReview()
        review.user = self.user
        review.lesson = lesson
        review.text = self.data["text"]
        review.star_rating = self.data["star_rating"]

        self.repository.store(review=review)
        return review

    def create(self) -> LessonReview:
        return self.review


class LessonReviewRemove:
    repository = LessonReviewRepository()

    def __init__(self, lesson_id: int, review_id: int, user: User):
        self.lesson_id = lesson_id
        self.review_id = review_id
        self.user = user

    @cached_property
    def review(self) -> LessonReview:
        review = self.repository.find_by_id(id_=self.review_id)
        if not review:
            raise NotFound(f"Undefined review with id {self.review_id}")
        if review.lesson.id != self.lesson_id:
            raise NotFound(
                f"Undefined review with id {self.review_id} for lesson with id {self.lesson_id}"
            )
        if review.user.id != self.user.id:
            raise PermissionDenied(
                f"User with id {self.user.id} can't remove review with id {self.review_id}"
            )

        return review

    def remove(self) -> LessonReview:
        self.repository.remove(review=self.review)
        return self.review
