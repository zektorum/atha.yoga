from rest_framework.serializers import ModelSerializer

from comment_resources import CommentResource
from lessons.models import Lesson


class ClassResource(ModelSerializer):
    comments = CommentResource(many=True)

    class Meta:
        model = Lesson
        fields = [
            "id",
            "name",
            "description",
            "is_single",
            "start_datetime",
            "comments",
        ]
