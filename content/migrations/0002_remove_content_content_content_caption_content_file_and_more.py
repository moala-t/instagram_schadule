# Generated by Django 4.2 on 2023-04-06 11:34

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("content", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="content",
            name="content",
        ),
        migrations.AddField(
            model_name="content",
            name="caption",
            field=models.TextField(default="this is caption"),
        ),
        migrations.AddField(
            model_name="content",
            name="file",
            field=models.FileField(null=True, upload_to="media"),
        ),
        migrations.AddField(
            model_name="content",
            name="is_reel",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="content",
            name="schadule",
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name="content",
            name="name",
            field=models.CharField(blank=True, default="", max_length=300),
        ),
    ]