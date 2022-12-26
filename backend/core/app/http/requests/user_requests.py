from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from core.app.utils.serializers import UnimplementedSerializer, PasswordField


class UserRegisterRequest(UnimplementedSerializer):
    email = serializers.EmailField()
    password = PasswordField()
    password_confirmation = serializers.CharField(min_length=8, max_length=128)

    def validate(self, attrs: dict) -> dict:
        if attrs["password"] != attrs["password_confirmation"]:
            raise ValidationError(
                "`password` and `password_confirmation` should be equal"
            )
        return attrs


class UserLoginRequest(UnimplementedSerializer):
    email = serializers.EmailField()
    password = PasswordField()


class UserChangePassRequest(UnimplementedSerializer):
    email = serializers.EmailField()
    password = PasswordField()
    new_password = PasswordField()

    def validate(self, attrs: dict) -> dict:
        if attrs["password"] == attrs["new_password"]:
            raise ValidationError("old and new passwords shouldn't be equal")
        return attrs


class SendTextRequest(UnimplementedSerializer):
    subject = serializers.CharField(min_length=0, max_length=100)
    message = serializers.CharField(min_length=0, max_length=10000)
    receivers = serializers.ListField(min_length=1)


class SendHTMLRequest(UnimplementedSerializer):
    subject = serializers.CharField(min_length=0, max_length=100)
    message = serializers.CharField(min_length=0, max_length=10000)
    receivers = serializers.ListField(min_length=1)


class UserSendPwdResetMailRequest(UnimplementedSerializer):
    email = serializers.EmailField()


class UserResetPassRequest(UnimplementedSerializer):
    pwd_reset_token = serializers.CharField(max_length=128)
    email = serializers.EmailField()
    new_password = PasswordField()


class UserProfileUpdateRequest(UnimplementedSerializer):
    username = serializers.CharField(max_length=150)
    first_name = serializers.CharField(max_length=100)
    last_name = serializers.CharField(max_length=100)
    about = serializers.CharField(max_length=100)
    avatar = serializers.ImageField()
