# Generated by Django 3.1.3 on 2020-11-28 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0002_auto_20201128_1457"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="subdirectory",
            field=models.FilePathField(
                allow_files=False,
                allow_folders=True,
                default="/data/",
                path="/data",
                recursive=True,
            ),
        ),
    ]
