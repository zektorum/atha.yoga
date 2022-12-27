from typing import Optional

from django.db.models import QuerySet, Q, F
from elasticsearch_dsl import Q as EQ
from rest_framework.exceptions import NotFound

from core.app.repositories.base_repository import BaseRepository
from core.models import User
from courses.app.repositories.types import CourseFilterData
from courses.documents import CourseDocument
from courses.models import Course


class CourseRepository(BaseRepository):
    model = Course

    def store(self, course: Course) -> None:
        course.save()

    def find_by_id(self, id_: int, raise_exception: bool = False) -> Optional[Course]:
        course = self.model.objects.filter(pk=id_).first()
        if not course and raise_exception:
            raise NotFound(f"Undefined course with id {id_}")
        return course

    def find_by_id_teacher(self, id_: int, teacher_id: int) -> Optional[Course]:
        return self.model.objects.filter(pk=id_, teacher_id=teacher_id).first()

    def find_user_favorite_courses(self, user: User) -> QuerySet[Course]:
        return user.favorite_courses.all()

    def add_user_favorite_course(self, user: User, course: Course) -> None:
        course.favorites.add(user)

    def remove_user_favorite_course(self, user: User, course: Course) -> None:
        course.favorites.remove(user)

    def filter(self, data: CourseFilterData) -> QuerySet[Course]:
        base_query = self.model.objects.all()
        filter_query = Q()
        if "query" in data:
            query = (
                CourseDocument.search()
                .query(
                    EQ(
                        "multi_match",
                        query=data["query"],
                        fields=["name", "description"],
                        fuzziness="AUTO:2,4",
                    )
                )
                .to_queryset()
            )
            if not query.exists():
                query = base_query.filter(
                    Q(name__icontains=data["query"])
                    | Q(description__icontains=data["query"])
                )
            base_query = query
        if "complexity" in data:
            filter_query &= Q(complexity=data["complexity"])
        if "start_datetime" in data:
            filter_query &= Q(start_datetime__date=data["start_datetime"].date())
        if "day" in data:
            filter_query &= Q(start_datetime__week_day=data["day"])
        if "end_datetime" in data:
            base_query = base_query.annotate(
                end_datetime=F("duration") + F("start_datetime")
            )
            filter_query &= Q(end_datetime__lte=data["end_datetime"])
        return base_query.filter(filter_query).order_by("-id")
