# Generated by Django 4.1 on 2022-08-21 10:29

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('videos_app', '0012_delete_viewcount'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='vote_ratio',
        ),
        migrations.RemoveField(
            model_name='video',
            name='vote_total',
        ),
        migrations.AddField(
            model_name='video',
            name='video_views',
            field=models.ManyToManyField(related_name='video_views', to=settings.AUTH_USER_MODEL),
        ),
    ]
