# Generated by Django 4.1 on 2022-08-28 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos_app', '0016_remove_review_value_review_comment_by_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='created',
        ),
        migrations.AlterField(
            model_name='review',
            name='comment',
            field=models.TextField(null=True),
        ),
    ]