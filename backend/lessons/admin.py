from django.contrib import admin
from .models import Lesson, Schedule, Comment


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


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "user",
        "lesson",
        "created_at",
    )
    list_filter = ("created_at",)
    date_hierarchy = "created_at"
