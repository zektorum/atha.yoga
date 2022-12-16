from typing import List, Union

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from polymorphic.models import PolymorphicModel


class TimeStampedModel(models.Model):
    id = models.BigAutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True, db_index=False)
    updated_at = models.DateTimeField(auto_now=True, db_index=False)

    class Meta(object):
        abstract = True
        ordering = ["-id"]


class Attachment(PolymorphicModel):
    image = models.ImageField()
    created_at = models.DateTimeField(auto_now_add=True, db_index=False)
    updated_at = models.DateTimeField(auto_now=True, db_index=False)

    class Meta(object):
        abstract = True


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
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"


class GenderTypes(models.TextChoices):
    MALE = "MALE"
    FEMALE = "FEMALE"


class QuestionnaireTeacherStatuses(models.TextChoices):
    MODERATION = "MODERATION"
    ACCEPTED = "ACCEPTED"
    DECLINED = "DECLINED"


class QuestionnaireTeacher(TimeStampedModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(_("name"), max_length=30)
    surname = models.CharField(_("surname"), max_length=30)
    date_of_birth = models.DateField(_("date of birth"))
    gender = models.CharField(
        _("gender"), max_length=10, choices=GenderTypes.choices, null=True
    )
    about_me = models.CharField(_("about my self"), max_length=3000)
    work_experience = models.CharField(_("work_experience"), max_length=1000)
    vk_link = models.URLField(_("vk link"), max_length=200, blank=True)
    telegram_link = models.URLField(_("telegram link"), max_length=200, blank=True)
    status = models.CharField(
        max_length=30,
        choices=QuestionnaireTeacherStatuses.choices,
        default=QuestionnaireTeacherStatuses.MODERATION,
    )

    class Meta:
        verbose_name = "Анкета преподавателя"
        verbose_name_plural = "Анкета преподавателя"


class QuestionnaireTeacherCertificatePhoto(Attachment):
    image = models.ImageField(upload_to="user_certificate/")
    questionnaire = models.ForeignKey(QuestionnaireTeacher, on_delete=models.CASCADE)


class QuestionnaireTeacherPassportPhoto(Attachment):
    image = models.ImageField(upload_to="user_passport/")
    questionnaire = models.ForeignKey(QuestionnaireTeacher, on_delete=models.CASCADE)


class QuestionnaireTeacherUserPhoto(Attachment):
    image = models.ImageField(upload_to="user_avatars/")
    questionnaire = models.ForeignKey(QuestionnaireTeacher, on_delete=models.CASCADE)
