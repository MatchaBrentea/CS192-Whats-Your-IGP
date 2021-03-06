# Generated by Django 2.0.3 on 2019-04-04 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0020_org_mobile_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orgmember',
            name='org',
        ),
        migrations.RemoveField(
            model_name='orgmember',
            name='user',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='user',
        ),
        migrations.AddField(
            model_name='igp',
            name='image',
            field=models.ImageField(blank=True, upload_to='images'),
        ),
        migrations.AddField(
            model_name='igp',
            name='view',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='OrgMember',
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]
