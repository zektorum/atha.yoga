from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    first_name = models.CharField(_("first name"), max_length=100, blank=False)
    last_name = models.CharField(_("last name"), max_length=100, blank=False)
    email = models.EmailField(_("email address"), unique=True, blank=False)

    about = models.CharField(max_length=100, blank=True)
    avatar = models.ImageField(upload_to="user_avatars/", blank=True)
    is_teacher = models.BooleanField(default=False)
