from django.db import models

from core.models import User, TimeStampedModel


class LessonTypes(models.TextChoices):
    ONLINE = "ONLINE"
    VIDEO = "VIDEO"


class LessonLevels(models.TextChoices):
    STARTING = "STARTING"
    CONTINUER = "CONTINUER"
    ADVANCED = "ADVANCED"


class LessonPrices(models.TextChoices):
    PAYMENT = "PAYMENT"
    DONATION = "DONATION"
    FREE = "FREE"


class LessonComplexities(models.TextChoices):
    EASY = "EASY"
    MEDIUM = "MEDIUM"
    HARD = "HARD"


class Lesson(TimeStampedModel):
    name = models.CharField(max_length=64)
    description = models.TextField(blank=True)
    lesson_type = models.CharField(max_length=30, choices=LessonTypes.choices)
    level = models.CharField(max_length=30, choices=LessonLevels.choices)
    single = models.BooleanField(default=False)
    duration = models.DurationField()
    start_datetime = models.DateTimeField()
    complexity = models.CharField(max_length=30, choices=LessonComplexities.choices)
    price = models.CharField(max_length=30, choices=LessonPrices.choices)
    cost = models.FloatField(null=True)
    teacher = models.ForeignKey(User, on_delete=models.CASCADE)


class Comment(TimeStampedModel):
    text = models.TextField(max_length=512)
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    lesson = models.ForeignKey(
        Lesson, related_name="comments", on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)
