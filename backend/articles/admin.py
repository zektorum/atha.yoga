from django.contrib import admin
from django_mptt_admin.admin import DjangoMpttAdmin

from articles.models import Article, Category, ArticleComment, Tag


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "author",
        "rating",
        "category",
        "is_draft",
        "created_at",
        "updated_at",
    )
    list_filter = (
        "is_draft",
        "category",
        "rating",
        "created_at",
        "updated_at",
    )
    date_hierarchy = "created_at"
    prepopulated_fields = {"slug": ("title",)}


@admin.register(Category)
class CategoryAdmin(DjangoMpttAdmin):
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(ArticleComment)
class ArticleCommentAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "polymorphic_ctype",
        "text",
        "user",
        "created_at",
        "article",
    )
    list_filter = ("created_at",)
    date_hierarchy = "created_at"
