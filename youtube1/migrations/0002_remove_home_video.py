# Generated by Django 4.0.1 on 2022-06-02 04:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('youtube1', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='home',
            name='video',
        ),
    ]
