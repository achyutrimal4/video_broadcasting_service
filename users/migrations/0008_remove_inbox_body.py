# Generated by Django 4.1 on 2022-09-12 07:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_alter_inbox_subject'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inbox',
            name='body',
        ),
    ]
