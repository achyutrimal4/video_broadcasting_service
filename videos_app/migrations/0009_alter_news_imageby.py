# Generated by Django 4.1 on 2022-09-13 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos_app', '0008_alter_news_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='imageBy',
            field=models.CharField(default='Funolympics Admin', max_length=200, verbose_name='Image By'),
        ),
    ]