from rest_framework import serializers

from core.app.utils.serializers import UnimplementedSerializer
from core.models import GenderTypes, QuestionnaireTeacher


class QuestionnaireTeacherRequest(UnimplementedSerializer):
    name = serializers.CharField(max_length=30)
    surname = serializers.CharField(max_length=30)
    date_of_birth = serializers.DateField()
    gender = serializers.ChoiceField(choices=GenderTypes.choices)
    about_me = serializers.CharField(max_length=3000)
    work_experience = serializers.CharField(max_length=1000)
    vk_link = serializers.CharField(max_length=50)
    telegram_link = serializers.CharField(max_length=50)
    certificate_photos = serializers.SerializerMethodField()
    passport_photo = serializers.SerializerMethodField()
    user_photo = serializers.SerializerMethodField()

    class Meta:
        model = QuestionnaireTeacher
        fields = ('name', 'surname', 'date_of_birth', 'gender', 'about_me', 'work_experience', 'vk_link',
                  'telegram_link', 'certificate_photos', 'passport_photo', 'user_photo')

    def get_photo_url(self, questionnaire):
        request = self.context.get('request')
        photo_url = questionnaire.photo.url
        return request.build_absolute_uri(photo_url)
