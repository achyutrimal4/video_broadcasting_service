# Generated by Django 4.1 on 2022-09-13 02:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos_app', '0006_livevideo'),
    ]

    operations = [
        migrations.AddField(
            model_name='livevideo',
            name='venue',
            field=models.CharField(blank=True, default='Bayjing FunOlympics Park', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='livevideo',
            name='url',
            field=models.TextField(verbose_name='Live URL'),
        ),
    ]
