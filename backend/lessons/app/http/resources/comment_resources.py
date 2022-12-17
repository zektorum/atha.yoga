from rest_framework.serializers import ModelSerializer

from lessons.models import LessonComment
from core.models import User


class LessonCommentUserResource(ModelSerializer):
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


class LessonCommentResource(ModelSerializer):
    user = LessonCommentUserResource()

    class Meta:
        model = LessonComment
        fields = [
            "id",
            "text",
            "user",
            "created_at",
        ]
