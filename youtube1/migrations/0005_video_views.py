# Generated by Django 4.0.1 on 2022-06-02 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('youtube1', '0004_rename_home_video'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='views',
            field=models.IntegerField(default=0),
        ),
    ]
