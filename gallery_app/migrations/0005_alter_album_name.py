# Generated by Django 4.1 on 2022-09-14 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery_app', '0004_alter_photo_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Album'),
        ),
    ]
