from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    # from AbstractUser, modified:
    first_name = models.CharField(_('first name'), max_length=100, blank=False)
    last_name = models.CharField(_('last name'), max_length=100, blank=False)
    email = models.EmailField(_('email address'), unique=True, blank=False)

    about = models.CharField(max_length=100, blank=True)
    image = models.ImageField(upload_to='user_images/', blank=True)
    is_instructor = models.BooleanField()
