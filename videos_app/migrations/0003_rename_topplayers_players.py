# Generated by Django 4.1 on 2022-09-10 12:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('videos_app', '0002_topplayers'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='TopPlayers',
            new_name='Players',
        ),
    ]
