# Generated by Django 2.1.5 on 2019-02-19 02:24

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_profile_userprofile'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='phone_number',
            new_name='mobile_number',
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='user',
            field=models.ForeignKey(on_delete='models.CASCADE', to=settings.AUTH_USER_MODEL),
        ),
    ]