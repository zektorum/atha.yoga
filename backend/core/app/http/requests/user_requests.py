from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from backend.core.app.utils.serializers import UnimplementedSerializer


class UserRegisterRequest(UnimplementedSerializer):
    email = serializers.EmailField()
    password = serializers.CharField()
    password_confirmation = serializers.CharField()

    def validate(self, attrs: dict) -> dict:
        if attrs["password"] != attrs["password_confirmation"]:
            raise ValidationError(
                "`password` and `password_confirmation` should be equal"
            )
        return attrs
