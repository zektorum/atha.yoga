from django.db import models
from core.models import User


class Class(models.Model):
    name = models.CharField(max_length=64, blank=False)
    description = models.TextField(max_length=512, blank=True)
    # type =
    # level =
    is_single = models.BooleanField(default=False)
    # connectedness =
    # duration =
    start_datetime = models.DateTimeField(blank=False)
    # price =
    # cost =
    # teacher =


class Comment(models.Model):
    text = models.TextField(max_length=512, blank=False)
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    _class = models.ForeignKey(Class, related_name="comments", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
