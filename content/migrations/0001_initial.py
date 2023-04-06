# Generated by Django 4.2 on 2023-04-05 22:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Content",
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
                ("name", models.CharField(default="", max_length=300)),
                ("content", models.FileField(default="", upload_to="")),
                ("is_story", models.BooleanField(default=False)),
                ("is_post", models.BooleanField(default=False)),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("modified", models.DateTimeField(auto_now=True)),
            ],
            options={
                "ordering": ["-modified"],
            },
        ),
    ]