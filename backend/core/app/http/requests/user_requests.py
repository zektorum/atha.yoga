from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from core.app.utils.serializers import UnimplementedSerializer


class UserRegisterRequest(UnimplementedSerializer):
    email = serializers.EmailField()
    password = serializers.CharField(min_length=8, max_length=128)
    password_confirmation = serializers.CharField(min_length=8, max_length=128)

    def validate(self, attrs: dict) -> dict:
        if attrs["password"] != attrs["password_confirmation"]:
            raise ValidationError(
                "`password` and `password_confirmation` should be equal"
            )
        return attrs


class UserLoginRequest(UnimplementedSerializer):
    email = serializers.EmailField()
    password = serializers.CharField(min_length=8, max_length=128)


class UserChangePassRequest(UnimplementedSerializer):
    email = serializers.EmailField()
    password = serializers.CharField(min_length=8, max_length=128)
    new_password = serializers.CharField(min_length=8, max_length=128)

    def validate(self, attrs: dict) -> dict:
        if attrs["password"] == attrs["new_password"]:
            raise ValidationError("old and new passwords shouldn't be equal")
        return attrs
