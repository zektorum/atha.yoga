from rest_framework.serializers import ModelSerializer

from core.models import QuestionnaireTeacher


class QuestionnaireTeacherResource(ModelSerializer):
    class Meta:
        model = QuestionnaireTeacher
        fields = [
            'id',
            'first_name',
            'last_name',
            'date_birth',
            'gender',
            'about_me',
            'work_experience',
            'vk_link',
            'telegram_link',
            'certificate_photos',
            'passport_photo',
            'user_photo'
        ]