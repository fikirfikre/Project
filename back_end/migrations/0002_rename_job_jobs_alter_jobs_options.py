# Generated by Django 4.1.7 on 2023-03-29 10:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("back_end", "0001_initial"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Job",
            new_name="Jobs",
        ),
        migrations.AlterModelOptions(
            name="jobs",
            options={"verbose_name_plural": "Jobs"},
        ),
    ]
