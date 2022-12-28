from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from polymorphic.models import PolymorphicModel

from core.models import User, TimeStampedModel, Transaction


class CourseTypes(models.TextChoices):
    ONLINE = "ONLINE"
    VIDEO = "VIDEO"


class CourseLevels(models.TextChoices):
    STARTING = "STARTING"
    CONTINUER = "CONTINUER"
    ADVANCED = "ADVANCED"


class CoursePaymentTypes(models.TextChoices):
    PAYMENT = "PAYMENT"
    DONATION = "DONATION"
    FREE = "FREE"


class CourseComplexities(models.TextChoices):
    EASY = "EASY"
    MEDIUM = "MEDIUM"
    HARD = "HARD"


class RepetitionWeekdays(models.IntegerChoices):
    MONDAY = 0
    TUESDAY = 1
    WEDNESDAY = 2
    THURSDAY = 3
    FRIDAY = 4
    SATURDAY = 5
    SUNDAY = 6


class Course(TimeStampedModel):
    name = models.CharField(max_length=64)
    description = models.TextField()
    course_type = models.CharField(max_length=30, choices=CourseTypes.choices)
    level = models.CharField(max_length=30, choices=CourseLevels.choices)
    single = models.BooleanField(default=False)
    duration = models.DurationField()
    start_datetime = models.DateTimeField()
    deadline_datetime = models.DateTimeField(null=True)
    complexity = models.CharField(max_length=30, choices=CourseComplexities.choices)
    teacher = models.ForeignKey(User, on_delete=models.CASCADE)
    link = models.URLField()
    link_info = models.CharField(max_length=100, blank=True)
    repeat_editing = models.BooleanField(default=False)
    payment = models.CharField(max_length=30, choices=CoursePaymentTypes.choices)
    price = models.FloatField(validators=(MinValueValidator(limit_value=0),))

    favorites = models.ManyToManyField(
        User, related_name="favorite_courses", blank=True
    )

    class Meta:
        verbose_name = "Занятие"
        verbose_name_plural = "Занятия"


class Review(PolymorphicModel, TimeStampedModel):
    text = models.TextField()
    star_rating = models.IntegerField(
        validators=(MinValueValidator(limit_value=1), MaxValueValidator(limit_value=5))
    )
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"


class CourseReview(Review):
    course = models.ForeignKey(Course, related_name="reviews", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Отзыв о курсе"
        verbose_name_plural = "Отзывы о курсе"


class Lesson(TimeStampedModel):
    course = models.ForeignKey(Course, related_name="lessons", on_delete=models.CASCADE)
    start_at = models.DateTimeField()
    participants = models.ManyToManyField(User)

    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"
        ordering = ("id",)


class Comment(PolymorphicModel):
    text = models.TextField(max_length=512)
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"


class CourseComment(Comment):
    course = models.ForeignKey(
        Course, related_name="comments", on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = "Комментарий к курсу"
        verbose_name_plural = "Комментарии к курсу"


class Ticket(TimeStampedModel):
    course = models.ForeignKey(Course, on_delete=models.DO_NOTHING)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    amount = models.IntegerField()

    class Meta:
        verbose_name = "Билет"
        verbose_name_plural = "Билеты"


class TicketTransaction(Transaction):
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    ticket_amount = models.IntegerField()
