# Generated by Django 2.1.4 on 2018-12-06 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20181206_1716'),
    ]

    operations = [
        migrations.AddField(
            model_name='igp',
            name='itype',
            field=models.CharField(default='merch', max_length=100),
            preserve_default=False,
        ),
    ]
