from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from core.models import User, QuestionnaireTeacher


class TeacherProfileResource(ModelSerializer):
    class Meta:
        model = QuestionnaireTeacher
        fields = [
            "id",
            "name",
            "surname",
            "date_of_birth",
            "gender",
            "about_me",
            "work_experience",
            "vk_link",
            "telegram_link",
        ]


class UserResource(ModelSerializer):
    public_teacher_profiles = TeacherProfileResource(many=True, allow_null=True)
    rate = serializers.DecimalField(
        default=0, max_digits=None, decimal_places=3, coerce_to_string=False
    )

    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "first_name",
            "last_name",
            "email",
            "about",
            "avatar",
            "public_teacher_profiles",
            "rate",
        ]
