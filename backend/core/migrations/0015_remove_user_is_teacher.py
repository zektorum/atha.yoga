# Generated by Django 4.1.4 on 2022-12-17 21:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0014_merge_20221217_2137"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="user",
            name="is_teacher",
        ),
    ]