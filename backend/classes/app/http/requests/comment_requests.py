from rest_framework import serializers
from core.app.utils.serializers import UnimplementedSerializer


class CommentAddRequest(UnimplementedSerializer):
    email = serializers.EmailField()
    text = serializers.CharField(max_length=512)
    class_id = serializers.IntegerField(min_value=1)


class CommentsGetRequest(UnimplementedSerializer):
    class_id = serializers.IntegerField(min_value=1)
