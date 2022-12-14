# Generated by Django 4.1 on 2022-09-13 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos_app', '0017_remove_news_author_alter_news_image_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='author',
            field=models.CharField(blank=True, default='Funolympics Admin', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='news',
            name='photo_caption',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='news',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/news/'),
        ),
        migrations.AlterField(
            model_name='news',
            name='title',
            field=models.CharField(max_length=255),
        ),
    ]
