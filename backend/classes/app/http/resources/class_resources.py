from rest_framework.serializers import ModelSerializer

from comment_resources import CommentResource
from classes.models import Class


class ClassResource(ModelSerializer):
    comments = CommentResource(many=True)

    class Meta:
        model = Class
        fields = [
            "id",
            "name",
            "description",
            "is_single",
            "start_datetime",
            "comments",
        ]
