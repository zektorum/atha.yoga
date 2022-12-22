from rest_framework import serializers
from core.app.utils.serializers import UnimplementedSerializer


class LessonCommentCreateRequest(UnimplementedSerializer):
    text = serializers.CharField(max_length=512)
