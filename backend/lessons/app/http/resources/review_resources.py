from rest_framework.serializers import ModelSerializer

from core.models import User
from lessons.models import LessonReview


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
