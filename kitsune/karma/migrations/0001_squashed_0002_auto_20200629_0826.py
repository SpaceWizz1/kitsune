# Generated by Django 4.1.7 on 2023-04-18 13:42

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    replaces = [("karma", "0001_initial"), ("karma", "0002_auto_20200629_0826")]

    initial = True

    dependencies = [
        ("auth", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Title",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
                    ),
                ),
                ("name", models.CharField(max_length=100, unique=True)),
                ("is_auto", models.BooleanField(default=False)),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True, help_text="Assign this title to these groups.", to="auth.group"
                    ),
                ),
                (
                    "users",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Assign this title to these users.",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]