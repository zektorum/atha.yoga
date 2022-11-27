from rest_framework.relations import SlugRelatedField
from rest_framework.serializers import ModelSerializer

from classes.models import Comment


class CommentResource(ModelSerializer):
    user = SlugRelatedField(slug_field="username", read_only=True)

    class Meta:
        model = Comment
        fields = [
            "text",
            "user",
            "created_at",
        ]
