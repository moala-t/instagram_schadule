# Generated by Django 4.2 on 2023-04-06 13:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("content", "0003_alter_content_options"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="content",
            options={"ordering": ["-modified"]},
        ),
    ]
