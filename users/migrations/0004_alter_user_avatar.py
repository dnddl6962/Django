# Generated by Django 5.1.4 on 2025-03-18 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0003_rename_profile_photo_user_avatar"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="avatar",
            field=models.URLField(blank=True),
        ),
    ]
