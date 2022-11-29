from rest_framework.serializers import ModelSerializer

from lessons.models import Comment
from core.models import User


class CommentUserResource(ModelSerializer):
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


class CommentResource(ModelSerializer):
    user = CommentUserResource()

    class Meta:
        model = Comment
        fields = [
            "id",
            "text",
            "user",
            "created_at",
        ]
