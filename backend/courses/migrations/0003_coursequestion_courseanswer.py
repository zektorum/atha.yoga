# Generated by Django 4.1.5 on 2023-01-27 17:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("courses", "0002_alter_ticket_course_lessonenrolleduser_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="CourseQuestion",
            fields=[
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Дата и время создания"
                    ),
                ),
                (
                    "updated_at",
                    models.DateTimeField(
                        auto_now=True, verbose_name="Дата и время изменения"
                    ),
                ),
                ("title", models.CharField(max_length=120, verbose_name="Заголовок")),
                ("text", models.TextField(verbose_name="Текст")),
                (
                    "author",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Автор",
                    ),
                ),
                (
                    "course",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="questions",
                        to="courses.basecourse",
                        verbose_name="Курс",
                    ),
                ),
            ],
            options={
                "verbose_name": "Вопрос по курсу",
                "verbose_name_plural": "Вопросы по курсу",
            },
        ),
        migrations.CreateModel(
            name="CourseAnswer",
            fields=[
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Дата и время создания"
                    ),
                ),
                (
                    "updated_at",
                    models.DateTimeField(
                        auto_now=True, verbose_name="Дата и время изменения"
                    ),
                ),
                ("text", models.TextField(verbose_name="Текст")),
                (
                    "author",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Автор",
                    ),
                ),
                (
                    "question",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="answers",
                        to="courses.coursequestion",
                        verbose_name="Вопрос",
                    ),
                ),
            ],
            options={
                "verbose_name": "Ответ на вопрос к курсу",
                "verbose_name_plural": "Ответы на вопрос к курсу",
            },
        ),
    ]
