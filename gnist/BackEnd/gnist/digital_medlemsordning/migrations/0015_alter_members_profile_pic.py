# Generated by Django 5.0.1 on 2024-03-08 18:45

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("digital_medlemsordning", "0014_alter_members_profile_pic"),
    ]

    operations = [
        migrations.AlterField(
            model_name="members",
            name="profile_pic",
            field=models.ImageField(
                default="profile_pics/default_profile_picture.png",
                null=True,
                upload_to="profile_pics",
            ),
        ),
    ]
