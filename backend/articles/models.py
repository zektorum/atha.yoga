from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from ckeditor.fields import RichTextField

from mptt.models import MPTTModel, TreeForeignKey
from core.models import TimeStampedModel, User
from core.models import Comment


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    class Meta:
        verbose_name = "Тэг"
        verbose_name_plural = "Тэги"


class Article(TimeStampedModel):
    title = models.CharField(max_length=100)
    content = RichTextField()
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    rating = models.FloatField(
        default=0.0,
        validators=(
            MinValueValidator(limit_value=0.0),
            MaxValueValidator(limit_value=5.0),
        ),
    )
    slug = models.SlugField(max_length=150, unique=True)
    is_draft = models.BooleanField(default=False)
    seo_keywords = models.CharField(max_length=255)
    seo_description = models.TextField()
    category = TreeForeignKey(
        "Category",
        blank=False,
        null=False,
        on_delete=models.PROTECT,
        related_name="articles",
    )
    tags = models.ManyToManyField(Tag, related_name="articles")

    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"


class ArticleComment(Comment):
    article = models.ForeignKey(
        Article, related_name="comments", on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = "Комментарий к статье"
        verbose_name_plural = "Комментарии к статье"


class Category(MPTTModel):
    name = models.CharField(max_length=50, unique=True)
    parent = TreeForeignKey(
        "self", on_delete=models.PROTECT, null=True, blank=True, related_name="children"
    )
    slug = models.SlugField()

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
