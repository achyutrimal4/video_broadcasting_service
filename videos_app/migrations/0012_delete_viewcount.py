# Generated by Django 4.1 on 2022-08-20 12:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('videos_app', '0011_viewcount'),
    ]

    operations = [
        migrations.DeleteModel(
            name='viewCount',
        ),
    ]
