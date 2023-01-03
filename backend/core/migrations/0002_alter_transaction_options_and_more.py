# Generated by Django 4.1.4 on 2022-12-26 08:14
from typing import Any

import django.db.models.deletion
from django.db import migrations, models


def forwards_func(apps: Any, schema_editor: Any) -> None:
    MyModel = apps.get_model('core', 'Transaction')
    ContentType = apps.get_model('contenttypes', 'ContentType')

    new_ct = ContentType.objects.get_for_model(MyModel)
    MyModel.objects.filter(polymorphic_ctype__isnull=True).update(polymorphic_ctype=new_ct)


class Migration(migrations.Migration):

    dependencies = [
        ("contenttypes", "0002_remove_content_type_name"),
        ("core", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="transaction",
            options={"base_manager_name": "objects"},
        ),
        migrations.AddField(
            model_name="transaction",
            name="polymorphic_ctype",
            field=models.ForeignKey(
                editable=False,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="polymorphic_%(app_label)s.%(class)s_set+",
                to="contenttypes.contenttype",
            ),
        ),
        migrations.RunPython(forwards_func, migrations.RunPython.noop),
    ]