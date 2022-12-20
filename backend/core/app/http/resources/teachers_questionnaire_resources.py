from rest_framework.serializers import ModelSerializer

from core.models import QuestionnaireTeacher


class QuestionnaireTeacherResource(ModelSerializer):
    class Meta:
        model = QuestionnaireTeacher
        fields = [
            "id",
            "user",
            "name",
            "surname",
            "date_of_birth",
            "gender",
            "about_me",
            "work_experience",
            "vk_link",
            "telegram_link",
            "status",
        ]
