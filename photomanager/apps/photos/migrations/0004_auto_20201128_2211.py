# Generated by Django 3.1.3 on 2020-11-28 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("photos", "0003_auto_20201128_2210"),
    ]

    operations = [
        migrations.AlterField(
            model_name="photo",
            name="file",
            field=models.FilePathField(
                allow_folders=True, help_text="Path to the photo file.", path="/data"
            ),
        ),
    ]
