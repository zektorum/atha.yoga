from rest_framework import serializers

from core.app.utils.serializers import UnimplementedSerializer
from core.models import GenderTypes


class QuestionnaireTeacherRequest(UnimplementedSerializer):
    name = serializers.CharField(max_length=30)
    surname = serializers.CharField(max_length=30)
    date_of_birth = serializers.DateField()
    gender = serializers.ChoiceField(choices=GenderTypes.choices)
    about_me = serializers.CharField(max_length=3000)
    work_experience = serializers.CharField(max_length=1000)
    vk_link = serializers.URLField()
    telegram_link = serializers.URLField()
    certificate_photos = serializers.ListField(child=serializers.ImageField())
    passport_photos = serializers.ListField(child=serializers.ImageField())
    user_photos = serializers.ListField(child=serializers.ImageField())
