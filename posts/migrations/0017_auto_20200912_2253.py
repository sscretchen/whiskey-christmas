# Generated by Django 3.1.1 on 2020-09-13 02:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0016_remove_comment_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='publishing_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
