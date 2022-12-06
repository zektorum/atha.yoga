from django.contrib import admin
from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "username",
        "email",
        "first_name",
        "last_name",
        "is_teacher",
        "roles",
        "is_active",
        "is_staff",
        "is_superuser",
    )
    list_display_links = ("id", "username", "email")
    list_filter = (
        "is_teacher",
        "last_login",
        "date_joined",
        "is_active",
        "is_staff",
        "is_superuser",
    )
    search_fields = ("username", "email", "first_name", "last_name")
    raw_id_fields = ("groups", "user_permissions")
