from rest_framework.serializers import ModelSerializer

from lessons.models import Lesson


class LessonResource(ModelSerializer):
    class Meta:
        model = Lesson
        fields = [
            "id",
            "name",
            "description",
            "lesson_type",
            "level",
            "single",
            "duration",
            "start_datetime",
            "price",
            "cost",
            "teacher",
        ]
