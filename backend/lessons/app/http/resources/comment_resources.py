from rest_framework.serializers import ModelSerializer

from core.models import User
from lessons.models import LessonComment


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
