from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from core.app.utils.serializers import UnimplementedSerializer
from lessons.models import LessonComplexities


class LessonFilterRequest(UnimplementedSerializer):
    query = serializers.CharField(max_length=100)
    complexity = serializers.ChoiceField(choices=LessonComplexities.choices)
    start_datetime = serializers.DateTimeField()
    day = serializers.IntegerField(min_value=1, max_value=7)
    end_datetime = serializers.DateTimeField()

    def validate(self, attrs: dict) -> dict:
        if "end_datetime" in attrs and "start_datetime" in attrs:
            if attrs["end_datetime"] < attrs["start_datetime"]:
                raise ValidationError("start_datetime must be less than end_datetime")
        return attrs
