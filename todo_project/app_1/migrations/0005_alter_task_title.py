# Generated by Django 5.0.4 on 2024-09-13 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app_1", "0004_remove_task_created"),
    ]

    operations = [
        migrations.AlterField(
            model_name="task",
            name="title",
            field=models.CharField(max_length=500),
        ),
    ]
