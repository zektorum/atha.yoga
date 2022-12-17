from django.contrib import admin
from .models import Lesson, Schedule, LessonComment, LessonReview


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "teacher",
        "lesson_type",
        "level",
        "complexity",
        "payment",
        "price",
        "single",
        "start_datetime",
        "deadline_datetime",
        "repeat_editing",
        "created_at",
    )
    list_display_links = ("id", "name")
    list_filter = (
        "lesson_type",
        "level",
        "complexity",
        "payment",
        "single",
        "start_datetime",
        "deadline_datetime",
        "repeat_editing",
        "created_at",
    )
    search_fields = ("name",)
    date_hierarchy = "created_at"


@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "lesson",
        "weekday",
        "start_time",
        "created_at",
    )
    list_filter = ("created_at",)
    date_hierarchy = "created_at"


@admin.register(LessonComment)
class LessonCommentAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "user",
        "lesson",
        "created_at",
    )
    search_fields = ("text",)
    list_filter = ("created_at",)
    date_hierarchy = "created_at"


@admin.register(LessonReview)
class LessonReviewAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "user",
        "lesson",
        "star_rating",
        "created_at",
    )
    search_fields = ("text",)
    list_filter = ("star_rating", "created_at")
    date_hierarchy = "created_at"
