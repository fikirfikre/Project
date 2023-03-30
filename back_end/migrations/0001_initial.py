# Generated by Django 4.1.7 on 2023-03-28 14:36

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="About",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Achievements",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=255)),
                ("description", models.TextField()),
                ("date", models.DateField(auto_now_add=True)),
            ],
            options={
                "verbose_name_plural": "Achievements",
            },
        ),
        migrations.CreateModel(
            name="Comment",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                ("email", models.EmailField(max_length=254)),
                ("description", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="ContactUs",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("email", models.EmailField(max_length=254)),
                ("suggestion", models.TextField()),
            ],
            options={
                "verbose_name_plural": "ContactUs",
            },
        ),
        migrations.CreateModel(
            name="Institution",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=255)),
                ("description", models.TextField()),
                (
                    "image",
                    models.FileField(
                        upload_to="institution/",
                        validators=[
                            django.core.validators.FileExtensionValidator(
                                ["svg", "jpeg", "png", "jpg"]
                            )
                        ],
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Job",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=255)),
                ("description", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="News",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=255)),
                ("description", models.TextField()),
                (
                    "image",
                    models.FileField(
                        upload_to="news/",
                        validators=[
                            django.core.validators.FileExtensionValidator(
                                ["svg", "jpeg", "png", "jpg"]
                            )
                        ],
                    ),
                ),
                ("date", models.DateField(auto_now_add=True)),
            ],
            options={
                "verbose_name_plural": "News",
            },
        ),
        migrations.CreateModel(
            name="Officials",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                ("title", models.CharField(max_length=255)),
                ("description", models.TextField()),
                ("twitter_links", models.CharField(max_length=255)),
                ("linked_links", models.CharField(max_length=255)),
                ("social_links", models.CharField(max_length=255)),
                (
                    "image",
                    models.FileField(
                        upload_to="officials/",
                        validators=[
                            django.core.validators.FileExtensionValidator(
                                ["svg", "jpeg", "png", "jpg"]
                            )
                        ],
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Officials",
            },
        ),
        migrations.CreateModel(
            name="Resource",
            fields=[
                (
                    "title",
                    models.CharField(max_length=255, primary_key=True, serialize=False),
                ),
                (
                    "image",
                    models.FileField(
                        upload_to="resources/",
                        validators=[
                            django.core.validators.FileExtensionValidator(
                                ["svg", "jpeg", "png", "jpg"]
                            )
                        ],
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Service",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=255)),
                ("description", models.TextField()),
                (
                    "image",
                    models.FileField(
                        upload_to="service/",
                        validators=[
                            django.core.validators.FileExtensionValidator(
                                ["svg", "jpeg", "png", "jpg"]
                            )
                        ],
                    ),
                ),
                ("date", models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name="Replay",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                ("email", models.EmailField(max_length=254)),
                ("description", models.TextField()),
                (
                    "comment",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="back_end.comment",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="comment",
            name="resource",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="back_end.resource"
            ),
        ),
        migrations.CreateModel(
            name="Article",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("article", models.FileField(upload_to="")),
                (
                    "resource",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="back_end.resource",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Applier",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("first_name", models.CharField(max_length=255)),
                ("last_name", models.CharField(max_length=255)),
                ("email", models.EmailField(max_length=254)),
                (
                    "cv",
                    models.FileField(
                        max_length=255,
                        upload_to="cvs/",
                        validators=[
                            django.core.validators.FileExtensionValidator(["pdf"])
                        ],
                    ),
                ),
                ("jobs", models.ManyToManyField(to="back_end.job")),
            ],
        ),
    ]