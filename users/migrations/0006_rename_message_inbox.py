# Generated by Django 4.1 on 2022-09-11 13:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_message'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Message',
            new_name='Inbox',
        ),
    ]
