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


class User(AbstractUser):
    first_name = models.CharField(_("first name"), max_length=100)
    last_name = models.CharField(_("last name"), max_length=100)
    email = models.EmailField(_("email address"), unique=True)

    about = models.CharField(max_length=100, blank=True)
    avatar = models.ImageField(upload_to="user_avatars/", blank=True)
    is_teacher = models.BooleanField(default=False)
