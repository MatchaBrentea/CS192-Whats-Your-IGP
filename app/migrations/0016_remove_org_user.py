# Generated by Django 2.1.7 on 2019-03-06 13:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_auto_20190306_1340'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='org',
            name='user',
        ),
    ]