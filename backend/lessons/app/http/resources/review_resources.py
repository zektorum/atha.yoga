from rest_framework.serializers import ModelSerializer

from lessons.models import LessonReview
from core.models import User


class LessonReviewUserResource(ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "first_name",
            "last_name",
            "email",
            "about",
            "avatar",
            "is_teacher",
        ]


class LessonReviewResource(ModelSerializer):
    user = LessonReviewUserResource()

    class Meta:
        model = LessonReview
        fields = [
            "id",
            "text",
            "star_rating",
            "user",
            "created_at",
        ]
