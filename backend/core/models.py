from typing import List, Union

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class TimeStampedModel(models.Model):
    id = models.BigAutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True, db_index=False)
    updated_at = models.DateTimeField(auto_now=True, db_index=False)

    class Meta(object):
        abstract = True
        ordering = ["-id"]


class UserRoles(models.TextChoices):
    STUDENT = "STUDENT"
    TEACHER = "TEACHER"
    MODERATOR = "MODERATOR"


def user_default_roles() -> List[Union[UserRoles, str]]:
    return [UserRoles.STUDENT]


class User(AbstractUser):
    first_name = models.CharField(_("first name"), max_length=100)
    last_name = models.CharField(_("last name"), max_length=100)
    email = models.EmailField(_("email address"), unique=True)

    about = models.CharField(max_length=100, blank=True)
    avatar = models.ImageField(upload_to="user_avatars/", blank=True)
    is_teacher = models.BooleanField(default=False)
    roles = models.JSONField(default=user_default_roles)
    pwd_reset_token = models.CharField(_("pwd reset token"), max_length=300)

    def has_role(self, role: UserRoles) -> bool:
        return role in self.roles

    def add_roles(self, roles: List[UserRoles]) -> None:
        self.roles = list({*self.roles, *roles})

    def remove_role(self, role: UserRoles) -> None:
        if not self.has_role(role=role):
            return
        del self.roles[self.roles.index(role)]

    class Meta:
        verbose_name = "Пользователи"
        verbose_name_plural = "Пользователи"


class GenderTypes(models.TextChoices):
    MALE = "MALE"
    FEMALE = "FEMALE"


class QuestionnaireTeacher(TimeStampedModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(_("name"), max_length=30)
    surname = models.CharField(_("surname"), max_length=30)
    date_of_birth = models.DateField(_("date of birth"))
    gender = models.CharField(_("gender"), max_length=10, choices=GenderTypes.choices)
    about_me = models.CharField(_("about my self"), max_length=3000)
    work_experience = models.CharField(_("work_experience"), max_length=1000)
    vk_link = models.CharField(_("vk link"), max_length=50, blank=True)
    telegram_link = models.CharField(_("telegram link"), max_length=50, blank=True)
    certificate_photos = models.ImageField(upload_to="user_certificate/")
    passport_photo = models.ImageField(upload_to="user_passport/")
    user_photo = models.ImageField(upload_to="user_avatars/")

    class Meta:
        verbose_name = "Анкета преподавателя"
        verbose_name_plural = "Анкета преподавателя"
