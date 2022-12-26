from django.contrib import admin
from django.core.handlers.wsgi import WSGIRequest

from .admin_actions import accept_questionnaires, decline_questionnaires
from .models import User, QuestionnaireTeacher


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "username",
        "email",
        "first_name",
        "last_name",
        "roles",
        "is_active",
        "is_staff",
        "is_superuser",
    )
    list_display_links = ("id", "username", "email")
    list_filter = (
        "last_login",
        "date_joined",
        "is_active",
        "is_staff",
        "is_superuser",
    )
    search_fields = ("username", "email", "first_name", "last_name")
    raw_id_fields = ("groups", "user_permissions")


@admin.register(QuestionnaireTeacher)
class QuestionnaireTeacherAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "status",
        "user",
        "name",
        "surname",
        "date_of_birth",
        "gender",
        "about_me",
        "work_experience",
        "vk_link",
        "telegram_link",
        "user_photo",
        "passport_photo",
        "user_with_passport_photo",
        "created_at",
        "updated_at",
    )
    list_filter = ("created_at", "updated_at", "user", "date_of_birth")
    raw_id_fields = ("certificate_photos",)
    search_fields = ("name",)
    date_hierarchy = "created_at"
    actions = [accept_questionnaires, decline_questionnaires]

    def has_add_permission(self, request: WSGIRequest) -> bool:
        return False

    def has_delete_permission(
        self, request: WSGIRequest, obj: QuestionnaireTeacher = None
    ) -> bool:
        return False

    def has_change_permission(
        self, request: WSGIRequest, obj: QuestionnaireTeacher = None
    ) -> bool:
        return False
